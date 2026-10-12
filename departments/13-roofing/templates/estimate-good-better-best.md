# Estimate: Good / Better / Best

Estimate {{ESTIMATE_ID}} | Customer {{CLIENT_NAME}} | Property {{PROPERTY_ADDRESS}} | Date {{DATE}} | Valid through {{VALID_THROUGH}}
Prepared by {{ESTIMATOR}} | Quantities from `takeoff-sheet.md` {{TAKEOFF_REF}}

## Tier definitions
| | Good | Better | Best |
|---|---|---|---|
| Product line | {{PRODUCT_GOOD}} | {{PRODUCT_BETTER}} | {{PRODUCT_BEST}} |
| Color | {{COLOR}} | {{COLOR}} | {{COLOR}} |
| Underlayment | {{UNDERLAY_GOOD}} | {{UNDERLAY_BETTER}} | {{UNDERLAY_BEST}} |
| Ventilation work | {{VENT_GOOD}} | {{VENT_BETTER}} | {{VENT_BEST}} |
| Warranty (workmanship) | {{WW_GOOD}} | {{WW_BETTER}} | {{WW_BEST}} |
| Manufacturer / system warranty | {{MW_GOOD}} | {{MW_BETTER}} | {{MW_BEST}} (certified installer required; VERIFY) |
| Price | {{PRICE_GOOD}} | {{PRICE_BETTER}} | {{PRICE_BEST}} |

## Line items (per tier)
| Code | Description | Qty | Unit | Unit price | Amount |
|---|---|---|---|---|---|
| {{ITEM_CODE}} | {{DESCRIPTION}} | {{QTY}} | {{UNIT}} | {{UNIT_PRICE}} | {{AMOUNT}} |

Standard lines: tear-off ({{LAYERS}} layers), deck allowance, replacement decking unit price, ice barrier (where required), underlayment, drip edge, starter, shingles, ridge, vents, pipe boots, flashing, chimney or skylight work, cleanup and magnet sweep, disposal, permit.

## Allowances and change triggers
Hidden decking at unit price {{DECKING_UNIT_PRICE}}; code-required items found on inspection; ventilation correction.

## Internal only (remove before customer copy)
Direct cost {{DIRECT_COST}} | Margin {{MARGIN_PCT}} (target {{TARGET_GROSS_MARGIN}}) | Markup equivalent {{MARKUP_PCT}} | Command: `python ../harnesses/job_cost.py price --cost {{COST}} --margin {{MARGIN_PCT}}`

Approved by {{OWNER}} on {{DATE}}.
