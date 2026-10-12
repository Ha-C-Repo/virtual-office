---
name: readability-gate
description: Measure story-text readability per spread and for the whole book against the age-band target, then revise and remeasure until in band.
---
# Readability Gate

## When to use
Pipeline step 3. After every substantive text revision.

## Inputs
- Manuscript from `../manuscript-drafting/SKILL.md` (story text only).
- Target band for the age group, stated in the concept record as {{TARGET_READABILITY_BAND}}.

## Method
1. Extract story text only: no title page, credits, dedication, back matter or disclosure line.
2. Measure each spread and the whole book with a recognized readability formula suited to early readers (an early-grade word-list formula for very young bands; a grade-level formula for early readers and chapter books). Use a script or library; do not estimate by eye.
3. Record scores in `../../templates/readability-report.md`, including flagged words (off-list or multi-syllable).
4. If a spread is out of band, revise the text, remeasure, and log the pass-to-pass change.
5. Repeat until the whole book and each spread are in band.

## Outputs
Completed readability report saved as numbered working file 03.

## Gates
- The threshold is fixed by the concept record. Never loosen it because a draft failed.
- Readability is necessary, not sufficient: the human read-aloud (blocking) still applies.
- Report the tool and version used so results are repeatable.
