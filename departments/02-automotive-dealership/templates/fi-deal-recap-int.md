# Deal Recap -INT (internal only): {{DEALERSHIP}}

Twin of `fi-deal-recap.md`. Never shown to or sent to the customer. Locked deal economics are owner-set; a value of zero means "not yet set" and blocks the calculation. All arithmetic comes from the calculator, with the audit log reference recorded below.

Deal reference: {{DEAL_REF}}   Unit: {{STOCK_NUMBER}}   VIN: {{VIN}}   Date: {{DATE}}
Calculator audit log ref: {{CALC_AUDIT_REF}}
Prepared by: {{FI_MANAGER}}   Owner review: {{OWNER}}

## Unit economics
Acquisition cost: {{ACQUISITION_COST}}
Pack: {{PACK}}
Recon spend to date (by grade budget {{RECON_BUDGET}}): {{RECON_SPEND}}
Floorplan interest accrued ({{FLOORPLAN_RATE}} with {{FLOORPLAN_LENDER}}): {{FLOORPLAN_INTEREST}}
Days in inventory: {{DAYS_IN_INVENTORY}}
Total cost basis: {{TOTAL_COST}}

## Gross
Selling price: {{PRICE}}
Front gross: {{FRONT_GROSS}}   Target: {{FRONT_GROSS_TARGET}}
Back gross (products): {{BACK_GROSS}}   Target: {{BACK_GROSS_TARGET}}
Reserve: {{RESERVE}}
Total gross: {{TOTAL_GROSS}}

## Structure checks
- Price vs corridor: {{WITHIN_OUTSIDE}} (corridor low {{CORRIDOR_LOW}}, high {{CORRIDOR_HIGH}})
- Minimum down for credit tier {{CREDIT_TIER}}: {{MIN_DOWN}}; actual {{CASH_DOWN}}
- Loan-to-value: {{LTV}}   Payment-to-income: {{PTI}}   Negative equity rolled: {{NEG_EQUITY}}
- Covered-borrower check recorded: {{YES_NO}} (date {{DATE}}; result {{COVERED / NOT_COVERED / INDETERMINATE}}; indeterminate is treated as covered)
- Exclusion-voiding structure flagged (cash advanced beyond price, financed add-ons): {{YES_NO}}
- Adverse action required: {{YES_NO}}

## Sign-off
Owner approves the number: {{OWNER_INITIALS}} {{DATE}}
Confidence tier of inputs: {{HIGH_MED_LOW}}. Open flags: {{FLAGS}}.
