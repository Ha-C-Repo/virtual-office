---
name: carrier-contracting-tracker
description: Source of record for appointment and ready-to-sell status by agent, carrier and plan year.
---
# Carrier contracting tracker

## When to use
Whenever a carrier paperwork event, appointment notice or ready-to-sell notice arrives, and before any statement that an agent can sell a carrier's product.

## Inputs
Carrier paperwork, carrier notices, portal confirmations (reviewed by a human).

## Steps
1. Find or open the row for agent x carrier x plan year.
2. Set status: not started, submitted, appointed, certified, RTS (ready to sell), terminated.
3. Record evidence path, writing number (as a placeholder in shared docs), and updated date.
4. Append the change to notes; never overwrite history.
5. When asked "can agent X sell carrier Y for year Z", answer only from the row. No row or no evidence means UNVERIFIED.

## Outputs
Updated row, status log line, answer with citation to the row.

## Gates
Carrier names appear on outward material only per appointment and approval status. Never fabricate an appointment. Field list in `../../knowledge/schemas.md`.
