---
name: operational-record-keeping
description: Choose and write the right operational record type after any piece of engineering work.
---
# Operational Record Keeping

## When to use
At the end of every work session and at each stage of a change.

## Record type chooser
| Situation | Record | Template |
|---|---|---|
| Measured something, changed nothing | Finding | `../../templates/finding.md` |
| Something shipped | Deploy record | `../../templates/deploy-record.md` |
| Session ending, work remains | Handoff | `../../templates/handoff.md` |
| Repeatable procedure | Runbook | `../../templates/runbook.md` |
| Owner answered a question | Decision record | `../../templates/decision-record.md` |
| Something broke | Incident report | `../../templates/incident-report.md` |
| Instructions for a code executor | Executor prompt | `../../templates/code-executor-prompt.md` |

## Steps
1. Pick the type. One record, one purpose.
2. Open with a one-paragraph answer.
3. Add method, measurements (dated), what changed, how it was verified, rollback, what remains, who must decide.
4. Mark facts measured or assumed.
5. State what it supersedes, if anything.
6. Strip secrets, account identifiers and personal data.

## Gates
Records for the principal are human-facing prose. Records for machines are structured. Do not mix the two.
