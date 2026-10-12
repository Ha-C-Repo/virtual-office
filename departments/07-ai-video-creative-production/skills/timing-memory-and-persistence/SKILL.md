---
name: timing-memory-and-persistence
description: Record observed generation durations, schedule check-ins, keep run state and resume after interruption.
---
# Timing Memory and Persistence

## When to use
Any long-running generation job.

## Timing memory
- Store, per node type, the list of observed durations in seconds with rolling mean, rolling standard deviation and last-updated (see `../../knowledge/schemas.md`).
- Next wait = mean plus one standard deviation. Check at that time, then at short intervals.
- Update the sample list after every completed node.

## Persistent driver
- Keep wave state: pending nodes, running nodes, completed nodes, failures.
- Schedule check-ins instead of busy polling.
- Circuit breaker: after repeated external-app errors, stop and report.

## Resume
1. After any interruption, read `../../templates/session-resume.md` and `../../templates/run-state.md`.
2. Run the pre-flight checks again (references, wiring, mode toggles, approved batch).
3. Continue from the first incomplete step; do not rerun completed nodes.

## Gates
A resumed run still needs the original cost-gate go; if the scope changed, quote again.
