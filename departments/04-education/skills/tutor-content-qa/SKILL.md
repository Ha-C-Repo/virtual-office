---
name: tutor-content-qa
description: Four-check pedagogy QA for tutoring output: correctness, step completeness, readability, explain-it-back.
---
# Tutor Content QA

## When to use
On any batch of tutor output (sample problems, regression sets, curriculum QA log items) before it is trusted.

## Inputs
Problem text, explanation draft (steps, final answer, practice variant, explain-it-back prompt), solver verdict, target grade band, cited fact base for non-math claims.

## Steps
1. Correctness: solver verdict is verified for math; for non-math, each factual claim traces to a cited fact base entry. No source means FAIL.
2. Step completeness: each step is needed for the band and no leap is unexplained.
3. Readability: sentence length and vocabulary suit the band; parent-facing text is adult plain English.
4. Explain-it-back: a practice variant and an explain-it-back prompt are both present. Either missing is FAIL.
5. Tone: patient, specific, no shaming, specific encouragement, honest uncertainty.
6. Record confidence (high, medium, low). Low goes to the curriculum QA log.

## Outputs
Pass/fail table with evidence per check, QA log entries.

## Gates
Never pass an item the solver refuted or could not check unless it is labeled "not checked" with a plain reason.
