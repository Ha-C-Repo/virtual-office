---
name: call-compliance-audit
description: Audit call transcripts against marketing and sales call rules, and track recording retention by regime.
---
# Call compliance audit

## When to use
For sampled or flagged calls, and monthly for the retention tracker.

## Steps
1. Obtain the transcript. Machine transcripts are medium confidence at best.
2. Run the deterministic transcript checker (sales-call mode for sales calls): disclaimer variants recognized and positioned before the first benefit keyword, prohibited phrases, spoken SSN, recording disclosure.
3. Judgment checks: call lawful to place; SOA valid and scope respected; disclaimer verbatim with real organization and plan counts; claim accuracy; election-period validity; transfer disclosure.
4. Tag findings high, medium or low confidence. Escalate to {{PRINCIPAL_ROLE}} the same day.
5. Retention tracker: record call date, regime, retention end, storage location, format. Older regime keeps the longer period; the newer regime minimum is 6 years (audio years 1 to 3, then audio or transcript years 4 to 6); the stricter overlay wins. List items within 12 months of retention end monthly.

## Outputs
Call audit record (`../../templates/call-audit-record.md`) and escalations.

## Gates
MANUAL items stay with a human reviewer. No recording is deleted before retention end.
