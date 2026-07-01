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

## Hero material (v1 — superseded 2026-07-01)
- Type: external public-domain image + self-authored layout.
- Source + URL: Wikimedia Commons, `File:StaatlichesBauhausTitelseite.jpg` — https://commons.wikimedia.org/wiki/File:StaatlichesBauhausTitelseite.jpg
- Asset path: `assets/images/staatliches-bauhaus-titelseite.jpg` (file kept, no longer referenced by hero)
- Image description: 1923 title page for Staatliches Bauhaus in Weimar 1919-1923, designed by László Moholy-Nagy.
- License: Public Domain Mark 1.0 / public domain per Wikimedia Commons file page.
- Notes: Used as the hero's large cropped typographic artifact until replaced by the 3D hero below.

## Hero material (v2 — current, 2026-07-01)
- Type: real 3D scan (GLB), rendered live in-browser via Three.js, replacing the static hero image.
- Source + URL: Sketchfab, "Armillary sphere (1771)" — https://sketchfab.com/3d-models/armillary-sphere-1771-41e23659c75241459eec6477d9e77c93
- Author: Virtual Museums of Małopolska — https://sketchfab.com/WirtualneMuzeaMalopolski (digitization of an object held by the Jagiellonian University Museum, Collegium Maius, Kraków)
- Asset path: `assets/models/armillary-sphere-1771.glb` (compressed from the original 64MB glTF download to 1.82MB via `@gltf-transform/cli optimize --texture-size 1024 --texture-compress webp`, meshopt geometry compression). Original license file kept at `assets/models/armillary-sphere-1771-LICENSE.txt`.
- License: CC BY 4.0 (http://creativecommons.org/licenses/by/4.0/) — attribution required, commercial use allowed. Required credit reproduced verbatim in `.exhibit-label small` on the page, plus this note.
- Rendering: `assets/js/hero-3d.js`, vanilla Three.js loaded as `<script type="module">` via an import map. On load, the model's real vertex positions are captured and each vertex is displaced along a random direction/magnitude ("scattered"), then eased back to its true position over ~2.2s (`easeOutBack`), after which it settles into a slow continuous auto-rotate. Positions used are always the object's real scanned geometry — the assembly animation is a deterministic display of real data, not AI-generated. Respects `prefers-reduced-motion` (skips scatter + auto-rotate, renders once at rest) and pauses the idle rotate loop via `IntersectionObserver` when the hero scrolls out of view.
- Three.js: vendored locally (not CDN) at `assets/js/vendor/three/` — `three@0.169.0` core + `GLTFLoader`/`BufferGeometryUtils`/`meshopt_decoder`/`RoomEnvironment` from the same package version, MIT license. Originally wired via a jsdelivr CDN import map; switched to a same-origin vendor copy after an automated security review flagged the missing-SRI supply-chain risk (2026-07-01), matching the existing local-fonts convention.
- Notes: Chosen over an AI image→3D pipeline (Higgsfield `generate_3d`) after concluding that route was too likely to fail for this content; chosen over a plain AI-generated video assembly (Higgsfield `generate_video`) because precise multi-part convergence is a known weak point of video diffusion models. Verified locally via a temporary `python3 -m http.server` + Playwright/CDP screenshot check (desktop + mobile viewports, no console errors) before shipping.

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
