# Workflow: Weekly Review Cadence

Skills: `../skills/reporting/SKILL.md`, `../skills/scheduling-and-routines/SKILL.md`, `../skills/registers/SKILL.md`. Template: `../templates/weekly-report.md`.

## Daily (short)
| Step | Who | Output |
|---|---|---|
| Morning brief: deadlines inside warning windows, overnight inbound, new reviews, compliance flags, one thing to do first | Coordinator (routine) | Brief to the owner role |
| Register sweep for expiries and missing evidence | Records keeper | Flag list |

## Weekly
| # | Step | Who | Gate |
|---|---|---|---|
| 1 | Pull numbers from sources of record with as-of stamps. | Coordinator | No stale inputs |
| 2 | Compute and cross-check totals. | Coordinator | Calculator, second path |
| 3 | Compare with target and prior week; sign the variance. | Coordinator | VERIFIED or ESTIMATED tag |
| 4 | Escalate underperformance triggers (for example consecutive weeks below target). | Coordinator | Automatic escalation |
| 5 | Review open promises, aged items, pipeline. | Coordinator | |
| 6 | Support quality audit: sample replies for voice and accuracy. | QA editor | |
| 7 | Cost review for AI and tool usage; flag any paid tool outside the approved stack. | Coordinator | Cost flagged as {{PRICE}} to confirm |
| 8 | Draft the weekly report. | Coordinator | Voice check |
| 9 | Owner review. | Owner role | |

## Monthly
Context audit (always-loaded memory, stale pointers, duplicate or overlapping skills, unused connectors, plaintext secrets). Report first; change nothing until approved. Consent expiry sweep. Retention-end list for the next 12 months.

## Quarterly
Platform and policy re-check (rule, source, date checked, next check). Skills audit. Model and routine recalibration.

## Yearly
Re-verify every dated rule, cap, calendar and enrollment window against the authority.
