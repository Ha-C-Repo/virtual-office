# Comp Grid: {{STOCK_NUMBER}}

Pricing is deterministic. A minimum of three sourced comps is required; fewer is a refusal, not a guess. The model never does the arithmetic: the calculator does, and the audit ref is recorded.

Unit: {{YEAR}} {{MAKE}} {{MODEL}} {{TRIM}}   Mileage: {{MILEAGE}}   Grade: {{GRADE}}   Date: {{DATE}}

| # | Comp source (category) | Date pulled | Year / trim | Mileage | Asking price | Distance or market | Notes |
|---|---|---|---|---|---|---|---|
| 1 | {{COMP_SOURCE}} | {{DATE}} | {{YEAR_TRIM}} | {{MILEAGE}} | {{PRICE}} | {{MARKET}} | {{NOTES}} |
| 2 | {{COMP_SOURCE}} | {{DATE}} | {{YEAR_TRIM}} | {{MILEAGE}} | {{PRICE}} | {{MARKET}} | {{NOTES}} |
| 3 | {{COMP_SOURCE}} | {{DATE}} | {{YEAR_TRIM}} | {{MILEAGE}} | {{PRICE}} | {{MARKET}} | {{NOTES}} |

Named book value: {{BOOK_NAME}}, dated {{BOOK_DATE}}: {{BOOK_VALUE}}

## Calculator output
- Corridor: {{CORRIDOR_LOW}} to {{CORRIDOR_HIGH}}
- Recommended price: median of comps, blended with named book value if present: {{RECOMMENDED_PRICE}}
- Floor: the higher of 8 percent below recommendation or 5 percent below corridor minimum: {{FLOOR_PRICE}}
- Grade is recorded but never moves the arithmetic.
- Calculator audit ref: {{CALC_AUDIT_REF}}

## Four sanity gates (`../skills/inventory-pricing-sanity-check/SKILL.md`)
| Gate | Result (PASS / CAUTION / FLAG / BLOCK) | Note |
|---|---|---|
| 1 Price vs comp corridor (no corridor = CAUTION) | {{RESULT}} | |
| 2 Mileage sourced (none = BLOCK, low-tier = FLAG, mid-tier = CAUTION) | {{RESULT}} | |
| 3 Price vs named, dated book value | {{RESULT}} | |
| 4 Package completeness | {{RESULT}} | |

Confidence score: start 100, minus 40 per BLOCK, 20 per FLAG, 10 per CAUTION = {{SCORE}}.
A markdown simulation for aged units is a report. A human decides.
