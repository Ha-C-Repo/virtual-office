# Workflow: Churn Save

Skill: `../skills/churn-save/SKILL.md`.

1. Trigger received (cancellation, red band, failed payment, angry reply).
2. Within one business hour: personal first touch, no discount.
3. Listen; capture reason; assign reason code.
4. Select from the offer matrix. **Gate:** off-matrix offers need principal approval.
5. Present the offer; set a decision date.
6. Outcome: saved (log terms, schedule 30-day check-in), lost (clean exit, data export, deletion terms).
7. Record economics and reason code in the customer config and the churn log.
8. Monthly: review reason codes with product for roadmap input.
