---
name: spec-driven-lifecycle
description: Six-stage gate (constitution check, specify, clarify, plan, tasks, implement) required before any structural code change.
---
# Spec-Driven Lifecycle

## When to use
Any new feature, schema change, API change, integration or change to the AI behavior layer. Not needed for typo fixes or copy edits.

## Inputs
Feature request, the constitution (numbered non-negotiable engineering rules), existing spec index.

## Steps
1. **Constitution check.** List each principle the feature touches (tenant isolation, secrets, flags default off, logging, cost telemetry). Note conflicts. A conflict stops the work until the principal resolves it.
2. **Specify.** Fill `../../templates/spec.md`: problem, users, behavior, non-goals, data touched, sources.
3. **Clarify.** List every UNKNOWN as a question for the owner. Do not proceed with assumptions. Record answers in a decision record.
4. **Plan.** Architecture, data model changes, migration order, flags, rollout, rollback, test approach.
5. **Tasks.** Small numbered tasks, each independently reviewable, each with acceptance criteria.
6. **Implement.** One task at a time using `../code-quality-loop/SKILL.md`; ship behind a flag, default OFF.

## Outputs
A spec file with a status line (draft, clarify resolved, plan-ready, implemented behind flag, gates open) and an updated spec index.

## Gates
- No structural code before step 5 is complete.
- Technical owner approves the plan and the shipped code.
- Principal approves anything customer-visible.
