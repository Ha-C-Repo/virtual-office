---
name: deductible-and-inducement-gate
description: Fail-closed screen for any outward text that waives, rebates, absorbs or hints at covering a deductible, or offers other prohibited inducements.
---
# Deductible and Inducement Gate

## When to use
On every customer-facing or public item: scripts, door hangers, ads, social posts, texts, emails, proposals, contracts, referral offers, review requests, invoices.

## Inputs
The text to be sent and its context (insured loss or not).

## Block list (any hit fails)
- Waiving, rebating, absorbing, "covering", crediting or reimbursing a deductible, however worded ("no out of pocket", "insurance pays for everything", "we will take care of your deductible", "free roof").
- Inflating an invoice or estimate to hide a deductible, or splitting invoices to avoid it.
- Gifts, cash, gift cards, discounts or services tied to filing a claim or referring a claim.
- Offering to negotiate coverage or act as the adjuster, or giving legal or coverage advice, without the required license.
- Guaranteeing claim approval or amounts.
- Urgency or fear claims not backed by photos.
- Referral rewards that depend on insurance claims (VERIFY {{STATE}}).

## Steps
1. Read the text against the block list. Search for key phrases, then read the context; word variations still count.
2. For each hit: quote it, give the rule, and propose a compliant rewrite, for example: "Your insurance policy determines what is covered. The homeowner is responsible for the deductible. We document the damage and provide an itemized estimate."
3. Re-run the gate on the rewrite.

## Outputs
Gate report: item, rule, pass/fail, evidence, required fix. Log refusals.

## Gates
- Fail closed: if the context is unclear, block and ask.
- The gate does not approve; the owner approves after a pass.
- State rules vary and change (VERIFY {{STATE}}); counsel reviews the block list yearly.
