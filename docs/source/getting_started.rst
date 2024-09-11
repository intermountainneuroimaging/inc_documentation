.. _getting_started:

Overview
========
Flywheel.io is an imaging platform used to receive, curate, manage, and analyze data from scientific facilities. Intermountain Neuroimaging Consortium (INC) is excited to host an “on premise” deployment of Flywheel.io for clinical, industry, and academic researchers within the region. The “on premise” instance means all data storage as well as computation is completed using University of Colorado services. INC at CU Boulder has leveraged the power of Flywheel.io and the considerable resources available through University of Colorado Research Computing to provide a seamless experience for all researchers from data collection at our MRI facilities to data analysis, visualization, and publication.

For those familiar with other “PACS” systems, Flywheel also provides a service to receive and view data directly from the Intermountain Neuroimaging Consortium's 3T Prisma Fit MR scanner.

Most importantly, Flywheel is a FAIR compliant platform. **F-A-I-R** are a set of data principles adopted by both the National Science Foundation (NSF) and National Institute of Health (NIH, beginning 2023) to prompt transparency and reproducibility. **F**\indability, **A**\ccessibility, **I**\nteroperability, and **R**\euse cornerstone these principles. Flywheel supports the FAIR data practice mission by ensuring rich metadata for all data stored within the platform. Flywheel also enforces the use of provenance, meaning the storage of information about "who, what, when, how" in data creation and management. By conforming to these best data practices, INC hopes to elevate the importance of transparent and reproducible research in the neuroimaging community.

Interested in learning more? Check out our introductory video `here <https://o365coloradoedu.sharepoint.com/:v:/s/INC-microsoft-teams/EcA4VTfuZzdAiCAvN19Y1qkBazUkLHGT9A-LddKcIKgoUQ?e=qGclwA>`_.

Also, check out Introduction to Flywheel Webinar `here <https://docs.flywheel.io/hc/en-us/articles/4536038984595-Webinar-series-Intro-to-Flywheel>`_.

At the Scanner
==============
Before starting a new or existing study in Flywheel, please set up a meeting with the Intermountain Neuroimaging Consortium Staff (`website <https://www.colorado.edu/mri/people>`_) who can help discuss your specific needs. While Flywheel.io provides almost endless flexibility in implementation of the platform, there are a few **critical** actions that must take place to ensure every image collected at INC lands in Flywheel in the right place.

Naming your Flywheel Session
*****************************
In order to ensure acquisitions are assigned to the correct Project, Subject, and Session this information **MUST** be entered at the scanner console correctly (in the field labelled **Accession Number**), using the following convention:
::

    Flywheel Accession Number Naming Convention:
    <project-label> / <subject-label> / <session-label>

While no constraints are placed on the format within each label, we highly recommend using BIDS_ compliant naming schemes for subject and session labels.

.. _BIDS: https://bids-specification.readthedocs.io/en/stable/02-common-principles.html

A minimal amount of additional information may be entered at the scanner for any study participant or scan session.
This information includes:

+---------------------+-----------------------------+--------------------------------+
| Scanner Field       | Usage                       | Notes                          |
+=====================+=============================+================================+
| Referring Physician | Principal Investigator      | (Required)                     |
+---------------------+-----------------------------+--------------------------------+
| Accession Number    | Flywheel Naming Convention  | (Required)                     |
+---------------------+-----------------------------+--------------------------------+
| Patient ID/Name     | URSI Identifier             | (Co-Enrollment in COINS Only)  |
+---------------------+-----------------------------+--------------------------------+
| Age                 | Age                         | (Co-Enrollment in COINS Only)  |
+---------------------+-----------------------------+--------------------------------+
| Gender              | Gender                      | (Co-Enrollment in COINS Only)  |
+---------------------+-----------------------------+--------------------------------+

INC currently records this information using the Scanner Requisition Form which should be submitted before each scan session. Still have questions? Check out our :ref:`faqs` page.

.. note::
    The naming convention outlined above is specific only to the INC instance of Flywheel. Other neuroimaging centers have individual conventions for tracking project, subject, and session IDs from during image acquisition.

Examples of Accession Numbers
*****************************

Study A has enrolled John Snow into their study, this is a longitudinal study, where the participant will return for 3 separate neuroimaging sessions. Below is an example of what is entered for the Accession Number field on the scanner console.

    :StudyA/101/S01:  The participant is assigned a subject-id of 101 and session-id of S01.

Importantly, Flywheel is different from COINS in that you do not need to pre-register your participants with his/her ID apriori (before the scan). In fact, INC recommends that the participants are not pre-registered in Flywheel, but rather that the studies check Flywheel after the scan completes to make sure there was no typo at the scanner. **No personally identifiable information can exist on the Flywheel platform (see MOU)**. In short, this means study teams must retain the key to their *Coded* data in a secure location outside Flywheel such as REDCap or on paper. Please consult the University of Colorado Institutional Review Board (IRB) regarding appropriate steps that must be taken to secure *Coded* and Personally Identifiable Information for human subject research.

Study B has enrolled Snow White into their study. This participant has already participated in another study conducted in the same laboratory. This study is cross-sectional with a single cohort, and therefore the study does not want to include a session flag.

    :Incorrect: StudyB/102/ or StudyB/102

        We have arbitrarily assigned the participant a subject-id 102, no link is required to the prior study **BUT** we are missing a required session label!

Flywheel naming convention is rigid and requires Project, Subject, **and** Session label to  ingest and route the data to the correct location.

    :Correct: StudyB/102/S1

        While this example study has only one session, we must enter all three labels: project, subject, and session every time!

.. note::
    *What happens if this naming goes wrong?* If a flywheel session was incorrectly named, all acquisitions associated with that session will be stored in an "Unsorted" project. This project is unique to each Principal Investigator (Flywheel "Group"). Study teams should take great care to ensure any missing or incorrectly named scans are caught quickly! Once a study has identified an incorrectly labelled scan, they should contact INC personnel immediately who will correct the error.

What is Pre-Registration? and Why it Matters?
**********************************************
For current INC users, you are likely accustom to storing participant information and subject-ids in COINS. COINS uses pre-registration to check that images generated on the scanner "match" coded information already entered into the COINS database. With this protocol, INC staff could immediately identify and flag scanning sessions with incorrectly entered participant codes. Flywheel provides a more streamlined approach that does not necessitate pre-registration. The bottom line here: in Flywheel, INC staff can no longer play any role in the confirmation that participant information was entered correctly at the scanner.

.. warning::
    Users should check all scans entering Flywheel **immediately** after the scan session is complete. Closely inspect that all participant information is correct and matches the information stored in your participant key outside Flywheel!

I Started my Study in COINS, What Happens Now?
**********************************************
All studies who wish to continue pre-registering and importing your data into COINS have the option to do so. All studies opting to continue using COINS will also have all new acquisitions stored in Flywheel. All scanner fields necessary for COINS convention are compatible with Flywheel convention. The one notable exception: while COINS has no restrictions on the value entered into "Accession Number", this field **MUST** conform to the Flywheel naming convention to comply with both COINS and Flywheel requirements.

What Information Can I Include in Flywheel?
*******************************************
INC at University of Colorado supports an "on premise" deployment of Flywheel.io. As all data and compute is conducted within UCB systems, we must conform to all data and privacy polices set forth by University of Colorado Research Computing (CURC) and Flywheel.io. As such, data must be de-identified before entering Flywheel. **NO** protected health information (PHI) and **NO** personally identifiable information (PII) may be stored in Flywheel. Examples of protected information includes:

 - first or last name
 - email address
 - phone number
 - mailing address
 - study enrollment or collection date (when paired with other identifying information)
 - detailed health history

Not sure if your data is correctly de-identified?  Please contact your IRB representative before placing any data in Flywheel!

Navigating The User Interface
=============================
Flywheel.io's user interface is a flexible powerful platform where users can do almost anything from creating and viewing data, to running analyses, and inviting collaborators to participate. The following provides a *brief* sample of the actions that can be taken within the Flywheel user interface. Please attend INC Courses on Using Flywheel to learn more!

Logging Into Flywheel
**********************
Flywheel uses CILogon service to manage access to their platform. CILogon is used by most academic institutions around the world to manage institutional accounts and therefore makes it very easy to add users, and log in with externally managed University credentials!

University of Colorado Users
++++++++++++++++++++++++++++++
    To logon as a UCB user, you need only a University of Colorado identikey. If you're not sure if you have one, contact INC staff.

    .. warning::
       Experiencing issues logging in? **Try changing browsers**. For more info visit our :ref:`faqs` page.


1. From your web browser, go to Flywheel `flywheel.rc.colorado.edu <https://flywheel.rc.colorado.edu>`_

2. Select University Credentials via CILogon

.. image:: imgs/getting_started/logging_in_1.png
   :alt: flywheel landing page

3. If this is your first time logging on, you will be redirected to the CILogon portal to select your organization.

    - Find University of Colorado Boulder
    - Check “Remember this Selection"
    - Click “Log on”

.. image:: imgs/getting_started/logging_in_2.png
   :alt: CILogon interface can be searched by institution

4. You will be directed to the CU Boulder logon page. Enter your identikey and password
5. You are now on the CU Boulder Flywheel Instance!

External Users
+++++++++++++++++
    Do you have an account with a University, ORCID, or another organization that uses the CILogon system? If you are not sure, you can check `here <https://cilogon.org/>`_.

    :I already have a CILogon Connected Account:

        Contact your collaborator at UCB with the appropriate credentials. Follow the instructions above to log in.

    :I do not have a CILogon Connected Account:
        Request a University of Colorado Boulder Affiliate Account through your UCB collaborator. These accounts will provide you access to the UCB systems for a period of one year, and usually can be generated within 5 business days.

The Flywheel Hierarchy
***********************
Before we get into how to navigate around the Flywheel interface, the following three sections are important building blocks to understand how Flywheel is designed. Understanding the Flywheel hierarchy, the back-end storage, and the container principle will help you navigate Flywheel and address your questions more readily.

A hierarchy is simply the system we rank or organize data according to a parent-child relationship. You might think of this as a folder on your computer that contains other folders and files. In this case the ‘parent’ folder has other ‘child’ sub-folders and files.

Flywheel uses a hierarchical data model to store data. In this way, data is automatically stored in an ordered way by principal investigator, study, subject, session, and acquisition. 

Object Based Storage Principles
********************************
We are not going to get into the weeds here… What is important is that Flywheel uses object based storage to store all raw and derived neuroimaging data. Object based storage is a type of data storage. Object based storage is generally more efficient and attaches a more information about how the data was created, modified, or used within the data structure itself. What does this mean for you? Neuroimaging storage on Flywheel takes up less disk space (its cheaper!) and contains a lot more information to search or retrieve data later. Interested in `learning more <https://www.ibm.com/cloud/blog/object-vs-file-vs-block-storage>`_?

What are Containers in Flywheel?
********************************
Containers are the data storage building blocks within Flywheel. Why does this matter? If you are thinking about retrieving data, running analyses, or even reviewing data already stored, you need to think about how to retrieve this data from a container. In layman's terms, a container could be thought of as a “folder” on your computer which can contain other “folders” or containers, as well as files or metadata. If you are unfamiliar with the concept of metadata, think of it as information about that folder, such as when it was created or modified, its name, etc.

In Flywheel containers are used to store “groups”, “projects”, “subjects”, “sessions”, “acquisitions”, and “analyses”. We get into the meaning of each of these containers below, but you can think of these containers as folders in Flywheel that bundle metadata and data together.

.. image:: imgs/getting_started/flywheel_architecture.png
   :alt: Basic Schematic describing flywheel architecture
   :width: 200pt

Image duplicated from docs.flywheel.io

Accessing My Groups
*********************
At INC, we use “Groups” to assign a principal investigator or laboratory. Here “Groups” can store multiple different projects or “studies”, have specific users and user permissions, and have administrative roles to add / edit / delete data and metadata for every container within. In Flywheel, you can identify Groups by the “tag” associated with any of your projects. As an Admin, you can also make changes to user permissions and projects within your “Group”. For more information on this topic, please refer to our documentation on ":ref:`User Permissions`".

Accessing My Projects
*********************
At INC, “Projects” are used to differentiate studies conducted within a Principal Investigator’s laboratory (ie, studies within a Flywheel "Group"). Users may be added to multiple projects, and once granted permission will be able to view the each project in Flywheel. All accessible projects may be viewed from the left hand ribbon on the projects page:

.. image:: imgs/getting_started/accessing_my_projects_1.png
   :alt: Flywheel projects view highlighting location of projects tab in left hand ribbon

In the second column of the project list you will find the parent Group for each project. “Projects” have several attributes including a description, project files, subjects, sessions, custom data views and more! Check out our upcoming tutorials to learn more about how to customize your project to meet your needs.

.. image:: imgs/getting_started/accessing_my_projects_2.png
   :alt: Flywheel projects view highlighting project attributes

Accessing My Subjects or Sessions
*********************************
If this is a new project, you may not see any subjects or sessions linked to your project. If you have already started scanning, or have uploaded historical/retrospective data from your project you should see each scan session in “sessions.”

.. note::
    *Still can't see your data?* Remember that pesky Accession Number? Well, if the first part of that string (ie the STUDY in STUDY/SUBJECT/SESSION) wasn't entered correctly at the scanner, your data doesn't know where to land on Flywheel. Not to worry, your data will be sitting in a project called Unsorted. If you can't see this project, contact INC staff or your lab admin of Flywheel who can add you to the Unsorted Project. From there, you can move that subject to the correct Project.

“Subjects” are used to bundle sessions collected on the same participant across multiple days or “sessions”. We identify subjects using a single Subject ID. This ID should be unique to the participant in the current study. If this ID needs to be “coded” with a reference to any personal identifiable information (PII), that PII **MUST** be stored outside Flywheel in a database such as COINS or REDCap. If you have questions about storing participant information, please contact INC!

From a project within Flywheel, the easiest way to access subjects and sessions is from the “Sessions” panel shown here:

.. image:: imgs/getting_started/accessing_subjects_and_sessions_1.png
   :alt: Flywheel projects view highlighting sessions attribute

Within the sessions panel, you may notice the sessions are sorted by date of collection, and show a summary of the Subject ID and Session ID for that set of acquisitions. To view the same data in “Subject view” you need to select the Subjects’ icon shown here:

.. image:: imgs/getting_started/accessing_subjects_and_sessions_2.png
   :alt: Flywheel projects view highlighting subjects panel

Accessing My Acquisitions and Files
***********************************
Finally, acquisitions are Flywheel containers within a session, and hold any files and metadata associated with a scanner sequence. For example, an acquisition may contain a set of dicoms, the nifti converted file for the same image, and task or behavioral data. As you may recall from earlier, these “containers” in layman's terms are just like folders or directories that hold relevant files. In Flywheel, we can see acquisitions and files within the project view, as shown below:

.. image:: imgs/getting_started/accessing_subjects_and_sessions_3.png
   :alt: Flywheel projects view highlighting acquisitions and file attributes

.. note::
    It's easy to confuse Acquisitions for Files because of how we use the term colloquially at the scanner. But don't be fooled, Acquisitions are not Files in Flywheel, they're still containers. In other words, an Acquisition's metadata (the information tab) will be different than the File's metadata.


Accessing My Analyses and Provenance
*************************************

Analyses are Flywheel containers that can be attached to a :code:`project`, :code:`subject`, :code:`session`, or :code:`acqusition`. For the purpose of exploring the user interface, we will focus on :code:`Session` level analyses. In the session view within Flywheel, all analyses are visible from the "Analysis" tab as shown below.

.. image:: imgs/getting_started/session_view_analysis_panel.png
   :alt: Flywheel session view highlighting session's analyses.

Analyses are stored in order from most recent to oldest. Analysis labels may be changed, and analyses may be deleted using the options menu at the right hand side of each analysis object.

Provenance is discussed more in the :ref:`Provenance` section. As an introduction, its good to be familiar with the provenance tab. You can review a history of all analyses run on your data in this tab, as well as view analysis logs and cancel or re-run analysis gears.

.. image:: imgs/getting_started/session_view_provenance_panel.png
   :alt: Flywheel session view highlighting session's provenance.

What to learn more about how to run gears in flywheel? visit ":ref:`Gears`" Basics. Also check out our documentation on running commonly used gears at INC in ":ref:`Running Commonly Used Gears`"

Collections
***********
Collections in Flywheel allow users to curate data from a range of projects or based on specific criteria. For example the ‘Radiologist Review’ collection will be used at UCB to curate images requiring incidental finding reviews for a radiologist. Further, collections can have a separate set of users and permissions in order to share specific sessions with users outside your study team. This feature can be found by clicking the collections view as seen here:

.. image:: imgs/getting_started/collections_1.png
   :alt: Flywheel collections panel.


Data Views and Project Reports
*******************************
Data Views and Project Reports can be used to compile metadata from any project. Data Views provide the most flexibility to generate tabular views of any metadata within flywheel such as age, race, sex, acquisition info, and more. These views can be shared or exported for 3rd party statistical packages.

Project Reports provide a summary of all sessions collected over a specific time range. Basic descriptive statistics are computed on all demographic information described in each session.

.. image:: imgs/getting_started/project_reports_1.png
   :alt: Flywheel project reports view.

Usage Reports
*******************
Usage Reports outline overall computing metrics for each project. Basic metrics include disk usage and number of gears (or Analyses) run.

.. image:: imgs/getting_started/usage_reports_1.png
   :alt: Flywheel project reports view.


How To Cite Us
==============
Using INC resources to collect or analyze neuroimaging data? Please cite us using the center's research resource identifier (RRID): `SCR_025079 <https://coremarketplace.org/?FacilityID=2661>`_.

This on-premise Flywheel platform is made possible by the hard work of many groups. Please cite us (Intermountain Neuroimaging Consortium) and the following collaborators if this platform has helped you produce your publication.
Collaborators:

* CU Boulder Research Computing (on top of who's platform we have deployed Flywheel)
* Flywheel.io (without whose continued support, this would not be possible)

Contact Us
***********
Interesting in getting started? Contact us `here <https://www.colorado.edu/mri/contact-us>`_ to request a copy of INC's Memorandum of Use and to set up a one on one consultation.

That’s it folks! Tune in for more information and tutorial regarding Flywheel at UCB!

.. sectionauthor:: Amy Hegarty <amy.hegarty@colorado.edu>