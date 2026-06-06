#!/usr/bin/env python3
"""Coverage scorecard: a heatmap table over the public scoring axes.

Reads data/coverage-scores.json (produced by scripts/score_coverage.py) and renders
a self-contained, dependency-free HTML table — ICP markets first, then the rest.

Public axes only (codifiability is intentionally excluded). Reachability is shown by
working-source TIER (hi/mid/lo), not raw %, to avoid the small-denominator trap
(a jurisdiction with 1 working / 0 blocked sources is not "100% reachable").
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
SCORES = ROOT / "data" / "coverage-scores.json"
OUT = HERE / "coverage-scorecard.html"

ICP = ["AE", "SA", "EG", "JO", "LB"]

LANG_LABEL = {
    "arabic_native": "Arabic only", "bilingual_ar_en": "Arabic + English",
    "bilingual_ar_fr": "Arabic + French", "english_available": "English avail.",
    "french_influenced": "French-influenced", "hebrew_native": "Hebrew",
    "persian_native": "Persian", "turkish_native": "Turkish", "other": "Other",
}

DEPTH_COLOR = {5: "#1f8f4e", 4: "#6b8f1f", 3: "#8f7a1f", 2: "#8f4a1f", 1: "#8f1f1f", 0: "#5a1313"}
REACH_COLOR = {"hi": "#1f8f4e", "mid": "#8f7a1f", "lo": "#8f1f1f"}
REACH_LABEL = {"hi": "Reachable", "mid": "Partial", "lo": "Blocked"}
REFORM_COLOR = {"yes": "#1f8f4e", "no": "#3a4256", "unclear": "#8f7a1f"}
REFORM_LABEL = {"yes": "Active 25–26", "no": "Stable", "unclear": "Unverified"}


def esc(s):
    return (str(s or "")).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def row_html(r, icp):
    cc = r["cc"]
    depth = r["corpus_depth"]
    reach = r["reachability"]
    rec = r.get("recency", {}) or {}
    reform = rec.get("recent_major_reform", "unclear")
    laws = ", ".join(rec.get("laws", []) or [])
    srcs = rec.get("sources", []) or []
    src_link = f' · <a href="{esc(srcs[0])}" target="_blank">source</a>' if srcs else ""
    lang = LANG_LABEL.get(r.get("language_regime"), r.get("language_regime") or "—")
    note = esc(r.get("language_note"))
    star = " ★" if icp else ""
    rclass = ' class="icp"' if icp else ""
    reform_title = esc(laws) if laws else "no clearly-sourced 2025–26 reform"
    return f"""<tr{rclass}>
  <td class="cc">{cc}{star}</td>
  <td class="country">{esc(r.get('country'))}</td>
  <td><span class="pill" style="background:{DEPTH_COLOR.get(depth,'#5a1313')}">{depth}/5</span></td>
  <td><span class="pill" style="background:{REACH_COLOR[reach['tier']]}" title="{reach['working']} working / {reach['blocked']} blocked sources">{REACH_LABEL[reach['tier']]}</span>
      <span class="sub">{reach['working']}w/{reach['blocked']}b</span></td>
  <td class="lang" title="{note}">{esc(lang)}</td>
  <td><span class="pill" style="background:{REFORM_COLOR.get(reform,'#3a4256')}" title="{reform_title}">{REFORM_LABEL.get(reform, reform)}</span>{src_link}</td>
</tr>"""


def main():
    rows = json.load(open(SCORES))
    by_cc = {r["cc"]: r for r in rows}
    ordered = [by_cc[c] for c in ICP if c in by_cc] + \
              [r for r in rows if r["cc"] not in ICP]

    reachable = sum(1 for r in rows if r["reachability"]["tier"] == "hi")
    blocked = sum(1 for r in rows if r["reachability"]["tier"] == "lo")
    active = sum(1 for r in rows if (r.get("recency") or {}).get("recent_major_reform") == "yes")
    deep = sum(1 for r in rows if r["corpus_depth"] >= 5)

    body = "\n".join(row_html(r, r["cc"] in ICP) for r in ordered)
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MENA Legal Atlas — Coverage Scorecard</title>
<style>
  :root {{ color-scheme: dark; }}
  body {{ margin:0; background:#0b1020; color:#e6ebf5;
    font:15px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; }}
  .wrap {{ max-width:1040px; margin:0 auto; padding:40px 24px 80px; }}
  h1 {{ font-size:26px; font-weight:800; margin:0 0 6px; }}
  .lede {{ color:#9aa6bf; margin:0 0 28px; max-width:680px; }}
  .stats {{ display:flex; flex-wrap:wrap; gap:14px; margin-bottom:30px; }}
  .stat {{ background:#121a2e; border:1px solid #1e2942; border-radius:12px; padding:14px 18px; min-width:120px; }}
  .stat b {{ display:block; font-size:28px; font-weight:800; }}
  .stat span {{ color:#9aa6bf; font-size:13px; }}
  table {{ width:100%; border-collapse:collapse; font-size:14px; }}
  th {{ text-align:left; color:#9aa6bf; font-weight:600; font-size:12px; text-transform:uppercase;
    letter-spacing:.04em; padding:8px 10px; border-bottom:1px solid #1e2942; }}
  td {{ padding:9px 10px; border-bottom:1px solid #141d31; vertical-align:middle; }}
  tr.icp {{ background:#101a30; }}
  tr.icp .cc {{ color:#ffd56b; }}
  .cc {{ font-weight:700; font-family:ui-monospace,Menlo,monospace; white-space:nowrap; }}
  .country {{ color:#cdd6ea; }}
  .pill {{ display:inline-block; padding:2px 9px; border-radius:999px; color:#fff;
    font-size:12px; font-weight:700; }}
  .sub {{ color:#6b7691; font-size:11px; margin-left:5px; }}
  .lang {{ color:#cdd6ea; }}
  a {{ color:#6ba8ff; text-decoration:none; }} a:hover {{ text-decoration:underline; }}
  .foot {{ color:#6b7691; font-size:12px; margin-top:26px; line-height:1.6; }}
  .foot code {{ background:#121a2e; padding:1px 5px; border-radius:4px; }}
</style></head><body><div class="wrap">
<h1>MENA Legal Atlas — Coverage Scorecard</h1>
<p class="lede">Where legal AI can actually operate across {len(rows)} MENA jurisdictions.
The sources are mapped almost everywhere — but mapped is not the same as <em>reachable</em>,
<em>current</em>, or <em>in your language</em>. ★ = HAQQ ICP markets.</p>
<div class="stats">
  <div class="stat"><b>{deep}/{len(rows)}</b><span>full 5-category source depth</span></div>
  <div class="stat"><b>{reachable}</b><span>actually reachable (4+ live sources)</span></div>
  <div class="stat"><b>{blocked}</b><span>fully blocked (0 live sources)</span></div>
  <div class="stat"><b>{active}</b><span>active 2025–26 reform (sourced)</span></div>
</div>
<table>
<thead><tr>
  <th>CC</th><th>Jurisdiction</th><th>Source depth</th>
  <th>Reachability</th><th>Language regime</th><th>Recency</th>
</tr></thead>
<tbody>
{body}
</tbody>
</table>
<p class="foot">
  <b>Source depth</b>: count of the 5 source categories present (gazette, consolidated, apex courts,
  regulators/sources, constitution) — same definition as the two-panel map.<br>
  <b>Reachability</b>: working-source <em>tier</em> (hi=4+, mid=1–3, lo=0) from worldwidelaw collection
  results — deliberately not raw %, since 1 working / 0 blocked is not "100% reachable".<br>
  <b>Language regime</b> &amp; <b>Recency</b>: recency checked via Linkup constrained to each
  jurisdiction's official domains; every "active reform" carries its source link and is only marked
  <em>yes</em> when the sources support it (else <em>Unverified</em>). Generated by
  <code>scripts/score_coverage.py</code> + <code>viz/build_scorecard.py</code>.
</p>
</div></body></html>"""
    OUT.write_text(html)
    print(f"wrote {OUT}")
    print(f"depth>=5: {deep}/{len(rows)} | reachable(hi): {reachable} | blocked(lo): {blocked} | active reform: {active}")


if __name__ == "__main__":
    main()
