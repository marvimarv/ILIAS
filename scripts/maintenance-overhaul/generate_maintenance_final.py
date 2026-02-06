#!/usr/bin/env python3
"""
Vollständiges Script zur Generierung der neuen maintenance.md Struktur
Verwendet maintenance.md als primäre Quelle für Authorities
"""

import json
import re
from collections import defaultdict
from pathlib import Path

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
    
    # Chat
    "Chatroom": "Chat",
    "Notifications": "Chat",
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
            'assign_authorities': [],
            'tester': None,
            'security_reports': None,
            'security_issues': None,
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
        
        # Test Cases
        test_cases_match = re.search(r'\* Authority to Curate Test Cases:(.*?)(?=\* Authority|\* Tester|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if test_cases_match:
            auth_data['test_cases'] = extract_links_from_line(test_cases_match.group(1))
        
        # Assign Authorities
        assign_match = re.search(r'\* Authority to \(De-\)Assign Authorities:(.*?)(?=\* Authority|\* Tester|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if assign_match:
            auth_data['assign_authorities'] = extract_links_from_line(assign_match.group(1))
        
        # Tester
        tester_match = re.search(r'\* (?:Tester|Testcases):(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if tester_match:
            tester_text = tester_match.group(1)
            links = extract_links_from_line(tester_text)
            if links:
                auth_data['tester'] = ', '.join(links)
            else:
                # Extrahiere Text ohne Links
                text_only = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', tester_text)
                text_only = re.sub(r'\s+', ' ', text_only).strip()
                auth_data['tester'] = text_only if text_only else None
        
        # Security Reports
        security_reports_match = re.search(r'\* Assignee for Security Reports:(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if security_reports_match:
            auth_data['security_reports'] = extract_single_link(security_reports_match.group(1))
        
        # Security Issues
        security_issues_match = re.search(r'\* Assignee for Security Issues:(.*?)(?=\* Authority|\* Assignee|\* Unit-specific|$)', full_text, re.DOTALL)
        if security_issues_match:
            auth_data['security_issues'] = extract_single_link(security_issues_match.group(1))
        
        # Guidelines - wird später basierend auf folder_name gesetzt
        guidelines_match = re.search(r'\* Unit-specific Guidelines[^:]*:(.*?)(?=\[//]|$)', full_text, re.DOTALL)
        if guidelines_match:
            extracted = extract_guidelines_from_line(guidelines_match.group(1))
            if extracted:
                auth_data['guidelines'] = extracted
            # Wenn LINK MISSING, wird es später durch Suche ersetzt oder entfernt
        
        components[comment_name] = {
            'component_name': component_name,
            'authorities': auth_data
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
    "DidacticTemplate": "Object Templates",
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
    "Notifications": "Chat",
    "Notification": "Notifications",
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
    # Wenn belong_to_component gesetzt ist und nicht "None", prüfe ob es ein ILIAS-Unterkomponenten-Name ist
    if belong_to_component and belong_to_component != 'None':
        # Prüfe ob belong_to_component bereits ein ILIAS-Unterkomponenten-Name ist
        if belong_to_component in ILIAS_SUBCOMPONENTS:
            return belong_to_component
        # Sonst verwende Mapping
        if belong_to_component in FOLDER_TO_ILIAS_COMPONENT.values():
            return belong_to_component
    
    # Verwende erweiterte Mapping-Tabelle
    if folder_name in FOLDER_TO_ILIAS_COMPONENT:
        return FOLDER_TO_ILIAS_COMPONENT[folder_name]
    
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

def format_authorities(auth_data, is_unmaintained=False):
    """Formatiere Authorities für Markdown"""
    if is_unmaintained or not auth_data:
        return {
            'conceptual': 'NONE',
            'code': 'NONE',
            'test_cases': 'NONE',
            'assign_authorities': 'NONE',
            'tester': 'NONE',
            'security_reports': 'NONE',
            'security_issues': 'NONE',
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
    
    return {
        'conceptual': format_list(auth_data.get('conceptual', [])),
        'code': format_list(auth_data.get('code', [])),
        'test_cases': format_list(auth_data.get('test_cases', [])),
        'assign_authorities': format_list(auth_data.get('assign_authorities', [])),
        'tester': auth_data.get('tester') or None,
        'security_reports': auth_data.get('security_reports'),
        'security_issues': auth_data.get('security_issues'),
        'guidelines': auth_data.get('guidelines')
    }

def format_component_section(component_name, folders, authorities_dict, is_unmaintained=False):
    """Formatiere eine Komponenten-Sektion"""
    folders_str = ', '.join([f'`{f}`' for f in sorted(folders)])
    
    # Erstelle Kommentar-Namen für die Komponente (verwende ersten folder oder component_name)
    comment_name = folders[0] if folders else component_name.replace(' ', '').replace('&', '').replace(',', '')
    
    if len(folders) == 1:
        # Einfache Komponente
        folder = folders[0]
        auth = authorities_dict.get(folder, {})
        formatted = format_authorities(auth, is_unmaintained)
        
        status_line = "\n**Status:** Unmaintained / NONE\n" if is_unmaintained else ""
        
        result = f"""[//]: # (BEGIN {comment_name})

#### {component_name}
{status_line}**Component Ordner:** {folders_str}

* Authority to Sign off on Conceptual Changes: {formatted['conceptual'] or 'NONE'}
* Authority to Sign off on Code Changes: {formatted['code'] or 'NONE'}
* Authority to Curate Test Cases: {formatted['test_cases'] or 'NONE'}
* Authority to (De-)Assign Authorities: {formatted['assign_authorities'] or 'NONE'}
* Tester: {formatted['tester'] or 'NONE'}
* Assignee for Security Reports: {formatted['security_reports'] or 'NONE'}
* Assignee for Security Issues: {formatted['security_issues'] or 'NONE'}"""
        
        # Füge Guidelines nur hinzu, wenn vorhanden
        if formatted['guidelines']:
            result += f"\n* Unit-specific Guidelines, Rules, and Regulations: {formatted['guidelines']}"
        
        result += f"""

[//]: # (END {comment_name})
"""
        return result
    else:
        # Komplexe Komponente mit mehreren Ordnern
        # Erstelle Kommentar-Namen für die Komponente
        comment_name = component_name.replace(' ', '').replace('&', '').replace(',', '').replace('(', '').replace(')', '')
        
        sections = [f"""[//]: # (BEGIN {comment_name})

#### {component_name}

**Component Ordner:** {folders_str}
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
* Authority to (De-)Assign Authorities: {formatted['assign_authorities'] or 'NONE'}
* Tester: {formatted['tester'] or 'NONE'}
* Assignee for Security Reports: {formatted['security_reports'] or 'NONE'}
* Assignee for Security Issues: {formatted['security_issues'] or 'NONE'}"""
            
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
    base_path = Path(__file__).parent.parent
    components_path = base_path / "components" / "ILIAS"
    maintenance_md_path = base_path / "docs" / "development" / "maintenance.md"
    output_path = base_path / "docs" / "development" / "maintenance.md"
    
    # Lese bestehende maintenance.md
    with open(maintenance_md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extrahiere Einleitung (alles vor "## Current Maintainerships")
    # Entferne doppelte "Current Maintainerships" falls vorhanden
    md_content_clean = re.sub(r'^## Current Maintainerships\s*\n\s*## Current Maintainerships', '## Current Maintainerships', md_content, flags=re.MULTILINE)
    intro_match = re.search(r'^(.*?)## Current Maintainerships', md_content_clean, re.DOTALL)
    if intro_match:
        intro = intro_match.group(1).rstrip()
    else:
        intro = md_content_clean.split('## Current Maintainerships')[0].rstrip()
    
    # Extrahiere Components aus maintenance.md
    md_components = extract_component_from_md(md_content)
    print(f"Extracted {len(md_components)} components from maintenance.md")
    
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
    
    # Extrahiere Authorities aus maintenance.md (primäre Quelle)
    # Mapping: folder_name -> authorities
    # Erstelle Mapping von comment_name zu component_name
    comment_to_component = {}
    for comment_name, md_data in md_components.items():
        component_name = md_data['component_name']
        comment_to_component[comment_name] = component_name
    
    # Ordne Authorities den folders zu
    for folder_name, data in components.items():
        belong_to = data.get('belong_to_component', 'None')
        component_name = folder_to_component_name.get(folder_name, folder_name)
        
        # Suche in md_components nach passendem Eintrag
        # Versuche zuerst über component_name
        found_authorities = None
        for comment_name, md_data in md_components.items():
            if md_data['component_name'] == component_name:
                found_authorities = md_data['authorities'].copy()
                break
        
        # Wenn nicht gefunden, versuche über comment_name (falls gleich folder_name)
        if not found_authorities and folder_name in md_components:
            found_authorities = md_components[folder_name]['authorities'].copy()
        
        # Wenn gefunden, setze Authorities und suche Guidelines
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
            # Auch für Components ohne Authorities (unmaintained) nach Guidelines suchen
            guidelines_link = find_guidelines_file(folder_name, component_name, base_path)
            if guidelines_link:
                authorities_dict[folder_name] = {'guidelines': f"[Guidelines]({guidelines_link})"}
            # Sonst versuche aus maintenance.json zu extrahieren (falls vorhanden)
            if data.get('has_json') and data.get('maintenance_json'):
                json_data = data['maintenance_json']
                # Extrahiere aus JSON (nur als Fallback)
                model = json_data.get('maintenance_model', 'Classic')
            first_maintainer = json_data.get('first_maintainer', '')
            second_maintainer = json_data.get('second_maintainer', '')
            tester = json_data.get('tester', '')
            testcase_writer = json_data.get('testcase_writer', '')
            
            # Parse und generiere Links
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
            
            if code_changes:
                auth_data = {
                    'conceptual': code_changes if model == 'Classic' else code_changes,
                    'code': code_changes,
                    'test_cases': [parse_user(testcase_writer)] if testcase_writer else code_changes if model == 'Classic' else [],
                    'assign_authorities': code_changes if model == 'Classic' else code_changes,
                    'tester': tester if tester else None,
                    'security_reports': code_changes[0] if code_changes else None,
                    'security_issues': code_changes[0] if code_changes else None,
                    'guidelines': None
                }
                # Suche nach Guidelines-Datei
                guidelines_link = find_guidelines_file(folder_name, component_name, base_path)
                if guidelines_link:
                    auth_data['guidelines'] = f"[Guidelines]({guidelines_link})"
                authorities_dict[folder_name] = auth_data
    
    # Gruppiere Components nach Komponenten-Namen
    grouped_by_component = defaultdict(list)
    for folder_name, data in components.items():
        component_name = folder_to_component_name.get(folder_name, folder_name)
        grouped_by_component[component_name].append(folder_name)
    
    # Organisiere nach Kategorien
    categories = defaultdict(lambda: defaultdict(list))
    
    for component_name, folders in grouped_by_component.items():
        # Bestimme Kategorie
        category = get_category_for_component(component_name)
        
        # Prüfe ob unmaintained
        is_unmaintained = all(not components.get(f, {}).get('has_json', False) for f in folders)
        
        categories[category][component_name] = {
            'folders': folders,
            'is_unmaintained': is_unmaintained
        }
    
    # Zähle maintained und unmaintained Components
    maintained_count = sum(1 for c in components.values() if c['has_json'])
    unmaintained_count = len(components) - maintained_count
    
    # Generiere neue maintenance.md
    # Entferne "## Current Maintainerships" aus intro falls vorhanden
    intro_clean = re.sub(r'\n## Current Maintainerships\s*\n', '\n', intro.rstrip())
    output_lines = [intro_clean, "", "## Current Maintainerships", ""]
    output_lines.append(f"Die folgende Struktur basiert auf der [offiziellen ILIAS-Komponentenstruktur](https://docu.ilias.de/go/wiki/wpage_1_1357).")
    output_lines.append("")
    output_lines.append(f"**Statistik:** {maintained_count} maintained Components, {unmaintained_count} unmaintained Components")
    output_lines.append("")
    
    # Sortiere Kategorien
    for cat_num in sorted(ILIAS_CATEGORIES.keys()):
        cat_name = ILIAS_CATEGORIES[cat_num]
        output_lines.append(f"### {cat_num}. {cat_name}")
        output_lines.append("")
        
        # Sortiere Komponenten alphabetisch
        component_items = sorted(categories[cat_num].items())
        
        for component_name, data in component_items:
            folders = data['folders']
            is_unmaintained = data['is_unmaintained']
            
            section = format_component_section(
                component_name,
                folders,
                authorities_dict,
                is_unmaintained
            )
            output_lines.append(section)
            output_lines.append("")
    
    # Unmaintained Components Sektion
    unmaintained = []
    for folder_name, data in components.items():
        if not data.get('has_json', False):
            unmaintained.append(folder_name)
    
    if unmaintained:
        output_lines.append("## Unmaintained Components")
        output_lines.append("")
        output_lines.append("The following directories are currently unmaintained:")
        output_lines.append("")
        for folder in sorted(unmaintained):
            output_lines.append(f"* ILIAS/{folder}")
    
    # Schreibe neue Datei
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"\nGenerated maintenance.md: {output_path}")
    print(f"Total components: {len(components)}")
    print(f"Components with maintenance.json: {sum(1 for c in components.values() if c['has_json'])}")
    print(f"Unmaintained components: {len(unmaintained)}")
    print(f"Components from maintenance.md: {len(md_components)}")

if __name__ == "__main__":
    main()
