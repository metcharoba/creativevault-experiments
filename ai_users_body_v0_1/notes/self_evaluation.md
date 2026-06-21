# Self-Evaluation — ai_users_body_v0_1

Honest, not promotional. 0 = same as recent builds, 5 = clearly a different/strong output.

| Criterion | Score | Basis |
|-----------|------:|-------|
| Different picture than before | 4 | organic / tactile material register は 70_design_experiments で under-explored 軸、過去の loud pop 系 / 静か archive 系のどちらでもない。「身体と AI 流体の融合像」という reading は他のどの build にも無い。Tillmans 似で止めずに Röntgen hand を統合して脱却した。 |
| Lead reference's composition actually used | 4 | Tillmans Freischwimmer 54 の非対称構図（重心右上 / 左下 bare ground）、material flow の 4 density gradation 共存、border / margin 無しの full-bleed、すべて v2 final に継承。Tillmans の olive palette は完全に避けて iron-blue に置換、register だけ借りた。 |
| Generic-AI-LP feel reduced | 5 | LP / SaaS UI 要素ゼロ、card grid / pill CTA / frosted glass / centered hero / floating cards すべて不在。AI 装飾 cliché（orbs / hexagons / network lines / circuits / wireframe）も不在。完全に作品としての 1 枚絵。 |
| Material feel | 4 | GPT 生成だが ink-on-paper / 暗室 photogram の質感が出ている。grain / 粒度は GPT 出力時点で十分、CC0 grain 重ねを「over-stacking 回避」で意図的に外した（honest call）。 |
| Non-uniformity (same-kind elements not templated) | 4 | density 1 軸のみ、4 階調共存（dense smear / threadlike trails / fine particulate dust / bare ground）。同一 visual mode 内で十分非均一だったので、追加軸（size / placement / rotation）は乗せず（AGENTS.md "stacked too thick" 回避、bird_voice の実証経験を適用）。 |
| Screen-as-artwork feel | 4 | 画面いっぱい 1 枚絵として self-contained、文字 / UI / 装飾なし。museum-print quality を狙い、おおむね到達。 |
| Strong top-to-bottom (not only the top) | 4 | landscape 1 枚なので「top-to-bottom」は構図縦軸として読む：手は右上から右下にかけて斜行配置、下端は bare ground と threadlike trails の細部、上端は dense smear、中央は threadlike trails と particulate dust。縦軸どこ切っても visual language 一貫。 |
| Register differs from recent builds | 4 | 直近の bird_voice (diagram/data-led) / maeda 系 (loud pop comic) / thought_gallery (quiet archive editorial) いずれとも register が異なる。house-tic (halftone, cream+red+blue+yellow, SIGNAL motif) も使わず。 |

## Residual AI-ness / weaknesses (honest)
- 手の認識度がやや高め。subject「抽象度高く」brief に対して、v2 は v1 より具象寄りに振れた。抽象度 v1 > v2 > literal x-ray の中間。subject の "壊す" / collision を優先した trade-off。
- 手の感触が skeletal で「疲労 / 死」寄りに読める。subject の「慣れ / 距離」軸からは少し外れる（ただし「疲労」は subject 内、逸脱ではない）。
- 構図は v1 からの継承で、完全に独立した composition ではない。v1 の base を活かしたのは GPT 統合の都合と integration 品質優先のため。
- GPT 生成依存。Codex 側で iteration 制御が限定的（prompt 設計 + reference 提示までしかできない）。

## Gate honesty check
- GATE 1 truly user-picked (not self-picked)? **yes** (Tillmans Freischwimmer 54 を user が "1か3だね" → A 選択、Röntgen hand pivot も user 判断、x-ray 候補 A vs C-i も user pick)
- GATE 2 a real captured screenshot was observed (not from memory)? **yes** (rfm_shot.py 自動取得 + Read で確認、observation はその実画像から書いた)

## One next change
- 次に同 register で 1 本やるなら **「手の認識度をもう一段下げて、抽象度を v1 寄りに戻す」** ── 「手だと気づくのに数秒かかる」程度の溶解度。今回の v2 は「手を残す」方を優先したが、subject「抽象度高く」原理主義なら手の輪郭をもう少しほどく余地がある。

## STEP E route check (honest, after the fact)
- 当初 route C (GPT + CC0 grain hybrid) を選択 → v1 で GPT 単独十分と判断 → 当初追加予定の CC0 grain は不採用。
- v1 完成後「Tillmans 似で止まる」課題が立ち、CC0 PD 外部素材を overlay する route に再進入 → Wellcome 解剖図 (1686) で v2_attempt_a (並列), v2_attempt_b (全面) 試作 → 両方「並べた」止まりで failed → engraving の discrete line vs flow の continuous field の視覚言語衝突が root cause と判定。
- pivot：x-ray (連続トーン body 素材) を選び、GPT 5.5 に v1 + Röntgen hand + Tillmans crop を統合 reference として渡し、unified image として再生成 → v2 final。
- 学び：**overlay 重ねは視覚言語が連続トーン同士でないと統合しない**。次回 overlay 路を取るなら最初から連続トーン素材を選ぶ。

## Build artifacts
- canonical: `ai_users_body_v0_1.png` (1536×1024) + `ai_users_body_v0_1.pdf` (300dpi)
- 出力: `screenshots/01_full_image.png` (full) + `screenshots/02_detail_hand_integration.png` (右半分 detail)
- 経過アセット（abandoned, 履歴として保持）: `assets/main_flow_gpt_v1.png` (Tillmans-aligned 初版) / `assets/main_flow_v2_attempt_a.png` (engraving 並列) / `assets/main_flow_v2_attempt_b.png` (engraving 全面) / `assets/overlay_wellcome_nervous_1686_raw.jpg` (engraving 原版) / `assets/xray_candidate_sole_1896.jpg` (検討候補)
