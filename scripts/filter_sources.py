#!/usr/bin/env python3
"""
filter_sources.py — clean the raw source-discovery output (zero API credits).

Drops the noise the .gov heuristic let through:
  - US federal domains (congress.gov, justice.gov, state.gov, *.gov w/o ccTLD)
  - wrong-country domains (e.g. .ss/.et under Sudan, .bh under Kuwait)
  - commercial / news "gazette" sites (*.com, *.co.uk, com.<cc>)
Keeps:
  - national official domains ending in the jurisdiction's ccTLD (.gov.<cc> or
    a non-commercial second level)
  - a curated allowlist of authoritative cross-border aggregators

Reads  phase-2-enrichment/source-discovery.yaml
Writes phase-2-enrichment/source-discovery.clean.yaml  (kept, merge-candidate)
       phase-2-enrichment/source-discovery.dropped.yaml (audit trail)

Usage: python3 scripts/filter_sources.py
"""
import pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "phase-2-enrichment"
SRC = OUTDIR / "source-discovery.yaml"

CCTLD = {
    "AE": "ae", "BH": "bh", "KW": "kw", "OM": "om", "QA": "qa", "SA": "sa",
    "EG": "eg", "IQ": "iq", "JO": "jo", "LB": "lb", "PS": "ps", "SY": "sy",
    "DZ": "dz", "LY": "ly", "MA": "ma", "MR": "mr", "TN": "tn", "YE": "ye",
    "SD": "sd", "SO": "so", "DJ": "dj", "KM": "km", "IR": "ir", "IL": "il",
    "TR": "tr",
}
GOOD_AGGREGATORS = ("guides.loc.gov", "loc.gov", "wipo.int", "constituteproject.org",
                    "refworld.org", "faolex.fao.org", "muqtafi.birzeit.edu")
COMMERCIAL_2ND = {"com", "net", "co", "org", "edu"}

def decide(domain, cc):
    """Return (keep: bool, bucket_or_reason: str)."""
    d = domain.lower().strip(".")
    if any(d == a or d.endswith("." + a) or d == a for a in GOOD_AGGREGATORS):
        return True, "aggregator"
    labels = d.split(".")
    tld = labels[-1]
    cctld = CCTLD.get(cc, "")
    if tld == "gov":                       # US federal (.gov with no country code)
        return False, "us-gov"
    if tld == "us":
        return False, "us-noise"
    if tld == cctld:                       # ends in this jurisdiction's ccTLD
        if len(labels) >= 2 and labels[-2] in COMMERCIAL_2ND:
            return False, f"commercial-under-cc(.{labels[-2]}.{tld})"
        if ".gov." in d or d.startswith("gov.") or "gov" in labels:
            return True, "national-gov"
        return True, "national"            # e.g. coursupreme.dz
    return False, f"wrong-or-foreign(.{tld})"

def main():
    data = yaml.safe_load(SRC.read_text())
    kept, dropped = [], []
    for j in data.get("jurisdictions", []):
        cc = j["cc"]
        k_list, d_list = [], []
        for s in j.get("new_sources", []):
            keep, why = decide(s["domain"], cc)
            row = {**s, "verdict": why}
            (k_list if keep else d_list).append(row)
        if k_list:
            kept.append({"cc": cc, "country": j["country"], "sources": k_list})
        if d_list:
            dropped.append({"cc": cc, "country": j["country"], "sources": d_list})

    (OUTDIR / "source-discovery.clean.yaml").write_text(
        yaml.safe_dump({"jurisdictions": kept}, allow_unicode=True, sort_keys=False))
    (OUTDIR / "source-discovery.dropped.yaml").write_text(
        yaml.safe_dump({"jurisdictions": dropped}, allow_unicode=True, sort_keys=False))

    tk = sum(len(x["sources"]) for x in kept)
    td = sum(len(x["sources"]) for x in dropped)
    print(f"{'='*64}\nFILTER RESULT\n{'='*64}")
    for x in kept:
        doms = ", ".join(s["domain"] for s in x["sources"])
        print(f"  {x['cc']}  +{len(x['sources']):>2}  {doms}")
    # drop-reason tally
    tally = {}
    for x in dropped:
        for s in x["sources"]:
            r = s["verdict"].split("(")[0]
            tally[r] = tally.get(r, 0) + 1
    print(f"\nKEPT {tk}  |  DROPPED {td}")
    print("dropped by reason:", ", ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    print(f"clean -> {OUTDIR}/source-discovery.clean.yaml")

if __name__ == "__main__":
    main()
