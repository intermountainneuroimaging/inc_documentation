<!--
author:      Quiz Tracker Demo
version:     1.0.0
comment:     Track quiz states and report on the final screen.
-->

# Quiz Tracking Example

Welcome to the quiz. Your answers will be tracked and summarized on the last slide.

---

## Question 1: Science

What is the chemical symbol for water?

[( )] CO2
[( )] O2
[[X]] H2O
[( )] NaCl

---

## Question 2: Geography

Which country is famous for the Eiffel Tower?

[[ ]] Germany
[[X]] France
[[ ]] Italy
[[ ]] Spain

---

## Question 3: Text Input

Type the lowercase word for a young cat:

[[kitten]]

---

## Final Results Report

Here is your performance summary for this session:

<script>
// LiaScript stores the state of all interactive elements in `window.LIA.state`
// We extract the tracking data for quizzes and text inputs
let trackingData = window.LIA.state;
let totalQuestions = 3;
let correctCount = 0;

// Check Question 1 & 2 (Multiple choice and single choice share a quiz structure)
// We look into the internal LiaScript vectors for solved states
if (trackingData && trackingData.quiz) {
  // Question 1 check (vector index 0)
  if (trackingData.quiz[0] && trackingData.quiz[0].solved === 1) correctCount++;
  // Question 2 check (vector index 1)
  if (trackingData.quiz[1] && trackingData.quiz[1].solved === 1) correctCount++;
}

// Check Question 3 (Text input/generic inputs are stored separately)
if (trackingData && trackingData.inputs) {
  // Question 3 check (vector index 0 for inputs)
  if (trackingData.inputs[0] && trackingData.inputs[0].solved === 1) correctCount++;
}

// Calculate the final percentage
let percentage = ((correctCount / totalQuestions) * 100).toFixed(0);

// Output the results dynamically to the LiaScript markdown screen
`### Your Score: ${correctCount} / ${totalQuestions} (${percentage}%)

${percentage >= 60 ? "**Status:** 🎉 Passed!" : "**Status:** ❌ Failed. Please try again."}`;
</script>
