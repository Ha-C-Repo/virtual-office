# 30-Day Check-In Record

Scheduled for every delivered unit. Completion is a KPI. A problem found here is routed the same day; a promise made is added to a we-owe.

Deal: {{DEAL_REF}}   Unit: {{STOCK_NUMBER}}   Delivered: {{DELIVERY_DATE}}   Check-in due: {{DUE_DATE}}   Customer: {{CUSTOMER_NAME}}
Contact method with recorded consent: {{CHANNEL}}   Done by: {{ROLE}}

## Draft message (approval queue first)
{{FIRST_NAME}}, it has been a month with your {{YEAR}} {{MODEL}}. How is it running? Anything we should look at? Call {{PHONE}} or reply here.

## Record
| Item | Result |
|---|---|
| Reached customer | {{YES_NO}} on {{DATE}} |
| Vehicle running as expected | {{YES_NO}} |
| Open we-owe items fulfilled | {{YES_NO}} ({{WO_NUMBER}}) |
| Issues reported | {{ISSUES}} |
| Goodwill or warranty repair needed | {{YES_NO}} |
| Titles, tags and registration received | {{YES_NO}} |
| Review requested | {{YES_NO}} (`reputation-review-request.md`) |
| Next retention touch | {{DATE_AND_TYPE}} |

## Routing
- Repair issue: open a repair authorization or goodwill repair (`service-we-owe.md`).
- Allegation of concealment, safety or title problem: stop, escalate to {{OWNER}} the same day (`reputation-escalation-note.md`).
- Not reached after 2 tries on different days: log and close, do not escalate channel without consent.
