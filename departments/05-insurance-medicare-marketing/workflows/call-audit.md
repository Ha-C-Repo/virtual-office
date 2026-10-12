# Call Audit Workflow

Skill: `../skills/call-compliance-audit/SKILL.md`.

## Steps
1. Select calls: random sample plus any flagged call.
2. Obtain the transcript; machine transcripts are medium confidence.
3. Run the deterministic transcript checker (sales mode for sales calls).
4. Judgment checks: lawful to place, SOA valid and in scope, disclaimer verbatim with real counts before benefit talk, claim accuracy, election-period validity, transfer disclosure.
5. Tag findings by confidence.
6. Write the audit record (`../templates/call-audit-record.md`).
7. Escalate to the principal the same day for any BLOCK-level finding.
8. Update the retention tracker; run the monthly list of recordings within 12 months of retention end.
9. Agent coaching is delivered by the principal or designee, not by the AI.

## Gates
MANUAL items stay with a human. No recording deleted before retention end. The stricter retention overlay wins.
