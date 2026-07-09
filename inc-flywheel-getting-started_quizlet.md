<!--
author:   Intermountain Neuroimaging Consortium
email:    amy.hegarty@colorado.edu
version:  1.0.0
language: en
narrator: US English Female

comment:  A shortened interactive training course covering INC Flywheel
          Getting Started — Overview, At the Scanner, Navigating the UI,
          and How to Cite Us. Course completion is tracked locally in the
          browser (sessionStorage) as the user progresses, and confirmed
          via a pre-filled email prompt at the end of the course.

logo:     https://www.colorado.edu/mri/sites/default/files/styles/large/public/page/INC_logo.png
-->

# INC Flywheel — Getting Started Training

Welcome to the **Intermountain Neuroimaging Consortium (INC) Flywheel** onboarding course.

This short training covers everything you need to know to get started using the Flywheel platform at INC — from setting up your study to scanning your first participant and finding your data.

> **📖 Full documentation:** This course is a quick summary. For the complete reference, visit [inc-documentation.readthedocs.io](https://inc-documentation.readthedocs.io/en/latest/).

> **⏱ Estimated time:** 10–15 minutes
>
> **📋 Modules:**
>
> 1. Overview — What is Flywheel? How is it deployed at INC?
> 2. Getting your MRI Data
> 3. Navigating the User Interface
> 4. How to Cite Us
>
> Your progress is tracked locally as you go. At the end, you'll be prompted to send a completion confirmation email. DO NOT FORGET this step - otherwise you will not be added to the platform.

---

## Before You Begin

Please enter your **CU Boulder IdentiKey** below. This is used to associate your quiz responses with your account in our training records.

> **ℹ️ What is an IdentiKey?** Your IdentiKey is your CU Boulder username... the part before `@colorado.edu` in your university email address (e.g. `jodo1234`). Don't have an identikey? Contact INC staff to request one.

[[IdentiKey username]]

<script>
const key = "@input".trim().toLowerCase();
if (key.length > 0) {
  sessionStorage.setItem("lia_identitykey", key);
}
// Always pass — this is a collection field, not a graded question
true;
</script>

> **✅ Once you've entered your IdentiKey above and pressed check, scroll down to begin the training.**

---

## 1. Overview — What is Flywheel? How is Flywheel Deployed at INC?

**Flywheel.io** is an imaging data management platform used to receive, curate, manage, and analyze neuroimaging data. INC hosts a **cloud deployment** of Flywheel.io: your imaging data and metadata are stored on **AWS cloud infrastructure (S3)**, while data analysis and computation run on **CU Boulder Research Computing's (CURC)** on-premise HPC clusters, **Blanca** and **Alpine**, backed by **PetaLibrary** storage.

![Flywheel computing architecture at CU Boulder](https://inc-documentation.readthedocs.io/en/latest/_images/facilities_data_analysis.jpg)

> **Note:** Before starting a new or existing study in Flywheel, you must set up a meeting with INC Staff to discuss your specific needs and obtain a copy of INC's **Memorandum of Use (MOU)**.

### Why use Flywheel?

Flywheel is built to **organize**, **store**, and **share** research and medical imaging data:

- **Organize**: a consistent `Group → Project → Subject → Session → Acquisition` hierarchy, with structured metadata captured automatically at every level.
- **Store**: secure, versioned, automatically backed-up storage with full provenance: every action taken on your data is logged (who, what, when, how).
- **Share**: fine-grained user permissions, Collections, and Data Views make it easy to collaborate and to meet NIH/NSF data-sharing requirements, including submission to the NDA.

### Key things to know

- INC hosts a **3T Prisma Fit MR scanner** whose data flows directly into Flywheel.
- Flywheel does **not** require pre-registration of participants before scanning — INC recommends checking Flywheel *after* the scan session to catch any typos.
- **No personally identifiable information (PII)** may ever exist on the Flywheel platform. Subject IDs must be coded, and the key to that coding must be stored outside Flywheel (e.g. in REDCap or on paper).

---

### 🧠 Check Your Understanding — Overview

**Q1:** Where is INC's Flywheel imaging data stored?

[( )] On the researcher's local workstation
[(X)] On AWS cloud infrastructure (S3)
[( )] Directly on the MRI scanner console
[( )] On a personal Google Drive or Dropbox account

<script>
const correct = @input === 1;

// Record locally — rolled into the completion email sent at the end of the course
const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "1 - Overview";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q2:** Does Flywheel require you to pre-register participants before a scan session?

[( )] Yes — participants must be registered before scanning begins
[(X)] No — INC recommends checking Flywheel *after* the scan to catch any typos
[( )] Yes — but only for longitudinal studies
[( )] Only for new participants, not returning ones

<script>
const correct = @input === 1;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "1 - Overview";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q3:** True or False: The key linking coded Subject IDs to personally identifiable information (PII) **may** be stored somewhere within Flywheel.

[[?]] Re-read "Key things to know" above — where must the key to coded participant data be stored?

[( )] True
[(X)] False

<script>
const correct = @input === 1;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "1 - Overview";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q4:** Which of the following is **NOT** one of Flywheel's core value propositions for managing imaging data?

[[?]] Three of these options are the "Organize / Store / Share" pillars from "Why use Flywheel?" above — one option describes something Flywheel does not do.

[( )] Organize — a consistent, searchable data hierarchy
[( )] Store — versioned, backed-up storage with full provenance
[( )] Share — fine-grained permissions, Collections, and Data Views
[(X)] Compute — Flywheel replaces the need for any HPC or compute cluster

<script>
const correct = @input === 3;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "1 - Overview";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

## 2. At the Scanner

We use automated transfer protocols to send DICOM data collected on the MRI scanner to the Flywheel web instance. Here at INC, we encode the **landing spot** for the DICOM data within two of the DICOM's header fields: `refering physician` and `accession number`. The MRI technician running your scan can help answer questions about how to set these fields to ensure the scanning session's data ends up in the right spot.

Here are a few things to keep in mind:

- The `refering physician` refers to the principal investigator for the lab, and is typically set at the beginning of the study and not changed. 

- Getting the **Routing String** stored in the `accession number` field correct at the scanner is the **most critical step** in getting your data into Flywheel correctly. If this is entered incorrectly, your data will not land in the right project.

### The Routing String Naming Convention

When your participant is set up on the scanner console, you **must** enter the following **Routing Sring** into the field labelled `accession number`:

```
<project-label> / <subject-label> / <session-label>
```

For example, for a study called `MyStudy`, participant `sub-101`, session `ses-01`:

```
MyStudy / sub-101 / ses-01
```

> **💡 Tip:** INC strongly recommends using **BIDS-compliant** naming for subject and session labels (e.g. `sub-101`, `ses-01`).

### What if the naming goes wrong?

If the `refering physician` or `accession number` is entered incorrectly, all acquisitions from that session will be placed in an **"Unknown"** or **"Unsorted (PI specific)" project**. Study teams must:

1. Check Flywheel promptly after each scan session
2. Contact INC staff immediately if a session is missing or misrouted
3. INC staff will correct the labelling error

### Additional scanner information

Beyond the `accession number`, a small amount of additional participant/session metadata is collected via the **Scanner Requisition Form**, which must be submitted before each scan session.

---

### 🧠 Check Your Understanding — At the Scanner

**Q5:** What is the correct format for the Accession Number field at the scanner console?

[( )] `<subject-label> / <session-label>`
[( )] `<group-label> / <project-label>`
[(X)] `<project-label> / <subject-label> / <session-label>`
[( )] `<session-label> / <subject-label> / <project-label>`

<script>
const correct = @input === 2;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "2 - At the Scanner";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q6:** Where does data go if the `accession number` is entered incorrectly?

[( )] It is automatically deleted after 24 hours
[( )] It is emailed to the PI
[(X)] It lands in an "Unsorted" project in the PI's Flywheel Group
[( )] It is renamed automatically to match Flywheel's naming convention

<script>
const correct = @input === 2;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "2 - At the Scanner";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q7:** What naming convention does INC recommend for subject and session labels?

[( )] Participant's initials followed by date of birth
[( )] Sequential numbers with no prefix (e.g. `001`, `002`)
[(X)] BIDS-compliant labels (e.g. `sub-101`, `ses-01`)
[( )] Free-form text with no restrictions

<script>
const correct = @input === 2;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "2 - At the Scanner";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q8:** True or False: The Scanner Requisition Form must be submitted before each scan session.

[(X)] True
[( )] False

<script>
const correct = @input === 0;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "2 - At the Scanner";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

## 3. Navigating the User Interface

Once logged into Flywheel, you will see the **Projects page** — your primary hub for navigating your data.

### Logging Into Flywheel

Flywheel uses **CILogon** to manage access — the same federated-login system used by most academic institutions. CU Boulder users log in with their **University of Colorado credentials** (IdentiKey); external collaborators can log in with an existing CILogon-connected account (e.g. from their home institution or ORCID), or request a CU Boulder Affiliate Account through their UCB collaborator.

![Flywheel landing page](https://inc-documentation.readthedocs.io/en/latest/_images/logging_in_1.png)

> **💡 Tip:** Having trouble logging in? Try changing browsers.

### The Flywheel Data Hierarchy

Flywheel organizes data into a strict hierarchy:

```
Group  →  Project  →  Subject  →  Session  →  Acquisition
```

| Level | Description |
|---|---|
| **Group** | The top-level container, typically corresponding to a PI or lab. Visible in the second column of the Projects list. |
| **Project** | A single study or dataset. Contains subjects, sessions, files, and metadata. |
| **Subject** | Bundles all sessions for one participant. Identified by a unique Subject ID. |
| **Session** | One visit/scan day for a participant. |
| **Acquisition** | A single scanner sequence within a session. Holds files and metadata. |

![Basic schematic describing Flywheel architecture](https://inc-documentation.readthedocs.io/en/latest/_images/flywheel_architecture.png)

### Navigating Projects

All accessible projects appear in the **left-hand ribbon** on the Projects page. Key features of a Project include:

- Description
- Project files
- Subjects and sessions list
- Custom data views
- Metadata

> **⚠️ Can't see your data?** If a session is missing from your project, the most likely cause is an incorrectly entered Accession Number at the scanner — causing data to land in the "Unsorted" project instead.

### Viewing Sessions and Subjects

From within a project, the **Sessions panel** lists all scan sessions sorted by date, with a summary of Subject ID and Session ID.

To switch to a subject-centric view, select the **Subjects icon** within the project.

### Collections and Data Views

**Collections** let you curate and share a subset of sessions across projects — for example, a "Radiologist Review" collection — without duplicating data or granting broader access than intended. **Data Views** let you extract and export metadata (age, sex, acquisition info, and more) across a project for statistical analysis or reporting.

![Flywheel collections panel](https://inc-documentation.readthedocs.io/en/latest/_images/collections_1.png)

---

### 🧠 Check Your Understanding — Navigating the UI

**Q9:** What is the correct order of the Flywheel data hierarchy?

[[?]] Start from the broadest container (a PI or lab) and work down to the narrowest (a single scanner sequence).

[( )] Project → Group → Subject → Acquisition → Session
[( )] Subject → Session → Project → Group → Acquisition
[(X)] Group → Project → Subject → Session → Acquisition
[( )] Group → Subject → Project → Acquisition → Session

<script>
const correct = @input === 2;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "3 - Navigating UI";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q10:** Where can you view all of your accessible projects in Flywheel?

[( )] In the top navigation menu bar
[(X)] In the left-hand ribbon on the Projects page
[( )] In a dropdown under your user profile
[( )] In the Admin settings panel

<script>
const correct = @input === 1;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "3 - Navigating UI";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q11:** What is an "Acquisition" in Flywheel?

[( )] A group of projects belonging to one PI
[( )] A participant's full set of visits across all sessions
[(X)] A single scanner sequence within a session, holding files and metadata
[( )] A metadata tag applied to a project

<script>
const correct = @input === 2;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "3 - Navigating UI";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q12:** If you cannot see data in your project, what is the most likely cause?

[[?]] Think back to what has to be typed correctly at the scanner console for data to land in the right project.

[[Accession Number]]

<script>
const ans = "@input".toLowerCase().trim();
const correct = ans.includes("accession");

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "3 - Navigating UI";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q13:** How do CU Boulder users log into Flywheel?

[( )] With a separate Flywheel-specific username and password
[(X)] With their University of Colorado credentials via CILogon
[( )] By requesting a one-time access code from INC staff
[( )] Flywheel does not require login for CU Boulder users

<script>
const correct = @input === 1;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "3 - Navigating UI";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

## 4. How to Cite Us

If INC's Flywheel platform has contributed to your publication, you are required to acknowledge the consortium and its collaborators.

### Citation Requirements

**Cite INC using its Research Resource Identifier (RRID):**

> Intermountain Neuroimaging Consortium, RRID: **SCR_025079**

**Also acknowledge the following collaborators:**

- **CU Boulder Research Computing (CURC)** — the infrastructure on which Flywheel is deployed
- **Flywheel.io** — without whose continued support this platform would not be possible

> **📬 Getting started?** Contact INC to request a copy of the Memorandum of Use and set up a one-on-one consultation.

---

### 🧠 Check Your Understanding — How to Cite Us

**Q14:** What identifier should you use to cite INC in a publication?

[( )] A DOI assigned per study
[( )] The PI's ORCID number
[(X)] INC's Research Resource Identifier (RRID): SCR_025079
[( )] A URL to the INC website

<script>
const correct = @input === 2;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "4 - How to Cite";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q15:** Which TWO collaborators must also be acknowledged alongside INC? Select all that apply.

[[?]] Select exactly two — check the "Also acknowledge the following collaborators" list above.

[[X]] CU Boulder Research Computing (CURC)
[[X]] Flywheel.io
[[ ]] Amazon Web Services
[[ ]] CU Anschutz Medical Campus

<script>
// @input is substituted as a JS array literal, e.g. [1, 1, 0, 0]
const sel = @input;
const correct = sel[0] === 1 && sel[1] === 1 && sel[2] === 0 && sel[3] === 0;

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "4 - How to Cite";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

**Q16:** What is INC's RRID number?

[[SCR_025079]]

<script>
const ans = "@input".trim().replace(/\s/g, "");
const correct = ans.toUpperCase().includes("SCR_025079");

const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");
const module = "4 - How to Cite";
if (!progress[module]) progress[module] = { correct: 0, total: 0 };
progress[module].total += 1;
if (correct) progress[module].correct += 1;
sessionStorage.setItem("lia_progress", JSON.stringify(progress));

correct;
</script>

---

## 🧠 Bonus: Brain Souvenirs

As a thank-you for participating in research, INC generates **"brain souvenir"** images for study participants.

### Electronic Souvenirs

Electronic brain souvenirs are generated **automatically for all study participants** — no gear needs to be manually launched. Lab staff should access and download the souvenir from the **list of session analyses** for that participant's session.

![Example electronic brain souvenir — sagittal MRI slice](https://inc-documentation.readthedocs.io/en/latest/_images/brain_souvenir_example.jpg)

> **📤 Sharing with participants:** Flywheel does not email or share the souvenir on your behalf. Communicate with the participant **directly** about how you'll share their electronic souvenir with them — check with your IRB coordinator about appropriate sharing methods.

### 3D Printed Souvenirs

Looking for something more lasting? INC also offers **3D printed brain souvenirs**, which can be picked up within **2 weeks** of the scan.

> **📝 Requesting a 3D print:** Interest in a 3D printed souvenir should be noted on the **Scanner Requisition Form** at the time of scheduling.

---

## 🎓 Training Complete!

Congratulations — you've completed the **INC Flywheel Getting Started** training!

### What you've learned

- ✅ What INC Flywheel is, how it's deployed (AWS cloud storage + CURC on-premise compute), and why it's valuable for organizing, storing, and sharing imaging data
- ✅ How to correctly enter the Accession Number at the scanner
- ✅ How to log into Flywheel and the Flywheel data hierarchy: Group → Project → Subject → Session → Acquisition
- ✅ How to navigate the Flywheel user interface, including Collections and Data Views
- ✅ How to cite INC in your publications (RRID: SCR_025079)

---

### 📧 Confirm Your Completion

Course completion is confirmed by email, not an automatic submission. Type **send** in the box below and press **Check** — this opens a pre-filled email in your default mail client, addressed to INC, with your IdentiKey and training summary already populated in the subject and body. Review it and hit **Send** in your mail client to complete the training.

> **ℹ️ Missing your IdentiKey?** If you skipped the "Before You Begin" step, scroll back to the top and enter it there first — it's read from the same session storage used to build this email.

[[send]]

<script>
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const progress = JSON.parse(sessionStorage.getItem("lia_progress") || "{}");

let totalCorrect = 0;
let totalQuestions = 0;
let summaryLines = "";
for (const [module, stats] of Object.entries(progress)) {
  totalCorrect += stats.correct;
  totalQuestions += stats.total;
  summaryLines += `- ${module}: ${stats.correct}/${stats.total}\n`;
}

const completedOn = new Date().toLocaleString();

const subject = `INC Flywheel Training Completed - ${identityKey}`;
const body =
`INC Flywheel Getting Started training - completion confirmation

IdentiKey:      ${identityKey}
Completed on:   ${completedOn}
Overall score:  ${totalCorrect} / ${totalQuestions}

Module breakdown:
${summaryLines}
This email confirms I have completed the INC Flywheel Getting Started training.`;

const mailtoLink = "mailto:inc@colorado.edu"
  + "?subject=" + encodeURIComponent(subject)
  + "&body=" + encodeURIComponent(body);

window.location.href = mailtoLink;

true;
</script>

---

### Next steps

- 📅 **Schedule a consultation** with INC staff before starting your study
- 📋 **Complete the Scanner Requisition Form** before each scan session
- 📖 **Explore the full documentation** at [inc-documentation.readthedocs.io](https://inc-documentation.readthedocs.io/en/latest/)
- ❓ **Questions?** Visit the [INC FAQs page](https://inc-documentation.readthedocs.io/en/latest/faqs.html)
