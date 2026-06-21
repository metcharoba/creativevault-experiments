# Materials Used (decided FIRST — STEP E) — ai_users_body_v0_1

## Fonts
| Font | Role | Source | License / usage |
|------|------|--------|-----------------|
| — | — (作品内に文字無し per brief) | — | — |

## Palette
- Ground: **warm bone / off-white** ≒ `#E8E0D2`–`#EFE7D7`（cream ではない、pure white でもない）
- Flow: **muted iron-blue** ≒ `#3A4A5C`–`#5A6B7D`、最濃部 `#1F2A36`（cyan / navy / teal ではない）
- 第三色なし。彩度を上げない。グラデーション虹色 NG。
- 根拠: 身体イメージ（質入れの青 / 鬱血）寄り、register killer の Tillmans olive 系を回避、house-tic（cream+red+blue+yellow）回避。

## Main visual route
- **Route C (A+B hybrid)** — GPT 生成 (main flow) + CC0 photo (grain layer)
- Codex 役割: prompt pack 設計 / 戻り画像の QA / CC0 grain 探し / PIL 合成 / 納品整形
- User 役割: GPT 生成実行、戻り画像を `assets/` に置く

## Hero / supporting material
- [x] CC0 / Public Domain (grain layer 用、source は GPT 戻り後に確定)
- [ ] CC-BY
- [ ] CC-BY-SA
- [ ] Official press kit / brand asset
- [x] Reference screenshot for observation only (Tillmans, fair use, screenshots/refs/lead_firstview.png)
- [ ] Self-made shapes
- [x] User-provided externally generated image (GPT 主役 flow)

| Role | Source + URL | Asset path | License | Attribution string |
|------|--------------|------------|---------|--------------------|
| Reference (observation only) | Wolfgang Tillmans, Freischwimmer 54 (2004) — https://sammlung.staedelmuseum.de/en/work/freischwimmer-54 | screenshots/refs/lead_firstview.png | © Wolfgang Tillmans / Städel Museum 所蔵。Fair use での観察のみ。再配布せず、final artifact にも組み込まない。 | (内部観察のみのため作品中に attribution 不要) |
| Main flow v1 (主役 visual, 初版) | User-provided GPT-generated image (prompt pack v1 部 / Tillmans register 借り) | assets/main_flow_gpt_v1.png | user 生成画像 / 内部使用 | — |
| Body anchor reference (v2 用) | Wilhelm Conrad Röntgen, "Hand mit Ringen" (1895), first medical x-ray ── https://en.wikipedia.org/wiki/File:First_medical_X-ray_by_Wilhelm_R%C3%B6ntgen_of_his_wife_Anna_Bertha_Ludwig%27s_hand_-_18951222.jpg | assets/xray_candidate_rontgen_hand_1895.jpg | Public Domain (published before 1931, life+100 expired) | (PD のため作中 attribution 不要、materials_used に記録) |
| Main flow v2 (主役 visual, 再生成) | User-provided GPT-generated image (prompt pack v2 部 / v1 + Röntgen hand を統合再生成) | assets/main_flow_gpt_v2.png | user 生成画像 / 内部使用 | — |
| Grain layer | 不採用 (v1 で既に grain 十分、over-stacking 回避) | — | — | — |

## Why this material (one line)
- Register が organic / tactile material で文字無し、subject が「AI 使う側の身体感覚」── GPT 生成自体が subject と meta-coherence を持ち、CC0 grain が photographic substrate authenticity を足す。

## Boundaries
- CreativeVault 70_design_experiments/ 内のみ
- 主役 flow は user-provided GPT 画像。Codex は素材として整形のみ。
- Grain は CC0 / PD 限定（CC-BY なら attribution 明記）。
- Tillmans の参照 screenshot は build observation のみ、final artifact には組み込まない。
