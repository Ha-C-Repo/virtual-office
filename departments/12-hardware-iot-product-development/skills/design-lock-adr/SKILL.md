---
name: design-lock-adr
description: Record architecture decisions as numbered design locks that freeze a choice and its reasons.
---
# Design Lock (Architecture Decision Record)

## When to use
Choosing a processor class, connectivity method, cloud architecture, data model, security approach, mobile platform strategy, or any decision hard to reverse.

## Steps
1. State the decision question and constraints.
2. List two to four options with pros, cons, cost and risk.
3. Choose; give the reasons.
4. State consequences and what would make us revisit.
5. Number it, date it, name the owner. Use `../../templates/design-lock.md`.
6. Store in the architecture folder; send a copy to IP coordinator.
7. Supersede, never edit, when changing a lock.

## Gates
Cross-area locks need the product development lead; locks with spend need the principal.
