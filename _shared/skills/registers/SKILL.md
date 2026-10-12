---
name: registers
description: How to design, keep and use registers (consent, disclosure, permits, obligations, correspondence, contacts, data processing, platform policy, permissions, AI disclosure). Registers are sources of record: append-only, evidence-linked, retention-aware. Use when any fact needs a durable home.
---

# Registers

## When to use
When a fact must be answerable later to a regulator, client, auditor or court; when a clock (expiry, deadline, retention) must run; when more than one department needs the same fact.

## Principles
1. One home per fact. Other documents link by path.
2. Append-only. Status changes append a note. Corrections append. Originals remain visible.
3. Evidence path on every row. No evidence means NOT STARTED.
4. Masked identities: initials plus last four characters of an assigned ID.
5. Clocks start at creation: validity, expiry, retention end, re-check date.
6. No row is deleted before retention end. Retire with approval and a log line.
7. Live registers (spreadsheet or database) are read directly. Never mirror them into prose.
8. A row does not clear a claim by itself. It supports a gate; it does not replace one.

## Register kinds (generic)
Consent and opt-out; disclosure (condition, AI, material facts); permits and licenses; obligations; correspondence; data processing; platform policy (rule, source, date checked, re-check); permissions and rights; production log; persons and clearance; certification and training; contracting and appointments; incidents.

## Steps
1. Pick or create the register from `../../templates/register.md`.
2. Define columns (field names in `../../knowledge/schemas.md`).
3. Add rows only with evidence.
4. Set clocks and a sweep schedule (see `../scheduling-and-routines/SKILL.md`).
5. Review monthly: items inside the warning window, rows missing evidence, UNVERIFIED rows.

## Outputs
Register rows, sweep report, list of items needing a human.

## Gates
No guessing a value. UNVERIFIED items never support a money-touching claim. Re-verify dated rules at least yearly.

## Anti-patterns
A register kept in someone's memory. Overwriting a status. Storing identifiers in clear text in prose files.
