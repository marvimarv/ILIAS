#!/usr/bin/env python3
"""
Tests für docs/development/maintenance.md:
- Alle Feature-Wiki-Links sind stabil (go/wiki/wpage_XXX_1357), keine gotoPage-URLs
- docu.ilias.de-Links nutzen erlaubte Formate (wiki, usr, pg)
- Komponenten-Blöcke sind vollständig (BEGIN/END, Pflicht-Authority-Zeilen)
- Optional: Abgleich mit maintenance_old.md (gleiche Komponenten, inhaltlich Maintainer etc.)

Ausführung:
  python test_maintenance_md.py              # nur Struktur/Links
  python test_maintenance_md.py --compare-old        # gleiche Komponenten (comment_name) in new
  python test_maintenance_md.py --compare-content    # Maintainer/Authorities pro Komponente old vs new
                                                     # (nur bei gleichem Komponentennamen; Abweichungen = FAIL)
"""

import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
MAINTENANCE_MD = REPO_ROOT / "docs" / "development" / "maintenance.md"
MAINTENANCE_OLD_MD = REPO_ROOT / "docs" / "development" / "maintenance_old.md"

# Erlaubte docu.ilias.de-Link-Formate
STABLE_WIKI_PATTERN = re.compile(r"https://docu\.ilias\.de/go/wiki/wpage_\d+_1357")
USER_LINK_PATTERN = re.compile(r"https://docu\.ilias\.de/go/usr/\d+")
PG_LINK_PATTERN = re.compile(r"https://docu\.ilias\.de/go/pg/\d+_\d+")
CAT_LINK_PATTERN = re.compile(r"https://docu\.ilias\.de/go/cat/\d+")
# Instabile / verbotene Links
GOTO_PAGE_PATTERN = re.compile(r"https://docu\.ilias\.de/ilias\.php\?[^)]*gotoPage")
ANY_DOCU_LINK = re.compile(r"https://docu\.ilias\.de/[^\s)\]]+")

COMPONENT_BLOCK = re.compile(r"\[//\]: # \(BEGIN (\w+)\)(.*?)\[//\]: # \(END \1\)", re.DOTALL)
REQUIRED_AUTHORITY_LINES = [
    "Authority to Sign off on Conceptual Changes",
    "Authority to Sign off on Code Changes",
    "Authority to Curate Test Cases",
    "Authority to (De-)Assign Authorities",
    "Assignee for Issues",
    "Assignee for Security Reports",
]


def test_no_unstable_wiki_links(content: str) -> list[str]:
    """Keine ilias.php?gotoPage-Links."""
    errors = []
    for m in GOTO_PAGE_PATTERN.finditer(content):
        errors.append(f"Instabiler Wiki-Link: {m.group(0)[:80]}...")
    return errors


def test_all_docu_links_stable(content: str) -> list[str]:
    """Alle docu.ilias.de-Links müssen erlaubte Formate haben (wiki: wpage_ nur)."""
    errors = []
    for m in ANY_DOCU_LINK.finditer(content):
        url = m.group(0).rstrip(")")
        if GOTO_PAGE_PATTERN.search(url):
            errors.append(f"Verbotener gotoPage-Link: {url[:90]}")
            continue
        if "/go/wiki/" in url and not re.search(r"/go/wiki/wpage_\d+_1357", url):
            errors.append(f"Wiki-Link nicht stabil (wpage_XXX_1357): {url[:90]}")
    return errors


def test_component_blocks_structure(content: str) -> list[str]:
    """Jeder Komponenten-Block (mit Component Folders) hat alle Pflicht-Zeilen."""
    errors = []
    for m in COMPONENT_BLOCK.finditer(content):
        comment_name, block = m.group(1), m.group(2)
        # Nur echte Komponenten-Einträge prüfen (mit *Component Folders:*), nicht z.B. "Authorities"-Intro
        if "*Component Folders:*" not in block:
            continue
        for line_label in REQUIRED_AUTHORITY_LINES:
            if line_label not in block:
                errors.append(f"Komponente {comment_name}: fehlende Zeile '{line_label}'")
    return errors


def test_component_blocks_balanced(content: str) -> list[str]:
    """BEGIN/END-Kommentare sind ausgeglichen."""
    begins = set(re.findall(r"\[//\]: # \(BEGIN (\w+)\)", content))
    ends = set(re.findall(r"\[//\]: # \(END (\w+)\)", content))
    missing_end = begins - ends
    missing_begin = ends - begins
    errors = []
    if missing_end:
        errors.append(f"BEGIN ohne END: {sorted(missing_end)}")
    if missing_begin:
        errors.append(f"END ohne BEGIN: {sorted(missing_begin)}")
    return errors


def normalize_component_name(name: str) -> str:
    """Komponentenname für Vergleich normalisieren (lowercase, keine Sonderzeichen inkl. Unicode-Bindestriche)."""
    if not name:
        return ""
    n = name.lower().strip()
    n = re.sub(r"[_\s\-\.&,()\u2010-\u2015]+", "", n)  # ASCII- und Unicode-Bindestriche (en-dash etc.)
    return n


def normalized_component_name_variants(name: str) -> set[str]:
    """Alle Vergleichsvarianten (z. B. 'X (aka Y)' → {norm(X), norm(Y)}; 'A, B and C' → norm(A and C))."""
    if not name:
        return set()
    variants = {normalize_component_name(name)}
    # "COPage (aka ILIAS Page Editor)" → auch "ILIAS Page Editor" normalisiert
    aka = re.search(r"\(aka\s+([^)]+)\)", name, re.IGNORECASE)
    if aka:
        variants.add(normalize_component_name(aka.group(1).strip()))
    # "Category, Category Reference and Repository" → "Category and Repository"
    if ", " in name and " and " in name:
        parts = [p.strip() for p in name.split(", ")]
        last = parts[-1]
        if " and " in last:
            last = last.split(" and ")[-1].strip()
        if parts[0] and last:
            variants.add(normalize_component_name(f"{parts[0]} and {last}"))
    # "X and Y Reference" → "X and Y" bzw. "X"
    if " and " in name and " reference" in name.lower():
        short = re.sub(r"\s+and\s+[\w\s]+reference\s*$", "", name, flags=re.IGNORECASE).strip()
        if short:
            variants.add(normalize_component_name(short))
    return variants


def normalize_authority_value(raw: str) -> str:
    """Wert einer Authority-Zeile vergleichbar machen: NONE/MISSING vereinheitlichen, Links → sortierte Link-Texte."""
    if not raw:
        return "NONE"
    raw = raw.replace("\n", " ").strip()
    upper = raw.upper()
    if upper in ("NONE", "MISSING") or "AUTHOR MISSING" in upper or "[MISSING]" in upper:
        return "NONE"
    # Alle [text](url) extrahieren, Text-Teile sortiert joinen
    links = re.findall(r"\[([^\]]+)\]\([^)]+\)", raw)
    if links:
        return ",".join(sorted(t.strip() for t in links))
    return raw.strip()[:80]


AUTHORITY_KEYS = [
    "conceptual",
    "code",
    "test_cases",
    "assign_authorities",
    "issues",
    "security_reports",
]
AUTHORITY_PATTERNS = [
    (r"\* Authority to Sign off on Conceptual Changes:(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|$)", "conceptual"),
    (r"\* Authority to Sign off on Code Changes:(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|$)", "code"),
    (r"\* Authority to Curate Test Cases:(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|$)", "test_cases"),
    (r"\* Authority to \(De-\)Assign Authorities:(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|$)", "assign_authorities"),
    (r"\* Assignee for Issues:(.*?)(?=\* Authority|\* Assignee for Security|\* Unit-specific|$)", "issues"),
    (r"\* Assignee for Security Reports:(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|$)", "security_reports"),
]


def parse_authorities_from_block(block: str) -> dict[str, str]:
    """Aus einem Komponenten-Block die 6 Authority-Werte (normalisiert) extrahieren."""
    out = {k: "NONE" for k in AUTHORITY_KEYS}
    for pattern, key in AUTHORITY_PATTERNS:
        m = re.search(pattern, block, re.DOTALL)
        if m:
            out[key] = normalize_authority_value(m.group(1))
    return out


def get_component_name_from_block(block: str) -> str:
    """Komponentenname aus Block: #### [Name](url) oder * **Name**."""
    m = re.search(r"####\s*\[([^\]]+)\]", block)
    if m:
        return m.group(1).strip()
    m = re.search(r"\* \*\*([^*]+)\*\*", block)
    if m:
        return m.group(1).strip()
    return ""


def extract_components_with_authorities(content: str, only_with_folders: bool = True) -> dict[str, dict]:
    """normalized_component_name -> {component_name, authorities dict}."""
    out = {}
    for m in COMPONENT_BLOCK.finditer(content):
        block = m.group(2)
        if only_with_folders and "*Component Folders:*" not in block:
            continue
        # Old-MD hat ggf. kein Component Folders, aber * **Name**
        name = get_component_name_from_block(block)
        if not name:
            continue
        norm = normalize_component_name(name)
        out[norm] = {
            "component_name": name,
            "authorities": parse_authorities_from_block(block),
        }
    return out


def extract_components_from_md(content: str) -> dict:
    """Comment_name -> {component_name, ...} aus maintenance.md."""
    out = {}
    for m in COMPONENT_BLOCK.finditer(content):
        comment_name = m.group(1)
        block = m.group(2)
        component_name = get_component_name_from_block(block)
        if not component_name and "*Component Folders:*" not in block:
            name_match = re.search(r"\* \*\*([^*]+)\*\*", block)
            component_name = name_match.group(1).strip() if name_match else ""
        out[comment_name] = {"component_name": component_name}
    return out


def _old_component_matched_in_new(old_variants: set[str], new_variants: set[str], min_substring_len: int = 8) -> bool:
    """Prüft, ob eine alte Komponente (via Varianten) in new vorkommt (exakt oder sinnvolles Substring)."""
    if old_variants & new_variants:
        return True
    for ov in old_variants:
        for nv in new_variants:
            if len(nv) >= min_substring_len and (nv in ov or ov in nv):
                return True
    return False


# Alte Komponenten, die in new in einem anderen Block aufgehen oder bewusst entfallen
OLD_COMPONENTS_MERGED_IN_NEW: set[str] = {
    "Data Protection",  # in new: Privacy… (BEGIN enthält Punkt, wird von COMPONENT_BLOCK nicht erfasst)
    "TermsOfService (aka Terms of Services)",
}

# Bekannte Umbenennungen/Strukturänderungen: alter Anzeigename → normalisierte Namen in maintenance.md
OLD_DISPLAY_NAME_ACCEPTED_NEW_NORMALIZED: dict[str, set[str]] = {
    "Category, Category Reference and Repository": {"categoryandrepository"},
    "Chatroom": {"chat"},
    "ECS Interface": {"ecsinterface", "ecsinterfaceelearningcommunityserver"},
    "Feed (aka Web Feeds)": {"newsrsswebfeeds"},
    "News": {"newsrsswebfeeds"},
    "Course and Course Reference": {"coursemanagement"},
    "CSS / Templates": {"style"},
    # Didactic Templates: Korrekt als "Didactic Templates" im Generator (kein Mapping nötig)
    "Favourites": {"favourites", "categoryandrepository"},  # ggf. unter Repository
    "GlobalCache": {"cache"},
    "Global Screen": {"globalscreenservice"},
    "Group and Group Reference": {"group"},
    "Init (aka Initialisation Service)": {"loginauthregistration"},
    "ItemGroup": {"itemgroups"},
    "LTI Provider": {"lti"},
    "MathJax": {"math"},
    "Object Service": {"iliasobject"},  # in new als ILIASObject
    "Open ID Connect": {"loginauthregistration"},
    "RBAC / Access Control": {"rbacandpermissions"},
    "Scorm (aka Learning Module SCORM 1.2 and 2004)": {"learningmodulescorm"},
    "Tasks": {"taskservice"},
    "Taxonomy": {"taxonomyservice"},
    "UICore": {"userinterface"},
    "Web Access Checker": {"securityinclwebaccesschecker"},
    "Webservices": {"webservicesoverviewsoaprest"},
    "xAPI/cmi5": {"xapi"},
}


def test_compare_with_old(md_content: str, old_content: str) -> list[str]:
    """Alle Komponenten aus old sind in new vorhanden (Vergleich über normalisierte Namen inkl. aka-/Substring-Varianten und bekanntes Mapping)."""
    old_by_name = extract_components_with_authorities(old_content, only_with_folders=False)
    new_by_name = extract_components_with_authorities(md_content, only_with_folders=True)
    new_variants = set()
    for data in new_by_name.values():
        new_variants.update(normalized_component_name_variants(data["component_name"]))
    errors = []
    for norm_name, old_data in old_by_name.items():
        if old_data["component_name"] in OLD_COMPONENTS_MERGED_IN_NEW:
            continue
        old_variants = normalized_component_name_variants(old_data["component_name"])
        if _old_component_matched_in_new(old_variants, new_variants):
            continue
        accepted = OLD_DISPLAY_NAME_ACCEPTED_NEW_NORMALIZED.get(old_data["component_name"])
        if accepted and (accepted & new_variants):
            continue
        errors.append(f"Komponente aus maintenance_old fehlt in maintenance.md: {old_data['component_name']}")
    return errors


def test_compare_content_with_old(md_content: str, old_content: str) -> list[str]:
    """
    Inhaltlicher Vergleich: Für Komponenten, die in beiden Dateien vorkommen (gleicher
    normalisierter Name), müssen die Maintainer/Authorities übereinstimmen.
    Komponenten nur in old (andere Struktur/Umbenennung) führen nicht zu Fehlern.
    """
    old_by_name = extract_components_with_authorities(old_content, only_with_folders=False)
    new_by_name = extract_components_with_authorities(md_content, only_with_folders=True)
    errors = []
    for norm_name, old_data in old_by_name.items():
        if norm_name not in new_by_name:
            continue  # Nur in old: andere Struktur/Name, kein Fehler
        new_data = new_by_name[norm_name]
        for key in AUTHORITY_KEYS:
            old_val = old_data["authorities"].get(key, "NONE")
            new_val = new_data["authorities"].get(key, "NONE")
            if old_val != new_val:
                errors.append(
                    f"{old_data['component_name']} / {key}: old={old_val!r} vs new={new_val!r}"
                )
    return errors


def run_tests(compare_old: bool = False) -> bool:
    if not MAINTENANCE_MD.is_file():
        print(f"Datei nicht gefunden: {MAINTENANCE_MD}", file=sys.stderr)
        return False

    content = MAINTENANCE_MD.read_text(encoding="utf-8")
    all_errors = []

    all_errors.extend(test_no_unstable_wiki_links(content))
    all_errors.extend(test_all_docu_links_stable(content))
    all_errors.extend(test_component_blocks_balanced(content))
    all_errors.extend(test_component_blocks_structure(content))

    compare_content = "--compare-content" in sys.argv
    if (compare_old or compare_content) and MAINTENANCE_OLD_MD.is_file():
        old_content = MAINTENANCE_OLD_MD.read_text(encoding="utf-8")
        if compare_old:
            all_errors.extend(test_compare_with_old(content, old_content))
        if compare_content:
            all_errors.extend(test_compare_content_with_old(content, old_content))
    elif compare_old or compare_content:
        print("Hinweis: maintenance_old.md nicht gefunden, Vergleich übersprungen.", file=sys.stderr)

    if all_errors:
        for e in all_errors:
            print(f"  FAIL: {e}", file=sys.stderr)
        print(f"\n{len(all_errors)} Fehler gefunden.", file=sys.stderr)
        return False
    print("Alle Prüfungen bestanden.")
    return True


def main() -> int:
    compare_old = "--compare-old" in sys.argv
    return 0 if run_tests(compare_old=compare_old) else 1


if __name__ == "__main__":
    sys.exit(main())
