# Linkup smoke test — 2026-05-22

> Can Linkup (sourced-search API) retrieve MENA **primary** law behind the walls the atlas documents?
> Ran ~15 queries across the 10 zero-scraper jurisdictions + UAE/Egypt controls. Verdict below.

## Verdict: atlas + Linkup are complementary, not redundant. The atlas is the moat.

| Mode | Result |
|---|---|
| Linkup standard, unconstrained | 4/12 surfaced an official domain in top 5. Arabic + commercially-saturated jurisdictions (Saudi, UAE, Egypt) returned law-firm SEO spam. |
| Linkup **deep**, unconstrained | **No improvement** — Iraq/UAE/Egypt returned the same spam. Depth is not the lever. |
| Linkup deep, **`includeDomains`** = atlas official domains | 🎯 Flips garbage → 90 results, all official portals, real decree-law text. Reaches `uaelegislation.gov.ae` / `mohre.gov.ae` content behind the walls. |
| Linkup `sourcedAnswer`, unconstrained | ⚠️ Confidently WRONG. Saudi Labor Law Art. 77 → "two months/year" (mangled the 2-month minimum), cited only law-firm marketing blogs. A naive answer-box ships hallucinated statute text. |

## Implications

1. **Do not** build an open-web "MENA legal search box." It hallucinates law and cites marketing.
2. **Do** build a constrained answer layer: per-jurisdiction `includeDomains` = atlas official-domain registry, with **cite-a-primary-source-or-refuse** guardrail.
3. The atlas's per-jurisdiction domain list is exactly the retrieval allowlist that makes Linkup safe for law. That's the defensible asset.
4. Paywalled primaries (Lebanon `jo.pcm.gov.lb`) degrade honestly → "primary exists, paywalled, pointer only." Matches the Ambiguity Index reachability narrative.

## Notable per-jurisdiction signal
- **Good unconstrained primaries:** Palestine `muqtafi.birzeit.edu` (canonical), Iran `faolex.fao.org` / WIPO Lex, Yemen/Sudan/Somalia via `constituteproject.org`.
- **Worst unconstrained:** Iraq (NGO/news only), Saudi-AR + Egypt-AR + UAE-EN (law-firm SEO spam).

Credits spent: ~15 queries (mostly standard, a few deep). Negligible.

---

## Enrichment sample (laws layer) — 2026-05-22

Built `scripts/enrich_laws.py`: for each jurisdiction, query Linkup constrained to
its atlas official-domains for 12 core codes. Staged in `phase-2-enrichment/` (NOT merged).

**Sample (AE/LB/SA): 36/36 "on official domain" — but that's a FALSE positive.**
`includeDomains` guarantees a same-domain hit; it does not guarantee the right law.
Graded by snippet:
- **Lebanon** — good: real law PDFs/records on `lp.gov.lb` (~50-60% correct doc).
- **Saudi** — noisy: `uqn.gov.sa` is a *news* gazette → media-forum page returned for "penal code". The correct constitution page (`laws.boe.gov.sa`) was access-restricted. ~1/5.
- **UAE** — noisy: portal chrome / SPA template placeholders. ~0-1/5.

**Three defects to fix before any merge:**
1. Returns homepages / news / category pages, not the law text.
2. No relevance check (can't tell penal code from a media forum).
3. No domain ranking (codified-law `laws.boe.gov.sa` vs news `uqn.gov.sa`).

Next: precision layer — relevance scorer (law keywords vs title+snippet) + access check
+ codified-domain ranking + discovery via constrained `sourcedAnswer` for real citations.
Re-validate sample, THEN sweep 25, THEN human gate before merge to atlas.yaml.

---

## Precision layer result — 2026-05-22 (the structural ceiling)

Added relevance scorer + access check + codified-domain ranking + sourcedAnswer
fallback. Honest sample: AE 6/12, LB 6/12, SA 3/12 = 15/36 (41%) — and grading
the accepts shows even that overstates it (Saudi's 3 are false positives: a 2025
royal decree tagged "constitution", a research paper tagged "commercial_code").

**Structural finding:** Linkup domain-constrained search returns *a* doc from the
official domain but cannot reliably retrieve the *specific codified law*, because
MENA legal portals are search-form SPAs/DBs (laws.boe.gov.sa, elaws.moj.gov.ae,
uaelegislation.gov.ae). Linkup indexes chrome/news/stray-PDFs, not the records
behind the query interface. Not a tuning problem — a crawlability ceiling.

**Precision is jurisdiction-dependent (portal architecture decides):**
- UAE ~5-6/12, Lebanon ~6/12 (crawlable law pages / PDFs) — usable WITH human check.
- Saudi ~0-1/12 (search-DB + news gazette) — not usable.

**Decision:** No jurisdiction-blind auto-merge. Viable paths = (1) human-verified
merge of high-confidence hits only + publish the precision benchmark; (2) pivot
Linkup to the SOURCE layer (re-verify + discover official domains across 25);
(3) keep full sweep as phase-2 staging for lawyer review, never canonical.
