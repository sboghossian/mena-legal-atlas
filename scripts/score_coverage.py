#!/usr/bin/env python3
"""Coverage scoring layer for the MENA Legal Atlas.

Turns the source map into a "where can legal AI actually operate" decision tool.
Five axes per jurisdiction:

  corpus_depth   0-5   how many of the 5 source categories exist (local, from atlas)
  reachability   0-100 % of worldwidelaw sources that actually produce data (local)
  recency        Linkup, constrained to the jurisdiction's OFFICIAL domains:
                 has a major national law been enacted/amended in 2025-26?
  language       OpenRouter (cheap): arabic_native / bilingual / english_available / ...
  codifiability  OpenRouter (cheap): Ambiguity-Index lens, 1-5  [INTERNAL ONLY]

corpus_depth + reachability reuse build_map.py's exact definitions so the scores
stay consistent with the published two-panel map.

Outputs:
  data/coverage-scores.json           PUBLIC  (no codifiability)
  data/coverage-scores-internal.json  INTERNAL (adds codifiability)

Every recency claim carries its Linkup source URLs — never fabricated.
Responses are cached under viz/cache/coverage/<CC>.json (idempotent; --refresh busts).

Usage:
  python3 scripts/score_coverage.py            # all 25, using cache
  python3 scripts/score_coverage.py --limit 3  # first 3 (smoke test)
  python3 scripts/score_coverage.py --refresh  # ignore cache, re-call APIs
"""
import argparse
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
ATLAS_JSON = ROOT / "phase-1-atlas" / "mena-legal-atlas.json"
DATA = ROOT / "data"
CACHE = ROOT / "viz" / "cache" / "coverage"

# ICP markets lead the narrative (highlighted first in the map / post).
ICP = ["AE", "SA", "EG", "JO", "LB"]

LINKUP_URL = "https://api.linkup.so/v1/search"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


# ---------- env ----------
def load_env():
    """Load .env.local from atlas root (gitignored) into os.environ."""
    envf = ROOT / ".env.local"
    if envf.exists():
        for line in envf.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


# ---------- local axes (reuse build_map.py definitions) ----------
def corpus_depth(e):
    a = e.get("authorities", {}) or {}
    return sum([
        bool(a.get("official_gazette")),
        bool(a.get("consolidated")),
        bool(a.get("apex_courts")),
        bool(a.get("key_regulators")) or bool(e.get("additional_sources")),
        any(x.get("law_key") == "constitution" for x in (e.get("key_legislation") or [])),
    ])


def reachability(e):
    wl = e.get("worldwidelaw_reconciled", {}) or {}
    work, blok = wl.get("working", 0), wl.get("blocked", 0)
    pct = round(100 * work / max(work + blok, 1))
    return {"working": work, "blocked": blok, "pct": pct,
            "tier": "hi" if work >= 4 else ("mid" if work >= 1 else "lo")}


def official_domains(e, cap=12):
    """Official source domains for Linkup includeDomains (trust filter)."""
    doms = []
    a = e.get("authorities", {}) or {}
    og = a.get("official_gazette") or {}
    for u in [og.get("url")] + [c.get("url") for c in (a.get("consolidated") or [])]:
        if u:
            d = urllib.parse.urlparse(u).netloc.replace("www.", "").lower()
            if d:
                doms.append(d)
    for s in (e.get("additional_sources") or []):
        if s.get("domain"):
            doms.append(s["domain"].lower())
    for k in (e.get("key_legislation") or []):
        if k.get("source_domain"):
            doms.append(k["source_domain"].lower())
    # dedupe, drop generic aggregators that aren't jurisdiction-official
    drop = {"constituteproject.org", "wipo.int", "loc.gov", "refworld.org"}
    seen, out = set(), []
    for d in doms:
        if d and d not in seen and d not in drop:
            seen.add(d)
            out.append(d)
    return out[:cap]


# ---------- API calls ----------
def http_post(url, payload, headers, timeout=90):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), method="POST",
        headers={"Content-Type": "application/json", **headers})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def linkup_recency(country, domains):
    """Constrained Linkup search: any major 2025-26 reform? Returns answer + source URLs."""
    key = os.environ["LINKUP_API_KEY"]
    q = (f"Has {country} enacted or substantially amended any major national law "
         f"(civil code, commercial/companies law, labor law, penal code, or data-protection law) "
         f"in 2025 or 2026? Name the law and date if so.")
    payload = {"q": q, "depth": "standard", "outputType": "sourcedAnswer"}
    if domains:
        payload["includeDomains"] = domains
    try:
        d = http_post(LINKUP_URL, payload, {"Authorization": f"Bearer {key}"})
    except urllib.error.HTTPError as ex:
        # retry once unconstrained if domain filter returns nothing usable
        if domains:
            payload.pop("includeDomains", None)
            d = http_post(LINKUP_URL, payload, {"Authorization": f"Bearer {key}"})
            d["_unconstrained_fallback"] = True
        else:
            raise
    return {
        "answer": d.get("answer", ""),
        "sources": [s.get("url") for s in (d.get("sources") or []) if s.get("url")][:6],
        "constrained": not d.get("_unconstrained_fallback", False),
    }


def openrouter_json(prompt, model_env="OPENROUTER_MODEL_CHEAP"):
    key = os.environ["OPENROUTER_API_KEY"]
    model = os.environ.get(model_env, "google/gemini-2.5-flash")
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a precise legal-data analyst. "
             "Respond with a single valid JSON object and nothing else."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.1,
        "response_format": {"type": "json_object"},
    }
    d = http_post(OPENROUTER_URL, payload, {
        "Authorization": f"Bearer {key}",
        "HTTP-Referer": "https://github.com/sboghossian/mena-legal-atlas",
        "X-Title": "MENA Legal Atlas coverage scoring",
    })
    txt = d["choices"][0]["message"]["content"]
    try:
        return json.loads(txt)
    except json.JSONDecodeError:
        a, b = txt.find("{"), txt.rfind("}")
        return json.loads(txt[a:b + 1])


def classify(entry, recency_blob):
    """One cheap OpenRouter call: language regime + codifiability + recency interpretation."""
    ctx = {
        "country": entry.get("country"),
        "legal_system": entry.get("legal_system"),
        "languages": entry.get("languages"),
        "citation_style": entry.get("citation_style"),
        "calendar": entry.get("calendar"),
        "linkup_recency_answer": recency_blob["answer"],
        "linkup_sources": recency_blob["sources"],
    }
    prompt = (
        "Given this jurisdiction context, return JSON with exactly these keys:\n"
        '  "language_regime": one of '
        '["arabic_native","bilingual_ar_en","bilingual_ar_fr","english_available",'
        '"french_influenced","hebrew_native","persian_native","turkish_native","other"]\n'
        '  "language_note": <=20 words on how legal text is actually published\n'
        '  "codifiability": {"score": 1-5 (1=mostly judgment-bound, 5=highly codified/deterministic), '
        '"rationale": <=25 words}\n'
        '  "recency": {"recent_major_reform": "yes"|"no"|"unclear", '
        '"laws": [short names], "grounded_in_sources": true|false}\n'
        "Base recent_major_reform ONLY on the provided linkup answer/sources; "
        "if they do not clearly support a 2025-26 reform, say \"unclear\" and grounded_in_sources=false.\n\n"
        f"CONTEXT:\n{json.dumps(ctx, ensure_ascii=False)}"
    )
    return openrouter_json(prompt)


# ---------- driver ----------
def score_one(cc, e, refresh):
    cache_f = CACHE / f"{cc}.json"
    if cache_f.exists() and not refresh:
        return json.loads(cache_f.read_text())

    doms = official_domains(e)
    rec = linkup_recency(e.get("country", cc), doms)
    cls = classify(e, rec)
    reach = reachability(e)

    row = {
        "cc": cc,
        "country": e.get("country", cc),
        "region": e.get("region"),
        "is_icp": cc in ICP,
        "corpus_depth": corpus_depth(e),          # 0-5
        "reachability": reach,                     # {pct, tier, working, blocked}
        "language_regime": cls.get("language_regime"),
        "language_note": cls.get("language_note"),
        "recency": {                               # grounded in Linkup sources
            **cls.get("recency", {}),
            "linkup_answer": rec["answer"][:600],
            "sources": rec["sources"],
            "domain_constrained": rec["constrained"],
        },
        "_internal": {"codifiability": cls.get("codifiability")},  # stripped from public file
    }
    cache_f.write_text(json.dumps(row, ensure_ascii=False, indent=2))
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="score only first N jurisdictions")
    ap.add_argument("--refresh", action="store_true", help="ignore cache, re-call APIs")
    args = ap.parse_args()

    load_env()
    for need in ("LINKUP_API_KEY", "OPENROUTER_API_KEY"):
        if not os.environ.get(need):
            sys.exit(f"missing {need} in atlas/.env.local")

    CACHE.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(exist_ok=True)
    atlas = json.load(open(ATLAS_JSON))
    items = list(atlas.items())
    if args.limit:
        items = items[:args.limit]

    rows = []
    for i, (cc, e) in enumerate(items, 1):
        try:
            row = score_one(cc, e, args.refresh)
            rows.append(row)
            r = row["recency"]
            print(f"[{i:2d}/{len(items)}] {cc} {row['country'][:22]:22s} "
                  f"depth={row['corpus_depth']} reach={row['reachability']['pct']:3d}% "
                  f"lang={row['language_regime']:16s} reform={r.get('recent_major_reform')} "
                  f"cod={row['_internal']['codifiability'].get('score')}")
        except Exception as ex:  # noqa: BLE001 — one bad jurisdiction shouldn't kill the run
            print(f"[{i:2d}/{len(items)}] {cc} FAILED: {ex}", file=sys.stderr)
        time.sleep(0.3)  # be polite to both APIs

    # public file: strip _internal
    public = []
    for r in rows:
        pr = {k: v for k, v in r.items() if k != "_internal"}
        public.append(pr)
    (DATA / "coverage-scores.json").write_text(json.dumps(public, ensure_ascii=False, indent=2))
    (DATA / "coverage-scores-internal.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    print(f"\nwrote data/coverage-scores.json ({len(public)} public rows, no codifiability)")
    print(f"wrote data/coverage-scores-internal.json ({len(rows)} rows, +codifiability)")


if __name__ == "__main__":
    main()
