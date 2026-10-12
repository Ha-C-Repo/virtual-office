# Lead Acknowledgment Reply

Draft only until the owner trusts the voice. Target: acknowledged inside the speed-to-lead target for the channel ({{TARGET_MINUTES}} minutes in hours). Name the actual vehicle and the actual price from the live record. Never promise financing, approval, trade value or availability that is not confirmed. Through the outbound gate and approval queue (`../workflows/02-sales-outbound-message.md`).

Lead id: {{LEAD_ID}}   Source: {{SITE_FORM / SOCIAL_MESSAGE / PORTAL / PHONE_LOG / WALK_IN}}   Received: {{DATE_TIME}}   Deduped against: {{CONTACT_REF}}
AI disclosure: if this reply comes from a conversational AI surface, the fixed disclosure template goes in the first message (`compliance-ai-disclosure-register.md`).

Subject: {{FIRST_NAME}}, the {{YEAR}} {{MODEL}} is here

{{FIRST_NAME}},

Thanks for asking about the {{YEAR}} {{MAKE}} {{MODEL}}, stock {{STOCK_NUMBER}}. It is on our lot now. It has {{MILEAGE}} miles and the price is {{PRICE}}.

{{ONE_SPECIFIC_FACT_FROM_RECORD}}

Want to see it? I can have it ready {{PROPOSED_DAY_1}} or {{PROPOSED_DAY_2}}. Reply with a time or call {{PHONE}}.

{{SIGNATURE_BLOCK}}

## Checks
- [ ] Vehicle and price match the live record today.
- [ ] Customer's actual question answered in the first two lines.
- [ ] No payment or rate unless the full disclosure block is attached.
- [ ] Voice check passed. Under 120 words.
- [ ] Logged in the pipeline (state LEAD) with timestamp for the speed-to-lead timer.
