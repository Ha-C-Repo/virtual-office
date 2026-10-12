# Measurement Verification Sheet

Property {{PROPERTY_ADDRESS}} | Report date {{REPORT_DATE}} | Source {{MEASUREMENT_SOURCE}} (aerial / manual / both) | Verified by {{VERIFIER}}

| Field | Aerial report | Manual / on-site | Difference | Chosen |
|---|---|---|---|---|
| Footprint sq ft | {{AERIAL_FOOTPRINT}} | {{MANUAL_FOOTPRINT}} | {{DIFF}} | {{CHOSEN}} |
| Roof area sq ft | {{AERIAL_AREA}} | {{MANUAL_AREA}} | {{DIFF}} | {{CHOSEN}} |
| Squares | {{AERIAL_SQUARES}} | {{MANUAL_SQUARES}} | {{DIFF}} | {{CHOSEN}} |
| Dominant pitch | {{AERIAL_PITCH}} | {{MANUAL_PITCH}} | {{DIFF}} | {{CHOSEN}} |
| Eave lf | {{A_EAVE}} | {{M_EAVE}} | {{DIFF}} | {{CHOSEN}} |
| Rake lf | {{A_RAKE}} | {{M_RAKE}} | {{DIFF}} | {{CHOSEN}} |
| Ridge lf | {{A_RIDGE}} | {{M_RIDGE}} | {{DIFF}} | {{CHOSEN}} |
| Hip lf | {{A_HIP}} | {{M_HIP}} | {{DIFF}} | {{CHOSEN}} |
| Valley lf | {{A_VALLEY}} | {{M_VALLEY}} | {{DIFF}} | {{CHOSEN}} |
| Wall flashing lf | {{A_WALL}} | {{M_WALL}} | {{DIFF}} | {{CHOSEN}} |
| Penetrations | {{A_PEN}} | {{M_PEN}} | {{DIFF}} | {{CHOSEN}} |

Variance percent {{VARIANCE_PCT}} against tolerance {{VARIANCE_TOLERANCE}}. Complex roof (many valleys, hips, dormers, steep sections)? {{YES_NO}}. On-site check done {{YES_NO}}.

Photo cross-check notes (additions, dormers, tree cover, flat sections): {{PHOTO_NOTES}}

Cross-check command: `python ../harnesses/takeoff_calc.py --length {{LENGTH}} --width {{WIDTH}} --rise {{RISE}} --json`

Decision and reason: {{DECISION}}
