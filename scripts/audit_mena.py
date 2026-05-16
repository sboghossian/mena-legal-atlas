#!/usr/bin/env python3
"""
Phase 0 audit: read worldwidelaw/legal-sources manifest.yaml, filter for MENA,
emit a structured audit table (CSV + JSON + Markdown).
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1] / "data" / "legal-sources-upstream"
OUT = Path(__file__).resolve().parents[1] / "phase-0-audit"
OUT.mkdir(parents=True, exist_ok=True)

# MENA scope: Arab League (22) + Iran + Israel + Turkey.
MENA = {
    "DZ": ("Algeria", "Arab League / Maghreb"),
    "BH": ("Bahrain", "Arab League / GCC"),
    "KM": ("Comoros", "Arab League / Africa"),
    "DJ": ("Djibouti", "Arab League / Horn"),
    "EG": ("Egypt", "Arab League / Mashriq"),
    "IQ": ("Iraq", "Arab League / Mashriq"),
    "JO": ("Jordan", "Arab League / Mashriq"),
    "KW": ("Kuwait", "Arab League / GCC"),
    "LB": ("Lebanon", "Arab League / Mashriq"),
    "LY": ("Libya", "Arab League / Maghreb"),
    "MR": ("Mauritania", "Arab League / Maghreb"),
    "MA": ("Morocco", "Arab League / Maghreb"),
    "OM": ("Oman", "Arab League / GCC"),
    "PS": ("Palestine", "Arab League / Mashriq"),
    "QA": ("Qatar", "Arab League / GCC"),
    "SA": ("Saudi Arabia", "Arab League / GCC"),
    "SO": ("Somalia", "Arab League / Horn"),
    "SD": ("Sudan", "Arab League / Africa"),
    "SY": ("Syria", "Arab League / Mashriq"),
    "TN": ("Tunisia", "Arab League / Maghreb"),
    "AE": ("United Arab Emirates", "Arab League / GCC"),
    "YE": ("Yemen", "Arab League / Arabian Peninsula"),
    "IR": ("Iran", "Non-Arab MENA"),
    "IL": ("Israel", "Non-Arab MENA"),
    "TR": ("Turkey", "Non-Arab MENA"),
}


def load_manifest() -> list[dict]:
    with open(REPO / "manifest.yaml", "r") as f:
        data = yaml.safe_load(f)
    return data["sources"]


def is_mena(src: dict) -> bool:
    return src.get("country") in MENA


def status_bucket(src: dict) -> str:
    """Collapse upstream statuses into 4 buckets."""
    status = (src.get("status") or "").lower()
    blocked = src.get("blocked_reason")
    if blocked:
        return "blocked"
    if status in ("complete", "complete-with-issues", "ready"):
        return "working"
    if status in ("in-progress", "wip", "draft", "partial"):
        return "partial"
    if status in ("stub", "planned", "todo", ""):
        return "stub"
    return status or "unknown"


def has_local_scraper(src: dict) -> bool:
    """Check whether the per-source directory has a real bootstrap.py."""
    src_id = src.get("id", "")
    p = REPO / "sources" / src_id / "bootstrap.py"
    if not p.exists():
        return False
    try:
        return p.stat().st_size > 500  # heuristic: above template boilerplate
    except OSError:
        return False


def has_samples(src: dict) -> int:
    src_id = src.get("id", "")
    sample_dir = REPO / "sources" / src_id / "sample"
    if not sample_dir.exists():
        return 0
    return len([p for p in sample_dir.iterdir() if p.is_file() and p.suffix == ".json"])


def main() -> None:
    sources = load_manifest()
    mena = [s for s in sources if is_mena(s)]
    mena.sort(key=lambda s: (s.get("country"), s.get("id")))

    rows = []
    for s in mena:
        cc = s["country"]
        country_name, region = MENA[cc]
        rows.append({
            "country_code": cc,
            "country": country_name,
            "region": region,
            "source_id": s.get("id"),
            "source_name": s.get("name"),
            "data_types": ",".join(s.get("data_types") or []),
            "url": s.get("url"),
            "auth": s.get("auth"),
            "status_upstream": s.get("status"),
            "status_bucket": status_bucket(s),
            "blocked_reason": s.get("blocked_reason"),
            "license": s.get("license_name"),
            "commercial_use": s.get("commercial_use"),
            "priority": s.get("priority"),
            "has_bootstrap": has_local_scraper(s),
            "sample_count": has_samples(s),
            "notes": (s.get("notes") or "").replace("\n", " ").strip(),
        })

    # --- CSV ---
    csv_path = OUT / "mena-audit.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # --- JSON ---
    json_path = OUT / "mena-audit.json"
    with open(json_path, "w") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    # --- Summary stats ---
    by_country = defaultdict(lambda: defaultdict(int))
    by_bucket = defaultdict(int)
    by_datatype = defaultdict(int)
    for r in rows:
        cc = r["country_code"]
        by_country[cc]["total"] += 1
        by_country[cc][r["status_bucket"]] += 1
        by_bucket[r["status_bucket"]] += 1
        for dt in (r["data_types"] or "").split(","):
            if dt:
                by_datatype[dt] += 1

    # --- Markdown summary ---
    md_path = OUT / "mena-audit.md"
    lines = []
    lines.append("# MENA Audit — worldwidelaw/legal-sources")
    lines.append("")
    lines.append("Phase 0 snapshot. Source: `manifest.yaml` from upstream repo "
                 "(github.com/worldwidelaw/legal-sources), cloned "
                 f"into [data/legal-sources-upstream/](../data/legal-sources-upstream/).")
    lines.append("")
    lines.append(f"**Total MENA sources cataloged upstream**: {len(rows)} "
                 f"across {len(by_country)} jurisdictions.")
    lines.append("")
    lines.append("## Status distribution")
    lines.append("")
    lines.append("| Bucket | Count |")
    lines.append("|---|---|")
    for b in ("working", "partial", "stub", "blocked", "unknown"):
        if by_bucket.get(b):
            lines.append(f"| {b} | {by_bucket[b]} |")
    lines.append("")

    lines.append("## Coverage by jurisdiction")
    lines.append("")
    lines.append("| CC | Country | Total | Working | Partial | Stub | Blocked |")
    lines.append("|---|---|---:|---:|---:|---:|---:|")
    # Include every MENA country, even those with zero sources upstream
    for cc, (name, _region) in sorted(MENA.items(), key=lambda kv: kv[1][0]):
        c = by_country.get(cc, {})
        lines.append(
            f"| {cc} | {name} | {c.get('total', 0)} | "
            f"{c.get('working', 0)} | {c.get('partial', 0)} | "
            f"{c.get('stub', 0)} | {c.get('blocked', 0)} |"
        )
    lines.append("")

    lines.append("## Data type coverage (any status)")
    lines.append("")
    lines.append("| Data type | Source count |")
    lines.append("|---|---:|")
    for dt, n in sorted(by_datatype.items(), key=lambda kv: -kv[1]):
        lines.append(f"| {dt} | {n} |")
    lines.append("")

    lines.append("## Sources detail (per jurisdiction)")
    lines.append("")
    last_cc = None
    for r in rows:
        if r["country_code"] != last_cc:
            last_cc = r["country_code"]
            lines.append(f"### {r['country_code']} — {r['country']}  ({r['region']})")
            lines.append("")
            lines.append("| Source | Types | Auth | Status | License | Samples | Notes |")
            lines.append("|---|---|---|---|---|---:|---|")
        notes = (r["notes"] or "")[:140]
        lines.append(
            f"| [{r['source_id']}]({r['url']}) | "
            f"{r['data_types']} | {r['auth'] or ''} | "
            f"**{r['status_bucket']}**{' (' + (r['blocked_reason'] or '') + ')' if r['blocked_reason'] else ''} | "
            f"{r['license'] or ''} | {r['sample_count']} | {notes} |"
        )
    lines.append("")

    md_path.write_text("\n".join(lines))

    print(f"Wrote: {csv_path}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    print()
    print(f"Sources: {len(rows)} across {len(by_country)} jurisdictions")
    print("By bucket:")
    for b, n in sorted(by_bucket.items(), key=lambda kv: -kv[1]):
        print(f"  {b:10s} {n}")


if __name__ == "__main__":
    main()
