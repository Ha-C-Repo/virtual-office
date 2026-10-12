---
name: investor-package
description: Assembles an investor package from verified financial and operating data in investor register.
---
# Investor package

## When to use
When {{OWNER_ROLE}} asks for a package for a prospective investor.

## Steps
1. Gather inputs: yield audits, reserve log, capex plan, inventory valuation (with count status), permit status, team structure.
2. Build per `../../templates/investor-package-outline.md`: summary, business model, traction metrics, unit economics, capital use, risks, compliance posture, team, ask.
3. Every figure cites source and date. Unsourced figures are labeled ESTIMATED or removed.
4. State assumptions for any projection. No promises of return.
5. Scrub with `../output-scrubber/SKILL.md`: no supplier names, internal cost detail, facility layout or staff pay data.
6. Mark confidentiality; recommend an NDA before sending.

## Outputs
Package draft and a separate internal note of what was withheld.

## Gates
{{OWNER_ROLE}} approves. Counsel reviews any offer terms.
