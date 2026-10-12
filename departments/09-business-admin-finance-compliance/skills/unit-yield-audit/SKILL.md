---
name: unit-yield-audit
description: Weekly net-yield audit per production unit with underperformance escalation and gap reporting in both directions.
---
# Unit yield audit

## When to use
Every Monday for the prior week.

## Inputs
Active asset count (with count status), gross sales for the last 7 days, operating cost spent, target net yield per unit.

## Steps
1. Pull the sales register, cost register and active count for each unit.
2. Net yield = gross sales minus operating cost for the week. Show arithmetic.
3. Percent of target = net yield divided by target.
4. Tag count status VERIFIED or ESTIMATED.
5. Compare register versus physical versus sales versus cost. Report gaps in both directions: assets sold but not in the register, assets in the register not found, cost without a source document.
6. Escalation: a unit below target for the configured number of consecutive weeks gets an escalation flag for {{OWNER_ROLE}}.
7. Write the audit row using the yield schema in `../../knowledge/schemas.md`.

## Outputs
Yield table, gap list, escalation list, summary paragraph. Template: `../../templates/weekly-yield-audit.md`.

## Gates
Internal only. Do not use ESTIMATED counts for escalation without stating so.
