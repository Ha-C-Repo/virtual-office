# Review Request Message

Sent after funding and delivery, to every customer, not a selected few. Never gate the request on satisfaction (no "only if you are happy"). Never offer anything in exchange. Goes through the outbound gate (`../workflows/02-sales-outbound-message.md`): consent ledger first, then channel content gate, then approval queue. Email needs a physical address and an opt-out; text needs recorded consent.

Channel: {{EMAIL_OR_TEXT}}   Consent state: {{GRANTED}}   Deal: {{DEAL_REF}}   Send after: {{DATE}}

## Email
Subject: {{FIRST_NAME}}, how did we do?

{{FIRST_NAME}},

Thank you for buying your {{YEAR}} {{MODEL}} from {{DEALERSHIP}}. How is it treating you?

If you have a minute, an honest review helps the next buyer. This link goes straight to our profile: {{REVIEW_LINK}}

If something is not right, call me first at {{PHONE}} and I will handle it.

{{OWNER_NAME_ROLE}}
{{DEALERSHIP}}, {{ADDRESS}}
{{UNSUBSCRIBE_LINE}}

## Text (only with recorded consent)
{{FIRST_NAME}}, {{OWNER_ROLE}} at {{DEALERSHIP}}. How is the {{MODEL}}? An honest review helps: {{REVIEW_LINK}} Reply STOP to opt out.

## Link source
Generate the link or QR code from the verified business profile only. A QR copy for the counter goes in the delivery packet.
