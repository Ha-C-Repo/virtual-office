# Follow-up Email: {{CONTEXT}}

Band: BRIEF   Doc number: {{DOC_NUMBER}}   Channel: email   Sender role: {{SENDER_ROLE}}

## Consent check (Step 0, required)
| Field | Value |
|---|---|
| Contact (masked) | {{MASKED_CONTACT}} |
| Channel consent row | {{REGISTER_ID}} |
| Consent basis | {{BASIS}} |
| Consent expiry | {{DATE}} |
| Opt-out checked | {{DATE}} |
If any row is missing, expired or revoked: no draft. Refusal note: {{WHAT_WOULD_CURE_IT}}.

## Draft
Subject: {{SUBJECT_5_TO_8_WORDS}}

Hello {{CONTACT_FIRST_NAME}},

{{ACKNOWLEDGE_THEIR_SPECIFIC_INQUIRY_AND_NAME_THE_ITEM}}

{{ONE_USEFUL_FACT_FROM_THE_RECORD_WITH_ACTUAL_PRICE_OR_STATUS}}

{{ONE_ASK}}

{{SIGNATURE_BLOCK}}
{{COMPANY}}   {{BUSINESS_ADDRESS}}   {{CONTACT_PHONE}}
To stop these emails, reply "stop" or use {{UNSUBSCRIBE_LINK}}.

## Cadence
| Touch | Timing | Channel | Status |
|---|---|---|---|
| Welcome | within 24 hours | email | {{STATUS}} |
| Next | at most one per week | email | {{STATUS}} |

## Internal note (-INT)
Consent basis and expiry: {{BASIS_EXPIRY}}. Promises made in this message: {{PROMISES_OR_NONE}} (logged on the promise list: {{YES_NO}}). Sweep date: {{DATE}}.
