---
name: skill-promotion-pipeline
description: How a repeated task becomes a template, then a skill, then an always-loaded skill. Includes the tests and approvals at each stage and the audit after any skill edit. Use when a task recurs three or more times, or when proposing or editing a skill.
---

# Skill promotion pipeline

## When to use
A task has been done three or more times by hand; someone proposes a new skill; a skill is edited; a quarterly skills audit is due.

## Stages
1. Observation. Log each occurrence: request, inputs, steps taken, output, defects. Keep the log in the decision log or the department's notes.
2. Template. At three occurrences, extract the stable parts into a template in `templates/`. Never create a new always-loaded skill first. Templates load on demand.
3. Draft skill. If the template needs steps and gates, write `skills/<name>/SKILL.md` using the skeleton: When to use, Inputs, Steps, Outputs, Gates, Anti-patterns. Add `../../templates/skill-definition.md` as the starting file.
4. Test. Run the draft on two real past cases and one deliberately bad case. The skill must pass the good cases and fail the bad one in the right way.
5. Review. QA editor checks structure and voice; compliance reviewer checks gates and claims; the human owner approves.
6. Promote. Add the skill to the department README list and to the routing table if it needs a trigger. Announce with a changelog line.
7. Always-loaded status is granted only to skills that apply to nearly every task (constitution, bands, voice). Everything else loads by trigger.
8. Audit. After any skill edit, run a skills audit: every phrase a skill calls "blocked" must be blocked somewhere; every referenced path exists; no two skills overlap without a stated boundary.
9. Retire. Unused skills are archived, not deleted, with a reason.

## Inputs
Occurrence log, draft skill, test cases.

## Outputs
Template or skill file, test record, changelog line, updated README and routing table.

## Gates
- Three-occurrence rule before promotion.
- Constitution check before approval.
- Amendments to governance skills follow the amendment protocol.
- Token discipline: keep the always-loaded set small; large reference material goes to a retrieval source, not into a skill.

## Anti-patterns
A skill written from one case. A skill that duplicates another. A skill with gates but no way to fail.
