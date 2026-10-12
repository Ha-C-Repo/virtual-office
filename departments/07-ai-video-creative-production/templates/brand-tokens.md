# Brand Tokens: {{COMPANY}}

```json
{
  "name": "{{BRAND_NAME}}",
  "version": "{{TOKEN_VERSION}}",
  "status": "draft | approved",
  "sources": ["{{SOURCE_1}}"],
  "identity": {
    "company": "{{COMPANY}}",
    "positioning_line": "{{POSITIONING_LINE}}",
    "signature_line": "{{SIGNATURE_LINE}}",
    "retired_lines": ["{{RETIRED_LINE}}"]
  },
  "logo": {
    "rule": "{{LOGO_RULE}}",
    "lockups": ["{{LOCKUP_1}}"],
    "pairing": "{{LOGO_PAIRING_RULE}}"
  },
  "surfaces": {
    "video": {"primary": "{{COLOR_PRIMARY}}", "accent": "{{COLOR_ACCENT}}", "type": "{{FONT_FAMILY}}"},
    "document": {"primary": "{{COLOR_PRIMARY}}", "type": "{{FONT_FAMILY}}"},
    "website": {"primary": "{{COLOR_PRIMARY}}", "background": "{{COLOR_BACKGROUND}}", "type": "{{FONT_FAMILY}}"}
  },
  "donts": {
    "banned_strings": ["{{BANNED_STRING}}"],
    "warn_strings": ["{{WARN_STRING}}"],
    "rules": ["{{RULE}}"]
  }
}
```
