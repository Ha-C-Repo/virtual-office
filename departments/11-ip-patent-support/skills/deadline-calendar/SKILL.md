---
name: deadline-calendar
description: Maintain an IP deadline calendar with early warnings, using dates supplied by counsel or the filing record.
---
# IP Deadline Calendar

## When to use
Whenever a deadline appears in the register, and weekly for the warning scan.

## Inputs
Register rows with `next_deadline`, `../../knowledge/deadline-types.md` (orientation only), counsel instructions.

## Steps
1. Enter each deadline with its source and the date recorded.
2. Set warnings at 90, 60, 30, 14 and 7 days. {{WARNING_WINDOWS}} overrides these.
3. Each week list deadlines inside the first window and send to the coordinator.
4. A deadline inside 14 days with no counsel acknowledgment goes to `../../workflows/deadline-escalation.md`.
5. After the date passes, record the outcome from a document (filed, extended, lapsed) or leave "outcome unknown" and ask.

## Outputs
Upcoming-deadline list and escalation messages.

## Gates
The calendar never calculates a legal deadline. A missing source blocks the entry.
