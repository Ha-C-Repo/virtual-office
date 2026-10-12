---
name: deliverable-compliance
description: Always-on baseline of forbidden items and the scan order applied to any outward document before the Medicare gate and scrubber.
---
# Deliverable compliance baseline

## When to use
Before drafting and before review of any document that could leave the office.

## Forbidden on any outward document
- Commission schedules, override splits, margins, production figures.
- PHI or PII outside approved systems. Sample records must be labeled SAMPLE.
- Unverifiable superlatives; any statistic without source and year.
- Carrier names beyond appointment or approval status; carrier disparagement; misleading side-by-side comparisons.
- Fabricated license numbers, producer numbers, appointments, certification status, enrollment figures or compliance status.
- Recreated logos or brand marks. Approved masters only. Trademark references are descriptive only.
- Claims about branch production, size or track record without {{PRINCIPAL_ROLE}} confirmation.
- Income or compensation figures in recruiting material (qualitative claims only).

## Scan order
1. Forbidden items above.
2. Disclaimers and required language by artifact type.
3. Demonstration label until the engagement is live.
4. Placeholder tokens: unresolved TBD, TBA or PENDING fail; bracket placeholders warn in demo mode.
5. Voice kill list (`../voice-check/SKILL.md`).

## Outputs
Findings list passed to `../medicare-compliance-gate/SKILL.md` and `../output-scrubber/SKILL.md`. Record in the internal memo.

## Gates
The outward piece and its internal memo are both scanned. PDF only for anything leaving the office.
