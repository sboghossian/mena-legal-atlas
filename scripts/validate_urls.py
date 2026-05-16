#!/usr/bin/env python3
"""
Validation pass: pull every URL from atlas.yaml, check liveness with HEAD
(falling back to GET), and emit a status report. Updates atlas.yaml in place
with `url_check` blocks per source.

Status codes we record:
  live              200/301/302
  forbidden_403     Cloudflare/WAF likely — content may still exist
  not_found_404
  server_error_5xx
  timeout
  dns_error
  unknown
"""
from __future__ import annotations

import concurrent.futures
import datetime
import json
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "phase-1-atlas" / "atlas.yaml"
REPORT = ROOT / "phase-1-atlas" / "url-validation-report.md"

UA = "Mozilla/5.0 (compatible; MENA-Atlas-Validator/1.0; +https://github.com/sboghossian/mena-legal-atlas)"
TIMEOUT = 15


def check(url: str) -> tuple[str, int | None, str]:
    if not url or not url.startswith(("http://", "https://")):
        return ("unknown", None, "not_an_http_url")
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            return ("live", resp.status, "")
    except urllib.error.HTTPError as e:
        # Many gazette servers reject HEAD; retry GET
        if e.code in (405, 501):
            try:
                req2 = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req2, timeout=TIMEOUT, context=ctx) as r2:
                    return ("live", r2.status, "via_get")
            except Exception as e2:
                return ("unknown", None, f"get_fallback_failed:{type(e2).__name__}")
        if e.code == 403:
            return ("forbidden_403", 403, e.reason or "")
        if e.code == 404:
            return ("not_found_404", 404, e.reason or "")
        if 500 <= e.code < 600:
            return ("server_error_5xx", e.code, e.reason or "")
        return ("unknown", e.code, e.reason or "")
    except urllib.error.URLError as e:
        reason = str(e.reason)
        if "timed out" in reason.lower():
            return ("timeout", None, reason)
        if isinstance(e.reason, socket.gaierror):
            return ("dns_error", None, reason)
        return ("unknown", None, reason)
    except socket.timeout:
        return ("timeout", None, "")
    except Exception as e:
        return ("unknown", None, f"{type(e).__name__}:{e}")


def collect_urls(atlas: dict) -> list[tuple[str, str, str]]:
    """Return [(cc, label, url), ...]."""
    out: list[tuple[str, str, str]] = []
    for cc, entry in atlas.items():
        auth = entry.get("authorities", {}) or {}
        og = auth.get("official_gazette") or {}
        if og.get("url"):
            out.append((cc, f"gazette:{og.get('name','?')}", og["url"]))
        for c in (auth.get("consolidated") or []):
            if c.get("url"):
                out.append((cc, f"consolidated:{c.get('name','?')}", c["url"]))
    return out


def main() -> None:
    atlas = yaml.safe_load(ATLAS.read_text())
    urls = collect_urls(atlas)
    print(f"Checking {len(urls)} URLs across {len(atlas)} jurisdictions...", file=sys.stderr)

    results: dict[str, tuple[str, int | None, str]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        future_to_key = {
            ex.submit(check, url): (cc, label, url)
            for (cc, label, url) in urls
        }
        for fut in concurrent.futures.as_completed(future_to_key):
            cc, label, url = future_to_key[fut]
            status, code, detail = fut.result()
            results[url] = (status, code, detail)
            mark = {
                "live": "OK",
                "forbidden_403": "WAF",
                "not_found_404": "404",
                "server_error_5xx": "5xx",
                "timeout": "TO",
                "dns_error": "DNS",
            }.get(status, "??")
            print(f"  [{mark}] {cc:3s} {url}", file=sys.stderr)

    # --- Bucket and report ---
    buckets: dict[str, list[tuple[str, str, str, int | None, str]]] = {}
    for cc, label, url in urls:
        status, code, detail = results[url]
        buckets.setdefault(status, []).append((cc, label, url, code, detail))

    today = datetime.date.today().isoformat()
    lines: list[str] = []
    lines.append("# URL Validation Report")
    lines.append("")
    lines.append(f"Run date: **{today}**  ·  Checked: **{len(urls)}** URLs across "
                 f"**{len(atlas)}** jurisdictions.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---:|")
    for s in ("live", "forbidden_403", "not_found_404", "server_error_5xx",
              "timeout", "dns_error", "unknown"):
        if buckets.get(s):
            lines.append(f"| {s} | {len(buckets[s])} |")
    lines.append("")
    lines.append("> `forbidden_403` typically means a WAF (Cloudflare, Azure) is blocking "
                 "the user-agent — the content is usually live but unreachable from non-"
                 "interactive clients. `dns_error` and `timeout` are real outages.")
    lines.append("")

    for status in ("dns_error", "timeout", "not_found_404", "server_error_5xx",
                   "forbidden_403", "unknown", "live"):
        rows = buckets.get(status) or []
        if not rows:
            continue
        lines.append(f"## {status} ({len(rows)})")
        lines.append("")
        lines.append("| CC | Source | URL | Code | Detail |")
        lines.append("|---|---|---|---:|---|")
        for cc, label, url, code, detail in sorted(rows):
            lines.append(f"| {cc} | {label} | {url} | {code if code else ''} | {detail[:80]} |")
        lines.append("")

    REPORT.write_text("\n".join(lines))
    print(f"\nWrote: {REPORT}", file=sys.stderr)

    # --- Annotate atlas.yaml in place ---
    for cc, entry in atlas.items():
        auth = entry.get("authorities", {}) or {}
        og = auth.get("official_gazette") or {}
        if og.get("url"):
            status, code, _ = results[og["url"]]
            og["url_check"] = {"status": status, "code": code, "checked_at": today}
        for c in (auth.get("consolidated") or []):
            if c.get("url"):
                status, code, _ = results[c["url"]]
                c["url_check"] = {"status": status, "code": code, "checked_at": today}

    ATLAS.write_text(yaml.safe_dump(atlas, sort_keys=False, allow_unicode=True, width=120))
    print(f"Annotated: {ATLAS}", file=sys.stderr)

    # --- Print summary stats ---
    print("\n=== Summary ===")
    for s in ("live", "forbidden_403", "dns_error", "timeout", "not_found_404",
              "server_error_5xx", "unknown"):
        if buckets.get(s):
            print(f"  {s:20s} {len(buckets[s])}")


if __name__ == "__main__":
    main()
