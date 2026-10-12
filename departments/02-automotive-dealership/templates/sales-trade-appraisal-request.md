# Trade Appraisal Request

Collects the facts needed to appraise a customer's trade. No trade value is promised in writing before inspection. A guaranteed trade-in allowance in any ad is blocked.

Lead / deal: {{LEAD_ID}} / {{DEAL_REF}}   Date: {{DATE}}   Customer: {{CUSTOMER_NAME}}

## Customer message (draft; approval queue first)
{{FIRST_NAME}}, to give you a real number on your trade, please send or bring: the VIN, current mileage, photos (front, rear, both sides, interior, odometer), and any loan payoff information. We confirm the figure after we see the vehicle.

## Trade facts
| Field | Value | Source |
|---|---|---|
| VIN | {{TRADE_VIN}} | customer / photo |
| Year / make / model / trim | {{TRADE_YMMT}} | VIN decode |
| Mileage | {{TRADE_MILEAGE}} | odometer photo |
| Title in hand | {{YES_NO}} | |
| Lienholder and payoff | {{LIENHOLDER}} / {{PAYOFF}} | payoff letter |
| Known issues (customer statement, LOW confidence) | {{ISSUES}} | customer |
| Accident or flood history stated | {{STATEMENT}} | customer |

## Appraisal (Inventory runs this; owner sets the offer)
Comp grid: `inventory-comp-grid.md` ref {{COMP_GRID_REF}}
Reconditioning estimate: {{RECON_ESTIMATE}}
Offer approved by owner: {{OFFER}}   Valid until: {{DATE}}
Equity position (calculator): {{EQUITY_RESULT}}

Conditions: offer is subject to inspection and a clean, assigned title.
