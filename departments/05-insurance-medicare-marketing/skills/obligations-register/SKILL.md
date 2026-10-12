---
name: obligations-register
description: Extracts obligations from signed agreements into a register with owners, triggers and status.
---
# Obligations register

## When to use
When any agreement (carrier, upline, vendor, agent) is signed or amended.

## Steps
1. Read the agreement clause by clause.
2. For each obligation record: source clause, obligation, type (deliverable, signature gate, money moment, notice), owner, due date or trigger, status, evidence link.
3. Status values: TEMPLATE, OPEN, IN PROGRESS, DONE, AT RISK, MISSED.
4. Overdue items flip to AT RISK automatically at the monthly sweep. Missed items prompt a NOTICE-CANDIDATE tag for `../contract-notice/SKILL.md`.

## Outputs
Register rows; monthly overdue list.

## Gates
Confidence tag on each extraction; low confidence to a human. Append-only history.
