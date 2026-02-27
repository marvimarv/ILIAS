ILIAS Maintenance
=================
The development of ILIAS is coordinated by the Product Manager and the
Technical Board. Many decisions are taken at the biweekly Jour Fixe, which is
open for participation to everyone. The source code is maintained by a growing
group of people, ranging from devoted maintainers to regular or even one-time
contributors.

# Special Roles

* **Product Management**: [Matthias Kunkel](https://docu.ilias.de/go/usr/115)
* **Technical Board**: [Rob Falkenstein](https://docu.ilias.de/go/usr/63946), [Marvin Hackfort](https://docu.ilias.de/go/usr/50523), [Michael Jansen](https://docu.ilias.de/go/usr/8784), [Franziska Wandelmaier](https://docu.ilias.de/go/usr/33833), [one vacant position]
* **Testcase Management**: [Fabian Kruse](https://docu.ilias.de/go/usr/27631)
* **Release Management**: [Fabian Wolf](https://docu.ilias.de/go/usr/29018)
* **Technical Documentation**: [Ann-Christin Gruber](https://docu.ilias.de/go/usr/94025)
* **Online Help**: [Alexandra Tödt](https://docu.ilias.de/go/usr/3139)

[//]: # (BEGIN Authorities)
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
They are the only ones allowed to modify the `maintenance.json` of a component.

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

[//]: # (END Authorities)

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
of the last `Authority to Sign off on Code Changes` would like to pass the
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

Components are listed alphabetically by component folder name.

[//]: # (BEGIN AccessControl)

#### [RBAC and Permissions](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`AccessControl`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AccessControl)

* Authority to Sign off on Conceptual Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Issues: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Reports: [skergomard](https://docu.ilias.de/go/usr/44474)

[//]: # (END AccessControl)


[//]: # (BEGIN Accessibility)

#### [Accessibility](https://docu.ilias.de/go/wiki/wpage_30_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Accessibility`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Accessibility)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Accessibility)


[//]: # (BEGIN Accordion)

#### [Accordion](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Accordion`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Accordion)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Accordion)


[//]: # (BEGIN ActiveRecord)

#### [ActiveRecord](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`ActiveRecord`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ActiveRecord)

* Authority to Sign off on Conceptual Changes: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Authority to Sign off on Code Changes: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Authority to Curate Test Cases: MISSING
* Authority to (De-)Assign Authorities: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Assignee for Issues: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Assignee for Security Reports: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)

[//]: # (END ActiveRecord)


[//]: # (BEGIN Administration)

#### [Administration](https://docu.ilias.de/go/wiki/wpage_246_1357)

*Component Folders:* [`Administration`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Administration), [`SystemFolder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/SystemFolder)


[//]: # (BEGIN Administration)

##### Administration
* Authority to Sign off on Conceptual Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Sign off on Code Changes: [fneumann](https://docu.ilias.de/go/usr/1560), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [fneumann](https://docu.ilias.de/go/usr/1560), [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [fneumann (Databay AG)](https://docu.ilias.de/go/usr/1560), [lscharmer (Databay AG)](https://docu.ilias.de/go/usr/87863)
* Assignee for Issues: [fneumann](https://docu.ilias.de/go/usr/1560)
* Assignee for Security Reports: [fneumann](https://docu.ilias.de/go/usr/1560)

[//]: # (END Administration)


[//]: # (BEGIN SystemFolder)

##### SystemFolder
* Authority to Sign off on Conceptual Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Sign off on Code Changes: [fneumann](https://docu.ilias.de/go/usr/1560), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [fneumann](https://docu.ilias.de/go/usr/1560), [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [fneumann (Databay AG)](https://docu.ilias.de/go/usr/1560), [lscharmer (Databay AG)](https://docu.ilias.de/go/usr/87863)
* Assignee for Issues: [fneumann](https://docu.ilias.de/go/usr/1560)
* Assignee for Security Reports: [fneumann](https://docu.ilias.de/go/usr/1560)

[//]: # (END SystemFolder)


[//]: # (END Administration)

[//]: # (BEGIN AdministrativeNotification)

#### [Administrative Notifications](https://docu.ilias.de/go/wiki/wpage_7290_1357)
*Component Folders:* [`AdministrativeNotification`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AdministrativeNotification)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END AdministrativeNotification)


[//]: # (BEGIN Metadata)

#### [Metadata](https://docu.ilias.de/go/wiki/wpage_973_1357)

*Component Folders:* [`ADT`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ADT), [`AdvancedMetaData`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AdvancedMetaData), [`MetaData`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MetaData)


[//]: # (BEGIN ADT)

##### ADT
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Curate Test Cases: [Alexandra Tödt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END ADT)


[//]: # (BEGIN AdvancedMetaData)

##### AdvancedMetaData
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Curate Test Cases: [Alexandra Tödt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END AdvancedMetaData)


[//]: # (BEGIN MetaData)

##### MetaData
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Curate Test Cases: [Alexandra Tödt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END MetaData)


[//]: # (END Metadata)

[//]: # (BEGIN AdvancedEditing)

#### [AdvancedEditing](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`AdvancedEditing`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AdvancedEditing)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END AdvancedEditing)


[//]: # (BEGIN App)

#### [App](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`App`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/App)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END App)


[//]: # (BEGIN AssessmentQuestion)

#### [AssessmentQuestion](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`AssessmentQuestion`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AssessmentQuestion)

* Authority to Sign off on Conceptual Changes: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Issues: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Security Reports: [dstrassner](https://docu.ilias.de/go/usr/48931), [mbecker](https://docu.ilias.de/go/usr/27266)

[//]: # (END AssessmentQuestion)


[//]: # (BEGIN LoginAuthRegistration)

#### [Login, Auth & Registration](https://docu.ilias.de/go/wiki/wpage_19_1357)

*Component Folders:* [`AuthApache`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AuthApache), [`Authentication`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Authentication), [`CAS`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CAS), [`Init`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Init), [`LDAP`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LDAP), [`OpenIdConnect`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/OpenIdConnect), [`Registration`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Registration)


[//]: # (BEGIN AuthApache)

##### AuthApache
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END AuthApache)


[//]: # (BEGIN Authentication)

##### Authentication
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Authentication)


[//]: # (BEGIN CAS)

##### CAS
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END CAS)


[//]: # (BEGIN Init)

##### Init
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Init)


[//]: # (BEGIN LDAP)

##### LDAP
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END LDAP)


[//]: # (BEGIN OpenIdConnect)

##### OpenIdConnect
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END OpenIdConnect)


[//]: # (BEGIN Registration)

##### Registration
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Registration)


[//]: # (END LoginAuthRegistration)

[//]: # (BEGIN AuthShibboleth)

#### [Shibboleth Authentication](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`AuthShibboleth`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/AuthShibboleth)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END AuthShibboleth)


[//]: # (BEGIN Awareness)

#### [Who is online?](https://docu.ilias.de/go/wiki/wpage_293_1357)
*Component Folders:* [`Awareness`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Awareness)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Awareness)


[//]: # (BEGIN BackgroundTasks)

#### [Background Tasks](https://docu.ilias.de/go/wiki/wpage_4383_1357)

*Component Folders:* [`BackgroundTasks`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/BackgroundTasks), [`BackgroundTasks_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/BackgroundTasks_)


[//]: # (BEGIN BackgroundTasks)

##### BackgroundTasks
* Authority to Sign off on Conceptual Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: MISSING
* Authority to (De-)Assign Authorities: [tjoussen (Databay AG)](https://docu.ilias.de/go/usr/103745)
* Assignee for Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END BackgroundTasks)


[//]: # (BEGIN BackgroundTasks_)

##### BackgroundTasks_
* Authority to Sign off on Conceptual Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: MISSING
* Authority to (De-)Assign Authorities: [tjoussen (Databay AG)](https://docu.ilias.de/go/usr/103745)
* Assignee for Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)

[//]: # (END BackgroundTasks_)


[//]: # (END BackgroundTasks)

[//]: # (BEGIN BackgroundTasks)

#### [BackgroundTasks](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`BackgroundTasks`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/BackgroundTasks)

* Authority to Sign off on Conceptual Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: MISSING
* Authority to (De-)Assign Authorities: [tjoussen (Databay AG)](https://docu.ilias.de/go/usr/103745)
* Assignee for Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END BackgroundTasks)


[//]: # (BEGIN Badge)

#### [Badges](https://docu.ilias.de/go/wiki/wpage_4203_1357)
*Component Folders:* [`Badge`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Badge)

* Authority to Sign off on Conceptual Changes: [fhelfer](https://docu.ilias.de/go/usr/93367)
* Authority to Sign off on Code Changes: [fhelfer](https://docu.ilias.de/go/usr/93367), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [fhelfer](https://docu.ilias.de/go/usr/93367)
* Assignee for Security Reports: [fhelfer](https://docu.ilias.de/go/usr/93367)

[//]: # (END Badge)


[//]: # (BEGIN Benchmark)

#### [Benchmark](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Benchmark)


[//]: # (BEGIN Bibliographic)

#### [Bibliographic List Item](https://docu.ilias.de/go/wiki/wpage_2553_1357)
*Component Folders:* [`Bibliographic`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Bibliographic)

* Authority to Sign off on Conceptual Changes: [lschmidt-tf](https://docu.ilias.de/go/usr/120143)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [maalers](https://docu.ilias.de/go/usr/119188)
* Authority to Curate Test Cases: [maalers](https://docu.ilias.de/go/usr/119188)
* Authority to (De-)Assign Authorities: [maalers](https://docu.ilias.de/go/usr/119188)
* Assignee for Issues: [maalers](https://docu.ilias.de/go/usr/119188)
* Assignee for Security Reports: [maalers](https://docu.ilias.de/go/usr/119188)

[//]: # (END Bibliographic)


[//]: # (BEGIN Block)

#### [Block](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Block`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Block)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Block)


[//]: # (BEGIN Blog)

#### [Blog](https://docu.ilias.de/go/wiki/wpage_1448_1357)
*Component Folders:* [`Blog`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Blog)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Blog)


[//]: # (BEGIN BookingManager)

#### [Booking Pool](https://docu.ilias.de/go/wiki/wpage_133_1357)
*Component Folders:* [`BookingManager`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/BookingManager)

* Authority to Sign off on Conceptual Changes: [simon.lowe](https://docu.ilias.de/go/usr/79091), [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [simon.lowe](https://docu.ilias.de/go/usr/79091), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to (De-)Assign Authorities: [simon.lowe (Databay AG)](https://docu.ilias.de/go/usr/79091), [oliver.samoila (Databay AG)](https://docu.ilias.de/go/usr/26160)
* Assignee for Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)

[//]: # (END BookingManager)


[//]: # (BEGIN Cache)

#### [Cache](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Cache`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Cache)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END Cache)


[//]: # (BEGIN Cache_)

#### [Cache_](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Cache_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Cache_)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Cache_)


[//]: # (BEGIN Calendar)

#### [Calendar](https://docu.ilias.de/go/wiki/wpage_23_1357)
*Component Folders:* [`Calendar`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Calendar)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Calendar)


[//]: # (BEGIN CategoryandRepository)

#### [Category and Repository](https://docu.ilias.de/go/wiki/wpage_106_1357)

*Component Folders:* [`Category`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Category), [`CategoryReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CategoryReference), [`Container`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Container), [`ContainerReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ContainerReference), [`Folder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Folder), [`Repository`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Repository), [`RootFolder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RootFolder)


[//]: # (BEGIN Category)

##### Category
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Category)


[//]: # (BEGIN CategoryReference)

##### CategoryReference
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END CategoryReference)


[//]: # (BEGIN Container)

##### Container
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Container)


[//]: # (BEGIN ContainerReference)

##### ContainerReference
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END ContainerReference)


[//]: # (BEGIN Folder)

##### Folder
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Folder)


[//]: # (BEGIN Repository)

##### Repository
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Repository)


[//]: # (BEGIN RootFolder)

##### RootFolder
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END RootFolder)


[//]: # (END CategoryandRepository)

[//]: # (BEGIN CategoryAndRepository)

#### [Category, Category Reference and Repository](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END CategoryAndRepository)


[//]: # (BEGIN Certificate)

#### [Certificate](https://docu.ilias.de/go/wiki/wpage_66_1357)
*Component Folders:* [`Certificate`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Certificate)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784), [ChrisPotter](https://docu.ilias.de/go/usr/90855)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Certificate)


[//]: # (BEGIN Chart)

#### [Chart](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Chart`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Chart)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Chart)


[//]: # (BEGIN Chat)

#### [Chatroom](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Chat)


[//]: # (BEGIN Chat)

#### [Chat](https://docu.ilias.de/go/wiki/wpage_37_1357)

*Component Folders:* [`Chatroom`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Chatroom), [`OnScreenChat`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/OnScreenChat)


[//]: # (BEGIN Chatroom)

##### Chatroom
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Chatroom)


[//]: # (BEGIN OnScreenChat)

##### OnScreenChat
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END OnScreenChat)


[//]: # (END Chat)

[//]: # (BEGIN Cloud)

#### [Cloud](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Cloud`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Cloud)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Cloud)


[//]: # (BEGIN CmiXapi)

#### [xAPI](https://docu.ilias.de/go/wiki/wpage_2921_1357)
*Component Folders:* [`CmiXapi`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CmiXapi)

* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)

[//]: # (END CmiXapi)


[//]: # (BEGIN Comments)

#### [Comments](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [skaiser](https://docu.ilias.de/go/usr/17260)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Comments)


[//]: # (BEGIN Component)

#### [Components Framework](https://docu.ilias.de/go/wiki/wpage_7285_1357)
*Component Folders:* [`Component`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Component)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Component)


[//]: # (BEGIN Component)

#### [Component](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Component`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Component)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087), [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Component)


[//]: # (BEGIN Conditions)

#### [Precondition Handling](https://docu.ilias.de/go/wiki/wpage_126_1357)
*Component Folders:* [`Conditions`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Conditions)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Conditions)


[//]: # (BEGIN Contact)

#### [Contacts](https://docu.ilias.de/go/wiki/wpage_3740_1357)
*Component Folders:* [`Contact`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Contact)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Contact)


[//]: # (BEGIN ContentPage)

#### [Content Page](https://docu.ilias.de/go/wiki/wpage_5369_1357)
*Component Folders:* [`ContentPage`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ContentPage)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END ContentPage)


[//]: # (BEGIN ContentPage)

#### [ContentPage](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`ContentPage`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ContentPage)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END ContentPage)


[//]: # (BEGIN Context)

#### [Context](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Context`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Context)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Context)


[//]: # (BEGIN COPage)

#### [ILIAS Page Editor](https://docu.ilias.de/go/wiki/wpage_2141_1357)
*Component Folders:* [`COPage`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/COPage)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [ezenzen](https://docu.ilias.de/go/usr/42910)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END COPage)


[//]: # (BEGIN CopyWizard)

#### [CopyWizard](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`CopyWizard`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CopyWizard)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END CopyWizard)


[//]: # (BEGIN CourseManagement)

#### [Course Management](https://docu.ilias.de/go/wiki/wpage_13_1357)

*Component Folders:* [`Course`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Course), [`CourseReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CourseReference)


[//]: # (BEGIN Course)

##### Course
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Course)


[//]: # (BEGIN CourseReference)

##### CourseReference
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END CourseReference)


[//]: # (END CourseManagement)

[//]: # (BEGIN CourseManagement)

#### [Course and Course Reference](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END CourseManagement)


[//]: # (BEGIN Cron)

#### [Cron Service](https://docu.ilias.de/go/wiki/wpage_2357_1357)
*Component Folders:* [`Cron`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Cron)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Cron)


[//]: # (BEGIN CSSAndTemplates)

#### [CSS / Templates](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [BettyFromHH](https://docu.ilias.de/go/usr/96573)
* Authority to Sign off on Code Changes: [BettyFromHH](https://docu.ilias.de/go/usr/96573), [rotegras](https://docu.ilias.de/go/usr/88399), [padvincenzo](https://docu.ilias.de/go/usr/87189)
* Authority to Curate Test Cases: [BettyFromHH](https://docu.ilias.de/go/usr/96573)
* Authority to (De-)Assign Authorities: [BettyFromHH](https://docu.ilias.de/go/usr/96573)
* Assignee for Issues: [BettyFromHH](https://docu.ilias.de/go/usr/96573)
* Assignee for Security Reports: [BettyFromHH](https://docu.ilias.de/go/usr/96573)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END CSSAndTemplates)


[//]: # (BEGIN CSV)

#### [CSV](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`CSV`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/CSV)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END CSV)


[//]: # (BEGIN Dashboard)

#### [Dashboard](https://docu.ilias.de/go/wiki/wpage_6092_1357)
*Component Folders:* [`Dashboard`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Dashboard)

* Authority to Sign off on Conceptual Changes: [iszmais](https://docu.ilias.de/go/usr/65630), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Sign off on Code Changes: [iszmais](https://docu.ilias.de/go/usr/65630), [lscharmer](https://docu.ilias.de/go/usr/87863), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [iszmais (Databay AG)](https://docu.ilias.de/go/usr/65630), [lscharmer (Databay AG)](https://docu.ilias.de/go/usr/87863)
* Assignee for Issues: [iszmais](https://docu.ilias.de/go/usr/65630)
* Assignee for Security Reports: [iszmais](https://docu.ilias.de/go/usr/65630)

[//]: # (END Dashboard)


[//]: # (BEGIN Data)

#### [Data](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Data`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Data)

* Authority to Sign off on Conceptual Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Data)


[//]: # (BEGIN Database)

#### [Database](https://docu.ilias.de/go/wiki/wpage_12_1357)
*Component Folders:* [`Database`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Database)

* Authority to Sign off on Conceptual Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [lscharmer](https://docu.ilias.de/go/usr/87863), [mjansen](https://docu.ilias.de/go/usr/8784), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: MISSING
* Authority to (De-)Assign Authorities: [lscharmer](https://docu.ilias.de/go/usr/87863)
* Assignee for Issues: [lscharmer](https://docu.ilias.de/go/usr/87863)
* Assignee for Security Reports: [lscharmer](https://docu.ilias.de/go/usr/87863)

[//]: # (END Database)


[//]: # (BEGIN DataCollection)

#### [Data Collection](https://docu.ilias.de/go/wiki/wpage_2340_1357)
*Component Folders:* [`DataCollection`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DataCollection)

* Authority to Sign off on Conceptual Changes: [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to Sign off on Code Changes: [iszmais](https://docu.ilias.de/go/usr/65630)
* Authority to Curate Test Cases: [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to (De-)Assign Authorities: [oliver.samoila (Databay AG)](https://docu.ilias.de/go/usr/26160)
* Assignee for Issues: [iszmais](https://docu.ilias.de/go/usr/65630)
* Assignee for Security Reports: [iszmais](https://docu.ilias.de/go/usr/65630)

[//]: # (END DataCollection)


[//]: # (BEGIN PrivacyTermsofServiceandDataProtectioninclTermsofService)

#### [Privacy, Terms of Service and Data Protection (incl. Terms of Service)](https://docu.ilias.de/go/wiki/wpage_4995_1357)

*Component Folders:* [`DataProtection`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DataProtection), [`PrivacySecurity`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/PrivacySecurity), [`TermsOfService`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/TermsOfService)


[//]: # (BEGIN DataProtection)

##### DataProtection
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [AUTHOR MISSING](https://docu.ilias.de/go/pg/64423_4793)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END DataProtection)


[//]: # (BEGIN PrivacySecurity)

##### PrivacySecurity
* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END PrivacySecurity)


[//]: # (BEGIN TermsOfService)

##### TermsOfService
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [AUTHOR MISSING](https://docu.ilias.de/go/pg/64423_4793)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END TermsOfService)


[//]: # (END PrivacyTermsofServiceandDataProtectioninclTermsofService)

[//]: # (BEGIN DataProtection)

#### [Data Protection](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`DataProtection`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DataProtection)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [AUTHOR MISSING](https://docu.ilias.de/go/pg/64423_4793)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END DataProtection)


[//]: # (BEGIN DataSet)

#### [DataSet](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`DataSet`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DataSet)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END DataSet)


[//]: # (BEGIN DI)

#### [DI](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`DI`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DI)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END DI)


[//]: # (BEGIN DidacticTemplate)

#### [Didactic Templates](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`DidacticTemplate`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/DidacticTemplate)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END DidacticTemplate)


[//]: # (BEGIN ECSInterface)

#### [ECS Interface](https://docu.ilias.de/go/wiki/wpage_1132_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Authority to Sign off on Code Changes: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Authority to Curate Test Cases: [jheim](https://docu.ilias.de/go/usr/40167), [SIG CampusConnect und ECS(A)](https://docu.ilias.de/go/grp/7893)
* Authority to (De-)Assign Authorities: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Assignee for Issues: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Assignee for Security Reports: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END ECSInterface)


[//]: # (BEGIN EmployeeTalk)

#### [Employee Talk](https://docu.ilias.de/go/wiki/wpage_7784_1357)
*Component Folders:* [`EmployeeTalk`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/EmployeeTalk)

* Authority to Sign off on Conceptual Changes: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Sign off on Code Changes: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Curate Test Cases: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to (De-)Assign Authorities: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Assignee for Issues: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Assignee for Security Reports: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END EmployeeTalk)


[//]: # (BEGIN EmployeeTalk)

#### [EmployeeTalk](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`EmployeeTalk`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/EmployeeTalk)

* Authority to Sign off on Conceptual Changes: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Sign off on Code Changes: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Curate Test Cases: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to (De-)Assign Authorities: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Assignee for Issues: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Assignee for Security Reports: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END EmployeeTalk)


[//]: # (BEGIN Environment)

#### [Environment](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Environment`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Environment)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Environment)


[//]: # (BEGIN EventHandling)

#### [EventHandling](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`EventHandling`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/EventHandling)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END EventHandling)


[//]: # (BEGIN Excel)

#### [Excel](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Excel`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Excel)

* Authority to Sign off on Conceptual Changes: [dstrassner](https://docu.ilias.de/goto_docu_usr_48931.html)
* Authority to Sign off on Code Changes: [skergomard](https://docu.ilias.de/goto_docu_usr_44474.html)
* Authority to Curate Test Cases: [dstrassner](https://docu.ilias.de/goto_docu_usr_48931.html)
* Authority to (De-)Assign Authorities: [dstrassner](https://docu.ilias.de/goto_docu_usr_48931.html)
* Assignee for Issues: [dstrassner](https://docu.ilias.de/goto_docu_usr_48931.html)
* Assignee for Security Reports: [dstrassner](https://docu.ilias.de/goto_docu_usr_48931.html)

[//]: # (END Excel)


[//]: # (BEGIN Exceptions)

#### [Exceptions](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Exceptions`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Exceptions)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Exceptions)


[//]: # (BEGIN Exercise)

#### [Exercise](https://docu.ilias.de/go/wiki/wpage_28_1357)
*Component Folders:* [`Exercise`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Exercise)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Exercise)


[//]: # (BEGIN Export)

#### [Export](https://docu.ilias.de/go/wiki/wpage_91_1357)
*Component Folders:* [`Export`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Export)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [Fabian](https://docu.ilias.de/go/usr/27631)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Export)


[//]: # (BEGIN Favourites)

#### [Favourites](https://docu.ilias.de/go/wiki/wpage_6091_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [iszmais](https://docu.ilias.de/go/usr/65630)
* Authority to Sign off on Code Changes: [iszmais](https://docu.ilias.de/go/usr/65630)
* Authority to Curate Test Cases: [iszmais](https://docu.ilias.de/go/usr/65630)
* Authority to (De-)Assign Authorities: [iszmais](https://docu.ilias.de/go/usr/65630)
* Assignee for Issues: [iszmais](https://docu.ilias.de/go/usr/65630)
* Assignee for Security Reports: [iszmais](https://docu.ilias.de/go/usr/65630)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Favourites)


[//]: # (BEGIN NewsRSSWebfeeds)

#### [News - RSS - Webfeeds](https://docu.ilias.de/go/wiki/wpage_38_1357)

*Component Folders:* [`Feeds`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Feeds), [`News`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/News)


[//]: # (BEGIN Feeds)

##### Feeds
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Feeds)


[//]: # (BEGIN News)

##### News
* Authority to Sign off on Conceptual Changes: [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [tjoussen](https://docu.ilias.de/go/usr/103745), [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to (De-)Assign Authorities: [oliver.samoila (Databay AG)](https://docu.ilias.de/go/usr/26160)
* Assignee for Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END News)


[//]: # (END NewsRSSWebfeeds)

[//]: # (BEGIN File)

#### [File](https://docu.ilias.de/go/wiki/wpage_4_1357)
*Component Folders:* [`File`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/File)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END File)


[//]: # (BEGIN FileDelivery)

#### [FileDelivery](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`FileDelivery`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/FileDelivery)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END FileDelivery)


[//]: # (BEGIN FileServices)

#### [FileServices](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`FileServices`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/FileServices)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END FileServices)


[//]: # (BEGIN Filesystem)

#### [Filesystem](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Filesystem`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Filesystem)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END Filesystem)


[//]: # (BEGIN FileUpload)

#### [FileUpload](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`FileUpload`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/FileUpload)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END FileUpload)


[//]: # (BEGIN Form)

#### [Form](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Form`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Form)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Form)


[//]: # (BEGIN Forum)

#### [Forum](https://docu.ilias.de/go/wiki/wpage_35_1357)

*Component Folders:* [`Forum`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Forum), [`Html`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Html)


[//]: # (BEGIN Forum)

##### Forum
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Forum)


[//]: # (BEGIN Html)

##### Html
* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: FH Aachen
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Html)


[//]: # (END Forum)

[//]: # (BEGIN GlobalCache)

#### [Global Cache](https://docu.ilias.de/go/wiki/wpage_6435_1357)

*Component Folders:* [`GlobalCache`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/GlobalCache), [`GlobalCache_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/GlobalCache_)


[//]: # (BEGIN GlobalCache)

##### GlobalCache
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END GlobalCache)


[//]: # (BEGIN GlobalCache_)

##### GlobalCache_
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END GlobalCache_)


[//]: # (END GlobalCache)

[//]: # (BEGIN GlobalCache)

#### [GlobalCache](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`GlobalCache`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/GlobalCache)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END GlobalCache)


[//]: # (BEGIN GlobalScreenService)

#### [Global Screen Service](https://docu.ilias.de/go/wiki/wpage_6079_1357)

*Component Folders:* [`GlobalScreen`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/GlobalScreen), [`GlobalScreen_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/GlobalScreen_)


[//]: # (BEGIN GlobalScreen)

##### GlobalScreen
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END GlobalScreen)


[//]: # (BEGIN GlobalScreen_)

##### GlobalScreen_
* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END GlobalScreen_)


[//]: # (END GlobalScreenService)

[//]: # (BEGIN GlobalScreen)

#### [GlobalScreen](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`GlobalScreen`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/GlobalScreen)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END GlobalScreen)


[//]: # (BEGIN Glossary)

#### [Glossary](https://docu.ilias.de/go/wiki/wpage_121_1357)
*Component Folders:* [`Glossary`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Glossary)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [ezenzen](https://docu.ilias.de/go/usr/42910)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Glossary)


[//]: # (BEGIN Group)

#### [Group](https://docu.ilias.de/go/wiki/wpage_39_1357)

*Component Folders:* [`Group`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Group), [`GroupReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/GroupReference)


[//]: # (BEGIN Group)

##### Group
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Group)


[//]: # (BEGIN GroupReference)

##### GroupReference
* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END GroupReference)


[//]: # (END Group)

[//]: # (BEGIN Group)

#### [Group and Group Reference](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Group`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Group)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Group)


[//]: # (BEGIN Help)

#### [Online Help](https://docu.ilias.de/go/wiki/wpage_415_1357)
*Component Folders:* [`Help`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Help)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Help)


[//]: # (BEGIN History)

#### [History](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`History`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/History)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [ezenzen](https://docu.ilias.de/go/usr/42910)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END History)


[//]: # (BEGIN HTMLLearningModule)

#### [Learning Module HTML](https://docu.ilias.de/go/wiki/wpage_135_1357)
*Component Folders:* [`HTMLLearningModule`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/HTMLLearningModule)

* Authority to Sign off on Conceptual Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to (De-)Assign Authorities: [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Issues: [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Security Reports: [mbecker](https://docu.ilias.de/go/usr/27266)

[//]: # (END HTMLLearningModule)


[//]: # (BEGIN HTTP)

#### [HTTP](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`HTTP`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/HTTP)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END HTTP)


[//]: # (BEGIN Http_)

#### [Http_](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Http_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Http_)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Http_)


[//]: # (BEGIN ILIASObject)

#### [ILIASObject](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`ILIASObject`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ILIASObject)

* Authority to Sign off on Conceptual Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [fawinike](https://docu.ilias.de/go/usr/44474)
* Authority to (De-)Assign Authorities: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Issues: [fawinike](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Reports: [fawinike](https://docu.ilias.de/go/usr/44474)

[//]: # (END ILIASObject)


[//]: # (BEGIN ILIASPageEditor)

#### [COPage (aka ILIAS Page Editor)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [ezenzen](https://docu.ilias.de/go/usr/42910)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END ILIASPageEditor)


[//]: # (BEGIN Imprint)

#### [Imprint](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Imprint`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Imprint)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Imprint)


[//]: # (BEGIN IndividualAssessment)

#### [Individual Assessment](https://docu.ilias.de/go/wiki/wpage_4226_1357)
*Component Folders:* [`IndividualAssessment`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/IndividualAssessment)

* Authority to Sign off on Conceptual Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to (De-)Assign Authorities: [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Issues: [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Security Reports: [mbecker](https://docu.ilias.de/go/usr/27266)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END IndividualAssessment)


[//]: # (BEGIN IndividualAssessment)

#### [IndividualAssessment](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`IndividualAssessment`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/IndividualAssessment)

* Authority to Sign off on Conceptual Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Sign off on Code Changes: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to Curate Test Cases: [mbecker](https://docu.ilias.de/go/usr/27266)
* Authority to (De-)Assign Authorities: [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Issues: [mbecker](https://docu.ilias.de/go/usr/27266)
* Assignee for Security Reports: [mbecker](https://docu.ilias.de/go/usr/27266)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END IndividualAssessment)


[//]: # (BEGIN InfoPage)

#### [InfoScreen (aka Info Page)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END InfoPage)


[//]: # (BEGIN InfoScreen)

#### [Info Page](https://docu.ilias.de/go/wiki/wpage_2095_1357)
*Component Folders:* [`InfoScreen`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/InfoScreen)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END InfoScreen)


[//]: # (BEGIN InitialisationService)

#### [Init (aka Initialisation Service)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END InitialisationService)


[//]: # (BEGIN ItemGroup)

#### [Item Groups](https://docu.ilias.de/go/wiki/wpage_7968_1357)
*Component Folders:* [`ItemGroup`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ItemGroup)

* Authority to Sign off on Conceptual Changes: [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [oliver.samoila](https://docu.ilias.de/go/usr/26160), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to (De-)Assign Authorities: [oliver.samoila (Databay AG)](https://docu.ilias.de/go/usr/26160)
* Assignee for Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END ItemGroup)


[//]: # (BEGIN ItemGroup)

#### [ItemGroup](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`ItemGroup`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ItemGroup)

* Authority to Sign off on Conceptual Changes: [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [oliver.samoila](https://docu.ilias.de/go/usr/26160), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to (De-)Assign Authorities: [oliver.samoila (Databay AG)](https://docu.ilias.de/go/usr/26160)
* Assignee for Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END ItemGroup)


[//]: # (BEGIN JavaScript)

#### [JavaScript](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`JavaScript`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/JavaScript)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END JavaScript)


[//]: # (BEGIN jQuery)

#### [jQuery](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`jQuery`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/jQuery)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END jQuery)


[//]: # (BEGIN KioskMode)

#### [KioskMode](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`KioskMode`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/KioskMode)

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Issues: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END KioskMode)


[//]: # (BEGIN KioskMode_)

#### [KioskMode_](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`KioskMode_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/KioskMode_)

* Authority to Sign off on Conceptual Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Sign off on Code Changes: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to Curate Test Cases: [rklees](https://docu.ilias.de/go/usr/34047)
* Authority to (De-)Assign Authorities: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Issues: [rklees](https://docu.ilias.de/go/usr/34047)
* Assignee for Security Reports: [rklees](https://docu.ilias.de/go/usr/34047)

[//]: # (END KioskMode_)


[//]: # (BEGIN Language)

#### [Language Handling](https://docu.ilias.de/go/wiki/wpage_211_1357)
*Component Folders:* [`Language`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Language)

* Authority to Sign off on Conceptual Changes: [mkunkel](https://docu.ilias.de/go/usr/115)
* Authority to Sign off on Code Changes: [mkunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340), [ChrisPotter](https://docu.ilias.de/go/usr/90855), [keven.clausen](https://docu.ilias.de/go/usr/100316), [cknof](https://docu.ilias.de/go/usr/90890)
* Authority to Curate Test Cases: [ChrisPotter](https://docu.ilias.de/go/usr/90855)
* Authority to (De-)Assign Authorities: [mkunkel](https://docu.ilias.de/go/usr/115)
* Assignee for Issues: [mkunkel](https://docu.ilias.de/go/usr/115)
* Assignee for Security Reports: [mkunkel](https://docu.ilias.de/go/usr/115)

[//]: # (END Language)


[//]: # (BEGIN LanguageHandling)

#### [Language](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [mkunkel](https://docu.ilias.de/go/usr/115)
* Authority to Sign off on Code Changes: [mkunkel](https://docu.ilias.de/go/usr/115), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340), [ChrisPotter](https://docu.ilias.de/go/usr/90855), [keven.clausen](https://docu.ilias.de/go/usr/100316), [cknof](https://docu.ilias.de/go/usr/90890)
* Authority to Curate Test Cases: [ChrisPotter](https://docu.ilias.de/go/usr/90855)
* Authority to (De-)Assign Authorities: [mkunkel](https://docu.ilias.de/go/usr/115)
* Assignee for Issues: [mkunkel](https://docu.ilias.de/go/usr/115)
* Assignee for Security Reports: [mkunkel](https://docu.ilias.de/go/usr/115)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END LanguageHandling)


[//]: # (BEGIN LearningHistory)

#### [Learning History](https://docu.ilias.de/go/wiki/wpage_5454_1357)
*Component Folders:* [`LearningHistory`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LearningHistory)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [ezenzen](https://docu.ilias.de/go/usr/42910)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END LearningHistory)


[//]: # (BEGIN LearningModule)

#### [Learning Module ILIAS](https://docu.ilias.de/go/wiki/wpage_33_1357)
*Component Folders:* [`LearningModule`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LearningModule)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [Balliel](https://docu.ilias.de/go/usr/18365)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END LearningModule)


[//]: # (BEGIN LearningModuleSCORM)

#### [Scorm (aka Learning Module SCORM 1.2 and 2004)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [wischniak](https://docu.ilias.de/go/usr/21896)
* Authority to Sign off on Code Changes: [qualitus.dahme](https://docu.ilias.de/go/usr/99160), [qualitus.hartwig](https://docu.ilias.de/go/usr/104063)
* Authority to Curate Test Cases: [emix](https://docu.ilias.de/go/usr/57311)
* Authority to (De-)Assign Authorities: [wischniak](https://docu.ilias.de/go/usr/21896)
* Assignee for Issues: [wischniak](https://docu.ilias.de/go/usr/21896)
* Assignee for Security Reports: [wischniak](https://docu.ilias.de/go/usr/21896)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END LearningModuleSCORM)


[//]: # (BEGIN LearningSequence)

#### [Learning Sequence](https://docu.ilias.de/go/wiki/wpage_5557_1357)
*Component Folders:* [`LearningSequence`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LearningSequence)

* Authority to Sign off on Conceptual Changes: [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Authority to Sign off on Code Changes: [keven.clausen](https://docu.ilias.de/go/usr/100316), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340), [jeanine.auerbach](https://docu.ilias.de/go/usr/101332)
* Authority to Curate Test Cases: [jeanine.auerbach](https://docu.ilias.de/go/usr/101332)
* Authority to (De-)Assign Authorities: [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Assignee for Issues: [katrin.grosskopf](https://docu.ilias.de/go/usr/68340)
* Assignee for Security Reports: [keven.clausen](https://docu.ilias.de/go/usr/100316)

[//]: # (END LearningSequence)


[//]: # (BEGIN LegalDocuments)

#### [LegalDocuments](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`LegalDocuments`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LegalDocuments)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [AUTHOR MISSING](https://docu.ilias.de/go/pg/64423_4793)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/34047)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END LegalDocuments)


[//]: # (BEGIN LegalDocuments)

#### [Legal Documents](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`LegalDocuments`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LegalDocuments)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [AUTHOR MISSING](https://docu.ilias.de/go/pg/64423_4793)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/34047)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END LegalDocuments)


[//]: # (BEGIN Like)

#### [Like](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Like`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Like)

* Authority to Sign off on Conceptual Changes: [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to Sign off on Code Changes: [fhelfer](https://docu.ilias.de/go/usr/93367), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [fhelfer](https://docu.ilias.de/go/usr/93367), [tjoussen](https://docu.ilias.de/go/usr/103745), [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to (De-)Assign Authorities: [oliver.samoila (Databay AG)](https://docu.ilias.de/go/usr/26160)
* Assignee for Issues: [fhelfer](https://docu.ilias.de/go/usr/93367)
* Assignee for Security Reports: [fhelfer](https://docu.ilias.de/go/usr/93367)

[//]: # (END Like)


[//]: # (BEGIN Link)

#### [Link](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Link`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Link)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [nadine.bauser](https://docu.ilias.de/go/usr/34662)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Link)


[//]: # (BEGIN Locator)

#### [Locator](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Locator`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Locator)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Locator)


[//]: # (BEGIN Logging)

#### [Logging](https://docu.ilias.de/go/wiki/wpage_148_1357)
*Component Folders:* [`Logging`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Logging)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Logging)


[//]: # (BEGIN LTI)

#### [LTI Provider](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [sergiosantiago02](https://docu.ilias.de/go/usr/110174)
* Authority to Sign off on Code Changes: [Zallax](https://docu.ilias.de/go/usr/101102), [sdiaz](https://docu.ilias.de/go/usr/105654), [smeyer](https://docu.ilias.de/goto_docu_usr_191.html), [sergiosantiago02](https://docu.ilias.de/go/usr/110174)
* Authority to Curate Test Cases: [jcop](https://docu.ilias.de/go/usr/30511)
* Authority to (De-)Assign Authorities: [jcop](https://docu.ilias.de/go/usr/30511)
* Assignee for Issues: [jcop](https://docu.ilias.de/go/usr/30511)
* Assignee for Security Reports: [jcop](https://docu.ilias.de/go/usr/30511)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END LTI)


[//]: # (BEGIN LTIConsumer)

#### [LTI Consumer](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`LTIConsumer`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LTIConsumer)

* Authority to Sign off on Conceptual Changes: [sergiosantiago02](https://docu.ilias.de/go/usr/110174)
* Authority to Sign off on Code Changes: [Zallax](https://docu.ilias.de/go/usr/101102), [sdiaz](https://docu.ilias.de/go/usr/105654), [sergiosantiago02](https://docu.ilias.de/go/usr/110174)
* Authority to Curate Test Cases: [jcop](https://docu.ilias.de/go/usr/30511)
* Authority to (De-)Assign Authorities: [jcop](https://docu.ilias.de/go/usr/30511)
* Assignee for Issues: [jcop](https://docu.ilias.de/go/usr/30511)
* Assignee for Security Reports: [jcop](https://docu.ilias.de/go/usr/30511)

[//]: # (END LTIConsumer)


[//]: # (BEGIN LTIProvider)

#### [LTI](https://docu.ilias.de/go/wiki/wpage_4335_1357)
*Component Folders:* [`LTIProvider`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/LTIProvider)

* Authority to Sign off on Conceptual Changes: [sergiosantiago02](https://docu.ilias.de/go/usr/110174)
* Authority to Sign off on Code Changes: [Zallax](https://docu.ilias.de/go/usr/101102), [sdiaz](https://docu.ilias.de/go/usr/105654), [smeyer](https://docu.ilias.de/goto_docu_usr_191.html), [sergiosantiago02](https://docu.ilias.de/go/usr/110174)
* Authority to Curate Test Cases: [jcop](https://docu.ilias.de/go/usr/30511)
* Authority to (De-)Assign Authorities: [jcop](https://docu.ilias.de/go/usr/30511)
* Assignee for Issues: [jcop](https://docu.ilias.de/go/usr/30511)
* Assignee for Security Reports: [jcop](https://docu.ilias.de/go/usr/30511)

[//]: # (END LTIProvider)


[//]: # (BEGIN Mail)

#### [Mail](https://docu.ilias.de/go/wiki/wpage_36_1357)
*Component Folders:* [`Mail`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Mail)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Mail)


[//]: # (BEGIN MainMenu)

#### [Main Menu](https://docu.ilias.de/go/wiki/wpage_6549_1357)
*Component Folders:* [`MainMenu`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MainMenu)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END MainMenu)


[//]: # (BEGIN MainMenu)

#### [MainMenu](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`MainMenu`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MainMenu)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END MainMenu)


[//]: # (BEGIN Maps)

#### [Maps](https://docu.ilias.de/go/wiki/wpage_2909_1357)
*Component Folders:* [`Maps`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Maps)

* Authority to Sign off on Conceptual Changes: [jeanine.auerbach](https://docu.ilias.de/go/usr/101332)
* Authority to Sign off on Code Changes: [keven.clausen](https://docu.ilias.de/go/usr/100316), [katrin.grosskopf](https://docu.ilias.de/go/usr/68340), [jeanine.auerbach](https://docu.ilias.de/go/usr/101332)
* Authority to Curate Test Cases: [jeanine.auerbach](https://docu.ilias.de/go/usr/101332)
* Authority to (De-)Assign Authorities: [jeanine.auerbach](https://docu.ilias.de/go/usr/101332)
* Assignee for Issues: [jeanine.auerbach](https://docu.ilias.de/go/usr/101332)
* Assignee for Security Reports: [keven.clausen](https://docu.ilias.de/go/usr/100316)

[//]: # (END Maps)


[//]: # (BEGIN Math)

#### [Math](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Math`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Math)

* Authority to Sign off on Conceptual Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Sign off on Code Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Curate Test Cases: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to (De-)Assign Authorities: [fneumann](https://docu.ilias.de/go/usr/1560)
* Assignee for Issues: [fneumann](https://docu.ilias.de/go/usr/1560)
* Assignee for Security Reports: [fneumann](https://docu.ilias.de/go/usr/1560)

[//]: # (END Math)


[//]: # (BEGIN MathJax)

#### [MathJax](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`MathJax`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MathJax)

* Authority to Sign off on Conceptual Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Sign off on Code Changes: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to Curate Test Cases: [fneumann](https://docu.ilias.de/go/usr/1560)
* Authority to (De-)Assign Authorities: [fneumann](https://docu.ilias.de/go/usr/1560)
* Assignee for Issues: [fneumann](https://docu.ilias.de/go/usr/1560)
* Assignee for Security Reports: [fneumann](https://docu.ilias.de/go/usr/1560)

[//]: # (END MathJax)


[//]: # (BEGIN MediaCast)

#### [Mediacast](https://docu.ilias.de/go/wiki/wpage_258_1357)
*Component Folders:* [`MediaCast`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MediaCast)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [berggold](https://docu.ilias.de/go/usr/22199)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END MediaCast)


[//]: # (BEGIN MediaCast)

#### [MediaCast](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`MediaCast`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MediaCast)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [berggold](https://docu.ilias.de/go/usr/22199)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END MediaCast)


[//]: # (BEGIN MediaPoolsandMediaObjects)

#### [Media Pools and Media Objects](https://docu.ilias.de/go/wiki/wpage_83_1357)

*Component Folders:* [`MediaObjects`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MediaObjects), [`MediaPool`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MediaPool)


[//]: # (BEGIN MediaObjects)

##### MediaObjects
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END MediaObjects)


[//]: # (BEGIN MediaPool)

##### MediaPool
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END MediaPool)


[//]: # (END MediaPoolsandMediaObjects)

[//]: # (BEGIN MediaObjects)

#### [Media Objects](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`MediaObjects`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MediaObjects)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END MediaObjects)


[//]: # (BEGIN MediaPool)

#### [Media Pool](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`MediaPool`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MediaPool)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END MediaPool)


[//]: # (BEGIN Membership)

#### [Membership](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Membership`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Membership)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Membership)


[//]: # (BEGIN Migration)

#### [Migration](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Migration`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Migration)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Migration)


[//]: # (BEGIN Multilingualism)

#### [Multilingualism](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Multilingualism`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Multilingualism)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Multilingualism)


[//]: # (BEGIN MyStaff)

#### [Staff](https://docu.ilias.de/go/wiki/wpage_4829_1357)
*Component Folders:* [`MyStaff`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/MyStaff)

* Authority to Sign off on Conceptual Changes: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Sign off on Code Changes: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Curate Test Cases: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to (De-)Assign Authorities: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Assignee for Issues: [tschmitz](https://docu.ilias.de/go/usr/92591)
* Assignee for Security Reports: [tschmitz](https://docu.ilias.de/go/usr/92591)

[//]: # (END MyStaff)


[//]: # (BEGIN News)

#### [News](https://docu.ilias.de/go/wiki/wpage_38_1357)
*Component Folders:* [`News`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/News)

* Authority to Sign off on Conceptual Changes: [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to Sign off on Code Changes: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [tjoussen](https://docu.ilias.de/go/usr/103745), [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to (De-)Assign Authorities: [oliver.samoila (Databay AG)](https://docu.ilias.de/go/usr/26160)
* Assignee for Issues: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Assignee for Security Reports: [tjoussen](https://docu.ilias.de/go/usr/103745)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END News)


[//]: # (BEGIN Notes)

#### [Notes and Comments](https://docu.ilias.de/go/wiki/wpage_31_1357)
*Component Folders:* [`Notes`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Notes)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [skaiser](https://docu.ilias.de/go/usr/17260)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Notes)


[//]: # (BEGIN NotesAndComments)

#### [Notes (aka Notes and Comments)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [skaiser](https://docu.ilias.de/go/usr/17260)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END NotesAndComments)


[//]: # (BEGIN Notification)

#### [Notification](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Notification`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Notification)

* Authority to Sign off on Conceptual Changes: [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/goto_docu_usr_8784.html), [iszmais](https://docu.ilias.de/goto_docu_usr_65630.html)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/goto_docu_usr_8784.html), [oliver.samoila](https://docu.ilias.de/go/usr/26160), [iszmais](https://docu.ilias.de/goto_docu_usr_65630.html)
* Authority to (De-)Assign Authorities: [oliver.samoila (Databay AG)](https://docu.ilias.de/go/usr/26160)
* Assignee for Issues: [mjansen](https://docu.ilias.de/goto_docu_usr_8784.html)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/goto_docu_usr_8784.html)

[//]: # (END Notification)


[//]: # (BEGIN Notifications)

#### [Notifications](https://docu.ilias.de/go/wiki/wpage_1754_1357)
*Component Folders:* [`Notifications`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Notifications)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [iszmais](https://docu.ilias.de/go/usr/65630)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [iszmais](https://docu.ilias.de/go/usr/65630)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784), [iszmais](https://docu.ilias.de/go/usr/65630)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Notifications)


[//]: # (BEGIN ObjectService)

#### [Object Service](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to (De-)Assign Authorities: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Issues: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Reports: [skergomard](https://docu.ilias.de/go/usr/44474)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END ObjectService)


[//]: # (BEGIN OnlineHelp)

#### [Help (aka Online Help)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149), [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END OnlineHelp)


[//]: # (BEGIN OpenIdConect)

#### [Open ID Connect](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END OpenIdConect)


[//]: # (BEGIN OrgUnit)

#### [Organisational Units](https://docu.ilias.de/go/wiki/wpage_2265_1357)
*Component Folders:* [`OrgUnit`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/OrgUnit)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [lschmidt-tf](https://docu.ilias.de/go/usr/120143)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087), [maalers](https://docu.ilias.de/go/usr/119188)
* Authority to Curate Test Cases: [wischniak](https://docu.ilias.de/go/usr/21896)
* Authority to (De-)Assign Authorities: [maalers](https://docu.ilias.de/go/usr/119188)
* Assignee for Issues: [maalers](https://docu.ilias.de/go/usr/119188)
* Assignee for Security Reports: [maalers](https://docu.ilias.de/go/usr/119188)

[//]: # (END OrgUnit)


[//]: # (BEGIN Password)

#### [Password](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Password`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Password)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Password)


[//]: # (BEGIN PermanentLink)

#### [Permanent Links](https://docu.ilias.de/go/wiki/wpage_575_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`PermanentLink`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/PermanentLink)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END PermanentLink)


[//]: # (BEGIN PersonalandSharedResources)

#### [Personal and Shared Resources](https://docu.ilias.de/go/wiki/wpage_1338_1357)

*Component Folders:* [`PersonalWorkspace`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/PersonalWorkspace), [`WorkspaceFolder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WorkspaceFolder), [`WorkspaceRootFolder`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WorkspaceRootFolder)


[//]: # (BEGIN PersonalWorkspace)

##### PersonalWorkspace
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END PersonalWorkspace)


[//]: # (BEGIN WorkspaceFolder)

##### WorkspaceFolder
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END WorkspaceFolder)


[//]: # (BEGIN WorkspaceRootFolder)

##### WorkspaceRootFolder
* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END WorkspaceRootFolder)


[//]: # (END PersonalandSharedResources)

[//]: # (BEGIN Poll)

#### [Poll](https://docu.ilias.de/go/wiki/wpage_2590_1357)
*Component Folders:* [`Poll`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Poll)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191), [tschmitz](https://docu.ilias.de/go/usr/92591)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Poll)


[//]: # (BEGIN Portfolio)

#### [Portfolio](https://docu.ilias.de/go/wiki/wpage_353_1357)
*Component Folders:* [`Portfolio`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Portfolio)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [ezenzen](https://docu.ilias.de/go/usr/42910)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Portfolio)


[//]: # (BEGIN QTI)

#### [QTI](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`QTI`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/QTI)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END QTI)


[//]: # (BEGIN Randomization)

#### [Randomization](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Randomization`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Randomization)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Randomization)


[//]: # (BEGIN Rating)

#### [Rating](https://docu.ilias.de/go/wiki/wpage_2784_1357)
*Component Folders:* [`Rating`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Rating)

* Authority to Sign off on Conceptual Changes: [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to Sign off on Code Changes: [fhelfer](https://docu.ilias.de/go/usr/93367)
* Authority to Curate Test Cases: [fhelfer](https://docu.ilias.de/go/usr/93367), [oliver.samoila](https://docu.ilias.de/go/usr/26160)
* Authority to (De-)Assign Authorities: [oliver.samoila (Databay AG)](https://docu.ilias.de/go/usr/26160)
* Assignee for Issues: [fhelfer](https://docu.ilias.de/go/usr/93367)
* Assignee for Security Reports: [fhelfer](https://docu.ilias.de/go/usr/93367)

[//]: # (END Rating)


[//]: # (BEGIN RBAC)

#### [RBAC / Access Control](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Issues: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Reports: [skergomard](https://docu.ilias.de/go/usr/44474)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END RBAC)


[//]: # (BEGIN Refinery)

#### [Refinery](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Refinery`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Refinery)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)

[//]: # (END Refinery)


[//]: # (BEGIN ECSInterfaceELearningCommunityServer)

#### [ECS Interface – E-Learning Community Server](https://docu.ilias.de/go/wiki/wpage_1132_1357)

*Component Folders:* [`RemoteCategory`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteCategory), [`RemoteCourse`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteCourse), [`RemoteFile`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteFile), [`RemoteGlossary`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteGlossary), [`RemoteGroup`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteGroup), [`RemoteLearningModule`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteLearningModule), [`RemoteTest`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteTest), [`RemoteWiki`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RemoteWiki)


[//]: # (BEGIN RemoteCategory)

##### RemoteCategory
* Authority to Sign off on Conceptual Changes: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Authority to Sign off on Code Changes: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Authority to Curate Test Cases: [jheim](https://docu.ilias.de/go/usr/40167), [SIG CampusConnect und ECS(A)](https://docu.ilias.de/go/grp/7893)
* Authority to (De-)Assign Authorities: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Assignee for Issues: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Assignee for Security Reports: [sdyhr](https://docu.ilias.de/go/usr/102107)

[//]: # (END RemoteCategory)


[//]: # (BEGIN RemoteCourse)

##### RemoteCourse
* Authority to Sign off on Conceptual Changes: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Authority to Sign off on Code Changes: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Authority to Curate Test Cases: [jheim](https://docu.ilias.de/go/usr/40167), [SIG CampusConnect und ECS(A)](https://docu.ilias.de/go/grp/7893)
* Authority to (De-)Assign Authorities: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Assignee for Issues: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Assignee for Security Reports: [sdyhr](https://docu.ilias.de/go/usr/102107)

[//]: # (END RemoteCourse)


[//]: # (BEGIN RemoteFile)

##### RemoteFile
* Authority to Sign off on Conceptual Changes: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Authority to Sign off on Code Changes: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Authority to Curate Test Cases: [jheim](https://docu.ilias.de/go/usr/40167), [SIG CampusConnect und ECS(A)](https://docu.ilias.de/go/grp/7893)
* Authority to (De-)Assign Authorities: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Assignee for Issues: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Assignee for Security Reports: [sdyhr](https://docu.ilias.de/go/usr/102107)

[//]: # (END RemoteFile)


[//]: # (BEGIN RemoteGlossary)

##### RemoteGlossary
* Authority to Sign off on Conceptual Changes: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Authority to Sign off on Code Changes: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Authority to Curate Test Cases: [jheim](https://docu.ilias.de/go/usr/40167), [SIG CampusConnect und ECS(A)](https://docu.ilias.de/go/grp/7893)
* Authority to (De-)Assign Authorities: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Assignee for Issues: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Assignee for Security Reports: [sdyhr](https://docu.ilias.de/go/usr/102107)

[//]: # (END RemoteGlossary)


[//]: # (BEGIN RemoteGroup)

##### RemoteGroup
* Authority to Sign off on Conceptual Changes: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Authority to Sign off on Code Changes: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Authority to Curate Test Cases: [jheim](https://docu.ilias.de/go/usr/40167), [SIG CampusConnect und ECS(A)](https://docu.ilias.de/go/grp/7893)
* Authority to (De-)Assign Authorities: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Assignee for Issues: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Assignee for Security Reports: [sdyhr](https://docu.ilias.de/go/usr/102107)

[//]: # (END RemoteGroup)


[//]: # (BEGIN RemoteLearningModule)

##### RemoteLearningModule
* Authority to Sign off on Conceptual Changes: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Authority to Sign off on Code Changes: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Authority to Curate Test Cases: [jheim](https://docu.ilias.de/go/usr/40167), [SIG CampusConnect und ECS(A)](https://docu.ilias.de/go/grp/7893)
* Authority to (De-)Assign Authorities: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Assignee for Issues: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Assignee for Security Reports: [sdyhr](https://docu.ilias.de/go/usr/102107)

[//]: # (END RemoteLearningModule)


[//]: # (BEGIN RemoteTest)

##### RemoteTest
* Authority to Sign off on Conceptual Changes: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Authority to Sign off on Code Changes: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Authority to Curate Test Cases: [jheim](https://docu.ilias.de/go/usr/40167), [SIG CampusConnect und ECS(A)](https://docu.ilias.de/go/grp/7893)
* Authority to (De-)Assign Authorities: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Assignee for Issues: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Assignee for Security Reports: [sdyhr](https://docu.ilias.de/go/usr/102107)

[//]: # (END RemoteTest)


[//]: # (BEGIN RemoteWiki)

##### RemoteWiki
* Authority to Sign off on Conceptual Changes: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Authority to Sign off on Code Changes: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Authority to Curate Test Cases: [jheim](https://docu.ilias.de/go/usr/40167), [SIG CampusConnect und ECS(A)](https://docu.ilias.de/go/grp/7893)
* Authority to (De-)Assign Authorities: [bogen](https://docu.ilias.de/go/usr/13815), [mglaubitz](https://docu.ilias.de/go/usr/28309)
* Assignee for Issues: [sdyhr](https://docu.ilias.de/go/usr/102107)
* Assignee for Security Reports: [sdyhr](https://docu.ilias.de/go/usr/102107)

[//]: # (END RemoteWiki)


[//]: # (END ECSInterfaceELearningCommunityServer)

[//]: # (BEGIN ResourceStorage)

#### [ILIAS Resource Storage Service](https://docu.ilias.de/go/wiki/wpage_6729_1357)
*Component Folders:* [`ResourceStorage`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ResourceStorage)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END ResourceStorage)


[//]: # (BEGIN RTE)

#### [RTE](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`RTE`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/RTE)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END RTE)


[//]: # (BEGIN Saml)

#### [SAML](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Saml`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Saml)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END Saml)


[//]: # (BEGIN LearningModuleSCORM)

#### [Learning Module SCORM](https://docu.ilias.de/go/wiki/wpage_32_1357)

*Component Folders:* [`Scorm2004`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Scorm2004), [`ScormAicc`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/ScormAicc)


[//]: # (BEGIN Scorm2004)

##### Scorm2004
* Authority to Sign off on Conceptual Changes: [wischniak](https://docu.ilias.de/go/usr/21896)
* Authority to Sign off on Code Changes: [qualitus.dahme](https://docu.ilias.de/go/usr/99160), [qualitus.hartwig](https://docu.ilias.de/go/usr/104063)
* Authority to Curate Test Cases: [emix](https://docu.ilias.de/go/usr/57311)
* Authority to (De-)Assign Authorities: [wischniak](https://docu.ilias.de/go/usr/21896)
* Assignee for Issues: [wischniak](https://docu.ilias.de/go/usr/21896)
* Assignee for Security Reports: [wischniak](https://docu.ilias.de/go/usr/21896)

[//]: # (END Scorm2004)


[//]: # (BEGIN ScormAicc)

##### ScormAicc
* Authority to Sign off on Conceptual Changes: [wischniak](https://docu.ilias.de/go/usr/21896)
* Authority to Sign off on Code Changes: [qualitus.dahme](https://docu.ilias.de/go/usr/99160), [qualitus.hartwig](https://docu.ilias.de/go/usr/104063)
* Authority to Curate Test Cases: [emix](https://docu.ilias.de/go/usr/57311)
* Authority to (De-)Assign Authorities: [wischniak](https://docu.ilias.de/go/usr/21896)
* Assignee for Issues: [wischniak](https://docu.ilias.de/go/usr/21896)
* Assignee for Security Reports: [wischniak](https://docu.ilias.de/go/usr/21896)

[//]: # (END ScormAicc)


[//]: # (END LearningModuleSCORM)

[//]: # (BEGIN Search)

#### [Search](https://docu.ilias.de/go/wiki/wpage_11_1357)
*Component Folders:* [`Search`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Search)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Search)


[//]: # (BEGIN Session)

#### [Session (Course & Group)](https://docu.ilias.de/go/wiki/wpage_2172_1357)
*Component Folders:* [`Session`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Session)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Session)


[//]: # (BEGIN Session)

#### [Session](https://docu.ilias.de/go/wiki/wpage_2172_1357)
*Component Folders:* [`Session`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Session)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [MISSING]
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Session)


[//]: # (BEGIN Setup)

#### [Setup](https://docu.ilias.de/go/wiki/wpage_40_1357)
*Component Folders:* [`Setup`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Setup)

* Authority to Sign off on Conceptual Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END Setup)


[//]: # (BEGIN setup_)

#### [setup_](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`setup_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/setup_)

* Authority to Sign off on Conceptual Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END setup_)


[//]: # (BEGIN Skill)

#### [Competence Management](https://docu.ilias.de/go/wiki/wpage_1161_1357)
*Component Folders:* [`Skill`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Skill)

* Authority to Sign off on Conceptual Changes: [cludolf](https://docu.ilias.de/go/usr/97658)
* Authority to Sign off on Code Changes: [cludolf](https://docu.ilias.de/go/usr/97658), [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [atoedt](https://docu.ilias.de/go/usr/3139)
* Authority to (De-)Assign Authorities: [cludolf](https://docu.ilias.de/go/usr/97658)
* Assignee for Issues: [cludolf](https://docu.ilias.de/go/usr/97658)
* Assignee for Security Reports: [cludolf](https://docu.ilias.de/go/usr/97658)

[//]: # (END Skill)


[//]: # (BEGIN soap)

#### [soap](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`soap`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/soap)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END soap)


[//]: # (BEGIN SOAPAuth)

#### [SOAP](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`SOAPAuth`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/SOAPAuth)

* Authority to Sign off on Conceptual Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Curate Test Cases: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to (De-)Assign Authorities: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [PerPascalSeeland](https://docu.ilias.de/go/usr/31492), [mjansen](https://docu.ilias.de/go/usr/8784)

[//]: # (END SOAPAuth)


[//]: # (BEGIN StaticURL)

#### [StaticURL](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`StaticURL`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/StaticURL)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END StaticURL)


[//]: # (BEGIN StudyProgramme)

#### [Study Programme](https://docu.ilias.de/go/wiki/wpage_3391_1357)

*Component Folders:* [`StudyProgramme`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/StudyProgramme), [`StudyProgrammeReference`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/StudyProgrammeReference)


[//]: # (BEGIN StudyProgramme)

##### StudyProgramme
* Authority to Sign off on Conceptual Changes: [lschmidt-tf](https://docu.ilias.de/go/usr/120143)
* Authority to Sign off on Code Changes: [maalers](https://docu.ilias.de/go/usr/119188)
* Authority to Curate Test Cases: [maalers](https://docu.ilias.de/go/usr/119188)
* Authority to (De-)Assign Authorities: [maalers](https://docu.ilias.de/go/usr/119188)
* Assignee for Issues: [maalers](https://docu.ilias.de/go/usr/119188)
* Assignee for Security Reports: [maalers](https://docu.ilias.de/go/usr/119188)

[//]: # (END StudyProgramme)


[//]: # (BEGIN StudyProgrammeReference)

##### StudyProgrammeReference
* Authority to Sign off on Conceptual Changes: [lschmidt-tf](https://docu.ilias.de/go/usr/120143)
* Authority to Sign off on Code Changes: [maalers](https://docu.ilias.de/go/usr/119188)
* Authority to Curate Test Cases: [maalers](https://docu.ilias.de/go/usr/119188)
* Authority to (De-)Assign Authorities: [maalers](https://docu.ilias.de/go/usr/119188)
* Assignee for Issues: [maalers](https://docu.ilias.de/go/usr/119188)
* Assignee for Security Reports: [maalers](https://docu.ilias.de/go/usr/119188)

[//]: # (END StudyProgrammeReference)


[//]: # (END StudyProgramme)

[//]: # (BEGIN Style)

#### [Style](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Style`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Style)

* Authority to Sign off on Conceptual Changes: [BettyFromHH](https://docu.ilias.de/go/usr/96573)
* Authority to Sign off on Code Changes: [BettyFromHH](https://docu.ilias.de/go/usr/96573), [rotegras](https://docu.ilias.de/go/usr/88399), [padvincenzo](https://docu.ilias.de/go/usr/87189)
* Authority to Curate Test Cases: [BettyFromHH](https://docu.ilias.de/go/usr/96573)
* Authority to (De-)Assign Authorities: [BettyFromHH](https://docu.ilias.de/go/usr/96573)
* Assignee for Issues: [BettyFromHH](https://docu.ilias.de/go/usr/96573)
* Assignee for Security Reports: [BettyFromHH](https://docu.ilias.de/go/usr/96573)

[//]: # (END Style)


[//]: # (BEGIN Survey)

#### [Survey](https://docu.ilias.de/go/wiki/wpage_27_1357)

*Component Folders:* [`Survey`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Survey), [`SurveyQuestionPool`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/SurveyQuestionPool)


[//]: # (BEGIN Survey)

##### Survey
* Authority to Sign off on Conceptual Changes: [sergiosant02](https://docu.ilias.de/go/usr/110174)
* Authority to Sign off on Code Changes: [sergiosant02](https://docu.ilias.de/go/usr/110174), [abrahammordev](https://docu.ilias.de/go/usr/110909), [juanma1331](https://docu.ilias.de/go/usr/107249)
* Authority to Curate Test Cases: [ezenzen](https://docu.ilias.de/go/usr/42910)
* Authority to (De-)Assign Authorities: [jcopado](https://docu.ilias.de/go/usr/30511)
* Assignee for Issues: [jcopado](https://docu.ilias.de/go/usr/30511)
* Assignee for Security Reports: [jcopado](https://docu.ilias.de/go/usr/30511)

[//]: # (END Survey)


[//]: # (BEGIN SurveyQuestionPool)

##### SurveyQuestionPool
* Authority to Sign off on Conceptual Changes: [sergiosant02](https://docu.ilias.de/go/usr/110174)
* Authority to Sign off on Code Changes: [sergiosant02](https://docu.ilias.de/go/usr/110174), [abrahammordev](https://docu.ilias.de/go/usr/110909), [juanma1331](https://docu.ilias.de/go/usr/107249)
* Authority to Curate Test Cases: [ezenzen](https://docu.ilias.de/go/usr/42910)
* Authority to (De-)Assign Authorities: [jcopado](https://docu.ilias.de/go/usr/30511)
* Assignee for Issues: [jcopado](https://docu.ilias.de/go/usr/30511)
* Assignee for Security Reports: [jcopado](https://docu.ilias.de/go/usr/30511)

[//]: # (END SurveyQuestionPool)


[//]: # (END Survey)

[//]: # (BEGIN SystemCheck)

#### [System Check](https://docu.ilias.de/go/wiki/wpage_2093_1357)
*Component Folders:* [`SystemCheck`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/SystemCheck)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END SystemCheck)


[//]: # (BEGIN Table)

#### [Table](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Table`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Table)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Table)


[//]: # (BEGIN Tagging)

#### [Tagging](https://docu.ilias.de/go/wiki/wpage_140_1357)
*Component Folders:* [`Tagging`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Tagging)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [skaiser](https://docu.ilias.de/go/usr/17260)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Tagging)


[//]: # (BEGIN Tasks)

#### [Task Service](https://docu.ilias.de/go/wiki/wpage_5108_1357)
*Component Folders:* [`Tasks`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Tasks)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Tasks)


[//]: # (BEGIN Tasks)

#### [Tasks](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Tasks`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Tasks)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [akill](https://docu.ilias.de/go/usr/149)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Tasks)


[//]: # (BEGIN Taxonomy)

#### [Taxonomy Service](https://docu.ilias.de/go/wiki/wpage_2304_1357)
*Component Folders:* [`Taxonomy`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Taxonomy)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: Tested separately in each module that supports taxonomies
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Taxonomy)


[//]: # (BEGIN Taxonomy)

#### [Taxonomy](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Taxonomy`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Taxonomy)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: Tested separately in each module that supports taxonomies
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Taxonomy)


[//]: # (BEGIN TermsOfService)

#### [TermsOfService (aka Terms of Services)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`TermsOfService`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/TermsOfService)

* Authority to Sign off on Conceptual Changes: [mjansen](https://docu.ilias.de/go/usr/8784)
* Authority to Sign off on Code Changes: [mjansen](https://docu.ilias.de/go/usr/8784), [lscharmer](https://docu.ilias.de/go/usr/87863)
* Authority to Curate Test Cases: [AUTHOR MISSING](https://docu.ilias.de/go/pg/64423_4793)
* Authority to (De-)Assign Authorities: [mjansen (Databay AG)](https://docu.ilias.de/go/usr/8784)
* Assignee for Issues: [mjansen](https://docu.ilias.de/go/usr/8784)
* Assignee for Security Reports: [mjansen](https://docu.ilias.de/go/usr/8784)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END TermsOfService)


[//]: # (BEGIN TestAssessment)

#### [Test & Assessment](https://docu.ilias.de/go/wiki/wpage_26_1357)

*Component Folders:* [`Test`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Test), [`TestQuestionPool`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/TestQuestionPool)


[//]: # (BEGIN Test)

##### Test
* Authority to Sign off on Conceptual Changes: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Authority to Sign off on Code Changes: [mbecker](https://docu.ilias.de/go/usr/27266), [skergomard](https://docu.ilias.de/go/usr/44474), [dstrassner](https://docu.ilias.de/go/usr/48931), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Authority to (De-)Assign Authorities: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Assignee for Issues: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Assignee for Security Reports: [dstrassner](https://docu.ilias.de/go/usr/48931)

[//]: # (END Test)


[//]: # (BEGIN TestQuestionPool)

##### TestQuestionPool
* Authority to Sign off on Conceptual Changes: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Authority to Sign off on Code Changes: [mbecker](https://docu.ilias.de/go/usr/27266), [skergomard](https://docu.ilias.de/go/usr/44474), [dstrassner](https://docu.ilias.de/go/usr/48931), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Authority to (De-)Assign Authorities: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Assignee for Issues: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Assignee for Security Reports: [dstrassner](https://docu.ilias.de/go/usr/48931)

[//]: # (END TestQuestionPool)


[//]: # (END TestAssessment)

[//]: # (BEGIN TestAndAssessment)

#### [Test and TestQuestionPool (aka Test & Assessment)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Authority to Sign off on Code Changes: [mbecker](https://docu.ilias.de/go/usr/27266), [skergomard](https://docu.ilias.de/go/usr/44474), [dstrassner](https://docu.ilias.de/go/usr/48931), [tjoussen](https://docu.ilias.de/go/usr/103745)
* Authority to Curate Test Cases: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Authority to (De-)Assign Authorities: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Assignee for Issues: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Assignee for Security Reports: [dstrassner](https://docu.ilias.de/go/usr/48931)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END TestAndAssessment)


[//]: # (BEGIN Tracking)

#### [Statistics and Learning Progress](https://docu.ilias.de/go/wiki/wpage_189_1357)
*Component Folders:* [`Tracking`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Tracking)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [AUTHOR MISSING](https://docu.ilias.de/go/pg/64423_4793)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END Tracking)


[//]: # (BEGIN Tree)

#### [Tree](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`Tree`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Tree)

* Authority to Sign off on Conceptual Changes: [Fabian Wolf](https://docu.ilias.de/go/usr/29018)
* Authority to Sign off on Code Changes: [Fabian Wolf](https://docu.ilias.de/go/usr/29018)
* Authority to Curate Test Cases: [Fabian Wolf](https://docu.ilias.de/go/usr/29018)
* Authority to (De-)Assign Authorities: [Fabian Wolf](https://docu.ilias.de/go/usr/29018)
* Assignee for Issues: [Fabian Wolf](https://docu.ilias.de/go/usr/29018)
* Assignee for Security Reports: [Fabian Wolf](https://docu.ilias.de/go/usr/29018)

[//]: # (END Tree)


[//]: # (BEGIN Types)

#### [Types](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Types`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Types)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Types)


[//]: # (BEGIN UserInterface)

#### [User Interface](https://docu.ilias.de/go/wiki/wpage_29_1357)

*Component Folders:* [`UI`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/UI), [`UIComponent`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/UIComponent), [`UICore`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/UICore), [`UI_`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/UI_)


[//]: # (BEGIN UI)

##### UI
* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE
* Unit-specific Guidelines, Rules, and Regulations: [Guidelines](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md)

[//]: # (END UI)


[//]: # (BEGIN UIComponent)

##### UIComponent
* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE
* Unit-specific Guidelines, Rules, and Regulations: [Guidelines](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md)

[//]: # (END UIComponent)


[//]: # (BEGIN UICore)

##### UICore
* Authority to Sign off on Conceptual Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Authority to Sign off on Code Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Authority to (De-)Assign Authorities: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Issues: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Security Reports: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END UICore)


[//]: # (BEGIN UI_)

##### UI_
* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE
* Unit-specific Guidelines, Rules, and Regulations: [Guidelines](https://github.com/ILIAS-eLearning/ILIAS/blob/trunk/components/ILIAS/UI/docs/COMMUNITY.md)

[//]: # (END UI_)


[//]: # (END UserInterface)

[//]: # (BEGIN UICore)

#### [UICore](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`UICore`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/UICore)

* Authority to Sign off on Conceptual Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Authority to Sign off on Code Changes: [tfuhrer](https://docu.ilias.de/go/usr/81947), [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Authority to (De-)Assign Authorities: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Issues: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Assignee for Security Reports: [tfuhrer](https://docu.ilias.de/go/usr/81947)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END UICore)


[//]: # (BEGIN User)

#### [User Service](https://docu.ilias.de/go/wiki/wpage_332_1357)
*Component Folders:* [`User`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/User)

* Authority to Sign off on Conceptual Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to (De-)Assign Authorities: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Issues: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Reports: [skergomard](https://docu.ilias.de/go/usr/44474)

[//]: # (END User)


[//]: # (BEGIN UserService)

#### [User (aka User Service)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Sign off on Code Changes: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to Curate Test Cases: [skergomard](https://docu.ilias.de/go/usr/44474)
* Authority to (De-)Assign Authorities: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Issues: [skergomard](https://docu.ilias.de/go/usr/44474)
* Assignee for Security Reports: [skergomard](https://docu.ilias.de/go/usr/44474)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END UserService)


[//]: # (BEGIN Utilities)

#### [Utilities](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Utilities`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Utilities)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Utilities)


[//]: # (BEGIN Verification)

#### [Verification](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Verification`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Verification)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Verification)


[//]: # (BEGIN VirusScanner)

#### [VirusScanner](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`VirusScanner`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/VirusScanner)

* Authority to Sign off on Conceptual Changes: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to Sign off on Code Changes: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to Curate Test Cases: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to (De-)Assign Authorities: [rschenk (Databay AG)](https://docu.ilias.de/go/usr/18065)
* Assignee for Issues: [rschenk](https://docu.ilias.de/go/usr/18065)
* Assignee for Security Reports: [rschenk](https://docu.ilias.de/go/usr/18065)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END VirusScanner)


[//]: # (BEGIN VirusScanner)

#### [Virus Scanner](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`VirusScanner`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/VirusScanner)

* Authority to Sign off on Conceptual Changes: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to Sign off on Code Changes: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to Curate Test Cases: [rschenk](https://docu.ilias.de/go/usr/18065)
* Authority to (De-)Assign Authorities: [rschenk (Databay AG)](https://docu.ilias.de/go/usr/18065)
* Assignee for Issues: [rschenk](https://docu.ilias.de/go/usr/18065)
* Assignee for Security Reports: [rschenk](https://docu.ilias.de/go/usr/18065)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END VirusScanner)


[//]: # (BEGIN WebAccessChecker)

#### [Security (incl. Web Access Checker)](https://docu.ilias.de/go/wiki/wpage_866_1357)
*Component Folders:* [`WebAccessChecker`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WebAccessChecker)

* Authority to Sign off on Conceptual Changes: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Authority to Sign off on Code Changes: [fwolf-ilias](https://docu.ilias.de/go/usr/29018), [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [AUTHOR MISSING](https://docu.ilias.de/go/pg/64423_4793)
* Authority to (De-)Assign Authorities: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Assignee for Issues: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Assignee for Security Reports: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END WebAccessChecker)


[//]: # (BEGIN WebAccessChecker)

#### [Web Access Checker](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`WebAccessChecker`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WebAccessChecker)

* Authority to Sign off on Conceptual Changes: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Authority to Sign off on Code Changes: [fwolf-ilias](https://docu.ilias.de/go/usr/29018), [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [AUTHOR MISSING](https://docu.ilias.de/go/pg/64423_4793)
* Authority to (De-)Assign Authorities: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Assignee for Issues: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Assignee for Security Reports: [fwolf-ilias](https://docu.ilias.de/go/usr/29018)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END WebAccessChecker)


[//]: # (BEGIN WebDAV)

#### [WebDAV](https://docu.ilias.de/go/wiki/wpage_5484_1357)
*Component Folders:* [`WebDAV`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WebDAV)

* Authority to Sign off on Conceptual Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Sign off on Code Changes: [fschmid](https://docu.ilias.de/go/usr/21087)
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Issues: [fschmid](https://docu.ilias.de/go/usr/21087)
* Assignee for Security Reports: [fschmid](https://docu.ilias.de/go/usr/21087)

[//]: # (END WebDAV)


[//]: # (BEGIN WebFeed)

#### [Feed (aka Web Feeds)](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: [kunkel](https://docu.ilias.de/go/usr/115)
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END WebFeed)


[//]: # (BEGIN WebResource)

#### [Weblink](https://docu.ilias.de/go/wiki/wpage_1420_1357)
*Component Folders:* [`WebResource`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WebResource)

* Authority to Sign off on Conceptual Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Sign off on Code Changes: [smeyer](https://docu.ilias.de/go/usr/191)
* Authority to Curate Test Cases: [nadine.bauser](https://docu.ilias.de/go/usr/34662)
* Authority to (De-)Assign Authorities: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Issues: [smeyer](https://docu.ilias.de/go/usr/191)
* Assignee for Security Reports: [smeyer](https://docu.ilias.de/go/usr/191)

[//]: # (END WebResource)


[//]: # (BEGIN WebServices)

#### [Web Services Overview: SOAP, REST, ...](https://docu.ilias.de/go/wiki/wpage_186_1357)
*Component Folders:* [`WebServices`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WebServices)

* Authority to Sign off on Conceptual Changes: [githamo](https://docu.ilias.de/go/usr/115389)
* Authority to Sign off on Code Changes: [githamo](https://docu.ilias.de/go/usr/115389), [sKarki999](https://docu.ilias.de/go/usr/112949)
* Authority to Curate Test Cases: [sKarki999](https://docu.ilias.de/go/usr/112949)
* Authority to (De-)Assign Authorities: [TimoScheuer](https://docu.ilias.de/go/usr/102976)
* Assignee for Issues: [sKarki999](https://docu.ilias.de/go/usr/112949)
* Assignee for Security Reports: [sKarki999](https://docu.ilias.de/go/usr/112949)

[//]: # (END WebServices)


[//]: # (BEGIN Webservices)

#### [Webservices](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [githamo](https://docu.ilias.de/go/usr/115389)
* Authority to Sign off on Code Changes: [githamo](https://docu.ilias.de/go/usr/115389), [sKarki999](https://docu.ilias.de/go/usr/112949)
* Authority to Curate Test Cases: [sKarki999](https://docu.ilias.de/go/usr/112949)
* Authority to (De-)Assign Authorities: [TimoScheuer](https://docu.ilias.de/go/usr/102976)
* Assignee for Issues: [sKarki999](https://docu.ilias.de/go/usr/112949)
* Assignee for Security Reports: [sKarki999](https://docu.ilias.de/go/usr/112949)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END Webservices)


[//]: # (BEGIN Wiki)

#### [Wiki](https://docu.ilias.de/go/wiki/wpage_34_1357)
*Component Folders:* [`Wiki`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Wiki)

* Authority to Sign off on Conceptual Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Sign off on Code Changes: [akill](https://docu.ilias.de/go/usr/149)
* Authority to Curate Test Cases: n.n., Uni Köln
* Authority to (De-)Assign Authorities: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Issues: [akill](https://docu.ilias.de/go/usr/149)
* Assignee for Security Reports: [akill](https://docu.ilias.de/go/usr/149)

[//]: # (END Wiki)


[//]: # (BEGIN WOPI)

#### [WOPI](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* [`WOPI`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/WOPI)

* Authority to Sign off on Conceptual Changes: fschmid
* Authority to Sign off on Code Changes: fschmid
* Authority to Curate Test Cases: fschmid
* Authority to (De-)Assign Authorities: fschmid
* Assignee for Issues: fschmid
* Assignee for Security Reports: fschmid

[//]: # (END WOPI)


[//]: # (BEGIN xAPIAndcmi5)

#### [xAPI/cmi5](https://docu.ilias.de/go/wiki/wpage_1_1357)
*Component Folders:* *(no dedicated folder in repository)*

* Authority to Sign off on Conceptual Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Sign off on Code Changes: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to Curate Test Cases: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Authority to (De-)Assign Authorities: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Issues: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Assignee for Security Reports: [ukohnle](https://docu.ilias.de/go/usr/21855)
* Unit-specific Guidelines, Rules, and Regulations: [LINK MISSING]('')

[//]: # (END xAPIAndcmi5)


[//]: # (BEGIN Xml)

#### [Xml](https://docu.ilias.de/go/wiki/wpage_1_1357)

**Status:** Unmaintained / NONE
*Component Folders:* [`Xml`](https://github.com/ILIAS-eLearning/ILIAS/tree/trunk/components/ILIAS/Xml)

* Authority to Sign off on Conceptual Changes: NONE
* Authority to Sign off on Code Changes: NONE
* Authority to Curate Test Cases: NONE
* Authority to (De-)Assign Authorities: NONE
* Assignee for Issues: NONE
* Assignee for Security Reports: NONE

[//]: # (END Xml)

