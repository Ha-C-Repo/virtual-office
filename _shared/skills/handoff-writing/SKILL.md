---
name: handoff-writing
description: Write a handoff that lets a fresh session or a new owner continue without the previous conversation. Answers: what closed, what remains sorted by what unblocks it, what to read first. Use at the end of every session and at every department boundary.
---

# Handoff writing

## When to use
End of a work session; before a department boundary; before a long pause; after an incident.

## Inputs
The session's work, the current status view, the decision log, open items.

## Steps
1. Open with one paragraph that answers: where does this stand?
2. List what closed, each with its verification evidence (the check run, the result).
3. List what remains, sorted by what unblocks it, not by importance. Name the owner and the blocker.
4. State decisions made (with date and who decided) and decisions pending (with options and recommendation).
5. Give the "read first" list: at most five files, in order.
6. State non-negotiables for the next session (hard rules that apply, protected files, gates).
7. Mark measured facts vs assumed facts. Date every measurement.
8. Define done: the observable condition that ends this work.
9. Write it to be read cold. No shorthand that needs the old chat. Use `../../templates/handoff.md`.

## Outputs
A dated handoff file, linked from the project's context layer.

## Gates
- Facts with sources; assumptions labeled.
- Living documents (registers, schedules, pipeline databases) are listed by path, never copied.
- A handoff with unverified "done" claims is rejected by the coordinator.

## Anti-patterns
A narrative of the session instead of a state snapshot. Burying the blocker. Copying live data into the handoff.
