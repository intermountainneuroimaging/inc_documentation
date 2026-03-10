<!--
author:   Intermountain Neuroimaging Consortium
email:    inc@colorado.edu
version:  1.0.0
language: en
narrator: US English Female

comment:  A shortened interactive training course covering INC Flywheel
          Getting Started — Overview, At the Scanner, Navigating the UI,
          and How to Cite Us. Quiz answers are submitted to a SharePoint
          List via Power Automate HTTP trigger.

logo:     https://www.colorado.edu/mri/sites/default/files/styles/large/public/page/INC_logo.png
-->

# INC Flywheel — Getting Started Training

Welcome to the **Intermountain Neuroimaging Consortium (INC) Flywheel** onboarding course.

This short training covers everything you need to know to get started using INC's on-premise Flywheel platform — from setting up your study to scanning your first participant and finding your data.

> **⏱ Estimated time:** 10–15 minutes
>
> **📋 Modules:**
>
> 1. Overview — What is INC Flywheel?
> 2. At the Scanner — Entering the Accession Number
> 3. Navigating the User Interface
> 4. How to Cite Us
>
> Your quiz responses are automatically saved as you go.

---

## Before You Begin

Please enter your **CU Boulder IdentiKey** below. This is used to associate your quiz responses with your account in our training records.

> **ℹ️ What is an IdentiKey?** Your IdentiKey is your CU Boulder username — the part before `@colorado.edu` in your university email address (e.g. `jodo1234`).

[[IdentiKey username]]

<!-- LiaScript text-quiz used as a plain input field.
     @input substitutes the raw string the user types.
     We store it in sessionStorage so every downstream quiz script
     can read it as identityKey without the user re-entering it.
     The script always returns true so the field is never marked wrong. -->
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

## 1. Overview — What is INC Flywheel?

**Flywheel.io** is an imaging data management platform used to receive, curate, manage, and analyze neuroimaging data. INC hosts an **"on-premise" deployment** of Flywheel, meaning all data storage and computation runs entirely on University of Colorado infrastructure — not on external cloud servers.

This setup connects your MRI acquisitions directly to analysis pipelines through CU Boulder Research Computing (CURC), including the **PetaLibrary** (data storage) and the **Blanca** high-performance compute cluster.

> **Note:** Before starting a new or existing study in Flywheel, you must set up a meeting with INC Staff to discuss your specific needs and obtain a copy of INC's **Memorandum of Use (MOU)**.

### Key things to know

- INC hosts a **3T Prisma Fit MR scanner** whose data flows directly into Flywheel.
- Flywheel replaces the older **COINS** system previously used at INC.
- Unlike COINS, Flywheel does **not** require pre-registration of participants before scanning.
- **No personally identifiable information (PII)** may ever exist on the Flywheel platform. Subject IDs must be coded, and the key to that coding must be stored outside Flywheel (e.g. in REDCap or on paper).

---

### 🧠 Quiz 1 — Overview

**Question 1.1:** Where is all data stored in INC's Flywheel deployment?

<!-- FIX: @input for single-choice returns a 0-based integer.
     Option index 1 (second option) is the correct answer. -->
[( )] On Flywheel.io's commercial cloud servers
[(X)] On University of Colorado infrastructure (CUmulus / CURC)
[( )] On the researcher's local workstation
[( )] On Amazon Web Services

<!-- FIX: Power Automate URL placeholder — replace before deploying.
     FIX: localStorage is not available in LiaScript's sandbox.
          Use a module-level script variable for session identity instead.
          The @uid macro is defined in the course header (see bottom of file).
     FIX: @input for single-choice is an integer, not a quoted string.
          Compare as integer: @input === 1  -->
<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const correct = @input === 1;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "1 - Overview",
    question: "Where is all data stored in INC's Flywheel deployment?",
    answer: correct ? "UColorado infrastructure (correct)" : "Incorrect option",
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 1.2:** Does Flywheel require you to pre-register participants before a scan session?

[( )] Yes — participants must be registered before scanning begins
[(X)] No — INC recommends checking Flywheel *after* the scan to catch any typos
[( )] Yes — but only for longitudinal studies
[( )] Only for new participants, not returning ones

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const correct = @input === 1;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "1 - Overview",
    question: "Does Flywheel require pre-registration of participants?",
    answer: correct ? "No, check after scan (correct)" : "Incorrect option",
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 1.3:** Where must the key to coded participant data be stored?

<!-- FIX: Text-quiz solution hint in double brackets is shown as placeholder
     length only — it is never revealed to the user. The <script> block
     handles all validation logic. -->
[[outside Flywheel]]

<!-- FIX: @input for a text quiz is a plain string — no quotes needed around
     the macro. Wrap in String() for safety before calling string methods. -->
<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const ans = "@input".toLowerCase().trim();
const correct = ans.includes("outside") || ans.includes("redcap");
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "1 - Overview",
    question: "Where must the key to coded participant data be stored?",
    answer: `"${ans}" — ${correct ? "correct" : "incorrect"}`,
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

## 2. At the Scanner

Getting the Accession Number right at the scanner is the **most critical step** in getting your data into Flywheel correctly. If this is entered incorrectly, your data will not land in the right project.

### The Accession Number Naming Convention

When your participant is set up on the scanner console, you **must** enter the following into the field labelled **Accession Number**:

```
<project-label> / <subject-label> / <session-label>
```

For example, for a study called `MyStudy`, participant `sub-101`, session `ses-01`:

```
MyStudy / sub-101 / ses-01
```

> **💡 Tip:** INC strongly recommends using **BIDS-compliant** naming for subject and session labels (e.g. `sub-101`, `ses-01`).

### What if the naming goes wrong?

If the Accession Number is entered incorrectly, all acquisitions from that session will be placed in an **"Unsorted" project** — a holding area unique to each PI's Flywheel Group. Study teams must:

1. Check Flywheel promptly after each scan session
2. Contact INC staff immediately if a session is missing or misrouted
3. INC staff will correct the labelling error

### Additional scanner information

Beyond the Accession Number, a small amount of additional participant/session metadata is collected via the **Scanner Requisition Form**, which must be submitted before each scan session.

---

### 🧠 Quiz 2 — At the Scanner

**Question 2.1:** What is the correct format for the Accession Number field at the scanner console?

[( )] `<subject-label> / <session-label>`
[( )] `<group-label> / <project-label>`
[(X)] `<project-label> / <subject-label> / <session-label>`
[( )] `<session-label> / <subject-label> / <project-label>`

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const correct = @input === 2;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "2 - At the Scanner",
    question: "Correct format for Accession Number field",
    answer: correct ? "project/subject/session (correct)" : "Incorrect option",
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 2.2:** Where does data go if the Accession Number is entered incorrectly?

[( )] It is automatically deleted after 24 hours
[( )] It is emailed to the PI
[(X)] It lands in an "Unsorted" project in the PI's Flywheel Group
[( )] It is held in a COINS database

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const correct = @input === 2;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "2 - At the Scanner",
    question: "Where does data go if Accession Number is wrong?",
    answer: correct ? "Unsorted project (correct)" : "Incorrect option",
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 2.3:** What naming convention does INC recommend for subject and session labels?

[( )] Participant's initials followed by date of birth
[( )] Sequential numbers with no prefix (e.g. `001`, `002`)
[(X)] BIDS-compliant labels (e.g. `sub-101`, `ses-01`)
[( )] Free-form text with no restrictions

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const correct = @input === 2;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "2 - At the Scanner",
    question: "What naming convention does INC recommend?",
    answer: correct ? "BIDS-compliant (correct)" : "Incorrect option",
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 2.4:** What form must be submitted before each scan session?

[[Scanner Requisition Form]]

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const ans = "@input".toLowerCase().trim();
const correct = ans.includes("requisition");
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "2 - At the Scanner",
    question: "What form must be submitted before each scan session?",
    answer: `"${ans}" — ${correct ? "correct" : "incorrect"}`,
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

## 3. Navigating the User Interface

Once logged into Flywheel, you will see the **Projects page** — your primary hub for navigating your data.

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

---

### 🧠 Quiz 3 — Navigating the UI

**Question 3.1:** What is the correct order of the Flywheel data hierarchy?

[( )] Project → Group → Subject → Acquisition → Session
[( )] Subject → Session → Project → Group → Acquisition
[(X)] Group → Project → Subject → Session → Acquisition
[( )] Group → Subject → Project → Acquisition → Session

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const correct = @input === 2;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "3 - Navigating UI",
    question: "Correct Flywheel data hierarchy order",
    answer: correct ? "Group→Project→Subject→Session→Acquisition (correct)" : "Incorrect option",
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 3.2:** Where can you view all of your accessible projects in Flywheel?

[( )] In the top navigation menu bar
[(X)] In the left-hand ribbon on the Projects page
[( )] In a dropdown under your user profile
[( )] In the Admin settings panel

<!-- FIX: Correct option is index 1 (second item, 0-based). Original script
     had @input === "1" as a string — now corrected to integer comparison. -->
<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const correct = @input === 1;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "3 - Navigating UI",
    question: "Where can you view all accessible projects?",
    answer: correct ? "Left-hand ribbon (correct)" : "Incorrect option",
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 3.3:** What is an "Acquisition" in Flywheel?

[( )] A group of projects belonging to one PI
[( )] A participant's full set of visits across all sessions
[(X)] A single scanner sequence within a session, holding files and metadata
[( )] A metadata tag applied to a project

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const correct = @input === 2;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "3 - Navigating UI",
    question: "What is an Acquisition in Flywheel?",
    answer: correct ? "Single scanner sequence (correct)" : "Incorrect option",
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 3.4:** If you cannot see data in your project, what is the most likely cause?

[[Accession Number]]

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const ans = "@input".toLowerCase().trim();
const correct = ans.includes("accession");
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "3 - Navigating UI",
    question: "If you can't see data in your project, what is the most likely cause?",
    answer: `"${ans}" — ${correct ? "correct" : "incorrect"}`,
    score: correct ? 1 : 0
  })
}).catch(() => {});
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

### 🧠 Quiz 4 — How to Cite Us

**Question 4.1:** What identifier should you use to cite INC in a publication?

[( )] A DOI assigned per study
[( )] The PI's ORCID number
[(X)] INC's Research Resource Identifier (RRID): SCR_025079
[( )] A URL to the INC website

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const correct = @input === 2;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "4 - How to Cite",
    question: "What identifier should you use to cite INC?",
    answer: correct ? "RRID SCR_025079 (correct)" : "Incorrect option",
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 4.2:** Which TWO collaborators must also be acknowledged alongside INC? Select all that apply.

<!-- FIX: Checkbox options must use uppercase X — [[x]] is invalid syntax.
     FIX: @input for multiple-choice returns an ARRAY of integers
          (0 = unchecked, 1 = checked), NOT a comma-separated index string.
          Correct logic: both index 0 and index 1 must be 1, others must be 0. -->
[[X]] CU Boulder Research Computing (CURC)
[[X]] Flywheel.io
[[ ]] Amazon Web Services
[[ ]] CU Anschutz Medical Campus

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
// @input is substituted as a JS array literal, e.g. [1, 1, 0, 0]
const sel = @input;
const correct = sel[0] === 1 && sel[1] === 1 && sel[2] === 0 && sel[3] === 0;
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "4 - How to Cite",
    question: "Which collaborators must be acknowledged?",
    answer: `selected: [${sel}] — ${correct ? "correct" : "incorrect"}`,
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

**Question 4.3:** What is INC's RRID number?

[[SCR_025079]]

<script>
const SHEET_URL = "https://default3ded8b1b070d462982e4c0b019f460.57.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8836ac9cd8b94c34954b57393aa9e84d/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=yRogStaTOJ7jLX3hOuhktEjsUoIFQxk_2KiBxd7WYXE";
const identityKey = sessionStorage.getItem("lia_identitykey") || "unknown";
const ans = "@input".trim().replace(/\s/g, "");
const correct = ans.toUpperCase().includes("SCR_025079");
fetch(SHEET_URL, {
  method: "POST",
  mode: "no-cors",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    identitykey: identityKey,
    module: "4 - How to Cite",
    question: "What is INC's RRID number?",
    answer: `"${ans}" — ${correct ? "correct" : "incorrect"}`,
    score: correct ? 1 : 0
  })
}).catch(() => {});
correct;
</script>

---

## 🎓 Training Complete!

Congratulations — you've completed the **INC Flywheel Getting Started** training!

### What you've learned

- ✅ What INC Flywheel is and how it differs from COINS
- ✅ How to correctly enter the Accession Number at the scanner
- ✅ The Flywheel data hierarchy: Group → Project → Subject → Session → Acquisition
- ✅ How to navigate the Flywheel user interface
- ✅ How to cite INC in your publications (RRID: SCR_025079)

---

### Next steps

- 📅 **Schedule a consultation** with INC staff before starting your study
- 📋 **Complete the Scanner Requisition Form** before each scan session
- 📖 **Explore the full documentation** at [inc-documentation.readthedocs.io](https://inc-documentation.readthedocs.io/en/latest/)
- ❓ **Questions?** Visit the [INC FAQs page](https://inc-documentation.readthedocs.io/en/latest/faqs.html)
