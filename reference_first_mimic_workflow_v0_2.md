# RFM Workflow v0.2 — Reference-first Mimic Workflow (gated)

Created: 2026-06-13
Status: **adopted** — supersedes v0.1 as the standard design-production route.
v0.1 (`reference_first_mimic_workflow_v0_1.md`) is kept for history.

## What changed vs v0.1 (and why)
v0.1 wrote its key steps as *rules*, so they kept getting skipped (all three
validation builds + the hospital poster decomposed references "from memory"; a
flyer once fabricated a "DOORS 18:45" line; the hospital poster shipped
all-placeholder fields). v0.2 turns the highest-leverage steps into **hard gates**
— you cannot proceed past a gate without the artifact existing:

- **GATE 0 — brief & scope confirmed (all formats).** Before any design, the USER
  confirms purpose/use and the required content. Web/LP: hero message + primary CTA
  + rough scope (how many links / nav items / sections; desktop + mobile).
  Poster / flyer / single image: every required field listed and its value confirmed
  one by one — unknowns marked `[PLACEHOLDER]`. **Never invent, auto-fill, or add an
  unrequested field.** Recorded in `notes/brief.md`.
- **GATE 1 — human picks the lead.** I present 3 candidate references; **you**
  choose the one lead ("これがいい"). I never auto-pick the lead.
- **GATE 2 — a real reference screenshot exists.** A PNG of the chosen lead must
  exist in `screenshots/refs/` before any decompose/observe/build work begins.
  - **Screenshot mode: auto-default + manual fallback** (decided 2026-06-13).
    I capture with `tools/rfm_shot.py`; if it reports SUSPECT/FAIL (cookie wall,
    login, blocked, blank), **you** capture manually and drop the PNG in.
- **GATE 3 — hero + structure approved (Web only).** TWO-step. Both must be signed
  off by the USER before building the rest of the page.
  - **3a. Hero look** — render the hero first-view ALONE
    (`screenshots/hero_checkpoint.png`), show it, USER confirms direction/feeling.
  - **3b. Structure** — write `notes/structure_proposal.md` enumerating
    EXACT nav labels (not just "4 items"), section order with IDs, what lives in
    each section (rows/items), mobile nav behavior, link count, and which fields
    stay `[PLACEHOLDER]`. USER ticks each one. **Hero "looks good" is NOT
    structure approval** — a separate sign-off is required.

Everything else (3 refs, avoid/aim, materials-first, one artifact, per-element
non-uniformity, top-to-bottom strength, self-eval) carries over unchanged.

---

## 1. Names / triggers / when (unchanged from v0.1)
- RFM Workflow / Reference-first Mimic Workflow / 参照先行ミミック制作.
- Triggers: 「RFMで1本作って」「参照先行で作って」「今までと違う絵でLP作って」
  「AIっぽくないWebを1本作って」「Reference-first mimicで作って」.
- Use for new Web/LP/top pages, direction trials, prototypes, visual experiments.
- Do NOT use for copy edits, bug fixes, minor CSS, MedicalVault, anything with
  secrets, or final polish of an already-adopted design.

## 2. Gated route

```
   ┌──────── GATE 0 — BRIEF & SCOPE (human confirms) ──────────────────┐
   │  Confirm purpose/use + required content BEFORE any design.         │
   │  Web/LP : hero message + primary CTA + rough scope (how many       │
   │           links / nav items / sections; desktop + mobile).         │
   │  Poster / flyer / single image : list EVERY required field and     │
   │           confirm each value one by one; unknowns = [PLACEHOLDER]. │
   │  Never invent / auto-fill / add an unrequested field.              │
   │  Record in notes/brief.md. No "OK" from user → do not proceed.     │
   └────────┬──────────────────────────────────────────────────────────┘
            │
STEP 0  Pick register/intent — keep it different from recent builds
        (check 70_design_experiments/AGENTS.md "known bias to AVOID").

STEP A  Present 3 references (strong, non-SaaS, non-card-UI).
        For each: name / URL / why / borrow / don't-borrow.
            │
   ┌────────▼ GATE 1 — HUMAN PICKS THE LEAD ───────────────────────────┐
   │  User chooses 1 lead (+1–2 support). Record pick + reason in       │
   │  notes/reference_candidates.md. Do NOT proceed until you choose.   │
   └────────┬──────────────────────────────────────────────────────────┘
            │
STEP B  Screenshot the lead (auto-default; run from inside the build dir):
            python3 ../tools/rfm_shot.py "<lead-url>" \
                screenshots/refs/lead_firstview.png
        If SUSPECT/FAIL → capture manually, save to the same folder.
            │
   ┌────────▼ GATE 2 — REAL SCREENSHOT EXISTS ─────────────────────────┐
   │  screenshots/refs/ must contain a verified, looked-at PNG.         │
   │  No file → STOP. Decompose/build do not start.                     │
   └────────┬──────────────────────────────────────────────────────────┘
            │
STEP C  Decompose from the screenshot: composition / whitespace / material /
        typography / information density / non-uniformity.
STEP D  Write borrow vs don't-borrow, then avoid-list and aim-list.
STEP E  Decide MATERIALS FIRST.
        Fonts: OFL / self-hosted (record license).
        Hero / supporting material — USE EXTERNAL MATERIAL AGGRESSIVELY when the
        register calls for real photo / print / artwork texture (Dia-style museum
        editorial, archive, publication, photography-led pages). Do NOT default to
        "self-made shapes" — that path silently weakens any image-led register.
        Allowed sources (record URL + license + attribution in notes/materials_used):
          • CC0 / Public Domain (Wikimedia Commons, museum open-access, etc.)
          • CC-BY / CC-BY-SA  (record attribution string + link)
          • Official press kits / brand assets per their stated terms
          • Reference screenshots for observation only (fair use; not redistributed)
          • Self-made shapes  (good for diagram / icon / type-led pieces)
        Pick the strongest material for the register — not the safest.
STEP F  Build in a NEW directory. Same visual language top-to-bottom.
        ├─ Web/LP: render the HERO first-view ALONE →
        │          screenshots/hero_checkpoint.png
        │     ┌────▼ GATE 3a — HERO LOOK APPROVED (Web only) ────────────┐
        │     │  Show the hero; USER confirms direction/feeling.         │
        │     │  No "OK" → revise the hero.                              │
        │     └────┬──────────────────────────────────────────────────────┘
        │          │
        │          ▼   Write notes/structure_proposal.md (enumerated)
        │     ┌────▼ GATE 3b — STRUCTURE APPROVED (Web only) ────────────┐
        │     │  Nav labels (each one) / section order + IDs / what      │
        │     │  lives in each section / mobile nav behavior / link      │
        │     │  count / which fields stay [PLACEHOLDER]. USER ticks     │
        │     │  EACH item. Hero-look OK ≠ structure OK.                 │
        │     │  No sign-off → do NOT build the rest yet.                │
        │     └────┬──────────────────────────────────────────────────────┘
        │          └─ then build the rest of the page.
        └─ Poster / single image: build the one artifact (fields per brief).
STEP G  Render output screenshots (desktop first-view, full, mobile); look.
STEP H  Self-evaluate: scores + honest residual AI-ness + one next change.
```

## 3. Strong rules (carried from v0.1 §6)
- Start from the **visual language**, not a pre-named concept.
- Never stop at candidates — always ship **one** built artifact.
- Do not fall back to: centred hero / pill CTA / frosted glass card / even card
  grid / dark gradient + floating cards.
- **Vary same-kind elements in at least 3 patterns** (frame / shadow / bleed-cut /
  texture / rotation / tone-density / whitespace). Placement varying is not enough.
- Keep strength **top-to-bottom** — no plain info-footer collapse.

## 4. Standard output (adds notes/brief.md + screenshots/refs/)
```
<new-dir>/
  index.html                         (or make_poster.py + .png/.pdf for posters)
  assets/
  notes/brief.md                     ← GATE 0 brief + required-fields confirm (NEW)
  notes/reference_candidates.md      ← the 3 + GATE 1 pick record (NEW)
  notes/reference_observation.md     ← written FROM the screenshot (GATE 2)
  notes/materials_used.md
  notes/structure_proposal.md        ← GATE 3b enumerated structure (Web only) (NEW)
  notes/build_log.md
  notes/self_evaluation.md
  screenshots/refs/lead_firstview.png   ← GATE 2 artifact (NEW)
  screenshots/hero_checkpoint.png       ← GATE 3a artifact, Web only (NEW)
  screenshots/01_desktop_firstview.png
  screenshots/02_desktop_full.png
  screenshots/03_mobile_full.png
```
Start by copying `_rfm_template/` into the new build directory.

## 5. Evaluation criteria (unchanged)
Score honestly + name one next change: different picture than before? lead
composition actually used? generic-AI-LP feel reduced? material feel?
non-uniformity? screen-as-artwork? strong top-to-bottom? same-kind elements
non-uniform (not templated)?

## 6. Boundaries
- **CreativeVault only.** No MedicalVault / LocalOnlyProjects.
- Screenshots = **read-only** web fetch. No login, no posting/sending/deleting.
- No secrets / .env / API key / token / webhook / raw response.
- External material is **encouraged**, not avoided. Allowed: OFL / CC0 / Public
  Domain / CC-BY / CC-BY-SA / official press-kit assets per their terms / fair-use
  reference screenshots for observation. Always record URL + license + attribution
  in `notes/materials_used.md`. Default to the strongest material for the register.
- No pasting external code; no wholesale copy of a reference (structure only).
