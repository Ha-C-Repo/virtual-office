---
name: site-diary
description: Processes daily field messages and voice-note transcripts into structured logs and a weekly digest, with confidence tags and supervisor approval.
---
## When to use
Daily, and for the Friday digest. See `../../workflows/11-site-diary-daily-routine.md`.

## Inputs
Unprocessed raw messages, cost codes, contract weather threshold.

## Steps
1. Read unprocessed messages.
2. Extract to DIARY, LABOR, QUANTITIES, DELIVERIES, DELAYS, TASKS (fields in `../../knowledge/schemas.md`).
3. Tag confidence. For LOW rows write a clarifying question to the supervisor.
4. Mark rows processed only after all targets are written.
5. Supervisor approves in the portal.
6. Friday: one-page digest from `../../templates/weekly-owner-digest.md`.

## Outputs
Log rows, questions, digest.

## Gates
Never auto-approve. Supplier names stay internal. Do not invent hours or quantities. Run in sandbox before live.
