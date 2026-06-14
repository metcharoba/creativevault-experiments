# Reference-first Mimic System — Validation Summary v0.1

Created: 2026-06-12
Scope: CreativeVault / design system validation. This is a **closing log** for the
three-build validation of the Reference-first mimic system. Read-only summary; it does
not modify the three experiments.

Experiments covered:
- `70_design_experiments/reference_first_mimic_test_v0_1/`
- `70_design_experiments/reference_first_mimic_test_v0_2/`
- `70_design_experiments/reference_first_mimic_test_v0_3/`

---

## 1. Validation purpose

Test whether a **reference-first** method (study strong real sites, then build an
original artifact that mimics structure but not content) can reliably move output away
from "generic AI mass-produced LP" — and whether it works across **different visual
registers**, not just one lucky aesthetic. Each run had to be a different system and
clearly distinct from the others, judged on a real built artifact + screenshots.

## 2. The three builds

| # | Name | Register | Lead reference(s) | What it is |
|---|---|---|---|---|
| v0_1 | **SECOND PRESSING** | dark/printerly — riso + newsprint, typographic poster | Klim Type Foundry (+ Risotto, Bureau Borsche) | A fictional risograph print show: misregistered duotone masthead, halftone plate, a ruled plates-ledger instead of cards. |
| v0_2 | **Quiet Holdings** | quiet/archival — reading-room finding aid, photo archive | Atlas of Places (+ Public Domain Review, CMA Open Access) | A fictional viewing room laying out six real CC0 photographs as a finding aid: hand-placed prints, mounts, red-pencil annotations, marginalia. |
| v0_3 | **SUPERFIZZ** | bright/pop — saturated soda packaging | Morag Myerscough (+ Camille Walala, Hey Studio) | A fictional "bureau of loud soft drinks": saturated colour-blocking, fat display type, die-cut sticker seals, a Fizz-o-meter bar chart. |

Each is a single self-contained `index.html` (no runtime CDN), uses only free/OFL/CC0
or self-authored material, and ships with notes + desktop/mobile screenshots +
a self-evaluation.

## 3. Conclusion

- **All three escaped the generic AI-LP** — no centred-hero → eyebrow → H1 → subtitle →
  pill stack, no frosted cards, no even card grid, no dark-gradient-plus-floating-cards,
  no orb/pill reliance — and each reads as a "screen-as-artwork", not a web template.
- **The three registers are clearly distinct** (dark/printerly vs quiet/archival vs
  bright/pop), so the result is not one lucky aesthetic: the method, not the mood, is
  doing the work. Three for three.
- **Verdict: the Reference-first mimic system is adopted as the standard production
  route for CreativeVault design work**, with the caveats in §6.

## 4. Success factors (what actually worked)

- **3 references** — gather at least three strong, non-SaaS, non-card-UI sites and note
  URL / why / borrow / don't-borrow for each.
- **1 lead reference** — commit to a single strongest lead (plus 1–2 support refs);
  don't average them.
- **avoid / aim list** — write the explicit "avoid" and "aim for" lists up front. This
  was the highest-leverage step every time: it mechanically removes pill / centred-hero /
  cards and locks the direction to one idea.
- **material-first decision** — decide fonts and the hero material before layout
  (v0_2 secured real CC0 photos first; v0_3 fixed the palette + bottle + seals first).
  This is what made the intended hero real instead of decorative.
- **single concrete artifact** — always build one real `index.html`, never stop at
  candidates.
- **screenshots** — render desktop first-view + full page + mobile and actually look.
- **self-evaluation** — score honestly (incl. residual AI-ness) and name one next change.

## 5. Standard route going forward

```
1. Pick register/intent (and keep it different from recent builds).
2. Find 3 strong references → choose 1 lead (+1–2 support). Record borrow/don't-borrow.
3. Write the avoid-list and the aim-list explicitly.
4. Decide materials FIRST: fonts (OFL, self-hosted) + hero material (CC0 image OR
   self-made shapes). Record URLs + licenses in notes/materials_used.
5. Build ONE self-contained index.html. Make the same visual language run top-to-bottom.
6. Render screenshots (desktop first-view, full, mobile); look at them.
7. Write a self-evaluation: scores + honest residual AI-ness + one next change.
```

Deliverable shape per build: `index.html`, `notes/{reference_observation, materials_used,
build_log, self_evaluation}.md`, `screenshots/{01_desktop_firstview, 02_desktop_full,
03_mobile_full}.png`.

## 6. Cautions for next time

- **Do not make same-kind elements uniform in treatment.** The recurring weakness across
  all three was per-element processing going templated — v0_2's identical photo mounts,
  v0_3's identical sticker frames. Placement was broken well; *treatment* was not. Next
  builds should deliberately vary frame / shadow / cut / texture element by element.
- **Observe at least one real reference screenshot.** All three decomposed references from
  *known* design language rather than a fresh live capture (medium fidelity). Upgrade the
  observation step to require capturing and reading at least one real reference screenshot.
- **Start from the visual language, not an existing concept name.** Lead with register +
  references + avoid/aim, and let the (fictional) theme follow. Don't start from a
  pre-named concept and decorate it.

## 7. Boundaries honored

- Work stayed inside **CreativeVault** only (`70_design_experiments/`).
- **No MedicalVault / LocalOnlyProjects / other vaults / Downloads** referenced.
- **No secrets / API keys / tokens / webhooks / .env / raw API responses** read.
  (External access was limited to keyless open data — Google Fonts OFL, CMA Open Access
  CC0 — recorded per build in `notes/materials_used`.)
- This summary is a **new single file**; the three experiments were not modified.
</content>
