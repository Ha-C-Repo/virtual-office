---
name: marketing-vehicle-ad-compliance
description: Tier 1 rules and scanner patterns for every outward vehicle ad, listing, caption and script, with a block versus warn split.
---
## BLOCK (law)
- Superlatives and unsubstantiated award or ranking claims.
- Universal-approval phrases (everyone financed, no credit rejected, we finance anyone, name your own price or payment).
- Savings, discount, "up to", "was-now" on used vehicles.
- Guaranteed trade-in allowance.
- "Loaded" or "fully equipped" without the option list.
- Condition claims beyond the grade.
- Unsourced vehicle facts or history claims ("clean history report", "one owner", "no accidents" with no document on record).
- Advertised vehicle not in possession with title assigned, or price excluding anything except registration, taxes and authorized charges.
- Price ad without year, make, model line or style, and used status.
- Any triggering financing term (down payment, payment, number of payments, finance charge) without the full disclosure block in the same creative.
- Generated vehicle, building, storefront or person imagery.
- Internal economics, unfilled placeholders, em-dashes.
- Warranty wording that does not match the buyer's guide.
- Non-English copy without a recorded bilingual reviewer.

## WARN (quality)
Cliches and urgency phrases, vague intensifiers, sentences over 25 words, passive streaks, more than one idea per creative. Warn rules never change an exit code. Conditional cliches warn when the substantiating document is on record.

## Steps
1. Load the single blocklist fail-closed.
2. Scan in marketing context (strictest).
3. Check specificity quota (at least one of year, mileage, price, stock number).
4. Output hits with locations and exit code.
