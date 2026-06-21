# Build Log — ai_users_body_v0_1

- Date: 2026-06-21
- Build dir: `70_design_experiments/ai_users_body_v0_1/`
- Route: reference_first_mimic_workflow_v0_2.md
- Format: single image (poster / key visual)
- Purpose: thought_gallery の Currently on view 2 枠目

## Gate trail (proof, not promise)
- GATE 0 brief: user signed off 2026-06-21
- STEP 0 register: organic / tactile material（under-explored 軸、bias-avoid 抵触なし）
- GATE 1 lead pick: Wolfgang Tillmans — Freischwimmer 54（user 選択、"1か3だね" → A）
- GATE 2 screenshot: `screenshots/refs/lead_firstview.png` captured via rfm_shot.py (auto, OK, 2880×4800, pixel_std 90.8), looked at: yes
- STEP C 観察: `notes/reference_observation.md`
- STEP D avoid/aim: 同上ファイル内
- STEP E materials: `notes/materials_used.md`（GPT 生成 + Röntgen hand PD ref）
- STEP F: `ai_users_body_v0_1.png` + `.pdf`（1536×1024）
- STEP G: `screenshots/01_full_image.png` + `screenshots/02_detail_hand_integration.png`
- STEP H: `notes/self_evaluation.md`

## Iteration trail（v1 → v2_attempt_a/b → v2 final）

### v1 — `assets/main_flow_gpt_v1.png`
GPT 5.5、prompt pack v1 + Tillmans crop attach、iron-blue on bone palette、非対称構図、4 density gradation。OK direction、Tillmans register 確立。**問題**：subject「壊す / 介入」未達、Tillmans 似で止まる。

### v2_attempt_a — `assets/main_flow_v2_attempt_a.png`（abandoned）
Wellcome 解剖図 1686（Public Domain Mark、`assets/overlay_wellcome_nervous_1686_raw.jpg`）を左側に scaled placement、multiply blend。**Fail**：左右二分の diptych、「並べた」感が抜けない。

### v2_attempt_b — `assets/main_flow_v2_attempt_b.png`（abandoned）
同 engraving を full-canvas で multiply、threshold 寄り contrast 補正。**Fail**：engraving が flow を呑む、ただの古い解剖図に見える。

### Root-cause 判定
**engraving (discrete line, multi-mode) × flow (continuous gradient field) は視覚言語が違いすぎて 1 枚に統合不可**。multiply overlay では「層が見える」止まりで unified image にならない。

### Pivot → v2 final
連続トーンの body 素材 (x-ray) に切り替え、Codex 側の合成ではなく **GPT 5.5 に v1 + Röntgen hand 1895 + Tillmans crop を統合 reference として渡し、unified image として再生成**。

### v2 final — `assets/main_flow_gpt_v2.png` → `ai_users_body_v0_1.png`
GPT 5.5、prompt pack v2 + 3 references attach + "Generate ONE unified image, not a collage or layer" 1 文添え。手が iron-blue flow から立ち上がる / 溶ける unified image を 1 発取得。**Success**：layer 感消失、subject 直撃、palette 厳守、文字 / ring / x-ray border 全部なし。

## Per-element non-uniformity (≥3 patterns) — what I actually varied
| Same-kind element | Treatment A | Treatment B | Treatment C | Treatment D |
|-------------------|-------------|-------------|-------------|-------------|
| iron-blue density | dense smear（手の本体、最濃 #1F2A36 帯）| threadlike trails（手から延びる細流） | fine particulate dust（中域散布） | bare ground（左下大開放、ground 露出） |

主軸 1 つ（density gradient）に絞り、size / placement / rotation 軸は乗せず（AGENTS.md "stacked too thick" 回避、bird_voice の修正経験適用）。

## Top-to-bottom strength
landscape 1 枚なので「縦軸どこ切っても visual language 一貫」で評価：上端 = dense smear（手の上腕入口）、中央 = threadlike trails + particulate dust、下端 = bare ground と細い trail の終端。plain info-footer 化はそもそも構造的に起きない（情報要素なし、純絵）。

## Notes / decisions / problems hit
- **Wellcome engraving の試行を捨てる判断**：3 試行で「並べた」止まりが確定した時点で root cause 認識、無理に押さず pivot 提案。
- **CC0 grain 不採用**：v1 で grain 十分、追加すると "stacked too thick" に該当。route C (hybrid) を route A (GPT 単独 + 後の GPT 統合再生成) に切り替え。
- **GPT 5.5 統合再生成の威力**：1 発で unified image 達成。Codex 内の Pillow 合成では物理的に出せない品質。次回似た案件は最初から GPT 統合 route を検討する価値あり。
- **abandoned files 保持**：履歴として `assets/main_flow_v2_attempt_a.png`, `main_flow_v2_attempt_b.png`, `overlay_wellcome_nervous_1686_raw.jpg`, `xray_candidate_sole_1896.jpg` を残置。次回参照用。
