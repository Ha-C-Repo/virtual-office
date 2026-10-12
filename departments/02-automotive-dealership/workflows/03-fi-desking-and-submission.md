# 03 F&I: Desking and Submission

Owner: F&I agent (`../agents/03-fi-agent.md`). Human owner: {{FI_MANAGER}}. Skills: `../skills/fi-desking/SKILL.md`, `fi-military-lending`, `fi-client-doc-scrubber`. All arithmetic is calculator output with an audit log. Customer credit data never goes through unpaid AI APIs or consumer chat.

## Steps
1. **Pull the unit.** Price, grade, disclosure needs from the unit record. Never retype the price.
2. **Run scenarios.** Calculator: payments at list, mid and floor credit tiers; out-the-door; negative-equity rollover; loan-to-value; payment-to-income. Use owner-locked economics (pack, recon budget, floorplan rate, gross targets, minimum down by tier, doc fee). A zero value means "not set" and blocks the run.
3. **Covered-borrower check.** Record the result on every deal regardless of what the buyer says. Indeterminate is treated as covered.
4. **Structure flags.** Flag any structure that could void the purchase-money exclusion (cash advanced beyond the price, certain financed add-ons) before submission. This stops the deal and goes to {{OWNER}} immediately.
5. **Product menu.** `../templates/fi-product-menu.md`, transparent prices, optional.
6. **Submit.** `../templates/fi-lender-packet-checklist.md`. Lender: {{LENDER}} (or in-house paper, declared).
7. **Stipulations.** `../templates/fi-stipulation-tracker.md`.
8. **Decline or changed terms.** Adverse-action notice for sign-off (`../templates/fi-adverse-action-notice.md`). A denial without a notice is an immediate escalation.
9. **Build the pair.** Client recap and `-INT` sheet together (`../templates/fi-deal-recap.md`, `fi-deal-recap-int.md`). Run the client-doc scrubber: no internal money, no placeholders.
10. **Four-pass review** (`08-compliance-four-pass-review.md`) before anything reaches the customer.

## Human sign-off
{{OWNER}} owns and approves the number. {{FI_MANAGER}} signs notices. Any payment shown carries the full disclosure block.

## KPIs
Covered-borrower checks as percent of funded deals (target 100). Adverse-action notices as percent of declines (target 100). Structures flagged before submission vs after funding.
