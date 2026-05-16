#!/usr/bin/env python3
"""
Phase 1 generator: compile per-jurisdiction atlas.yaml + Phase 0 audit
into a headline Markdown doc, a machine-readable JSON, and a priority
action list.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ATLAS_YAML = ROOT / "phase-1-atlas" / "atlas.yaml"
AUDIT_JSON = ROOT / "phase-0-audit" / "mena-audit.json"
OUT_DIR = ROOT / "phase-1-atlas"


REGION_ORDER = [
    "GCC",
    "Mashriq",
    "Maghreb",
    "Arabian_Peninsula",
    "Horn",
    "Africa",
    "Non-Arab_MENA",
]

PRIORITY_RANK = {
    "critical": 4,
    "high": 3,
    "medium": 2,
    "low": 1,
    "very_low": 0,
    "maximum": 4,
}


def compose_priority_score(entry: dict) -> int:
    p = entry.get("priority", {}) or {}
    icp = PRIORITY_RANK.get((p.get("haqq_icp") or "").lower(), 0)
    gap = PRIORITY_RANK.get((p.get("upstream_gap") or "").lower(), 0)
    # Map tractability inversely (easy = bonus)
    tract = {"high": 2, "medium": 1, "low": 0, "very_low": -1}.get(
        (p.get("tractability") or "").lower(), 0
    )
    return icp * 3 + gap * 2 + tract


def main() -> None:
    atlas = yaml.safe_load(ATLAS_YAML.read_text())
    audit_rows = json.loads(AUDIT_JSON.read_text())

    # Index audit rows by country code
    audit_by_cc: dict[str, list[dict]] = {}
    for r in audit_rows:
        audit_by_cc.setdefault(r["country_code"], []).append(r)

    # --- machine-readable JSON (atlas + reconciled audit counts) ---
    enriched = {}
    for cc, entry in atlas.items():
        rows = audit_by_cc.get(cc, [])
        working = [r for r in rows if r["status_bucket"] == "working"]
        blocked = [r for r in rows if r["status_bucket"] == "blocked"]
        entry["worldwidelaw_reconciled"] = {
            "total": len(rows),
            "working": len(working),
            "blocked": len(blocked),
            "working_source_ids": [r["source_id"] for r in working],
            "blocked_source_ids": [r["source_id"] for r in blocked],
        }
        entry["priority_score"] = compose_priority_score(entry)
        enriched[cc] = entry

    (OUT_DIR / "mena-legal-atlas.json").write_text(
        json.dumps(enriched, indent=2, ensure_ascii=False)
    )

    # --- priority action list ---
    ranked = sorted(enriched.items(), key=lambda kv: -kv[1]["priority_score"])
    action_lines = [
        "# MENA Legal Data Atlas — Priority Action List",
        "",
        "Sorted by composite priority score:",
        "`(haqq_icp × 3) + (upstream_gap × 2) + tractability_bonus`",
        "",
        "| Rank | CC | Country | Score | HAQQ ICP | Upstream gap | Tractability | Working / Blocked |",
        "|---:|---|---|---:|---|---|---|---|",
    ]
    for i, (cc, e) in enumerate(ranked, 1):
        p = e.get("priority", {}) or {}
        recon = e["worldwidelaw_reconciled"]
        action_lines.append(
            f"| {i} | {cc} | {e['country']} | {e['priority_score']} | "
            f"{p.get('haqq_icp', '-')} | {p.get('upstream_gap', '-')} | "
            f"{p.get('tractability', '-')} | "
            f"{recon['working']} / {recon['blocked']} |"
        )
    (OUT_DIR / "priority-action-list.md").write_text("\n".join(action_lines))

    # --- main Atlas markdown doc ---
    lines: list[str] = []
    lines.append("# MENA Legal Data Atlas")
    lines.append("")
    lines.append("*An open map of every legal-data source in the Middle East and "
                 "North Africa — official gazettes, consolidated legislation portals, "
                 "apex courts, and sectoral regulators — with structured pointers "
                 "for anyone contributing scrapers, indexes, or research.*")
    lines.append("")
    lines.append(f"**Coverage**: {len(enriched)} jurisdictions.  ")
    total_sources = sum(e["worldwidelaw_reconciled"]["total"] for e in enriched.values())
    total_working = sum(e["worldwidelaw_reconciled"]["working"] for e in enriched.values())
    total_blocked = sum(e["worldwidelaw_reconciled"]["blocked"] for e in enriched.values())
    lines.append(
        f"**Upstream state** (worldwidelaw/legal-sources @ HEAD): "
        f"{total_sources} sources cataloged across MENA — "
        f"**{total_working} working ({100*total_working//max(total_sources,1)}%) · "
        f"{total_blocked} blocked ({100*total_blocked//max(total_sources,1)}%)**."
    )
    lines.append("")
    lines.append("Companion files:")
    lines.append("- [Phase 0 audit](../phase-0-audit/mena-audit.md) — raw audit of upstream coverage")
    lines.append("- [Priority action list](priority-action-list.md) — ranked target list")
    lines.append("- [`mena-legal-atlas.json`](mena-legal-atlas.json) — machine-readable")
    lines.append("- [`atlas.yaml`](atlas.yaml) — source of truth")
    lines.append("")
    lines.append("## Why this exists")
    lines.append("")
    lines.append(
        "Every MENA country publishes its laws somewhere on the internet, but the "
        "patchwork of gazette PDFs, academic mirrors, regulator rulebooks, and "
        "court portals is undocumented in any single place. Out of 118 MENA sources "
        "cataloged in [worldwidelaw/legal-sources](https://github.com/worldwidelaw/legal-sources), "
        f"only {100*total_working//max(total_sources,1)}% currently produce data — and 10 jurisdictions have **zero** "
        "working scrapers. This Atlas exists to make the gap legible, point "
        "contributors at the right primary sources, and unblock the next wave of "
        "MENA legal-tech building on open data."
    )
    lines.append("")
    lines.append("## Headline gaps")
    lines.append("")
    no_working = sorted(
        [(cc, e) for cc, e in enriched.items() if e["worldwidelaw_reconciled"]["working"] == 0],
        key=lambda kv: -kv[1]["priority_score"],
    )
    lines.append("Jurisdictions with **zero working scrapers** upstream:")
    lines.append("")
    for cc, e in no_working:
        p = e.get("priority", {}) or {}
        lines.append(
            f"- **{cc} · {e['country']}** — ICP: `{p.get('haqq_icp','-')}` · "
            f"Tractability: `{p.get('tractability','-')}` · "
            f"Blocked: {e['worldwidelaw_reconciled']['blocked']} sources"
        )
    lines.append("")

    # --- per-jurisdiction entries, grouped by region ---
    lines.append("## Jurisdictions")
    lines.append("")
    by_region: dict[str, list[tuple[str, dict]]] = {}
    for cc, e in enriched.items():
        by_region.setdefault(e.get("region", "Other"), []).append((cc, e))

    for region in REGION_ORDER:
        entries = sorted(by_region.get(region, []), key=lambda kv: kv[1]["country"])
        if not entries:
            continue
        lines.append(f"### {region.replace('_', ' ')}")
        lines.append("")
        for cc, e in entries:
            render_country(lines, cc, e)
        lines.append("")

    # --- legend ---
    lines.append("## Methodology")
    lines.append("")
    lines.append(
        "Field definitions in [`atlas.yaml`](atlas.yaml). "
        "Each entry is currently **unverified** unless a `validator` is attached — "
        "the Atlas v0.1 is researcher-compiled. Phase 2 of the project will pair "
        "each jurisdiction with a local lawyer to validate the entry."
    )
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append(
        "Atlas content is published under **CC BY 4.0**. Upstream "
        "worldwidelaw/legal-sources code is **AGPL-3.0 with a commercial license**; "
        "any contributions to upstream are governed by their CLA. This repository "
        "does not bundle their scraper code."
    )

    (OUT_DIR / "mena-legal-atlas.md").write_text("\n".join(lines))

    print(f"Wrote: {OUT_DIR / 'mena-legal-atlas.md'}")
    print(f"Wrote: {OUT_DIR / 'mena-legal-atlas.json'}")
    print(f"Wrote: {OUT_DIR / 'priority-action-list.md'}")
    print()
    print(f"Atlas covers {len(enriched)} jurisdictions")
    print(f"  Sources upstream: {total_sources} ({total_working} working, {total_blocked} blocked)")
    print(f"  Jurisdictions with zero working scrapers: {len(no_working)}")
    print()
    print("Top 5 priority targets:")
    for cc, e in sorted(enriched.items(), key=lambda kv: -kv[1]["priority_score"])[:5]:
        print(f"  {cc} {e['country']:<25s} score={e['priority_score']}")


def _url_badge(check: dict | None) -> str:
    if not check:
        return ""
    mapping = {
        "live": "live",
        "forbidden_403": "WAF-blocked",
        "not_found_404": "404",
        "server_error_5xx": "5xx",
        "timeout": "timeout",
        "dns_error": "DNS error",
        "unknown": "unknown",
    }
    label = mapping.get(check.get("status"), check.get("status") or "?")
    return f"`[{label}]`"


def render_country(lines: list[str], cc: str, e: dict) -> None:
    lines.append(f"#### {cc} — {e['country']}")
    lines.append("")
    legal_system = e.get("legal_system", "—").replace("_", " ")
    languages = ", ".join(e.get("languages", []))
    lines.append(f"- **Legal system**: {legal_system}")
    lines.append(f"- **Languages**: {languages}")
    lines.append(f"- **Calendar**: {e.get('calendar', '-')}")
    lines.append(f"- **Citation style**: `{e.get('citation_style', '-')}`")
    lines.append("")

    auth = e.get("authorities", {}) or {}
    og = auth.get("official_gazette")
    if og:
        lines.append("**Official gazette**")
        lines.append("")
        badge = _url_badge(og.get("url_check"))
        lines.append(f"- {og.get('name', '?')} — [{og.get('url', '')}]({og.get('url', '')}) {badge}")
        if og.get("format"):
            lines.append(f"  - Format: `{og['format']}`")
        if og.get("auth"):
            lines.append(f"  - Auth: `{og['auth']}`")
        if og.get("notes"):
            lines.append(f"  - {og['notes']}")
        lines.append("")

    cons = auth.get("consolidated") or []
    if cons:
        lines.append("**Consolidated legislation**")
        lines.append("")
        for c in cons:
            badge = _url_badge(c.get("url_check"))
            lines.append(f"- {c.get('name', '?')} — [{c.get('url','')}]({c.get('url','')}) {badge}")
            if c.get("operator"):
                lines.append(f"  - Operator: {c['operator']}")
            if c.get("notes"):
                lines.append(f"  - {c['notes']}")
        lines.append("")

    courts = auth.get("apex_courts") or []
    if courts:
        lines.append("**Apex courts**")
        lines.append("")
        for c in courts:
            lines.append(f"- {c}")
        lines.append("")

    regs = auth.get("key_regulators") or []
    if regs:
        lines.append("**Key regulators**")
        lines.append("")
        for r in regs:
            lines.append(f"- {r}")
        lines.append("")

    recon = e["worldwidelaw_reconciled"]
    lines.append("**Upstream state (worldwidelaw)**")
    lines.append("")
    lines.append(f"- Total: {recon['total']} · Working: **{recon['working']}** · Blocked: **{recon['blocked']}**")
    if recon["working_source_ids"]:
        lines.append(f"  - Working: {', '.join('`'+i+'`' for i in recon['working_source_ids'])}")
    if recon["blocked_source_ids"]:
        lines.append(f"  - Blocked: {', '.join('`'+i+'`' for i in recon['blocked_source_ids'])}")
    if e.get("worldwidelaw", {}).get("dominant_blocker"):
        lines.append(f"  - Dominant blocker: `{e['worldwidelaw']['dominant_blocker']}`")
    lines.append("")

    hints = e.get("unblock_hints") or []
    if hints:
        lines.append("**Unblock hints**")
        lines.append("")
        for h in hints:
            lines.append(f"- {h}")
        lines.append("")

    p = e.get("priority", {}) or {}
    lines.append("**Priority**")
    lines.append("")
    lines.append(
        f"- HAQQ ICP: `{p.get('haqq_icp','-')}` · "
        f"Upstream gap: `{p.get('upstream_gap','-')}` · "
        f"Tractability: `{p.get('tractability','-')}` · "
        f"**Score: {e['priority_score']}**"
    )
    lines.append("")

    if e.get("notes"):
        lines.append(f"> {e['notes'].strip()}")
        lines.append("")

    lines.append("---")
    lines.append("")


if __name__ == "__main__":
    main()
