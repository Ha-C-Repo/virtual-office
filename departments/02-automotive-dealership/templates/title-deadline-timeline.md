# Deadline Timeline: {{DEAL_REF}}

Anchor dates: sale date {{SALE_DATE}}, delivery date {{DELIVERY_DATE}}, funded date {{FUNDED_DATE}}. A missing anchor date raises dependency risk early. A rule whose day count is unknown is NEEDS_INPUT, never guessed.

Confidence: VERIFY = day count confirmed from authority text; OFFICE = house rule.
Warning levels: URGENT at 3 days or fewer, THIS WEEK at 7 days or fewer. "Filed" and "recorded" are different states.

| Key | Deadline | Basis (rule and offset) | Due date | Confidence | Status (NEEDS_INPUT / OPEN / FILED / RECORDED / SKIPPED) | Completed | Warning level |
|---|---|---|---|---|---|---|---|
| odometer_disclosure | Odometer statement executed | {{RULE}} / {{OFFSET_DAYS}} | {{DATE}} | {{VERIFY_OFFICE}} | {{STATUS}} | {{DATE}} | {{LEVEL}} |
| title_application | Title application filed | {{RULE}} / {{OFFSET_DAYS}} | {{DATE}} | {{VERIFY_OFFICE}} | {{STATUS}} | {{DATE}} | {{LEVEL}} |
| temp_tag_expiry | Temp tag expires | {{RULE}} / {{OFFSET_DAYS}} | {{DATE}} | {{VERIFY_OFFICE}} | {{STATUS}} | {{DATE}} | {{LEVEL}} |
| lien_perfection | Lien perfected (financed only) | {{RULE}} / {{OFFSET_DAYS}} | {{DATE}} | {{VERIFY_OFFICE}} | {{STATUS}} | {{DATE}} | {{LEVEL}} |
| covered_borrower_check | Check recorded | at write-up | {{DATE}} | OFFICE | {{STATUS}} | {{DATE}} | {{LEVEL}} |
| buyers_guide_on_file | Guide on file, matches contract | at sale | {{DATE}} | OFFICE | {{STATUS}} | {{DATE}} | {{LEVEL}} |
| warranty_admin_filing | Warranty or service-contract filing (skip if as-is) | {{RULE}} / {{OFFSET_DAYS}} | {{DATE}} | {{VERIFY_OFFICE}} | {{STATUS}} | {{DATE}} | {{LEVEL}} |
| post_sale_checkin | 30-day check-in | delivery + 30 | {{DATE}} | OFFICE | {{STATUS}} | {{DATE}} | {{LEVEL}} |

## Office-level deadlines
| Item | Holder (role) | Due | Status |
|---|---|---|---|
| Dealer license renewal ({{LICENSE_NUMBER}}) | {{OWNER}} | {{LICENSE_EXPIRY}} | {{STATUS}} |
| Continuing education | {{LICENSED_ROLE}} | {{DATE}} | {{STATUS}} |
| Bond or insurance certificates | {{OWNER}} | {{DATE}} | {{STATUS}} |
