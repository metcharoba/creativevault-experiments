# RFM Gate Checklist (copy this whole folder per build)

Route: `reference_first_mimic_workflow_v0_2.md`. Work top to bottom. A gate that
is not checked = the build is NOT allowed to proceed past it.

## GATE 0 — brief & scope confirmed  🔒
- [x] `notes/brief.md` filled (Web → §A scope incl. link/section count;
      Poster/single → §B every required field + value).
- [x] No invented / auto-filled / unrequested fields; unknowns = [PLACEHOLDER].
- [x] **User signed off the brief** ("OK").
> No sign-off → do not pick references / do not design.

## STEP 0 — register
- [x] Register/intent chosen, and it differs from recent builds
      (checked against `../AGENTS.md` "known bias to AVOID").

## GATE 1 — human picks the lead  🔒
- [x] 3 references presented (name / URL / why / borrow / don't-borrow).
- [x] **User chose 1 lead** (+1–2 support) and it is recorded in
      `notes/reference_candidates.md`.
> Do not pass GATE 1 by self-picking. Wait for the user's "これがいい".

## GATE 2 — real reference screenshot exists  🔒
- [x] `screenshots/refs/lead_firstview.png` exists for the chosen lead.
- [x] It was **captured**, not imagined:
      `python3 ../tools/rfm_shot.py "<lead-url>" screenshots/refs/lead_firstview.png`
      (auto-default; if SUSPECT/FAIL → user captures manually, same path).
- [x] The screenshot was actually **looked at** (not just file-present).
> No verified screenshot file → STOP. `reference_observation.md` stays empty.

## After the gates
- [x] STEP C decompose written FROM the screenshot → `notes/reference_observation.md`
- [x] STEP D borrow/don't-borrow + avoid-list + aim-list written
- [x] STEP E materials decided FIRST + licenses recorded → `notes/materials_used.md`

### GATE 3 — hero approved (Web only)  🔒
- [x] Hero first-view rendered ALONE → `screenshots/hero_checkpoint.png`
- [x] **User confirmed** direction + scope ("this hero + N links/sections is right").
  - Confirmed after reopening: main nav should be `Hero / On View / Rooms / Collection Notes`; `X` and `note` move to small top-right external links under `Elsewhere`; `Studio Room` and `Letter Cabinet` appear as preparing rooms and in the footer.
> No "OK" → revise the hero; do NOT build the rest yet. (Skip GATE 3 for posters/single images.)

- [x] STEP F artifact built in this directory (top-to-bottom strength)
- [x] STEP F per-element treatment varied ≥3 patterns (record in build_log)
- [x] STEP G output screenshots rendered + looked at
- [x] STEP H self-evaluation written incl. residual AI-ness + one next change
