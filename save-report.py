#!/usr/bin/env -S uv run --quiet
# /// script
# requires-python = ">=3.10"
# dependencies = ["markdown>=3.5"]
# ///
"""
save-report.py — render a CoinPicks markdown research report to a PDF and file it
in the user's "Altcoin Database" folder (their local version of the Notion tiered DBs).

Usage (Claude runs this for the user):
    uv run save-report.py <report.md> --ticker SOGNI --name "Sogni AI" [--dir "..."]

    The dependency is declared in the PEP-723 header above, so uv installs it on first run.
    Plain `python3 save-report.py` fails with a clear message pointing back here.

How it works:
  1. Markdown -> styled HTML (large, readable fonts; yellow section headers like the Notion entries).
  2. HTML -> PDF using headless Chrome / Edge / Chromium (every engine user has Chrome, since the
     Claude for Chrome extension requires it). Falls back to leaving a print-ready HTML file if no
     browser binary is found.
  3. Files the result in "~/Altcoin Database/<TICKER> <Name>.pdf" by default.

This is intentionally dependency-light: only the pure-Python `markdown` package, provided by uv.
"""
import argparse
import os
import platform
import re
import shutil
import subprocess
import sys

HTML_TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>
  @page {{ size: Letter; margin: 0.6in; }}
  body {{ font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
         font-size: 14pt; line-height: 1.5; color: #1a1a1a; max-width: 100%; }}
  h1 {{ font-size: 21pt; margin: 20px 0 6px; line-height: 1.25; }}
  h2 {{ font-size: 18pt; margin: 16px 0 6px; }}
  h3 {{ font-size: 15pt; margin: 14px 0 4px; }}
  p, li {{ font-size: 14pt; }}
  .hl {{ background: #fff2a8; padding: 1px 5px; border-radius: 3px; }}
  a {{ color: #1a57c2; word-break: break-word; }}
  hr {{ border: none; border-top: 1px solid #dddddd; margin: 16px 0; }}
  code {{ background: #f3f3f3; padding: 1px 4px; border-radius: 3px; font-size: 12pt; }}
  blockquote {{ border-left: 3px solid #f9d54a; margin: 8px 0; padding: 2px 14px;
               color: #333; font-style: italic; }}
  ul {{ margin: 6px 0 6px 0; }}
  /* Tables. The `extra` extension already emits real <table> markup; before 2026-08-30
     nothing styled it, so every comparison table in a report printed as borderless,
     cramped text. Reports are the deliverable buyers keep, so this matters. */
  table {{ border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 12pt;
          page-break-inside: avoid; }}
  th, td {{ border: 1px solid #d9d9d9; padding: 7px 10px; text-align: left;
           vertical-align: top; }}
  th {{ background: #fff2a8; font-weight: 600; font-size: 12pt; }}
  tbody tr:nth-child(even) {{ background: #fafafa; }}
  td code {{ font-size: 11pt; }}
</style></head><body>
{body}
</body></html>"""


def md_to_html(md_text):
    try:
        import markdown  # declared in the PEP-723 header above, so `uv run` provides it
    except ModuleNotFoundError:
        sys.exit(
            "This script needs the 'markdown' package, which plain python3 does not have.\n"
            "Run it through uv instead, which installs it automatically:\n\n"
            "    uv run save-report.py <report.md> --ticker TAO --name \"Bittensor\"\n\n"
            "Nothing is broken and nothing needs installing by hand: uv reads the dependency\n"
            "list at the top of this file and fetches it for you."
        )
    # The reports use Notion's `<span color="yellow_bg">` highlight syntax. Turn it into a real
    # highlight so the section headers render yellow in the PDF, like the Notion entries.
    md_text = md_text.replace('<span color="yellow_bg">', '<span class="hl">')
    return markdown.markdown(md_text, extensions=["extra", "sane_lists", "nl2br"])


def find_browser():
    """Locate a Chrome/Edge/Chromium binary for headless PDF printing."""
    sysname = platform.system()
    candidates = []
    if sysname == "Darwin":
        candidates = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
            "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        ]
    elif sysname == "Windows":
        pf = os.environ.get("PROGRAMFILES", r"C:\Program Files")
        pfx = os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)")
        la = os.environ.get("LOCALAPPDATA", "")
        candidates = [
            pf + r"\Google\Chrome\Application\chrome.exe",
            pfx + r"\Google\Chrome\Application\chrome.exe",
            (la + r"\Google\Chrome\Application\chrome.exe") if la else "",
            pf + r"\Microsoft\Edge\Application\msedge.exe",
            pfx + r"\Microsoft\Edge\Application\msedge.exe",
        ]
    else:  # Linux
        for n in ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge"]:
            p = shutil.which(n)
            if p:
                candidates.append(p)
    for c in candidates:
        if c and os.path.exists(c):
            return c
    for n in ["google-chrome", "chrome", "chromium", "msedge"]:
        p = shutil.which(n)
        if p:
            return p
    return None


def render_pdf(browser, html_path, pdf_path):
    """Try newer then older headless flags; return True on success."""
    src = "file://" + os.path.abspath(html_path)
    for flags in (["--headless=new"], ["--headless"]):
        try:
            subprocess.run(
                [browser, *flags, "--disable-gpu", "--no-pdf-header-footer",
                 f"--print-to-pdf={pdf_path}", src],
                check=True, timeout=120, capture_output=True,
            )
            if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
                return True
        except Exception:
            continue
    return False


def safe_name(s):
    s = re.sub(r"[^\w \-().$]", "", s).strip()
    return s or "report"


def main():
    ap = argparse.ArgumentParser(description="Save a CoinPicks research report as a PDF in the Altcoin Database folder.")
    ap.add_argument("report", help="Path to the markdown report file.")
    ap.add_argument("--ticker", default="", help="Ticker, e.g. SOGNI (used in the filename).")
    ap.add_argument("--name", default="", help="Project name, e.g. 'Sogni AI'.")
    ap.add_argument("--dir", default="", help="Target folder. Default: ~/Altcoin Database")
    args = ap.parse_args()

    if not os.path.exists(args.report):
        sys.exit(f"Report file not found: {args.report}")

    with open(args.report, encoding="utf-8") as f:
        md_text = f.read()

    title = (f"{args.ticker} {args.name}").strip() or os.path.splitext(os.path.basename(args.report))[0]
    body = md_to_html(md_text)
    htmldoc = HTML_TEMPLATE.format(title=title, body=body)

    out_dir = args.dir or os.path.join(os.path.expanduser("~"), "Altcoin Database")
    os.makedirs(out_dir, exist_ok=True)

    base = safe_name(title)
    html_path = os.path.join(out_dir, base + ".html")
    pdf_path = os.path.join(out_dir, base + ".pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(htmldoc)

    browser = find_browser()
    if browser and render_pdf(browser, html_path, pdf_path):
        os.remove(html_path)
        print(f"PDF saved: {pdf_path}")
        return

    print(f"HTML saved (no browser found for auto-PDF): {html_path}")
    print("Open it in any browser and use Print > Save as PDF, or ask Claude to render it for you.")


if __name__ == "__main__":
    main()
