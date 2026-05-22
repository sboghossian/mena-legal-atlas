#!/usr/bin/env python3
"""
discover_deep.py — go wide with Linkup where it's validated to work.

Two passes:
  A. SECTORAL source discovery — central bank, capital-markets, tax, data-protection,
     competition, IP, labour, company-registrar — the official regulators the atlas's
     gazette/court-centric map misses. Output schema matches source-discovery.yaml so
     filter_sources.py can clean it.
  B. CONSTITUTIONS layer — constrained to authoritative aggregators (Constitute Project,
     WIPO Lex) which ARE crawlable, unlike national portals. Output schema matches
     verified-laws.yaml so merge_laws.py can merge it.

Usage: python3 scripts/discover_deep.py            # all 25
       python3 scripts/discover_deep.py LB SA       # subset
"""
import json, os, re, sys, time, datetime, urllib.request, urllib.parse, pathlib

KEY = os.environ.get("LINKUP_KEY", "")
URL = "https://api.linkup.so/v1/search"
ROOT = pathlib.Path(__file__).resolve().parent.parent
ATLAS = ROOT / "phase-1-atlas" / "atlas.yaml"
OUTDIR = ROOT / "phase-2-enrichment"

SECTORAL = [
    "{c} central bank official website",
    "{c} capital markets authority or securities commission official website",
    "{c} tax authority official website",
    "{c} personal data protection authority official website",
    "{c} competition authority official website",
    "{c} intellectual property office official website",
    "{c} ministry of labour official website",
    "{c} commercial registry or companies registrar official",
]
AGG_DOMAINS = ["constituteproject.org", "wipo.int"]
DOMAIN_RE = re.compile(r"(?:https?://)?(?:www\.)?([a-z0-9.\-]+\.[a-z]{2,})", re.I)
OFFICIAL_HINTS = ("moj", "court", "justice", "parliament", "majlis", "gazette",
                  "legislation", "mahkam", "supreme", "cassation", "diwan", "bank",
                  "tax", "zatca", "customs", "securities", "capitalmarket", "cma",
                  "competition", "ipo", "trademark", "patent", "labour", "labor",
                  "registry", "registrar", "authority", "presidency", "boe", "knesset")
AGGREGATORS = ("faolex.fao.org", "wipo.int", "constituteproject.org", "refworld.org",
               "loc.gov", "muqtafi.birzeit.edu")
SECONDARY = ("wikipedia", "wikisource", "blog", "linkedin", "facebook", "scribd",
             "lexology", "mondaq", "lawfirm", "reuters", "aljazeera", "researchgate",
             "academia.edu", "jstor", "ssrn", "twitter", "x.com", "bloomberg")

def load_atlas():
    import yaml
    return yaml.safe_load(ATLAS.read_text())

def collect(node, out):
    if isinstance(node, dict):
        for v in node.values(): collect(v, out)
    elif isinstance(node, list):
        for v in node: collect(v, out)
    elif isinstance(node, str): out.append(node)

def known_domains(jb):
    s = []; collect(jb, s)
    return {m.lower().strip(".") for x in s for m in DOMAIN_RE.findall(x)}

def search(q, include=None, depth="standard"):
    p = {"q": q, "depth": depth, "outputType": "searchResults"}
    if include: p["includeDomains"] = include
    req = urllib.request.Request(URL, data=json.dumps(p).encode(), method="POST",
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())

def dom(u):
    try: return urllib.parse.urlparse(u).netloc.replace("www.", "").lower()
    except: return ""

def classify(d):
    if any(s in d for s in SECONDARY): return None
    if any(a in d for a in AGGREGATORS): return "aggregator"
    if ".gov" in d or any(h in d for h in OFFICIAL_HINTS): return "official"
    return None

def main():
    import yaml
    if not KEY: sys.exit("set LINKUP_KEY env var")
    atlas = load_atlas()
    targets = [a.upper() for a in sys.argv[1:]] or list(atlas.keys())
    OUTDIR.mkdir(exist_ok=True)
    src_out, const_out = [], {}

    for cc in targets:
        if cc not in atlas: print(f"skip {cc}"); continue
        jb = atlas[cc]; country = jb.get("country", cc); known = known_domains(jb)
        print(f"\n{'='*64}\n{cc} — {country}\n{'='*64}")

        # Pass A: sectoral source discovery
        found = {}
        for tmpl in SECTORAL:
            try: res = search(tmpl.format(c=country))
            except Exception as e: print(f"  err {e}"); continue
            for r in res.get("results", [])[:6]:
                d = dom(r.get("url", ""));
                if not d: continue
                cls = classify(d)
                if not cls or d in known: continue
                if any(d.endswith(k) or k.endswith(d) for k in known): continue
                found.setdefault(d, {"domain": d, "kind": cls, "example_url": r.get("url",""),
                                     "name": r.get("name","")[:90], "found_by": tmpl.format(c=country)})
            time.sleep(0.25)
        if found:
            src_out.append({"cc": cc, "country": country, "new_sources": list(found.values())})
            print(f"  sectoral: +{len(found)} candidate domains")

        # Pass B: constitution via aggregators
        try:
            res = search(f"{country} constitution full text", AGG_DOMAINS, "standard")
            best = None
            for r in res.get("results", []):
                d = dom(r.get("url", "")); nm = (r.get("name","") or "").lower()
                if any(a in d for a in AGG_DOMAINS) and ("constitut" in nm or "basic law" in nm or country.lower() in nm):
                    best = r; break
            if best:
                const_out[cc] = [{
                    "law_key": "constitution", "law_name": f"Constitution of {country}",
                    "title": best.get("name","")[:120], "official_url": best.get("url",""),
                    "source_domain": dom(best.get("url","")),
                    "discovered_via": "linkup_aggregator",
                    "verified_by": "linkup_aggregator (spot-check before relying)",
                    "verified_at": datetime.date.today().isoformat(),
                    "note": "Authoritative aggregator (Constitute Project / WIPO Lex).",
                }]
                print(f"  constitution: {dom(best.get('url',''))}")
        except Exception as e:
            print(f"  const err {e}")
        time.sleep(0.25)

    (OUTDIR / "source-discovery-deep.yaml").write_text(
        yaml.safe_dump({"jurisdictions": src_out}, allow_unicode=True, sort_keys=False))
    (OUTDIR / "verified-laws-aggregator.yaml").write_text(
        yaml.safe_dump(const_out, allow_unicode=True, sort_keys=False))
    tot = sum(len(x["new_sources"]) for x in src_out)
    print(f"\n{'#'*64}\nDEEP SWEEP: +{tot} sectoral source candidates, "
          f"{len(const_out)} constitutions\nstaged in {OUTDIR}\n{'#'*64}")

if __name__ == "__main__":
    main()
