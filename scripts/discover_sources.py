#!/usr/bin/env python3
"""
discover_sources.py — Linkup in its working lane: find OFFICIAL legal-source
domains the atlas is missing.

Unlike enrich_laws (document-level, structurally capped), source-discovery only
needs domain-level precision, which Linkup does well. For each jurisdiction it
runs a few discovery queries, keeps only official (.gov / ministry / court) or
authoritative-aggregator domains, and diffs against what the atlas already lists.
Output is STAGED (phase-2-enrichment/source-discovery.yaml), never auto-merged.

Usage:
  python3 scripts/discover_sources.py              # all 25
  python3 scripts/discover_sources.py LB SA AE     # subset
"""
import json, os, re, sys, time, urllib.request, urllib.parse, pathlib, datetime

KEY = os.environ.get("LINKUP_KEY", "")
URL = "https://api.linkup.so/v1/search"
ROOT = pathlib.Path(__file__).resolve().parent.parent
ATLAS = ROOT / "phase-1-atlas" / "atlas.yaml"
OUTDIR = ROOT / "phase-2-enrichment"

QUERIES = [
    "{c} official gazette website",
    "{c} consolidated legislation portal government",
    "{c} supreme court or court of cassation official website",
    "{c} ministry of justice legislation database official",
]
DOMAIN_RE = re.compile(r"(?:https?://)?(?:www\.)?([a-z0-9.\-]+\.[a-z]{2,})", re.I)
OFFICIAL_HINTS = ("moj", "court", "justice", "parliament", "majlis", "gazette",
                  "legislation", "mahkam", "supreme", "cassation", "diwan",
                  "presidency", "boe", "uqn", "knesset", "elaws", "tashri",
                  "qanon", "qanoon", "legalaffairs", "dustur")
AGGREGATORS = ("faolex.fao.org", "wipo.int", "constituteproject.org",
               "refworld.org", "loc.gov", "muqtafi.birzeit.edu", "ilo.org")
SECONDARY = ("wikipedia", "wikisource", "blog", "linkedin", "facebook", "scribd",
             "lexology", "mondaq", "lawfirm", "news", "reuters", "aljazeera",
             "researchgate", "academia.edu", "jstor", "ssrn", "twitter", "x.com")

def load_atlas():
    import yaml
    return yaml.safe_load(ATLAS.read_text())

def collect_strings(node, out):
    if isinstance(node, dict):
        for v in node.values(): collect_strings(v, out)
    elif isinstance(node, list):
        for v in node: collect_strings(v, out)
    elif isinstance(node, str):
        out.append(node)

def known_domains(jblock):
    s = []; collect_strings(jblock, s)
    doms = set()
    for x in s:
        for m in DOMAIN_RE.findall(x):
            doms.add(m.lower().strip("."))
    return doms

def search(q):
    body = json.dumps({"q": q, "depth": "standard", "outputType": "searchResults"}).encode()
    req = urllib.request.Request(URL, data=body, method="POST",
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode())

def dom(u):
    try: return urllib.parse.urlparse(u).netloc.replace("www.", "").lower()
    except: return ""

def classify(d):
    if any(s in d for s in SECONDARY): return None
    if d in AGGREGATORS or any(a in d for a in AGGREGATORS): return "aggregator"
    if ".gov" in d or any(h in d for h in OFFICIAL_HINTS): return "official"
    return None

def discover(cc, jblock):
    country = jblock.get("country", cc)
    known = known_domains(jblock)
    print(f"\n{'='*70}\n{cc} — {country}  (knows {len(known)} domains)\n{'='*70}")
    found = {}
    for tmpl in QUERIES:
        q = tmpl.format(c=country)
        try:
            res = search(q)
        except Exception as e:
            print(f"  ERROR {e}"); continue
        for r in res.get("results", [])[:8]:
            u = r.get("url", ""); d = dom(u)
            if not d: continue
            cls = classify(d)
            if not cls: continue
            if d in known or any(d.endswith(k) or k.endswith(d) for k in known): continue
            if d not in found:
                found[d] = {"domain": d, "kind": cls, "example_url": u,
                            "name": r.get("name", "")[:90], "found_by": q}
        time.sleep(0.3)
    new = list(found.values())
    for f in new:
        print(f"  + [{f['kind']:<10}] {f['domain']:<32} {f['name'][:40]}")
    if not new: print("  (no new official domains)")
    return {"cc": cc, "country": country, "known_count": len(known),
            "new_sources": new, "discovered_at": datetime.date.today().isoformat()}

def main():
    import yaml
    if not KEY: sys.exit("set LINKUP_KEY env var")
    atlas = load_atlas()
    args = [a.upper() for a in sys.argv[1:]] or list(atlas.keys())
    OUTDIR.mkdir(exist_ok=True)
    out = []
    for cc in args:
        if cc not in atlas: print(f"skip {cc}"); continue
        out.append(discover(cc, atlas[cc]))
    (OUTDIR / "source-discovery.yaml").write_text(
        yaml.safe_dump({"jurisdictions": out}, allow_unicode=True, sort_keys=False))
    print(f"\n\n{'#'*70}\nSUMMARY — new official-source candidates per jurisdiction\n{'#'*70}")
    tot = 0
    for o in out:
        n = len(o["new_sources"]); tot += n
        if n: print(f"  {o['cc']}  +{n}  ({o['country']})")
    print(f"  TOTAL new candidate domains: {tot}   staged in {OUTDIR}/source-discovery.yaml")

if __name__ == "__main__":
    main()
