---
name: answer-verification
description: Build the check plan from the learner's text and route the solver verdict into a result: certified, unchecked, solver-only or failed.
---
# Answer Verification

## When to use
Designing, testing or changing the tutoring pipeline's verification path.

## Inputs
Learner problem text, explanation draft, solver contract, `../../templates/solver-test-vectors.md`.

## Steps
1. Build the check plan from the learner's own text, never from the model: single equation in one unknown, pure numeric expression, or out-of-domain (known before any model call).
2. The model returns steps, final answer in its own structured field, practice variant, explain-it-back prompt, uncertainty flag.
3. The solver verifies the final answer against the original problem.
4. Route the verdict:
   - verified: show steps and certified answer plus variant and prompt (outcome CERTIFIED).
   - unverifiable: show steps labeled "not checked" with a plain reason; confidence LOW; log to curriculum QA (UNCHECKED).
   - refuted: do not show the draft as an answer; exactly one retry with the solver result as a constraint; if still refuted show the solver answer only, no steps, and log (SOLVER_ONLY). The retry never counts against the learner's quota.
   - provider offline: if the solver can answer alone, show the certified answer with a note; else a plain failure (FAILED). No silent queue or background retry.
5. Save to local history. Increment the meter only on successful outcomes.

## Outputs
Tutor result: outcome, steps, answer, verdict, confidence, practice variant, explain-it-back prompt, message, model_calls, counts_against_meter.

## Gates
Fail closed. A verified result with a failed audit write is downgraded to unverifiable. Test that a wrong answer cannot ship and that retries are bounded to one by counting calls.
