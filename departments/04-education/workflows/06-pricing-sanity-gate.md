# 06 Pricing Sanity Gate

Owner: product-manager | Approver: {{OWNER}}

## Steps
1. Owner supplies pricing inputs with named sources (`../templates/business-config.md`). Unmeasured inputs are marked UNMEASURED.
2. Run `../skills/pricing-sanity-check/SKILL.md` using a script for all arithmetic.
3. Evaluate against heavy users (tail), not the mean.
4. GATE: negative margin = FAIL. Free exposure above the owner's ceiling = FAIL. Ceiling unset = BLOCKED-ON-CEILING.
5. If pass, owner approves and the config is updated with date and approver.
6. Public copy is checked to match the config.

## Outputs
Economics table, verdict, approved config.
