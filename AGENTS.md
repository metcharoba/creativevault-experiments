# AGENTS.md — 70_design_experiments

Design work in this folder follows the **Reference-first mimic** route.
Canonical sources (read these first):
- `reference_first_mimic_workflow_v0_2.md` — **the route (gated; current).**
- `reference_first_mimic_workflow_v0_1.md` — previous route, kept for history.
- `reference_first_mimic_validation_summary_v0_1.md` — rationale + §6 cautions.
- `_rfm_template/` — copy this whole folder to start a build; `00_GATES.md` is
  the per-build checklist. Auto screenshot helper: `tools/rfm_shot.py`.

This file adds the bias-avoidance learned from reviewing all artifacts on 2026-06-13.
It applies to every agent (Codex included) doing design work here.

## Standard route (do every build) — HARD GATES
0. **GATE 0 🔒 — brief & scope (the USER confirms).** Before any design, confirm
   purpose/use + required content in `notes/brief.md`. Web/LP: hero message + primary
   CTA + rough scope (how many links / nav items / sections; desktop+mobile).
   Poster/flyer/single image: list EVERY required field and confirm each value one by
   one; unknowns = [PLACEHOLDER]. **Never invent / auto-fill / add an unrequested
   field.** No user "OK" → do not pick references / do not design.
1. Pick register/intent — and keep it DIFFERENT from recent builds (see "Known bias").
2. Present 3 strong non-SaaS / non-card references (name/URL/why/borrow/don't-borrow).
   **GATE 1 🔒 — the USER picks the lead.** Do not self-pick; wait for "これがいい".
   Record the pick in `notes/reference_candidates.md`.
2b. Screenshot the chosen lead (run from inside the build dir):
   `python3 ../tools/rfm_shot.py "<url>" screenshots/refs/lead_firstview.png`
   (auto-default; if SUSPECT/FAIL the user
   captures manually, same path). **GATE 2 🔒 — a real, looked-at screenshot must
   exist before any decompose/build.** No file → STOP.
3. Write the explicit **avoid-list** and **aim-list** up front (highest-leverage step).
4. Decide materials FIRST. **Use external material aggressively** for photo /
   print / artwork / archive registers — Dia-style museum editorial,
   publication, archive, photography-led pages collapse into a weak CSS-block
   approximation if you fall back to "self-made shapes". Allowed sources (record
   URL + license + attribution in `notes/materials_used`):
   - CC0 / Public Domain (Wikimedia Commons, museum open-access)
   - CC-BY / CC-BY-SA (record attribution string + link)
   - Official press kits / brand assets per their stated terms
   - Reference screenshots for observation only (fair use; not redistributed)
   - Self-made shapes (use for diagram / icon / type-led pieces, not by default)
   Fonts: OFL, self-hosted.
5. Build ONE self-contained artifact (`index.html`, or `.png`/`.pdf` for print).
   **Web/LP only — GATE 3 is TWO-step 🔒**, both signed off by the USER before
   building the rest of the page:
   - **3a Hero look:** render the hero first-view ALONE
     (`screenshots/hero_checkpoint.png`); USER confirms direction/feeling.
   - **3b Structure:** write `notes/structure_proposal.md` enumerating EXACT
     nav labels (not "4 items"), section order with IDs, what lives in each
     section, mobile nav behavior, link count, and which fields stay
     `[PLACEHOLDER]`. USER ticks each one. **Hero "looks good" is NOT structure
     approval.** No sign-off → do NOT build the rest yet.
   Posters / single images skip GATE 3.
6. Render and actually look at screenshots (desktop first-view, full, mobile —
   or detail crops for print).
7. Write `notes/self_evaluation`: 0–5 scores, honest residual AI-ness, the
   difference vs recent builds, and one concrete next change.

Deliverable shape: artifact + `notes/{reference_observation, materials_used,
build_log, self_evaluation}.md` + screenshots. (This holds even for one-shot
poster/flyer builds made via a design skill — still write a self_evaluation and
record fonts/licenses.)

## Known bias to AVOID (reviewed 2026-06-13, all 9 artifacts)
The collection collapses into two poles plus a few house-tics. Do not reinforce
them — diversify on purpose.
- **Two poles**: quiet riso/archival editorial  ⇄  loud primary-color pop/comic.
  Under-explored, prefer these next: mono / one-color minimal typography;
  CC0 photo-led editorial; diagram / map / data-led; organic / tactile material;
  3D / print-material; Japanese vertical-set layout.
- **Overused motif**: "SIGNAL / transmission" (Signal Dept, Signal Cabinet,
  Creative Signal Night) and the copy "fragments / experiments / future / ideas".
  Reach for fresh vocabulary and metaphor.
- **House-tics**: halftone dots + print misregistration; cream/bone paper with a
  red + blue (+yellow) palette; condensed-bold (loud) or high-contrast serif+italic
  (quiet). Try at least one build that explicitly BANS these.

## Recurring weaknesses (from the self-evaluations + the 2026-06-13 review)
- **Per-element treatment goes uniform.** Placement gets broken well, but every
  same-kind element (cards, photo mounts, stickers, speech bubbles, info panels)
  defaults to one frame / shadow / cut / texture, which reads templated. Vary the
  treatment element by element.
- **Observation fidelity.** Builds tend to decompose references from memory rather
  than a real capture. **Now a hard gate (GATE 2):** observe at least ONE real
  reference screenshot before building. If a brief cites reference images and none
  are attached, obtain/observe one (or ask) before starting.
- **Concept-first decoration.** Start from visual language + references + avoid/aim,
  and let any (fictional) theme follow. Do NOT start from a pre-named concept and
  decorate it.

## Before starting any new build
List the existing registers / motifs / palette / tics already in this folder, then
deliberately choose something different. New ≠ a fresh coat on the same two poles.
