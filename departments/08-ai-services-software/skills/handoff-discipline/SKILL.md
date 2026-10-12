---
name: handoff-discipline
description: End each work session with a cold-readable handoff and a shared vocabulary ledger so the next session loses nothing.
---
# Handoff Discipline

## When to use
End of every session; before switching executors; before context gets long and quality drops.

## Steps
1. Write `../../templates/handoff.md`: what closed, what remains, ordered by what unblocks the most, current state snapshot, open decisions and who owns them.
2. Update the ubiquitous-language ledger: plain-English business term, code symbols, definition and scope, any constitution constraint.
3. Keep sandbox spikes in a clearly marked scratch area, never mixed into production code.
4. Start the next session by reading the handoff and ledger, not by re-deriving context.

## Gates
A handoff must make sense to a reader with no memory of the session. If it does not, rewrite it.
