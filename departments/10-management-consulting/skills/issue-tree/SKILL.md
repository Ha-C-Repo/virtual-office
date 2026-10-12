---
name: issue-tree
description: Build a mutually exclusive, collectively exhaustive issue tree and prioritize branches to investigate.
---
# Issue Tree

## When to use
Structuring a diagnostic or any open business question.

## Steps
1. State the key question as a decision ("Should {{CLIENT}} do X?") or a gap ("Why has margin fallen?").
2. Split into branches that do not overlap and together cover the question (profit = revenue minus cost; revenue = volume times price; etc.).
3. Go two to three levels deep.
4. For each leaf write the hypothesis and the data that would prove or disprove it.
5. Rank leaves by impact and ease of testing; investigate the top few first.
6. Revise as data arrives; keep a log of branches closed.

## Output
One-page tree plus a work plan (`../../templates/work-plan.md`).
