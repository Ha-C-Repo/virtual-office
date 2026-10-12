---
name: service-call-leak-triage
description: Triage leak and callback calls, decide emergency tarping, assign a visit and record the cause and warranty position.
---
# Service Call and Leak Triage

## When to use
Any reported leak, callback or damage on an existing or completed roof.

## Inputs
Caller report, address, job history and warranty register, weather, photos from the caller.

## Steps
1. Classify: **emergency** (active water entry, open roof, storm damage), **urgent** (stain, intermittent leak), **routine** (cosmetic, question). Target response by class ({{SERVICE_RESPONSE_TARGET}}).
2. Safety advice to the caller: protect belongings, avoid ceilings with water, stay off the roof, turn off power if water reaches fixtures or lights. Do not advise them to climb.
3. Check job history: our roof (workmanship), other contractor's roof (not covered), storm event (insurance route), maintenance issue.
4. Emergency tarp: get written authorization (`../../templates/tarp-authorization.md`); photograph before and after; keep receipts. For an insured loss attach to the claim file.
5. Create a ticket (`../../templates/service-ticket.md`).
6. Visit and find the cause: flashing, penetration, fastener, ventilation condensation, ice damming, gutter overflow, siding or window leaks that are not roof related. Photos and moisture notes.
7. Determine cause and covered status as `covered`, `not covered`, or `undetermined`. State reasons from the warranty form. Owner decides goodwill.
8. Repair or quote; close the ticket with photos; update the warranty log.

## Outputs
Triage class, tarp authorization, ticket, findings, resolution log.

## Gates
- Never admit liability or deny coverage in the first call.
- Owner approves goodwill repairs and any cost to the customer.
- Tarp work obeys fall protection rules (`../fall-protection-plan/SKILL.md`).
- Run `../deductible-and-inducement-gate/SKILL.md` on any message about insurance.
