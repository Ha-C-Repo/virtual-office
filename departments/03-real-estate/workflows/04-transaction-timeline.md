# 04 Transaction Timeline

Owner: transaction-coordinator | Approver: {{PRINCIPAL_AGENT}}

## Steps
1. Executed contract received. Start the 24-hour clock.
2. Extract dates with clause references: effective, option end, financing, appraisal, title, HOA, closing (`../skills/transaction-timeline/SKILL.md`).
3. Compute days-until with a script.
4. GATE: principal confirms the extracted dates.
5. Publish the calendar to {{CALENDAR_LOCATION}}.
6. Build the document checklist by transaction type.
7. Daily deadline pull; run `../skills/deadline-risk-detector/SKILL.md`. Alert the principal on NEAR, STALLED, LAPSED.
8. Handle change requests with `../skills/amendment-generator/SKILL.md`. GATE: principal approves any change to price, repairs or dates.
9. Closing checklist, final walkthrough, funds and keys.
10. Post-closing: update contact record, schedule retention touches (`07-outbound-and-lead-retention.md`), archive the file.

## Outputs
Deadline table, calendar, checklists, alert log, amendments, closing record.
