# Build Log

- Date: 2026-06-13
- Build dir: `70_design_experiments/creativevault_thought_gallery_rfm_v0_1`
- Route: reference_first_mimic_workflow_v0_2.md

## Gate trail (proof, not promise)
- GATE 1 lead pick: see `reference_candidates.md` — Letterform Archive chosen by user, Cabinet Magazine retained as support.
- GATE 2 screenshot: `screenshots/refs/lead_firstview.png` — captured with `rfm_shot.py`, looked at: yes.
- GATE 3 hero checkpoint: `screenshots/hero_checkpoint.png` — user said the overall picture looked good and requested English copy. After process correction, structure was explicitly confirmed: main nav `Hero / On View / Rooms / Collection Notes`; top-right `Elsewhere` links for X/note; preparing rooms for Studio Room and Letter Cabinet; footer Elsewhere list.

## Per-element non-uniformity (≥3 patterns) — what I actually varied
| Same-kind element | Treatment A | Treatment B | Treatment C |
|-------------------|-------------|-------------|-------------|
| Hero/section image areas | Public-domain Bauhaus image cropped full-width as a large artifact | Same image recropped as smaller article thumbnail | Pure CSS catalog block in yellow/red/black |
| Content entries | Image-led experiment entry | Text-led notes entry with ruled-paper texture | Abstract catalog/index entry with geometric blocks |
| Sections | White museum/news listing | Black room-index band with horizontal rules | White collection notes feature spread |
| Navigation/labels | Top announcement strip | Centered identity masthead | Black exhibit label over image |

## Top-to-bottom strength
- The lower half keeps the Letterform-like institutional rhythm: On View three-up listings, a black Rooms band, and a Collection Notes feature spread. It avoids footer-only collapse by giving each section a different material treatment and headline scale.

## Notes / decisions / problems hit
- Initial Dia-led hero felt too weak/generic and was abandoned.
- User requested a more museum-like direction; Letterform Archive became the lead.
- User then requested external image material. Used Wikimedia Commons public-domain Bauhaus title page and recorded source/license in `materials_used.md`.
- Visible copy was switched to English after hero checkpoint feedback.
- Mobile screenshots initially clipped right edges in headless Chrome; mobile CSS was constrained and headings set to wrap safely.
- Process issue: I advanced from hero checkpoint into the full build without pausing for an explicit section-structure confirmation. This was corrected; the user confirmed the final nav/section plan through questions.
- Final small revision: added top-right Elsewhere links, changed main nav to the four page sections, added preparing Studio Room and Letter Cabinet rows, added footer Elsewhere links, and replaced the repeated lower Bauhaus image with a public-domain Caslon specimen image.
