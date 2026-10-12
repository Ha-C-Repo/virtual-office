# Research Notes: Roofing Department

This department was synthesized from public-source research (trade press, vendor blog posts, federal safety guidance, state insurance department consumer pages, permit handouts). It is generic: no vendors, brands or companies are named. Treat everything as a starting point to be confirmed locally.

## What was researched
| Topic | Source types | Confidence |
|---|---|---|
| Pitch factor, squares, waste, bundles, accessories takeoff | trade how-to articles, supplier handouts | High for geometry, medium for coverage rates |
| Lead speed and intake practice | marketing blogs, CRM vendor posts | Low-medium; statistics unverified |
| Fall protection | federal safety regulation text and FAQs, safety trade posts | High for regulation text, medium for blog restatements |
| Insurance claim flow, ACV/RCV, supplements | state insurance department pages, trade press | Medium; varies by policy and state |
| Deductible and inducement rules | state insurance department pages, trade press | Medium; state-specific, VERIFY |
| Permits and code (layers, ice barrier, laps, ventilation) | model residential code summaries, permit handouts | Medium; local amendments vary |
| Commercial systems and warranties | manufacturer-neutral trade guides | Medium |
| Moisture surveys | trade guides, an ASTM method reference | Medium |
| Job costing, margins, overhead | contractor finance articles | Low-medium; figures are illustrative |
| Marketing and reputation | marketing blogs, consumer protection pages | Medium |
| AI/automation use cases | vendor blogs | Low; claims are marketing |

## Conflicting or uncertain figures (do not quote without checking)
- **Waste factors**: commonly 10 percent for a simple gable, about 12 percent for hip, 15 percent or more for complex, up to 25 percent for very complex. Sources differ; confirm with the supplier and the roof (VERIFY).
- **Bundles per square**: 3 for 3-tab, 3 to 4 for architectural, 4 to 5 for premium or designer lines. Always read the data sheet.
- **Starter and ridge coverage per bundle**: about 105 linear ft starter and 20 linear ft ridge cap were cited; products differ (VERIFY).
- **Underlayment roll coverage**: depends on product; the harness default of 10 squares per roll is a placeholder (VERIFY).
- **Fall protection height numbers**: blogs cite different heights and exemptions; the residential-roof 4 ft trigger and the infeasibility/written plan route should be read from the current federal text and state plan (VERIFY). The relief for inspection or assessment is narrow and should be confirmed in the current FAQ (VERIFY).
- **Ventilation ratio**: 1/150 versus 1/300 net free area depends on code edition and conditions (VERIFY).
- **Ice barrier extent**: eave to at least 24 in inside the exterior wall line is the common model-code text; local maps and amendments differ (VERIFY).
- **Cancellation periods**: three business days is a common statutory baseline for off-premises sales; some states add insurance-denial rescission (VERIFY).
- **Warranty registration window**: about 30 days is common; programs vary (VERIFY).
- **Margin ranges**: gross roughly 25 to 40 percent, net high single digits to low teens (illustrative only).
- **Speed-to-lead statistics** from vendor sources: unverified, not quoted. The department's own measure is `minutes_to_first_response` in the lead log.
- **Time to estimate**: sources suggest quick estimates win more jobs (the research cited about 24 hours versus about 5 days); treat as directional, measure your own median.

## Open gaps
1. **Retention and turnover data** for roofing crews: under-documented. HR skills use placeholders.
2. **Product-specific installation specifications**: nailing patterns, exposure, fastener counts, high-wind rules. Read the current manufacturer instructions; the office does not hold them.
3. **State-specific statutes**: contractor licensing, deductible law, public adjuster limits, AOB, rescission, lien forms, deposit caps, solicitation permits. Needs a counsel-reviewed `{{STATE_RULES}}` file.
4. **Current rate benchmarks**: labor rates, piece rates, material prices, workers compensation class rates, overhead percentages. All local placeholders.
5. **Commercial specifics**: design wind uplift, energy code R-values, drainage design, and manufacturer warranty form terms need project-specific review.
6. **Tool/AI accuracy**: no verified accuracy figures for photo damage assessment or aerial measurement; accuracy must be measured by the office using `../skills/aerial-measurement-verification/SKILL.md` variance logs.

## How to use these notes
- Before a rule in `rules.md` is used in a document going to a customer, regulator or carrier, clear its VERIFY tag and record the source and date in the project file.
- When a conflict appears, the order of authority is: statute and adopted code, then policy or contract, then manufacturer instruction, then this department's defaults.
- Update this file when a local check settles one of the figures above. Note the date and who verified it.
