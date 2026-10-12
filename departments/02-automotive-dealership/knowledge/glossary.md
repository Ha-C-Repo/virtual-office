# Glossary: Automotive Dealership

Sections are prefixed by function number. Terms shared across functions are under 00.

## 00 Cross-function
- **Tier 1 / Tier 2 / Tier 3:** immutable (law) / owner preference (logged) / default.
- **Gate:** an automated or procedural check that can stop an output. **Block** = law violation, stops. **Warn** = copy quality, advisory. **SKIP** = a check that did not run; a coverage hole. **Fail-closed:** if the check cannot run or a token is unfilled, the answer is "blocked". **One door:** a single path every item must pass.
- **Exit code:** 0 clean, 1 blocked, 2 usage or input error (not a pass).
- **-INT twin:** the internal companion of a client document carrying cost, pack, recon spend, floorplan interest, reserve and gross.
- **Confidence tag:** HIGH / MED / LOW on every extracted fact.
- **Practice run:** offline regression of the gates using clean and dirty sample pairs.
- **Approval queue:** the list of drafts awaiting a human decision.
- **Live documents:** the source files an agent must read directly rather than a copy.

## 01 Inventory
- **Stock number:** unique lot identifier for a unit. **VIN decode / reconcile:** decode from a public source, then compare to documents and photos.
- **Unit record:** structured facts, documents, defects and grade for one vehicle.
- **Grade A Inspected / B Declared / C As-Is Unverified:** the evidence levels that gate what copy may claim.
- **Disclosure set:** defects that must appear in copy, guide, register and photos.
- **Recon:** reconditioning. **Front-line ready:** recon closed and the unit may be listed.
- **Comp corridor:** low-to-high range of comparable asking prices. **Book value:** a named, dated published valuation. **Floor price:** lowest price the owner will accept. **Days-to-turn:** days from acquisition to sale. **Aged inventory:** units past the days-to-turn threshold. **Markdown schedule:** owner-set price steps for aged units.
- **Syndication:** pushing listings to channels. **Drift:** mismatch between live listings and the lot.
- **Four-part image rule:** office owns the pixels; vehicle unaltered; labeled and the label travels; original retained.
- **Specificity quota:** every creative needs at least one of year, mileage, price, stock number.

## 02 Sales
- **Up:** a walk-in prospect. **Speed-to-lead:** time from inquiry to first response.
- **Write-up:** the first deal sheet with price and terms. **Desking:** structuring the deal.
- **Pipeline states:** LEAD, APPOINTMENT, WRITE_UP, CREDIT_SUBMITTED, APPROVED, DELIVERED, FUNDED; side states LOST, UNWOUND, REPO.
- **Consent ledger:** record of who agreed to be contacted on which channel. **EBR:** established business relationship. **DNC:** do-not-call. **Retention touch:** a service-due, expiry, equity or maturity message. **Equity mining:** finding customers whose payoff is below current vehicle value.

## 03 Finance and Insurance
- **F&I:** finance and insurance. **Product menu:** optional add-on products with prices. **Stipulations (stips):** lender conditions to fund.
- **Adverse action:** the notice owed when credit is denied or offered on worse terms.
- **Reserve / pack / floorplan / front gross / back gross:** internal economics. **Funded:** the lender has paid.
- **MAPR:** military annual percentage rate. **Covered borrower:** an active-duty servicemember or dependent protected by the military lending rule. **Purchase-money exclusion:** a feature of the rule that can be lost by certain structures.
- **LTV / PTI:** loan-to-value / payment-to-income.
- **Negative equity:** trade payoff exceeds its value.

## 04 Title and Admin
- **Deal jacket:** the file of all documents for a sale. **TT&L:** tax, title and license.
- **Odometer statement:** signed disclosure of mileage at transfer. **Temp tag:** temporary registration. **Lien perfection:** the lender's recorded interest on the title. **Filed vs recorded:** submitted vs accepted by the state.
- **Doc fee:** the dealer documentary fee. **Dealer license:** state authority to sell.
- **VERIFY / OFFICE:** deadline confidence labels. **NEEDS_INPUT:** day count unknown.
- **URGENT / THIS WEEK:** warning levels at 3 and 7 days.

## 05 Service and Recon
- **We-owe / due bill:** written promise to a buyer for something not done at delivery. **Repair authorization:** approval to fix a stated defect. **Goodwill repair:** a post-sale courtesy repair with no implied legal obligation.
- **Recon-closed gate:** no listing until recon is closed.
- **30-day check-in:** scheduled post-sale contact.

## 06 Marketing
- **Buyer's guide:** the federally required window form (as-is vs warranty). **As-is box.**
- **Ad substantiation register:** proof file for ad claims. **Superlative:** "best", "number one" and similar; blocked.
- **Disclosure block:** the set of financing terms required whenever any one appears.
- **Dimension tags:** format, hook, topic, media, length, cta. **Fast lane / slow lane:** weekly actions on large effects vs cumulative learning. **Not separated:** the honest report when evidence is too thin.
- **Ken Burns:** slow pan and zoom over a still.

## 07 Reputation
- **Class 1 to 4:** review classes by risk. **Escalation note.** **Review queue.** **Off-limits designation:** a military board ban on dealer patronage.

## 08 Compliance
- **Five registers:** ad substantiation, AI disclosure, data processing, vehicle condition disclosure, platform policy.
- **Safeguards program:** the written customer-data security program. **Qualified individual.**
- **AI disclosure:** a fixed first-message statement that a surface is AI.
