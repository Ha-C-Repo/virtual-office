---
name: permit-tracker
description: Permit register with expiry calendar and renewal flags.
---
# Permit tracker

## When to use
On any permit event (issued, renewed, amended, expired) and in the weekly compliance review.

## Steps
1. Record per permit: authority, permit, number, cost, term, issued, expires, status.
2. Compute days to expiry. Flag at 90, 60 and 30 days.
3. Expired permits: status EXPIRED, stop affected activity, notify {{OWNER_ROLE}}.
4. Link each permit to the trade documents and sales it governs.

## Outputs
Register rows (`../../templates/permit-register.md`) and the renewal calendar.

## Gates
Never invent a number or date; flag the gap. Renewal submissions are approved by {{OWNER_ROLE}}.
