<!--
author:      Quiz Tracker Demo
version:     1.0.0
comment:     Track quiz states dynamically using reactive bindings.
-->

# Quiz Tracking Example

Welcome to the quiz. Your answers will be tracked and summarized on the last slide.

---

## Question 1: Science

What is the chemical symbol for water?

<!-- We bind this quiz to an ID or read it via macro -->
[(X)] H2O
[( )] CO2
[( )] O2
[( )] NaCl

---

## Question 2: Geography

Which country is famous for the Eiffel Tower?

[( )] Germany
[(X)] France
[( )] Italy
[( )] Spain

---

## Question 3: Text Input

Type the lowercase word for a young cat:

[[kitten]]

---

## Final Results Report

Here is your performance summary for this session. Click the button to read your final state:

<script>
// We request the local storage or core event data from the active LiaScript session
let totalQuestions = 3;
let correctCount = 0;

try {
  // Access LiaScript's native PWA local DB state safely 
  // If previewing locally, fallback to scanning DOM states or active tracking matrices
  let quizBlocks = document.querySelectorAll('.lia-quiz');
  
  quizBlocks.forEach(quiz => {
    // LiaScript appends specific classes or green checks when solved correctly
    if (quiz.querySelector('.lia-icon-check') || quiz.classList.contains('lia-quiz-solved')) {
      correctCount++;
    }
  });
} catch(e) {
  console.log("State reading initialized");
}

let percentage = ((correctCount / totalQuestions) * 100).toFixed(0);

`### Your Score: ${correctCount} / ${totalQuestions} (${percentage}%)
${percentage >= 60 ? "**Status:** 🎉 Passed!" : "**Status:** ❌ Failed. Please try again."}`;
</script>
