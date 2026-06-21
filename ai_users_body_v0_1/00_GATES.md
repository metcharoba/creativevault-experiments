# RFM Gate Checklist (copy this whole folder per build)

Route: `reference_first_mimic_workflow_v0_2.md`. Work top to bottom. A gate that
is not checked = the build is NOT allowed to proceed past it.

## GATE 0 — brief & scope confirmed  🔒
- [x] `notes/brief.md` filled (Web → §A scope incl. link/section count;
      Poster/single → §B every required field + value).
- [x] No invented / auto-filled / unrequested fields; unknowns = [PLACEHOLDER].
- [x] **User signed off the brief** ("OK"). (2026-06-21)
> No sign-off → do not pick references / do not design.

## STEP 0 — register
- [x] Register/intent chosen: **organic / tactile material** (image-led / material-led, under-explored 軸、外部素材ルート想定)
      checked against `../AGENTS.md` "known bias to AVOID" — 2極外、house-tic 外、SIGNAL 外、bird_voice の diagram と被らず。

## GATE 1 — human picks the lead  🔒
- [x] 3 references presented (name / URL / why / borrow / don't-borrow).
- [x] **User chose 1 lead** (#1 Tillmans Freischwimmer 54) and it is recorded in
      `notes/reference_candidates.md`. (2026-06-21)
> Do not pass GATE 1 by self-picking. Wait for the user's "これがいい".

## GATE 2 — real reference screenshot exists  🔒
- [x] `screenshots/refs/lead_firstview.png` exists for the chosen lead. (2880x4800, 2.9MB)
- [x] It was **captured** via `rfm_shot.py` (exit 0, pixel_std 90.8, real-looking).
- [x] The screenshot was actually **looked at** (Read by Claude, 観察を reference_observation.md に記述、Tillmans 作品 + museum chrome 構造を確認)。
> No verified screenshot file → STOP. `reference_observation.md` stays empty.

## After the gates
- [x] STEP C decompose written FROM the screenshot → `notes/reference_observation.md`
- [x] STEP D borrow/don't-borrow + avoid-list + aim-list written
- [x] STEP E materials decided FIRST + licenses recorded → `notes/materials_used.md`
- [x] STEP E route check passed: image-led 主役 visual は GPT 生成 (v1) → GPT 統合再生成 (v2) ルート、Codex は素材 QA + 整形のみ。procedural drawing は不採用。

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

- [x] STEP F artifact built: `ai_users_body_v0_1.png` (1536×1024) + `.pdf` 同名、build_log に v1 / v2_attempt_a / v2_attempt_b / v2 final の経緯記録。
- [x] STEP F per-element treatment varied ≥3 patterns: density gradation 4 階調（dense smear / threadlike trails / fine particulate dust / bare ground）が同一 visual mode 内に共存。register が material 連続体なので、追加軸（size / placement / rotation）は乗せず（AGENTS.md "stacked too thick" 回避）。
- [x] STEP G output screenshots rendered + looked at: `screenshots/01_full_image.png` (full) + `screenshots/02_detail_hand_integration.png` (右半分 detail crop)。
- [x] STEP H self-evaluation written → `notes/self_evaluation.md`
