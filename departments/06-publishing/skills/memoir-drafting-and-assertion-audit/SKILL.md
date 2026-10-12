---
name: memoir-drafting-and-assertion-audit
description: Architecture, chapter-by-chapter drafting with a passage authorship ledger, and an assertion audit that diffs every claim to source.
---
# Memoir Drafting and Assertion Audit

## When to use
Pipeline steps 12 to 14 (gate G5c) and the recurring loop in `../../workflows/memoir-drafting-loop.md`.

## Architecture (step 12)
- Timeline v2 from interviews plus sources.
- Outline by chapter.
- One sentence stating the subject of the book, approved by the subject.

## Drafting
1. One chapter at a time from a chapter brief (`../../templates/memoir-chapter-brief.md`) listing sources, allowed facts, quotes and open questions.
2. Authorship mode governs how much is drafted: A Organizer (structure only), B Collaborator (co-written), C Draft-first (drafted for the subject to rework).
3. Every passage is tiered in the **passage authorship ledger**: tier 1 human-written, tier 2 human-rewritten from a draft, tier 3 AI as generated. Default down when unsure.
4. Content guard: output may use only content words and exact numbers present in the input brief. No invented sensory detail or dialogue.
5. Quotes come only from source text and are verified by script against the source archive. No song lyrics.

## Assertion audit
1. Extract every factual claim (people, places, dates, numbers, quotes, causal statements).
2. Diff each claim to a source reference. Classify: supported, partly supported, unsupported, contradicted.
3. Unsupported or contradicted claims are removed or sent back to the subject as questions.
4. Tag confidence (high, medium, low). Low goes to a human.

## Outputs
Chapter draft, ledger update, voice-fidelity report, assertion-audit table.

## Gates
G5c requires: audit with no open unsupported claims, fidelity report, human read by the subject. Version every draft; never overwrite.
