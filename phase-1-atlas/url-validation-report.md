# URL Validation Report

Run date: **2026-05-16**  ·  Checked: **61** URLs across **25** jurisdictions.

## Summary

| Status | Count |
|---|---:|
| live | 28 |
| forbidden_403 | 4 |
| not_found_404 | 3 |
| server_error_5xx | 2 |
| timeout | 10 |
| dns_error | 8 |
| unknown | 6 |

> `forbidden_403` typically means a WAF (Cloudflare, Azure) is blocking the user-agent — the content is usually live but unreachable from non-interactive clients. `dns_error` and `timeout` are real outages.

## dns_error (8)

| CC | Source | URL | Code | Detail |
|---|---|---|---:|---|
| IR | gazette:Rūznāme-ye Rasmī | https://www.rrk.ir |  | [Errno 8] nodename nor servname provided, or not known |
| JO | consolidated:Legislation Bureau (LOB) | https://lob.jo |  | [Errno 8] nodename nor servname provided, or not known |
| KW | gazette:Kuwait Al-Yawm (Kuwait Today) | https://www.alkuwait-alyoum.com |  | [Errno 8] nodename nor servname provided, or not known |
| LY | consolidated:LawSocietyLY archive | https://lawsocietyly.org |  | [Errno 8] nodename nor servname provided, or not known |
| MR | consolidated:Secrétariat Général du Gouvernement | https://www.sgg.gov.mr |  | [Errno 8] nodename nor servname provided, or not known |
| PS | gazette:Al-Waqāʾiʿ al-Filasṭīniyyah | https://www.maqam.najah.edu |  | [Errno 8] nodename nor servname provided, or not known |
| YE | consolidated:Ministry of Legal Affairs | https://yemenmla.gov.ye |  | [Errno 8] nodename nor servname provided, or not known |
| YE | consolidated:Sabq Law (private aggregator) | https://sabqlaw.net |  | [Errno 8] nodename nor servname provided, or not known |

## timeout (10)

| CC | Source | URL | Code | Detail |
|---|---|---|---:|---|
| AE | consolidated:eLaws (MOJ legacy) | https://elaws.moj.gov.ae |  | timed out |
| EG | consolidated:ECA Legal Corpus | https://eca.gov.eg |  | timed out |
| IR | consolidated:Qavanin (DOTIC) | https://qavanin.ir |  | timed out |
| LB | consolidated:Lebanese Parliament archive | https://www.lp.gov.lb |  |  |
| PS | consolidated:Al-Muqtafi | https://muqtafi.birzeit.edu |  | timed out |
| SA | consolidated:Bureau of Experts (BoE) Laws Portal | https://laws.boe.gov.sa |  | timed out |
| SA | consolidated:National Center for Archives and Records (NCAR) | https://www.ncar.gov.sa |  | timed out |
| SA | gazette:Umm al-Qurā Gazette | https://www.uqn.gov.sa |  | timed out |
| TN | consolidated:LegislationTN | https://legislation.tn |  | timed out |
| YE | gazette:Al-Jarīdah al-Rasmīyah | https://www.yemen.gov.ye |  | timed out |

## not_found_404 (3)

| CC | Source | URL | Code | Detail |
|---|---|---|---:|---|
| KW | consolidated:e.gov.kw legal portal | https://www.e.gov.kw/sites/kgoenglish/Pages/Visitors/Laws.aspx | 404 | Not Found |
| MA | consolidated:SGG Bulletin Officiel | http://www.sgg.gov.ma | 404 | Not Found |
| MA | gazette:Bulletin Officiel (Al-Jarīdah al-Rasmīyah) | http://www.sgg.gov.ma | 404 | Not Found |

## server_error_5xx (2)

| CC | Source | URL | Code | Detail |
|---|---|---|---:|---|
| QA | consolidated:Al Meezan | https://www.almeezan.qa | 500 | Internal Server Error |
| QA | gazette:Al-Jarīdah al-Rasmīyah | https://www.almeezan.qa | 500 | Internal Server Error |

## forbidden_403 (4)

| CC | Source | URL | Code | Detail |
|---|---|---|---:|---|
| AE | consolidated:UAE Legislation Portal | https://uaelegislation.gov.ae | 403 | Forbidden |
| AE | gazette:UAE Official Gazette (Al-Jarīdah al-Rasmīyah) | https://uaelegislation.gov.ae/en/official-gazette | 403 | Forbidden |
| IL | gazette:Reshumot | https://www.gov.il/he/departments/publications/?OfficeId=... | 403 | Forbidden |
| IQ | consolidated:Iraqi Legal Database (ILD) | https://iraqld.hjc.iq | 403 | Forbidden |

## unknown (6)

| CC | Source | URL | Code | Detail |
|---|---|---|---:|---|
| LB | consolidated:LegiLiban (parliament-linked) | https://legiliban.ul.edu.lb |  | [Errno 61] Connection refused |
| LB | gazette:Al-Jarīdah al-Rasmīyah (Journal Officiel de la République Libanaise) | https://www.pcm.gov.lb |  | [Errno 61] Connection refused |
| SY | consolidated:Syrian People's Assembly | https://parliament.gov.sy |  | [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl. |
| SY | gazette:Al-Jarīdah al-Rasmīyah | https://parliament.gov.sy |  | [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl. |
| TN | consolidated:JORT | https://www.iort.gov.tn |  | [Errno 61] Connection refused |
| TN | gazette:Journal Officiel de la République Tunisienne (JORT) | https://www.iort.gov.tn |  | [Errno 61] Connection refused |

## live (28)

| CC | Source | URL | Code | Detail |
|---|---|---|---:|---|
| BH | consolidated:LLOC (Legislation and Legal Opinion Commission) | https://www.lloc.gov.bh | 200 |  |
| BH | gazette:Al-Jarīdah al-Rasmīyah | https://www.legalaffairs.gov.bh/ | 200 |  |
| DJ | consolidated:Présidence | https://www.presidence.dj | 200 |  |
| DJ | gazette:Journal Officiel de la République de Djibouti | https://www.journalofficiel.dj | 200 |  |
| DZ | consolidated:JORADP | https://www.joradp.dz | 200 |  |
| DZ | gazette:Journal Officiel (Al-Jarīdah al-Rasmīyah) | https://www.joradp.dz | 200 |  |
| EG | consolidated:Manshurat | https://manshurat.org | 200 |  |
| EG | gazette:Al-Waqāʾiʿ al-Miṣriyyah | https://manshurat.org | 200 |  |
| IL | consolidated:Knesset | https://main.knesset.gov.il/Activity/Legislation/Laws | 247 |  |
| IL | consolidated:Nevo (commercial) | https://www.nevo.co.il | 200 |  |
| IQ | consolidated:KRG Legal Database | https://perleman.org | 200 |  |
| IQ | gazette:Al-Waqāʾiʿ al-ʿIrāqiyyah | https://www.moj.gov.iq | 200 |  |
| JO | gazette:Al-Jarīdah al-Rasmīyah | http://www.pm.gov.jo/print | 200 |  |
| KM | gazette:Journal Officiel de l'Union des Comores | https://www.beit-salam.km | 200 |  |
| LB | consolidated:USJ Legal Informatics (CEDROMA) | https://www.usj.edu.lb/cedroma | 200 |  |
| LY | consolidated:Ministry of Justice (Tripoli) | https://aladel.gov.ly | 200 |  |
| LY | gazette:Al-Jarīdah al-Rasmīyah | https://aladel.gov.ly | 200 |  |
| MA | consolidated:Adala (MOJ portal) | http://adala.justice.gov.ma | 200 |  |
| MR | gazette:Journal Officiel | https://www.journalofficiel.dj | 200 |  |
| OM | consolidated:Qanoon Portal | https://qanoon.om | 200 |  |
| OM | gazette:Al-Jarīdah al-Rasmīyah | https://qanoon.om | 200 |  |
| PS | consolidated:Maqam (An-Najah) | https://maqam.najah.edu | 200 |  |
| SD | consolidated:Ministry of Justice | https://moj.gov.sd | 200 |  |
| SD | gazette:Sudan Gazette | https://moj.gov.sd | 200 |  |
| SO | consolidated:Ministry of Justice | https://moj.gov.so | 200 |  |
| SO | gazette:Faafinta Rasmiga ah ee Jamhuuriyadda Federaalka Soomaaliya | https://moj.gov.so | 200 |  |
| TR | consolidated:Mevzuat Bilgi Sistemi | https://www.mevzuat.gov.tr | 200 |  |
| TR | gazette:Resmî Gazete | https://www.resmigazete.gov.tr | 200 | via_get |
