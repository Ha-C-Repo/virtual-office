# Workflow: Register Maintenance

Skill: `../skills/registers/SKILL.md`. Template: `../templates/register.md`. Agent: records keeper.

| # | Step | Gate |
|---|---|---|
| 1 | Receive the event and its evidence document. | No evidence, no row |
| 2 | Read the document itself; do not rely on its summary. | Verify, do not generate |
| 3 | Add or update the row: date, masked subject, status, confidence, evidence path, clocks. | Append-only |
| 4 | Start clocks: validity, expiry, retention end, re-check date. | |
| 5 | Mask identities (initials plus last four characters of an assigned ID). | |
| 6 | Back up before any overwrite; add a changelog line. | `backup-before-overwrite.md` |
| 7 | Sweep on schedule: warning window, missing evidence, UNVERIFIED rows, past-expiry rows still active. | |
| 8 | Route flags to the owner role with the item and the cure. | |
| 9 | Retention end: retire with approval and a log line. Never delete earlier. | Human approval |
| 10 | Yearly: re-verify dated rules the register depends on. | |

Opt-outs and revocations update the register the same day.
