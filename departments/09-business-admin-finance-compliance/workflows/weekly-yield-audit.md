# Weekly Yield Audit (Monday ledger)

Agent: finance controller. Skill: `../skills/unit-yield-audit/SKILL.md`. Template: `../templates/weekly-yield-audit.md`.

## Steps
1. Confirm inputs are within freshness windows (`../skills/verify-dont-generate/SKILL.md`). Refuse stale data.
2. Pull active counts, 7-day gross sales, operating cost per unit.
3. Compute net yield and percent of target; show arithmetic.
4. Tag count status VERIFIED or ESTIMATED.
5. Reconcile register, physical, sales and cost; list gaps in both directions.
6. Apply the underperformance trigger; list units escalated.
7. Write yield rows to the register.
8. GATE: {{OWNER_ROLE}} reviews the exceptions list.

## Output
Audit table, gap list, escalation list, one-paragraph summary.
