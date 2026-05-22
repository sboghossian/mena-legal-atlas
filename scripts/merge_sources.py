#!/usr/bin/env python3
"""
merge_sources.py — merge filtered source candidates into the canonical atlas.

Reads a *.clean.yaml produced by filter_sources.py and appends each kept domain
under the jurisdiction's `additional_sources:` list in atlas.yaml. Idempotent
(dedupes by domain). Provenance preserved so canonical stays auditable.

Usage:
  python3 scripts/merge_sources.py [clean.yaml]            # dry-run
  python3 scripts/merge_sources.py [clean.yaml] --apply    # write atlas.yaml
"""
import sys, datetime, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
ATLAS = ROOT / "phase-1-atlas" / "atlas.yaml"

def main():
    apply = "--apply" in sys.argv
    paths = [a for a in sys.argv[1:] if not a.startswith("-")]
    src = pathlib.Path(paths[0]) if paths else ROOT / "phase-2-enrichment" / "source-discovery.clean.yaml"
    atlas = yaml.safe_load(ATLAS.read_text())
    data = yaml.safe_load(src.read_text()) or {}
    added = 0
    for j in data.get("jurisdictions", []):
        cc = j["cc"]
        if cc not in atlas:
            print(f"skip {cc}"); continue
        lst = atlas[cc].setdefault("additional_sources", [])
        have = {e.get("domain") for e in lst}
        # also dedupe against domains already anywhere in the jurisdiction block
        blob = yaml.safe_dump(atlas[cc], allow_unicode=True)
        for s in j.get("sources", []):
            d = s["domain"]
            if d in have or d in blob:
                continue
            lst.append({
                "domain": d, "kind": s.get("verdict", s.get("kind", "")),
                "url": s.get("example_url", ""), "name": s.get("name", ""),
                "discovered_via": "linkup", "added_at": datetime.date.today().isoformat(),
            })
            have.add(d); added += 1
            print(f"  + {cc}/{d}")
    print(f"\n{added} sources to add. {'WRITING' if apply else 'DRY-RUN (use --apply)'}")
    if apply and added:
        ATLAS.write_text(yaml.safe_dump(atlas, allow_unicode=True, sort_keys=False))
        print(f"wrote {ATLAS}")

if __name__ == "__main__":
    main()
