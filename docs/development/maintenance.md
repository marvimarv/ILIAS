ILIAS Maintenance
=================
The development of ILIAS is coordinated by the Product Manager and the
Technical Board. Many decisions are taken at the biweekly Jour Fixe, which is
open for participation to everyone. The source code is maintained by a growing
group of people, ranging from devoted maintainers to regular or even one-time
contributors.

# Special Roles

* **Product Management**: [Matthias Kunkel](https://docu.ilias.de/go/usr/115)
* **Technical Board**: [Rob Falkenstein](https://docu.ilias.de/go/usr/63946), [Marvin Hackfort](https://docu.ilias.de/go/usr/50523), [Michael Jansen](https://docu.ilias.de/go/usr/8784), [Franziska Wandelmaier](https://docu.ilias.de/go/usr/33833)
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
* If the person holding the **Authority to (De-)Assign Authorities** assigns a new **Authority to Curate Test Cases** the Testcase Management MUST be informed about the change.

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

Die folgende Struktur basiert auf der [offiziellen ILIAS-Komponentenstruktur](https://docu.ilias.de/go/wiki/wpage_1_1357).

**Statistik:** 163 maintained Components, 17 unmaintained Components, 308 NONE Authority-Einträge

### 1. [General Topics](https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#1_General_Topics)

[//]: # (BEGIN PrivacyTermsofServiceandDataProtectionincl.TermsofService)

#### [Privacy, Terms of Service and Data Protection (incl. Terms of Service)](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`DataProtection`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DataProtection), [`PrivacySecurity`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/PrivacySecurity), [`TermsOfService`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/TermsOfService)


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

#### [Security (incl. Web Access Checker)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`WebAccessChecker`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WebAccessChecker)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [ttruffer](https://docu.ilias.de/go/usr/42894)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087), [ukohnle](https://docu.ilias.de/go/usr/21855)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END WebAccessChecker)


### 2. [Accessibility, Usability and User Interface](https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#2_Accessibility_Usability_and_User_Interface)

[//]: # (BEGIN Accessibility)

#### [Accessibility](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Accessibility`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Accessibility)

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

#### [User Interface](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`UI`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/UI), [`UIComponent`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/UIComponent), [`UICore`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/UICore), [`UI_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/UI_)


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

### 3. [ILIAS core](https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#3_ILIAS_core)

[//]: # (BEGIN Accordion)

#### [Accordion](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Accordion`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Accordion)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Accordion)


[//]: # (BEGIN ActiveRecord)

#### [ActiveRecord](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`ActiveRecord`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ActiveRecord)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END ActiveRecord)


[//]: # (BEGIN App)

#### [App](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`App`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/App)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END App)


[//]: # (BEGIN Benchmark)

#### [Benchmark](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`Benchmark`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Benchmark)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Benchmark)


[//]: # (BEGIN CSV)

#### [CSV](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`CSV`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CSV)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END CSV)


[//]: # (BEGIN Cache)

#### [Cache](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`Cache`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Cache)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Cache)


[//]: # (BEGIN Chart)

#### [Chart](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Chart`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Chart)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Chart)


[//]: # (BEGIN Cloud)

#### [Cloud](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`Cloud`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Cloud)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Cloud)


[//]: # (BEGIN Component)

#### [Components Framework](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Component`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Component)

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END Component)


[//]: # (BEGIN Context)

#### [Context](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Context`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Context)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Context)


[//]: # (BEGIN Cron)

#### [Cron Service](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Cron`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Cron)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: kunkel(115)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Cron)


[//]: # (BEGIN DI)

#### [DI](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`DI`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DI)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END DI)


[//]: # (BEGIN Data)

#### [Data](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Data`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Data)

* Authority to Sign off on Conceptual Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [lscharmer](https://docu.ilias.de/go/usr/87863)
* Assignee for Security Issues: [lscharmer](https://docu.ilias.de/go/usr/87863)

[//]: # (END Data)


[//]: # (BEGIN Database)

#### [Database](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Database`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Database)

* Authority to Sign off on Conceptual Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [lscharmer](https://docu.ilias.de/go/usr/87863), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [lscharmer](https://docu.ilias.de/go/usr/87863), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [lscharmer](https://docu.ilias.de/go/usr/87863)
* Assignee for Security Issues: [lscharmer](https://docu.ilias.de/go/usr/87863)

[//]: # (END Database)


[//]: # (BEGIN Environment)

#### [Environment](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Environment`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Environment)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Environment)


[//]: # (BEGIN EventHandling)

#### [EventHandling](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`EventHandling`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/EventHandling)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END EventHandling)


[//]: # (BEGIN Excel)

#### [Excel](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Excel`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Excel)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Excel)


[//]: # (BEGIN Exceptions)

#### [Exceptions](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Exceptions`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Exceptions)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Exceptions)


[//]: # (BEGIN FileDelivery)

#### [FileDelivery](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`FileDelivery`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/FileDelivery)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END FileDelivery)


[//]: # (BEGIN FileServices)

#### [FileServices](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`FileServices`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/FileServices)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END FileServices)


[//]: # (BEGIN FileUpload)

#### [FileUpload](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`FileUpload`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/FileUpload)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END FileUpload)


[//]: # (BEGIN Filesystem)

#### [Filesystem](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Filesystem`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Filesystem)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END Filesystem)


[//]: # (BEGIN Form)

#### [Form](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Form`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Form)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Form)


[//]: # (BEGIN HTTP)

#### [HTTP](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`HTTP`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/HTTP)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END HTTP)


[//]: # (BEGIN History)

#### [History](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`History`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/History)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END History)


[//]: # (BEGIN Http_)

#### [Http_](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Http_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Http_)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Http_)


[//]: # (BEGIN ResourceStorage)

#### [ILIAS Resource Storage Service](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`ResourceStorage`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ResourceStorage)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END ResourceStorage)


[//]: # (BEGIN ILIASObject)

#### [ILIASObject](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`ILIASObject`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ILIASObject)

* Authority to Sign off on Conceptual Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to (De-)Assign Authorities: [fawinike](https://docu.ilias.de/go/usr/44474)
* Tester: NONE
* Assignee for Security Reports: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Issues: [fawinike](https://docu.ilias.de/go/usr/44474)

[//]: # (END ILIASObject)


[//]: # (BEGIN Imprint)

#### [Imprint](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Imprint`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Imprint)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Imprint)


[//]: # (BEGIN JavaScript)

#### [JavaScript](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`JavaScript`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/JavaScript)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END JavaScript)


[//]: # (BEGIN KioskMode)

#### [KioskMode](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`KioskMode`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/KioskMode)

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047)
* Tester: NONE
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END KioskMode)


[//]: # (BEGIN KioskMode_)

#### [KioskMode_](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`KioskMode_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/KioskMode_)

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047)
* Tester: NONE
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END KioskMode_)


[//]: # (BEGIN LTIConsumer)

#### [LTI Consumer](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`LTIConsumer`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LTIConsumer)

* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Tester: NONE
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)

[//]: # (END LTIConsumer)


[//]: # (BEGIN Language)

#### [Language Handling](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Language`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Language)

* Authority to Sign off on Conceptual Changes: [kunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Authority to Sign off on Code Changes: [kunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Authority to (De-)Assign Authorities: [kunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Tester: kunkel(115)
* Assignee for Security Reports: [kunkel](https://docu.ilias.de/go/usr/115)
* Assignee for Security Issues: [kunkel](https://docu.ilias.de/go/usr/115)

[//]: # (END Language)


[//]: # (BEGIN LegalDocuments)

#### [LegalDocuments](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`LegalDocuments`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LegalDocuments)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END LegalDocuments)


[//]: # (BEGIN Like)

#### [Like](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Like`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Like)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: NONE
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Like)


[//]: # (BEGIN Link)

#### [Link](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Link`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Link)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Link)


[//]: # (BEGIN Locator)

#### [Locator](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Locator`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Locator)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Locator)


[//]: # (BEGIN Logging)

#### [Logging](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Logging`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Logging)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Logging)


[//]: # (BEGIN Math)

#### [Math](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Math`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Math)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Math)


[//]: # (BEGIN Membership)

#### [Membership](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Membership`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Membership)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Membership)


[//]: # (BEGIN Migration)

#### [Migration](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Migration`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Migration)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Migration)


[//]: # (BEGIN Multilingualism)

#### [Multilingualism](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`Multilingualism`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Multilingualism)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Multilingualism)


[//]: # (BEGIN DidacticTemplate)

#### [Object Templates](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`DidacticTemplate`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DidacticTemplate)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END DidacticTemplate)


[//]: # (BEGIN Password)

#### [Password](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Password`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Password)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Password)


[//]: # (BEGIN PermanentLink)

#### [Permanent Links](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`PermanentLink`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/PermanentLink)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END PermanentLink)


[//]: # (BEGIN AccessControl)

#### [RBAC and Permissions](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`AccessControl`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AccessControl)

* Authority to Sign off on Conceptual Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [fawinike](https://docu.ilias.de/go/usr/44474)
* Tester: kunkel(115)
* Assignee for Security Reports: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Issues: [fawinike](https://docu.ilias.de/go/usr/44474)

[//]: # (END AccessControl)


[//]: # (BEGIN RTE)

#### [RTE](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`RTE`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RTE)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END RTE)


[//]: # (BEGIN Refinery)

#### [Refinery](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Refinery`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Refinery)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Refinery)


[//]: # (BEGIN Saml)

#### [SAML](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Saml`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Saml)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Saml)


[//]: # (BEGIN AuthSOAP)

#### [SOAP](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`AuthSOAP`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AuthSOAP)

* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)
* Assignee for Security Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492)

[//]: # (END AuthSOAP)


[//]: # (BEGIN AuthShibboleth)

#### [Shibboleth Authentication](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`AuthShibboleth`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AuthShibboleth)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END AuthShibboleth)


[//]: # (BEGIN StaticURL)

#### [StaticURL](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`StaticURL`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/StaticURL)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END StaticURL)


[//]: # (BEGIN Style)

#### [Style](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Style`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Style)

* Authority to Sign off on Conceptual Changes: [braun](https://docu.ilias.de/go/usr/27123), [amstutz](https://docu.ilias.de/go/usr/26468)
* Authority to Sign off on Code Changes: [braun](https://docu.ilias.de/go/usr/27123), [amstutz](https://docu.ilias.de/go/usr/26468)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [braun](https://docu.ilias.de/go/usr/27123), [amstutz](https://docu.ilias.de/go/usr/26468)
* Tester: fschmid(21087)
* Assignee for Security Reports: [braun](https://docu.ilias.de/go/usr/27123)
* Assignee for Security Issues: [braun](https://docu.ilias.de/go/usr/27123)

[//]: # (END Style)


[//]: # (BEGIN Table)

#### [Table](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Table`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Table)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Table)


[//]: # (BEGIN Tree)

#### [Tree](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Tree`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Tree)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Tree)


[//]: # (BEGIN Utilities)

#### [Utilities](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Utilities`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Utilities)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Utilities)


[//]: # (BEGIN Verification)

#### [Verification](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Verification`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Verification)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Verification)


[//]: # (BEGIN VirusScanner)

#### [VirusScanner](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`VirusScanner`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/VirusScanner)

* Authority to Sign off on Conceptual Changes: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to Sign off on Code Changes: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to Curate Test Cases: [tloewen](https://docu.ilias.de/go/usr/41553)
* Authority to (De-)Assign Authorities: [rschenk](https://docu.ilias.de/go/usr/18065)
* Tester: tloewen(41553)
* Assignee for Security Reports: [rschenk](https://docu.ilias.de/go/usr/18065)
* Assignee for Security Issues: [rschenk](https://docu.ilias.de/go/usr/18065)

[//]: # (END VirusScanner)


[//]: # (BEGIN WOPI)

#### [WOPI](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`WOPI`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WOPI)

* Authority to Sign off on Conceptual Changes: fschmid
* Authority to Sign off on Code Changes: fschmid
* Authority to Curate Test Cases: fschmid
* Authority to (De-)Assign Authorities: fschmid
* Tester: NONE
* Assignee for Security Reports: fschmid
* Assignee for Security Issues: fschmid

[//]: # (END WOPI)


[//]: # (BEGIN WebServices)

#### [Web Services Overview: SOAP, REST, ...](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`WebServices`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WebServices)

* Authority to Sign off on Conceptual Changes: [Jephte](https://docu.ilias.de/go/usr/70542)
* Authority to Sign off on Code Changes: [Jephte](https://docu.ilias.de/go/usr/70542)
* Authority to Curate Test Cases: [Jephte](https://docu.ilias.de/go/usr/70542)
* Authority to (De-)Assign Authorities: [Jephte](https://docu.ilias.de/go/usr/70542)
* Tester: NONE
* Assignee for Security Reports: [Jephte](https://docu.ilias.de/go/usr/70542)
* Assignee for Security Issues: [Jephte](https://docu.ilias.de/go/usr/70542)

[//]: # (END WebServices)


[//]: # (BEGIN Xml)

#### [Xml](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Xml`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Xml)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Xml)


[//]: # (BEGIN jQuery)

#### [jQuery](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`jQuery`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/jQuery)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END jQuery)


[//]: # (BEGIN setup_)

#### [setup_](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`setup_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/setup_)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END setup_)


[//]: # (BEGIN soap)

#### [soap](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`soap`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/soap)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END soap)


### 4. [General Services](https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#4_General_Services)

[//]: # (BEGIN BackgroundTasks)

#### [Background Tasks](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`BackgroundTasks`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/BackgroundTasks), [`BackgroundTasks_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/BackgroundTasks_)


[//]: # (BEGIN BackgroundTasks)

##### BackgroundTasks
* Authority to Sign off on Conceptual Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)

[//]: # (END BackgroundTasks)


[//]: # (BEGIN BackgroundTasks_)

##### BackgroundTasks_
* Authority to Sign off on Conceptual Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)

[//]: # (END BackgroundTasks_)


[//]: # (END BackgroundTasks)

[//]: # (BEGIN Badge)

#### [Badges](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Badge`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Badge)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: Thomas.schroeder(38330)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Badge)


[//]: # (BEGIN Calendar)

#### [Calendar](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Calendar`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Calendar)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Tester: berggold(22199)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Calendar)


[//]: # (BEGIN Certificate)

#### [Certificate](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Certificate`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Certificate)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [christian.hueser](https://docu.ilias.de/go/usr/41129)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: christian.hueser(41129)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Certificate)


[//]: # (BEGIN Skill)

#### [Competence Management](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Skill`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Skill)

* Authority to Sign off on Conceptual Changes: [tfamula](https://docu.ilias.de/go/usr/58959), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [tfamula](https://docu.ilias.de/go/usr/58959), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [tfamula](https://docu.ilias.de/go/usr/58959), [akill](https://docu.ilias.de/go/usr/149)
* Tester: wolfganghuebsch(18455)
* Assignee for Security Reports: [tfamula](https://docu.ilias.de/go/usr/58959)
* Assignee for Security Issues: [tfamula](https://docu.ilias.de/go/usr/58959)

[//]: # (END Skill)


[//]: # (BEGIN Contact)

#### [Contacts](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Contact`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Contact)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [suittenpointner](https://docu.ilias.de/go/usr/3458)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: abaulig1(44386)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Contact)


[//]: # (BEGIN Dashboard)

#### [Dashboard](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Dashboard`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Dashboard)

* Authority to Sign off on Conceptual Changes: [iszmais](https://docu.ilias.de/go/usr/65630), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [iszmais](https://docu.ilias.de/go/usr/65630), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [iszmais](https://docu.ilias.de/go/usr/65630), [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [iszmais](https://docu.ilias.de/go/usr/65630)
* Assignee for Security Issues: [iszmais](https://docu.ilias.de/go/usr/65630)

[//]: # (END Dashboard)


[//]: # (BEGIN ECSInterface)

#### [ECS Interface](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`RemoteCategory`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteCategory), [`RemoteCourse`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteCourse), [`RemoteFile`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteFile), [`RemoteGlossary`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteGlossary), [`RemoteGroup`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteGroup), [`RemoteLearningModule`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteLearningModule), [`RemoteTest`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteTest), [`RemoteWiki`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteWiki)


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

#### [Export](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Export`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Export)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: Fabian(27631)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Export)


[//]: # (BEGIN GlobalScreen)

#### [Global Screen Service](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`GlobalScreen`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/GlobalScreen)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END GlobalScreen)


[//]: # (BEGIN COPage)

#### [ILIAS Page Editor](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`COPage`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/COPage)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: FH Aachen
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END COPage)


[//]: # (BEGIN InfoScreen)

#### [Info Page](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`InfoScreen`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/InfoScreen)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END InfoScreen)


[//]: # (BEGIN LearningHistory)

#### [Learning History](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`LearningHistory`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LearningHistory)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: oliver.samoila(26160)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END LearningHistory)


[//]: # (BEGIN MainMenu)

#### [Main Menu](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`MainMenu`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MainMenu)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END MainMenu)


[//]: # (BEGIN Maps)

#### [Maps](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Maps`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Maps)

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047), [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047), [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047), [dkloepfer](https://docu.ilias.de/go/usr/42712)
* Tester: miriamhoelscher(25370)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END Maps)


[//]: # (BEGIN Metadata)

#### [Metadata](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`ADT`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ADT), [`AdvancedMetaData`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AdvancedMetaData), [`MetaData`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MetaData)


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

#### [Notes and Comments](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Notes`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Notes)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [skaiser](https://docu.ilias.de/go/usr/17260)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: skaiser(17260)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Notes)


[//]: # (BEGIN Help)

#### [Online Help](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Help`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Help)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: atoedt(3139)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Help)


[//]: # (BEGIN OrgUnit)

#### [Organisational Units](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`OrgUnit`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/OrgUnit)

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [wischniak](https://docu.ilias.de/go/usr/21896)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047), [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: wischniak(21896)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END OrgUnit)


[//]: # (BEGIN PersonalandSharedResources)

#### [Personal and Shared Resources](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`PersonalWorkspace`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/PersonalWorkspace), [`WorkspaceFolder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WorkspaceFolder), [`WorkspaceRootFolder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WorkspaceRootFolder)


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

#### [Portfolio](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Portfolio`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Portfolio)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [KlausVorkauf](https://docu.ilias.de/go/usr/5890)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: KlausVorkauf(5890)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Portfolio)


[//]: # (BEGIN Conditions)

#### [Precondition Handling](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Conditions`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Conditions)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Tester: kunkel(115)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Conditions)


[//]: # (BEGIN Rating)

#### [Rating](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Rating`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Rating)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: Fabian(27631)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Rating)


[//]: # (BEGIN Search)

#### [Search](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Search`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Search)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: Future Learning
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Search)


[//]: # (BEGIN MyStaff)

#### [Staff](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`MyStaff`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MyStaff)

* Authority to Sign off on Conceptual Changes: [tfamula](https://docu.ilias.de/go/usr/58959), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Sign off on Code Changes: [tfamula](https://docu.ilias.de/go/usr/58959), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Curate Test Cases: [tfamula](https://docu.ilias.de/go/usr/58959), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to (De-)Assign Authorities: [tfamula](https://docu.ilias.de/go/usr/58959), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Tester: qualitus.morgunova(69410)
* Assignee for Security Reports: [tfamula](https://docu.ilias.de/go/usr/58959)
* Assignee for Security Issues: [tfamula](https://docu.ilias.de/go/usr/58959)

[//]: # (END MyStaff)


[//]: # (BEGIN Tracking)

#### [Statistics and Learning Progress](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Tracking`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Tracking)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [bromberger](https://docu.ilias.de/go/usr/198)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: suittenpointner(3458)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Tracking)


[//]: # (BEGIN Tagging)

#### [Tagging](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Tagging`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Tagging)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149), [mstuder](https://docu.ilias.de/go/usr/8473)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [mstuder](https://docu.ilias.de/go/usr/8473)
* Authority to Curate Test Cases: [skaiser](https://docu.ilias.de/go/usr/17260)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149), [mstuder](https://docu.ilias.de/go/usr/8473)
* Tester: skaiser(17260)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Tagging)


[//]: # (BEGIN Tasks)

#### [Task Service](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Tasks`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Tasks)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: NONE
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Tasks)


[//]: # (BEGIN Taxonomy)

#### [Taxonomy Service](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Taxonomy`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Taxonomy)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: Tested separately in each module that supports taxonomies
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: Tested separately in each module that supports taxonomies
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Taxonomy)


[//]: # (BEGIN User)

#### [User Service](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`User`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/User)

* Authority to Sign off on Conceptual Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to (De-)Assign Authorities: [fawinike](https://docu.ilias.de/go/usr/44474)
* Tester: NONE
* Assignee for Security Reports: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Issues: [fawinike](https://docu.ilias.de/go/usr/44474)

[//]: # (END User)


[//]: # (BEGIN WebDAV)

#### [WebDAV](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`WebDAV`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WebDAV)

* Authority to Sign off on Conceptual Changes: [fawinike](https://docu.ilias.de/go/usr/44474), [rheer](https://docu.ilias.de/go/usr/47872)
* Authority to Sign off on Code Changes: [fawinike](https://docu.ilias.de/go/usr/44474), [rheer](https://docu.ilias.de/go/usr/47872)
* Authority to Curate Test Cases: [fawinike](https://docu.ilias.de/go/usr/44474), [rheer](https://docu.ilias.de/go/usr/47872)
* Authority to (De-)Assign Authorities: [fawinike](https://docu.ilias.de/go/usr/44474), [rheer](https://docu.ilias.de/go/usr/47872)
* Tester: NONE
* Assignee for Security Reports: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Issues: [fawinike](https://docu.ilias.de/go/usr/44474)

[//]: # (END WebDAV)


[//]: # (BEGIN Awareness)

#### [Who is online?](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Awareness`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Awareness)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: amersch(15114)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Awareness)


### 5. [Container Objects](https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#5_Container_Objects)

[//]: # (BEGIN CategoryandRepository)

#### [Category and Repository](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`Category`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Category), [`CategoryReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CategoryReference), [`Container`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Container), [`ContainerReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ContainerReference), [`Folder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Folder), [`Repository`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Repository), [`RootFolder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RootFolder)


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

#### [Course Management](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`Course`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Course), [`CourseReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CourseReference)


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

#### [Group](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`Group`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Group), [`GroupReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/GroupReference)


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

#### [Item Groups](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`ItemGroup`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ItemGroup)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [berggold](https://docu.ilias.de/go/usr/22199)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: berggold(22199)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END ItemGroup)


[//]: # (BEGIN LearningSequence)

#### [Learning Sequence](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`LearningSequence`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LearningSequence)

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Curate Test Cases: [scarlino](https://docu.ilias.de/go/usr/56074)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047)
* Tester: mglaubitz(28309)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Issues: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END LearningSequence)


[//]: # (BEGIN Session)

#### [Session](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Session`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Session)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: iLUB Universität Bern
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: iLUB Universität Bern
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Session)


[//]: # (BEGIN StudyProgramme)

#### [Study Programme](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`StudyProgramme`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/StudyProgramme), [`StudyProgrammeReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/StudyProgrammeReference)


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
* Authority to Sign off on Conceptual Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [lscharmer](https://docu.ilias.de/go/usr/87863), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [lscharmer](https://docu.ilias.de/go/usr/87863), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: NONE
* Assignee for Security Reports: [lscharmer](https://docu.ilias.de/go/usr/87863)
* Assignee for Security Issues: [lscharmer](https://docu.ilias.de/go/usr/87863)

[//]: # (END StudyProgrammeReference)


[//]: # (END StudyProgramme)

### 6. [Communication and Syndication](https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#6_Communication_and_Syndication)

[//]: # (BEGIN AdministrativeNotification)

#### [Administrative Notifications](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`AdministrativeNotification`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AdministrativeNotification)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END AdministrativeNotification)


[//]: # (BEGIN Chat)

#### [Chat](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`Chatroom`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Chatroom), [`Notifications`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Notifications), [`OnScreenChat`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/OnScreenChat)


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

#### [Forum](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`Forum`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Forum), [`Html`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Html)


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

#### [Mail](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Mail`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Mail)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Authority to Curate Test Cases: [amersch](https://docu.ilias.de/go/usr/15114)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784), [nadia](https://docu.ilias.de/go/usr/14206)
* Tester: amersch(15114)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Mail)


[//]: # (BEGIN News)

#### [News](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`News`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/News)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [Thomas.schroeder](https://docu.ilias.de/go/usr/38330)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: Thomas.schroeder(38330)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END News)


[//]: # (BEGIN Feeds)

#### [News - RSS - Webfeeds](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Feeds`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Feeds)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: kunkel(115)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Feeds)


[//]: # (BEGIN Notification)

#### [Notifications](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Notification`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Notification)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Notification)


### 7. [Learning and Content Objects](https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#7_Learning_and_Content_Objects)

[//]: # (BEGIN Bibliographic)

#### [Bibliographic List Item](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Bibliographic`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Bibliographic)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [mstuder](https://docu.ilias.de/go/usr/8473)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: marko.glaubitz(28309)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END Bibliographic)


[//]: # (BEGIN Blog)

#### [Blog](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Blog`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Blog)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [KlausVorkauf](https://docu.ilias.de/go/usr/5890)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: PaBer(33766)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Blog)


[//]: # (BEGIN BookingManager)

#### [Booking Pool](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`BookingManager`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/BookingManager)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [e.coroian](https://docu.ilias.de/go/usr/37215)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: wolfganghuebsch(18455)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END BookingManager)


[//]: # (BEGIN ContentPage)

#### [Content Page](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`ContentPage`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ContentPage)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Tester: NONE
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Issues: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END ContentPage)


[//]: # (BEGIN DataCollection)

#### [Data Collection](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`DataCollection`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DataCollection)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END DataCollection)


[//]: # (BEGIN File)

#### [File](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`File`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/File)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [tloewen](https://docu.ilias.de/go/usr/41553)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: tloewen(41553)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Issues: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END File)


[//]: # (BEGIN Glossary)

#### [Glossary](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Glossary`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Glossary)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: atoedt(3139)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Glossary)


[//]: # (BEGIN LTIProvider)

#### [LTI](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`LTIProvider`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LTIProvider)

* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855), [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: atoedt(3139)
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)

[//]: # (END LTIProvider)


[//]: # (BEGIN HTMLLearningModule)

#### [Learning Module HTML](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`HTMLLearningModule`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/HTMLLearningModule)

* Authority to Sign off on Conceptual Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to (De-)Assign Authorities: [mbecker](https://docu.ilias.de/go/usr/27266)
* Tester: NONE
* Assignee for Security Reports: [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Security Issues: [mbecker](https://docu.ilias.de/go/usr/27266)

[//]: # (END HTMLLearningModule)


[//]: # (BEGIN LearningModule)

#### [Learning Module ILIAS](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`LearningModule`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LearningModule)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [Balliel](https://docu.ilias.de/go/usr/18365)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: Balliel(18365)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END LearningModule)


[//]: # (BEGIN LearningModuleSCORM)

#### [Learning Module SCORM](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`Scorm2004`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Scorm2004), [`ScormAicc`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ScormAicc)


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

#### [Media Pools and Media Objects](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`MediaObjects`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MediaObjects), [`MediaPool`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MediaPool)


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

#### [Mediacast](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`MediaCast`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MediaCast)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [berggold](https://docu.ilias.de/go/usr/22199)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: berggold(22199)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END MediaCast)


[//]: # (BEGIN WebResource)

#### [Weblink](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`WebResource`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WebResource)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [nadine.bauser](https://docu.ilias.de/go/usr/34662)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: nadine.bauser(34662)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END WebResource)


[//]: # (BEGIN Wiki)

#### [Wiki](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Wiki`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Wiki)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [abaulig1](https://docu.ilias.de/go/usr/44386)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: abaulig1(44386)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Wiki)


[//]: # (BEGIN CmiXapi)

#### [xAPI](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`CmiXapi`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CmiXapi)

* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Tester: NONE
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)

[//]: # (END CmiXapi)


### 8. [Evaluation, Feedback and Testing](https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#8_Evaluation_Feedback_and_Testing)

[//]: # (BEGIN EmployeeTalk)

#### [Employee Talk](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`EmployeeTalk`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/EmployeeTalk)

* Authority to Sign off on Conceptual Changes: [tschmitz](https://docu.ilias.de/go/usr/92591), [tfamula](https://docu.ilias.de/go/usr/58959)
* Authority to Sign off on Code Changes: [tschmitz](https://docu.ilias.de/go/usr/92591), [tfamula](https://docu.ilias.de/go/usr/58959)
* Authority to Curate Test Cases: [tschmitz](https://docu.ilias.de/go/usr/92591), [tfamula](https://docu.ilias.de/go/usr/58959)
* Authority to (De-)Assign Authorities: [tschmitz](https://docu.ilias.de/go/usr/92591), [tfamula](https://docu.ilias.de/go/usr/58959)
* Tester: qualitus.morgunova(69410)
* Assignee for Security Reports: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Assignee for Security Issues: [tschmitz](https://docu.ilias.de/go/usr/92591)

[//]: # (END EmployeeTalk)


[//]: # (BEGIN Exercise)

#### [Exercise](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Exercise`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Exercise)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [KlausVorkauf](https://docu.ilias.de/go/usr/5890)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Tester: miriamwegener(23051)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Issues: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Exercise)


[//]: # (BEGIN IndividualAssessment)

#### [Individual Assessment](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`IndividualAssessment`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/IndividualAssessment)

* Authority to Sign off on Conceptual Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to (De-)Assign Authorities: [mbecker](https://docu.ilias.de/go/usr/27266)
* Tester: kunkel(115)
* Assignee for Security Reports: [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Security Issues: [mbecker](https://docu.ilias.de/go/usr/27266)

[//]: # (END IndividualAssessment)


[//]: # (BEGIN Poll)

#### [Poll](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`Poll`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Poll)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Tester: Future Learning
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Issues: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Poll)


[//]: # (BEGIN Survey)

#### [Survey](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`Survey`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Survey), [`SurveyQuestionPool`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/SurveyQuestionPool)


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

#### [Test & Assessment](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`Test`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Test), [`TestQuestionPool`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/TestQuestionPool)


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

### 9. [Administration](https://docu.ilias.de/ilias.php?baseClass=ilwikihandlergui&cmdNode=14x:rn:150&cmdClass=ilWikiPageGUI&cmd=preview&ref_id=1357&page=Overview#9_Administration)

[//]: # (BEGIN Administration)

#### [Administration](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`Administration`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Administration), [`SystemFolder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/SystemFolder)


[//]: # (BEGIN Administration)

##### Administration
* Authority to Sign off on Conceptual Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Sign off on Code Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [fneumann](https://docu.ilias.de/go/usr/1560)
* Tester: kunkel(115)
* Assignee for Security Reports: [fneumann](https://docu.ilias.de/go/usr/1560)
* Assignee for Security Issues: [fneumann](https://docu.ilias.de/go/usr/1560)

[//]: # (END Administration)


[//]: # (BEGIN SystemFolder)

##### SystemFolder
* Authority to Sign off on Conceptual Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Tester: NONE
* Assignee for Security Reports: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Security Issues: [tfuhrer](https://docu.ilias.de/go/usr/81947)

[//]: # (END SystemFolder)


[//]: # (END Administration)

[//]: # (BEGIN LoginAuthRegistration)

#### [Login, Auth & Registration](https://docu.ilias.de/go/wiki/wpage_1_1357)

*Component Ordner:* [`AuthApache`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AuthApache), [`Authentication`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Authentication), [`Init`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Init), [`LDAP`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LDAP), [`OpenIdConnect`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/OpenIdConnect), [`Registration`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Registration)


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

#### [Setup](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Ordner:* [`Setup`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Setup)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Tester: NONE
* Assignee for Security Reports: NONE
* Assignee for Security Issues: NONE

[//]: # (END Setup)


[//]: # (BEGIN SystemCheck)

#### [System Check](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Ordner:* [`SystemCheck`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/SystemCheck)

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
* ILIAS/Benchmark
* ILIAS/Cache
* ILIAS/Cloud
* ILIAS/FileDelivery
* ILIAS/FileServices
* ILIAS/History
* ILIAS/Multilingualism
* ILIAS/PermanentLink
* ILIAS/Setup
* ILIAS/StaticURL
* ILIAS/StudyProgrammeReference
* ILIAS/SystemFolder
* ILIAS/UI_
* ILIAS/setup_
* ILIAS/soap