# viz — coverage map + benchmark

Self-contained data-viz + benchmark tooling for the atlas. Large inputs (d3, geometry,
LDH snapshot) are **not committed** — they're regenerable. Only the script files and the
rendered `coverage-map.png` are tracked.

## Regenerate

```bash
cd viz
curl -sL https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js -o d3.v7.min.js
curl -sL https://cdn.jsdelivr.net/npm/topojson-client@3/dist/topojson-client.min.js -o topojson-client.min.js
curl -sL https://cdn.jsdelivr.net/npm/world-atlas@2/countries-50m.json -o countries-50m.json
curl -sL https://zachlaik.github.io/LegalDataHunter/status.json -o ldh-status.json   # Legal Data Hunter live coverage (public)

python3 build_map.py        # -> coverage-map.html
python3 benchmark_ldh.py    # -> ../phase-2-enrichment/BENCHMARK-vs-legal-data-hunter.md

# render to PNG (headless Chrome):
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --force-device-scale-factor=2 --window-size=1840,1040 \
  --screenshot="$PWD/coverage-map.png" "file://$PWD/coverage-map.html"
```

## Files

- `build_map.py` — two-panel MENA choropleth: *where the law lives* (source coverage) vs *where you can reach it* (reachability).
- `benchmark_ldh.py` — MENA Legal Atlas vs Legal Data Hunter, computed from LDH's live public `status.json`.
- `coverage-map.png` — committed artifact (the two-panel map).
