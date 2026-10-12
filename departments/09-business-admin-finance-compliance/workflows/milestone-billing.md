# Milestone Billing

Agent: billing and procurement clerk. Skill: `../skills/ar-milestone-billing/SKILL.md`. Template: `../templates/invoice.md`.

## Steps
1. Trigger: a milestone is reached (deposit, signing, material arrival, progress against the schedule of values).
2. Confirm the trigger with a document (signed contract, delivery receipt, progress report).
3. Draft the invoice from the contract terms.
4. GATE: {{OWNER_ROLE}} approves and sends.
5. Weekly overdue sweep: reminder drafts at 7, 14 and 21 days.
6. Update status: draft, sent, paid, overdue.
7. Monthly aging report to {{OWNER_ROLE}}.
