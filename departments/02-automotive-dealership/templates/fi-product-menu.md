# Product Menu: {{DEALERSHIP}}

Transparent pricing. Every product shows its price and term, whether it is optional, and that declining it does not affect the credit decision. Prices come from the owner-locked product price list; the model never sets them. Do not finance an add-on without checking the covered-borrower structure rule first (`../skills/fi-military-lending/SKILL.md`).

Deal: {{DEAL_REF}}   Unit: {{STOCK_NUMBER}}   Date: {{DATE}}   Customer: {{CUSTOMER_NAME}}

| Product | What it covers | What it does not cover | Price | Term / miles | Provider (category) | Accept / Decline (initials) |
|---|---|---|---|---|---|---|
| {{PRODUCT_1}} | {{COVERS_1}} | {{EXCLUDES_1}} | {{PRICE_1}} | {{TERM_1}} | {{PROVIDER_1}} | {{INITIALS}} |
| {{PRODUCT_2}} | {{COVERS_2}} | {{EXCLUDES_2}} | {{PRICE_2}} | {{TERM_2}} | {{PROVIDER_2}} | {{INITIALS}} |
| {{PRODUCT_3}} | {{COVERS_3}} | {{EXCLUDES_3}} | {{PRICE_3}} | {{TERM_3}} | {{PROVIDER_3}} | {{INITIALS}} |

## Payment effect (calculator output)
| Scenario | Products included | Payment | Months | APR |
|---|---|---|---|---|
| Base | None | {{PAYMENT}} | {{TERM_MONTHS}} | {{APR}} |
| Selected | {{SELECTED}} | {{PAYMENT}} | {{TERM_MONTHS}} | {{APR}} |

Disclosure block (shown whenever any payment appears): down payment {{CASH_DOWN}}; payment and months as above; APR {{APR}}; the rate may increase after approval.

Warranty or service-contract terms must match the buyer's guide: {{WARRANTY_TERMS}}.
Customer acknowledgment: {{BUYER_SIGNATURE}} {{DATE}}
