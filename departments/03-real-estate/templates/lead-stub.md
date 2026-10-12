# Lead Stub

One small file per lead. Name it `{{LEAD_ID}}-{{DATE_STAMP}}.txt`. Lead IDs are sequential. Key-value lines only.

```
Lead ID: {{LEAD_ID}}
Name: {{CLIENT_NAME}}
Phone: {{CONTACT_PHONE}}
Email: {{CONTACT_EMAIL}}
Property interest: {{PROPERTY_INTEREST}}
Source: {{LEAD_SOURCE}}
Consent: {{CONSENT_CHANNELS}} on {{CONSENT_DATE}}
Notes: {{NOTES}}
```

Rules:
- Record consent only where it was given.
- Opt-outs are recorded in the consent ledger and apply to every channel.
- Do not store sensitive data beyond what is needed to serve the lead.
