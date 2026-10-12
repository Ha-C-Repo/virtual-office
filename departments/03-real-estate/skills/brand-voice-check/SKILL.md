---
name: brand-voice-check
description: Final voice pass that removes AI-isms and enforces the brokerage brand voice and formatting rules.
---
# Brand Voice Check

## When to use
The last pass on any text for clients or the public, and on emails drafted in the owner's voice.

## Inputs
Draft text, `../../templates/brand-voice-guide.md`.

## Steps
1. Remove banned patterns: em-dashes, three-adjective lists, "not just X, it's Y", vague intensifiers, cliches, emojis in client documents.
2. Replace vague claims with concrete, sourced ones.
3. Shorten: short sentences, active voice, one idea per sentence.
4. Confirm no unfilled tokens remain.
5. For emails in the owner's voice: warm, direct, plain; no stock openers or closers.
6. List the changes made.

## Outputs
Revised text and a change list.

## Gates
Voice edits never change numbers, dates or legal wording. If a fix would alter meaning, flag it for the principal.
