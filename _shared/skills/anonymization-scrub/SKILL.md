---
name: anonymization-scrub
description: Procedure for removing names, contact details, identifiers, entity-tied amounts and secrets from any text, replacing them with consistent placeholders. Use before storing material in the office, before sharing outward, and when building templates from real documents.
---

# Anonymization scrub

## When to use
Turning a real document into a template; ingesting source material; preparing an outward copy; closing a build.

## Rules
- Remove person, company, brand, product, client, project, book, character and location names.
- Remove emails, phones, addresses, URLs, domains, handles.
- Remove license, policy, permit, account, VIN, tax and other IDs.
- Remove entity-tied dollar amounts; keep formulas and structures.
- Remove secrets and never reproduce them.
- Replace software and AI vendors with categories.
- Public regulations and standards may be named.
- Use roles: "the owner/operator", "the principal".
- Placeholder form: `{{UPPER_SNAKE_CASE}}`. Reuse tokens consistently.

## Steps
1. Pattern scan: at-signs, domain patterns, long digit groups, currency symbols, long random strings, capitalized multi-word names.
2. Manual read for names the patterns miss.
3. Replace, keeping meaning. Make one token per concept and reuse it.
4. Re-scan the whole file.
5. Record the pass in the changelog without the removed values.

## Outputs
Scrubbed file, replacement count by type, confirmation line.

## Gates
Secrets present means BLOCK and report location only. Unresolved ambiguity means ask.

## Anti-patterns
Replacing a name with a different real-looking name. Leaving a name in a filename or heading. Writing the original value in the log.
