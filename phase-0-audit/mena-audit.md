# MENA Audit — worldwidelaw/legal-sources

Phase 0 snapshot. Source: `manifest.yaml` from upstream repo (github.com/worldwidelaw/legal-sources), cloned into [data/legal-sources-upstream/](../data/legal-sources-upstream/).

**Total MENA sources cataloged upstream**: 118 across 24 jurisdictions.

## Status distribution

| Bucket | Count |
|---|---|
| working | 42 |
| blocked | 76 |

## Coverage by jurisdiction

| CC | Country | Total | Working | Partial | Stub | Blocked |
|---|---|---:|---:|---:|---:|---:|
| DZ | Algeria | 6 | 4 | 0 | 0 | 2 |
| BH | Bahrain | 6 | 1 | 0 | 0 | 5 |
| KM | Comoros | 1 | 0 | 0 | 0 | 1 |
| DJ | Djibouti | 1 | 1 | 0 | 0 | 0 |
| EG | Egypt | 10 | 3 | 0 | 0 | 7 |
| IR | Iran | 2 | 0 | 0 | 0 | 2 |
| IQ | Iraq | 3 | 0 | 0 | 0 | 3 |
| IL | Israel | 7 | 0 | 0 | 0 | 7 |
| JO | Jordan | 5 | 1 | 0 | 0 | 4 |
| KW | Kuwait | 3 | 1 | 0 | 0 | 2 |
| LB | Lebanon | 6 | 0 | 0 | 0 | 6 |
| LY | Libya | 2 | 1 | 0 | 0 | 1 |
| MR | Mauritania | 1 | 1 | 0 | 0 | 0 |
| MA | Morocco | 6 | 3 | 0 | 0 | 3 |
| OM | Oman | 3 | 3 | 0 | 0 | 0 |
| PS | Palestine | 1 | 0 | 0 | 0 | 1 |
| QA | Qatar | 7 | 4 | 0 | 0 | 3 |
| SA | Saudi Arabia | 11 | 0 | 0 | 0 | 11 |
| SO | Somalia | 1 | 0 | 0 | 0 | 1 |
| SD | Sudan | 1 | 0 | 0 | 0 | 1 |
| SY | Syria | 1 | 1 | 0 | 0 | 0 |
| TN | Tunisia | 6 | 2 | 0 | 0 | 4 |
| TR | Turkey | 13 | 9 | 0 | 0 | 4 |
| AE | United Arab Emirates | 15 | 7 | 0 | 0 | 8 |
| YE | Yemen | 0 | 0 | 0 | 0 | 0 |

## Data type coverage (any status)

| Data type | Source count |
|---|---:|
| legislation | 52 |
| case_law | 45 |
| doctrine | 30 |
| parliamentary_proceedings | 1 |

## Sources detail (per jurisdiction)

### AE — United Arab Emirates  (Arab League / GCC)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [AE/ADGM](https://www.adgm.com/adgm-courts/judgments) | case_law | none | **blocked** (duplicate_of_AE/ADGM-Courts) |  | 0 | Duplicate of AE/ADGM-Courts which already covers adgm.com with 143 judgments. |
| [AE/ADGM-Courts](https://www.adgm.com/adgm-courts/judgments) | case_law | none | **working** | https://www.adgm.com/adgm-courts/judgments | 11 | 143 judgments (2017-present). SSR HTML + PDF on assets.adgm.com. Full text via pdfplumber. |
| [AE/ADGM-Legislation](https://www.adgm.com/legal-framework) | legislation | none | **working** | https://www.adgm.com/legal-framework | 11 | ~60 regulations/rules PDFs from ADGM courts legislation page + Abu Dhabi founding laws. Full text via PDF extraction. |
| [AE/CBUAE](https://rulebook.centralbank.ae/en) | doctrine | none | **working** | CBUAE Rulebook Terms of Use | 16 | Drupal 10 site at rulebook.centralbank.ae. 192 regulation pages with full text (avg 97K chars). Banking, insurance, AML/CFT, consumer protec |
| [AE/DFSA-Enforcement](https://www.dfsa.ae/what-we-do/enforcement/regulatory-actions) | doctrine | none | **blocked** (cloudflare_protection) |  | 0 | 8 enforcement cases in 2024. Fines exceeding $2.5M. Active enforcement. |
| [AE/DIFC](https://www.difccourts.ae/rules-decisions/judgments-orders) | case_law | none | **working** | DIFC Courts Disclaimer | 11 | ~5,000 judgments (2007-present). Full text in HTML. CFI, Court of Appeal, SCT, Arbitration, T&C, DEC, Enforcement. |
| [AE/DIFC-Courts](https://www.difccourts.ae/rules-decisions/judgments-orders) | case_law | none | **blocked** (azure_waf_protection) |  | 0 | English-language common law court. CFI + Court of Appeal + Arbitration. Searchable. Also on BAILII. |
| [AE/DIFC-Legislation](https://www.difc.com/business/laws-and-regulations/legal-database) | legislation | none | **working** | https://www.difc.com/business/laws-and-regulations/legal-database | 11 | 139 PDFs (29 laws, 29 regulations, 17 amendments). Full text via PDF extraction. |
| [AE/FSRA-Enforcement](https://www.adgm.com/operating-in-adgm/additional-obligations-of-financial-services-entities/enforcement/regulatory-actions) | doctrine | none | **working** | https://www.adgm.com/operating-in-adgm/additional-obligations-of-financial-services-entities/enforcement/regulatory-actions | 11 | 69 enforcement decisions (Final Notices, Penalty Notices, Enforceable Undertakings). Full text via PDF extraction. |
| [AE/FTA-PublicClarifications](https://tax.gov.ae/en/taxes/vat/guides.references.aspx) | doctrine | none | **working** | https://tax.gov.ae/en/taxes/vat/guides.references.aspx | 16 | 188 VAT + corporate tax + excise tax guides and public clarifications. Full text via PDF extraction. |
| [AE/FederalLegislation](https://elaws.moj.gov.ae/) | legislation | none | **blocked** (geo_blocked_and_cloudflare) |  | 0 | elaws.moj.gov.ae geo-blocked (TCP timeout from non-UAE IPs). uaelegislation.gov.ae behind Cloudflare WAF (403). No public API. data.bayanat. |
| [AE/Legislation](https://uaelegislation.gov.ae) | legislation | cloudflare | **blocked** (cloudflare_protection) |  | 0 | From issue #155. UAE official federal laws portal. Blocked by Cloudflare WAF. No accessible API found. |
| [AE/SCA](https://www.sca.gov.ae/) | doctrine | none | **blocked** (api_requires_auth) |  | 0 | sca.gov.ae API at /api/PublicApi/GetContentList requires CSRF auth. Cannot access programmatically. |
| [AE/TDRC-TaxAppeals](https://www.tax.gov.ae) | case_law | none | **blocked** (no_public_access) |  | 0 | TDRC decisions are not publicly published. Protected by Article 7 of Tax Procedures Law (confidentiality). Communicated only to parties (tax |
| [AE/eLaws](https://elaws.moj.gov.ae/) | legislation,case_law | none | **blocked** (geo_ip_block) |  | 15 | Issue #343: site unreachable (connection timeout from both local and VPS). |
### BH — Bahrain  (Arab League / GCC)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [BH/CBB](https://www.cbb.gov.bh/) | doctrine | none | **blocked** (third_party_paywall) |  | 0 | CBB Rulebook hosted on Thomson Reuters (cbben.thomsonreuters.com) - returns 403. Not open data. Laws page is JavaScript-rendered. |
| [BH/ConstitutionalCourt](https://www.ccb.bh/) | case_law | none | **blocked** (waf_blocks_requests) |  | 0 | Returns 403 Forbidden |
| [BH/Courts](https://www.sjc.bh/) | case_law | none | **blocked** (no_api_geo_restricted) |  | 0 | ahkam.sjc.bh times out (geo-restricted or JS-only). No public API. data.gov.bh has zero legal datasets. Eastlaws has content but is subscrip |
| [BH/LLOCLegislation](https://www.lloc.gov.bh) | legislation | none | **blocked** (dns_unreachable) |  | 15 | Issue #405: DNS unreachable (lloc.gov.bh not resolvable from VPS or local). Domain may be down or geo-restricted. |
| [BH/Legislation](https://www.legalaffairs.gov.bh/) | legislation | none | **blocked** (duplicate) |  | 0 | Duplicate of BH/LLOCLegislation (same site: lloc.gov.bh = legalaffairs.gov.bh) |
| [BH/NBR-TaxGuidance](https://www.nbr.gov.bh/tax_guide) | doctrine | none | **working** | Government of Bahrain, National Bureau for Revenue. Tax guidance published for public access. No formal open licence specified. | 15 | 15 VAT/excise/DMTT guidance PDFs with full text. S3-hosted PDFs extracted via pdf_extract. |
### DJ — Djibouti  (Arab League / Horn)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [DJ/JournalOfficiel](https://www.journalofficiel.dj/) | legislation | none | **working** | https://www.journalofficiel.dj/ | 16 |  |
### DZ — Algeria  (Arab League / Maghreb)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [DZ/ConseilConstitutionnel](https://cour-constitutionnelle.dz/) | case_law | none | **working** | Official Algerian court decisions — public domain (government decisions). Published by the Cour constitutionnelle. Constitutional court decisions are public judicial acts under Algerian law. | 31 | WordPress REST API. ~1200 posts, decisions split from year-grouped pages. Full text. |
| [DZ/CourSupreme](https://coursupreme.dz/) | case_law | none | **working** | Official Algerian court decisions — public domain (government decisions). Published by the Cour supreme via WordPress. Court decisions are public judicial acts under Algerian law. | 16 | WordPress REST API custom post type /decision. 1,261 decisions in Arabic. Full text. |
| [DZ/DGI-TaxGuidance](https://www.mfdgi.gov.dz/) | doctrine | none | **blocked** (server_unreachable) |  | 0 | mfdgi.gov.dz returns HTTP 500 Internal Server Error. Web app in failure state. |
| [DZ/JORADP](https://www.joradp.dz) | legislation | none | **working** | Open Government Data | 13 |  |
| [DZ/JORADP2](https://www.joradp.dz/) | legislation | none | **blocked** (redundant_source) |  | 0 |  |
| [DZ/SupremeCourt-Decisions](https://www.coursupreme.dz/) | case_law | none | **working** | Open Government Data | 13 | WordPress REST API. ~1,261 decisions 2000-2023. Full text in Arabic. |
### EG — Egypt  (Arab League / Mashriq)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [EG/CBE](https://www.cbe.org.eg/en/laws-regulations/regulations/circulars) | doctrine | none | **working** | Open Government Data | 16 |  |
| [EG/CourtOfCassation](https://www.cc.gov.eg/) | case_law | none | **blocked** (requires_login) |  | 0 | cc.gov.eg requires login (username/email + password) to access judgments search. Legislations sidebar is public but judgments are behind aut |
| [EG/ECA](https://eca.org.eg/) | case_law | none | **blocked** (server_error) |  | 0 | eca.org.eg returns HTTP 500 Internal Server Error. |
| [EG/ETA-AdditionalGuidance](https://www.eta.gov.eg/en/digital-services) | doctrine | none | **blocked** (waf_blocks_requests) |  | 0 | Drupal 9 site but WAF blocks all API/JSON access |
| [EG/ETA-TaxGuidance](https://www.eta.gov.eg/en/home) | doctrine | none | **blocked** (waf_blocks_requests) |  | 0 | Drupal 9 site but WAF blocks all API/JSON access |
| [EG/FRA](https://fra.gov.eg/) | doctrine | none | **blocked** (auth_required) |  | 0 | fra.gov.eg shows 'You are not authorized to access this Page.' Access denied. |
| [EG/JACC](https://www.cc.gov.eg/) | case_law | required | **blocked** (auth_required) |  | 0 | cc.gov.eg is actually the Court of Cassation (not Constitutional Court). All judgment search pages redirect to login (302). Requires account |
| [EG/LegalCorpus](https://huggingface.co/datasets/dataflare/egypt-legal-corpus) | legislation | none | **working** | MIT License | 15 | From issue #214. MIT-licensed dataset with 2,434 Egyptian laws. Full text (25M+ tokens, avg 87K chars/doc). Arabic content. Hugging Face dat |
| [EG/SCC](https://www.sccourt.gov.eg/) | case_law | none | **working** | Official Egyptian court decisions — published by the Supreme Constitutional Court. Court decisions are public judicial acts under Egyptian law. Open government data. | 16 | ~9,190 decisions via Django REST API. Arabic text from multiple fields. |
| [EG/SupremeCourt](https://www.cc.gov.eg/) | case_law | required | **blocked** (auth_required) |  | 0 | Duplicate of EG/CourtOfCassation and EG/JACC. cc.gov.eg requires login for all judgment pages. ELPAI portal (elpai.idsc.gov.eg) has 460K+ li |
### IL — Israel  (Non-Arab MENA)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [IL/HasadnaKnesset](https://github.com/hasadna/knesset-data) | legislation | none | **blocked** (auth_required) |  | 0 | Open-source tools to access Israeli Parliament data. Python library. Bills, votes, committees, members. |
| [IL/ITA-TaxCirculars](https://www.taxes.gov.il/) | doctrine | none | **blocked** (waf_javascript_challenge) |  | 0 | taxes.gov.il retired → gov.il with Cloudflare managed challenge. ~207 Hebrew-only PDF circulars. All programmatic access returns 403. |
| [IL/Knesset](https://knesset.gov.il/Odata/ParliamentInfo.svc) | legislation | geo_blocked | **blocked** (geo_blocking) |  | 0 | From issue #219. Knesset OData API with KNS_Bill, laws tables. API works from Israeli IPs only. Returns maintenance page from US/EU. Require |
| [IL/KnessetLegislation](https://m.knesset.gov.il/en/activity/pages/legislation.aspx) | legislation | none | **blocked** (site_maintenance) |  | 0 | knesset.gov.il entirely down for maintenance (OData API + PDF server). Hasadna mirror has CSV metadata but PDFs redirect to maintenance page |
| [IL/KnessetOData](https://knesset.gov.il/Odata/ParliamentInfo.svc) | legislation | none | **blocked** (geo_blocked) |  | 0 | Re-blocked: original issue (geo_blocked) not solvable by PDF extraction alone |
| [IL/KnessetOData-Retry](https://knesset.gov.il/Odata/ParliamentInfo.svc/) | legislation | none | **blocked** (geo_blocked) |  | 0 | 2026-04-01 Still geo-blocked. HTTP 303 redirect to maintenance-page-geo from non-Israeli IPs. Hasadna mirror has metadata only, no full text |
| [IL/SupremeCourt](https://iscd.huji.ac.il) | case_law | none | **blocked** (connection_timeout) |  | 0 | From issue #219. Hebrew University hosted. 16K+ Supreme Court decisions 2010-2018 with 61 variables. Downloadable SPSS/CSV datasets. Site ti |
### IQ — Iraq  (Arab League / Mashriq)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [IQ/IRAQLD](https://iraqld.e-sjc-services.iq/) | legislation | none | **blocked** (cloudflare_protection) |  | 0 | Cloudflare managed challenge blocks all programmatic access. No API. ASP.NET Web Forms with ViewState-dependent navigation. 27K+ legal texts |
| [IQ/IraqiGazette](https://www.moj.gov.iq/iraqmag/) | legislation | none | **blocked** (server_unreachable) |  | 0 | moj.gov.iq entirely unreachable (connection timeout on all URLs). Site appears geo-blocked or down. PDF extraction capability exists but sit |
| [IQ/SupremeCourt](https://www.iraqfsc.iq/) | case_law | none | **blocked** (cloudflare_js_challenge) |  | 0 | Site behind Cloudflare JS challenge, all requests return 403. No API. PDFs require headless browser + PDF extraction. |
### IR — Iran  (Non-Arab MENA)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [IR/Qavanin](https://qavanin.ir/) | legislation | none | **blocked** (arvancloud_403) |  | 0 | ArvanCloud CDN returns 403 on all requests. Likely geo-blocked or requires browser automation. No API discovered. |
| [IR/SupremeCourt](https://www.divanealee.ir/) | case_law | none | **blocked** (geo_blocked) |  | 0 | All Iranian legal databases geo-blocked from outside Iran (403/timeout). No APIs exist. Domain divanealee.ir defunct, migrated to eadl.ir wh |
### JO — Jordan  (Arab League / Mashriq)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [JO/ConstitutionalCourt](https://www.jcc.gov.jo/) | case_law | none | **blocked** (site_unreachable) |  | 1 | cco.gov.jo (actual site) and jc.jo both timeout. Connection refused from both local and VPS. Blocked 2026-04-07. |
| [JO/CourtOfCassation](https://www.jc.jo/) | case_law | none | **blocked** (site_rebuilt_decisions_removed) |  | 0 | Decisions section removed during site rebuild from OctoberCMS to ASP.NET. All /ar/decision/ routes return 404. No alternative API or open da |
| [JO/ISTD-TaxGuidance](https://istd.gov.jo/Default/En) | doctrine | none | **blocked** (server_unreachable) |  | 0 | Connection timeout from all tested locations. Site unreachable. |
| [JO/LOBLegislation](https://www.lob.gov.jo/) | legislation | none | **working** | Official Jordanian legislation — public government data provided by the Legislation and Opinion Bureau. No formal open data license published; standard government copyright applies. | 13 | All Jordanian legislation since 1921. Full text. Free access. Official government portal. |
| [JO/Legislation](https://www.lob.gov.jo/) | legislation | none | **blocked** (vps_ip_blocked) |  | 15 | Issue #359: VPS IP blocked by lob.gov.jo (works locally, 0 records on VPS). ASMX web service with RSA/AES encryption. 6,495+ instruments: la |
### KM — Comoros  (Arab League / Africa)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [KM/Legislation](https://www.droit-afrique.com/pays/comores/) | legislation | none | **blocked** (droit_afrique_403) |  | 0 | droit-afrique.com returns 403 globally (htaccess misconfiguration on OVHcloud). Same as INTL/DroitAfrique. Revisit when site recovers. |
### KW — Kuwait  (Arab League / GCC)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [KW/Courts](https://www.moj.gov.kw/) | case_law | none | **blocked** (auth_required) |  | 0 | Re-blocked: original issue (auth_required) not solvable by PDF extraction alone |
| [KW/Kuwait](https://www.moj.gov.kw/) | legislation | none | **blocked** (no_full_text_access) |  | 0 | Re-blocked: original issue (no_full_text_access) not solvable by PDF extraction alone |
| [KW/MOF-TaxGuidance](https://www.mof.gov.kw) | doctrine | none | **working** | Government of Kuwait, Ministry of Finance. Tax laws, circulars, and guidance published for public access. No formal open licence specified. | 16 | 250 PDFs across laws, decrees, decisions, circulars, guidance manuals from mof.gov.kw. Full text extracted via PDF. |
### LB — Lebanon  (Arab League / Mashriq)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [LB/Courts](https://www.cassation.org/) | case_law | none | **blocked** (domain_down_no_open_data) |  | 0 | cassation.org domain is down (DNS failure). No open data portal for Lebanese court decisions. Only commercial databases (Sader, IDREL) exist |
| [LB/LegiLiban](http://legiliban.ul.edu.lb) | legislation | institutional | **blocked** (institutional_access_only) |  | 0 | From issue #228. Lebanese University Center for Legal Informatics. Contains all Lebanese legislation since Ottoman period (1920+). Only acce |
| [LB/Legislation-Portal](https://www.legallaw.ul.edu.lb/) | legislation | subscription_required | **blocked** (no_api_subscription_required) |  | 0 | No public API. Official Gazette (jo.pcm.gov.lb) requires paid subscription. Lebanese University Legal Informatics Center (legallaw.ul.edu.lb |
| [LB/MinistryOfJustice](https://justice.gov.lb/index.php/laws/1) | legislation | none | **blocked** (no_full_text_access) |  | 0 | From issue #228. Only 3 of 14 laws have PDF full text (Arabic PDFs). Other 11 laws including Constitution only show excerpts with circular " |
| [LB/MoF-TaxGuidance](https://www.finance.gov.lb/en-us/Taxation/) | doctrine | none | **blocked** (ssl_certificate_error) |  | 0 | SSL certificate verification error. Site inaccessible. |
| [LB/OfficialGazette](https://jo.pcm.gov.lb) | legislation | subscription | **blocked** (subscription_required) |  | 0 | From issue #228. Official Gazette from Presidency of Council of Ministers. Requires paid subscription (10M or 5M LBP annual cards via LibanP |
### LY — Libya  (Arab League / Maghreb)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [LY/DCAF](https://security-legislation.ly/) | legislation | none | **working** | CC BY 4.0 | 16 | 2,175 Libyan legal texts via WP REST API. Full text in Arabic. Decrees, laws, resolutions, judicial decisions, bylaws. CC BY 4.0. |
| [LY/LawSocietyLY](https://lawsociety.ly/en/) | legislation,case_law | none | **blocked** (cloudflare) |  | 0 | Cloudflare managed challenge on all pages. robots.txt explicitly blocks AI bots. WP REST API exists but inaccessible. Needs browser automati |
### MA — Morocco  (Arab League / Maghreb)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [MA/Adala](https://adala.justice.gov.ma) | legislation,case_law | unknown | **blocked** (network_access) |  | 0 | From issue #195. Ministry of Justice legal portal with Textes_Juridiques and Jurisprudence. DNS times out from external IPs (same as cspj.ma |
| [MA/AdalaJustice](https://adala.justice.gov.ma/) | legislation | none | **working** | Open access, no authentication required. | 16 | 7,575 Moroccan legal texts via REST API + PDF extraction. Arabic/French. |
| [MA/ConseilConcurrence](https://conseil-concurrence.ma/) | case_law,doctrine | none | **working** | Kingdom of Morocco — official competition decisions and advisory opinions published for public access. No formal open licence specified; standard government copyright applies. | 16 | 1269 posts via WordPress REST API. Full text in French. Competition decisions, merger control, advisory opinions. |
| [MA/CourDeCassation](https://juriscassation.cspj.ma) | case_law | unknown | **blocked** (network_access) |  | 0 | From issue #195. Supreme Council of the Judicial Power portal launched Jan 2022. ~7,700+ decisions. Free public access. DNS resolution fails |
| [MA/DGI-TaxGuidance](https://www.tax.gov.ma/) | doctrine | none | **blocked** (server_unreachable) |  | 0 | tax.gov.ma SSL/TLS handshake times out. Server unreachable from outside Morocco. |
| [MA/SGG-BulletinOfficiel](https://www.sgg.gov.ma/) | legislation | none | **working** | Official Moroccan gazette — Bulletin Officiel published by the Secretariat General of the Government. Official legislation texts are public acts of the Kingdom of Morocco. No formal open data license published. | 16 |  |
### MR — Mauritania  (Arab League / Maghreb)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [MR/JournalOfficiel](https://www.msgg.gov.mr/fr/droit-mauritanien/le-journal-officiel.html) | legislation | none | **working** | mentions legales | 16 | 15+ journal officiel issues with full text via PDF extraction. Avg 185K chars per issue. |
### OM — Oman  (Arab League / GCC)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [OM/DecreeOm](https://decree.om/) | legislation | none | **working** | Open Government Data | 15 | 10K+ English-translated Omani laws via WordPress API. Royal Decrees, Ministerial Decisions, Consolidated Laws, Treaties. 15 samples. |
| [OM/Legislation](https://qanoon.om/) | legislation | none | **working** | https://qanoon.om/ | 15 | ~11,800+ Arabic legislation via WordPress REST API. Royal Decrees (4,875), Ministerial Decisions (4,446), Official Gazette (875), Legal Opin |
| [OM/TaxAuthority-Guidance](https://tms.taxoman.gov.om/portal/) | doctrine,legislation | none | **working** | Government of Oman, Tax Authority. Royal Decrees, regulations, and tax guidance published for public access. No formal open licence specified. | 13 | ~100+ PDFs across 9 categories (Income Tax, VAT, Excise, PIT laws/regulations/guidelines, DTAs). Full text extracted via pdf_extract. Arabic |
### PS — Palestine  (Arab League / Mashriq)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [PS/AlMuqtafi](https://muqtafi.birzeit.edu/) | legislation,case_law | none | **blocked** (site_unreachable) |  | 0 | Site unreachable. Auth may be needed. |
### QA — Qatar  (Arab League / GCC)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [QA/AlMeezan](https://www.almeezan.qa/) | legislation | none | **working** | https://www.almeezan.qa/ | 15 | ID enumeration (2284-6500). ~4000 laws with full article text. Arabic with some English translations. Laws, decrees, amiri decisions, minist |
| [QA/AlMeezanCaseLaw](https://www.almeezan.qa/) | case_law | none | **working** | Official Qatari case law — published by the Ministry of Justice via Al Meezan. Court decisions are public judicial acts under Qatari law. No formal open data license published. | 20 |  |
| [QA/CourtOfCassation](https://www.sjc.gov.qa/) | case_law | none | **blocked** (duplicate_of_QA_AlMeezanCaseLaw) |  | 0 | Duplicate - Court of Cassation rulings already covered by QA/AlMeezanCaseLaw which fetches from almeezan.qa (same data source). |
| [QA/Courts](https://www.sjc.gov.qa/) | case_law | none | **blocked** (duplicate_of_QA/AlMeezanCaseLaw) |  | 0 | sjc.gov.qa is an administrative portal with no judgments; court decisions are on almeezan.qa (already covered by QA/AlMeezanCaseLaw). |
| [QA/GTA-TaxCirculars](https://gta.gov.qa/en/circulars) | doctrine | none | **working** | Government open access | 0 | ~28 tax circulars, decisions, and laws. English PDFs with full text extraction. Covers income tax, excise tax, withholding tax, global minim |
| [QA/QCB](https://www.qcb.gov.qa/) | doctrine | none | **blocked** (anti_bot_protection) |  | 0 | SharePoint-based site — content dynamically rendered, no API or structured data endpoints found. SSL cert issues. |
| [QA/QFCRT](https://www.qicdrc.gov.qa/judgments) | case_law | none | **working** | Government open access | 13 |  |
### SA — Saudi Arabia  (Arab League / GCC)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [SA/BOELaws](https://laws.boe.gov.sa/) | legislation | none | **blocked** (geo_restricted) |  | 0 | Site and all Saudi gov portals (od.data.gov.sa, istitlaa.ncc.gov.sa, boe.gov.sa) timeout from non-Saudi IPs. No API, no open dataset on Hugg |
| [SA/BoeLaws](https://laws.boe.gov.sa/) | legislation | none | **blocked** (duplicate_and_geo_restricted) |  | 0 | Duplicate of SA/BOELaws. Site geo-restricted, unreachable from non-Saudi IPs. |
| [SA/CMA](https://cma.org.sa/) | case_law,doctrine | none | **blocked** (server_unreachable) |  | 0 | cma.org.sa connection timeout. OpenData API is for market stats only, not regulations. |
| [SA/GAC](https://gac.gov.sa/) | case_law,doctrine | none | **blocked** (server_unreachable) |  | 0 | gac.gov.sa returns 503 Service Unavailable. |
| [SA/GSTC](https://gstc.gov.sa/) | case_law | none | **blocked** (server_unreachable) |  | 0 | gstc.gov.sa returns 404. Website appears non-functional. |
| [SA/NCC-OpenData](https://istitlaa.ncc.gov.sa/en/About/Pages/OpenData.aspx) | legislation | none | **blocked** (connection_timeout) |  | 0 | istitlaa.ncc.gov.sa connection times out. Also tried laws.boe.gov.sa — same timeout. Saudi government sites unreachable from this network. |
| [SA/NajizLegal](https://www.moj.gov.sa/) | case_law | api_key | **blocked** (auth_required) |  | 0 | API gateway at laws-gateway.moj.gov.sa requires JWT auth. Developer registration at developers.najiz.sa requires organizational account (gov |
| [SA/SAMA](https://www.sama.gov.sa/) | doctrine | none | **blocked** (server_unreachable) |  | 0 | sama.gov.sa ECONNRESET. Connection refused from tested locations. |
| [SA/SupremeCourt](https://laws.moj.gov.sa/) | case_law | none | **blocked** (spa_requires_browser_automation) |  | 0 | Nuxt.js SPA on laws.moj.gov.sa. Backend API at laws-gateway.moj.gov.sa is behind Apigee with JWT auth (Saudi IAM/Absher). No public REST API |
| [SA/ZATCA-Guidance](https://zatca.gov.sa/en/Pages/default.aspx) | doctrine | none | **blocked** (duplicate_source) |  | 0 | Duplicate of existing SA/ZATCA-Guidance (already complete) |
| [SA/ZATCA-VAT](https://zatca.gov.sa/en/RulesRegulations/Taxes/Pages/WithholdingTax.aspx) | doctrine | none | **blocked** (duplicate_source) |  | 0 | Covered by existing SA/ZATCA-Guidance source |
### SD — Sudan  (Arab League / Africa)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [SD/Legislation](https://sudanlii.org/) | legislation,case_law | none | **blocked** (domain_not_registered) |  | 0 | sudanlii.org domain does not exist (never registered). Sudan is not part of AfricanLII/Laws.Africa network. No programmatic API for Sudan le |
### SO — Somalia  (Arab League / Horn)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [SO/Legislation](https://somalilii.org/) | legislation | none | **blocked** (domain_not_registered) |  | 0 | somalilii.org domain does not exist. Somalia not in AfricanLII/Laws.Africa. No national legislation database available. Only ~13 PDFs via Af |
### SY — Syria  (Arab League / Mashriq)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [SY/Legislation](https://sana.sy/presidency/) | legislation | none | **working** | Syrian Arab News Agency (SANA) — official state news agency. Presidential decrees are public legal instruments. No formal open licence specified. | 16 | Full-text presidential decrees from sana.sy (Arabic). ~104 decrees from transitional government (2025+). Parliament site offline; SANA is pr |
### TN — Tunisia  (Arab League / Maghreb)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [TN/CourDeCassation](https://juricaf.org/recherche/+/facet_pays:Tunisie) | case_law | none | **working** | ODbL 1.0 | 16 | 28 decisions (2005-2019) via Juricaf (AHJUCAF). Full text in French. ODBL license. |
| [TN/DGI-TaxGuidance](https://www.finances.gov.tn/fr/structures-du-ministere/la-direction-generale-des-impots) | doctrine | none | **blocked** (no_api_pdf_only) |  | 0 | Has Documentation Fiscale section but primarily PDF-based. No API or structured data access. |
| [TN/IORT](https://www.iort.gov.tn/) | legislation | none | **blocked** (no_api_access) |  | 0 | iort.gov.tn returns 403. legislation.tn times out. 9anoun.tn uses Livewire dynamic loading (needs Playwright). No programmatic access to Tun |
| [TN/JORT](http://www.iort.gov.tn) | legislation | none | **blocked** (webdev_session_required) |  | 0 | Re-blocked: original issue (webdev_session_required) not solvable by PDF extraction alone |
| [TN/JORT-Legislation](https://legislation-securite.tn/) | legislation | none | **working** | Managed by DCAF (Geneva Centre for Security Sector Governance). Copyright DCAF; all rights reserved per site footer. Underlying Tunisian legislation texts are official state acts. | 16 | WordPress REST API at legislation-securite.tn. ~3954 texts, 80% with French full text. DCAF Geneva Centre for Security Sector Governance dat |
| [TN/LegislationTN](http://www.legislation.tn/en) | legislation | none | **blocked** (site_down) |  | 0 | legislation.tn consistently times out. Drupal-based CMS but unreachable. Alternative 9anoun.tn requires Livewire/Playwright. |
### TR — Turkey  (Non-Arab MENA)

| Source | Types | Auth | Status | License | Samples | Notes |
|---|---|---|---|---|---:|---|
| [TR/AnayasaMahkemesi](https://www.anayasa.gov.tr) | case_law | none | **working** | Open Government Data | 13 | Complete. Norm review (normkararlarbilgibankasi) 5.4K decisions + Individual applications (kararlarbilgibankasi) 16K+ decisions since 2012.  |
| [TR/ConstitutionalCourt](https://kararlarbilgibankas.anayasa.gov.tr/) | case_law | none | **blocked** (duplicate_of_existing) |  | 0 | Duplicate of TR/AnayasaMahkemesi which is already complete. Same data source (kararlarbilgibankasi.anayasa.gov.tr). |
| [TR/Danistay](https://www.danistay.gov.tr) | case_law | none | **working** | Open Government Data | 13 |  |
| [TR/GIB-Ozelgeler](https://gib.gov.tr) | doctrine | none | **working** | Government open access — Turkish Revenue Administration tax rulings (ozelgeler). Official government documents are publicly accessible; legal texts are not copyrightable under Turkish IP law (Art. 31 of Law No. 5846). | 12 | 18,079 binding tax rulings (özelgeler) from GİB. Covers income tax, VAT, corporate tax, stamp duty. Full text via vergibulustayi.com aggrega |
| [TR/GIB-TaxCirculars](https://www.gib.gov.tr/en/) | doctrine | none | **working** |  | 0 | GIB Spring Boot REST API. 4448 total docs across 8 types (sirkuler/teblig/genelYazilar/icGenelge/cbk/bkk/yonetmelik/gerekce). ~3500 have inl |
| [TR/Mevzuat](https://www.mevzuat.gov.tr) | legislation | none | **blocked** (vps_ip_blocked) |  | 15 | Code works fine locally (15 sample records with full text). VPS (Hetzner) IP blocked by mevzuat.gov.tr after ~2,686 records. Requires reside |
| [TR/MevzuatGov-Scraper](https://www.mevzuat.gov.tr/) | legislation | none | **blocked** (duplicate) |  | 0 | Duplicate of TR/MevzuatHF (complete, 907 laws). mevzuat.gov.tr VPS IP blocked. |
| [TR/MevzuatHF](https://huggingface.co/datasets/muhammetakkurt/mevzuat-gov-dataset) | legislation | none | **working** | MIT License | 15 | 907 Turkish laws with full text articles. Avg 19K chars/doc. MIT license. |
| [TR/RekabetKurumu](https://www.rekabet.gov.tr/tr/Kararlar) | case_law | none | **working** | Turkish Competition Authority (public decisions) | 16 | COMPLETE: 10,239 board decisions via HTML scraping + PDF extraction. Covers mergers, competition violations, exemptions, privatization. 15 s |
| [TR/ResmiGazete](https://www.resmigazete.gov.tr) | legislation | none | **working** | All rights reserved (Resmi Gazete). Official gazette content is publicly accessible; the site states all rights reserved per Turkish copyright notice. Official legal texts are not copyrightable under Turkish IP law (Art. 31 of Law No. 5846). | 13 | COMPLETE: Turkish Official Gazette via archive HTML pages. Daily gazette since 1920. Laws, decrees, regulations with full text. 12 sample re |
| [TR/SPK](https://www.spk.gov.tr/) | case_law,doctrine | none | **blocked** |  | 0 | SPA with SSL certificate issues. No accessible API endpoint found. |
| [TR/TBMM](https://www.tbmm.gov.tr/Tutanaklar/TutanakMetinleri) | parliamentary_proceedings | none | **working** | Public domain — Turkish parliamentary proceedings (tutanak). Official legislative records are not subject to copyright under Turkish IP law (Art. 31 of Law No. 5846). | 15 |  |
| [TR/Yargitay](https://www.yargitay.gov.tr) | case_law | none | **working** | Open Government Data | 16 | TIER 2: Supreme court for civil and criminal matters. ~6 million decisions via Bedesten API. Full text from base64-encoded HTML. 23 Civil +  |
