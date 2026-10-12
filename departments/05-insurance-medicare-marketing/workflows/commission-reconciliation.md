# Commission Reconciliation Workflow

Agent: commission reconciler. Skill: `../skills/commission-reconciliation/SKILL.md`.

## Steps
1. Receive statement. Record row count and period from the statement itself.
2. Normalize columns to the standard schema; log mapping decisions.
3. Match lines to the comp grid on carrier x product x level (exact = high, fuzzy = medium).
4. Compute expected from the grid only; compute signed variance.
5. Classify MATCH, VARIANCE, UNMATCHED with confidence and reason.
6. FMV cap check on Medicare Advantage and Part D lines; renewal at half of initial; flag exceedances; verify the cap table year.
7. Aggregate by carrier and writing agent; integrity check on the sum of variances.
8. Produce the report and `-INT` memo (`../templates/commission-reconciliation-report.md`) with masked IDs.
9. Human review of all flagged lines.
10. Where a variance stands, draft a commission variance notice (`../skills/contract-notice/SKILL.md`).

## Gates and sign-off
Gate: never fill a missing grid rate or cap. Sign-off: principal reviews the human review list; no dispute is raised without principal approval. Commission data stays internal.
