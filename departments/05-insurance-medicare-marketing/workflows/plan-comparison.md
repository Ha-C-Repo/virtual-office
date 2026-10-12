# Plan Comparison Workflow

Skill: `../skills/carrier-comparison/SKILL.md`.

## Steps
1. Agent gathers client inputs: medication list transcribed exactly, providers, pharmacy, budget.
2. Confirm SOA is active for the products to be discussed (`../skills/soa-register/SKILL.md`).
3. Retrieve benefits live from approved sources. Record source and retrieval date.
4. Fill the twelve-factor worksheet with arithmetic shown.
5. Validate the election period (`election-period-validation.md`).
6. Agent completes the worksheet with the client.
7. The AI never renders the verdict.

## Gates
No cached benefits. Carrier names per appointment status only. Worksheet is internal unless the agent hands it to the client.
