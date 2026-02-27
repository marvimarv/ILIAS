#!/usr/bin/env python3
"""
Vollständiges Script zur Generierung der neuen maintenance.md Struktur.

Autoritätsquelle ist immer maintenance_old.md (Pflicht). maintenance.md ist die
generierte Ausgabe und wird nie als Quelle gelesen. Fehlt für einen Ordner ein
Eintrag in maintenance_old.md, wird maintenance.json im jeweiligen Ordner als
Fallback genutzt.
"""

import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

# Branch -> Authority-Dateiname (Input); Ausgabe ist immer maintenance.md im jeweiligen Branch
BRANCH_INPUT_MAP = {
    "release_10": "maintenance_old_10.md",
    "release_11": "maintenance_old_11.md",
    "trunk": "maintenance_old_trunk.md",
}
# Authority-Dateiname -> GitHub-Tree-Branch für Component-Folder-Links
INPUT_TO_TREE_BRANCH = {
    "maintenance_old_10.md": "release_10",
    "maintenance_10.md": "release_10",
    "maintenance_old_11.md": "release_11",
    "maintenance_11.md": "release_11",
    "maintenance_old_trunk.md": "trunk",
    "maintenance_trunk.md": "trunk",
    "maintenance_old.md": "trunk",
}
DEFAULT_INPUT_NAME = "maintenance_old.md"
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

def format_component_section(component_name, folders, authorities_dict, is_unmaintained=False, real_folders=None, tree_branch="trunk"):
    """Formatiere eine Komponenten-Sektion. real_folders: set der echten Ordner-Namen. tree_branch: Branch für GitHub-Ordner-Links (z. B. release_10)."""
    github_base = f"{GITHUB_REPO_TREE}/{tree_branch}/components/ILIAS"
    if real_folders is not None and folders and not (set(folders) & real_folders):
        folders_str = "*(no dedicated folder in repository)*"
    else:
        folders_str = ', '.join([f'[`{f}`]({github_base}/{f})' for f in sorted(folders)])
    
    # Feature Wiki Link für die Komponente
    feature_wiki_link = get_feature_wiki_link(component_name)
    component_name_with_link = f"[{component_name}]({feature_wiki_link})"
    
    # Erstelle Kommentar-Namen für die Komponente (verwende ersten folder oder component_name)
    comment_name = folders[0] if folders else component_name.replace(' ', '').replace('&', '').replace(',', '')
    
    if len(folders) == 1:
        # Einfache Komponente
        folder = folders[0]
        auth = authorities_dict.get(folder, {})
        formatted = format_authorities(auth, is_unmaintained)
        
        status_line = "\n**Status:** Unmaintained / NONE\n" if is_unmaintained else ""
        
        result = f"""[//]: # (BEGIN {comment_name})

#### {component_name_with_link}
{status_line}*Component Folders:* {folders_str}

* Authority to Sign off on Conceptual Changes: {formatted['conceptual'] or 'NONE'}
* Authority to Sign off on Code Changes: {formatted['code'] or 'NONE'}
* Authority to Curate Test Cases: {formatted['test_cases'] or 'NONE'}
* Tester: {formatted['tester'] or 'NONE'}
* Authority to (De-)Assign Authorities: {formatted['assign_authorities'] or 'NONE'}
* Assignee for Issues: {formatted['issues'] or 'NONE'}
* Assignee for Security Reports: {formatted['security_reports'] or 'NONE'}"""
        
        # Füge Guidelines nur hinzu, wenn vorhanden
        if formatted['guidelines']:
            result += f"\n* Unit-specific Guidelines, Rules, and Regulations: {formatted['guidelines']}"
        
        result += f"""

[//]: # (END {comment_name})
"""
        return result
    else:
        # Komplexe Komponente mit mehreren Ordnern; Kommentar nur \w (damit BEGIN/END vom Test geparst werden)
        comment_name = component_name.replace(' ', '').replace('&', '').replace(',', '').replace('(', '').replace(')', '')
        comment_name = re.sub(r'[^\w]', '', comment_name)  # En-Dash, Bindestriche etc. entfernen
        
        sections = [f"""[//]: # (BEGIN {comment_name})

#### {component_name_with_link}

*Component Folders:* {folders_str}
"""]
        
        for folder in sorted(folders):
            auth = authorities_dict.get(folder, {})
            formatted = format_authorities(auth, is_unmaintained)
            
            status_line = "\n**Status:** Unmaintained / NONE\n" if is_unmaintained else ""
            
            # BEGIN Kommentar VOR dem Content
            section_text = f"""
[//]: # (BEGIN {folder})

##### {folder}
{status_line}* Authority to Sign off on Conceptual Changes: {formatted['conceptual'] or 'NONE'}
* Authority to Sign off on Code Changes: {formatted['code'] or 'NONE'}
* Authority to Curate Test Cases: {formatted['test_cases'] or 'NONE'}
* Tester: {formatted['tester'] or 'NONE'}
* Authority to (De-)Assign Authorities: {formatted['assign_authorities'] or 'NONE'}
* Assignee for Issues: {formatted['issues'] or 'NONE'}
* Assignee for Security Reports: {formatted['security_reports'] or 'NONE'}"""
            
            # Füge Guidelines nur hinzu, wenn vorhanden
            if formatted['guidelines']:
                section_text += f"\n* Unit-specific Guidelines, Rules, and Regulations: {formatted['guidelines']}"
            
            # END Kommentar NACH dem Content
            section_text += f"""

[//]: # (END {folder})
"""
            sections.append(section_text)
        
        sections.append(f"\n[//]: # (END {comment_name})")
        return '\n'.join(sections)

def main():
    base_path = Path(__file__).parent.parent.parent
    script_dir = Path(__file__).resolve().parent
    if "--refresh-wiki-links" in sys.argv:
        sys.argv.remove("--refresh-wiki-links")
        overview_html = base_path / "onlylocal" / "Seite: Feature Wiki: Overview: DOCU.html"
        if overview_html.exists():
            print("Aktualisiere Feature-Wiki-Permalinks (Link in Zwischenablage kopieren)…")
            import subprocess
            rc = subprocess.run(
                [sys.executable, str(script_dir / "extract_feature_wiki_wpage_ids.py"), str(overview_html)],
                cwd=str(base_path),
            )
            if rc.returncode != 0:
                print("Hinweis: Extractor beendet mit Fehlercode.", file=sys.stderr)
        else:
            print("Hinweis: Overview-HTML nicht gefunden, überspringe --refresh-wiki-links.", file=sys.stderr)
    components_path = base_path / "components" / "ILIAS"
    dev_dir = base_path / "docs" / "development"
    maintenance_old_path, output_path = _resolve_maintenance_paths(base_path)
    maintenance_md_path = dev_dir / "maintenance.md"

    # Autoritätsquelle ist die gewählte maintenance_old*.md; Ausgabe in output_path (z. B. maintenance.md).
    # Fehlt ein Eintrag in der Autoritätsdatei, wird maintenance.json im Ordner als Fallback genutzt.
    with open(maintenance_old_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    print(f"Using {maintenance_old_path.name} as authority source (maintenance.json only when entry missing in old)")

    # Extrahiere Einleitung (alles vor "## Current Maintainerships")
    # Entferne doppelte "Current Maintainerships" falls vorhanden
    md_content_clean = re.sub(r'^## Current Maintainerships\s*\n\s*## Current Maintainerships', '## Current Maintainerships', md_content, flags=re.MULTILINE)
    # Entferne "## Unmaintained Components" Sektion aus der Einleitung (falls vorhanden)
    md_content_clean = re.sub(r'\n## Unmaintained Components.*?\n## Current Maintainerships', '\n## Current Maintainerships', md_content_clean, flags=re.DOTALL)
    intro_match = re.search(r'^(.*?)## Current Maintainerships', md_content_clean, re.DOTALL)
    if intro_match:
        intro = intro_match.group(1).rstrip()
    elif "# Components and Related Authorities" in md_content_clean:
        # maintenance_old.md hat oft kein "## Current Maintainerships" – Komponentenliste beginnt hier; nur Text davor als Intro
        intro = md_content_clean.split("# Components and Related Authorities", 1)[0].rstrip()
    else:
        intro = md_content_clean.split('## Current Maintainerships')[0].rstrip()
    
    # Authorities nur aus dem Listen-Abschnitt (ab "## Current Maintainerships"), damit keine doppelten Blöcke (Intro vs. Liste) einander überschreiben
    content_for_authorities = md_content
    if "## Current Maintainerships" in md_content:
        content_for_authorities = md_content.split("## Current Maintainerships", 1)[-1]
    md_components = extract_component_from_md(content_for_authorities)
    print(f"Extracted {len(md_components)} components from maintenance_old.md")
    
    # Mapping: comment_name -> folder_name
    # Wir müssen herausfinden, welche folder-Namen zu welchen comment-Namen gehören
    comment_to_folders = defaultdict(list)
    
    # Sammle alle Components aus maintenance.json
    components = {}
    authorities_dict = {}
    
    # Finde alle component Ordner
    for folder in components_path.iterdir():
        if folder.is_dir():
            folder_name = folder.name
            maintenance_json = folder / "maintenance.json"
            
            if maintenance_json.exists():
                json_data = parse_maintenance_json(maintenance_json)
                if json_data:
                    belong_to = json_data.get('belong_to_component', 'None')
                    components[folder_name] = {
                        'belong_to_component': belong_to,
                        'maintenance_json': json_data,
                        'has_json': True
                    }
            else:
                components[folder_name] = {
                    'belong_to_component': 'None',
                    'maintenance_json': None,
                    'has_json': False
                }
    
    # Erstelle Mapping von folder_name zu component_name
    folder_to_component_name = {}
    for folder_name, data in components.items():
        belong_to = data.get('belong_to_component', 'None')
        component_name = get_component_name_from_folder(folder_name, belong_to)
        folder_to_component_name[folder_name] = component_name
    
    # Pro Ordner: MD nutzen wenn (1) Ordner in "Component Folders:" steht, oder (2) Alter-Format-Block ohne diese Zeile: comment_name = folder_name.
    md_folder_to_comment = {}
    for comment_name, md_data in md_components.items():
        folders_in_block = md_data.get('folders', [])
        if folders_in_block:
            for f in folders_in_block:
                md_folder_to_comment[f] = comment_name
        else:
            # Altes Format: Keine "Component Folders:"-Zeile → Block gilt für Ordner mit gleichem Namen wie comment_name (z. B. DataCollection)
            if comment_name not in md_folder_to_comment:
                md_folder_to_comment[comment_name] = comment_name
    comment_to_component = {}
    for comment_name, md_data in md_components.items():
        comment_to_component[comment_name] = md_data['component_name']
    
    # Ordne Authorities den folders zu (nur MD wenn dieser Ordner in der MD explizit unter Component Folders steht)
    for folder_name, data in components.items():
        belong_to = data.get('belong_to_component', 'None')
        component_name = folder_to_component_name.get(folder_name, folder_name)
        found_authorities = None
        
        if folder_name in md_folder_to_comment:
            comment_name = md_folder_to_comment[folder_name]
            found_authorities = md_components[comment_name]['authorities'].copy()
        
        # Wenn gefunden (Ordner in MD genannt), setze Authorities und suche Guidelines
        if found_authorities:
            # Suche nach Guidelines-Datei (auch für unmaintained Components)
            guidelines_link = find_guidelines_file(folder_name, component_name, base_path)
            if guidelines_link:
                # Überschreibe immer mit gefundenen Guidelines
                found_authorities['guidelines'] = f"[Guidelines]({guidelines_link})"
            elif found_authorities.get('guidelines') == "[LINK MISSING]('')":
                # Entferne LINK MISSING wenn keine Guidelines gefunden
                found_authorities['guidelines'] = None
            
            authorities_dict[folder_name] = found_authorities
        else:
            # Kein Eintrag in maintenance_old.md für diesen Ordner → Fallback: maintenance.json im Ordner
            guidelines_link = find_guidelines_file(folder_name, component_name, base_path)
            if guidelines_link:
                authorities_dict[folder_name] = {'guidelines': f"[Guidelines]({guidelines_link})"}
            elif data.get('has_json') and data.get('maintenance_json'):
                json_data = data['maintenance_json']
                model = json_data.get('maintenance_model', 'Classic')
                first_maintainer = json_data.get('first_maintainer', '')
                second_maintainer = json_data.get('second_maintainer', '')
                tester = json_data.get('tester', '')
                testcase_writer = json_data.get('testcase_writer', '')

                def parse_user(user_str):
                    if not user_str:
                        return None
                    match = re.match(r'^([^(]+)\((\d+)\)$', user_str.strip())
                    if match:
                        return f"[{match.group(1)}](https://docu.ilias.de/go/usr/{match.group(2)})"
                    return user_str

                code_changes = []
                if first_maintainer:
                    code_changes.append(parse_user(first_maintainer))
                if second_maintainer:
                    code_changes.append(parse_user(second_maintainer))
                code_changes_filtered = [c for c in code_changes if c and str(c).strip()]

                if code_changes_filtered:
                    test_cases_list = []
                    if testcase_writer and str(testcase_writer).strip():
                        u = parse_user(testcase_writer)
                        if u:
                            test_cases_list.append(u)
                    if not test_cases_list and model == 'Classic':
                        test_cases_list = code_changes_filtered
                    tester_list = []
                    if tester and str(tester).strip():
                        u = parse_user(tester)
                        if u:
                            tester_list.append(u)
                    auth_data = {
                        'conceptual': code_changes_filtered,
                        'code': code_changes_filtered,
                        'test_cases': test_cases_list,
                        'tester': tester_list,
                        'assign_authorities': code_changes_filtered,
                        'issues': code_changes_filtered,
                        'security_reports': code_changes_filtered,
                        'guidelines': None
                    }
                    gl_link = find_guidelines_file(folder_name, component_name, base_path)
                    if gl_link:
                        auth_data['guidelines'] = f"[Guidelines]({gl_link})"
                    authorities_dict[folder_name] = auth_data
                else:
                    authorities_dict[folder_name] = {}
    
    # Gruppiere Components nach Komponenten-Namen
    grouped_by_component = defaultdict(list)
    for folder_name, data in components.items():
        component_name = folder_to_component_name.get(folder_name, folder_name)
        grouped_by_component[component_name].append(folder_name)
    
    # Organisiere Components mit ihren Status-Informationen
    component_list = []
    
    for component_name, folders in grouped_by_component.items():
        # Unmaintained nur wenn alle Authorities NONE sind (Eintrag aus maintenance_old.md oder JSON kann Authorities liefern)
        all_authorities_are_none = True
        for folder in folders:
            auth_data = authorities_dict.get(folder, {})
            if not all_authorities_none(auth_data):
                all_authorities_are_none = False
                break
        is_unmaintained = all_authorities_are_none
        
        # Sortiere nach erstem Component-Ordner (alphabetisch)
        first_folder = sorted(folders)[0] if folders else component_name
        
        component_list.append({
            'component_name': component_name,
            'folders': folders,
            'is_unmaintained': is_unmaintained,
            'sort_key': first_folder.lower()  # Für case-insensitive Sortierung
        })
    
    # Zähle maintained und unmaintained (nach tatsächlich gesetzten Authorities aus old MD oder JSON)
    maintained_count = 0
    unmaintained_count = 0
    for folder_name, data in components.items():
        auth_data = authorities_dict.get(folder_name, {})
        if not all_authorities_none(auth_data):
            maintained_count += 1
        else:
            unmaintained_count += 1
    
    # Zähle alle "NONE" Einträge in den Authorities
    none_count = 0
    # Zähle für alle Components (auch die ohne authorities_dict Eintrag)
    for folder_name in components.keys():
        auth_data = authorities_dict.get(folder_name, {})
        formatted = format_authorities(auth_data, all_authorities_none(auth_data))
        for key in ['conceptual', 'code', 'test_cases', 'tester', 'assign_authorities', 'issues', 'security_reports']:
            if formatted.get(key) == 'NONE':
                none_count += 1
    
    # Generiere neue maintenance.md
    # Entferne "## Current Maintainerships" aus intro falls vorhanden
    intro_clean = re.sub(r'\n## Current Maintainerships\s*\n', '\n', intro.rstrip())
    # Entferne auch "## Unmaintained Components" Sektion falls noch vorhanden (inkl. Inhalt bis zum nächsten ##)
    intro_clean = re.sub(r'\n## Unmaintained Components.*?(?=\n##|\Z)', '', intro_clean, flags=re.DOTALL)
    # Entferne auch Reste der Unmaintained Components Sektion (Text ohne Überschrift)
    intro_clean = re.sub(r'\nThe following directories are currently unmaintained:.*?(?=\n##|\Z)', '', intro_clean, flags=re.DOTALL)
    # Entferne deutsche Einleitungstexte (sollen nicht in der Ausgabe stehen)
    intro_clean = re.sub(r'\n?Die folgende Struktur basiert auf der \[offiziellen ILIAS-Komponentenstruktur\]\([^)]+\)\.?\s*', '\n', intro_clean)
    intro_clean = re.sub(r'\n?The following structure is based on the \[official ILIAS component structure\]\([^)]+\)\.?\s*', '\n', intro_clean)
    # Sicherstellen: Intro enthält beide Felder "Authority to Curate Test Cases" und "Tester" in "How Authority Assignments are Stored"
    if 'How Authority Assignments are Stored' in intro_clean and '"Tester"' not in intro_clean:
        tester_bullet = '\n* **"Tester"**: An array in the form [ `<username> (<userid>), <company> (<company_page>)` ] pointing to valid users on https://docu.ilias.de.\n'
        intro_clean = intro_clean.replace('* **"Assignee for Issues"**:', tester_bullet + '* **"Assignee for Issues"**:', 1)
    output_lines = [intro_clean, "", "## Current Maintainerships", ""]
    output_lines.append(f"Components are listed alphabetically by component folder name.")
    output_lines.append("")
    
    # Sortiere Components alphabetisch nach erstem Component-Ordner
    component_list_sorted = sorted(component_list, key=lambda x: x['sort_key'])
    real_folders = set(components.keys())
    tree_branch = INPUT_TO_TREE_BRANCH.get(maintenance_old_path.name, "trunk")
    print(f"Component folder links use branch: {tree_branch}")
    
    for component_data in component_list_sorted:
        component_name = component_data['component_name']
        folders = component_data['folders']
        is_unmaintained = component_data['is_unmaintained']
        
        section = format_component_section(
            component_name,
            folders,
            authorities_dict,
            is_unmaintained,
            real_folders=real_folders,
            tree_branch=tree_branch
        )
        output_lines.append(section)
        output_lines.append("")
    
    # Schreibe neue Datei
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"\nGenerated maintenance.md: {output_path}")
    print(f"Total components: {len(components)}")
    print(f"Components with maintenance.json: {sum(1 for c in components.values() if c['has_json'])}")
    print(f"Unmaintained components: {unmaintained_count}")
    print(f"Components from maintenance.md: {len(md_components)}")

def _git_current_branch(base_path: Path) -> str | None:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=str(base_path),
            capture_output=True,
            text=True,
            timeout=5,
        )
        if r.returncode == 0 and r.stdout:
            return r.stdout.strip() or None
    except Exception:
        pass
    return None


def _resolve_maintenance_paths(base_path: Path) -> tuple[Path, Path]:
    dev_dir = base_path / "docs" / "development"
    parser = __import__("argparse").ArgumentParser(description="Generate maintenance.md from authority file.")
    parser.add_argument(
        "--input", "-i",
        metavar="FILE",
        help=f"Authority file (e.g. maintenance_old.md, maintenance_old_10.md, maintenance_old_trunk.md). Default: from branch or prompt.",
    )
    parser.add_argument(
        "--output", "-o",
        metavar="FILE",
        help=f"Output file. Default: {OUTPUT_NAME}",
    )
    args, _ = parser.parse_known_args()

    out_name = (args.output or OUTPUT_NAME).strip()
    if not out_name.endswith(".md"):
        out_name = out_name + ".md"
    output_path = Path(args.output).resolve() if args.output and Path(args.output).is_absolute() else dev_dir / out_name

    if args.input:
        in_path = Path(args.input)
        if not in_path.is_absolute():
            in_path = dev_dir / in_path.name
        if not in_path.exists():
            print(f"Fehler: Autoritätsdatei nicht gefunden: {in_path}", file=sys.stderr)
            sys.exit(1)
        return in_path, output_path

    branch = _git_current_branch(base_path)
    suggested = BRANCH_INPUT_MAP.get(branch or "") or DEFAULT_INPUT_NAME
    candidates = [f.name for f in dev_dir.glob("maintenance_old*.md")]
    if not candidates:
        print(f"Fehler: Keine Datei maintenance_old*.md in {dev_dir} gefunden.", file=sys.stderr)
        sys.exit(1)
    default_path = dev_dir / suggested
    if default_path.exists():
        print(f"Branch: {branch or '(unbekannt)'} -> Autoritätsdatei: {suggested}")
        return default_path, output_path
    if len(candidates) == 1:
        only = dev_dir / candidates[0]
        print(f"Branch: {branch or '(unbekannt)'}; eine Autoritätsdatei gefunden: {candidates[0]}")
        return only, output_path
    print(f"Branch: {branch or '(unbekannt)'}. Mehrere Autoritätsdateien: {', '.join(sorted(candidates))}")
    print(f"Welche Autoritätsdatei verwenden? [{' / '.join(sorted(candidates))}]")
    try:
        choice = input(f"Dateiname (Enter = {suggested}): ").strip() or suggested
    except EOFError:
        choice = suggested
    chosen = dev_dir / (choice if choice.endswith(".md") else choice + ".md")
    if not chosen.exists():
        chosen = dev_dir / suggested
    if not chosen.exists():
        print(f"Fehler: Datei nicht gefunden: {chosen}", file=sys.stderr)
        sys.exit(1)
    return chosen, output_path


if __name__ == "__main__":
    main()
