# RFM Gate Checklist (copy this whole folder per build)

Route: `reference_first_mimic_workflow_v0_2.md`. Work top to bottom. A gate that
is not checked = the build is NOT allowed to proceed past it.

## GATE 0 — brief & scope confirmed  🔒
- [ ] `notes/brief.md` filled (Web → §A scope incl. link/section count;
      Poster/single → §B every required field + value).
- [ ] No invented / auto-filled / unrequested fields; unknowns = [PLACEHOLDER].
- [ ] **User signed off the brief** ("OK").
> No sign-off → do not pick references / do not design.

## STEP 0 — register
- [ ] Register/intent chosen, and it differs from recent builds
      (checked against `../AGENTS.md` "known bias to AVOID").

## GATE 1 — human picks the lead  🔒
- [ ] 3 references presented (name / URL / why / borrow / don't-borrow).
- [ ] **User chose 1 lead** (+1–2 support) and it is recorded in
      `notes/reference_candidates.md`.
> Do not pass GATE 1 by self-picking. Wait for the user's "これがいい".

## GATE 2 — real reference screenshot exists  🔒
- [ ] `screenshots/refs/lead_firstview.png` exists for the chosen lead.
- [ ] It was **captured**, not imagined:
      `python3 ../tools/rfm_shot.py "<lead-url>" screenshots/refs/lead_firstview.png`
      (auto-default; if SUSPECT/FAIL → user captures manually, same path).
- [ ] The screenshot was actually **looked at** (not just file-present).
> No verified screenshot file → STOP. `reference_observation.md` stays empty.

## After the gates
- [ ] STEP C decompose written FROM the screenshot → `notes/reference_observation.md`
- [ ] STEP D borrow/don't-borrow + avoid-list + aim-list written
- [ ] STEP E materials decided FIRST + licenses recorded → `notes/materials_used.md`

### GATE 3a — hero LOOK approved (Web only)  🔒
- [ ] Hero first-view rendered ALONE → `screenshots/hero_checkpoint.png`
- [ ] **User confirmed** the hero direction / feeling.
> No "OK" → revise the hero. Do NOT continue.

### GATE 3b — STRUCTURE approved (Web only)  🔒
- [ ] `notes/structure_proposal.md` enumerates: every nav label (not just a count),
      section order + IDs, what lives in each section, mobile nav behavior, total
      link count, and which fields stay `[PLACEHOLDER]`.
- [ ] **User ticked each enumerated item.** (Hero "looks good" ≠ structure OK.)
> No sign-off → do NOT build the rest yet. (Skip GATE 3 for posters/single images.)

- [ ] STEP F artifact built in this directory (top-to-bottom strength)
- [ ] STEP F per-element treatment varied ≥3 patterns (record in build_log)
- [ ] STEP G output screenshots rendered + looked at
- [ ] STEP H self-evaluation written incl. residual AI-ness + one next change
