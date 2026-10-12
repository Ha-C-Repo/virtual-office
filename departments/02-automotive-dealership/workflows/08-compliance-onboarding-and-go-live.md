# 08 Compliance: Onboarding Interview and Go-Live

Owner: Compliance agent with {{OWNER}}. One question at a time. Never invent an answer. Dealer identity lives in one profile; a missing required field blocks output (no defaults). Keep jurisdiction law as the standard; parameterize county, market and nearby installations.

## Interview (record each answer in the dealer profile)
1. License number and expiry ({{LICENSE_NUMBER}}, {{LICENSE_EXPIRY}}).
2. Legal entity and trade name ({{LEGAL_ENTITY}}, {{DEALERSHIP}}).
3. Authoritative domain.
4. Whether a service department operates, and where.
5. Actual unit count and where inventory data lives.
6. Lenders, in-house paper, and servicer.
7. Warranty terms: duration, mileage cap, coverage, deductible, administrator. Must reconcile with the buyer's guide ({{WARRANTY_TERMS}}).
8. Consent and likeness for any pictured person.
9. Source of any award claim.
10. Who controls the business Page versus any personal profile.
11. County, market, and nearby installation ({{COUNTY}}, {{MARKET}}, {{NEARBY_INSTALLATION}}).
12. Doc fee ({{DOC_FEE}}).
End with a TODO list of what is still blank.

## Go-live gates (all required)
- [ ] License on file.
- [ ] County set.
- [ ] Warranty terms stated.
- [ ] Doc fee set.
- [ ] Lender recorded, or an explicit in-house-only declaration.
- [ ] Ad substantiation register seeded or explicitly empty (`../templates/compliance-ad-substantiation-register.md`).
- [ ] Compliance check passing on a sample ad built from the filled profile.
- [ ] Five registers created, safeguards program written, owner decisions recorded.
- [ ] Unfilled placeholder scan clean on all outward templates.

## Sign-off
{{OWNER}} signs go-live. Any gate not met keeps the office in draft mode: it may prepare documents but nothing leaves.
