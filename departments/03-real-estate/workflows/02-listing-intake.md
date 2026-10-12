# 02 Listing Intake

Owner: listing-cma-analyst | Approver: {{PRINCIPAL_AGENT}}

## Steps
1. Receive an address, listing reference or document folder for {{PROPERTY_ADDRESS}}.
2. If only an address or portal reference exists, run `../skills/portal-listing-intake/SKILL.md`. Pull only what licensing allows; otherwise ask the agent to export or upload. Public-web data is LOW confidence and cannot set property facts, comps or valuations.
3. Create the listing folder: source documents, working, final. Video and tour output never write into the listing folder directly.
4. Classify documents (`../skills/listing-doc-classifier/SKILL.md`).
5. Produce the gap list with who is asked for what.
6. GATE: status COMPLETE required to proceed to `01-cma-listing-presentation.md` or `03-tour-build.md`.
7. Store intake record with per-field source and confidence.

## Outputs
Listing folder, classification table, gap list, intake record.
