---
name: client-doc-scrubber
description: Final scrub of a client-facing document: strips internal data, verifies AI labels, finds unfilled placeholders.
---
# Client Document Scrubber

## When to use
The last step before a client document is exported or shown to the principal as final.

## Inputs
Draft client document and its internal twin.

## Steps
1. Search for internal-only content: net sheet figures, commission, fees, split, discount floor, strategy notes, internal file names (the `-INT` suffix), confidence tags written for staff.
2. Search for unfilled placeholders (`{{...}}`), TODO, TBD, lorem text.
3. Confirm AI-generated images and text carry the required label.
4. Confirm the fair-housing line and required footer are present.
5. Confirm voice rules from `../brand-voice-check/SKILL.md`.
6. Cross-check that every number matches the internal twin.

## Outputs
Scrub report and a cleaned document, or a block with line references.

## Gates
Run the export validator afterward (`../two-pdf-pair-check/SKILL.md`). Non-zero exit blocks release. Human sign-off before anything leaves the office.
