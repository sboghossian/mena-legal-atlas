#!/usr/bin/env python3
"""Two-panel MENA map: where the law LIVES (source coverage) vs where you can REACH it."""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ATLAS = HERE.parent / "phase-1-atlas" / "mena-legal-atlas.json"
TOPO = HERE / "countries-50m.json"

ID2CC = {12:"DZ",48:"BH",174:"KM",262:"DJ",818:"EG",368:"IQ",400:"JO",414:"KW",
         422:"LB",434:"LY",478:"MR",504:"MA",512:"OM",275:"PS",634:"QA",682:"SA",
         706:"SO",729:"SD",760:"SY",788:"TN",784:"AE",887:"YE",364:"IR",376:"IL",792:"TR"}

atlas = json.load(open(ATLAS))
data = {}
cov_complete = tw = tb = 0
for cc, e in atlas.items():
    a = e.get("authorities", {}) or {}
    cov = sum([bool(a.get("official_gazette")), bool(a.get("consolidated")),
               bool(a.get("apex_courts")),
               bool(a.get("key_regulators")) or bool(e.get("additional_sources")),
               any(x.get("law_key") == "constitution" for x in (e.get("key_legislation") or []))])
    work = (e.get("worldwidelaw_reconciled", {}) or {}).get("working", 0)
    blok = (e.get("worldwidelaw_reconciled", {}) or {}).get("blocked", 0)
    tw += work; tb += blok
    cov_tier = "hi" if cov >= 5 else ("mid" if cov >= 3 else "lo")
    reach_tier = "hi" if work >= 4 else ("mid" if work >= 1 else "lo")
    if cov >= 5: cov_complete += 1
    data[cc] = {"country": e.get("country", cc), "cov": cov_tier, "reach": reach_tier}

cov_pct = round(100 * cov_complete / 25)          # 80
reach_pct = round(100 * tw / max(tw + tb, 1))     # 36
topo = json.load(open(TOPO))

html = """<!DOCTYPE html><html><head><meta charset="utf-8">
<script src="./d3.v7.min.js"></script><script src="./topojson-client.min.js"></script>
<style>html,body{margin:0;background:#0b1020;}
#stage{width:1840px;height:1040px;font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;}</style>
</head><body><div id="stage"><svg id="m" width="1840" height="1040"></svg></div>
<script>
const TOPO=__TOPO__, DATA=__DATA__, ID2CC=__ID2CC__;
const W=1840,H=1040;
const COL={hi:"#2fa36b",mid:"#e0922c",lo:"#c0203f"};
const svg=d3.select("#m");
svg.append("rect").attr("width",W).attr("height",H).attr("fill","#0b1020");
const countries=topojson.feature(TOPO,TOPO.objects.countries).features;
countries.forEach(f=>f.cc=ID2CC[+f.id]||null);
const menaFit=countries.filter(f=>f.cc&&DATA[f.cc]&&f.cc!=="KM");

// title
svg.append("text").attr("x",60).attr("y",60).attr("fill","#fff").attr("font-size","42px")
  .attr("font-weight","800").text("Where MENA law lives — and where you can actually reach it");
svg.append("text").attr("x",60).attr("y",94).attr("fill","#9fb0cc").attr("font-size","19px")
  .text("MENA Legal Data Atlas · 25 jurisdictions · the gap between mapping the law and retrieving it");

const PANELS=[
 {x0:60,x1:900, label:"WHERE THE LAW LIVES", sub:"official sources mapped across all 5 categories",
  big:"__COVPCT__%", bigsub:"jurisdictions complete", metric:"cov",
  legend:[["hi","all 5 categories"],["mid","3–4 categories"],["lo","≤2 categories"]]},
 {x0:940,x1:1780, label:"WHERE YOU CAN REACH IT", sub:"official sources that produce machine-readable data",
  big:"__REACHPCT__%", bigsub:"of sources produce data", metric:"reach",
  legend:[["hi","4+ working sources"],["mid","1–3 working"],["lo","0 — online but unreachable"]]},
];

const defs=svg.append("defs");
PANELS.forEach((p,i)=>{
  defs.append("clipPath").attr("id","clip"+i).append("rect")
    .attr("x",p.x0-6).attr("y",286).attr("width",p.x1-p.x0+12).attr("height",612);
  // header
  svg.append("text").attr("x",p.x0).attr("y",150).attr("fill","#cdd8ea").attr("font-size","17px")
    .attr("font-weight","700").attr("letter-spacing","1.5px").text(p.label);
  svg.append("text").attr("x",p.x0).attr("y",174).attr("fill","#7e8db0").attr("font-size","14px").text(p.sub);
  svg.append("text").attr("x",p.x1).attr("y",168).attr("text-anchor","end").attr("fill","#fff")
    .attr("font-size","58px").attr("font-weight","800").text(p.big);
  svg.append("text").attr("x",p.x1).attr("y",192).attr("text-anchor","end").attr("fill","#9fb0cc")
    .attr("font-size","14px").text(p.bigsub);
  // legend
  const lg=svg.append("g").attr("transform",`translate(${p.x0},206)`);
  p.legend.forEach((it,i)=>{const r=lg.append("g").attr("transform",`translate(${i*0},${i*22})`);
    r.append("rect").attr("width",14).attr("height",14).attr("rx",3).attr("fill",COL[it[0]]);
    r.append("text").attr("x",22).attr("y",12).attr("fill","#cdd8ea").attr("font-size","13.5px").text(it[1]);});
  // map
  const proj=d3.geoMercator().fitExtent([[p.x0+10,300],[p.x1-10,892]],
    {type:"FeatureCollection",features:menaFit});
  const path=d3.geoPath(proj);
  const g=svg.append("g").attr("clip-path",`url(#clip${i})`);
  g.selectAll("path.bg").data(countries.filter(f=>!(f.cc&&DATA[f.cc])))
    .join("path").attr("d",path).attr("fill","#161d2e").attr("stroke","#0b1020").attr("stroke-width",0.4);
  g.selectAll("path.mn").data(countries.filter(f=>f.cc&&DATA[f.cc]))
    .join("path").attr("d",path).attr("fill",f=>COL[DATA[f.cc][p.metric]])
    .attr("stroke","rgba(255,255,255,.28)").attr("stroke-width",0.7);
  // Comoros marker
  const c=proj([44.3,-11.7]);
  if(c){g.append("circle").attr("cx",c[0]).attr("cy",c[1]).attr("r",5).attr("fill",COL[DATA.KM[p.metric]])
        .attr("stroke","rgba(255,255,255,.4)");
        g.append("text").text("KM").attr("x",c[0]+9).attr("y",c[1]+4).attr("fill","rgba(255,255,255,.7)").attr("font-size","11px");}
});

// footer benchmark band
svg.append("rect").attr("x",0).attr("y",H-92).attr("width",W).attr("height",92).attr("fill","#070b16");
svg.append("text").attr("x",60).attr("y",H-58).attr("fill","#cdd8ea").attr("font-size","15px").attr("font-weight","700")
  .attr("letter-spacing","1px").text("BENCHMARK · MENA legal-source coverage");
const bench=[
  ["Legal Data Hunter (global crawler)","163 MENA sources · 41% working · 56% complete globally"],
  ["MENA Legal Atlas (this map)","+233 official sources · 152 new to LDH · 80% jurisdiction coverage"],
];
bench.forEach((b,i)=>{const y=H-32+i*0; const x=60+i*820;
  svg.append("text").attr("x",x).attr("y",H-34).attr("fill","#9fb0cc").attr("font-size","13px").attr("font-weight","700").text(b[0]);
  svg.append("text").attr("x",x).attr("y",H-16).attr("fill","#fff").attr("font-size","14px").text(b[1]);});
svg.append("text").attr("x",W-60).attr("y",H-34).attr("text-anchor","end").attr("fill","#cdd8ea")
  .attr("font-size","14px").attr("font-weight","700").text("github.com/sboghossian/mena-legal-atlas");
svg.append("text").attr("x",W-60).attr("y",H-16).attr("text-anchor","end").attr("fill","#7e8db0")
  .attr("font-size","12px").text("Stephane Boghossian · HAQQ Legal AI · data 2026-05-22");
document.title="ready";
</script></body></html>"""

html = (html.replace("__TOPO__", json.dumps(topo)).replace("__DATA__", json.dumps(data, ensure_ascii=False))
            .replace("__ID2CC__", json.dumps(ID2CC)).replace("__COVPCT__", str(cov_pct))
            .replace("__REACHPCT__", str(reach_pct)))
(HERE / "coverage-map.html").write_text(html)
print(f"wrote coverage-map.html | coverage={cov_pct}% reach={reach_pct}% complete={cov_complete}/25")
