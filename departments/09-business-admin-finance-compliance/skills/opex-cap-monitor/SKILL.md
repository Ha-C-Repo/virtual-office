---
name: opex-cap-monitor
description: Checks monthly operating cost per unit against minimum and maximum caps and flags exceptions.
---
# Operating-cost cap monitor

## When to use
Monthly close, and whenever an invoice above a threshold is logged.

## Steps
1. Read the cost register by unit and month: utilities, consumables, chemicals or media, substrates, lab testing, total.
2. Compare total to cap_min and cap_max for the unit. Set within_cap yes or no.
3. For any out-of-cap line, trace to source invoices; list missing documents.
4. Recommend nothing beyond the facts; the owner decides on action.

## Outputs
Opex table per unit and month; exceptions list.

## Gates
Procurement controls: purchases above the approval threshold need {{OWNER_ROLE}} approval before commitment. Never edit a past month; append a correction.
