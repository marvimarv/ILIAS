#!/usr/bin/env python3
"""
Extrahiert stabile Feature-Wiki-URLs (wpage_XXX_1357) für alle Wiki-Seiten.

Strategie: Für jede Seite wird die Wiki-Seite per HTTP geladen und der Link
des Buttons „Link in Zwischenablage kopieren“ aus dem JavaScript (copyText)
ausgelesen – das ist die stabile URL.

1) Seitenliste: aus der Overview-HTML (gotoPage-Links) oder aus --pages.
2) Pro Seite: GET gotoPage-URL → im Response-HTML nach copyText("...wpage_XXX_1357") suchen.
3) Ergebnis: feature_wiki_wpage_ids.json

Verwendung:
  python extract_feature_wiki_wpage_ids.py [pfad/zur/Overview.html]
  python extract_feature_wiki_wpage_ids.py --pages "Taxonomy_Service,Forum,Accessibility"

Ausgabe: feature_wiki_wpage_ids.json im Skript-Verzeichnis.
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

# Regex: Permalink aus dem „Link in Zwischenablage kopieren“-Handler (copyText im JS)
PERMLINK_PATTERN = re.compile(
    r'copyText\s*\(\s*"(https:\\/\\/docu\.ilias\.de\\/go\\/wiki\\/wpage_(\d+)_1357)"\s*\)',
    re.IGNORECASE,
)
GOTO_PAGE_PATTERN = re.compile(
    r"cmd=gotoPage&ref_id=1357&page=([^&\"]+)",
    re.IGNORECASE,
)
STABLE_LINK_PATTERN = re.compile(
    r'href="https://docu\.ilias\.de/go/wiki/wpage_(\d+)_1357"[^>]*>([^<]+)</a>',
    re.IGNORECASE,
)

BASE_GOTO = (
    "https://docu.ilias.de/ilias.php"
    "?baseClass=ilwikihandlergui&cmdNode=14x:rn&cmdClass=ilobjwikigui"
    "&cmd=gotoPage&ref_id=1357&page={page}&from_page=Overview"
)
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_HTML = Path(__file__).resolve().parents[2] / "onlylocal" / "Seite: Feature Wiki: Overview: DOCU.html"
OUTPUT_JSON = SCRIPT_DIR / "feature_wiki_wpage_ids.json"
REQUEST_DELAY_S = 0.5


def link_text_to_page_param(text: str) -> str:
    """Link-Text → URL-page-Parameter (z.B. 'Taxonomy Service' → 'Taxonomy_Service')."""
    param = text.strip().replace(" ", "_")
    return urllib.parse.quote(param, safe="_")


def extract_page_names_from_html(html_path: Path) -> set:
    """Sammelt alle page= Werte aus gotoPage-Links in der Overview-HTML."""
    text = html_path.read_text(encoding="utf-8", errors="replace")
    return set(m.group(1) for m in GOTO_PAGE_PATTERN.finditer(text))


def extract_stable_links_from_html(html_path: Path) -> dict:
    """Liest bereits vorhandene wpage-Links aus der HTML-Datei (Sidebar)."""
    text = html_path.read_text(encoding="utf-8", errors="replace")
    mapping = {}
    for m in STABLE_LINK_PATTERN.finditer(text):
        wpage_id, link_text = int(m.group(1)), m.group(2)
        mapping[link_text_to_page_param(link_text)] = wpage_id
    return mapping


def fetch_permalink_from_page(page_param: str, opener: urllib.request.OpenerDirector) -> int | None:
    """
    Lädt die Wiki-Seite per gotoPage-URL und liest den Permalink
    aus dem Button „Link in Zwischenablage kopieren“ (copyText im HTML).
    """
    # page_param kann aus der HTML schon encodiert sein (z.B. Test_%26_Assessment)
    url = BASE_GOTO.format(page=page_param)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; ILIAS-maintenance-extractor/1.0)"})
        with opener.open(req, timeout=20) as r:
            html = r.read().decode("utf-8", errors="replace")
        match = PERMLINK_PATTERN.search(html)
        if match:
            return int(match.group(2))
    except Exception:
        pass
    return None


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Extrahiert stabile Feature-Wiki wpage-IDs.")
    parser.add_argument(
        "html_path",
        nargs="?",
        default=None,
        help="Pfad zur gespeicherten Overview-HTML (für Seitenliste + Sidebar-Links)",
    )
    parser.add_argument(
        "--pages",
        type=str,
        default=None,
        help="Komma-getrennte page-Parameter (z.B. Taxonomy_Service,Forum). Überschreibt Seitenliste aus HTML.",
    )
    parser.add_argument(
        "--no-fetch",
        action="store_true",
        help="Nur aus Overview-HTML extrahieren, keine Seiten per HTTP abfragen.",
    )
    args = parser.parse_args()

    html_path = Path(args.html_path) if args.html_path else DEFAULT_HTML
    mapping = {}

    if html_path.is_file():
        mapping.update(extract_stable_links_from_html(html_path))
        page_names = extract_page_names_from_html(html_path)
        if not args.pages:
            print(f"Seitenliste aus {html_path.name}: {len(page_names)} Einträge.")
    else:
        if not args.pages:
            print("Weder HTML-Datei gefunden noch --pages angegeben.", file=sys.stderr)
            return 1
        page_names = set()

    if args.pages:
        page_names = {p.strip() for p in args.pages.split(",") if p.strip()}
        print(f"Seitenliste aus --pages: {len(page_names)} Einträge.")

    if not args.no_fetch and page_names:
        opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
        total = len(page_names)
        for i, page_param in enumerate(sorted(page_names), 1):
            if page_param in mapping:
                continue
            wpage_id = fetch_permalink_from_page(page_param, opener)
            if wpage_id is not None:
                mapping[page_param] = wpage_id
                print(f"  [{i}/{total}] {page_param} → wpage_{wpage_id}_1357")
            else:
                print(f"  [{i}/{total}] {page_param} → (Permalink nicht gefunden)", file=sys.stderr)
            time.sleep(REQUEST_DELAY_S)

    OUTPUT_JSON.write_text(json.dumps(mapping, indent=2, sort_keys=True), encoding="utf-8")
    print(f"\nGespeichert: {OUTPUT_JSON} ({len(mapping)} Einträge)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
