---
name: ai-guardrails-gate
description: Rule gate on AI output before customer delivery. Blocks invented facts, license numbers, models and completion guarantees.
---
# AI Guardrails Gate

## When to use
Any AI-generated text, estimate or proposal that a customer or their customer will see.

## Checks
1. No invented license numbers, certifications, insurance details or registration ids.
2. No invented product models, part numbers or specifications; use only items from the catalog.
3. No guarantees of completion dates or outcomes; use ranges and assumptions.
4. Quantities and prices trace to a source (catalog, takeoff, rate table) or are labeled estimates.
5. No personal data from other tenants.
6. Legal, safety or engineering advice carries a "consult a licensed professional" note where relevant.
7. Tone follows the tenant's vertical config.

## Result
PASS (silent), AUTO-FIX minor issues, or BLOCK with the reason shown to the human reviewer.

## Gates
BLOCK means a human reviews before anything is delivered.
