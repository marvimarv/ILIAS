ILIAS Maintenance
=================
The development of ILIAS is coordinated by the Product Manager and the
Technical Board. Many decisions are taken at the biweekly Jour Fixe, which is
open for participation to everyone. The source code is maintained by a growing
group of people, ranging from devoted maintainers to regular or even one-time
contributors.

# Special Roles

* **Product Management**: [Matthias Kunkel](https://docu.ilias.de/go/usr/115)
* **Technical Board**: [Michael Jansen](https://docu.ilias.de/go/usr/8784), [Stephan Kergomard](https://docu.ilias.de/go/usr/44474), [Richard Klees](https://docu.ilias.de/go/usr/34047), [Nico Roeser](https://docu.ilias.de/go/usr/72730), [Fabian Schmid](https://docu.ilias.de/go/usr/21087)
* **Testcase Management**: [Fabian Kruse](https://docu.ilias.de/go/usr/27631)
* **Release Management**: [Fabian Wolf](https://docu.ilias.de/go/usr/29018)
* **Technical Documentation**: [Ann-Christin Gruber](https://docu.ilias.de/go/usr/94025)
* **Online Help**: [Alexandra Tödt](https://docu.ilias.de/go/usr/3139)

# Authorities
The ILIAS community strives to create and maintain a secure, reliable, and
adaptable learning management. We foster participation by a diverse set of
developers, designers, testers and other contributors, but we also have to
guarantee the sustainability and the quality of the ILIAS source code.

To make sure people with diverse backgrounds and capabilities can participate
in our community and contribute to the development of ILIAS and its code base,
we split the code into units (often called components, even though the term
is hard to define) and we define a set of authorities community members can have
concerning these units of code. We understand an authority as the counterpart of
a responsibility: the people having the authorities to do something in a unit of
code also assume the responsibility for the corresponding functions.

For the context of ILIAS, we define **four** different authorities:

1. **Authority to Sign off on Conceptual Changes**: The people listed here are
authorised to decide on the future course of the component. Depending on the
social organisation, this decision is taken collectively or individually. In any
case a close coordination with the people holding *the Authority to Sign off on
Code Changes* will be necessary. The people listed here are authorised to
set the checked and attendance flag for features to be discussed at the Jour Fixe.
They should be contacted first for changes to the functionality of a component.
2. **Authority to Sign off on Code Changes**: The people listed here are
authorised to contribute directly to the code base of the ILIAS core. They are
authorised to commit directly to the codebase of the ILIAS core and to merge
Pull Requests. They are the ones deciding on the structure and quality of the
code of a component.
3. **Authority to Curate Test Cases**: The people listed here are
authorised to modify and delete existing test cases. They also have the final
say on new test cases and can ask for modifications. They will be the ones
contacted if there are questions concerning the test cases for a component.
4. **Authority to (De-)Assign Authorities**: The people listed here are
authorised to assign and deassign other people to the authorities of a component
They are the only ones allowed to modify the `maintanance.json` of a component.

Each of these authorities can be held by a different set of people. This means
that the social organisation of different groups working on different parts of
the code of ILIAS can be different.
Right now ILIAS knows a few different social structures for the maintenance of
units in the code of ILIAS:

* In the **"Classic Model"** all authorities are concentrated in one person and
this person works mostly alone.
* In the **Coordinator Model** all authorities are concentrated in one or more
people and they work together with other developers in the community to improve
the code.
* In the **"Test and Assessment Model"** the authorities **to Sign off on Conceptual
Changes**, **to Curate Test Cases**, and **to (De-)Assign Authorities**
lie with one person and the **Authority to Sign off on Code Changes** with two
others.

More will surely emerge as the optimal solution for each unit is found.

# Responsibilites
Independently of the social organisation, for each [component](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/docs/development/components-and-directories.md) the following
responsibilites need to be assumed:

* All people holding an authority must agree to coordinate the development
of their [component](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/docs/development/components-and-directories.md)
with the Product Manager and with the people maintaining other units of code.
* One of the people holding either the **Authority to Sign off on Code Changes** or
the **Authority to Sign off on Conceptual Changes** gets assigned related bugs
automatically by the [Issue-Tracker](https://mantis.ilias.de). S/he is responsible
to make sure all issues receive a response within the defined time frame and are
either fixed in a timely manner or postponed/closed with a solid explanation.
* The people holding the **Authority to Sign off on Code Changes** are responsible
for pull requests to their component and get assigned related pull requests
according to the [Rules for Maintainers and Coordinators
assigned to PRs](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/docs/development/contributing.md#rules-for-community-members-assigned-to-prs).
* The person/people holding the **Authority to (De-)Assign Authorities**
coordinate assignments of authorities with the Product Manager and the Technical
Board, who hold a vetoing power over these decisions.

# Additional Rules and Guidelines
* Although the first decision on new features or feature removals in a unit of
code lie with the person/people holding the **Authority to Sign off on Conceptual
Changes** the final decisions are made by them together with the Product
Manager during the Jour Fixe meetings after an open discussion.
* If nobody holds the **Authority to (De-)Assign Authorities** for a
[component](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/docs/development/components-and-directories.md),
it defaults to the Technical Board.
* Final decision about getting write access to the ILIAS development system
(GitHub) is handled by the Product Manager together with the Technical Board.
* Authorities are listed with the name of the person holding the authority. In
addition the company the person is working for can be listed, too.
* If a company is listed for the last assignee of the **Authority to (De-)Assign
Authorities** the company can propose a prioritized candidate for the
succession.

## Process to Change Authorities
* To apply for an `Authority` of a `Component` that currently has a holder of the
`Authority to (De-)Assign Authorities`, it is recommended to contact this person
before taking the next step.
* Please provide a pull request against the `trunk`-branch of the [official ILIAS Repository](https://github.com/ILIAS-eLearning/ILIAS)
to change assignments to `Authorities` for some `Component`. Please explain in
the comment of the pull request why this change should be made. Also shortly
report your exchange with the person holding the `Authority to (De-)Assign
Authorities`, if you are not this person. Add the tags `authorities` and
`documentation`.
* The PR will be assigned to all persons with `Authorities to (De-)Assign Authority`.
These persons are asked to document in the PR if they accept the new assignment
or not. If they accept the assignment, they should also add the tag `technical board`.
* The Product Manager and the Technical Board will discuss the request as quickly
as possible. Depending on the `Authority`, the `Component`, and their role in the
community, the new assignees might be invited for a short talk to get to know them
and their plans for the `Component` better.
* If the Product Manager and the Technical Board do not veto the new assignment,
they take the pull request for the next Jour Fixe for an announcement and merge it
afterwards.
* If you want to give up an `Authority` for a `Component`, please contact all persons
with the `Authority to (De-)Assign Authorities` in that `Component`. If you are the
last person holding the `Authority to (De-)Assign Authorities`, please contact
the Product Manager and the Technical Board per email instead.
* If the person with `Authority to (De-)Assign Authorities` for a `Component` wants
to remove someone from an assignment to an `Authority` in said `Component`, she should
open a PR against the `trunk`-branch of the [official ILIAS Repository](https://github.com/ILIAS-eLearning/ILIAS)
and tag it with `authorities`, `documentation` and `jour fixe`. The change will
then be announced on the next Jour Fixe.
* If a `Component` lacks an `Authority to Sign off on Code Changes` or if the holder
of the last `Authority to Sign off on Code Chagnes` would like to pass the
responsibility over to somebody else, the `Component` is added to the agenda of
the Jour Fixe by the Product Manager.


## How Authority Assignments are Stored
Authorities are tracked in `maintenance.json` files placed in the root of the
corresponding [component](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/docs/development/components-and-directories.md)
of ILIAS. The file contains the following fields:

* **"Authority to Sign off on Conceptual Changes"**:
    An array in the form [ `<username> (<userid>, <company> (<company_page>)` ]
    pointing to valid users on https://docu.ilias.de.
* **"Authority to Sign off on Code Changes"**:
    An array in the form [ `<username> (<userid>), <company> (<company_page>)` ]
    pointing to valid users/companies on https://docu.ilias.de.
* **"Authority to Curate Test Cases"**:
    An array in the form [ `<username> (<userid>), <company> (<company_page>)` ]
    pointing to valid users on https://docu.ilias.de.
* **"Authority to (De-)Assign Authorities"**:
    An array in the form [ `<username> (<userid>), <company> (<company_page>)` ]
    pointing to valid users on https://docu.ilias.de.
* **"Tester"**:
    An array in the form [ `<username> (<userid>), <company> (<company_page>)` ]
    pointing to valid users on https://docu.ilias.de.
* **"Assignee for Issues"**:
    A string in the form `<username> (<userid>), <company> (<company_page>)`
    pointing to valid users on https://docu.ilias.de.
* **"Assignee for Security Reports"**:
    A string in the form `<username> (<userid>), <company> (<company_page>)`
    pointing to valid users on https://docu.ilias.de.
* **"Unit-specific Guidelines, Rules, and Regulations"**:
    Link to a file `COMMUNITY.md` in the root of the unity in the trunk branch on
    GitHub specifying the guidelines, rules, and regulations for collaboration.

## Current Maintainerships

Die folgende Struktur basiert auf der [offiziellen ILIAS-Komponentenstruktur](https://docu.ilias.de/go/wiki/wpage_1_1357) und organisiert alle Components nach den 9 ILIAS-Hauptkategorien. Jede Unterkomponente (z.B. "Test & Assessment", "Login, Auth & Registration") wird als eigene Sektion dargestellt, da sie eigene Maintainer haben kann. Components ohne `maintenance.json` werden als "unmaintained" markiert und alphabetisch innerhalb ihrer Kategorie aufgelistet.

**Statistik:** 177 maintained Components, 16 unmaintained Components

### 1. General Topics

[//]: # (BEGIN PrivacyTermsofServiceandDataProtectionincl.TermsofService)

#### Privacy, Terms of Service and Data Protection (incl. Terms of Service)

**Component Ordner:** `DataProtection`, `PrivacySecurity`, `TermsOfService`


[//]: # (BEGIN DataProtection)

##### DataProtection
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END DataProtection)


[//]: # (BEGIN PrivacySecurity)

##### PrivacySecurity
* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END PrivacySecurity)


[//]: # (BEGIN TermsOfService)

##### TermsOfService
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END TermsOfService)


[//]: # (END PrivacyTermsofServiceandDataProtectionincl.TermsofService)

[//]: # (BEGIN WebAccessChecker)

#### Security (incl. Web Access Checker)
**Component Ordner:** `WebAccessChecker`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [ttruffer](https://docu.ilias.de/go/usr/42894)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087), [ukohnle](https://docu.ilias.de/go/usr/21855)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END WebAccessChecker)


### 2. Accessibility, Usability and User Interface

[//]: # (BEGIN Accessibility)

#### Accessibility
**Component Ordner:** `Accessibility`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE
* Unit-specific Guidelines, Rules, and Regulations: [Guidelines](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/docs/development/accessibility.md)

[//]: # (END Accessibility)


[//]: # (BEGIN UserInterface)

#### User Interface

**Component Ordner:** `UI`, `UIComponent`, `UICore`, `UI_`


[//]: # (BEGIN UI)

##### UI
* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE
* Unit-specific Guidelines, Rules, and Regulations: [Guidelines](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md)

[//]: # (END UI)


[//]: # (BEGIN UIComponent)

##### UIComponent
* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE
* Unit-specific Guidelines, Rules, and Regulations: [Guidelines](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md)

[//]: # (END UIComponent)


[//]: # (BEGIN UICore)

##### UICore
* Authority to Sign off on Conceptual Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Security Issues: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Unit-specific Guidelines, Rules, and Regulations: [Guidelines](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md)

[//]: # (END UICore)


[//]: # (BEGIN UI_)

##### UI_
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: Fabian(27631)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Unit-specific Guidelines, Rules, and Regulations: [Guidelines](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md)

[//]: # (END UI_)


[//]: # (END UserInterface)

### 3. ILIAS core

[//]: # (BEGIN Accordion)

#### Accordion
**Component Ordner:** `Accordion`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Accordion)


[//]: # (BEGIN ActiveRecord)

#### ActiveRecord
**Component Ordner:** `ActiveRecord`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END ActiveRecord)


[//]: # (BEGIN AdvancedEditing)

#### AdvancedEditing
**Component Ordner:** `AdvancedEditing`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END AdvancedEditing)


[//]: # (BEGIN App)

#### App

**Status:** Unmaintained / NONE
**Component Ordner:** `App`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END App)


[//]: # (BEGIN AssessmentQuestion)

#### AssessmentQuestion
**Component Ordner:** `AssessmentQuestion`

* Authority to Sign off on Conceptual Changes: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Tester: SIG EA
* Assignee for Security Reports: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Assignee for Security Issues: [dstrassner](https://docu.ilias.de/go/usr/48931)

[//]: # (END AssessmentQuestion)


[//]: # (BEGIN Block)

#### Block
**Component Ordner:** `Block`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Block)


[//]: # (BEGIN CSV)

#### CSV

**Status:** Unmaintained / NONE
**Component Ordner:** `CSV`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END CSV)


[//]: # (BEGIN Cache)

#### Cache

**Status:** Unmaintained / NONE
**Component Ordner:** `Cache`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Cache)


[//]: # (BEGIN Cache_)

#### Cache_
**Component Ordner:** `Cache_`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: NONE
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Cache_)


[//]: # (BEGIN Chart)

#### Chart
**Component Ordner:** `Chart`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Chart)


[//]: # (BEGIN Cloud)

#### Cloud

**Status:** Unmaintained / NONE
**Component Ordner:** `Cloud`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Cloud)


[//]: # (BEGIN Component)

#### Components Framework
**Component Ordner:** `Component`

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END Component)


[//]: # (BEGIN Context)

#### Context
**Component Ordner:** `Context`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Context)


[//]: # (BEGIN CopyWizard)

#### CopyWizard
**Component Ordner:** `CopyWizard`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END CopyWizard)


[//]: # (BEGIN Cron)

#### Cron Service
**Component Ordner:** `Cron`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: kunkel(115)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Cron)


[//]: # (BEGIN DI)

#### DI
**Component Ordner:** `DI`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END DI)


[//]: # (BEGIN Data)

#### Data
**Component Ordner:** `Data`

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047)
* Tester: NONE
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END Data)


[//]: # (BEGIN DataSet)

#### DataSet
**Component Ordner:** `DataSet`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END DataSet)


[//]: # (BEGIN Database)

#### Database
**Component Ordner:** `Database`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END Database)


[//]: # (BEGIN Environment)

#### Environment
**Component Ordner:** `Environment`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Environment)


[//]: # (BEGIN EventHandling)

#### EventHandling
**Component Ordner:** `EventHandling`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END EventHandling)


[//]: # (BEGIN Excel)

#### Excel
**Component Ordner:** `Excel`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Excel)


[//]: # (BEGIN Exceptions)

#### Exceptions
**Component Ordner:** `Exceptions`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Exceptions)


[//]: # (BEGIN FileDelivery)

#### FileDelivery

**Status:** Unmaintained / NONE
**Component Ordner:** `FileDelivery`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END FileDelivery)


[//]: # (BEGIN FileServices)

#### FileServices

**Status:** Unmaintained / NONE
**Component Ordner:** `FileServices`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END FileServices)


[//]: # (BEGIN FileUpload)

#### FileUpload
**Component Ordner:** `FileUpload`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END FileUpload)


[//]: # (BEGIN Filesystem)

#### Filesystem
**Component Ordner:** `Filesystem`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END Filesystem)


[//]: # (BEGIN Form)

#### Form
**Component Ordner:** `Form`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Form)


[//]: # (BEGIN HTTP)

#### HTTP
**Component Ordner:** `HTTP`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END HTTP)


[//]: # (BEGIN History)

#### History
**Component Ordner:** `History`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END History)


[//]: # (BEGIN Http_)

#### Http_
**Component Ordner:** `Http_`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Http_)


[//]: # (BEGIN ResourceStorage)

#### ILIAS Resource Storage Service
**Component Ordner:** `ResourceStorage`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END ResourceStorage)


[//]: # (BEGIN ILIASObject)

#### ILIASObject
**Component Ordner:** `ILIASObject`

* Authority to Sign off on Conceptual Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to (De-)Assign Authorities: [fawinike](https://docu.ilias.de/go/usr/44474)
* Tester: NONE
* Assignee for Security Reports: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Issues: [fawinike](https://docu.ilias.de/go/usr/44474)

[//]: # (END ILIASObject)


[//]: # (BEGIN Imprint)

#### Imprint
**Component Ordner:** `Imprint`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Imprint)


[//]: # (BEGIN JavaScript)

#### JavaScript
**Component Ordner:** `JavaScript`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END JavaScript)


[//]: # (BEGIN KioskMode)

#### KioskMode
**Component Ordner:** `KioskMode`

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047)
* Tester: NONE
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END KioskMode)


[//]: # (BEGIN KioskMode_)

#### KioskMode_
**Component Ordner:** `KioskMode_`

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047)
* Tester: NONE
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END KioskMode_)


[//]: # (BEGIN LTIConsumer)

#### LTI Consumer
**Component Ordner:** `LTIConsumer`

* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Tester: NONE
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)

[//]: # (END LTIConsumer)


[//]: # (BEGIN Language)

#### Language Handling
**Component Ordner:** `Language`

* Authority to Sign off on Conceptual Changes: [kunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Authority to Sign off on Code Changes: [kunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Authority to (De-)Assign Authorities: [kunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Tester: kunkel(115)
* Assignee for Security Reports: [kunkel](https://docu.ilias.de/go/usr/115)
* Assignee for Security Issues: [kunkel](https://docu.ilias.de/go/usr/115)

[//]: # (END Language)


[//]: # (BEGIN LegalDocuments)

#### LegalDocuments
**Component Ordner:** `LegalDocuments`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END LegalDocuments)


[//]: # (BEGIN Like)

#### Like
**Component Ordner:** `Like`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: NONE
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Like)


[//]: # (BEGIN Link)

#### Link
**Component Ordner:** `Link`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Link)


[//]: # (BEGIN Locator)

#### Locator
**Component Ordner:** `Locator`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Locator)


[//]: # (BEGIN Logging)

#### Logging
**Component Ordner:** `Logging`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Logging)


[//]: # (BEGIN Math)

#### Math
**Component Ordner:** `Math`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Math)


[//]: # (BEGIN MathJax)

#### MathJax
**Component Ordner:** `MathJax`

* Authority to Sign off on Conceptual Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Sign off on Code Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Curate Test Cases: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to (De-)Assign Authorities: [fneumann](https://docu.ilias.de/go/usr/1560)
* Tester: claudio.fischer(41113)
* Assignee for Security Reports: [fneumann](https://docu.ilias.de/go/usr/1560)
* Assignee for Security Issues: [fneumann](https://docu.ilias.de/go/usr/1560)

[//]: # (END MathJax)


[//]: # (BEGIN Membership)

#### Membership
**Component Ordner:** `Membership`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Membership)


[//]: # (BEGIN Migration)

#### Migration
**Component Ordner:** `Migration`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Migration)


[//]: # (BEGIN Multilingualism)

#### Multilingualism
**Component Ordner:** `Multilingualism`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Multilingualism)


[//]: # (BEGIN DidacticTemplate)

#### Object Templates
**Component Ordner:** `DidacticTemplate`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END DidacticTemplate)


[//]: # (BEGIN Password)

#### Password
**Component Ordner:** `Password`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Password)


[//]: # (BEGIN PermanentLink)

#### Permanent Links

**Status:** Unmaintained / NONE
**Component Ordner:** `PermanentLink`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END PermanentLink)


[//]: # (BEGIN QTI)

#### QTI
**Component Ordner:** `QTI`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END QTI)


[//]: # (BEGIN AccessControl)

#### RBAC and Permissions
**Component Ordner:** `AccessControl`

* Authority to Sign off on Conceptual Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [fawinike](https://docu.ilias.de/go/usr/44474)
* Tester: kunkel(115)
* Assignee for Security Reports: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Issues: [fawinike](https://docu.ilias.de/go/usr/44474)

[//]: # (END AccessControl)


[//]: # (BEGIN RTE)

#### RTE
**Component Ordner:** `RTE`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END RTE)


[//]: # (BEGIN Randomization)

#### Randomization
**Component Ordner:** `Randomization`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Randomization)


[//]: # (BEGIN Refinery)

#### Refinery
**Component Ordner:** `Refinery`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Refinery)


[//]: # (BEGIN Saml)

#### SAML
**Component Ordner:** `Saml`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Saml)


[//]: # (BEGIN SOAPAuth)

#### SOAP
**Component Ordner:** `SOAPAuth`

* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END SOAPAuth)


[//]: # (BEGIN AuthShibboleth)

#### Shibboleth Authentication
**Component Ordner:** `AuthShibboleth`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END AuthShibboleth)


[//]: # (BEGIN StaticURL)

#### StaticURL

**Status:** Unmaintained / NONE
**Component Ordner:** `StaticURL`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END StaticURL)


[//]: # (BEGIN Style)

#### Style
**Component Ordner:** `Style`

* Authority to Sign off on Conceptual Changes: [braun](https://docu.ilias.de/go/usr/27123), [amstutz](https://docu.ilias.de/go/usr/26468)
* Authority to Sign off on Code Changes: [braun](https://docu.ilias.de/go/usr/27123), [amstutz](https://docu.ilias.de/go/usr/26468)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [braun](https://docu.ilias.de/go/usr/27123), [amstutz](https://docu.ilias.de/go/usr/26468)
* Tester: fschmid(21087)
* Assignee for Security Reports: [braun](https://docu.ilias.de/go/usr/27123)
* Assignee for Security Issues: [braun](https://docu.ilias.de/go/usr/27123)

[//]: # (END Style)


[//]: # (BEGIN Table)

#### Table
**Component Ordner:** `Table`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Table)


[//]: # (BEGIN Tree)

#### Tree
**Component Ordner:** `Tree`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Tree)


[//]: # (BEGIN Types)

#### Types

**Status:** Unmaintained / NONE
**Component Ordner:** `Types`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Types)


[//]: # (BEGIN Utilities)

#### Utilities
**Component Ordner:** `Utilities`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Utilities)


[//]: # (BEGIN Verification)

#### Verification
**Component Ordner:** `Verification`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Verification)


[//]: # (BEGIN VirusScanner)

#### VirusScanner
**Component Ordner:** `VirusScanner`

* Authority to Sign off on Conceptual Changes: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to Sign off on Code Changes: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to Curate Test Cases: [tloewen](https://docu.ilias.de/go/usr/41553)
* Authority to (De-)Assign Authorities: [rschenk](https://docu.ilias.de/go/usr/18065)
* Tester: tloewen(41553)
* Assignee for Security Reports: [rschenk](https://docu.ilias.de/go/usr/18065)
* Assignee for Security Issues: [rschenk](https://docu.ilias.de/go/usr/18065)

[//]: # (END VirusScanner)


[//]: # (BEGIN WOPI)

#### WOPI
**Component Ordner:** `WOPI`

* Authority to Sign off on Conceptual Changes: fschmid
* Authority to Sign off on Code Changes: fschmid
* Authority to Curate Test Cases: fschmid
* Authority to (De-)Assign Authorities: fschmid
* Tester: NONE
* Assignee for Security Reports: fschmid
* Assignee for Security Issues: fschmid

[//]: # (END WOPI)


[//]: # (BEGIN WebServices)

#### Web Services Overview: SOAP, REST, ...
**Component Ordner:** `WebServices`

* Authority to Sign off on Conceptual Changes: [Jephte](https://docu.ilias.de/go/usr/70542)
* Authority to Sign off on Code Changes: [Jephte](https://docu.ilias.de/go/usr/70542)
* Authority to Curate Test Cases: [Jephte](https://docu.ilias.de/go/usr/70542)
* Authority to (De-)Assign Authorities: [Jephte](https://docu.ilias.de/go/usr/70542)
* Tester: NONE
* Assignee for Security Reports: [Jephte](https://docu.ilias.de/go/usr/70542)
* Assignee for Security Issues: [Jephte](https://docu.ilias.de/go/usr/70542)

[//]: # (END WebServices)


[//]: # (BEGIN Xml)

#### Xml
**Component Ordner:** `Xml`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Xml)


[//]: # (BEGIN jQuery)

#### jQuery
**Component Ordner:** `jQuery`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END jQuery)


[//]: # (BEGIN setup_)

#### setup_

**Status:** Unmaintained / NONE
**Component Ordner:** `setup_`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END setup_)


[//]: # (BEGIN soap)

#### soap

**Status:** Unmaintained / NONE
**Component Ordner:** `soap`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END soap)


### 4. General Services

[//]: # (BEGIN BackgroundTasks)

#### Background Tasks

**Component Ordner:** `BackgroundTasks`, `BackgroundTasks_`


[//]: # (BEGIN BackgroundTasks)

##### BackgroundTasks
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END BackgroundTasks)


[//]: # (BEGIN BackgroundTasks_)

##### BackgroundTasks_
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END BackgroundTasks_)


[//]: # (END BackgroundTasks)

[//]: # (BEGIN Badge)

#### Badges
**Component Ordner:** `Badge`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: Thomas.schroeder(38330)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Badge)


[//]: # (BEGIN Calendar)

#### Calendar
**Component Ordner:** `Calendar`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Tester: berggold(22199)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Calendar)


[//]: # (BEGIN Certificate)

#### Certificate
**Component Ordner:** `Certificate`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [christian.hueser](https://docu.ilias.de/go/usr/41129)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: christian.hueser(41129)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Certificate)


[//]: # (BEGIN Skill)

#### Competence Management
**Component Ordner:** `Skill`

* Authority to Sign off on Conceptual Changes: [tfamula](https://docu.ilias.de/go/usr/58959), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [tfamula](https://docu.ilias.de/go/usr/58959), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [tfamula](https://docu.ilias.de/go/usr/58959), [akill](https://docu.ilias.de/go/usr/149)
* Tester: wolfganghuebsch(18455)
* Assignee for Security Reports: [tfamula](https://docu.ilias.de/go/usr/58959)
* Assignee for Security Issues: [tfamula](https://docu.ilias.de/go/usr/58959)

[//]: # (END Skill)


[//]: # (BEGIN Contact)

#### Contacts
**Component Ordner:** `Contact`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [suittenpointner](https://docu.ilias.de/go/usr/3458)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: abaulig1(44386)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Contact)


[//]: # (BEGIN Dashboard)

#### Dashboard
**Component Ordner:** `Dashboard`

* Authority to Sign off on Conceptual Changes: [iszmais](https://docu.ilias.de/go/usr/65630), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [iszmais](https://docu.ilias.de/go/usr/65630), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [iszmais](https://docu.ilias.de/go/usr/65630), [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [iszmais](https://docu.ilias.de/go/usr/65630)
* Assignee for Security Issues: [iszmais](https://docu.ilias.de/go/usr/65630)

[//]: # (END Dashboard)


[//]: # (BEGIN ECSInterface)

#### ECS Interface

**Component Ordner:** `RemoteCategory`, `RemoteCourse`, `RemoteFile`, `RemoteGlossary`, `RemoteGroup`, `RemoteLearningModule`, `RemoteTest`, `RemoteWiki`


[//]: # (BEGIN RemoteCategory)

##### RemoteCategory
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: [bogen](https://docu.ilias.de/go/usr/13815)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: bogen(13815)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END RemoteCategory)


[//]: # (BEGIN RemoteCourse)

##### RemoteCourse
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: [bogen](https://docu.ilias.de/go/usr/13815)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: bogen(13815)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END RemoteCourse)


[//]: # (BEGIN RemoteFile)

##### RemoteFile
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: [bogen](https://docu.ilias.de/go/usr/13815)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: bogen(13815)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END RemoteFile)


[//]: # (BEGIN RemoteGlossary)

##### RemoteGlossary
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: [bogen](https://docu.ilias.de/go/usr/13815)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: bogen(13815)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END RemoteGlossary)


[//]: # (BEGIN RemoteGroup)

##### RemoteGroup
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: [bogen](https://docu.ilias.de/go/usr/13815)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: bogen(13815)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END RemoteGroup)


[//]: # (BEGIN RemoteLearningModule)

##### RemoteLearningModule
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: [bogen](https://docu.ilias.de/go/usr/13815)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: bogen(13815)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END RemoteLearningModule)


[//]: # (BEGIN RemoteTest)

##### RemoteTest
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: [bogen](https://docu.ilias.de/go/usr/13815)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: bogen(13815)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END RemoteTest)


[//]: # (BEGIN RemoteWiki)

##### RemoteWiki
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: [bogen](https://docu.ilias.de/go/usr/13815)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: bogen(13815)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END RemoteWiki)


[//]: # (END ECSInterface)

[//]: # (BEGIN Export)

#### Export
**Component Ordner:** `Export`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: Fabian(27631)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Export)


[//]: # (BEGIN GlobalCache)

#### Global Cache

**Component Ordner:** `GlobalCache`, `GlobalCache_`


[//]: # (BEGIN GlobalCache)

##### GlobalCache
* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END GlobalCache)


[//]: # (BEGIN GlobalCache_)

##### GlobalCache_
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END GlobalCache_)


[//]: # (END GlobalCache)

[//]: # (BEGIN GlobalScreenService)

#### Global Screen Service

**Component Ordner:** `GlobalScreen`, `GlobalScreen_`


[//]: # (BEGIN GlobalScreen)

##### GlobalScreen
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END GlobalScreen)


[//]: # (BEGIN GlobalScreen_)

##### GlobalScreen_
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END GlobalScreen_)


[//]: # (END GlobalScreenService)

[//]: # (BEGIN COPage)

#### ILIAS Page Editor
**Component Ordner:** `COPage`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: FH Aachen
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END COPage)


[//]: # (BEGIN InfoScreen)

#### Info Page
**Component Ordner:** `InfoScreen`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END InfoScreen)


[//]: # (BEGIN LearningHistory)

#### Learning History
**Component Ordner:** `LearningHistory`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: oliver.samoila(26160)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END LearningHistory)


[//]: # (BEGIN MainMenu)

#### Main Menu
**Component Ordner:** `MainMenu`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END MainMenu)


[//]: # (BEGIN Maps)

#### Maps
**Component Ordner:** `Maps`

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047), [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047), [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047), [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Tester: miriamhoelscher(25370)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END Maps)


[//]: # (BEGIN Metadata)

#### Metadata

**Component Ordner:** `ADT`, `AdvancedMetaData`, `MetaData`


[//]: # (BEGIN ADT)

##### ADT
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [abaulig1](https://docu.ilias.de/go/usr/44386)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: abaulig1(44386)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END ADT)


[//]: # (BEGIN AdvancedMetaData)

##### AdvancedMetaData
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [abaulig1](https://docu.ilias.de/go/usr/44386)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: abaulig1(44386)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END AdvancedMetaData)


[//]: # (BEGIN MetaData)

##### MetaData
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [abaulig1](https://docu.ilias.de/go/usr/44386)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: abaulig1(44386)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END MetaData)


[//]: # (END Metadata)

[//]: # (BEGIN Notes)

#### Notes and Comments
**Component Ordner:** `Notes`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [skaiser](https://docu.ilias.de/go/usr/17260)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: skaiser(17260)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Notes)


[//]: # (BEGIN Help)

#### Online Help
**Component Ordner:** `Help`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: atoedt(3139)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Help)


[//]: # (BEGIN OrgUnit)

#### Organisational Units
**Component Ordner:** `OrgUnit`

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [wischniak](https://docu.ilias.de/go/usr/21896)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: wischniak(21896)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END OrgUnit)


[//]: # (BEGIN PersonalandSharedResources)

#### Personal and Shared Resources

**Component Ordner:** `PersonalWorkspace`, `WorkspaceFolder`, `WorkspaceRootFolder`


[//]: # (BEGIN PersonalWorkspace)

##### PersonalWorkspace
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: KlausVorkauf(5890)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END PersonalWorkspace)


[//]: # (BEGIN WorkspaceFolder)

##### WorkspaceFolder
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: KlausVorkauf(5890)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END WorkspaceFolder)


[//]: # (BEGIN WorkspaceRootFolder)

##### WorkspaceRootFolder
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: KlausVorkauf(5890)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END WorkspaceRootFolder)


[//]: # (END PersonalandSharedResources)

[//]: # (BEGIN Portfolio)

#### Portfolio
**Component Ordner:** `Portfolio`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [KlausVorkauf](https://docu.ilias.de/go/usr/5890)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: KlausVorkauf(5890)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Portfolio)


[//]: # (BEGIN Conditions)

#### Precondition Handling
**Component Ordner:** `Conditions`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Tester: kunkel(115)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Conditions)


[//]: # (BEGIN Rating)

#### Rating
**Component Ordner:** `Rating`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: Fabian(27631)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Rating)


[//]: # (BEGIN Search)

#### Search
**Component Ordner:** `Search`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: Future Learning
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Search)


[//]: # (BEGIN MyStaff)

#### Staff
**Component Ordner:** `MyStaff`

* Authority to Sign off on Conceptual Changes: [tfamula](https://docu.ilias.de/go/usr/58959), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Sign off on Code Changes: [tfamula](https://docu.ilias.de/go/usr/58959), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Curate Test Cases: [tfamula](https://docu.ilias.de/go/usr/58959), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to (De-)Assign Authorities: [tfamula](https://docu.ilias.de/go/usr/58959), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Tester: qualitus.morgunova(69410)
* Assignee for Security Reports: [tfamula](https://docu.ilias.de/go/usr/58959)
* Assignee for Security Issues: [tfamula](https://docu.ilias.de/go/usr/58959)

[//]: # (END MyStaff)


[//]: # (BEGIN Tracking)

#### Statistics and Learning Progress
**Component Ordner:** `Tracking`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [bromberger](https://docu.ilias.de/go/usr/198)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: suittenpointner(3458)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Tracking)


[//]: # (BEGIN Tagging)

#### Tagging
**Component Ordner:** `Tagging`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [mstuder](https://docu.ilias.de/go/usr/8473)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [mstuder](https://docu.ilias.de/go/usr/8473)
* Authority to Curate Test Cases: [skaiser](https://docu.ilias.de/go/usr/17260)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [mstuder](https://docu.ilias.de/go/usr/8473)
* Tester: skaiser(17260)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Tagging)


[//]: # (BEGIN Tasks)

#### Task Service
**Component Ordner:** `Tasks`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: NONE
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Tasks)


[//]: # (BEGIN Taxonomy)

#### Taxonomy Service
**Component Ordner:** `Taxonomy`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: Tested separately in each module that supports taxonomies
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: Tested separately in each module that supports taxonomies
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Taxonomy)


[//]: # (BEGIN User)

#### User Service
**Component Ordner:** `User`

* Authority to Sign off on Conceptual Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to (De-)Assign Authorities: [fawinike](https://docu.ilias.de/go/usr/44474)
* Tester: NONE
* Assignee for Security Reports: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Issues: [fawinike](https://docu.ilias.de/go/usr/44474)

[//]: # (END User)


[//]: # (BEGIN WebDAV)

#### WebDAV
**Component Ordner:** `WebDAV`

* Authority to Sign off on Conceptual Changes: [fawinike](https://docu.ilias.de/go/usr/44474), [rheer](https://docu.ilias.de/go/usr/47872)
* Authority to Sign off on Code Changes: [fawinike](https://docu.ilias.de/go/usr/44474), [rheer](https://docu.ilias.de/go/usr/47872)
* Authority to Curate Test Cases: [fawinike](https://docu.ilias.de/go/usr/44474), [rheer](https://docu.ilias.de/go/usr/47872)
* Authority to (De-)Assign Authorities: [fawinike](https://docu.ilias.de/go/usr/44474), [rheer](https://docu.ilias.de/go/usr/47872)
* Tester: NONE
* Assignee for Security Reports: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Issues: [fawinike](https://docu.ilias.de/go/usr/44474)

[//]: # (END WebDAV)


[//]: # (BEGIN Awareness)

#### Who is online?
**Component Ordner:** `Awareness`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: amersch(15114)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Awareness)


### 5. Container Objects

[//]: # (BEGIN CategoryandRepository)

#### Category and Repository

**Component Ordner:** `Category`, `CategoryReference`, `Container`, `ContainerReference`, `Folder`, `Repository`, `RootFolder`


[//]: # (BEGIN Category)

##### Category
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: miriamhoelscher(25370)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Category)


[//]: # (BEGIN CategoryReference)

##### CategoryReference
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: miriamhoelscher(25370)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END CategoryReference)


[//]: # (BEGIN Container)

##### Container
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: miriamhoelscher(25370)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Container)


[//]: # (BEGIN ContainerReference)

##### ContainerReference
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: miriamhoelscher(25370)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END ContainerReference)


[//]: # (BEGIN Folder)

##### Folder
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: miriamhoelscher(25370)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Folder)


[//]: # (BEGIN Repository)

##### Repository
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: miriamhoelscher(25370)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Repository)


[//]: # (BEGIN RootFolder)

##### RootFolder
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: miriamhoelscher(25370)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END RootFolder)


[//]: # (END CategoryandRepository)

[//]: # (BEGIN CourseManagement)

#### Course Management

**Component Ordner:** `Course`, `CourseReference`


[//]: # (BEGIN Course)

##### Course
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Course)


[//]: # (BEGIN CourseReference)

##### CourseReference
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END CourseReference)


[//]: # (END CourseManagement)

[//]: # (BEGIN Group)

#### Group

**Component Ordner:** `Group`, `GroupReference`


[//]: # (BEGIN Group)

##### Group
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Group)


[//]: # (BEGIN GroupReference)

##### GroupReference
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END GroupReference)


[//]: # (END Group)

[//]: # (BEGIN ItemGroup)

#### Item Groups
**Component Ordner:** `ItemGroup`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [berggold](https://docu.ilias.de/go/usr/22199)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: berggold(22199)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END ItemGroup)


[//]: # (BEGIN LearningSequence)

#### Learning Sequence
**Component Ordner:** `LearningSequence`

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Curate Test Cases: [scarlino](https://docu.ilias.de/go/usr/56074)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047)
* Tester: mglaubitz(28309)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END LearningSequence)


[//]: # (BEGIN Session)

#### Session
**Component Ordner:** `Session`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Session)


[//]: # (BEGIN StudyProgramme)

#### Study Programme

**Component Ordner:** `StudyProgramme`, `StudyProgrammeReference`


[//]: # (BEGIN StudyProgramme)

##### StudyProgramme
* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047), [shecken](https://docu.ilias.de/go/usr/45419)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047), [shecken](https://docu.ilias.de/go/usr/45419)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047), [shecken](https://docu.ilias.de/go/usr/45419)
* Tester: mstuder(8473)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END StudyProgramme)


[//]: # (BEGIN StudyProgrammeReference)

##### StudyProgrammeReference
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END StudyProgrammeReference)


[//]: # (END StudyProgramme)

### 6. Communication and Syndication

[//]: # (BEGIN AdministrativeNotification)

#### Administrative Notifications

**Status:** Unmaintained / NONE
**Component Ordner:** `AdministrativeNotification`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END AdministrativeNotification)


[//]: # (BEGIN Chat)

#### Chat

**Component Ordner:** `Chatroom`, `Notifications`, `OnScreenChat`


[//]: # (BEGIN Chatroom)

##### Chatroom
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Tester: elena(49160)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Chatroom)


[//]: # (BEGIN Notifications)

##### Notifications
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Tester: abaulig1(44386)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Notifications)


[//]: # (BEGIN OnScreenChat)

##### OnScreenChat
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Tester: abaulig1(44386)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END OnScreenChat)


[//]: # (END Chat)

[//]: # (BEGIN Forum)

#### Forum

**Component Ordner:** `Forum`, `Html`


[//]: # (BEGIN Forum)

##### Forum
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Tester: e.paulmann(8645)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Forum)


[//]: # (BEGIN Html)

##### Html
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Tester: e.paulmann(8645)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Html)


[//]: # (END Forum)

[//]: # (BEGIN Mail)

#### Mail
**Component Ordner:** `Mail`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Authority to Curate Test Cases: [amersch](https://docu.ilias.de/go/usr/15114)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Tester: amersch(15114)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Mail)


[//]: # (BEGIN News)

#### News
**Component Ordner:** `News`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [Thomas.schroeder](https://docu.ilias.de/go/usr/38330)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: Thomas.schroeder(38330)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END News)


[//]: # (BEGIN Feeds)

#### News - RSS - Webfeeds
**Component Ordner:** `Feeds`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: kunkel(115)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Feeds)


[//]: # (BEGIN Notification)

#### Notifications
**Component Ordner:** `Notification`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Notification)


### 7. Learning and Content Objects

[//]: # (BEGIN Bibliographic)

#### Bibliographic List Item
**Component Ordner:** `Bibliographic`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [mstuder](https://docu.ilias.de/go/usr/8473)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: marko.glaubitz(28309)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END Bibliographic)


[//]: # (BEGIN Blog)

#### Blog
**Component Ordner:** `Blog`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [KlausVorkauf](https://docu.ilias.de/go/usr/5890)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: PaBer(33766)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Blog)


[//]: # (BEGIN BookingManager)

#### Booking Pool
**Component Ordner:** `BookingManager`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [e.coroian](https://docu.ilias.de/go/usr/37215)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: wolfganghuebsch(18455)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END BookingManager)


[//]: # (BEGIN ContentPage)

#### Content Page
**Component Ordner:** `ContentPage`

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END ContentPage)


[//]: # (BEGIN DataCollection)

#### Data Collection
**Component Ordner:** `DataCollection`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END DataCollection)


[//]: # (BEGIN File)

#### File
**Component Ordner:** `File`

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [tloewen](https://docu.ilias.de/go/usr/41553)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: tloewen(41553)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END File)


[//]: # (BEGIN Glossary)

#### Glossary
**Component Ordner:** `Glossary`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: atoedt(3139)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Glossary)


[//]: # (BEGIN LTIProvider)

#### LTI
**Component Ordner:** `LTIProvider`

* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: atoedt(3139)
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)

[//]: # (END LTIProvider)


[//]: # (BEGIN HTMLLearningModule)

#### Learning Module HTML
**Component Ordner:** `HTMLLearningModule`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [suittenpointner](https://docu.ilias.de/go/usr/3458)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: suittenpointner(3458)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END HTMLLearningModule)


[//]: # (BEGIN LearningModule)

#### Learning Module ILIAS
**Component Ordner:** `LearningModule`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [Balliel](https://docu.ilias.de/go/usr/18365)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: Balliel(18365)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END LearningModule)


[//]: # (BEGIN LearningModuleSCORM)

#### Learning Module SCORM

**Component Ordner:** `Scorm2004`, `ScormAicc`


[//]: # (BEGIN Scorm2004)

##### Scorm2004
* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [suittenpointner](https://docu.ilias.de/go/usr/3458)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Tester: suittenpointner(3458)
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)

[//]: # (END Scorm2004)


[//]: # (BEGIN ScormAicc)

##### ScormAicc
* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [suittenpointner](https://docu.ilias.de/go/usr/3458)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Tester: suittenpointner(3458)
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)

[//]: # (END ScormAicc)


[//]: # (END LearningModuleSCORM)

[//]: # (BEGIN MediaPoolsandMediaObjects)

#### Media Pools and Media Objects

**Component Ordner:** `MediaObjects`, `MediaPool`


[//]: # (BEGIN MediaObjects)

##### MediaObjects
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: kunkel(115)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END MediaObjects)


[//]: # (BEGIN MediaPool)

##### MediaPool
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: kunkel(115)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END MediaPool)


[//]: # (END MediaPoolsandMediaObjects)

[//]: # (BEGIN MediaCast)

#### Mediacast
**Component Ordner:** `MediaCast`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [berggold](https://docu.ilias.de/go/usr/22199)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: berggold(22199)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END MediaCast)


[//]: # (BEGIN WebResource)

#### Weblink
**Component Ordner:** `WebResource`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [nadine.bauser](https://docu.ilias.de/go/usr/34662)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: nadine.bauser(34662)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END WebResource)


[//]: # (BEGIN Wiki)

#### Wiki
**Component Ordner:** `Wiki`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [abaulig1](https://docu.ilias.de/go/usr/44386)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: abaulig1(44386)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Wiki)


[//]: # (BEGIN CmiXapi)

#### xAPI
**Component Ordner:** `CmiXapi`

* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Tester: NONE
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)

[//]: # (END CmiXapi)


### 8. Evaluation, Feedback and Testing

[//]: # (BEGIN EmployeeTalk)

#### Employee Talk
**Component Ordner:** `EmployeeTalk`

* Authority to Sign off on Conceptual Changes: [tschmitz](https://docu.ilias.de/go/usr/92591), [tfamula](https://docu.ilias.de/go/usr/58959)
* Authority to Sign off on Code Changes: [tschmitz](https://docu.ilias.de/go/usr/92591), [tfamula](https://docu.ilias.de/go/usr/58959)
* Authority to Curate Test Cases: [tschmitz](https://docu.ilias.de/go/usr/92591), [tfamula](https://docu.ilias.de/go/usr/58959)
* Authority to (De-)Assign Authorities: [tschmitz](https://docu.ilias.de/go/usr/92591), [tfamula](https://docu.ilias.de/go/usr/58959)
* Tester: qualitus.morgunova(69410)
* Assignee for Security Reports: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Assignee for Security Issues: [tschmitz](https://docu.ilias.de/go/usr/92591)

[//]: # (END EmployeeTalk)


[//]: # (BEGIN Exercise)

#### Exercise
**Component Ordner:** `Exercise`

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [KlausVorkauf](https://docu.ilias.de/go/usr/5890)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: miriamwegener(23051)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Exercise)


[//]: # (BEGIN IndividualAssessment)

#### Individual Assessment
**Component Ordner:** `IndividualAssessment`

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047), [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047), [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Authority to Curate Test Cases: [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047), [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Tester: kunkel(115)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END IndividualAssessment)


[//]: # (BEGIN Poll)

#### Poll
**Component Ordner:** `Poll`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: Future Learning
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Poll)


[//]: # (BEGIN Survey)

#### Survey

**Component Ordner:** `Survey`, `SurveyQuestionPool`


[//]: # (BEGIN Survey)

##### Survey
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [Xus](https://docu.ilias.de/go/usr/50418)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [Xus](https://docu.ilias.de/go/usr/50418)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [Xus](https://docu.ilias.de/go/usr/50418)
* Tester: e.coroian(37215)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Survey)


[//]: # (BEGIN SurveyQuestionPool)

##### SurveyQuestionPool
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [Xus](https://docu.ilias.de/go/usr/50418)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [Xus](https://docu.ilias.de/go/usr/50418)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [Xus](https://docu.ilias.de/go/usr/50418)
* Tester: e.coroian(37215)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END SurveyQuestionPool)


[//]: # (END Survey)

[//]: # (BEGIN TestAssessment)

#### Test & Assessment

**Component Ordner:** `Test`, `TestQuestionPool`


[//]: # (BEGIN Test)

##### Test
* Authority to Sign off on Conceptual Changes: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Tester: SIG EA
* Assignee for Security Reports: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Assignee for Security Issues: [dstrassner](https://docu.ilias.de/go/usr/48931)

[//]: # (END Test)


[//]: # (BEGIN TestQuestionPool)

##### TestQuestionPool
* Authority to Sign off on Conceptual Changes: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Tester: SIG EA
* Assignee for Security Reports: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Assignee for Security Issues: [dstrassner](https://docu.ilias.de/go/usr/48931)

[//]: # (END TestQuestionPool)


[//]: # (END TestAssessment)

### 9. Administration

[//]: # (BEGIN Administration)

#### Administration

**Component Ordner:** `Administration`, `SystemFolder`


[//]: # (BEGIN Administration)

##### Administration
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: kunkel(115)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Administration)


[//]: # (BEGIN SystemFolder)

##### SystemFolder
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: kunkel(115)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END SystemFolder)


[//]: # (END Administration)

[//]: # (BEGIN LoginAuthRegistration)

#### Login, Auth & Registration

**Component Ordner:** `AuthApache`, `Authentication`, `CAS`, `Init`, `LDAP`, `OpenIdConnect`, `Registration`


[//]: # (BEGIN AuthApache)

##### AuthApache
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: vimotion(25105)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END AuthApache)


[//]: # (BEGIN Authentication)

##### Authentication
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: vimotion(25105)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END Authentication)


[//]: # (BEGIN CAS)

##### CAS
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: vimotion(25105)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END CAS)


[//]: # (BEGIN Init)

##### Init
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: vimotion(25105)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END Init)


[//]: # (BEGIN LDAP)

##### LDAP
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: vimotion(25105)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END LDAP)


[//]: # (BEGIN OpenIdConnect)

##### OpenIdConnect
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: NONE
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END OpenIdConnect)


[//]: # (BEGIN Registration)

##### Registration
* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Tester: vimotion(25105)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END Registration)


[//]: # (END LoginAuthRegistration)

[//]: # (BEGIN Setup)

#### Setup

**Status:** Unmaintained / NONE
**Component Ordner:** `Setup`

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Setup)


[//]: # (BEGIN SystemCheck)

#### System Check
**Component Ordner:** `SystemCheck`

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END SystemCheck)


## Unmaintained Components

The following directories are currently unmaintained:

* ILIAS/AdministrativeNotification
* ILIAS/App
* ILIAS/CSV
* ILIAS/Cache
* ILIAS/Cloud
* ILIAS/FileDelivery
* ILIAS/FileServices
* ILIAS/GlobalCache
* ILIAS/PermanentLink
* ILIAS/Setup
* ILIAS/StaticURL
* ILIAS/StudyProgrammeReference
* ILIAS/Types
* ILIAS/UI_
* ILIAS/setup_
* ILIAS/soap