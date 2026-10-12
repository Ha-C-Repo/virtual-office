# Register: {{REGISTER_NAME}}

Purpose: {{PURPOSE}}
Owner role: {{OWNER_ROLE}}   Keeper: records keeper   Retention: {{RETENTION_RULE}}
Review cadence: {{CADENCE}}   Last reviewed: {{DATE}}

## Rules
1. Append-only. Status changes add a note. Corrections add a new row or note; originals stay visible.
2. Evidence path on every row. No evidence means status NOT STARTED and evidence "none".
3. Identities masked: initials plus last four characters of an assigned ID.
4. Clocks start at row creation. Rows inside the warning window are flagged at each review.
5. No deletion before retention end. Retire with approval and a changelog line.
6. A row supports a gate; it never replaces one. UNVERIFIED rows support no money-touching claim.

## Columns
| ID | Date recorded | Subject (masked) | Type | Status | Confidence | Evidence path | Valid from | Valid until / expiry | Retention end | Owner role | Recorded by (role) | Notes (append only) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {{ID}} | {{DATE}} | {{MASKED_SUBJECT}} | {{TYPE}} | {{STATUS}} | {{HIGH_MED_LOW}} | {{PATH}} | {{DATE}} | {{DATE}} | {{DATE}} | {{OWNER_ROLE}} | {{ROLE}} | {{NOTE}} |

## Status values
NOT STARTED, OPEN, IN PROGRESS, DONE, AT RISK, MISSED, ACTIVE, EXPIRED, REVOKED, CONSUMED, UNVERIFIED. Use only the values this register defines.

## Sweep checklist
- [ ] Rows inside the warning window
- [ ] Rows with no evidence path
- [ ] UNVERIFIED rows older than the re-check interval
- [ ] Rows past expiry still marked active
- [ ] Items needing a human decision

## Changelog
| UTC timestamp | Change | Approver role | Backup path |
|---|---|---|---|
| {{TIMESTAMP}} | {{CHANGE}} | {{ROLE}} | {{BACKUP_PATH}} |
