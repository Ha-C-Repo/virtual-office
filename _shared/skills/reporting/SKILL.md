---
name: reporting
description: Produces weekly, monthly and ad hoc reports (status, KPI, pipeline, finance, compliance) from sources of record with measured numbers, stated freshness, and a one-line headline. Use for any recurring or one-off report.
---

# Reporting

## When to use
Weekly status, monthly review, pipeline summary, KPI pack, investor or board update, compliance scorecard, morning briefing.

## Inputs
Registers and data sources by path, reporting period, audience, template `../../templates/status-report.md` or `../../templates/weekly-report.md`.

## Steps
1. State the headline in one sentence: the one thing the reader should know.
2. Pull numbers from the source of record. Stamp each with its as-of date. Refuse stale inputs where a freshness window applies.
3. Compute with a calculator or script; cross-check totals (for example, sum of variances equals total variance).
4. Tag each number VERIFIED or ESTIMATED. ESTIMATED requires the method.
5. Compare against target and prior period. Show the variance with sign.
6. List decisions needed from the human, risks, and items inside warning windows.
7. Prose for narrative; a table for numbers. Keep it one page when possible.
8. Internal twin holds detail and sources. Outward versions (investor, client) carry only what that audience may see.
9. Voice firewall, QA editor, human sign-off for outward reports.

## Outputs
Report, internal twin, as-of stamps, decisions list.

## Gates
- No number without a source and a date.
- Underperformance triggers (for example consecutive periods below target) escalate automatically to the human.
- Honest limits: say "not separated" or "insufficient data" instead of choosing a winner.
- Routines that produce reports ship only after their output passes owner review twice.

## Anti-patterns
Burying the headline. Mixing verified and estimated figures without labels. Reporting activity instead of results.
