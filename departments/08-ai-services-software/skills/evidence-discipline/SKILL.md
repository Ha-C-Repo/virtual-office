---
name: evidence-discipline
description: Verify, do not generate. Rules for separating measured facts from assumptions in investigations and reports.
---
# Evidence Discipline

## When to use
Investigations, audits, incident analysis, any report that states how a system behaves.

## Steps
1. Investigate read-only first. Make no change until the finding is written.
2. Record each fact with its source (command, query, file, screen) and date.
3. Tag each statement MEASURED or ASSUMED. Assumptions need a plan to verify.
4. Re-measure before relying on an old number.
5. After a fix, prove it in the real environment, not only in tests.
6. Prove backups by restoring them to a scratch database.
7. When a count or measurement is needed from a document, extract it deterministically (text layer, script); do not trust visual estimates.

## Outputs
A finding record with a measurements table and a list of open assumptions.

## Gates
A fix is not "closed" until the production verification is recorded.
