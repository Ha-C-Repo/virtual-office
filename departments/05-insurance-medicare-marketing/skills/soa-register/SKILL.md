---
name: soa-register
description: Scope of Appointment tracking with validity and retention clocks.
---
# Scope of Appointment register

## When to use
Whenever a beneficiary agrees to the products to be discussed in a personal appointment, and before any appointment is held.

## Steps
1. Record the SOA event: masked beneficiary ID, products scoped, date agreed, method, appointment date.
2. Compute validity end (12 months from agreement) and retention end (10 years).
3. Status: active, expired or consumed.
4. Before any appointment, confirm an active SOA exists that covers the products to be discussed. If the scope is exceeded, a new SOA is required.
5. Record evidence path and confidence tag.

## Outputs
Register row. Monthly list of rows near expiry or retention end.

## Gates
Append-only; no deletion before retention end. Beneficiary identity masked. No SOA, no personal appointment. Fields in `../../knowledge/schemas.md`.
