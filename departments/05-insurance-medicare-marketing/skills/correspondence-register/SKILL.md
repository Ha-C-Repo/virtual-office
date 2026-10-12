---
name: correspondence-register
description: Per-counterparty communications log with action-required tracking and a pre-signature sweep.
---
# Correspondence register

## When to use
For each material communication with a carrier, upline, vendor, agent or lead-transfer partner.

## Steps
1. Log: ID, date, direction, from, to, medium, subject, reference, action required, response due, status, link to evidence.
2. At the monthly sweep, flag items past response-due as AT RISK.
3. Pre-signature sweep: before any agreement or amendment is signed, search the log for negotiated items missing from the final text and report them.
4. Log lead transfers and data-sharing consents here.

## Outputs
Register rows, overdue list, pre-signature discrepancy list.

## Gates
Append-only. Do not summarize what you have not read; cite the link.
