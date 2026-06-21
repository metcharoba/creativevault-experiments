# Build Log

- Date: 2026-06-15
- Build dir: `70_design_experiments/bird_voice_time_chart_v0_1/`
- Route: reference_first_mimic_workflow_v0_2.md
- Purpose: X (Twitter) 投稿用 1枚画像。架空の「鳥の声の時刻分布」ダイアグラム。

## Gate trail (proof, not promise)
- GATE 0 brief sign-off: `notes/brief.md` 末尾、user OK (2026-06-15)。
  時刻表記は抽象化(具体日時を避ける)旨の修正を反映済。
- GATE 1 lead pick: `notes/reference_candidates.md` — user picked #2 Florence Nightingale ローズダイアグラム (1858)。
- GATE 2 screenshot: `screenshots/refs/lead_firstview.png` — `tools/rfm_shot.py` で自動取得し、目視済。`notes/reference_observation.md` は実際に画像を見て書いた。
- GATE 3 (Web only): N/A (Poster)

## Per-element non-uniformity (≥3 patterns) — what I actually varied
8 つの species disc を**6 つの描画モード**に分けた。サイズ・配置・ラベル位置も非均一。

| Same-kind element | Treatment A | Treatment B | Treatment C |
|-------------------|-------------|-------------|-------------|
| ウェッジ描画 | 塗り (スズメ/ヒヨドリ/ツバメ) | 線のみ (ハシブトガラス) | 点群 (シジュウカラ) |
| ウェッジ描画 (続) | 茎+終端ドット (メジロ) | 同心三層 (キジバト) | 放射ハッチ (ウグイス) |
| disc サイズ | 大 230 (ヒヨドリ) | 中 200–210 (5 種) | 小 180–190 (キジバト/ツバメ) |
| 外周ティック | 24 刻み (4 種) | 12 刻み (4 種) | (種により混在) |
| disc 配置 | 標準位置 (3 つ) | 下げ (#2, #6) | 上げ (#3, #4) |
| ラベル位置 | 全種 下に重ねる(統一) | — | — |
| インク色 | dark ink (5 種) | accent terracotta (3 種) | — |

合計**6つのウェッジ描画モード** × サイズ 3 段階 × 配置 3 パターン。
**templated-grid 感を避けるため、ティック数とディスクサイズを意図的に揃えていない**。
(v0.1 初版にあった side-label の異質配置はユーザ指摘で削除。「3パターン以上の非均一」は描画モード/サイズ/配置で確保。)

## Top-to-bottom strength
- 上端: 黒太罫 + 左寄せ大型タイトル(中央寄せヒーローを避ける)
- 中段: 8 つの非均一 disc(版面の主役)
- METHOD パラグラフ: 左に accent カラーの短い罫 + monoタイポラベル「METHOD」、本文は日本語で。**プレーン info-footer に崩れない**ように、本文の前に色つきの罫を入れて方向感を残す。
- 下端: 黒灰 1px 罫 + 左右に mono クレジット(架空データ宣言 + 架空観測者名)。罫線が版面を二度締める。

## Notes / decisions / problems hit
- 当初は side-by-side 2 円(Nightingale 模倣)を考えたが、対称ミラーは AI 模倣の典型に陥りやすいと判断し、**small multiples × 8 種**に分解。
- パレット: クリーム+赤+青+黄(house-tic)を明確に避け、リネン白 + ダークフォレスト + テラコッタの 3 色運用に。
- フォント: すべて OFL(Noto Serif JP / Noto Sans JP / IBM Plex Mono)、Google Fonts から `@import`。ローカルレンダリングにのみ使用。
- 時刻表記: ユーザ指示で具体日時を避け、「ある一日」「夜明け前から日暮れまで」など抽象化。
- レンダリング: `make_poster.py` で SVG inline の HTML を生成、Chrome `--headless=new` で 1080×1350 × DPR 2 = 2160×2700 にラスタライズ。
- 残課題は self_evaluation.md。
- ユーザレビュー後の修正 (2026-06-15):
  1. METHOD ラベルと本文が grid layout で被っていた。`.method` を grid → block + inline-block へ変更し、ラベル(短罫付き)を上、本文を下に独立配置。
  2. #4 シジュウカラだけ side-label で横並びになっていて全体から浮いていた。`side_label = set()` で除去し、他と同じ縦並びに統一(描画モード=点群はそのまま維持)。
- **データは完全に架空。** 私が手で振った値。フィールドガイドのラフな経験則(早朝合唱・薄明二度のピーク・ウグイス早朝のみ等)に「それっぽさ」だけ寄せたもので、観測根拠はゼロ。版面下部に "FICTIONAL DATASET" と明記。
