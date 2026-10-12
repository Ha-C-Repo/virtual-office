# Workflow: Customer Onboarding and Config Capture

1. Confirm signed agreement or trial agreement is on file.
2. Create or update the customer config (`../templates/customer-config.md`).
3. Select the vertical config; list default job types, scope, exclusions, line items, compliance framework, pricing model.
4. Enable modules for the tier. **Gate:** technical owner confirms tenant created with isolation checks passed.
5. Import data. Verify counts against the customer's source.
6. Train key users; schedule check-ins at day {{DAY_ONE}}, {{DAY_SEVEN}}, {{DAY_THIRTY}}.
7. Define the activation event (first real workflow completed). Track time to activation.
8. If location or other sensitive features are used, deliver the consent notice (`../templates/location-consent-notice.md`) and record consent.
9. Hand the account to customer success.
