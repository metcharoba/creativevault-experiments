# Self-Evaluation — Reference-first mimic test v0.1

Created: 2026-06-12
Honest, not promotional. 0 = no change vs generic AI LP, 5 = clearly a different thing.

## D. Difference vs previous AI-ish LP output

| Axis | Score | Basis |
|---|---:|---|
| Different picture than before | 4 | Flat newsprint paper, misregistered duotone, halftone plate, a ruled ledger. A different *category* from the dark-gradient + glass-card LP. Not 5 because the entrance is still "giant title, then a line of copy" — a near-universal syntax. |
| Reference composition used | 4 | Klim's "oversized type = the image + ruled index", Risotto's registration offset/grain, Borsche's scale-break & overlap all landed in code. |
| Artistic-ness | 4 | Reads as printed matter: misregistration kept on purpose, stamps, tape, paper shadow. |
| Material feel | 4 | Self-made `feTurbulence` grain + 2-ink overprint + tape + paper drop-shadow, not CSS-gradient gloss. |
| Noise feel | 4 | Real grain (feTurbulence) + halftone screen, much more present than the old faint dot layers. |
| Non-uniformity | 3 | Title/plate overlap, uneven ledger indents, rotated stamps — but the underlying grid (ledger rows, footer 2-col + dl) is still fairly orderly. Could be broken harder. |
| Generic AI-LP reduction | 4 | No pill, no orb, no frosted glass, no centred hero, no dark gradient, no Tailwind look. |
| "Screen as artwork" feel | 4 | Closer to a print poster than a web template. |

## E. AI-ness that remains (honest)

- **Centred hero:** avoided on desktop (left-anchored). But on mobile it collapses to a
  vertical stack, and the "huge word → explanatory sentence" order is still the普遍 LP grammar.
- **Uniform cards:** gone — replaced by an editorial ledger.
- **Pill CTA:** gone — underlined text link + stamp instead.
- **Gradient-dependence:** mostly avoided (paper is flat). Caveat: the footer drop-shadow
  and the duotone rely on solid colour, which is fine, but the plate is colour-heavy.
- **Circle / orb escape:** no orb — BUT the halftone plate is literally built from
  thousands of **circular dots**. It's meaningful (a print screen), yet "round shapes"
  are still doing a lot of the visual work. Worth flagging honestly.
- **Over-tidy:** the ledger and the footer `dl` are still quite neat / table-like. The
  asymmetry is mostly in the hero; the lower half behaves.
- **Did the reference matter?** Yes — the ledger-instead-of-cards and the registration
  offset are direct, useful borrowings. But observation was from *known* design language,
  not a fresh live screenshot study, so the fidelity is medium, not deep.

## F. Single next change

Push the riso material **through the body**, not just the hero. Right now it's a
"polished hero + plain ledger/footer" — itself an AI tell (strong top, ordinary rest).
Next: give the ledger rows and footer faint registration offset / ink-density unevenness
(per-block micro-offset + occasional overprint smudge), and let one or two ledger entries
carry their own tiny generative halftone, so the *whole sheet* feels printed — not just
the masthead. That single move attacks the biggest remaining weakness (non-uniformity =
3, over-tidy lower half) most directly.
</content>
