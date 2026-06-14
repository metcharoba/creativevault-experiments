# Build Log — Reference-first mimic test v0.3

Created: 2026-06-12

## What was built
A single self-contained `index.html`: "SUPERFIZZ", a fictional research bureau for
loud soft drinks. Purpose: re-run the reference-first pipeline in a THIRD visual
language — bright maximalist designed-pop — distinct from v0.1 (riso poster) and
v0.2 (photo archive), and test whether the system also works for bright/playful.

## Pipeline
1. Reviewed v0.1 + v0.2 self-evaluations first, to (a) carry the wins (explicit
   avoid/seek list, materials-first, language running top-to-bottom, non-uniform
   placement) and (b) avoid repeating riso / photo-archive.
2. `frontend-design:frontend-design` skill invoked (maximalist register: "maximalist
   needs elaborate code with extensive effects").
3. Reference-first: lead = **Morag Myerscough** (colour-block + big type + pattern);
   pattern vocabulary = **Camille Walala** (stripes/zigzag/triangles, not dots);
   flat-shape craft = **Hey Studio**. See `reference_observation_v0_3.md`.
4. theme-factory approach: a saturated "soda" token set (tangerine/cherry/lime/grape/
   blue/yellow + warm ink) — colour-blocking per section, NOT one flat bg.
5. algorithmic-art / canvas-design philosophy: built the visual objects from a few
   precise flat shapes (bottle, spiky burst seals, ribbon banners, bar chart) rather
   than photos or generated canvas.
6. OFL fonts (Bricolage Grotesque + Shrikhand) self-hosted — different families again.

## Key moves (bright pop, but not cheap, and different from v0.1/v0.2)
- Saturated colour-BLOCKING per section is the page structure; stickers/objects cross
  the block seams. Same loud language (Shrikhand + sticker borders + zigzag seams +
  burst seals + grain) runs hero → flavours → meter → how-to → visit → footer.
- Anti-cheap-pop guards: NO pastel (saturated), NO emoji (text ★ only), NO round
  reliance (burst seals are spiky 16-point stars via clip-path; number pips are
  folded-corner squares), NO pill (chevron + ribbon banners, angular clip-paths).
- Design density via a pseudo-scientific layer: CO₂ vol / pH / batch readouts, a
  hand-drawn "Fizz-o-meter" bar chart, a ticker — multiple information registers.
- Non-uniform flavour tags: each a different colour / size / rotation / clip-path,
  overlapping, off the text grid.
- Self-made geometric soda bottle (SVG), drop-shadowed like a die-cut sticker.

## Gotchas / fixes
- Stray non-ASCII char in a CSS `--cherry` declaration (typo) — removed; the page now
  has one clean cherry token.
- Same hardened reveal as v0.2 (in-view on first paint + safety timeout) so headless
  screenshots and real users never see hidden content. Reduced-motion: ticker, bottle
  wobble, bubbles and pop-in all disabled, page fully static.
- Full-page screenshot trimmed to the footer's bottom (page ≈ 5.15k px).

## Run
Open `index.html` in a browser (fully local/self-contained).
Screenshots in `screenshots/` (01 first view, 02 full desktop, 03 mobile).
</content>
