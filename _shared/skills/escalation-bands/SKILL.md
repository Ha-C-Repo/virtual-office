---
name: escalation-bands
description: Four escalation bands that decide how much autonomy the office has on a task: AUTO (execute), DRAFT (draft with voice check), BRIEF (draft, brief the human, ship only on approval), WAIT (escalate, do not draft). Use to label every task and every output.
---

# Escalation bands

## When to use
Every task gets a band at intake, and every output starts with its band label as the first line (for example `BAND: BRIEF`). When in doubt, escalate up.

## The bands
| Band | Meaning | Examples |
|---|---|---|
| AUTO | Execute without asking. Low risk, reversible, internal only, no money or regulated content. | Logging a register row from a document on file, formatting notes, running a read-only check, building an index |
| DRAFT | Produce a draft and run the voice check. A human reviews before use. | Internal memo, first-pass report, blog outline, meeting minutes |
| BRIEF | Draft, then brief the human with the deliverable, internal twin, gate results and open flags. Nothing ships until approved. | Client proposal, outward email, listing copy, regulated marketing piece, public reply, anything with a price |
| WAIT | Escalate. Do not draft. State the issue, the options and what would cure it. | Legal threat, safety allegation, request to bypass a gate, missing consent, a contract signature, a termination, a regulator contact, a credential request |

## Inputs
The task, its audience, whether it leaves the office, whether it touches money, people, safety, health, children or law.

## Steps
1. Ask: does it leave the office? Does it contain a number that costs money? Does it touch a regulated topic? Is it reversible?
2. Start at AUTO. Move up one band for each yes: leaves the office (at least BRIEF), money or regulated (BRIEF), allegation, signature, safety, legal, or gate bypass (WAIT).
3. If two people could disagree on the band, take the higher one.
4. Write the band label as the first line of the output.
5. Record any band override in the decision log.

## Outputs
A band label and, for BRIEF and WAIT, a one-paragraph reason.

## Gates
- A lower band cannot be chosen to avoid review.
- Bands may be raised by any agent and lowered only by the human owner, with a log line.
- WAIT items are never "drafted anyway for convenience".

## Anti-patterns
Calling an outward email DRAFT because it is short. Treating a repeat task as AUTO after it failed once. Letting urgency lower the band.
