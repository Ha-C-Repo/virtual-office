# 03 Spec-Driven Lifecycle

Owner: product-manager | Approver: {{OWNER}}

## Stages
constitution -> specify -> clarify -> plan -> tasks -> implement

## Steps
1. Constitution: Tier 1 rules are fixed. Any change follows the amendment protocol and needs owner approval.
2. Specify: write the spec from `../templates/product-spec.md`.
3. Clarify: list open questions; owner answers; no assumption closes a question.
4. Run `../skills/spec-completeness-check/SKILL.md` and reconcile against the request.
5. Classify maturity (`../skills/spec-maturity-classifier/SKILL.md`). GATE: only final or frozen specs are implemented.
6. Plan: architecture notes, dependency justifications.
7. Tasks: small, testable, mapped to AC numbers.
8. Run `../skills/scope-creep-detector/SKILL.md` on each new request.
9. Implement with small diffs; plan before code; independent fresh-session review one concern at a time; test-feedback-repair loop.
10. SIGN-OFF: owner accepts against the acceptance criteria.

## Outputs
Final spec, task list, reconciliation table, change log entries.
