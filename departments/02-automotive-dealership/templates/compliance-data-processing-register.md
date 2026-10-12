# Data Processing Register: {{DEALERSHIP}}

Owner: Compliance (08). One row per customer document received. Credit applications, licenses, pay stubs, SSN and bank details never go through unpaid AI APIs or consumer chat.

| Deal / stock | Document type | Received | Contains SSN / DOB / income (Y/N each) | Storage location (specific path or system) | Retention expiry | Destroyed (date) | Destruction certificate ref | Sub-processors touched | No-training confirmed |
|---|---|---|---|---|---|---|---|---|---|
| {{DEAL_REF}} / {{STOCK_NUMBER}} | {{DOC_TYPE}} | {{DATE}} | {{SSN}} / {{DOB}} / {{INCOME}} | {{STORAGE_LOCATION}} | {{RETENTION_DATE}} | {{DATE_OR_OPEN}} | {{CERT_REF}} | {{SUBPROCESSORS}} | {{YES_NO}} |

## Rules
1. "The project folder" is not a storage location. Name the system and path.
2. A sub-processor without a confirmed no-training term is not used for customer data.
3. Destruction on solid-state storage is a cryptographic erase with a certificate and file hash.
4. Rows past retention expiry and not destroyed appear on the monthly scorecard.
