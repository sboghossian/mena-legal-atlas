#!/usr/bin/env python3
"""
enrich_laws.py — discover the foundational LAWS layer the atlas is missing.

For each jurisdiction, query Linkup CONSTRAINED to that jurisdiction's official
domains (from atlas.yaml) for each core code/law, then SCORE candidates for
precision (relevance + document-type + codified-domain rank + access). A
candidate is ACCEPTED only if it clears the score threshold; otherwise the gap
stays honest. On a miss, a constrained sourcedAnswer fallback tries to recover a
real citation. Output is STAGED (phase-2-enrichment/), never auto-merged.

Usage:
  python3 scripts/enrich_laws.py AE LB SA      # specific jurisdictions
  python3 scripts/enrich_laws.py all           # full sweep (25)
"""
import json, os, re, sys, time, datetime, urllib.request, urllib.parse, pathlib

KEY = os.environ.get("LINKUP_KEY", "")
URL = "https://api.linkup.so/v1/search"
ROOT = pathlib.Path(__file__).resolve().parent.parent
ATLAS = ROOT / "phase-1-atlas" / "atlas.yaml"
OUTDIR = ROOT / "phase-2-enrichment"
ACCEPT = 3  # minimum total score to accept a candidate

# key, EN name, AR phrase (query), EN keywords (scoring), AR keywords (scoring)
CORE_LAWS = [
    ("constitution",       "Constitution / Basic Law",       "الدستور القانون الأساسي للحكم",
        ["constitution", "basic law"], ["دستور", "النظام الأساسي", "الأساسي للحكم"]),
    ("civil_code",         "Civil Code",                      "القانون المدني المعاملات المدنية",
        ["civil code", "civil transactions", "civil law"], ["القانون المدني", "المعاملات المدنية", "الموجبات والعقود"]),
    ("civil_procedure",    "Civil Procedure Code",            "قانون أصول المحاكمات المدنية المرافعات",
        ["civil procedure"], ["أصول المحاكمات المدنية", "المرافعات", "الإجراءات المدنية"]),
    ("penal_code",         "Penal / Criminal Code",           "قانون العقوبات",
        ["penal code", "criminal code", "crimes and penalties"], ["العقوبات", "الجرائم والعقوبات"]),
    ("criminal_procedure", "Criminal Procedure Code",         "قانون أصول المحاكمات الجزائية الإجراءات الجنائية",
        ["criminal procedure"], ["المحاكمات الجزائية", "الإجراءات الجنائية", "الإجراءات الجزائية"]),
    ("commercial_code",    "Commercial Code",                 "القانون التجاري قانون المعاملات التجارية",
        ["commercial code", "commercial transactions"], ["القانون التجاري", "التجارية"]),
    ("companies_law",      "Companies Law",                   "قانون الشركات نظام الشركات",
        ["companies law", "commercial companies"], ["الشركات"]),
    ("labor_law",          "Labor Law",                       "قانون العمل نظام العمل",
        ["labour law", "labor law"], ["قانون العمل", "نظام العمل"]),
    ("personal_status",    "Personal Status / Family Law",    "قانون الأحوال الشخصية",
        ["personal status", "family law"], ["الأحوال الشخصية"]),
    ("tax_law",            "Income Tax / VAT Law",            "قانون ضريبة الدخل القيمة المضافة",
        ["income tax", "value added tax", "vat"], ["ضريبة الدخل", "القيمة المضافة"]),
    ("arbitration_law",    "Arbitration Law",                 "قانون التحكيم نظام التحكيم",
        ["arbitration"], ["التحكيم"]),
    ("data_protection",    "Data Protection / Privacy Law",   "قانون حماية البيانات الشخصية",
        ["data protection", "personal data", "privacy law"], ["حماية البيانات", "البيانات الشخصية"]),
]

DOMAIN_RE = re.compile(r"(?:https?://)?(?:www\.)?([a-z0-9.\-]+\.[a-z]{2,})", re.I)
# domains that host CODIFIED law text rank above news-style gazettes
CODIFIED_HINTS = ("laws.", "boe", "legislation", "elaws", "lp.gov", "moj",
                  "birzeit", "muqtafi", "tashri", "legalaffairs", "qanon",
                  "qanoon", "dustur", "wipo", "faolex", "constituteproject")
RESTRICTED_RE = re.compile(r"(not allowed|restricted by policy|access to this page|"
                           r"\{\{|الاشتراك|اشترك|تسجيل الدخول|subscription|please log ?in|"
                           r"requires? a? ?subscription)", re.I)
NEWS_PATH = ("/news/", "details?p=", "/details", "privacy", "sector=", "newsletter")

def load_atlas():
    import yaml
    return yaml.safe_load(ATLAS.read_text())

def collect_strings(node, out):
    if isinstance(node, dict):
        for v in node.values(): collect_strings(v, out)
    elif isinstance(node, list):
        for v in node: collect_strings(v, out)
    elif isinstance(node, str):
        out.append(node)

def official_domains(jblock):
    strings = []
    collect_strings(jblock.get("authorities", {}), strings)
    collect_strings(jblock.get("unblock_hints", []), strings)
    doms = set()
    for s in strings:
        for m in DOMAIN_RE.findall(s):
            d = m.lower().strip(".")
            if d.count(".") >= 1 and not d.endswith(".pdf"):
                doms.add(d)
    pref = {d for d in doms if (".gov" in d or "boe." in d or "moj" in d
            or "legislation" in d or "gazette" in d or "majlis" in d
            or "knesset" in d or "parliament" in d or "birzeit" in d
            or "legalaffairs" in d or "qanon" in d or "qanoon" in d)}
    return sorted(pref) if pref else sorted(doms)

def search(q, include_domains, output="searchResults", depth="standard"):
    payload = {"q": q, "depth": depth, "outputType": output}
    if include_domains: payload["includeDomains"] = include_domains
    body = json.dumps(payload).encode()
    req = urllib.request.Request(URL, data=body, method="POST",
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())

def dom(u):
    try: return urllib.parse.urlparse(u).netloc.replace("www.", "")
    except: return u

def path_of(u):
    try: return urllib.parse.urlparse(u).path or "/"
    except: return "/"

def score_candidate(law, url, name, snippet):
    """Return (total, relevance, reasons[])."""
    text = f"{name} {snippet}".lower()
    _, en_name, _, en_kw, ar_kw = law
    rel = sum(1 for k in en_kw if k in text) + sum(1 for k in ar_kw if k in text)
    reasons = []
    score = rel * 3
    if rel: reasons.append(f"rel+{rel}")
    # document type
    u = url.lower(); p = path_of(url).lower()
    if u.endswith((".pdf", ".doc", ".docx")): score += 3; reasons.append("pdf+3")
    if any(t in u for t in ("lawdetails", "/laws/", "legislation", "regulations", "tashri")):
        score += 2; reasons.append("lawpath+2")
    if p in ("", "/"): score -= 3; reasons.append("homepage-3")
    if any(t in u for t in NEWS_PATH): score -= 3; reasons.append("newspath-3")
    # codified-domain rank
    d = dom(url).lower()
    if any(h in d for h in CODIFIED_HINTS): score += 2; reasons.append("codified+2")
    # access / restriction
    if RESTRICTED_RE.search(f"{name} {snippet}"): score -= 6; reasons.append("restricted-6")
    if len((snippet or "").strip()) < 20: score -= 2; reasons.append("thin-2")
    return score, rel, reasons

def best_from_results(law, results):
    best = None
    for r in results[:15]:
        url = r.get("url", ""); name = r.get("name", ""); snip = r.get("content", "") or ""
        sc, rel, why = score_candidate(law, url, name, snip)
        cand = {"url": url, "name": name[:120], "snippet": snip[:240],
                "domain": dom(url), "score": sc, "relevance": rel, "why": why}
        if best is None or sc > best["score"]:
            best = cand
    return best

def enrich(cc, jblock):
    country = jblock.get("country", cc)
    allow = official_domains(jblock)
    print(f"\n{'='*84}\n{cc} — {country}\n  allowlist: {allow}\n{'='*84}")
    entries = []
    for law in CORE_LAWS:
        key, en_name, ar_phrase, _, _ = law
        q = f"{country} {en_name} {ar_phrase} official full text"
        used = "standard"
        try:
            res = search(q, allow, "searchResults", "standard")
            results = res.get("results", [])
            if not results:
                used = "deep"; res = search(q, allow, "searchResults", "deep")
                results = res.get("results", [])
            best = best_from_results(law, results) if results else None
        except Exception as e:
            print(f"  [{key}] ERROR {e}")
            entries.append({"law_key": key, "law_name": en_name, "accepted": False, "error": str(e)})
            continue

        accepted = bool(best and best["score"] >= ACCEPT and best["relevance"] >= 1)
        citation = ""
        if not accepted:  # fallback: constrained sourcedAnswer to recover a real citation
            try:
                fa = search(f"What is the official {en_name} of {country}? Give the exact law "
                            f"number and year and the official source URL.", allow,
                            "sourcedAnswer", "standard")
                citation = (fa.get("answer", "") or "")[:200]
                fbest = best_from_results(law, fa.get("sources", []))
                if fbest and fbest["score"] >= ACCEPT and fbest["relevance"] >= 1:
                    best, accepted, used = fbest, True, "sourcedAnswer"
            except Exception:
                pass

        mark = "✅" if accepted else "❌"
        dshow = best["domain"] if best else "-"
        sshow = best["score"] if best else "-"
        print(f"  {mark} {key:<18} score={sshow:>3} {dshow}")
        e = {"law_key": key, "law_name": en_name, "accepted": accepted,
             "depth_used": used, "query": q, "discovered_at": datetime.date.today().isoformat()}
        if best:
            e.update({"official_url": best["url"], "source_domain": best["domain"],
                      "source_name": best["name"], "snippet": best["snippet"],
                      "score": best["score"], "relevance": best["relevance"], "why": best["why"]})
        if citation: e["fallback_citation"] = citation
        entries.append(e)
        time.sleep(0.3)
    acc = sum(1 for e in entries if e.get("accepted"))
    print(f"  --> {acc}/{len(CORE_LAWS)} laws ACCEPTED (precision-scored)")
    return {"cc": cc, "country": country, "allowlist": allow,
            "accepted": acc, "total": len(CORE_LAWS), "laws": entries}

def main():
    import yaml
    if not KEY: sys.exit("set LINKUP_KEY env var")
    atlas = load_atlas()
    args = sys.argv[1:] or ["AE", "LB", "SA"]
    targets = list(atlas.keys()) if args == ["all"] else [a.upper() for a in args]
    OUTDIR.mkdir(exist_ok=True)
    summary = []
    for cc in targets:
        if cc not in atlas: print(f"skip {cc}"); continue
        out = enrich(cc, atlas[cc])
        (OUTDIR / f"{cc}-laws.candidates.yaml").write_text(
            yaml.safe_dump(out, allow_unicode=True, sort_keys=False))
        summary.append(out)
    print(f"\n\n{'#'*84}\nSUMMARY (precision-scored)\n{'#'*84}")
    for s in summary:
        print(f"  {s['cc']}  {s['accepted']:>2}/{s['total']}  accepted  ({s['country']})")
    tf = sum(s["accepted"] for s in summary); tt = sum(s["total"] for s in summary)
    print(f"  TOTAL: {tf}/{tt} ({100*tf//max(tt,1)}%) accepted   staged in {OUTDIR}")

if __name__ == "__main__":
    main()
