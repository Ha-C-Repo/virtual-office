# Appointment Confirmation

Draft only. Goes through the outbound gate and owner voice check, then the approval queue. Sent by a human. Use the channel the customer used, and only if consent for that channel is recorded.

Lead id: {{LEAD_ID}}   Channel: {{CHANNEL}}   Consent: {{GRANTED}}

Subject (email): {{FIRST_NAME}}, your visit on {{APPOINTMENT_DAY}}

{{FIRST_NAME}},

You are set for {{APPOINTMENT_DAY}} at {{APPOINTMENT_TIME}} at {{ADDRESS}}. We will have the {{YEAR}} {{MAKE}} {{MODEL}}, stock {{STOCK_NUMBER}}, pulled up and ready.

Price on the car: {{PRICE}}. Mileage: {{MILEAGE}}.

Please bring: your driver's license, proof of insurance{{TRADE_IN_CLAUSE}}.

If anything changes, call {{PHONE}}. Ask for {{SALES_ROLE}}.

{{SIGNATURE_BLOCK}}

## Before sending
- [ ] Unit is on the ground and front-line ready (check the unit record).
- [ ] Price matches the live listing.
- [ ] No payment, rate or approval promise in the message.
- [ ] Appointment logged in the pipeline (state APPOINTMENT) and a reminder set for the day before.
