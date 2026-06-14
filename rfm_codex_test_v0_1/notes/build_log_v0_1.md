# Build Log v0.1

## Workflow notes

- Read the approved RFM workflow and validation summary.
- Used `frontend-design` guidance for a specific visual register and anti-template checks.
- Chose a fictional subject only after reference/material decisions: Signal Cabinet 23.
- Did not read existing v0_1 / v0_2 / v0_3 implementation files or their screenshots.

## Build steps

1. Created the new experiment folder:
   - `70_design_experiments/rfm_codex_test_v0_1/`
   - `assets/`
   - `notes/`
   - `screenshots/`
2. Searched and recorded references:
   - Space Jam 1996
   - Cameron's World
   - Windows 93
   - Telehack
3. Captured the lead reference screenshot:
   - `notes/lead_reference_spacejam_1996.png`
4. Downloaded and recorded licensed external assets:
   - Arecibo message SVG from Wikimedia Commons.
   - Micro 5 and IBM Plex Mono font files from Google Fonts.
5. Authored local SVG materials:
   - `assets/kiosk_disc.svg`
   - `assets/pulsar_sheet.svg`
   - `assets/noise_tile.svg`
6. Built `index.html` as a single local HTML page using local assets.
7. Captured screenshots with headless Chrome.
8. Reworked viewport-dependent CSS after the first full screenshot showed `vh` sections stretching under tall screenshot viewports.
9. Captured final true full-page screenshots through Chrome DevTools Protocol.

## Display verification

Final screenshot outputs:
- `screenshots/01_desktop_firstview.png`
- `screenshots/02_desktop_full.png` at 1440 x 3442
- `screenshots/03_mobile_full.png` at 405 x 6248

Verification notes:
- Desktop first view shows the intended lead-reference-derived structure: central specimen/object cluster with irregular orbiting labels.
- Desktop full screenshot includes the lower sections and final closing module.
- Mobile full screenshot includes the full page to the final closing note.
- Text remains legible and no major incoherent overlap was observed.
- The page can be opened directly as `index.html`; no dev server is required.

## Adjustments made after screenshot review

- Added caps to hero and stage heights so tall screenshot viewports do not stretch the first section.
- Added caps to the specimen window and closing section so mobile/full screenshots stay representative.
- Kept the intentional overlaps in the first-view object cluster, because the reference language depends on placed objects rather than clean layout lanes.

## Boundary check

- Work stayed in `CreativeVault`.
- No MedicalVault, LocalOnlyProjects, other vaults, Downloads, secrets, `.env`, API keys, tokens, webhooks, or raw responses were used.
- Existing files outside the new experiment directory were not modified.
