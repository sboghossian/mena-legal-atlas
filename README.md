# MENA Legal Data Atlas

An open map of every legal-data source in the Middle East and North Africa — gazettes, consolidated legislation, apex courts, sectoral regulators — with structured pointers for anyone contributing scrapers, indexes, or research on top of MENA open law.

**Status**: v1.0 — researcher-compiled with a URL-validation pass. Per-jurisdiction lawyer validation lands in v1.1.

## What's here

```
mena-legal-atlas/
├── phase-0-audit/          # Audit of worldwidelaw/legal-sources MENA coverage
│   ├── mena-audit.md         Human-readable status table
│   ├── mena-audit.csv        Per-source rows
│   └── mena-audit.json       Machine-readable
├── phase-1-atlas/          # The Atlas itself
│   ├── atlas.yaml            Source-of-truth structured data (25 jurisdictions)
│   ├── mena-legal-atlas.md   Headline document
│   ├── mena-legal-atlas.json Machine-readable
│   └── priority-action-list.md  Ranked targets for Phase 2
├── scripts/
│   ├── audit_mena.py         Regenerates Phase 0 from upstream manifest
│   └── generate_atlas.py     Compiles Phase 1 outputs from atlas.yaml + audit
└── data/legal-sources-upstream/   # shallow clone of worldwidelaw/legal-sources
```

## TL;DR (Phase 0 + 1 findings)

- **118 MENA sources** cataloged in [worldwidelaw/legal-sources](https://github.com/worldwidelaw/legal-sources) across 24 jurisdictions.
- **Only 36% currently produce data** (42 working, 76 blocked).
- **10 jurisdictions have zero working scrapers**: Lebanon, Saudi Arabia, Israel, Iraq, Iran, Palestine, Sudan, Somalia, Comoros, Yemen.
- **Yemen** has no entries upstream at all — the only completely greenfield MENA jurisdiction.
- The dominant blockers are **Cloudflare WAF, geo-IP restrictions, third-party paywalls, and login walls** — not missing source code.

Top 5 priority targets (composite score = ICP × 3 + upstream gap × 2 + tractability bonus):

| Rank | Country | Score | Why |
|---:|---|---:|---|
| 1 | Lebanon | 21 | Zero working scrapers, critical HAQQ ICP, Stephane's diaspora network |
| 2 | Saudi Arabia | 18 | 11 blocked / 0 working, top GCC ICP, requires Hijri date handling |
| 3 | Egypt | 16 | Largest Arabic-speaking corpus, 7 blocked / 3 working |
| 4 | UAE | 13 | High ICP but partial coverage exists in free zones (DIFC/ADGM) |
| 5 | Kuwait | 13 | Medium-tractability gap |

See [phase-1-atlas/priority-action-list.md](phase-1-atlas/priority-action-list.md) for the full ranking.

## How to use

### Read the Atlas
Open [`phase-1-atlas/mena-legal-atlas.md`](phase-1-atlas/mena-legal-atlas.md) — it's the headline document.

### Build downstream
Consume [`phase-1-atlas/mena-legal-atlas.json`](phase-1-atlas/mena-legal-atlas.json) — it's the machine-readable version with reconciled upstream source IDs.

### Contribute corrections
Atlas entries are in [`phase-1-atlas/atlas.yaml`](phase-1-atlas/atlas.yaml). Open a PR with edits. Run `python scripts/generate_atlas.py` to regenerate downstream files.

### Refresh from upstream
```bash
cd data/legal-sources-upstream && git pull
cd ../.. && python scripts/audit_mena.py && python scripts/generate_atlas.py
```

## Scope: what counts as "MENA"

25 jurisdictions:

- **Arab League (22)**: DZ, BH, KM, DJ, EG, IQ, JO, KW, LB, LY, MR, MA, OM, PS, QA, SA, SO, SD, SY, TN, AE, YE
- **Non-Arab MENA (3)**: IR (Iran), IL (Israel), TR (Turkey)

Edge cases are flagged in each country entry. The Atlas takes no position on contested sovereignty (Iraqi KRG vs Federal, Libya GNU vs HoR, Yemen IRG vs Houthi, Palestine PA vs Hamas, post-2024 Syria) — it documents the parallel sources where they exist.

## Validation status

Every entry is currently **unverified**. v0.1 is researcher-compiled from public sources, the upstream `manifest.yaml`, and the maintainer's domain knowledge. **Do not treat as authoritative.**

Phase 2 of the project will pair each jurisdiction with a local lawyer or law-school validator. Validator credit will be added per entry.

## License

- **Atlas content** (this repo): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — use, modify, redistribute with attribution.
- **Upstream worldwidelaw/legal-sources** is AGPL-3.0 with a commercial license. We do **not** bundle their scraper code — only cross-reference their source IDs. Any contributions back to upstream will be governed by their CLA.

## Why this exists

HAQQ Legal AI is a MENA-focused legal AI company. Operating in the region quickly surfaces a fact that no global index captures: every country publishes its laws somewhere, but the patchwork of gazette PDFs, academic mirrors, regulator rulebooks, and court portals has never been documented in one place.

The Atlas is the map. The corpus is the byproduct.

## Enriched layers (Linkup experiment, 2026-05)

Two new layers were added to `atlas.yaml` via a sourced-search API (Linkup), staged and
filtered before merge — see [`linkup-smoke-test.md`](linkup-smoke-test.md) and
[`phase-2-enrichment/PRECISION-BENCHMARK.md`](phase-2-enrichment/PRECISION-BENCHMARK.md):

- **`additional_sources`** — 233 official-source domains (central banks, tax/data-protection/
  competition/IP authorities, courts, registrars) the gazette-centric map missed. Domain-level
  discovery is where AI search reliably works.
- **`key_legislation`** — constitutions for 21 jurisdictions (via Constitute Project / WIPO Lex)
  + 1 verified primary entry (Lebanon).

Honest caveat: building a *document-level* laws catalog by AI search caps at ~3% precision —
MENA portals are search-DB SPAs whose law text no crawler indexes. The benchmark documents why.

## Roadmap

- **v1.0 (now)** — researcher-compiled Atlas + Phase 0 audit + URL validation
- **v1.1** — per-jurisdiction validation by local lawyers (starting LB + SA)
- **v1.2** — interactive web view
- **v2.0** — scraper contributions land upstream for top 5 priority jurisdictions

## Contact

Maintained by Stephane Boghossian (Head of Growth, HAQQ Legal AI). Atlas authorship is a HAQQ-sponsored open project; opinions are the maintainer's.
