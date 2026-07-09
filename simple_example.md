<!--
author:   Intermountain Neuroimaging Consortium
email:    amy.hegarty@colorado.edu
version:  0.1.0
comment:  Minimal test course used to isolate what actually works before
          layering on the real INC Flywheel content. Two natively-graded
          quiz questions (no scripts attached to any quiz - that pattern
          has repeatedly broken in testing), plus a completion form built
          from plain HTML/JS that reads the DOM directly instead of going
          through LiaScript's @input substitution.
-->

# Minimal Test Course

This is a stripped-down test course. The goal is to confirm two things work in isolation before adding real content:

1. Two ordinary quiz questions, graded natively by LiaScript (no custom scripting).
2. A completion form that opens a pre-filled email via a real button click.

---

## Question 1

What is 2 + 2?

[( )] 3
[(X)] 4
[( )] 5

---

## Question 2

Which of these is a primary color?

[( )] Green
[(X)] Blue
[( )] Purple

---

## Final Assessment

Please enter your email and click the button to submit your final course report.

<form id="course-completion-form">
  <input type="email" id="user-email" placeholder="Enter your email" required>
  <button type="button" onclick="sendCompletionEmail()">Submit &amp; Notify</button>
</form>

<script>
function sendCompletionEmail() {
  var userEmail = document.getElementById("user-email").value;

  if (!userEmail) {
    alert("Please enter your email first.");
    return;
  }

  var subject = "Minimal Test Course Completed - " + userEmail;
  var body = "The user has completed the course.\n\nSubmitted email: " + userEmail;

  var mailtoLink = "mailto:amy.hegarty@colorado.edu"
    + "?subject=" + encodeURIComponent(subject)
    + "&body=" + encodeURIComponent(body);

  window.location.href = mailtoLink;
}
</script>
