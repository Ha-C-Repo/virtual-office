# Workflow: Spec-Driven Development

Owner: `solutions-architect`. Approver for code: technical owner.

1. Intake the request. Log it in the spec index with status draft.
2. Constitution check (`../skills/spec-driven-lifecycle/SKILL.md`). **Gate:** any conflict goes to the principal.
3. Specify using `../templates/spec.md`. If it involves location, biometrics, minors, content or currency, run `../skills/trust-safety-design-review/SKILL.md`.
4. Clarify. List UNKNOWNs; get answers from owners; record decisions. **Gate:** no unresolved UNKNOWN affecting data or security.
5. Plan. Include flag, rollout, rollback, AI cost estimate. **Gate (sign-off):** technical owner approves the plan.
6. Tasks. Small, testable.
7. Implement with `../skills/code-quality-loop/SKILL.md`; independent review by `engineering-reviewer`.
8. Promote per `environment-promotion.md`.
9. Close: update the spec status, deploy record, handoff.
