---
name: release-notes-format
description: Write release notes in short (character-limited) and long forms that lead with the user-visible change.
---
# Release Notes Format

## When to use
Each release candidate.

## Inputs
Change list, version, date, known limitations, character limit {{NOTES_CHAR_LIMIT}}.

## Steps
1. Short form: lead with the user-visible change in one or two sentences, within the limit.
2. Long form: version and date; New; Improved; Fixed; known limitations.
3. Only describe things a user can see or feel. No internal refactors, costs, or vendor names.
4. Run `../public-copy-scrubber/SKILL.md`.
5. Pair with the internal build report (`../release-pair-check/SKILL.md`). Same version number in both.

## Outputs
Short and long release notes using `../../templates/release-notes.md`.

## Gates
No outcome promises. Owner approval before publishing.
