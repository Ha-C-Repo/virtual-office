---
name: open-house-kit
description: Build a complete open house kit: sign-in sheet, flyer, feature sheet, tour link, follow-up sequence, internal notes.
---
# Open House Kit

## When to use
An open house is scheduled for {{PROPERTY_ADDRESS}} on {{EVENT_DATE}}.

## Inputs
Listing record, photos, tour link, brand voice guide, event time window.

## Steps
1. Sign-in sheet with a consent line for follow-up (`../../templates/open-house-signin-sheet.md`).
2. Flyer and feature sheet from sourced facts only (`../../templates/open-house-flyer-and-feature-sheet.md`).
3. Tour QR or link, if a tour is published and approved.
4. Follow-up sequence: same-evening thank-you, day-2 feedback ask (`../../templates/followup-sequence.md`).
5. Internal agent notes: traffic log, visitor feedback, offers received.
6. Run `../listing-compliance/SKILL.md` on every public piece.

## Outputs
Printable kit, follow-up drafts in the approval queue, internal notes file.

## Gates
Follow-up goes only to visitors who consented, through the outbound gate. Flyers carry required broker identification and the fair-housing line.
