# Temp Tag Log: {{DEALERSHIP}}

Temp tag issuance and expiry are enforced aggressively. Every tag is logged when issued. Tag stock is counted weekly against this log. Never backdate.

| Tag id | Issued date | Expiry date | Deal | Unit (stock / VIN) | Buyer (role: buyer; name in jacket only) | Issued by | Permanent plate / title application filed | Date filed | Warning level | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| {{TAG_ID}} | {{DATE}} | {{DATE}} | {{DEAL_REF}} | {{STOCK_NUMBER}} / {{VIN}} | buyer | {{ROLE}} | {{YES_NO}} | {{DATE}} | {{LEVEL}} | ACTIVE / FILED / EXPIRED / VOIDED |

## Rules
1. Expiry less than or equal to 3 days with no filing: URGENT, escalate to {{OWNER}}.
2. Expiry less than or equal to 7 days with no filing: THIS WEEK.
3. Expired with no filing: stop, notify the buyer through the approved channel, and escalate.
4. Voided or spoiled tags are logged with a reason.
5. Weekly tag stock count: {{COUNT_ON_HAND}} on hand vs {{COUNT_EXPECTED}} expected. Difference: {{DIFF}}.
