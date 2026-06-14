# Materials Used — Reference-first mimic test v0.2

Created: 2026-06-12

## Images (all CC0 / Public Domain — Cleveland Museum of Art Open Access)

Source API: `https://openaccess-api.clevelandart.org` (keyless, `cc0=1`).
CDN: `https://openaccess-cdn.clevelandart.org`. All six are `share_license_status: CC0`.
Used as the page's primary visual material (placed, cropped, framed, annotated).

| Local file | Accession | Title | Maker | Date | Technique | Image URL |
|---|---|---|---|---|---|---|
| `assets/images/01_portrait.jpg` | 2017.8.2 | Untitled (Portrait of a Woman) | Etienne Carjat | 1879 | Photograph on enamel in copper-alloy frame | https://openaccess-cdn.clevelandart.org/2017.8.2/2017.8.2_web.jpg |
| `assets/images/02_pictorialist.jpg` | 1985.203 | Untitled | Robert Demachy | c. 1900–1906 | gum bichromate print | https://openaccess-cdn.clevelandart.org/1985.203/1985.203_web.jpg |
| `assets/images/03_botanical.jpg` | 2019.9 | Convolvulus and Metamorphosis of the Convolvulus Hawk Moth | Maria Sibylla Merian | c. 1670–90 | watercolour on vellum | https://openaccess-cdn.clevelandart.org/2019.9/2019.9_web.jpg |
| `assets/images/04_insects.jpg` | 2022.9 | Studies of Insects | Johannes Bronckhorst | c. 1665–1727 | watercolour & opaque watercolour | https://openaccess-cdn.clevelandart.org/2022.9/2022.9_web.jpg |
| `assets/images/05_landscape.jpg` | 1993.162 | Landscape | Henry White | 1856 | albumen print from wet collodion | https://openaccess-cdn.clevelandart.org/1993.162/1993.162_web.jpg |
| `assets/images/06_acropolis.jpg` | 2021.58 | View of the Acropolis | Adolphe Braun & Co. | c. 1880s | mammoth carbon print | https://openaccess-cdn.clevelandart.org/2021.58/2021.58_web.jpg |

- License note: CMA marks these Open Access **CC0** (public domain dedication);
  no permission or attribution required. On-page credits are given anyway, as good
  practice, and the page states the works are public domain shown as a design exercise.
- Note: AIC (artic.edu) IIIF was tried first but is behind a Cloudflare challenge
  (HTTP 403); switched to CMA, which serves CC0 JPEGs directly.

## Fonts (downloaded locally, self-hosted — no runtime CDN)

| File | Family | License |
|---|---|---|
| `assets/fonts/CormorantGaramond-500.woff2` | Cormorant Garamond 500 | OFL-1.1 |
| `assets/fonts/CormorantGaramond-600.woff2` | Cormorant Garamond 600 | OFL-1.1 |
| `assets/fonts/CormorantGaramond-500italic.woff2` | Cormorant Garamond 500 italic | OFL-1.1 |
| `assets/fonts/Archivo-400.woff2` | Archivo 400 | OFL-1.1 |
| `assets/fonts/Archivo-600.woff2` | Archivo 600 | OFL-1.1 |

Source: Google Fonts (fonts.gstatic.com), latin subset only. Different families from
v0.1 (which used Big Shoulders Display + Fraunces).

## Self-authored

- Paper grain, dust speckle, vignette, corner crop-marks, mount frames, corner ticks,
  red annotation call-outs and leader stubs — all self-made CSS/SVG.

## Boundaries honored

- Worked only inside `.../reference_first_mimic_test_v0_2/`.
- No MedicalVault / LocalOnlyProjects / other vaults. No secrets / API keys / tokens
  / .env. The CMA Open Access API is keyless public data.
- No existing files overwritten. No external code pasted. No reference site copied.
- No CreativeWorld / NMG / SECOND PRESSING context, copy, or design reused.
</content>
