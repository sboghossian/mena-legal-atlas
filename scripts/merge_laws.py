#!/usr/bin/env python3
"""
merge_laws.py — merge HUMAN-VERIFIED laws into the canonical atlas.

Reads phase-2-enrichment/verified-laws.yaml and injects each entry under the
matching jurisdiction's `key_legislation:` list in phase-1-atlas/atlas.yaml.
Idempotent (dedupes by law_key). Only verified entries ever reach canonical.

Usage:
  python3 scripts/merge_laws.py            # dry-run (prints plan)
  python3 scripts/merge_laws.py --apply    # write atlas.yaml
"""
import sys, pathlib, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
ATLAS = ROOT / "phase-1-atlas" / "atlas.yaml"
VERIFIED = ROOT / "phase-2-enrichment" / "verified-laws.yaml"

def main():
    apply = "--apply" in sys.argv
    atlas = yaml.safe_load(ATLAS.read_text())
    verified = yaml.safe_load(VERIFIED.read_text()) or {}
    added = 0
    for cc, laws in verified.items():
        if cc not in atlas:
            print(f"skip {cc} (not in atlas)"); continue
        kl = atlas[cc].setdefault("key_legislation", [])
        have = {e.get("law_key") for e in kl}
        for law in laws:
            if law.get("law_key") in have:
                print(f"  = {cc}/{law['law_key']} already present"); continue
            kl.append(law); added += 1
            print(f"  + {cc}/{law['law_key']} -> {law.get('source_domain')}")
    print(f"\n{added} entries to add. {'WRITING' if apply else 'DRY-RUN (use --apply)'}")
    if apply and added:
        ATLAS.write_text(yaml.safe_dump(atlas, allow_unicode=True, sort_keys=False))
        print(f"wrote {ATLAS}")

if __name__ == "__main__":
    main()
