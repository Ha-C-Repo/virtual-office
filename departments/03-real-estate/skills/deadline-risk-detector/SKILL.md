---
name: deadline-risk-detector
description: Watch transaction dates and flag deadlines that are near, stalled, or silently lapsed.
---
# Deadline Risk Detector

## When to use
Daily during any open transaction, and after any amendment.

## Inputs
Deadline table from `../transaction-timeline/SKILL.md`, checklist status, last-activity dates.

## Steps
1. For each open item compute days-until with a script.
2. Classify: NEAR (within {{DEADLINE_ALERT_DAYS}} days with the item open), STALLED (no activity for {{STALL_DAYS}} days), LAPSED (date passed with no recorded outcome).
3. LAPSED items are the priority: confirm whether the event occurred and record it.
4. Draft a short alert to the principal listing the item, date, what is outstanding, and the suggested next action.

## Outputs
Risk list sorted by severity, alert draft.

## Gates
Do not message outside parties from this skill. Alerts go to the principal only. Do not assume an event happened because its date passed.
