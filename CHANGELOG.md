# Changelog

All notable changes to this project will be documented here.
The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [1.1] — 2026-06-06

### Added
- **Coverage scoring layer** (`scripts/score_coverage.py`) — scores all 25 jurisdictions
  on five axes: source depth, reachability tier, language regime, recency, and
  codifiability (internal-only). Recency is checked via Linkup constrained to each
  jurisdiction's official domains; language + codifiability via OpenRouter (model IDs
  read from env, never hard-coded). Outputs `data/coverage-scores.json` (public, no
  codifiability) and `data/coverage-scores-internal.json`.
- **Coverage scorecard viz** (`viz/build_scorecard.py` → `viz/coverage-scorecard.html`
  + `.png`) — heatmap table, HAQQ ICP markets pinned first. Reachability shown by
  working-source tier, not raw %, to avoid the small-denominator trap.
- README "Coverage Scorecard (Phase 2)" section.

### Changed
- Refreshed the Legal Data Hunter benchmark off the live public `status.json`
  (2026-06-06): LDH MENA now 243 sources / 44% complete (was 163 / 41% on 2026-05-22);
  unique official domains we surface that LDH lacks is now 99 (was ~150) as LDH expanded.

### Headline finding
- 20/25 jurisdictions have full 5-category source depth, but only 4 are actually
  reachable (4+ live sources) and 10 are fully blocked (0 live sources).

## [1.0] — 2026-05-16

First public release.

### Added
- Phase 0 audit of every MENA source in `worldwidelaw/legal-sources`
  - 118 sources across 24 jurisdictions cataloged
  - Status buckets: 42 working, 76 blocked
  - Structured CSV / JSON / Markdown outputs
- Phase 1 Atlas covering 25 MENA jurisdictions
  - Per-jurisdiction entries with official gazette, consolidated portals, apex
    courts, key regulators, upstream state, unblock hints, priority score
  - `atlas.yaml` is the source of truth; generator renders MD + JSON downstream
- URL validation pass on 61 atlas URLs
  - Annotated each URL with `url_check` block: status, code, checked_at
  - 28 live, 4 WAF-blocked, 8 DNS errors, 10 timeouts, 3 404s, 2 5xx, 6 unknown
- Priority action list ranking jurisdictions by composite score
  - Top 5: Lebanon (21), Saudi Arabia (18), Egypt (16), UAE (13), Kuwait (13)
- LinkedIn announcement drafts (three variants)
- CC BY 4.0 license

### Known limits
- Every Atlas entry is **researcher-compiled and unverified by a local lawyer**.
  Do not treat as legal authority.
- "URL live" only means HTTP 200/301/302 — content correctness not verified.
- Hijri/Solar-Hijri calendar handling is documented per-country but not
  implemented in any tooling.
- 10 jurisdictions have zero working scrapers upstream. The Atlas documents
  the gap; it does not close it.

### Next
- v1.1 — per-jurisdiction lawyer validation for top-5 priority targets
- v1.2 — interactive web view at `mena-legal-atlas.haqq.ai` (Lovable)
- v2.0 — scraper contributions land upstream for LB and SA
