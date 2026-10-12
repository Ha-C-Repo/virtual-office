# Commission Reconciliation Report

Document number: CMP-{{YEAR}}-{{ABBREV}}-{{SEQ}}   (internal memo: append -INT)
Internal only. Contains commission data. Never outward.

## Statement read
Carrier: {{CARRIER}}   Statement period: {{PERIOD}}   Rows read: {{ROW_COUNT}}
Columns mapped: {{MAPPING_DECISIONS}}
Comp grid version: {{GRID_VERSION}}   FMV cap table year: {{CAP_YEAR}}

## Totals
| Carrier | Paid | Expected | Variance | Lines MATCH | VARIANCE | UNMATCHED |
|---|---|---|---|---|---|---|
| {{CARRIER}} | {{PAID}} | {{EXPECTED}} | {{VARIANCE}} | {{N}} | {{N}} | {{N}} |

By writing agent: same columns with {{WRITING_AGENT_ID}} as key.
Integrity check: sum of line variances equals total variance: yes / no.

## Line detail (record ID masked as initials plus last four)
| Line ID | Record ref | Matched grid row | Expected | Paid | Variance | Status | Confidence | Reason | Flags |
|---|---|---|---|---|---|---|---|---|---|
| {{LINE_ID}} | {{MASKED_REF}} | {{GRID_ROW}} | | | | MATCH / VARIANCE / UNMATCHED | high / medium / low | {{REASON}} | FMV-EXCEEDS-CAP / none |

## Human review list
Every VARIANCE, UNMATCHED, low-confidence line and cap flag is listed here with an owner and due date.

## Sign-off
Reviewed by {{REVIEWER_ROLE}} on {{DATE}}. Disputes escalated through draft notice: yes / no.
