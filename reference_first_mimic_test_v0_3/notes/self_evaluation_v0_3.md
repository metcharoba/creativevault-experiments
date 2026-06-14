# Self-Evaluation — Reference-first mimic test v0.3

Created: 2026-06-12
Honest, not promotional. 0 = nearly the same as before, 5 = clearly a different system output.

## D. Difference vs v0.1 / v0.2

| Axis | Score | Basis |
|---|---:|---|
| Different picture than v0.1 | 5 | Saturated colour-blocking + Shrikhand + sticker borders vs riso poster. Different fonts; no registration offset, no newsprint, no single giant-type gambit. |
| Different picture than v0.2 | 5 | Bright maximalist pop vs quiet photo archive. No photos, no finding-aid, no mount frames. |
| Bright pop feel | 5 | Tangerine / cherry / lime / grape / blue / yellow saturated blocks, giant fat display, burst seals, a ticker. Unmistakably loud. |
| Reference composition used | 4 | Myerscough's colour-block + big type, Walala's angular pattern (zigzag), Hey's flat-shape bottle all landed. |
| Pop without being cheap | 4 | No pastel, no emoji, no round reliance; a pseudo-scientific data layer (CO₂/pH/batch) + a bar chart give it rigour. |
| Material/shape runs through the whole page | 4 | Grain + zigzag seams + sticker borders + burst seals + colour blocks continue to the footer — not just a strong top. |
| Non-uniformity | 4 | Tags differ in colour / size / rotation / clip-path and overlap; steps are rotated; the grid is broken. |
| Generic AI-LP reduction | 4 | No centred hero, no even card grid, no pill, no orb, no dark gradient, no Tailwind look. |
| "Screen as artwork" feel | 4 | Reads like a toy box / shop POP / packaging spread, not a web template. |

## E. AI-ness that remains (honest)

- **Centred hero:** avoided (logotype left, bottle right). But the `bigbanner` and a few
  block headings sit centred-ish; mobile stacks vertically (universal fallback).
- **Uniform cards:** the tags are placed non-uniformly, BUT every tag uses the *same*
  treatment — 3px black border + hard drop-shadow + folded pip. The how-to steps repeat
  the same frame too. This is the **same "uniform framing language" tell flagged in v0.2,
  now in sticker form**: placement varies, processing doesn't. The clearest weakness.
- **Pill CTA:** none — chevron and ribbon banners (angular clip-paths) instead.
- **Gradient-dependence:** fully avoided — flat saturated colour everywhere (arguably
  TOO flat; grain is the only rescue from dead-flat digital).
- **Round / orb escape:** no orb; seals are spiky stars, pips are squares. BUT the fizz
  **bubbles are circles**, and the bottle cap/label-star carry curves — a small lean on
  round shapes remains.
- **Pastel / emoji cheap-pop:** avoided (saturated colour, text ★ not emoji).
- **Over-tidy:** colours clash hard, but the underlying skeleton (tag grid, even bar
  spacing, step row) is fairly orderly. The chaos is in colour/rotation, less in structure.
- **Only-the-top-strong:** fixed — the footer is as loud as the hero. A real win.
- **Did the reference matter?** Yes — colour-block + big type (Myerscough), angular
  pattern (Walala), flat-shape build (Hey) are visible. Observation was again from known
  design language, not a fresh live screenshot study: medium fidelity.

## F. System evaluation — v0.1 vs v0.2 vs v0.3

- **Reproducible across 3 registers?** Yes. Dark/printerly (v0.1), quiet/archival (v0.2),
  bright/pop (v0.3) all escaped the generic AI-LP and are clearly different from each other.
  3 for 3.
- **Could it hit dark / quiet / bright on demand?** Yes — the register changed cleanly each
  time and is legible within one second.
- **Which step did the most work?** Consistently: **naming a lead reference + writing an
  explicit avoid/seek list.** That fixes the direction and mechanically removes
  centred-hero / pill / cards. Strong second: **deciding materials first** (fonts, and the
  hero object — photos in v0.2, the bottle/seals/palette in v0.3).
- **Weakest step (recurring)?** **Per-element processing goes uniform** — riso mounts in
  v0.2, sticker frames in v0.3. The system breaks *placement* well but defaults every item
  to one treatment, which reads templated. Secondary: **observation fidelity** (known
  design language, not a real screenshot study).
- **Make it the standard route?** Yes. Formalise: 3 refs → 1 lead → avoid/seek list →
  materials first → single self-contained HTML → screenshot self-critique.
- **Where to improve next — reference / materials / implementation?**
  **Implementation > reference.** Add a rule: *vary the per-element treatment*
  (frame / shadow / cut / texture) so processing isn't uniform. Then upgrade observation
  to "capture at least one real reference screenshot." The prompt side has done its job in
  all three runs.
</content>
