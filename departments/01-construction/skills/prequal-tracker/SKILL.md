---
name: prequal-tracker
description: Tracks the 12-item contractor prequalification checklist, computes percent complete and ranks open blockers from verified data only.
---
## When to use
Daily briefing and whenever a prequalification request arrives.

## Inputs
Checklist status, document dates and expiries.

## Steps
1. Load `../../templates/prequalification-checklist.md`.
2. Mark each item: COMPLETE, EXPIRING (inside 30 days), MISSING or NOT_APPLICABLE.
3. Compute percent complete.
4. Rank blockers: critical first (experience-mod letter, insurance certificates, quality-management certification).
5. Surface critical blockers in the morning briefing until cleared.

## Outputs
Ranked blocker list.

## Gates
Verified data only. Do not mark an item complete from memory; cite the document and date.
