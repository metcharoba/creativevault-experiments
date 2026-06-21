# GPT Image Generation Prompt Pack — ai_users_body_v0_1

> User が ChatGPT (GPT 5.5 / image gen) にコピペして主役 visual を生成するための pack。
> 戻ってきた PNG を `assets/main_flow_gpt_v1.png` として保存し、Codex が grain layer 合成へ進む。
> 1 回で気に入らなければ v2, v3 と版を重ねていい。

## 投げ方（GPT 5.5）

1. **下の英語 prompt をコピペ**
2. **参照画像を attach**: `screenshots/refs/lead_work_crop.png`（Tillmans 作品本体だけを crop した clean 版、1880×2592）
3. **送信時に必ず以下を 1 文添える**（落とすと Tillmans の olive 色をコピーされる）:
   > "Use the attached image as a **composition and density reference only**. Do NOT use its palette. The palette MUST be the iron-blue on bone specified in the prompt above."

---

## Prompt（英語版、推奨）

```
Camera-less darkroom-style abstract image, light-on-photo-paper feeling.
No figure, no face, no body part, no text, no symbols, no logo, no watermark.

Composition:
- Single full-bleed image, no border, no frame, no margin, no vignette.
- Strongly asymmetric: principal density concentrated on the top-right area,
  the opposite (lower-left) side left almost bare (ground exposed).
- Four density gradations coexist in one image:
  - dense smear: a concentrated mass of pigment / light, highest density
  - threadlike trails: mid-density fine flowing lines streaming from the dense mass
  - fine particulate dust: low-density dispersed grain in the mid-field
  - bare ground: large empty areas where the ground color is fully exposed
- One primary non-uniformity axis only: density gradient. Do not add size,
  placement, or rotational variation.

Surface:
- Soft edges throughout, no hard outlines, no vector look.
- Dissolved / diffused transitions, like ink in water or smoke in light,
  but NOT photographic ink-in-water (no literal water motif).
- Quiet, restrained, museum-print quality. Looks like an abstract photogram.

Palette (strict, do not deviate):
- Ground: warm bone / off-white, NOT cream, NOT pure white.
  Target hex range #E8E0D2 to #EFE7D7.
- Flow: muted iron-blue, NOT cyan, NOT navy, NOT teal.
  Target hex range #3A4A5C to #5A6B7D, with darkest concentrations #1F2A36.
- No third color. No saturated hue. No rainbow gradient.
  Strictly two-color (ground + single flow color family).

Mood / subject (high abstraction):
The work is about the bodily sense of an everyday AI user — fatigue,
habituation, distance — but rendered purely as material flow. No imagery
of a body. No imagery of a machine. The surface itself carries the sense.

Aspect ratio: 3:2 landscape (e.g. 1536 x 1024 or higher resolution).
```

## 禁止事項（生成 AI が滑り込ませがちなもの。明示禁止）

- Wolfgang Tillmans 本人の olive-green / brown specific palette
- 人物 / 顔 / 手 / 目 / 身体パーツ
- 文字 / 数字 / 記号 / ロゴ / watermark / signature
- AI / tech cliché: orbs, hexagons, network lines, nodes, circuits, wireframe,
  dots-and-lines diagrams, geometric overlays, brain icons, glowing centers
- 写真リアルな ink-in-water / smoke の literal な題材化（Tillmans 真似に寄る）
- vector / plastic / gloss / 3D render look
- 蛍光色, neon, posterization, gradient mesh
- frame, vignette, polaroid border, drop shadow

## 戻り画像の取り扱い

1. 生成された PNG を `70_design_experiments/ai_users_body_v0_1/assets/main_flow_gpt_v1.png` として保存（バージョン違いは `_v2.png`, `_v3.png`）。
2. Codex に「v1 入った」と伝える → Codex が画像確認 → grain layer 探しと合成に進む。
3. 「palette が違う / asymmetric が弱い / cliché が出た」場合は prompt を修正して再生成。修正箇所を Codex に伝えれば prompt pack を編集します。

## Format / 提出

- aspect ratio: 3:2 landscape 推奨（自由比なので 4:3 / 5:4 等も可、要相談）
- file format: PNG（loss less）
- resolution: 1536×1024 以上推奨
- save path: `70_design_experiments/ai_users_body_v0_1/assets/main_flow_gpt_v1.png`

---

# v2 Prompt Pack ── Röntgen hand integration

> v1 で Tillmans 似の register は確立。v2 では「身体（Röntgen 1895 hand x-ray）が flow の中から立ち上がる / 溶ける」統合像を 1 枚で再生成する。
> Overlay 重ねでは並べた感が抜けなかった（v2_attempt_a, v2_attempt_b 参照）ため、GPT 側で unified image として生成する。

## 投げ方（GPT 5.5）

下の英語 prompt をコピペ + **3 つ** の reference 画像を attach:

1. **Composition / register reference**: `screenshots/refs/lead_work_crop.png`（Tillmans Freischwimmer 54 crop）── 非対称構図と material flow の register を借りる
2. **Body anchor reference**: `assets/xray_candidate_rontgen_hand_1895.jpg`（Röntgen 1895 hand x-ray）── 身体の形を borrow（sepia 色は borrow しない）
3. **Current state reference**: `assets/main_flow_gpt_v1.png`（前 step の iron-blue flow）── palette と density gradation の継承元

送信時に必ず添える 1 文（落とすと統合に失敗する）:

> "Generate ONE unified image, not a collage or layer. The hand from the x-ray reference must DISSOLVE INTO and EMERGE FROM the iron-blue flow — it should not look like an x-ray placed on top of an abstract image. The hand's bones should appear AS density patterns of the flow itself."

## Prompt（英語版）

```
Camera-less darkroom-style abstract image, light-on-photo-paper feeling.
No face, no body apart from a single hand, no text, no symbols, no logo,
no watermark, no caption, no handwriting, no museum stamp.

Subject (high abstraction):
The image is about the bodily sense of an everyday AI user — fatigue,
habituation, distance. A single human hand emerges from and dissolves into
an iron-blue material flow. The hand is the only body part shown; it is
not posed or active, it simply surfaces from the flow as if x-rayed through
the flow itself. Bones, soft-tissue gradient, and finger contour are
discernible but FUSED with the flow's own density gradations — not pasted
on, not framed, not bordered.

Composition (inherit from the v1 reference):
- Single full-bleed image, no border, no frame, no margin, no vignette.
- Strongly asymmetric: the hand and principal density concentrated on
  the right side (or top-right), the opposite side left almost bare
  (ground exposed).
- Four density gradations coexist:
  - dense smear: the densest area, around the hand's palm/knuckles
  - threadlike trails: mid-density flow streaming from the hand into the
    surrounding space (finger-like and not finger-like at once)
  - fine particulate dust: low-density dispersed grain in the mid-field
  - bare ground: large empty areas where the ground color is fully exposed
- One primary non-uniformity axis: density gradient. No size / placement /
  rotation variation axes added.

Hand integration (this is the hardest part — get it right):
- The hand is X-RAY-like but NOT a literal x-ray. Bones are visible as
  density variations in the iron-blue flow; soft tissue is rendered as
  paler iron-blue washes; the hand has no hard outline.
- The hand should appear as if the flow itself is taking the shape of a
  hand momentarily — like ink in water that has organized into hand form
  but is still part of the same continuous fluid.
- The hand should NOT have: sharp x-ray border, sepia/brown coloration of
  the historical reference, vintage paper card mount, handwriting, stamp,
  ring (no wedding ring on the finger), or any text label.

Surface:
- Soft edges throughout, no hard outlines, no vector look.
- Dissolved / diffused transitions, like ink in water or smoke in light.
- Quiet, restrained, museum-print quality. Looks like an abstract photogram
  that happened to record a hand.

Palette (strict, do not deviate):
- Ground: warm bone / off-white, NOT cream, NOT pure white.
  Target hex range #E8E0D2 to #EFE7D7.
- Flow + hand together: muted iron-blue, NOT cyan, NOT navy, NOT teal.
  Target hex range #3A4A5C to #5A6B7D, with darkest concentrations
  #1F2A36 in the densest hand areas (palm, knuckles).
- NO sepia, NO brown, NO yellow paper tone (DO NOT inherit the Röntgen
  reference's sepia coloration — translate fully to iron-blue on bone).
- No third color. No saturated hue. No rainbow gradient.

Aspect ratio: 3:2 landscape (1536 x 1024 or higher).
```

## 禁止事項（v2 では特に注意）

- v1 で禁止した全項目（cliche, frame, neon 等）
- **layer / collage / placed look** ── 「重ねた」「貼った」見た目
- **literal x-ray look** ── 医療用 x-ray の硬い縁、純黒背景
- **Röntgen reference の sepia / brown / paper card mount / handwriting / stamp**
- **wedding ring on the finger**（reference にはあるが、本作には不要）
- 手以外の身体パーツ（顔・腕全体・体幹・他の手）
- 解剖学的に正確すぎる骨配置（medical illustration 風になる）── 暗示で十分

## 戻り画像

- save path: `70_design_experiments/ai_users_body_v0_1/assets/main_flow_gpt_v2.png`
- 「v2 入った」と Codex に伝える → Codex 確認 → 統合度判定 → STEP F 仕上げ / 再生成判断
