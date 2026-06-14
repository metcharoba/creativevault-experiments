# Self-Evaluation — Reference-first mimic test v0.2

Created: 2026-06-12
Honest, not promotional. 0 = nearly the same as v0.1, 5 = clearly a different system output.

## D. Difference vs v0.1

| Axis | Score | Basis |
|---|---:|---|
| Different picture than v0.1 | 5 | Different fonts (Cormorant/Archivo vs Big Shoulders/Fraunces), different palette (bone + curator-red vs riso), photographs as hero, finding-aid grammar. Zero riso / registration-offset / giant-type. |
| Photo / exhibition / archive feel | 4 | Six real CC0 photographs framed as physical prints on a table, with shelf marks, mounts and annotations. Reads as a viewing room, not a gallery grid. |
| Reference composition used | 4 | Atlas of Places' photo-led finding aid, PDR's annotation/marginalia, CMA's catalogue caption pattern all landed. |
| Material runs through the whole page | 4 | Grain + dust + vignette + page crop-marks + mount frames + red crop-corners + marginalia continue down to the credits ledger — not just a strong top. |
| Avoided "only the top is strong" | 4 | The lower half keeps the same plate+caption+annotation rhythm and the credits are a finding-aid, not a generic footer. Biggest improvement over v0.1. |
| Non-uniformity | 4 | Every plate has a different size / rotation / bleed; captions sit away from their image; marginalia land in the gaps; the 12-col sheet is deliberately under-filled. |
| Generic AI-LP reduction | 4 | No centred hero, no cards, no pill, no orb, no dark gradient, no Tailwind look. |
| "Screen as artwork" feel | 4 | Closer to a catalogue laid on a table than a web template. |

## E. AI-ness that remains (honest)

- **Centred hero:** avoided on desktop (title low-left, image bleeding top-right).
  Mobile collapses to a vertical stack — the universal small-screen fallback.
- **Uniform cards:** none. BUT every plate gets the *same* treatment (white mount +
  shadow + red crop-corners). Placement is non-uniform, yet the *framing language is
  uniform* — a mild template tell. Real archives mix frames, tape, sleeves, bare prints.
- **Pill CTA:** none — and correctly no CTA at all (it's a viewing, not a funnel).
- **Gradient-dependence:** avoided; paper is flat, image overlay is a faint multiply.
- **Round / orb escape:** no orb; annotation markers are squares. One real ellipse
  remains — Carjat's portrait sits in a physical oval frame. Intentional (it's the
  object), but it is an ellipse on screen.
- **Over-tidy:** the credits ledger and caption hierarchy are still orderly. The
  "hand-placed" feel is implied by rotation, not by genuinely irregular handling
  (no fingerprints, pencil marks, uneven mount shadows).
- **Did the reference matter?** Yes — finding-aid + annotation + photo-as-hero are
  clearly Atlas/PDR-derived. But observation was again from known design language,
  not a fresh live screenshot study: medium fidelity.

## F. System evaluation — v0.1 vs v0.2

- **Reproducible?** Looks like it. Two runs both escaped the generic AI-LP, and in two
  genuinely different visual languages (industrial riso poster vs quiet photo archive).
  The same route carried over: references → decomposition → theme tokens → materials →
  single self-contained HTML → screenshot self-critique.
- **Which step did the most work?** Naming the **reference + an explicit
  avoid/seek list**. That mechanically kills centred-hero / pill / cards and locks the
  direction to one idea. Close second: **collecting materials first** (v0.2 securing
  real CC0 photos up front is what made "photo as hero" real rather than decorative).
- **Weakest step?** (1) **Observation fidelity** — decomposing from known design
  language instead of actually studying a live screenshot. (2) **Uniform treatment** —
  the framing language repeats and starts to feel templated. (3) Minor: headless
  screenshot reveal timing was flaky (an implementation detail, now hardened).
- **Make it the standard route?** Yes, conditionally — formalise
  "3 refs → 1 lead → avoid/seek list → materials first → single HTML → screenshot
  self-critique" as the pipeline.
- **Where to improve next — prompt / reference / materials / implementation?**
  **Reference selection > implementation.** Specifically: (a) upgrade observation into
  a required step ("capture at least one real reference screenshot and decompose it"),
  and (b) in implementation, deliberately *vary the framing language per item* so the
  "processing" is not uniform. The prompt side is already doing enough; the materials
  side worked well this round.
</content>
