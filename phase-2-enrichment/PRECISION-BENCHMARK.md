# Can AI search build a MENA legal database? A precision benchmark

> Experiment, 2026-05-22. We pointed a sourced-search API (Linkup) at the MENA Legal
> Atlas's gap — the missing *laws* layer — and measured how much of a real, primary-source
> legal catalog it could build automatically. Short answer: **~3%.** The 97% is the lesson.

## The setup

The atlas maps *where* MENA law lives (gazettes, courts, regulators) across 25 jurisdictions,
and documents that **only 36% of catalogued sources produce data** — the rest sit behind
Cloudflare WAF, geo-IP, paywalls, login walls. The obvious next step: use an AI search API
to retrieve the actual foundational codes (constitution, civil, penal, labor, tax…) per
jurisdiction and enrich the atlas.

We tested on 3 jurisdictions × 12 core codes = **36 queries**, on a spectrum of portal types:
UAE (modern legislation portal), Lebanon (#1 zero-scraper target), Saudi (search-DB + news gazette).

## The funnel (this is the headline)

| Stage | Result | Reading |
|---|---:|---|
| Queries run | 36 | — |
| Returned a result from an **official domain** | 36 (100%) | `includeDomains` *guarantees* this. Meaningless alone. |
| Passed an automated **precision scorer** (relevance + doc-type + access) | 15 (41%) | Killed the obvious junk. |
| **Human-verified as the actual law, on a usable primary URL** | **1 (3%)** | The only number that matters. |

The single clean hit: the **Lebanese Constitution** (English PDF, on Parliament's own domain).

## Why the scorer's 41% was a mirage

Reading the 15 "accepts" by hand, almost all were **adjacent** documents whose Arabic keywords
overlapped the query:

- UAE "penal code" → the **Cybercrime** decree-law. "companies law" → a **corporate-tax** nexus
  decision. "civil code" → a **journal article** citing the law. "personal status" → a
  **furniture-dispute court ruling**. "data protection" → a **telemarketing** policy.
- Lebanon "penal code" & "companies law" → the same **Public Procurement** PDF.
- Saudi "constitution" → a **2025 royal decree** (not the 1992 Basic Law). "commercial code" →
  a **peer-reviewed research paper** on bankruptcy.

## The two real findings

**1. Constraint solves trust, not precision.** Restricting search to the atlas's official
domains eliminates law-firm SEO spam (unconstrained, the API confidently *hallucinated*
Saudi Labor Law Art. 77 and cited only marketing blogs). But it cannot retrieve the *specific*
codified law — it returns whatever the crawler indexed from that domain: chrome, news, journals,
rulings, stray PDFs.

**2. The ceiling is portal architecture, not model quality.** MENA legal portals
(`laws.boe.gov.sa`, `elaws.moj.gov.ae`, `uaelegislation.gov.ae`) are **search-form databases**.
The law text lives *behind a query interface*, on URLs no crawler has indexed. Precision tracked
portal type exactly: where law pages are crawlable (Lebanon PDFs, some UAE `/legislations/{id}`),
you get hits; where they're a search-DB (Saudi), you get ~0. No amount of scorer tuning moves this.

## What it means for legal AI

- **Grounding ≠ web search.** A legal-AI answer engine for MENA cannot be a search box over the
  open web, even a domain-constrained one. It needs *document-level ingestion* — partnerships,
  bulk feeds, or per-portal connectors — not retrieval.
- **The allowlist is necessary but not sufficient.** The atlas's domain registry makes search
  *safe* (no spam, no hallucinated citations). It does not make it *complete*.
- **The honest-degradation principle holds.** Better to return "primary source exists, not
  retrievable" (Lebanon gazette is paywalled; Saudi codes are behind a search form) than to
  guess. The 97% gap is a true map of where MENA open law is unreachable — which is the atlas's
  whole point.

## Reproduce

```bash
export LINKUP_KEY=...
python3 scripts/enrich_laws.py AE LB SA      # discover + score → phase-2-enrichment/
python3 scripts/merge_laws.py --apply        # merge only human-verified (verified-laws.yaml)
```
