# Reference Observation (written FROM the screenshot — GATE 2) — ai_users_body_v0_1

- Lead: Wolfgang Tillmans — Freischwimmer 54 (2004)
- URL: https://sammlung.staedelmuseum.de/en/work/freischwimmer-54
- Screenshot file: `screenshots/refs/lead_firstview.png`  (captured: auto, rfm_shot.py OK, 2880x4800, pixel_std 90.8)
- Capture note: rfm_shot.py OK、museum page 上部の作品図版を主体として観察。

## Decomposed from the screenshot
- **Composition:** 作品図版は museum page 上部の大きな矩形に full-bleed で配置。作品内部は強く非対称 — 主要な密度は **画面右上から右半分** に集中、左半分はほぼ空。重心は対角線上 (左下→右上)。横位置の中央や水平垂直の対称は使われていない。
- **Whitespace / ma:** 「空」は cream / pale yellow の地として大きく残る。これは余白ではなく **同じ重さの構成要素として残されている**（背景処理ではなく ground そのもの）。
- **Material / texture:** ink-in-water / 煙 / 液体に沈んだ有機物 のような表情。エッジは全部 soft / 拡散。線ではなく濃度のフィールド。微細な点状の沈殿物が局所的に散る。一切のハードエッジが無い。
- **Typography (pairing, contrast, scale):** 作品自体には文字無し。museum page 側は institutional sans-serif（白/灰、極小サイズ）、作品図版とは明確に分離されている。
- **Information density:** 作品内部の情報密度はゼロ（記号 / アイコン / 図像なし）。あるのは material と density だけ。一切の representation 無し。
- **Non-uniformity (how same-kind elements differ):** 煙状の flow 自体が非均一 — 密度高（dark dense smear）/ 中（threadlike trail）/ 低（fine particulate dust）/ ground 露出 の 4 階調が共存。同じ「煙」要素でも厚み・濁度・線の太さ・拡散度が全部違う。

## Borrow vs don't-borrow
- **Borrow:**
  - 全面 1 枚絵としての immersion（border / margin で囲まない）
  - 強い asymmetric composition（重心を一方に寄せ、反対側を bare のまま残す）
  - 表面=作品（material そのものが subject）
  - figure / 文字 / 記号 不在
  - 同一系統の要素を **濃度 / 拡散度 / 線太さ / 露出度** で非均一に変える
  - 抑制された 2 色構成（ground 1 色 + 流れ 1 色系統）
- **Don't-borrow:**
  - Tillmans の olive-green / dark brown の具体配色（derivative risk）
  - 写真 grain の literal な質感
  - ink-in-water / 煙 そのものの題材化（同じ素材を使うと「Tillmans の真似」になる）

## Avoid-list (house-tics banned this build)
- halftone dots / 印刷ズレ（house-tic）
- cream/bone paper + red+blue(+yellow)（house-tic、色だけでなく組み合わせも禁止）
- condensed-bold 単独 / high-contrast serif+italic 単独（house-tic）
- comic bursts / 吹き出し / 強調記号（loud pop pole）
- "SIGNAL / transmission / fragments / experiments / future / ideas" 語彙
- diagram / chart / map / data-led 構造（bird_voice 既出）
- 中央寄せ / 対称構図 / pill CTA / frosted glass / card grid / floating cards
- 主役 visual の self-made polygon / 自前ペン線 / SVG drawn drawing（image-led の silent register killer、事前許可なし）
- procedural な「AI 装飾」（線でできた回路、ノード、グリッド、wireframe 等）

## Aim-list
- 1 枚絵としての immersion、border / margin 無し
- 強い asymmetric composition（重心を一方に寄せ、反対側は bare ground）
- material そのものが subject（表面が AI 使う側の身体感覚を語る）
- 抑制されたパレット（ground 1 色 + 流れ 1 色系統、Tillmans の olive 系は外す）
- 主役 visual は external material ルート（CC0 photo の強処理 or GPT 生成）
- 濃度 / 拡散度 / 線太さ / 露出度 の **1 つの非均一軸（"濃度勾配"）** に絞り、サイズ・配置の追加軸は乗せない（diagram register ではないが、material 系も追加軸を乗せると register が弱る）

## Per-element-treatment plan (the recurring weakness)
material 系の register は「同一要素」がそもそも flow / smear の濃度違いになる構造。主軸 1 つに絞った上で、以下 4 階調を 1 枚内に共存させる:
- **dense smear** — 主要な重心、最も濃い濃度、輪郭は dissolve（frame: なし、treatment: 中心 mass）
- **threadlike trail** — dense から離れて延びる中濃度の流れ（frame: なし、treatment: 線状 trail）
- **fine particulate dust** — 周辺に散る微細な沈殿（frame: なし、treatment: 点状散布）
- **bare ground** — 何も無い領域（frame: なし、treatment: 露出、これも構成要素として残す）
