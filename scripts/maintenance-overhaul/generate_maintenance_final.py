#!/usr/bin/env python3
"""
Generates docs/development/maintenance.md.

Authority source is always maintenance_trunk.md (never the generated output).
If a folder has no entry in maintenance_trunk.md, its maintenance.json is used
as fallback.  The --branch flag controls only which branch appears in GitHub
links (e.g. release_10, release_11, trunk).
"""

import argparse
import difflib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

FUZZY_MATCH_RATIO_THRESHOLD = 0.82
AUTHORITY_SOURCE_NAME = "maintenance_trunk.md"
OUTPUT_NAME = "maintenance.md"
GITHUB_REPO_TREE = "https://github.com/ILIAS-eLearning/ILIAS/tree"

# ILIAS Kategorien-Mapping
ILIAS_CATEGORIES = {
    1: "General Topics",
    2: "Accessibility, Usability and User Interface",
    3: "ILIAS core",
    4: "General Services",
    5: "Container Objects",
    6: "Communication and Syndication",
    7: "Learning and Content Objects",
    8: "Evaluation, Feedback and Testing",
    9: "Administration"
}

# Feature Wiki URLs für jede Kategorie
FEATURE_WIKI_URLS = {
    1: "https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#1_General_Topics",
    2: "https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#2_Accessibility_Usability_and_User_Interface",
    3: "https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#3_ILIAS_core",
    4: "https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#4_General_Services",
    5: "https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#5_Container_Objects",
    6: "https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#6_Communication_and_Syndication",
    7: "https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#7_Learning_and_Content_Objects",
    8: "https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#8_Evaluation_Feedback_and_Testing",
    9: "https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#9_Administration"
}

# ILIAS Unterkomponenten-Mapping (von Komponentenname zu Kategorie)
# Diese Liste basiert auf der ILIAS-Dokumentation
ILIAS_SUBCOMPONENTS = {
    # 1. General Topics
    "Development Support": 1,
    "Guidelines": 1,
    "Performance": 1,
    "Privacy, Terms of Service and Data Protection (incl. Terms of Service)": 1,
    "Privacy, Terms of Service and Data Protection": 1,
    "Security (incl. Web Access Checker)": 1,
    "Streamlining": 1,
    
    # 2. Accessibility, Usability and User Interface
    "Accessibility": 2,
    "Mobile Support": 2,
    "UI Kitchen Sink": 2,
    "Usability": 2,
    "User Interface": 2,
    
    # 3. ILIAS core
    "Components Framework": 3,
    "Cron Service": 3,
    "Database": 3,
    "ILIAS Resource Storage Service": 3,
    "Interfaces": 3,
    "Language Handling": 3,
    "Logging": 3,
    "Object Templates": 3,
    "Permanent Links": 3,
    "RBAC and Permissions": 3,
    "Web Services Overview: SOAP, REST, ...": 3,
    "Web Services Overview": 3,
    
    # 4. General Services
    "Background Tasks": 4,
    "Badges": 4,
    "Calendar": 4,
    "Certificate": 4,
    "Competence Management": 4,
    "Contacts": 4,
    "Dashboard": 4,
    "ECS Interface – E-Learning Community Server": 4,
    "ECS Interface": 4,
    "Export": 4,
    "Favourites": 4,
    "Global Screen Service": 4,
    "Global Cache": 4,
    "ILIAS Page Editor": 4,
    "Info Page": 4,
    "Learning History": 4,
    "Main Menu": 4,
    "Maps": 4,
    "Metadata": 4,
    "Notes and Comments": 4,
    "Online Help": 4,
    "Organisational Units": 4,
    "Personal and Shared Resources": 4,
    "Portfolio": 4,
    "Precondition Handling": 4,
    "Rating": 4,
    "Search": 4,
    "Staff": 4,
    "Statistics and Learning Progress": 4,
    "Tagging": 4,
    "Task Service": 4,
    "Taxonomy Service": 4,
    "User Service": 4,
    "WebDAV": 4,
    "Who is online?": 4,
    
    # 5. Container Objects
    "Category and Repository": 5,
    "Course Management": 5,
    "Group": 5,
    "Item Groups": 5,
    "Learning Sequence": 5,
    "Session (Course & Group)": 5,
    "Session": 5,
    "Study Programme": 5,
    
    # 6. Communication and Syndication
    "Administrative Notifications": 6,
    "Chat": 6,
    "Forum": 6,
    "Learning Communities": 6,
    "Mail": 6,
    "News - RSS - Webfeeds": 6,
    "News": 6,
    "Notification": 6,
    "Notifications": 6,
    
    # 7. Learning and Content Objects
    "Bibliographic List Item": 7,
    "Blog": 7,
    "Booking Pool": 7,
    "Content Page": 7,
    "Data Collection": 7,
    "File": 7,
    "Glossary": 7,
    "Learning Module HTML": 7,
    "Learning Module ILIAS": 7,
    "Learning Module SCORM": 7,
    "LTI": 7,
    "Media Pools and Media Objects": 7,
    "Mediacast": 7,
    "Weblink": 7,
    "Wiki": 7,
    "xAPI": 7,
    
    # 8. Evaluation, Feedback and Testing
    "Employee Talk": 8,
    "Exercise": 8,
    "Individual Assessment": 8,
    "Poll": 8,
    "Survey": 8,
    "Test & Assessment": 8,
    
    # 9. Administration
    "Administration": 9,
    "Login, Auth & Registration": 9,
    "Setup": 9,
    "System Check": 9,
    "User Administration": 9,
}

# Mapping von folder-Namen zu Komponenten-Namen (basierend auf belong_to_component)
FOLDER_TO_COMPONENT = {
    # Test & Assessment
    "Test": "Test & Assessment",
    "TestQuestionPool": "Test & Assessment",
    
    # Survey
    "Survey": "Survey",
    "SurveyQuestionPool": "Survey",
    
    # Login, Auth & Registration
    "Authentication": "Login, Auth & Registration",
    "AuthApache": "Login, Auth & Registration",
    "AuthShibboleth": "Shibboleth Authentication",
    "Registration": "Login, Auth & Registration",
    "CAS": "Login, Auth & Registration",
    "LDAP": "Login, Auth & Registration",
    "OpenIdConnect": "Login, Auth & Registration",
    "Saml": "SAML",
    "SOAPAuth": "SOAP",
    "Init": "Login, Auth & Registration",
    
    # Category and Repository
    "Category": "Category and Repository",
    "CategoryReference": "Category and Repository",
    "Container": "Category and Repository",
    "ContainerReference": "Category and Repository",
    "Folder": "Category and Repository",
    "Repository": "Category and Repository",
    "RootFolder": "Category and Repository",
    
    # Course Management
    "Course": "Course Management",
    "CourseReference": "Course Management",
    
    # Group
    "Group": "Group",
    "GroupReference": "Group",
    
    # Chat (nur Chatroom + OnScreenChat; Notifications ist eigene Komponente)
    "Chatroom": "Chat",
    "OnScreenChat": "Chat",
    
    # Forum
    "Forum": "Forum",
    "Html": "Forum",
    
    # General Kiosk-Mode
    "KioskMode": "General Kiosk-Mode",
    "KioskMode_": "General Kiosk-Mode",
    
    # GlobalScreen
    "GlobalScreen": "GlobalScreen",
    "GlobalScreen_": "GlobalScreen",
    
    # Learning Module SCORM
    "Scorm2004": "Learning Module SCORM",
    "ScormAicc": "Learning Module SCORM",
    
    # My Workspace
    "PersonalWorkspace": "My Workspace",
    "WorkspaceFolder": "My Workspace",
    "WorkspaceRootFolder": "My Workspace",
    
    # Administration
    "Administration": "Administration",
    "SystemFolder": "Administration",
    
    # ECS Interface
    "RemoteCategory": "ECS Interface",
    "RemoteCourse": "ECS Interface",
    "RemoteFile": "ECS Interface",
    "RemoteGlossary": "ECS Interface",
    "RemoteGroup": "ECS Interface",
    "RemoteLearningModule": "ECS Interface",
    "RemoteTest": "ECS Interface",
    "RemoteWiki": "ECS Interface",
    
    # Metadata
    "ADT": "Metadata",
    "AdvancedMetaData": "Metadata",
    "MetaData": "Metadata",
    
    # Background Tasks
    "BackgroundTasks": "Background Tasks",
    "BackgroundTasks_": "Background Tasks",
    
    # Global Cache
    "GlobalCache": "Global Cache",
    "GlobalCache_": "Global Cache",
}

def parse_maintenance_json(file_path):
    """Parse eine maintenance.json Datei"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None

def normalize_name(name):
    """Normalisiere einen Component-Namen für flexiblen Vergleich"""
    if not name:
        return ""
    # Konvertiere zu lowercase, entferne Leerzeichen und Sonderzeichen
    normalized = name.lower().strip()
    # Entferne häufige Sonderzeichen und normalisiere Leerzeichen
    normalized = re.sub(r'[_\s\-\.]+', '', normalized)
    return normalized


def _fuzzy_match_folder_to_old_block(folder_name_normalized: str, old_format_blocks: list[tuple[str, list[str]]]) -> str | None:
    """
    Finde den besten passenden Alter-Format-Block für einen Ordner (normalisierter Name).
    old_format_blocks: Liste von (comment_name, [normalized_candidates]) – z. B. comment_name + component_name normalisiert.
    Nutzt SequenceMatcher-Ratio; nur ein eindeutiger Treffer oberhalb FUZZY_MATCH_RATIO_THRESHOLD wird zurückgegeben.
    """
    if not folder_name_normalized or not old_format_blocks:
        return None
    best_comment = None
    best_ratio = FUZZY_MATCH_RATIO_THRESHOLD
    second_ratio = 0.0
    for comment_name, candidates in old_format_blocks:
        block_best = 0.0
        for c in candidates:
            if not c:
                continue
            block_best = max(block_best, difflib.SequenceMatcher(None, folder_name_normalized, c).ratio())
        if block_best > best_ratio:
            second_ratio = best_ratio
            best_ratio = block_best
            best_comment = comment_name
        elif block_best > second_ratio:
            second_ratio = block_best
    # Eindeutig: bester Treffer mind. 0.05 besser als der zweite
    if best_comment is not None and (best_ratio - second_ratio) >= 0.05:
        return best_comment
    return best_comment if best_comment is not None and second_ratio < FUZZY_MATCH_RATIO_THRESHOLD else None

def extract_component_from_md(md_content):
    """Extrahiere alle Components aus der maintenance.md"""
    components = {}
    
    # Pattern für Component-Blöcke
    pattern = r'\[//\]: # \(BEGIN (\w+)\)(.*?)\[//\]: # \(END \1\)'
    
    for match in re.finditer(pattern, md_content, re.DOTALL):
        comment_name = match.group(1)
        content = match.group(2)
        
        # Extrahiere Komponentenname
        component_match = re.search(r'\* \*\*([^*]+)\*\*', content)
        if not component_match:
            continue
        
        component_name = component_match.group(1).strip()
        
        # Extrahiere Authorities
        auth_data = {
            'conceptual': [],
            'code': [],
            'test_cases': [],
            'tester': [],
            'assign_authorities': [],
            'issues': [],
            'security_reports': [],
            'guidelines': "[LINK MISSING]('')"
        }
        
        # Parse Authorities - verbesserte Version für mehrzeilige Authorities
        # Verwende Regex, um alle Authorities direkt zu extrahieren
        full_text = content
        
        # Conceptual Changes
        conceptual_match = re.search(r'\* Authority to Sign off on Conceptual Changes:(.*?)(?=\* Authority|\* Tester|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if conceptual_match:
            auth_data['conceptual'] = extract_links_from_line(conceptual_match.group(1))
        
        # Code Changes
        code_match = re.search(r'\* Authority to Sign off on Code Changes:(.*?)(?=\* Authority|\* Tester|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if code_match:
            auth_data['code'] = extract_links_from_line(code_match.group(1))
        
        # Test Cases (Links oder Fallback: Plain-Text wie "FH Aachen", "n.n., Uni Köln", "MISSING")
        test_cases_match = re.search(r'\* Authority to Curate Test Cases:(.*?)(?=\* Authority|\* Tester|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if test_cases_match:
            raw = test_cases_match.group(1).strip().replace('\n', ' ').strip()
            links = extract_links_from_line(raw)
            auth_data['test_cases'] = links if links else ([raw] if raw else [])
        
        # Tester (eigenes Feld, getrennt von Authority to Curate Test Cases)
        tester_match = re.search(r'\* Tester:(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|\[//\]|$)', full_text, re.DOTALL)
        if tester_match:
            raw = tester_match.group(1).strip().replace('\n', ' ').strip()
            links = extract_links_from_line(raw)
            auth_data['tester'] = links if links else ([raw] if raw else [])
        
        # Assign Authorities
        assign_match = re.search(r'\* Authority to \(De-\)Assign Authorities:(.*?)(?=\* Authority|\* Tester|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if assign_match:
            auth_data['assign_authorities'] = extract_links_from_line(assign_match.group(1))
        
        # Issues (alle Links als Liste, z. B. Data/Refinery mit zwei Personen)
        issues_match = re.search(r'\* Assignee for Issues:(.*?)(?=\* Authority|\* Tester|\* Assignee for Security|\* Unit-specific|$)', full_text, re.DOTALL)
        if issues_match:
            auth_data['issues'] = extract_links_from_line(issues_match.group(1))
        
        # Security Reports (alle Links als Liste)
        security_reports_match = re.search(r'\* Assignee for Security Reports:(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if security_reports_match:
            auth_data['security_reports'] = extract_links_from_line(security_reports_match.group(1))
        
        # Guidelines - wird später basierend auf folder_name gesetzt
        guidelines_match = re.search(r'\* Unit-specific Guidelines[^:]*:(.*?)(?=\[//]|$)', full_text, re.DOTALL)
        if guidelines_match:
            extracted = extract_guidelines_from_line(guidelines_match.group(1))
            if extracted:
                auth_data['guidelines'] = extracted
            # Wenn LINK MISSING, wird es später durch Suche ersetzt oder entfernt
        
        # Ordner aus "Component Folders:" extrahieren – nur wenn dieser Block einen Ordner nennt, gilt er für diesen Ordner
        folders_in_block = []
        component_folders_match = re.search(r'\*Component Folders\s*\*:\s*(.*?)(?=\n\* |\n\n|$)', content, re.DOTALL)
        if component_folders_match and '(no dedicated folder' not in component_folders_match.group(1):
            # Format: [`FolderName`](url) oder [`FolderName`](url), ...
            for m in re.finditer(r'\[`([^`]+)`\]\([^)]+\)', component_folders_match.group(1)):
                folders_in_block.append(m.group(1))
        
        components[comment_name] = {
            'component_name': component_name,
            'component_name_normalized': normalize_name(component_name),
            'comment_name_normalized': normalize_name(comment_name),
            'authorities': auth_data,
            'folders': folders_in_block,
        }
    
    return components

def extract_links_from_line(line):
    """Extrahiere alle Links aus einer Zeile"""
    pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    links = []
    for match in re.finditer(pattern, line):
        links.append(f"[{match.group(1)}]({match.group(2)})")
    return links

def extract_single_link(line):
    """Extrahiere einen einzelnen Link"""
    links = extract_links_from_line(line)
    return links[0] if links else None

def extract_tester_from_line(line):
    """Extrahiere Tester-Informationen"""
    tester_text = line.replace('* Tester:', '').replace('* Testcases:', '').strip()
    # Extrahiere Links
    links = extract_links_from_line(tester_text)
    if links:
        return ', '.join(links)
    # Extrahiere Text ohne Links
    text_only = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', tester_text)
    return text_only.strip() if text_only.strip() else None

def merge_tester(current, line):
    """Merge Tester-Informationen"""
    if isinstance(current, str):
        current = current
    else:
        current = str(current) if current else ""
    
    line_clean = line.lstrip(',*').strip()
    links = extract_links_from_line(line_clean)
    if links:
        if current:
            return f"{current}, {', '.join(links)}"
        return ', '.join(links)
    
    text_only = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line_clean)
    if text_only.strip():
        if current:
            return f"{current}, {text_only.strip()}"
        return text_only.strip()
    
    return current

# Mapping von component-Namen zu Guidelines-Dateien
COMPONENT_GUIDELINES = {
    "Accessibility": "https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/docs/development/accessibility.md",
    "User Interface": "https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md",
    "UI-Service": "https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md",
    "UI": "https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md",
    "UICore": "https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md",
    "UIComponent": "https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md",
}

def find_guidelines_file(folder_name, component_name, base_path):
    """Suche nach Guidelines-Dateien für einen component"""
    # Prüfe zuerst component-spezifisches Mapping
    if component_name in COMPONENT_GUIDELINES:
        return COMPONENT_GUIDELINES[component_name]
    
    # Prüfe ob COMMUNITY.md im component Ordner existiert
    community_md = base_path / "components" / "ILIAS" / folder_name / "COMMUNITY.md"
    if community_md.exists():
        return f"https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/{folder_name}/COMMUNITY.md"
    
    # Prüfe ob community.md existiert (lowercase)
    community_md_lower = base_path / "components" / "ILIAS" / folder_name / "community.md"
    if community_md_lower.exists():
        return f"https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/{folder_name}/community.md"
    
    # Prüfe ob docs/COMMUNITY.md existiert
    community_docs = base_path / "components" / "ILIAS" / folder_name / "docs" / "COMMUNITY.md"
    if community_docs.exists():
        return f"https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/{folder_name}/docs/COMMUNITY.md"
    
    # Keine Guidelines gefunden
    return None

def extract_guidelines_from_line(line):
    """Extrahiere Guidelines-Link"""
    pattern = r'\[LINK MISSING\]\([^\)]*\)|\[([^\]]+)\]\(([^\)]+)\)'
    match = re.search(pattern, line)
    if match:
        if match.group(1):
            return f"[{match.group(1)}]({match.group(2)})"
        return None  # LINK MISSING - wird später entfernt
    return None

# Erweiterte Mapping-Tabelle: folder_name -> ILIAS Unterkomponenten-Name
FOLDER_TO_ILIAS_COMPONENT = {
    # 1. General Topics
    "PrivacySecurity": "Privacy, Terms of Service and Data Protection (incl. Terms of Service)",
    "TermsOfService": "Privacy, Terms of Service and Data Protection (incl. Terms of Service)",
    "DataProtection": "Privacy, Terms of Service and Data Protection (incl. Terms of Service)",
    "WebAccessChecker": "Security (incl. Web Access Checker)",
    
    # 2. Accessibility, Usability and User Interface
    "Accessibility": "Accessibility",
    "UI": "User Interface",
    "UICore": "User Interface",
    "UIComponent": "User Interface",
    "UI_": "User Interface",
    
    # 3. ILIAS core
    "Component": "Components Framework",
    "Cron": "Cron Service",
    "Database": "Database",
    "ResourceStorage": "ILIAS Resource Storage Service",
    "Language": "Language Handling",
    "Logging": "Logging",
    "DidacticTemplate": "Didactic Templates",
    "PermanentLink": "Permanent Links",
    "AccessControl": "RBAC and Permissions",
    "WebServices": "Web Services Overview: SOAP, REST, ...",
    
    # 4. General Services
    "BackgroundTasks": "Background Tasks",
    "BackgroundTasks_": "Background Tasks",
    "Badge": "Badges",
    "Calendar": "Calendar",
    "Certificate": "Certificate",
    "Skill": "Competence Management",
    "Contact": "Contacts",
    "Dashboard": "Dashboard",
    "RemoteCategory": "ECS Interface – E-Learning Community Server",
    "RemoteCourse": "ECS Interface – E-Learning Community Server",
    "RemoteFile": "ECS Interface – E-Learning Community Server",
    "RemoteGlossary": "ECS Interface – E-Learning Community Server",
    "RemoteGroup": "ECS Interface – E-Learning Community Server",
    "RemoteLearningModule": "ECS Interface – E-Learning Community Server",
    "RemoteTest": "ECS Interface – E-Learning Community Server",
    "RemoteWiki": "ECS Interface – E-Learning Community Server",
    "Export": "Export",
    "Favourites": "Favourites",
    "GlobalScreen": "Global Screen Service",
    "GlobalScreen_": "Global Screen Service",
    "GlobalCache": "Global Cache",
    "GlobalCache_": "Global Cache",
    "COPage": "ILIAS Page Editor",
    "InfoScreen": "Info Page",
    "LearningHistory": "Learning History",
    "MainMenu": "Main Menu",
    "Maps": "Maps",
    "MetaData": "Metadata",
    "ADT": "Metadata",
    "AdvancedMetaData": "Metadata",
    "Notes": "Notes and Comments",
    "Help": "Online Help",
    "OrgUnit": "Organisational Units",
    "PersonalWorkspace": "Personal and Shared Resources",
    "WorkspaceFolder": "Personal and Shared Resources",
    "WorkspaceRootFolder": "Personal and Shared Resources",
    "Portfolio": "Portfolio",
    "Conditions": "Precondition Handling",
    "Rating": "Rating",
    "Search": "Search",
    "MyStaff": "Staff",
    "Tracking": "Statistics and Learning Progress",
    "Tagging": "Tagging",
    "Tasks": "Task Service",
    "Taxonomy": "Taxonomy Service",
    "User": "User Service",
    "WebDAV": "WebDAV",
    "Awareness": "Who is online?",
    
    # 5. Container Objects
    "Category": "Category and Repository",
    "Repository": "Category and Repository",
    "Container": "Category and Repository",
    "Folder": "Category and Repository",
    "RootFolder": "Category and Repository",
    "CategoryReference": "Category and Repository",
    "ContainerReference": "Category and Repository",
    "Course": "Course Management",
    "CourseReference": "Course Management",
    "Group": "Group",
    "GroupReference": "Group",
    "ItemGroup": "Item Groups",
    "LearningSequence": "Learning Sequence",
    "Session": "Session (Course & Group)",
    "StudyProgramme": "Study Programme",
    "StudyProgrammeReference": "Study Programme",
    
    # 6. Communication and Syndication
    "AdministrativeNotification": "Administrative Notifications",
    "Chatroom": "Chat",
    "OnScreenChat": "Chat",
    "Notifications": "Notifications",   # eigene Komponente (Plural), nicht mit Chat zusammenfassen
    "Notification": "Notification",     # eigene Komponente (Singular)
    "Forum": "Forum",
    "Html": "Forum",
    "Mail": "Mail",
    "News": "News - RSS - Webfeeds",
    "Feeds": "News - RSS - Webfeeds",
    
    # 7. Learning and Content Objects
    "Bibliographic": "Bibliographic List Item",
    "Blog": "Blog",
    "BookingManager": "Booking Pool",
    "ContentPage": "Content Page",
    "DataCollection": "Data Collection",
    "File": "File",
    "Glossary": "Glossary",
    "HTMLLearningModule": "Learning Module HTML",
    "LearningModule": "Learning Module ILIAS",
    "Scorm2004": "Learning Module SCORM",
    "ScormAicc": "Learning Module SCORM",
    "LTIProvider": "LTI",
    "LTIConsumer": "LTI Consumer",
    "MediaPool": "Media Pools and Media Objects",
    "MediaObjects": "Media Pools and Media Objects",
    "MediaCast": "Mediacast",
    "WebResource": "Weblink",
    "Wiki": "Wiki",
    "CmiXapi": "xAPI",
    
    # 8. Evaluation, Feedback and Testing
    "EmployeeTalk": "Employee Talk",
    "Exercise": "Exercise",
    "IndividualAssessment": "Individual Assessment",
    "Poll": "Poll",
    "Survey": "Survey",
    "SurveyQuestionPool": "Survey",
    "Test": "Test & Assessment",
    "TestQuestionPool": "Test & Assessment",
    
    # 9. Administration
    "Administration": "Administration",
    "SystemFolder": "Administration",
    "Authentication": "Login, Auth & Registration",
    "AuthApache": "Login, Auth & Registration",
    "AuthShibboleth": "Shibboleth Authentication",
    "Registration": "Login, Auth & Registration",
    "CAS": "Login, Auth & Registration",
    "LDAP": "Login, Auth & Registration",
    "OpenIdConnect": "Login, Auth & Registration",
    "Saml": "SAML",
    "SOAPAuth": "SOAP",
    "Init": "Login, Auth & Registration",
    "Setup": "Setup",
    "SystemCheck": "System Check",
}

def get_component_name_from_folder(folder_name, belong_to_component):
    """Bestimme den ILIAS-Unterkomponenten-Namen für einen folder"""
    # Explizites Ordner-Mapping hat Vorrang (korrigiert ggf. veraltete belong_to in maintenance.json)
    if folder_name in FOLDER_TO_ILIAS_COMPONENT:
        return FOLDER_TO_ILIAS_COMPONENT[folder_name]
    # Wenn belong_to_component gesetzt ist und nicht "None", prüfe ob es ein ILIAS-Unterkomponenten-Name ist
    if belong_to_component and belong_to_component != 'None':
        if belong_to_component in ILIAS_SUBCOMPONENTS:
            return belong_to_component
        if belong_to_component in FOLDER_TO_ILIAS_COMPONENT.values():
            return belong_to_component
    
    # Fallback: Verwende altes Mapping
    if folder_name in FOLDER_TO_COMPONENT:
        component_name = FOLDER_TO_COMPONENT[folder_name]
        # Prüfe ob es ein ILIAS-Unterkomponenten-Name ist
        if component_name in ILIAS_SUBCOMPONENTS:
            return component_name
    
    # Fallback: Verwende folder_name als Komponentenname
    return folder_name

def get_category_for_component(component_name):
    """Bestimme die Kategorie für eine Komponente"""
    # Prüfe ILIAS Unterkomponenten
    if component_name in ILIAS_SUBCOMPONENTS:
        return ILIAS_SUBCOMPONENTS[component_name]
    
    # Fallback: Verwende folder_name Mapping
    # (wird später implementiert)
    return 3  # Default: ILIAS core

def all_authorities_none(auth_data):
    """Prüfe ob alle Authorities NONE sind"""
    if not auth_data:
        return True
    
    def is_none_or_empty(value):
        if value is None:
            return True
        if isinstance(value, list):
            # Prüfe ob Liste leer ist oder nur leere Strings enthält
            if len(value) == 0:
                return True
            # Filtere leere Strings und prüfe ob Liste dann leer ist
            filtered = [item for item in value if item and str(item).strip()]
            return len(filtered) == 0
        if isinstance(value, str):
            return value.strip() == '' or value.strip().upper() == 'NONE'
        return False
    
    # Prüfe alle relevanten Authorities
    return (
        is_none_or_empty(auth_data.get('conceptual')) and
        is_none_or_empty(auth_data.get('code')) and
        is_none_or_empty(auth_data.get('test_cases')) and
        is_none_or_empty(auth_data.get('tester')) and
        is_none_or_empty(auth_data.get('assign_authorities')) and
        is_none_or_empty(auth_data.get('issues')) and
        is_none_or_empty(auth_data.get('security_reports'))
    )

def format_authorities(auth_data, is_unmaintained=False):
    """Formatiere Authorities für Markdown"""
    if is_unmaintained or not auth_data:
        return {
            'conceptual': 'NONE',
            'code': 'NONE',
            'test_cases': 'NONE',
            'tester': 'NONE',
            'assign_authorities': 'NONE',
            'issues': 'NONE',
            'security_reports': 'NONE',
            'guidelines': None  # Keine Guidelines für unmaintained
        }
    
    def format_list(items):
        if not items:
            return None
        filtered = [item for item in items if item]
        if not filtered:
            return None
        if len(filtered) == 1:
            return filtered[0]
        return ', '.join(filtered)
    
    def format_single_or_list(val):
        if val is None:
            return None
        if isinstance(val, list):
            return format_list(val)
        return val

    formatted = {
        'conceptual': format_list(auth_data.get('conceptual', [])),
        'code': format_list(auth_data.get('code', [])),
        'test_cases': format_list(auth_data.get('test_cases', [])),
        'tester': format_list(auth_data.get('tester', [])),
        'assign_authorities': format_list(auth_data.get('assign_authorities', [])),
        'issues': format_single_or_list(auth_data.get('issues')),
        'security_reports': format_single_or_list(auth_data.get('security_reports')),
        'guidelines': auth_data.get('guidelines')
    }
    
    # Wenn alle formatierten Werte None sind, setze sie auf 'NONE'
    if all(formatted.get(k) is None for k in ['conceptual', 'code', 'test_cases', 'tester', 'assign_authorities', 'issues', 'security_reports']):
        formatted.update({
            'conceptual': 'NONE',
            'code': 'NONE',
            'test_cases': 'NONE',
            'tester': 'NONE',
            'assign_authorities': 'NONE',
            'issues': 'NONE',
            'security_reports': 'NONE'
        })
    
    return formatted

# Stabile Feature-Wiki-URLs: wpage_ID_1357 (aus feature_wiki_wpage_ids.json, erzeugt via extract_feature_wiki_wpage_ids.py)
_FEATURE_WIKI_WPAGE_IDS = None

def _load_feature_wiki_wpage_ids():
    """Lädt page_name -> wpage_id aus feature_wiki_wpage_ids.json (falls vorhanden)."""
    global _FEATURE_WIKI_WPAGE_IDS
    if _FEATURE_WIKI_WPAGE_IDS is not None:
        return _FEATURE_WIKI_WPAGE_IDS
    json_path = Path(__file__).resolve().parent / "feature_wiki_wpage_ids.json"
    if json_path.is_file():
        try:
            _FEATURE_WIKI_WPAGE_IDS = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            _FEATURE_WIKI_WPAGE_IDS = {}
    else:
        _FEATURE_WIKI_WPAGE_IDS = {}
    return _FEATURE_WIKI_WPAGE_IDS

def get_feature_wiki_link(component_name):
    """Erstelle Feature Wiki Link für eine Komponente (stabile URL wenn Mapping vorhanden)."""
    import urllib.parse

    component_to_page = {
        "Privacy, Terms of Service and Data Protection (incl. Terms of Service)": "Privacy%2C_Terms_of_Service_and_Data_Protection",
        "Privacy, Terms of Service and Data Protection": "Privacy%2C_Terms_of_Service_and_Data_Protection",
        "Security (incl. Web Access Checker)": "Security",
        "Web Services Overview: SOAP, REST, ...": "Web_Services_Overview%3A_SOAP%2C_REST%2C_...",
        "Web Services Overview": "Web_Services_Overview%3A_SOAP%2C_REST%2C_...",
        "ECS Interface – E-Learning Community Server": "ECS_Interface",
        "ECS Interface": "ECS_Interface",
        "Session (Course & Group)": "Session_%28Course_%26_Group%29",
        "Session": "Session_%28Course_%26_Group%29",
        "News - RSS - Webfeeds": "News_-_RSS_-_Webfeeds",
        "News": "News_-_RSS_-_Webfeeds",
        "Test & Assessment": "Test_%26_Assessment",
        "Login, Auth & Registration": "Login%2C_Auth_%26_Registration",
        "User Service (incl. Personal Profile)": "User_Service",
        "User Service": "User_Service",
        "User Administration": "User_Service",
        "Who is online?": "Who_is_online%3F",
        "RBAC and Permissions": "RBAC",
    }

    if component_name in component_to_page:
        page_name = component_to_page[component_name]
    else:
        page_name = component_name.replace(' ', '_')
        page_name = urllib.parse.quote(page_name, safe='_')

    wpage_ids = _load_feature_wiki_wpage_ids()
    wpage_id = wpage_ids.get(page_name)
    if wpage_id is not None:
        return f"https://docu.ilias.de/go/wiki/wpage_{wpage_id}_1357"
    # Kein eigener Wiki-Eintrag: stabile Link zur allgemeinen Feature-Wiki-Übersicht
    return "https://docu.ilias.de/go/wiki/wpage_1_1357"

def format_folder_section(folder_name, belongs_to_name, auth_data, is_unmaintained, tree_branch):
    """Formatiere einen einzelnen Ordner-Block für die Ausgabe."""
    github_link = f"{GITHUB_REPO_TREE}/{tree_branch}/components/ILIAS/{folder_name}"
    formatted = format_authorities(auth_data, is_unmaintained)
    status_line = "\n**Status:** Unmaintained / NONE\n" if is_unmaintained else ""
    wiki_link = get_feature_wiki_link(belongs_to_name or folder_name)
    display_name = belongs_to_name or folder_name
    belongs_to_line = f"\n*Belongs to:* [{display_name}]({wiki_link})\n"

    result = f"""[//]: # (BEGIN {folder_name})

#### [{folder_name}]({github_link})
{status_line}{belongs_to_line}
* Authority to Sign off on Conceptual Changes: {formatted['conceptual'] or 'NONE'}
* Authority to Sign off on Code Changes: {formatted['code'] or 'NONE'}
* Authority to Curate Test Cases: {formatted['test_cases'] or 'NONE'}
* Tester: {formatted['tester'] or 'NONE'}
* Authority to (De-)Assign Authorities: {formatted['assign_authorities'] or 'NONE'}
* Assignee for Issues: {formatted['issues'] or 'NONE'}
* Assignee for Security Reports: {formatted['security_reports'] or 'NONE'}"""

    if formatted['guidelines']:
        result += f"\n* Unit-specific Guidelines, Rules, and Regulations: {formatted['guidelines']}"

    result += f"""

[//]: # (END {folder_name})
"""
    return result

def _parse_user(user_str):
    """Parse 'username(id)' -> Markdown link."""
    if not user_str:
        return None
    match = re.match(r'^([^(]+)\((\d+)\)$', user_str.strip())
    if match:
        return f"[{match.group(1)}](https://docu.ilias.de/go/usr/{match.group(2)})"
    return user_str


def _authorities_from_json(json_data, folder_name, component_name, base_path):
    """Build authorities dict from a maintenance.json entry."""
    model = json_data.get('maintenance_model', 'Classic')
    first_maintainer = json_data.get('first_maintainer', '')
    second_maintainer = json_data.get('second_maintainer', '')
    tester = json_data.get('tester', '')
    testcase_writer = json_data.get('testcase_writer', '')

    code_changes = []
    if first_maintainer:
        code_changes.append(_parse_user(first_maintainer))
    if second_maintainer:
        code_changes.append(_parse_user(second_maintainer))
    code_changes = [c for c in code_changes if c and str(c).strip()]

    if not code_changes:
        return {}

    test_cases_list = []
    if testcase_writer and str(testcase_writer).strip():
        u = _parse_user(testcase_writer)
        if u:
            test_cases_list.append(u)
    if not test_cases_list and model == 'Classic':
        test_cases_list = code_changes

    tester_list = []
    if tester and str(tester).strip():
        u = _parse_user(tester)
        if u:
            tester_list.append(u)

    auth = {
        'conceptual': code_changes,
        'code': code_changes,
        'test_cases': test_cases_list,
        'tester': tester_list,
        'assign_authorities': code_changes,
        'issues': code_changes,
        'security_reports': code_changes,
        'guidelines': None,
    }
    gl = find_guidelines_file(folder_name, component_name, base_path)
    if gl:
        auth['guidelines'] = f"[Guidelines]({gl})"
    return auth


def _build_md_folder_mapping(md_components):
    """Build folder_name -> comment_name mapping from parsed MD blocks."""
    md_folder_to_comment = {}
    old_format_blocks = []
    for comment_name, md_data in md_components.items():
        folders_in_block = md_data.get('folders', [])
        if folders_in_block:
            for f in folders_in_block:
                md_folder_to_comment[f] = comment_name
        else:
            if comment_name not in md_folder_to_comment:
                md_folder_to_comment[comment_name] = comment_name
            comp_norm = normalize_name(md_data['component_name'])
            if comp_norm and comp_norm not in md_folder_to_comment:
                md_folder_to_comment[comp_norm] = comment_name
            cands = [normalize_name(comment_name), comp_norm]
            old_format_blocks.append((comment_name, [c for c in cands if c]))
    return md_folder_to_comment, old_format_blocks


def _find_md_comment(folder_name, md_folder_to_comment, old_format_blocks):
    """Resolve folder_name to a comment_name via exact, normalised, or fuzzy match."""
    comment = md_folder_to_comment.get(folder_name) or md_folder_to_comment.get(normalize_name(folder_name))
    if not comment and old_format_blocks:
        comment = _fuzzy_match_folder_to_old_block(normalize_name(folder_name), old_format_blocks)
    return comment


def _clean_intro(intro_text):
    """Remove generated artefacts from the intro section."""
    t = re.sub(r'\n## Current Maintainerships\s*\n', '\n', intro_text.rstrip())
    t = re.sub(r'\n## Unmaintained Components.*?(?=\n##|\Z)', '', t, flags=re.DOTALL)
    t = re.sub(r'\nThe following directories are currently unmaintained:.*?(?=\n##|\Z)', '', t, flags=re.DOTALL)
    t = re.sub(r'\n?Die folgende Struktur basiert auf der \[offiziellen ILIAS-Komponentenstruktur\]\([^)]+\)\.?\s*', '\n', t)
    t = re.sub(r'\n?The following structure is based on the \[official ILIAS component structure\]\([^)]+\)\.?\s*', '\n', t)
    if 'How Authority Assignments are Stored' in t and '"Tester"' not in t:
        bullet = '\n* **"Tester"**: An array in the form [ `<username> (<userid>), <company> (<company_page>)` ] pointing to valid users on https://docu.ilias.de.\n'
        t = t.replace('* **"Assignee for Issues"**:', bullet + '* **"Assignee for Issues"**:', 1)
    return t


def main():
    parser = argparse.ArgumentParser(description="Generate maintenance.md from maintenance_trunk.md.")
    parser.add_argument(
        "--branch", "-b",
        required=True,
        help="Branch name for GitHub component links (e.g. release_10, release_11, trunk).",
    )
    parser.add_argument("--refresh-wiki-links", action="store_true", help="Refresh Feature-Wiki wpage IDs before generating.")
    args = parser.parse_args()
    tree_branch = args.branch

    base_path = Path(__file__).parent.parent.parent
    script_dir = Path(__file__).resolve().parent
    if args.refresh_wiki_links:
        overview_html = base_path / "onlylocal" / "Seite: Feature Wiki: Overview: DOCU.html"
        if overview_html.exists():
            import subprocess
            subprocess.run([sys.executable, str(script_dir / "extract_feature_wiki_wpage_ids.py"), str(overview_html)], cwd=str(base_path))
        else:
            print("Hinweis: Overview-HTML nicht gefunden, ueberspringe --refresh-wiki-links.", file=sys.stderr)

    dev_dir = base_path / "docs" / "development"
    authority_path = dev_dir / AUTHORITY_SOURCE_NAME
    output_path = dev_dir / OUTPUT_NAME
    components_path = base_path / "components" / "ILIAS"

    if not authority_path.exists():
        print(f"Error: {AUTHORITY_SOURCE_NAME} not found in {dev_dir}", file=sys.stderr)
        sys.exit(1)

    md_content = authority_path.read_text(encoding='utf-8')
    print(f"Authority source: {AUTHORITY_SOURCE_NAME}")
    print(f"GitHub links branch: {tree_branch}")

    # ---- Extract intro ----
    md_clean = re.sub(r'^## Current Maintainerships\s*\n\s*## Current Maintainerships', '## Current Maintainerships', md_content, flags=re.MULTILINE)
    md_clean = re.sub(r'\n## Unmaintained Components.*?\n## Current Maintainerships', '\n## Current Maintainerships', md_clean, flags=re.DOTALL)
    intro_match = re.search(r'^(.*?)## Current Maintainerships', md_clean, re.DOTALL)
    if intro_match:
        intro = intro_match.group(1).rstrip()
    elif "# Components and Related Authorities" in md_clean:
        intro = md_clean.split("# Components and Related Authorities", 1)[0].rstrip()
    else:
        intro = md_clean.split('## Current Maintainerships')[0].rstrip()

    # ---- Parse authority blocks from MD ----
    content_for_authorities = md_content
    if "## Current Maintainerships" in md_content:
        content_for_authorities = md_content.split("## Current Maintainerships", 1)[-1]
    md_components = extract_component_from_md(content_for_authorities)
    print(f"Extracted {len(md_components)} blocks from {AUTHORITY_SOURCE_NAME}")

    # ---- Collect component folders and their maintenance.json ----
    components = {}
    for folder in components_path.iterdir():
        if not folder.is_dir():
            continue
        folder_name = folder.name
        mj = folder / "maintenance.json"
        if mj.exists():
            json_data = parse_maintenance_json(mj)
            if json_data:
                components[folder_name] = {
                    'belong_to_component': json_data.get('belong_to_component', 'None'),
                    'maintenance_json': json_data,
                    'has_json': True,
                }
                continue
        components[folder_name] = {'belong_to_component': 'None', 'maintenance_json': None, 'has_json': False}

    # ---- Determine "belongs to" group per folder ----
    folder_to_group = {}
    for folder_name, data in components.items():
        folder_to_group[folder_name] = get_component_name_from_folder(folder_name, data.get('belong_to_component', 'None'))

    # ---- Resolve authorities per folder (MD first, then JSON fallback) ----
    md_folder_map, old_blocks = _build_md_folder_mapping(md_components)
    authorities_dict = {}
    for folder_name, data in components.items():
        group_name = folder_to_group.get(folder_name, folder_name)
        comment = _find_md_comment(folder_name, md_folder_map, old_blocks)
        if comment:
            auth = md_components[comment]['authorities'].copy()
            gl = find_guidelines_file(folder_name, group_name, base_path)
            if gl:
                auth['guidelines'] = f"[Guidelines]({gl})"
            elif auth.get('guidelines') == "[LINK MISSING]('')":
                auth['guidelines'] = None
            authorities_dict[folder_name] = auth
        elif data.get('has_json') and data.get('maintenance_json'):
            authorities_dict[folder_name] = _authorities_from_json(data['maintenance_json'], folder_name, group_name, base_path)
        else:
            gl = find_guidelines_file(folder_name, group_name, base_path)
            authorities_dict[folder_name] = {'guidelines': f"[Guidelines]({gl})"} if gl else {}

    # ---- Count stats ----
    unmaintained_count = sum(1 for fn in components if all_authorities_none(authorities_dict.get(fn, {})))

    # ---- Build output ----
    intro_clean = _clean_intro(intro)
    output_lines = [
        intro_clean, "",
        "## Current Maintainerships", "",
        "Components are listed alphabetically by their folder name in `components/ILIAS/`.",
        "",
    ]

    for folder_name in sorted(components.keys(), key=str.lower):
        auth = authorities_dict.get(folder_name, {})
        is_unmaintained = all_authorities_none(auth)
        group_name = folder_to_group.get(folder_name, folder_name)
        section = format_folder_section(folder_name, group_name, auth, is_unmaintained, tree_branch)
        output_lines.append(section)
        output_lines.append("")

    output_path.write_text('\n'.join(output_lines), encoding='utf-8')

    print(f"\nGenerated: {output_path}")
    print(f"Folders: {len(components)} | Unmaintained: {unmaintained_count} | MD blocks: {len(md_components)}")


if __name__ == "__main__":
    main()
