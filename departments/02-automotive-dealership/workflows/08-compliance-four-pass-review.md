# 08 Compliance: Four-Pass Review

Owner: Compliance agent (`../agents/08-compliance-agent.md`). Required before any client deliverable leaves the office (deal recap, listing, ad, notice, we-owe). Skill: `../skills/compliance-verification-before-completion/SKILL.md`. Report the exit code observed.

## Three owner gates before the passes
1. **Deal ownership.** One named human owns the number.
2. **Document reading** before pricing or an ad: inventory the documents, classify them, flag what is missing.
3. **Review before output.**

## Passes
1. **Calculation cross-check.** Re-run figures through the calculators. Compare price to corridor. Sample high-risk numbers more than once. The model never signs off its own number.
2. **Record completeness.** Every fact traces to a source with a confidence tag. Conflicts are resolved, not averaged.
3. **Leak scan.** No cost, pack, recon spend, floorplan interest, reserve, gross or staff names on the client side. The `-INT` twin exists (`../skills/fi-client-doc-scrubber/SKILL.md`).
4. **Layout, labels and ad-law screen.** Blocklist, disclosure block, buyer's guide agreement, grade-adjective gate, AI-image labels, no unfilled placeholders, no em-dashes.

## Result
Exit 0 clean. Exit 1 blocked: return to the owning function with the failing line. Exit 2 usage or input error: not a pass. SKIP rows are coverage holes and are listed.

## After delivery
One line to {{OWNER}}: what went out, the headline number, confidence tier, open flags.

## Periodic
Monthly: registers audit (`../skills/compliance-registers-audit/SKILL.md`) and scorecard (`../templates/compliance-scorecard.md`). Quarterly: platform policy re-check, safeguards program review.
