# Materials Used (decided FIRST — STEP E)

> Decide fonts + hero material before layout. Record every source + license.

## Fonts
| Font | Role | Source | License / usage |
|------|------|--------|-----------------|
| Bricolage Grotesque 500/700 | identity, hero message, nav, section headings | Reused local files from `reference_first_mimic_test_v0_3/assets/fonts/`; original family: Google Fonts | SIL Open Font License 1.1 |
| IBM Plex Mono 400/500 | object labels, captions, catalog marks | Reused local files from `rfm_codex_test_v0_1/assets/`; original family: IBM / Google Fonts | SIL Open Font License 1.1 |

## Palette
- White: `#ffffff`
- Ink black: `#0a0a0a`
- Archive red: `#ff241f`
- Specimen yellow: `#e4c43a`
- Deep green: `#0e4a33`
- Warm gray: `#efefed`
- Utility gray: `#767676`

## Hero material
- Type: external public-domain image + self-authored layout.
- Source + URL: Wikimedia Commons, `File:StaatlichesBauhausTitelseite.jpg` — https://commons.wikimedia.org/wiki/File:StaatlichesBauhausTitelseite.jpg
- Asset path: `assets/images/staatliches-bauhaus-titelseite.jpg`
- Image description: 1923 title page for Staatliches Bauhaus in Weimar 1919-1923, designed by László Moholy-Nagy.
- License: Public Domain Mark 1.0 / public domain per Wikimedia Commons file page.
- Notes: The image is used as the hero's large cropped typographic artifact. The surrounding header, black exhibit label, Japanese hero message, seal, and preview section are self-authored for this build while structurally referencing Letterform Archive.

## Supporting Image Material

- Source + URL: Wikimedia Commons, `File:Caslon 1841 specimen Sixteen-line Pica fat face typeface.jpg` — https://commons.wikimedia.org/wiki/File:Caslon_1841_specimen_Sixteen-line_Pica_fat_face_typeface.jpg
- Asset path: `assets/images/caslon-1841-fat-face.jpg`
- Image description: Specimen of the Caslon type foundry's Sixteen-line Pica fat face typeface, 1841.
- License: Public domain / Public Domain Mark 1.0 per Wikimedia Commons API metadata and file page.
- Notes: Used in the lower `Collection Notes` section to avoid repeating the Bauhaus hero image and to deepen the typography archive feel.

## Boundaries
Inside CreativeVault `70_design_experiments/` only. No MedicalVault /
LocalOnlyProjects. No secrets, no network side-effects. If a font is a system
font, it is used for LOCAL rasterization only (not embedded / not redistributed).
