# MENA Legal Data Atlas

*An open map of every legal-data source in the Middle East and North Africa — official gazettes, consolidated legislation portals, apex courts, and sectoral regulators — with structured pointers for anyone contributing scrapers, indexes, or research.*

**Coverage**: 25 jurisdictions.  
**Upstream state** (worldwidelaw/legal-sources @ HEAD): 118 sources cataloged across MENA — **42 working (35%) · 76 blocked (64%)**.

Companion files:
- [Phase 0 audit](../phase-0-audit/mena-audit.md) — raw audit of upstream coverage
- [Priority action list](priority-action-list.md) — ranked target list
- [`mena-legal-atlas.json`](mena-legal-atlas.json) — machine-readable
- [`atlas.yaml`](atlas.yaml) — source of truth

## Why this exists

Every MENA country publishes its laws somewhere on the internet, but the patchwork of gazette PDFs, academic mirrors, regulator rulebooks, and court portals is undocumented in any single place. Out of 118 MENA sources cataloged in [worldwidelaw/legal-sources](https://github.com/worldwidelaw/legal-sources), only 35% currently produce data — and 10 jurisdictions have **zero** working scrapers. This Atlas exists to make the gap legible, point contributors at the right primary sources, and unblock the next wave of MENA legal-tech building on open data.

## Headline gaps

Jurisdictions with **zero working scrapers** upstream:

- **LB · Lebanon** — ICP: `critical` · Tractability: `medium` · Blocked: 6 sources
- **SA · Saudi Arabia** — ICP: `high` · Tractability: `medium` · Blocked: 11 sources
- **IQ · Iraq** — ICP: `medium` · Tractability: `low` · Blocked: 3 sources
- **YE · Yemen** — ICP: `low` · Tractability: `low` · Blocked: 0 sources
- **PS · Palestine** — ICP: `low` · Tractability: `medium` · Blocked: 1 sources
- **IL · Israel** — ICP: `low` · Tractability: `medium` · Blocked: 7 sources
- **IR · Iran** — ICP: `low` · Tractability: `low` · Blocked: 2 sources
- **KM · Comoros** — ICP: `very_low` · Tractability: `low` · Blocked: 1 sources
- **SD · Sudan** — ICP: `very_low` · Tractability: `very_low` · Blocked: 1 sources
- **SO · Somalia** — ICP: `very_low` · Tractability: `very_low` · Blocked: 1 sources

## Jurisdictions

### GCC

#### BH — Bahrain

- **Legal system**: civil law with sharia influence
- **Languages**: arabic, english
- **Calendar**: gregorian
- **Citation style**: `law_no_X_for_YYYY`

**Official gazette**

- Al-Jarīdah al-Rasmīyah — [https://www.legalaffairs.gov.bh/](https://www.legalaffairs.gov.bh/) `[live]`
  - Format: `pdf`
  - Auth: `none_in_principle`
  - Issued by Legal Affairs Directorate.

**Consolidated legislation**

- LLOC (Legislation and Legal Opinion Commission) — [https://www.lloc.gov.bh](https://www.lloc.gov.bh) `[live]`
  - lloc.gov.bh = legalaffairs.gov.bh (same operator). DNS currently unresolvable from non-BH ranges.

**Apex courts**

- Court of Cassation
- Constitutional Court (ccb.bh)

**Key regulators**

- Central Bank of Bahrain - cbb.gov.bh (rulebook on Thomson Reuters - paywalled)
- National Bureau for Revenue (NBR)

**Upstream state (worldwidelaw)**

- Total: 6 · Working: **1** · Blocked: **5**
  - Working: `BH/NBR-TaxGuidance`
  - Blocked: `BH/CBB`, `BH/ConstitutionalCourt`, `BH/Courts`, `BH/LLOCLegislation`, `BH/Legislation`
  - Dominant blocker: `dns_unreachable + waf`

**Unblock hints**

- Try resolving lloc.gov.bh from a Bahraini residential proxy
- CBB rulebook is on a TR subdomain; only working path is direct partnership with CBB
- ccb.bh returns 403; try via google cache + archive.org
- data.gov.bh has zero legal datasets — file a request issue

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `high` · Tractability: `low` · **Score: 12**

> One of the worst access situations in the GCC despite small corpus size.

---

#### KW — Kuwait

- **Legal system**: civil law with sharia influence
- **Languages**: arabic
- **Calendar**: gregorian
- **Citation style**: `law_no_X_for_YYYY`

**Official gazette**

- Kuwait Al-Yawm (Kuwait Today) — [https://www.alkuwait-alyoum.com](https://www.alkuwait-alyoum.com) `[DNS error]`
  - Format: `pdf`

**Consolidated legislation**

- e.gov.kw legal portal — [https://www.e.gov.kw/sites/kgoenglish/Pages/Visitors/Laws.aspx](https://www.e.gov.kw/sites/kgoenglish/Pages/Visitors/Laws.aspx) `[404]`

**Apex courts**

- Court of Cassation
- Constitutional Court

**Key regulators**

- Central Bank of Kuwait (CBK)
- Capital Markets Authority (CMA)
- Kuwait Tax Authority (MOF)

**Upstream state (worldwidelaw)**

- Total: 3 · Working: **1** · Blocked: **2**
  - Working: `KW/MOF-TaxGuidance`
  - Blocked: `KW/Courts`, `KW/Kuwait`
  - Dominant blocker: `unknown`

**Unblock hints**

- Kuwait National Assembly (kna.kw) publishes draft + enacted laws
- Kuwait Bar Association archives may be the most complete unofficial source

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `high` · Tractability: `medium` · **Score: 13**

> HAQQ has limited GCC presence outside UAE/SA — Kuwait is low-customer-density.

---

#### OM — Oman

- **Legal system**: civil law with sharia influence
- **Languages**: arabic, english
- **Calendar**: gregorian
- **Citation style**: `royal_decree_no_X_of_YYYY`

**Official gazette**

- Al-Jarīdah al-Rasmīyah — [https://qanoon.om](https://qanoon.om) `[live]`
  - Format: `html_pdf`
  - Run by Ministry of Justice and Legal Affairs.

**Consolidated legislation**

- Qanoon Portal — [https://qanoon.om](https://qanoon.om) `[live]`
  - Operator: MOJ

**Apex courts**

- Supreme Court
- Administrative Court

**Key regulators**

- Central Bank of Oman (CBO)
- Tax Authority
- Capital Market Authority

**Upstream state (worldwidelaw)**

- Total: 3 · Working: **3** · Blocked: **0**
  - Working: `OM/DecreeOm`, `OM/Legislation`, `OM/TaxAuthority-Guidance`
  - Dominant blocker: `none`

**Unblock hints**

- Oman is the cleanest GCC case — qanoon.om is well-structured
- Extend existing scrapers to capture Royal Decrees archive back to 1971

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `low` · Tractability: `high` · **Score: 10**

> Strong starting point for "GCC complete" milestone.

---

#### QA — Qatar

- **Legal system**: civil law with sharia influence
- **Languages**: arabic, english
- **Calendar**: gregorian
- **Citation style**: `law_no_X_of_YYYY`

**Official gazette**

- Al-Jarīdah al-Rasmīyah — [https://www.almeezan.qa](https://www.almeezan.qa) `[5xx]`
  - Format: `html`
  - Run by Ministry of Justice. Bilingual.

**Consolidated legislation**

- Al Meezan — [https://www.almeezan.qa](https://www.almeezan.qa) `[5xx]`
  - Operator: MOJ

**Apex courts**

- Court of Cassation
- QFC Civil and Commercial Court

**Key regulators**

- Qatar Central Bank (QCB)
- QFC Regulatory Tribunal (QFCRT)
- General Tax Authority (GTA)

**Upstream state (worldwidelaw)**

- Total: 7 · Working: **4** · Blocked: **3**
  - Working: `QA/AlMeezan`, `QA/AlMeezanCaseLaw`, `QA/GTA-TaxCirculars`, `QA/QFCRT`
  - Blocked: `QA/CourtOfCassation`, `QA/Courts`, `QA/QCB`
  - Dominant blocker: `unknown`

**Unblock hints**

- Al Meezan is well-structured — almost a model portal for the region
- QFC has separate English-language regime; combine for full coverage

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `medium` · Tractability: `high` · **Score: 12**

> Best-organized civil-law portal in the GCC.

---

#### SA — Saudi Arabia

- **Legal system**: islamic law with codified statutes
- **Languages**: arabic, partial_english
- **Calendar**: hijri_primary_gregorian_secondary
- **Citation style**: `royal_decree_no_X_of_YYYY_hijri`

**Official gazette**

- Umm al-Qurā Gazette — [https://www.uqn.gov.sa](https://www.uqn.gov.sa) `[timeout]`
  - Format: `pdf`
  - Published weekly. Full archive online.

**Consolidated legislation**

- Bureau of Experts (BoE) Laws Portal — [https://laws.boe.gov.sa](https://laws.boe.gov.sa) `[timeout]`
  - Operator: Council of Ministers Bureau of Experts
- National Center for Archives and Records (NCAR) — [https://www.ncar.gov.sa](https://www.ncar.gov.sa) `[timeout]`

**Apex courts**

- Supreme Court
- Supreme Administrative Court (Diwan al-Mazalim)
- Court of Appeal (multiple)

**Key regulators**

- Saudi Central Bank (SAMA)
- Capital Market Authority (CMA)
- General Authority of Zakat and Tax (ZATCA)
- Communications, Space & Technology Commission (CST)
- Saudi Data and AI Authority (SDAIA)

**Upstream state (worldwidelaw)**

- Total: 11 · Working: **0** · Blocked: **11**
  - Blocked: `SA/BOELaws`, `SA/BoeLaws`, `SA/CMA`, `SA/GAC`, `SA/GSTC`, `SA/NCC-OpenData`, `SA/NajizLegal`, `SA/SAMA`, `SA/SupremeCourt`, `SA/ZATCA-Guidance`, `SA/ZATCA-VAT`
  - Dominant blocker: `requires_auth + cloudflare`

**Unblock hints**

- laws.boe.gov.sa is THE source for codified statutes — pursue scraping with Saudi residential proxy
- Hijri-Gregorian conversion is non-trivial — must implement both ways
- MOJ portal (moj.gov.sa) publishes Supreme Court rulings since 2017 reform — high priority
- Najiz (najiz.sa) e-court service has public-decisions endpoint behind login wall
- SAMA rulebook is public PDF — clean win
- SDAIA has its own AI/data laws portal — newly relevant

**Priority**

- HAQQ ICP: `high` · Upstream gap: `critical` · Tractability: `medium` · **Score: 18**

> Highest-impact gap in the entire region. SA is a top-3 HAQQ ICP market and
has ZERO working scrapers in upstream. Hijri calendar handling is the
technical wedge that excludes most non-MENA contributors.

---

#### AE — United Arab Emirates

- **Legal system**: civil law with sharia influence
- **Languages**: arabic, english
- **Calendar**: gregorian
- **Citation style**: `federal_law_no_X_of_YYYY`

**Official gazette**

- UAE Official Gazette (Al-Jarīdah al-Rasmīyah) — [https://uaelegislation.gov.ae/en/official-gazette](https://uaelegislation.gov.ae/en/official-gazette) `[WAF-blocked]`
  - Format: `pdf`
  - Auth: `cloudflare_WAF`
  - Issued by Ministry of Justice. Full archive online since 1971.

**Consolidated legislation**

- UAE Legislation Portal — [https://uaelegislation.gov.ae](https://uaelegislation.gov.ae) `[WAF-blocked]`
  - Operator: MOJ
  - Federal laws, decree-laws, cabinet resolutions. Bilingual.
- eLaws (MOJ legacy) — [https://elaws.moj.gov.ae](https://elaws.moj.gov.ae) `[timeout]`
  - Geo-blocked from non-UAE IPs.

**Apex courts**

- Federal Supreme Court
- Court of Cassation (Dubai)
- Court of Cassation (Abu Dhabi)
- DIFC Courts (common-law, English-language)
- ADGM Courts (common-law, English-language)

**Key regulators**

- Central Bank (CBUAE) - rulebook.centralbank.ae
- Securities and Commodities Authority (SCA)
- Federal Tax Authority (FTA)
- DFSA (DIFC financial regulator)
- FSRA (ADGM financial regulator)

**Upstream state (worldwidelaw)**

- Total: 15 · Working: **7** · Blocked: **8**
  - Working: `AE/ADGM-Courts`, `AE/ADGM-Legislation`, `AE/CBUAE`, `AE/DIFC`, `AE/DIFC-Legislation`, `AE/FSRA-Enforcement`, `AE/FTA-PublicClarifications`
  - Blocked: `AE/ADGM`, `AE/DFSA-Enforcement`, `AE/DIFC-Courts`, `AE/FederalLegislation`, `AE/Legislation`, `AE/SCA`, `AE/TDRC-TaxAppeals`, `AE/eLaws`
  - Dominant blocker: `cloudflare_WAF + geo_ip_block`

**Unblock hints**

- Federal MOJ portal is cloudflare-WAF gated; pursue MOU with MOJ Open Data team rather than scraping
- Bayanat (data.bayanat.ae) sometimes hosts MOJ datasets — check periodically
- SCA API requires CSRF auth — request a public API key via SCA contact form
- TDRC tax appeals are protected by Tax Procedures Law Art 7 confidentiality — unscrapeable by design

**Priority**

- HAQQ ICP: `high` · Upstream gap: `medium` · Tractability: `low_for_federal_high_for_freezones` · **Score: 13**

> Free zones (DIFC, ADGM) have the best open access. Federal is the hard part.

---


### Mashriq

#### EG — Egypt

- **Legal system**: civil law french influence
- **Languages**: arabic
- **Calendar**: gregorian
- **Citation style**: `law_no_X_for_YYYY`

**Official gazette**

- Al-Waqāʾiʿ al-Miṣriyyah — [https://manshurat.org](https://manshurat.org) `[live]`
  - Format: `pdf`
  - Primary aggregator is Manshurat (Cabinet-linked).

**Consolidated legislation**

- Manshurat — [https://manshurat.org](https://manshurat.org) `[live]`
  - Operator: Information and Decision Support Center (IDSC)
- ECA Legal Corpus — [https://eca.gov.eg](https://eca.gov.eg) `[timeout]`

**Apex courts**

- Court of Cassation (Mahkamat al-Naqd)
- Supreme Constitutional Court (SCC)
- Council of State (Majlis al-Dawla)

**Key regulators**

- Central Bank of Egypt (CBE)
- Financial Regulatory Authority (FRA)
- Egyptian Tax Authority (ETA)

**Upstream state (worldwidelaw)**

- Total: 10 · Working: **3** · Blocked: **7**
  - Working: `EG/CBE`, `EG/LegalCorpus`, `EG/SCC`
  - Blocked: `EG/CourtOfCassation`, `EG/ECA`, `EG/ETA-AdditionalGuidance`, `EG/ETA-TaxGuidance`, `EG/FRA`, `EG/JACC`, `EG/SupremeCourt`
  - Dominant blocker: `unknown`

**Unblock hints**

- Manshurat is the de facto national legal database — extend coverage from current Legal Corpus scraper
- Court of Cassation digital archive needs Arabic-OCR pipeline for pre-2010 decisions
- SCC publishes rulings PDF — relatively clean

**Priority**

- HAQQ ICP: `high` · Upstream gap: `high` · Tractability: `medium` · **Score: 16**

> Largest Arabic-speaking legal system. High-value target.

---

#### IQ — Iraq

- **Legal system**: civil law french influence plus kurdish overlay
- **Languages**: arabic, kurdish, english_partial
- **Calendar**: gregorian
- **Citation style**: `law_no_X_for_YYYY`

**Official gazette**

- Al-Waqāʾiʿ al-ʿIrāqiyyah — [https://www.moj.gov.iq](https://www.moj.gov.iq) `[live]`
  - Format: `pdf`
  - Published by MOJ. KRG has separate gazette in Erbil.

**Consolidated legislation**

- Iraqi Legal Database (ILD) — [https://iraqld.hjc.iq](https://iraqld.hjc.iq) `[WAF-blocked]`
  - Operator: Higher Judicial Council
- KRG Legal Database — [https://perleman.org](https://perleman.org) `[live]`
  - Kurdistan Regional Government legislation in Kurdish + Arabic.

**Apex courts**

- Federal Supreme Court (iraqfsc.iq)
- Court of Cassation
- KRG Court of Cassation (separate)

**Key regulators**

- Central Bank of Iraq (CBI)
- Securities Commission (ISC)

**Upstream state (worldwidelaw)**

- Total: 3 · Working: **0** · Blocked: **3**
  - Blocked: `IQ/IRAQLD`, `IQ/IraqiGazette`, `IQ/SupremeCourt`
  - Dominant blocker: `unknown`

**Unblock hints**

- iraqld.hjc.iq is the obvious starting point — test whether captcha is bypassable
- KRG corpus is a separate scraper — don't conflate with federal
- Pre-2003 Saddam-era laws still in force in many areas — needs historical coverage

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `high` · Tractability: `low` · **Score: 12**

> Politically loaded — KRG vs Federal authority is contested. Abbas/Sherif
review required before publishing. Treat as two parallel jurisdictions.

---

#### JO — Jordan

- **Legal system**: civil law french influence
- **Languages**: arabic
- **Calendar**: gregorian
- **Citation style**: `law_no_X_for_YYYY`

**Official gazette**

- Al-Jarīdah al-Rasmīyah — [http://www.pm.gov.jo/print](http://www.pm.gov.jo/print) `[live]`
  - Format: `pdf`

**Consolidated legislation**

- Legislation Bureau (LOB) — [https://lob.jo](https://lob.jo) `[DNS error]`
  - Operator: Prime Minister's Office

**Apex courts**

- Court of Cassation
- Constitutional Court
- High Administrative Court

**Key regulators**

- Central Bank of Jordan (CBJ)
- Income and Sales Tax Department (ISTD)
- Securities Commission (JSC)

**Upstream state (worldwidelaw)**

- Total: 5 · Working: **1** · Blocked: **4**
  - Working: `JO/LOBLegislation`
  - Blocked: `JO/ConstitutionalCourt`, `JO/CourtOfCassation`, `JO/ISTD-TaxGuidance`, `JO/Legislation`
  - Dominant blocker: `unknown`

**Unblock hints**

- lob.jo is the official source — extend to capture regulations and PM decisions
- Jordan E-Government has bilingual subset worth indexing

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `medium` · Tractability: `high` · **Score: 12**

> One of the more tractable Mashriq jurisdictions.

---

#### LB — Lebanon

- **Legal system**: civil law french influence with personal status pluralism
- **Languages**: arabic, french
- **Calendar**: gregorian
- **Citation style**: `law_no_X_dated_YYYY-MM-DD`

**Official gazette**

- Al-Jarīdah al-Rasmīyah (Journal Officiel de la République Libanaise) — [https://www.pcm.gov.lb](https://www.pcm.gov.lb) `[unknown]`
  - Format: `pdf`
  - Issued by Presidency of Council of Ministers. Weekly. Digital archive incomplete pre-2003.

**Consolidated legislation**

- LegiLiban (parliament-linked) — [https://legiliban.ul.edu.lb](https://legiliban.ul.edu.lb) `[unknown]`
  - Currently DNS-unreachable. May have moved or been deprecated.
- USJ Legal Informatics (CEDROMA) — [https://www.usj.edu.lb/cedroma](https://www.usj.edu.lb/cedroma) `[live]`
  - Saint Joseph University academic mirror, often more reliable than official sources.
- Lebanese Parliament archive — [https://www.lp.gov.lb](https://www.lp.gov.lb) `[timeout]`

**Apex courts**

- Court of Cassation (Mahkamat al-Tamyīz)
- Constitutional Council (Majlis Dustūrī)
- State Council (Majlis Shūrā al-Dawlah)

**Key regulators**

- Banque du Liban (BDL)
- Capital Markets Authority (CMA)
- Tax Authority (MOF)
- Personal status courts (18 confessional regimes — non-codified)

**Upstream state (worldwidelaw)**

- Total: 6 · Working: **0** · Blocked: **6**
  - Blocked: `LB/Courts`, `LB/LegiLiban`, `LB/Legislation-Portal`, `LB/MinistryOfJustice`, `LB/MoF-TaxGuidance`, `LB/OfficialGazette`
  - Dominant blocker: `dns_unreachable + login_required`

**Unblock hints**

- {'First fix': 'ping LegiLiban current status via archive.org and USJ contacts'}
- PCM gazette PDFs are the most stable primary source — direct PDF crawl works
- Partner with USJ CEDROMA (Saint Joseph University academic mirror) for a maintained data feed
- Personal status laws are NOT codified — needs special treatment (out-of-scope for v1)

**Priority**

- HAQQ ICP: `critical` · Upstream gap: `critical` · Tractability: `medium` · **Score: 21**

> Stephane's diaspora wedge. Zero working scrapers + critical HAQQ ICP +
Stephane's direct network. Strongest single bet in the entire Atlas.

---

#### PS — Palestine

- **Legal system**: hybrid ottoman british jordanian egyptian
- **Languages**: arabic, english_partial
- **Calendar**: gregorian
- **Citation style**: `varies_by_era`

**Official gazette**

- Al-Waqāʾiʿ al-Filasṭīniyyah — [https://maqam.najah.edu](https://maqam.najah.edu) `[DNS error]`
  - Format: `pdf`
  - Issued by PA in West Bank. Gaza has separate Hamas-issued gazette.

**Consolidated legislation**

- Al-Muqtafi — [https://muqtafi.birzeit.edu](https://muqtafi.birzeit.edu) `[timeout]`
  - Operator: Birzeit University Institute of Law
  - De facto national legal database. Academic, well-maintained.
- Maqam (An-Najah) — [https://maqam.najah.edu](https://maqam.najah.edu) `[live]`
  - Operator: An-Najah National University

**Apex courts**

- Supreme Court (Ramallah)
- High Constitutional Court
- Sharia Courts (personal status)

**Key regulators**

- Palestine Monetary Authority (PMA)
- Palestine Capital Market Authority
- Tax Department

**Upstream state (worldwidelaw)**

- Total: 1 · Working: **0** · Blocked: **1**
  - Blocked: `PS/AlMuqtafi`
  - Dominant blocker: `unknown`

**Unblock hints**

- Al-Muqtafi (Birzeit) is the academic gold standard — partner directly with Institute of Law
- Layered legal system means citation conventions vary by era — needs explicit period tagging
- PA vs Hamas legislation divergence post-2007 needs explicit handling

**Priority**

- HAQQ ICP: `low` · Upstream gap: `high` · Tractability: `medium` · **Score: 10**

> Politically loaded. Abbas/Sherif review required. Academic partnership with
Birzeit is the highest-leverage path.

---

#### SY — Syria

- **Legal system**: civil law french influence
- **Languages**: arabic
- **Calendar**: gregorian
- **Citation style**: `law_no_X_for_YYYY`

**Official gazette**

- Al-Jarīdah al-Rasmīyah — [https://parliament.gov.sy](https://parliament.gov.sy) `[unknown]`
  - Format: `pdf`

**Consolidated legislation**

- Syrian People's Assembly — [https://parliament.gov.sy](https://parliament.gov.sy) `[unknown]`

**Apex courts**

- Court of Cassation
- Supreme Constitutional Court

**Key regulators**

- Central Bank of Syria
- Syrian Tax Authority

**Upstream state (worldwidelaw)**

- Total: 1 · Working: **1** · Blocked: **0**
  - Working: `SY/Legislation`
  - Dominant blocker: `none`

**Unblock hints**

- Parliament site is the only viable primary source
- Sanctions exposure — confirm with Abbas before publishing scraper or hosting corpus
- Post-Dec 2024 transition may invalidate or amend large parts of the corpus — track explicitly

**Priority**

- HAQQ ICP: `low` · Upstream gap: `low` · Tractability: `medium` · **Score: 6**

> Currently in legal transition (post Dec 2024). Corpus is unstable —
legitimacy of pre-transition laws is contested. Atlas should explicitly
timestamp Syrian sources.

---


### Maghreb

#### DZ — Algeria

- **Legal system**: civil law french influence
- **Languages**: arabic, french
- **Calendar**: gregorian
- **Citation style**: `ordonnance_or_loi_no_X-Y_du_DD-MM-YYYY`

**Official gazette**

- Journal Officiel (Al-Jarīdah al-Rasmīyah) — [https://www.joradp.dz](https://www.joradp.dz) `[live]`
  - Format: `pdf_html`
  - Run by Secrétariat Général du Gouvernement.

**Consolidated legislation**

- JORADP — [https://www.joradp.dz](https://www.joradp.dz) `[live]`
  - Operator: Government Secretariat

**Apex courts**

- Cour Suprême
- Conseil Constitutionnel (now Cour constitutionnelle)
- Conseil d'État

**Key regulators**

- Bank of Algeria
- DGI (tax)
- COSOB (securities)

**Upstream state (worldwidelaw)**

- Total: 6 · Working: **4** · Blocked: **2**
  - Working: `DZ/ConseilConstitutionnel`, `DZ/CourSupreme`, `DZ/JORADP`, `DZ/SupremeCourt-Decisions`
  - Blocked: `DZ/DGI-TaxGuidance`, `DZ/JORADP2`
  - Dominant blocker: `server_unreachable`

**Unblock hints**

- DGI tax portal returns 500 — wait for govt to fix or pivot to MOF gazette
- Coverage already strong — focus on case law completeness (CourSupreme has WordPress API)

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `low` · Tractability: `high` · **Score: 10**

> Strongest Maghreb coverage in upstream. Maintain rather than build.

---

#### LY — Libya

- **Legal system**: civil law french italian influence
- **Languages**: arabic, italian_historical
- **Calendar**: gregorian
- **Citation style**: `law_no_X_for_YYYY`

**Official gazette**

- Al-Jarīdah al-Rasmīyah — [https://aladel.gov.ly](https://aladel.gov.ly) `[live]`
  - Format: `pdf`
  - Bifurcated state — Tripoli (GNU) and Benghazi (HoR) issue separate gazettes.

**Consolidated legislation**

- Ministry of Justice (Tripoli) — [https://aladel.gov.ly](https://aladel.gov.ly) `[live]`
- LawSocietyLY archive — [https://lawsocietyly.org](https://lawsocietyly.org) `[DNS error]`

**Apex courts**

- Supreme Court (Tripoli)
- Constitutional Chamber

**Key regulators**

- Central Bank of Libya (CBL) - bifurcated

**Upstream state (worldwidelaw)**

- Total: 2 · Working: **1** · Blocked: **1**
  - Working: `LY/DCAF`
  - Blocked: `LY/LawSocietyLY`
  - Dominant blocker: `unknown`

**Unblock hints**

- Bifurcation must be explicit — two parallel corpora since 2014
- DCAF (Geneva Centre for Security Sector Governance) Libya page is best non-official aggregator

**Priority**

- HAQQ ICP: `low` · Upstream gap: `high` · Tractability: `low` · **Score: 9**

> Same political-instability caveats as Syria. Treat as two jurisdictions.

---

#### MR — Mauritania

- **Legal system**: islamic law with french civil overlay
- **Languages**: arabic, french
- **Calendar**: gregorian
- **Citation style**: `ordonnance_no_X_du_DD-MM-YYYY`

**Official gazette**

- Journal Officiel — [https://www.journalofficiel.dj](https://www.journalofficiel.dj) `[live]`
  - Format: `pdf`

**Consolidated legislation**

- Secrétariat Général du Gouvernement — [https://www.sgg.gov.mr](https://www.sgg.gov.mr) `[DNS error]`

**Apex courts**

- Cour Suprême
- Conseil Constitutionnel

**Key regulators**

- Banque Centrale de Mauritanie

**Upstream state (worldwidelaw)**

- Total: 1 · Working: **1** · Blocked: **0**
  - Working: `MR/JournalOfficiel`
  - Dominant blocker: `none`

**Unblock hints**

- Smallest corpus in MENA — entire codified law set fits in a few hundred PDFs
- SGG is reachable but slow — use polite rate limit

**Priority**

- HAQQ ICP: `very_low` · Upstream gap: `low` · Tractability: `high` · **Score: 4**

> Small but tractable. Low priority unless completionism mandates it.

---

#### MA — Morocco

- **Legal system**: civil law french influence with islamic personal status
- **Languages**: arabic, french
- **Calendar**: gregorian
- **Citation style**: `dahir_no_X-Y_du_DD-MM-YYYY`

**Official gazette**

- Bulletin Officiel (Al-Jarīdah al-Rasmīyah) — [http://www.sgg.gov.ma](http://www.sgg.gov.ma) `[404]`
  - Format: `pdf`
  - Issued by Secrétariat Général du Gouvernement.

**Consolidated legislation**

- Adala (MOJ portal) — [http://adala.justice.gov.ma](http://adala.justice.gov.ma) `[live]`
- SGG Bulletin Officiel — [http://www.sgg.gov.ma](http://www.sgg.gov.ma) `[404]`

**Apex courts**

- Cour de Cassation
- Cour Constitutionnelle

**Key regulators**

- Bank Al-Maghrib
- DGI (tax)
- AMMC (capital markets)
- Conseil de la Concurrence

**Upstream state (worldwidelaw)**

- Total: 6 · Working: **3** · Blocked: **3**
  - Working: `MA/AdalaJustice`, `MA/ConseilConcurrence`, `MA/SGG-BulletinOfficiel`
  - Blocked: `MA/Adala`, `MA/CourDeCassation`, `MA/DGI-TaxGuidance`
  - Dominant blocker: `unknown`

**Unblock hints**

- SGG Bulletin Officiel PDF archive is the gold standard primary source
- Adala has decent coverage but inconsistent metadata — needs normalization

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `medium` · Tractability: `high` · **Score: 12**

> Comparatively easy. Maintain + extend rather than rebuild.

---

#### TN — Tunisia

- **Legal system**: civil law french influence
- **Languages**: arabic, french
- **Calendar**: gregorian
- **Citation style**: `loi_no_X-Y_du_DD-MM-YYYY`

**Official gazette**

- Journal Officiel de la République Tunisienne (JORT) — [https://www.iort.gov.tn](https://www.iort.gov.tn) `[unknown]`
  - Format: `pdf`
  - Issued by Imprimerie Officielle.

**Consolidated legislation**

- JORT — [https://www.iort.gov.tn](https://www.iort.gov.tn) `[unknown]`
- LegislationTN — [https://legislation.tn](https://legislation.tn) `[timeout]`

**Apex courts**

- Cour de Cassation
- Tribunal Administratif

**Key regulators**

- Banque Centrale de Tunisie (BCT)
- DGI (tax)
- CMF (financial markets)

**Upstream state (worldwidelaw)**

- Total: 6 · Working: **2** · Blocked: **4**
  - Working: `TN/CourDeCassation`, `TN/JORT-Legislation`
  - Blocked: `TN/DGI-TaxGuidance`, `TN/IORT`, `TN/JORT`, `TN/LegislationTN`
  - Dominant blocker: `unknown`

**Unblock hints**

- JORT site has been stable for years — direct PDF crawl
- Post-2021 political situation has produced procedural irregularities — flag as needed

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `medium` · Tractability: `high` · **Score: 12**

---


### Arabian Peninsula

#### YE — Yemen

- **Legal system**: civil law with sharia influence
- **Languages**: arabic
- **Calendar**: hijri_and_gregorian
- **Citation style**: `law_no_X_for_YYYY`

**Official gazette**

- Al-Jarīdah al-Rasmīyah — [https://www.yemen.gov.ye](https://www.yemen.gov.ye) `[timeout]`
  - Format: `pdf`
  - Bifurcated state — IRG (Aden, internationally recognized) and Houthi-controlled (Sanaa) issue parallel laws since 2014/2015.

**Consolidated legislation**

- Ministry of Legal Affairs — [https://yemenmla.gov.ye](https://yemenmla.gov.ye) `[DNS error]`
  - Currently of uncertain status given conflict.
- Sabq Law (private aggregator) — [https://sabqlaw.net](https://sabqlaw.net) `[DNS error]`

**Apex courts**

- Supreme Court (de jure single, de facto bifurcated)

**Key regulators**

- Central Bank of Yemen - bifurcated between Aden and Sanaa branches

**Upstream state (worldwidelaw)**

- Total: 0 · Working: **0** · Blocked: **0**
  - Dominant blocker: `missing_entirely`

**Unblock hints**

- File "New Source" issue upstream — Yemen has zero coverage
- Pre-2014 unified corpus is the most realistic v1 target
- Post-2014 parallel corpora need explicit IRG/Houthi labeling
- Yemeni Bar Association archives may be the most complete remaining record
- University of Sanaa Law School historically maintained academic mirrors

**Priority**

- HAQQ ICP: `low` · Upstream gap: `maximum` · Tractability: `low` · **Score: 11**

> The ONLY MENA country with zero entries in worldwidelaw. Greenfield
contribution opportunity, but politically and operationally hard.

---


### Horn

#### DJ — Djibouti

- **Legal system**: civil law french influence with sharia personal status
- **Languages**: french, arabic
- **Calendar**: gregorian
- **Citation style**: `loi_no_X-Y_du_DD-MM-YYYY`

**Official gazette**

- Journal Officiel de la République de Djibouti — [https://www.journalofficiel.dj](https://www.journalofficiel.dj) `[live]`
  - Format: `pdf`

**Consolidated legislation**

- Présidence — [https://www.presidence.dj](https://www.presidence.dj) `[live]`

**Apex courts**

- Cour Suprême
- Conseil Constitutionnel

**Key regulators**

- Banque Centrale de Djibouti

**Upstream state (worldwidelaw)**

- Total: 1 · Working: **1** · Blocked: **0**
  - Working: `DJ/JournalOfficiel`
  - Dominant blocker: `none`

**Unblock hints**

- Smallest viable MENA corpus
- Already covered upstream — maintain only

**Priority**

- HAQQ ICP: `very_low` · Upstream gap: `low` · Tractability: `high` · **Score: 4**

---

#### SO — Somalia

- **Legal system**: pluralist civil islamic xeer customary
- **Languages**: somali, arabic, italian_historical, english
- **Calendar**: gregorian
- **Citation style**: `varies`

**Official gazette**

- Faafinta Rasmiga ah ee Jamhuuriyadda Federaalka Soomaaliya — [https://moj.gov.so](https://moj.gov.so) `[live]`
  - Format: `pdf`

**Consolidated legislation**

- Ministry of Justice — [https://moj.gov.so](https://moj.gov.so) `[live]`

**Apex courts**

- Supreme Court (Mogadishu)
- Constitutional Court (provisional)

**Key regulators**

- Central Bank of Somalia

**Upstream state (worldwidelaw)**

- Total: 1 · Working: **0** · Blocked: **1**
  - Blocked: `SO/Legislation`
  - Dominant blocker: `unknown`

**Unblock hints**

- Federal vs Federal Member State (Puntland, Somaliland) divergence is structural
- Xeer customary law is uncodified — out-of-scope for v1
- Diaspora law schools (Hargeisa, Mogadishu Univ) maintain partial archives

**Priority**

- HAQQ ICP: `very_low` · Upstream gap: `high` · Tractability: `very_low` · **Score: 5**

> Lowest priority. Cover only after every other MENA jurisdiction is at v1.

---


### Africa

#### KM — Comoros

- **Legal system**: civil law french influence with sharia
- **Languages**: french, arabic, comorian
- **Calendar**: gregorian
- **Citation style**: `loi_no_X_du_DD-MM-YYYY`

**Official gazette**

- Journal Officiel de l'Union des Comores — [https://www.beit-salam.km](https://www.beit-salam.km) `[live]`
  - Format: `pdf`

**Apex courts**

- Cour Suprême

**Key regulators**

- Banque Centrale des Comores

**Upstream state (worldwidelaw)**

- Total: 1 · Working: **0** · Blocked: **1**
  - Blocked: `KM/Legislation`
  - Dominant blocker: `unknown`

**Unblock hints**

- Tiny corpus — fits in a few hundred PDFs
- Often shared with Comorian diaspora at La Reunion (French) — French sources may mirror

**Priority**

- HAQQ ICP: `very_low` · Upstream gap: `high` · Tractability: `low` · **Score: 6**

> Skip in v1 unless completionism demands it.

---

#### SD — Sudan

- **Legal system**: civil law with islamic law overlay in transition
- **Languages**: arabic, english_partial
- **Calendar**: gregorian
- **Citation style**: `law_no_X_for_YYYY`

**Official gazette**

- Sudan Gazette — [https://moj.gov.sd](https://moj.gov.sd) `[live]`
  - Format: `pdf`
  - Disrupted by 2023-2024 conflict.

**Consolidated legislation**

- Ministry of Justice — [https://moj.gov.sd](https://moj.gov.sd) `[live]`

**Apex courts**

- Supreme Court
- Constitutional Court

**Key regulators**

- Central Bank of Sudan

**Upstream state (worldwidelaw)**

- Total: 1 · Working: **0** · Blocked: **1**
  - Blocked: `SD/Legislation`
  - Dominant blocker: `unknown`

**Unblock hints**

- Pre-2019 corpus is most legally certain
- Civil war ongoing — most authorities offline
- University of Khartoum Faculty of Law historically maintained academic archives

**Priority**

- HAQQ ICP: `very_low` · Upstream gap: `high` · Tractability: `very_low` · **Score: 5**

> Defer until conflict stabilizes.

---


### Non-Arab MENA

#### IR — Iran

- **Legal system**: islamic law with civil codes
- **Languages**: farsi, arabic_for_religious_texts
- **Calendar**: solar_hijri_jalali_calendar
- **Citation style**: `law_of_DD-MM-YYYY_solar_hijri`

**Official gazette**

- Rūznāme-ye Rasmī — [https://www.rrk.ir](https://www.rrk.ir) `[DNS error]`
  - Format: `pdf`

**Consolidated legislation**

- Qavanin (DOTIC) — [https://qavanin.ir](https://qavanin.ir) `[timeout]`
  - Operator: Office of the President - Center for Codification of Laws

**Apex courts**

- Supreme Court
- Constitutional Council (Guardian Council)
- Administrative Justice Court

**Key regulators**

- Central Bank of Iran (CBI)
- Securities and Exchange Organization (SEO)
- Iranian National Tax Administration (INTA)

**Upstream state (worldwidelaw)**

- Total: 2 · Working: **0** · Blocked: **2**
  - Blocked: `IR/Qavanin`, `IR/SupremeCourt`
  - Dominant blocker: `unknown`

**Unblock hints**

- Solar Hijri (Jalali) calendar conversion is the technical wedge
- Sanctions exposure for hosting Iranian legal data — confirm with Abbas
- DOTIC qavanin.ir is the gold-standard official source
- Farsi language requires separate NLP pipeline from Arabic

**Priority**

- HAQQ ICP: `low` · Upstream gap: `high` · Tractability: `low` · **Score: 9**

> Sanctions and language barrier make this politically and technically
distinct from Arab MENA. Often excluded from "Arab Legal Atlas" framing.
Decision required: include or carve out into separate sub-project.

---

#### IL — Israel

- **Legal system**: common law with civil law codifications and jewish law in personal status
- **Languages**: hebrew, arabic, english_partial
- **Calendar**: gregorian_with_hebrew_for_religious
- **Citation style**: `law_name_year_section`

**Official gazette**

- Reshumot — [https://www.gov.il/he/departments/publications/?OfficeId=...](https://www.gov.il/he/departments/publications/?OfficeId=...) `[WAF-blocked]`
  - Format: `pdf`

**Consolidated legislation**

- Nevo (commercial) — [https://www.nevo.co.il](https://www.nevo.co.il) `[live]`
- Knesset — [https://main.knesset.gov.il/Activity/Legislation/Laws](https://main.knesset.gov.il/Activity/Legislation/Laws) `[live]`

**Apex courts**

- Supreme Court (Beit ha-Mishpat ha-Elyon)
- Supreme Rabbinical Court (personal status for Jews)
- Sharia Courts (personal status for Muslims)

**Key regulators**

- Bank of Israel
- Israel Securities Authority (ISA)
- Tax Authority

**Upstream state (worldwidelaw)**

- Total: 7 · Working: **0** · Blocked: **7**
  - Blocked: `IL/HasadnaKnesset`, `IL/ITA-TaxCirculars`, `IL/Knesset`, `IL/KnessetLegislation`, `IL/KnessetOData`, `IL/KnessetOData-Retry`, `IL/SupremeCourt`
  - Dominant blocker: `anti_bot_and_paywall`

**Unblock hints**

- Knesset publishes laws under permissive terms — direct PDF/HTML crawl
- Supreme Court rulings via gov.il are publicly accessible but anti-bot protected
- Nevo is the dominant commercial database — out-of-scope for open data
- Hebrew-RTL processing is the technical wedge

**Priority**

- HAQQ ICP: `low` · Upstream gap: `high` · Tractability: `medium` · **Score: 10**

> Politically sensitive in MENA framing. Stephane's stated peace-first
posture suggests including without commentary. Abbas review required.

---

#### TR — Turkey

- **Legal system**: civil law swiss french german influence
- **Languages**: turkish, english_partial
- **Calendar**: gregorian
- **Citation style**: `law_no_X_dated_DD-MM-YYYY`

**Official gazette**

- Resmî Gazete — [https://www.resmigazete.gov.tr](https://www.resmigazete.gov.tr) `[live]`
  - Format: `pdf_html`

**Consolidated legislation**

- Mevzuat Bilgi Sistemi — [https://www.mevzuat.gov.tr](https://www.mevzuat.gov.tr) `[live]`
  - Operator: Presidency

**Apex courts**

- Anayasa Mahkemesi (Constitutional Court)
- Yargıtay (Court of Cassation)
- Danıştay (Council of State)

**Key regulators**

- Central Bank (TCMB)
- SPK (capital markets)
- GİB (revenue / tax)
- Rekabet Kurumu (competition)

**Upstream state (worldwidelaw)**

- Total: 13 · Working: **9** · Blocked: **4**
  - Working: `TR/AnayasaMahkemesi`, `TR/Danistay`, `TR/GIB-Ozelgeler`, `TR/GIB-TaxCirculars`, `TR/MevzuatHF`, `TR/RekabetKurumu`, `TR/ResmiGazete`, `TR/TBMM`, `TR/Yargitay`
  - Blocked: `TR/ConstitutionalCourt`, `TR/Mevzuat`, `TR/MevzuatGov-Scraper`, `TR/SPK`
  - Dominant blocker: `anti_bot`

**Unblock hints**

- Best-covered MENA country in upstream — maintain rather than build
- Anti-bot on a few courts can likely be bypassed with proper UA + rate limiting

**Priority**

- HAQQ ICP: `medium` · Upstream gap: `low` · Tractability: `high` · **Score: 10**

> Whether Turkey is "MENA" is contested. Included here because HAQQ has
Turkish-speaking customers and Turkey is in the regional regulatory
conversation.

---


## Methodology

Field definitions in [`atlas.yaml`](atlas.yaml). Each entry is currently **unverified** unless a `validator` is attached — the Atlas v0.1 is researcher-compiled. Phase 2 of the project will pair each jurisdiction with a local lawyer to validate the entry.

## License

Atlas content is published under **CC BY 4.0**. Upstream worldwidelaw/legal-sources code is **AGPL-3.0 with a commercial license**; any contributions to upstream are governed by their CLA. This repository does not bundle their scraper code.