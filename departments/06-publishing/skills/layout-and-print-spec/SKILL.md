---
name: layout-and-print-spec
description: Layout rules and print/ebook specifications: trim, bleed, gutter, spine math, color space, fixed-layout versus reflowable ebooks, cover specs.
---
# Layout and Print Spec

## When to use
Pipeline steps 10 to 12, and before illustration (dimensions must be known before prompts are written).

## Rules
- Text is a separate typeset layer. Never bake text into art.
- **Fixed-layout ebook** for picture books and any title where text placement matters. **Reflowable ebook** for prose-heavy chapter books.
- Define for each title and record in the title record: trim size {{TRIM_SIZE}}, bleed {{BLEED}}, safe margin {{SAFE_MARGIN}}, gutter {{GUTTER}}, page count, paper type, resolution (at least the printer minimum, measured), color space (CMYK for print, RGB for ebook).
- Keep faces, key text and hands inside the safe margin and away from the gutter.
- **Spine math (print only):** spine width = page count x paper thickness per page. Use the printer's cover calculator and record its output. Cover total width = back + spine + front + bleed on both outer edges.
- Ebook cover: separate file at the retailer's stated ratio and minimum pixel size; check current requirement and log it.
- Embed fonts; verify licenses for every font.

## Steps
1. Choose format and record specs.
2. Typeset text over art for each spread.
3. Export ebook (and print PDF if applicable).
4. For print: generate cover from calculator, convert to CMYK, order a physical proof.
5. A human reviews the proof page by page. Blocking.

## Gates
Never order print or publish without logged sign-off. Specs are measured from exports, not assumed.
