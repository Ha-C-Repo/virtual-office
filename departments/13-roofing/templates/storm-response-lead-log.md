# Storm Response Lead Log

Event {{EVENT_ID}} | Date {{EVENT_DATE}} | Type {{EVENT_TYPE}} | Area {{SERVICE_AREA}} | Log owner {{LOG_OWNER}}

Daily capacity: inspections {{INSPECTIONS_PER_DAY}}, tarps {{TARPS_PER_DAY}}. Backlog limit {{MAX_BACKLOG_DAYS}} days. Status message approved by {{OWNER}} on {{DATE}}.

| Lead id | Received | Source | Address | Triage class (open roof or leak / inspection / information) | First response (minutes) | Assigned to | Scheduled | Tarp authorized (y/n) | Insured claim intended (y/n) | Outcome |
|---|---|---|---|---|---|---|---|---|---|---|
| {{LEAD_ID}} | {{RECEIVED_AT}} | {{SOURCE}} | {{PROPERTY_ADDRESS}} | {{TRIAGE_CLASS}} | {{MINUTES}} | {{ASSIGNEE}} | {{SCHEDULED_AT}} | {{YES_NO}} | {{YES_NO}} | {{OUTCOME}} |

## Daily summary
New {{NEW}} | Tarped {{TARPED}} | Inspected {{INSPECTED}} | Waiting {{WAITING}} | Median wait {{MEDIAN_WAIT}} | Pricing policy {{PRICING_POLICY}} (normal price book unless owner decides; legal limits checked; VERIFY)

## Compliance
Canvassing permits current {{YES_NO}} | Consent basis recorded {{YES_NO}} | Gate passed on messages {{YES_NO}}

Debrief notes after the event: {{DEBRIEF}}
