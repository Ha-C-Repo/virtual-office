# 00 Unit to Listing: Gate Order (cross-function)

Owner: Compliance (`../agents/08-compliance-agent.md`) with Inventory. Applies before any unit becomes a live listing and whenever a listing changes. Report the exit code actually observed (0 clean, 1 blocked, 2 usage or input error, which is not a pass). A SKIP is a coverage hole. Clean gates over LOW-confidence input still yield a LOW-confidence deliverable.

## Order
1. **Facts audit.** Every fact on the unit record has a source and a HIGH / MED / LOW tag (`../templates/inventory-unit-record.md`).
2. **VIN verify.** Decode reconciles with documents and photos. Mismatch stops here.
3. **Sanity gates.**
   - Price vs corridor, mileage sourced, book value, package completeness (`../templates/inventory-comp-grid.md`).
   - Photo standard (`../templates/inventory-photo-manifest.md`).
   - Buyer's guide generated and consistent with ad warranty language.
   - Every disclosed defect present in copy and photographed (`../templates/inventory-disclosure-set.md`).
4. **Compliance check** on all outward copy in marketing context, the strictest: blocklist, specificity quota, disclosure block, grade-adjective gate, ad substantiation register.
5. **Client/INT pair validation.** Client document has its `-INT` twin; leak scan on the client side.
6. **Practice-run regression.** Only if gate code or skills changed since the last pass.
7. **Skills audit.** Only if a skill changed.

## Stop conditions
Any BLOCK returns the unit to the owning function with the failing line. No override on a Tier 1 gate. Placeholders still unfilled in outward copy are a block.

## Sign-off
{{OWNER}} approves the price and the listing. Compliance records the exit codes in the unit record.
