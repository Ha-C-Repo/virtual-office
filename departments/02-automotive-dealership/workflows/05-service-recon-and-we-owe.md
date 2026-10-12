# 05 Service and Recon: Recon and We-Owe

Owner: Service and Recon agent (`../agents/05-service-recon-agent.md`). Human owner: {{RECON_LEAD}}. Skill: `../skills/service-we-owe-generator/SKILL.md`.

## Recon flow
1. The condition audit emits a recon work order (`../templates/inventory-recon-work-order.md`).
2. Open a recon log (`../templates/service-recon-log.md`) with arrival date.
3. The shop closes items. Closing a recon item and fulfilling its we-owe are one action, recorded once.
4. Compare spend with the grade budget. Over budget: tell {{OWNER}} before more spend.
5. Re-run the grade (`../skills/inventory-condition-grading/SKILL.md`).
6. Recon-closed gate: a unit is not listed until recon is closed and the grade reflects what was found and fixed. Send the front-line-ready signal to Inventory.

## We-owe flow
1. Any promise to a buyer (made at demo, write-up or delivery) becomes a line on a due bill the same day (`../templates/service-we-owe.md`). Numbering `WO-<stock>-<NNN>`.
2. Types: DUE BILL, REPAIR AUTHORIZATION (defect ref, repair, authorizer), GOODWILL REPAIR (post-sale, no implied legal obligation).
3. Internal twin carries cost and markup (`../templates/service-we-owe-int.md`). The client copy never shows cost.
4. Status: DRAFT, APPROVED, OPEN, FULFILLED, CANCELED. {{OWNER}} approves.
5. Daily overdue check. Any item past promise date escalates to {{OWNER}} the same day.
6. Fulfilled: record the date, collect buyer sign-off.

## Post-sale
30-day check-in (`../templates/service-30-day-checkin.md`). Goodwill repairs follow the we-owe flow. A concealment or safety claim goes to `07-reputation-review-response.md` class 1.

## KPIs
We-owe items closed by promise date (target 100 percent), average days-to-recon-close, 30-day check-ins completed vs scheduled.
