# Materials Used (decided FIRST — STEP E)

## Fonts
| Font | Role | Source | License |
|------|------|--------|---------|
| Noto Serif JP | 日本語タイトル・キャプション | Google Fonts (Adobe / Google) | SIL OFL 1.1 |
| Noto Sans JP | 日本語小ラベル(凡例・ティック) | Google Fonts | SIL OFL 1.1 |
| IBM Plex Mono | 英数字ラベル・時刻ティック・数値 | IBM | SIL OFL 1.1 |

(自前ホストで CSS から `@font-face`。配布物には埋め込まない=このリポジトリ内のラスタライズだけに使う。)

## Palette
- 紙地: **#E8E6DD** (くすんだリネン白。クリーム+暖色寄りを避け、わずかに緑〜灰に振った無彩)
- インク主: **#1C2A28** (ほぼ黒に近いダーク・フォレスト)
- アクセント: **#B4593A** (退色した煉瓦・テラコッタ。赤+青+黄の house-tic ではないトーン)
- 補助グレー: **#8E8B7E** (キャプション罫線・小ラベル)

クリーム+赤青黄の house-tic を明確に外す。1 ベース + 1 ダーク + 1 アクセント。

## Hero / supporting material
- [x] Self-made shapes (このビルドは diagram-led — 図形+タイポ主導は許容範囲)
- [x] Reference screenshot for observation only (Nightingale Wikimedia Commons file ページ。**観察用のみ**で再配布しない)

| Role | Source + URL | Asset path | License | Attribution |
|------|--------------|------------|---------|-------------|
| 参照画像(観察用) | https://commons.wikimedia.org/wiki/File:Nightingale-mortality.jpg | `screenshots/refs/lead_firstview.png` | Public Domain (1858) | Florence Nightingale (1858) — observation only, not redistributed in the artifact |
| 図形 + タイポ | self-made (SVG inside index.html) | `index.html` | n/a | — |

## Why this material (one line)
- ダイアグラム/模式図 register の本体は**点・線・塗りで描く図形**そのもの。CC0 写真や AI 生成画像を持ち込むと register が崩れる。Nightingale はあくまで「観察用の参照」で、絵としては輸入しない。

## Boundaries (確認)
- CreativeVault `70_design_experiments/` 内のみ。
- MedicalVault / LocalOnlyProjects は触れない。
- 観察用スクリーンショットは fair use 観察のみ、artifact には埋め込まない。
- 秘匿情報 / API key / 患者情報なし。
