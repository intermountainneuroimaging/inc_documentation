.. _at_the_scanner:

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

Study B has enrolled Snow White into their study. This participant has already participated in another study conducted in the same laboratory. This study is cross-sectional with a single cohort, and therefore the study does not want to include a session flag.

    :Incorrect: StudyB/102/ or StudyB/102

        We have arbitrarily assigned the participant a subject-id 102, no link is required to the prior study **BUT** we are missing a required session label!

Flywheel naming convention is rigid and requires Project, Subject, **and** Session label to  ingest and route the data to the correct location.

    :Correct: StudyB/102/S1

        While this example study has only one session, we must enter all three labels: project, subject, and session every time!

.. note::
    *What happens if this naming goes wrong?* If a Flywheel session was incorrectly named, all acquisitions associated with that session will be stored in an "Unsorted" project. This project is unique to each Principal Investigator (Flywheel "Group"). Study teams should take great care to ensure any missing or incorrectly named scans are caught quickly! Once a study has identified an incorrectly labelled scan, they should contact INC personnel immediately who will correct the error.

We highly recommend that lab staff checks the Flywheel data repository after every scan session to make sure there was no typo at the scanner.

**No personally identifiable information can exist on the Flywheel platform (see MOU)**. Study teams must retain the key to their *Coded* data in a secure location outside Flywheel such as REDCap or on paper. Please consult the University of Colorado Institutional Review Board (IRB) regarding appropriate steps that must be taken to secure *Coded* and Personally Identifiable Information for human subject research.

.. warning::
    Users should check all scans entering Flywheel **immediately** after the scan session is complete. Closely inspect that all participant information is correct and matches the information stored in your participant key outside Flywheel!

I Started my Study in COINS, What Happens Now?
**********************************************
All studies who wish to continue pre-registering and importing your data into COINS have the option to do so. All studies opting to continue using COINS will also have all new acquisitions stored in Flywheel. All scanner fields necessary for COINS convention are compatible with Flywheel convention. The one notable exception: while COINS has no restrictions on the value entered into "Accession Number", this field **MUST** conform to the Flywheel naming convention to comply with both COINS and Flywheel requirements.

Information Prohibited from Flywheel.io
*******************************************
INC at University of Colorado supports a "cloud" deployment of Flywheel.io. All data are stored in AWS S3 data storage and subject to the data security agreements in place by University of Colorado and Flywheel.io (ref here). As such, data must be de-identified before entering Flywheel. **NO** protected health information (PHI) and **NO** personally identifiable information (PII) may be stored in Flywheel. Examples of protected information includes:

 - first or last name
 - email address
 - phone number
 - mailing address
 - study enrollment or collection date (when paired with other identifying information such as specific disease diagnoses)
 - detailed health history

Not sure if your data is correctly de-identified?  Please contact your IRB representative before placing any data in Flywheel!

.. sectionauthor:: Amy Hegarty <amy.hegarty@colorado.edu>
