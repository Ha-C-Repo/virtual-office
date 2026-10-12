# 01 Learner Problem-Solving Flow (runtime)

Owner: verification-engineer | Reviewer: tutor-content-qa

## Steps
1. Intake: typed text or photo.
   - Photo: optional crop first, then vision transcription with confidence. The learner edits and MUST confirm. Unconfirmed transcription has no path to a solve.
2. Build the check plan from the learner's own text (never the model): one equation in one unknown, a pure numeric expression, or out-of-domain (known before any model call).
3. Model drafts: steps, final answer in its own structured field, practice variant, explain-it-back prompt, uncertainty flag.
4. Solver verifies the final answer against the original problem.
5. Route the verdict:
   - verified: show steps and certified answer, plus variant and prompt.
   - unverifiable: show steps labeled "not checked" with a plain reason; confidence LOW; log to curriculum QA.
   - refuted: hide the draft; one retry with the solver result as a constraint; if still refuted show solver answer only, log. Retry never counts against quota.
   - provider offline: certified answer with a note if the solver can answer alone; otherwise a plain failure. No silent queue.
6. Save to local history. Increment the meter only on successful outcomes.

## Outcome set
CERTIFIED, UNCHECKED, SOLVER_ONLY, FAILED.

## Confidence tagging
High / medium / low on every extraction and solution. Edited transcription is never high. Model-flagged uncertainty or a non-verified verdict forces low. Low is shown as "check this step".

## Gates
Fail closed. Test: a wrong answer cannot ship; retries bounded to one by counting calls.
