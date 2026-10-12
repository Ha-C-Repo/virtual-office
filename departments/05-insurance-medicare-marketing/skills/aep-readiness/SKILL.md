---
name: aep-readiness
description: Annual Enrollment Period war room. Builds the master calendar, per-agent checklist and gap report, and drafts the kickoff email.
---
# AEP readiness

## When to use
Starting in early summer each year, and again for the January new-effective-date window.

## Inputs
Roster, carrier contracting tracker (`../carrier-contracting-tracker/SKILL.md`), SOA register, regulator calendar for the year.

## Steps
1. Build the master calendar: training opens, certification deadlines, annual notice of change delivered by September 30, next-year marketing starts October 1, AEP October 15 to December 7, new-effective-date calls in January, open enrollment period January 1 to March 31.
2. Build the per-agent checklist: license active in each selling state (flag expirations before AEP ends); annual industry certification passed and transmitted to each carrier; carrier product certifications per carrier; E&O spanning the whole season; ready-to-sell notice on file per carrier; book-of-business review done.
3. Marketing readiness: approved pieces for the season are cleared through `../../workflows/outward-deliverable-chain.md`.
4. Gap report (`../../templates/aep-gap-report.md`): each item is PASS, GAP or UNVERIFIED. A missing ready-to-sell notice is UNVERIFIED, never PASS.
5. Draft the kickoff email (`../../templates/aep-kickoff-email.md`) in principal voice with dated milestones.

## Outputs
Calendar, gap report, kickoff email draft, internal memo.

## Gates
Re-verify every date against the regulator each June. Kickoff email is held for {{PRINCIPAL_ROLE}} approval. Never mark an item PASS without evidence.
