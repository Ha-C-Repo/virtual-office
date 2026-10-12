---
name: code-quality-loop
description: Plan first, small diffs, session reset before quality drops, independent review, test-feedback-repair.
---
# Code Quality Loop

## When to use
Any AI-assisted code change.

## Steps
1. **Plan first.** The executor states the plan; a reviewer checks it against the spec before code is written.
2. **Small diffs.** One task per session where possible. Use stop conditions such as "if more than {{MAX_FILES}} files change, list them first."
3. **Reset.** When responses degrade or context is long, write a handoff and start a fresh session.
4. **Independent review.** A fresh session or the `engineering-reviewer` reads the diff cold.
5. **Test-feedback-repair.** Run tests; feed failures back; repeat until green; do not edit tests merely to pass.
6. **Record.** Deploy record and handoff.

## Roles
Planner/reviewer model reasons and critiques; code-executing agent implements. Use `../../templates/code-executor-prompt.md` for the executor brief.

## Gates
No self-promotion to production. The technical owner approves shipping.
