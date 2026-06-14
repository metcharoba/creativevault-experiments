# Build Log — Reference-first mimic test v0.1

Created: 2026-06-12

## What was built
A single self-contained `index.html`: a fictional risograph print show
("SECOND PRESSING" by the fictional "Gutter Press") used purely as a vehicle to
test the reference-first / design-stack pipeline against generic AI-LP output.

## Pipeline
1. `frontend-design:frontend-design` skill invoked first (anti-AI-slop guidance:
   distinctive type, committed aesthetic, asymmetry, texture/grain).
2. Reference-first: chose editorial type-foundry composition (Klim) as the lead,
   riso material (Risotto) as the surface, scale-break/overlap (Bureau Borsche) as
   the layout attitude. See `reference_observation_v0_1.md`.
3. theme-factory approach: defined an on-the-fly "Newsprint Riso" token set
   (paper / ink / pink / blue / hair + 3 type roles) in `:root`.
4. algorithmic-art approach: a seeded (`mulberry32`) generative halftone field
   rendered in two offset ink layers on a vanilla `<canvas>` (no p5/CDN, to keep
   the file self-contained). This is the page's main "image".
5. canvas-design philosophy: poster-grade hierarchy, oversized display lockup,
   one dominant gesture, body set as printed matter.
6. OFL fonts (Big Shoulders Display, Fraunces italic) downloaded locally and
   referenced via `@font-face` — no runtime CDN.

## Key moves (anti-AI)
- Misregistered duotone masthead (pink + blue offset layers, `mix-blend:multiply`).
- Flat newsprint paper (NOT a dark gradient); grain via self-made `feTurbulence`.
- Plates shown as a ruled editorial **ledger** (numbered rows), not cards.
- CTA = underlined text link + rubber stamps, NOT a pill.
- Generative halftone plate bleeds off-grid; stamps rotated off-grid.

## Gotcha / fix
- Headless full-page screenshot first came out blank: the IntersectionObserver
  reveal didn't fire within the default `--virtual-time-budget` because the canvas
  rAF loop keeps the page "busy". Fixed by raising the budget to ~10s and adding
  `--run-all-compositor-stages-before-draw`. (Reduced-motion path renders fully
  static, so accessibility is unaffected.)
- Relocated the blue stamp (`.stamp.two`) out of the meta text; stamps hidden < 760px.

## Run
Open `index.html` directly in a browser (fully local, self-contained).
Screenshots in `screenshots/` (01 first view, 02 full desktop, 03 mobile).
</content>
