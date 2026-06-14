# Build Log — Reference-first mimic test v0.2

Created: 2026-06-12

## What was built
A single self-contained `index.html`: "Quiet Holdings", a fictional viewing room
("The Cold Store") that lays out six real public-domain studies/photographs as a
finding aid. Purpose: re-run the reference-first pipeline in a DIFFERENT visual
language from v0.1 (no riso / no registration offset / no newsprint / no
giant-type-only) and test reproducibility.

## Pipeline
1. Reviewed `../reference_first_mimic_test_v0_1/notes/self_evaluation_v0_1.md`
   first — targeted its weak points: "lower half too tidy", "only top is strong",
   "circle reliance".
2. `frontend-design:frontend-design` skill invoked (refined/restrained register
   this time, per its "minimalism needs precision" note).
3. Reference-first: lead = **Atlas of Places** (photo-led archive / finding-aid);
   annotation voice = **Public Domain Review**; object/caption grammar + the actual
   CC0 images = **Cleveland Museum of Art Open Access**. See `reference_observation_v0_2.md`.
4. theme-factory approach: a "Cold Store" token set — bone paper, warm ink, one
   curatorial-red accent, three type roles.
5. Materials FIRST: pulled six CC0 images from CMA Open Access before layout, so
   real photographs (not generated art) could be the hero.
6. canvas-design philosophy: object-on-table composition, plates hand-placed,
   captions as catalogue entries.
7. OFL fonts (Cormorant Garamond + Archivo) downloaded locally — different families
   from v0.1, no runtime CDN.

## Key moves (anti-AI, and different from v0.1)
- Photographs are the hero; the first view is a dark print bleeding off the top-right,
  title set low-left in open paper. No centred hero, no giant-type stunt.
- Non-uniform 12-col sheet: each plate a different size / rotation / bleed; captions
  placed away from their image; marginalia dropped into the gaps.
- Material runs the whole page: paper grain, scanner dust, vignette, page crop-marks,
  mount frames, red crop-corners, red square annotation ticks, curator marginalia —
  all the way down to the credits ledger (lower half kept strong).
- Single curatorial-red accent (no gradients, no orbs; annotation markers are squares).
- Honest integrity: real titles/makers/dates + CC0 credit; the "Cold Store", shelf
  marks and notes are clearly stated as fictional in the colophon.

## Gotchas / fixes
- AIC (artic.edu) IIIF is behind a Cloudflare challenge (403) — switched image source
  to Cleveland Museum of Art Open Access (direct CC0 CDN).
- Headless reveal timing was flaky (first-view came out blank). Hardened the script:
  reveal in-view elements on first paint + a safety timeout, so content can never
  stay hidden (better for real users too). Reduced-motion renders fully static.
- Page is ~6.6k px tall; full-page screenshot taken at 7200px to include the credits.

## Run
Open `index.html` in a browser (fully local/self-contained).
Screenshots in `screenshots/` (01 first view, 02 full desktop @7200, 03 mobile).
</content>
