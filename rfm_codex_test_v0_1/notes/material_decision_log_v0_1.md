# Material Decision Log v0.1

## Chosen subject

Fictional subject: **Signal Cabinet 23**, a 1990s educational multimedia kiosk for inspecting interstellar message fragments, CD-ROM teaching plates, and machine annotations.

Audience: people inspecting a visual design experiment, not real customers.

Single job: demonstrate whether Codex can use RFM plus material-first decisions to escape generic AI LP language.

## Material strategy before implementation

Needed materials:
- A real external diagram that can anchor the page as an information object.
- A locally hosted display font with a low-resolution / kiosk label character.
- A locally hosted monospaced utility face for technical labels and dense readings.
- Self-authored SVG objects: disc plate, pulsar sheet, dither/noise tile, and small interface markers.
- CSS textures: scanlines, pixel-grid overlays, misregistration, and non-uniform panel borders.

Why CSS alone is not enough:
- The core test is whether material can become the visual subject. CSS-only rectangles would likely slide back into generic panels.
- A real diagram has irreducible detail, aspect ratio, and cultural specificity that is difficult to fake with simple gradients.
- Fonts change the page's voice more reliably than generic system sans-serif.
- Self-authored SVGs allow object-specific shapes without copying reference artwork.

External materials to use:
- `assets/arecibo_message.svg` from Wikimedia Commons.
- `assets/micro-5-400.ttf` from Google Fonts.
- `assets/ibm-plex-mono-{400,500,700}.ttf` from Google Fonts.

Self-authored materials to create:
- `assets/kiosk_disc.svg`: a CD-ROM-like teaching disc object.
- `assets/pulsar_sheet.svg`: a line-map / signal direction sheet.
- `assets/noise_tile.svg`: a small dither texture tile.
- Inline SVG/CSS markers for calibration ticks, node connectors, and scan blocks.

Where the materials become the visual lead:
- Arecibo SVG: vertical central specimen, cropped and repeated as the main "signal strip".
- CD-ROM disc: first-view counterweight and lower-page artifact.
- Pulsar sheet: diagrammatic support object in both the first view and lower "route table".
- Noise/scan textures: applied across the whole page so the material language continues below the fold.

Non-uniformity rule:
- Repeated node panels will use at least three treatments:
  1. Cut-corner hard frame with yellow label tab.
  2. Offset shadow frame with magenta calibration stripe.
  3. Bleeding image/object slab with rotated caption and no full border.
- Lower modules will also vary frame, shadow, rotation, tone, density, and whitespace.

## Design stack plan

Used:
- `frontend-design`: for visual planning, avoiding template LP patterns, and making a specific subject/register.

Not used:
- `algorithmic-art`: no p5/particle/generative-art build was needed; small deterministic textures are enough.
- `canvas-design`: output is an HTML page, not a static poster/PDF.
- `theme-factory`: a bespoke palette is more appropriate than a preset theme.
- `brand-guidelines`: no Anthropic-branded artifact.
- `web-artifacts-builder`: single-file HTML is requested; React/shadcn would add unnecessary structure.
