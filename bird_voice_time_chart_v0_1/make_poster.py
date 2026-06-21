#!/usr/bin/env python3
"""bird_voice_time_chart_v0_1 — generate index.html with inline SVG.

Run from inside this build directory:
    python3 make_poster.py
Then render to PNG:
    /Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome \\
      --headless=new --disable-gpu --hide-scrollbars \\
      --window-size=1080,1350 --force-device-scale-factor=2 \\
      --screenshot=screenshots/poster_main.png \\
      "file://$(pwd)/index.html"

Boundaries: CreativeVault / 70_design_experiments only. All data is fictional.
"""
import math
from pathlib import Path

# ---- Fictional data ----------------------------------------------------------
# 8 species x 24 hourly activity values in [0, 1]. Fake but shaped to be readable.
SPECIES = [
    {
        "jp": "スズメ", "en": "PASSER MONTANUS",
        "note": "早朝から続く声。昼に一度静かになり夕にまた戻る。",
        "mode": "fill",   "size": 210,  "color": "ink",
        "ticks": 24,
        "data": [0.00, 0.00, 0.00, 0.10, 0.40, 0.70, 0.90, 0.85, 0.60, 0.50,
                 0.40, 0.30, 0.20, 0.20, 0.30, 0.40, 0.55, 0.65, 0.50, 0.30,
                 0.10, 0.00, 0.00, 0.00],
    },
    {
        "jp": "ヒヨドリ", "en": "HYPSIPETES AMAUROTIS",
        "note": "午前と午後に大きな声。昼に一度落ち、夕方に再び。",
        "mode": "fill",   "size": 230,  "color": "accent",
        "ticks": 24,
        "data": [0.00, 0.00, 0.00, 0.00, 0.20, 0.50, 0.65, 0.80, 0.95, 0.75,
                 0.45, 0.30, 0.50, 0.70, 0.85, 0.70, 0.50, 0.40, 0.30, 0.20,
                 0.05, 0.00, 0.00, 0.00],
    },
    {
        "jp": "ハシブトガラス", "en": "CORVUS MACRORHYNCHOS",
        "note": "夜明けと日暮れの薄明に二度の山。",
        "mode": "line",   "size": 210,  "color": "ink",
        "ticks": 12,
        "data": [0.00, 0.00, 0.00, 0.20, 0.60, 0.95, 0.80, 0.55, 0.40, 0.30,
                 0.20, 0.20, 0.20, 0.25, 0.30, 0.45, 0.65, 0.85, 0.95, 0.70,
                 0.30, 0.10, 0.00, 0.00],
    },
    {
        "jp": "シジュウカラ", "en": "PARUS MINOR",
        "note": "早朝の合唱。昼には粒のように散る。",
        "mode": "dot",    "size": 200,  "color": "ink",
        "ticks": 24,
        "data": [0.00, 0.00, 0.00, 0.00, 0.30, 0.70, 0.85, 0.75, 0.60, 0.50,
                 0.40, 0.30, 0.20, 0.15, 0.10, 0.10, 0.20, 0.30, 0.25, 0.10,
                 0.00, 0.00, 0.00, 0.00],
    },
    {
        "jp": "メジロ", "en": "ZOSTEROPS JAPONICUS",
        "note": "朝の窓の外、午前の遅い時間に最も濃い。",
        "mode": "lollipop", "size": 210, "color": "accent",
        "ticks": 24,
        "data": [0.00, 0.00, 0.00, 0.00, 0.00, 0.10, 0.30, 0.60, 0.85, 0.70,
                 0.55, 0.35, 0.20, 0.20, 0.30, 0.30, 0.20, 0.10, 0.00, 0.00,
                 0.00, 0.00, 0.00, 0.00],
    },
    {
        "jp": "キジバト", "en": "STREPTOPELIA ORIENTALIS",
        "note": "一日中、低く、おなじ調子で。",
        "mode": "ring",   "size": 180,  "color": "ink",
        "ticks": 12,
        "data": [0.00, 0.00, 0.00, 0.10, 0.20, 0.30, 0.30, 0.30, 0.30, 0.30,
                 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.25, 0.20,
                 0.10, 0.00, 0.00, 0.00],
    },
    {
        "jp": "ウグイス", "en": "HORORNIS DIPHONE",
        "note": "夜明けに突然はじまり、午前のうちに消える。",
        "mode": "hatch",  "size": 210,  "color": "ink",
        "ticks": 12,
        "data": [0.00, 0.00, 0.00, 0.10, 0.50, 0.95, 0.85, 0.55, 0.25, 0.10,
                 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
                 0.00, 0.00, 0.00, 0.00],
    },
    {
        "jp": "ツバメ", "en": "HIRUNDO RUSTICA",
        "note": "薄明の二度。空気の透ける時間に鳴く。",
        "mode": "fill",   "size": 190,  "color": "accent",
        "ticks": 24,
        "data": [0.00, 0.00, 0.00, 0.00, 0.20, 0.55, 0.65, 0.50, 0.30, 0.20,
                 0.20, 0.20, 0.30, 0.40, 0.45, 0.55, 0.65, 0.75, 0.85, 0.50,
                 0.10, 0.00, 0.00, 0.00],
    },
]

INK = "#1C2A28"
ACCENT = "#B4593A"
PAPER = "#E8E6DD"
MUTE = "#8E8B7E"

# ---- SVG primitives ----------------------------------------------------------
def polar(cx, cy, r, deg):
    """Return (x, y) for radius r at angle deg (0deg = top, clockwise)."""
    rad = math.radians(deg - 90)
    return (cx + r * math.cos(rad), cy + r * math.sin(rad))


def disc_svg(species):
    size = 210  # 全 disc 統一サイズ(整列重視)
    cx, cy = size / 2, size / 2
    r_in = size * 0.18
    r_out = size * 0.44
    color = INK if species["color"] == "ink" else ACCENT
    data = species["data"]
    n = len(data)
    sweep_per = 360 / n
    pieces = []

    # Outer tick ring
    tick_count = species["ticks"]
    for i in range(tick_count):
        deg = i * (360 / tick_count)
        major = (i % (tick_count // 4 if tick_count >= 4 else 1)) == 0
        r1 = r_out + 6
        r2 = r_out + (14 if major else 9)
        x1, y1 = polar(cx, cy, r1, deg)
        x2, y2 = polar(cx, cy, r2, deg)
        pieces.append(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{MUTE}" stroke-width="{1.2 if major else 0.6}" />'
        )
    # Hour labels at cardinal positions
    for hr in (0, 6, 12, 18):
        deg = (hr / 24) * 360
        lx, ly = polar(cx, cy, r_out + 26, deg)
        pieces.append(
            f'<text x="{lx:.2f}" y="{ly:.2f}" font-family="IBM Plex Mono" '
            f'font-size="8.5" fill="{MUTE}" text-anchor="middle" '
            f'dominant-baseline="middle" letter-spacing="0.08em">{hr:02d}</text>'
        )

    # Center dot
    pieces.append(
        f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="1.5" fill="{INK}" />'
    )

    mode = species["mode"]

    if mode == "fill":
        for i, v in enumerate(data):
            if v <= 0.01:
                continue
            a0 = i * sweep_per - sweep_per / 2
            a1 = a0 + sweep_per
            r = r_in + (r_out - r_in) * v
            p0 = polar(cx, cy, r_in, a0)
            p1 = polar(cx, cy, r, a0)
            p2 = polar(cx, cy, r, a1)
            p3 = polar(cx, cy, r_in, a1)
            large = 0
            d = (
                f"M {p0[0]:.2f} {p0[1]:.2f} "
                f"L {p1[0]:.2f} {p1[1]:.2f} "
                f"A {r:.2f} {r:.2f} 0 {large} 1 {p2[0]:.2f} {p2[1]:.2f} "
                f"L {p3[0]:.2f} {p3[1]:.2f} "
                f"A {r_in:.2f} {r_in:.2f} 0 {large} 0 {p0[0]:.2f} {p0[1]:.2f} Z"
            )
            pieces.append(
                f'<path d="{d}" fill="{color}" fill-opacity="0.85" stroke="{PAPER}" stroke-width="0.6" />'
            )

    elif mode == "line":
        for i, v in enumerate(data):
            if v <= 0.01:
                continue
            deg = i * sweep_per
            r = r_in + (r_out - r_in) * v
            p0 = polar(cx, cy, r_in, deg)
            p1 = polar(cx, cy, r, deg)
            pieces.append(
                f'<line x1="{p0[0]:.2f}" y1="{p0[1]:.2f}" '
                f'x2="{p1[0]:.2f}" y2="{p1[1]:.2f}" '
                f'stroke="{color}" stroke-width="1.6" stroke-linecap="round" />'
            )

    elif mode == "dot":
        # density: more dots = louder
        for i, v in enumerate(data):
            if v <= 0.01:
                continue
            deg = i * sweep_per
            count = max(1, int(round(v * 9)))
            for k in range(count):
                rr = r_in + 4 + (r_out - r_in - 8) * (k / max(count - 1, 1))
                px, py = polar(cx, cy, rr, deg)
                pieces.append(
                    f'<circle cx="{px:.2f}" cy="{py:.2f}" r="1.4" fill="{color}" />'
                )

    elif mode == "lollipop":
        for i, v in enumerate(data):
            if v <= 0.01:
                continue
            deg = i * sweep_per
            r = r_in + (r_out - r_in) * v
            p0 = polar(cx, cy, r_in, deg)
            p1 = polar(cx, cy, r, deg)
            pieces.append(
                f'<line x1="{p0[0]:.2f}" y1="{p0[1]:.2f}" '
                f'x2="{p1[0]:.2f}" y2="{p1[1]:.2f}" '
                f'stroke="{color}" stroke-width="0.7" />'
            )
            pieces.append(
                f'<circle cx="{p1[0]:.2f}" cy="{p1[1]:.2f}" r="{2.0 + v*2.2:.2f}" '
                f'fill="{color}" />'
            )

    elif mode == "ring":
        # 3 nested rings; fill the ring whose tier the value reaches
        tiers = [0.15, 0.30, 0.45]
        ring_radii = [
            r_in + (r_out - r_in) * 0.20,
            r_in + (r_out - r_in) * 0.55,
            r_in + (r_out - r_in) * 0.90,
        ]
        # Background ring outlines
        for rr in ring_radii:
            pieces.append(
                f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rr:.2f}" '
                f'fill="none" stroke="{MUTE}" stroke-width="0.5" stroke-dasharray="2 3" />'
            )
        for i, v in enumerate(data):
            if v <= 0.01:
                continue
            a0 = i * sweep_per - sweep_per / 2
            a1 = a0 + sweep_per
            for ti, t in enumerate(tiers):
                if v < t:
                    break
                rr = ring_radii[ti]
                p0 = polar(cx, cy, rr - 4, a0)
                p1 = polar(cx, cy, rr + 4, a0)
                p2 = polar(cx, cy, rr + 4, a1)
                p3 = polar(cx, cy, rr - 4, a1)
                d = (
                    f"M {p0[0]:.2f} {p0[1]:.2f} "
                    f"L {p1[0]:.2f} {p1[1]:.2f} "
                    f"A {rr+4:.2f} {rr+4:.2f} 0 0 1 {p2[0]:.2f} {p2[1]:.2f} "
                    f"L {p3[0]:.2f} {p3[1]:.2f} "
                    f"A {rr-4:.2f} {rr-4:.2f} 0 0 0 {p0[0]:.2f} {p0[1]:.2f} Z"
                )
                pieces.append(
                    f'<path d="{d}" fill="{color}" fill-opacity="0.78" />'
                )

    elif mode == "hatch":
        # short radial hatches; count scales with value
        for i, v in enumerate(data):
            if v <= 0.01:
                continue
            count = max(1, int(round(v * 6)))
            spread = sweep_per * 0.7
            for k in range(count):
                if count == 1:
                    offset = 0
                else:
                    offset = -spread / 2 + (spread * k / (count - 1))
                deg = i * sweep_per + offset
                p0 = polar(cx, cy, r_in + 2, deg)
                p1 = polar(cx, cy, r_in + (r_out - r_in) * v, deg)
                pieces.append(
                    f'<line x1="{p0[0]:.2f}" y1="{p0[1]:.2f}" '
                    f'x2="{p1[0]:.2f}" y2="{p1[1]:.2f}" '
                    f'stroke="{color}" stroke-width="0.9" stroke-linecap="round" />'
                )

    body = "\n    ".join(pieces)
    return (
        f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" '
        f'xmlns="http://www.w3.org/2000/svg">\n    {body}\n  </svg>'
    )


# ---- HTML --------------------------------------------------------------------
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>鳥の声の時刻分布</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@500;700&family=Noto+Sans+JP:wght@300;500&family=IBM+Plex+Mono:wght@300;500&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ width: 1080px; height: 1080px; overflow: hidden; }}
  body {{
    background: {PAPER};
    color: {INK};
    font-family: 'Noto Sans JP', sans-serif;
    font-weight: 300;
    position: relative;
    padding: 60px 64px 50px;
  }}
  .rule-top {{
    border-top: 2px solid {INK};
    padding-top: 14px;
  }}
  .title-block {{
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: end;
    margin-bottom: 6px;
  }}
  .title-jp {{
    font-family: 'Noto Serif JP', serif;
    font-size: 62px;
    font-weight: 700;
    line-height: 1.02;
    letter-spacing: 0.02em;
  }}
  .title-en {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    font-weight: 300;
    text-transform: uppercase;
    letter-spacing: 0.22em;
    color: {MUTE};
    text-align: right;
    line-height: 1.6;
  }}
  .deck {{
    border-top: 1px solid {MUTE};
    border-bottom: 1px solid {MUTE};
    padding: 8px 0;
    margin: 12px 0 26px;
    display: flex;
    justify-content: space-between;
    font-size: 12.5px;
    letter-spacing: 0.02em;
  }}
  .deck .mono {{
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: 0.14em;
    color: {MUTE};
    font-size: 11px;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: auto auto;
    gap: 16px 0;
    align-items: start;
    justify-items: center;
    margin-bottom: 18px;
  }}
  .disc {{
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    width: 100%;
  }}
  .disc svg {{ display: block; }}
  .disc-no {{
    position: absolute;
    top: 0;
    left: 12px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    color: {MUTE};
  }}
  .species-jp {{
    font-family: 'Noto Serif JP', serif;
    font-weight: 500;
    font-size: 17px;
    margin-top: 8px;
    text-align: center;
  }}
  .species-en {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 8.5px;
    letter-spacing: 0.12em;
    color: {MUTE};
    margin-top: 3px;
    text-align: center;
  }}
  .species-note {{
    font-size: 10.5px;
    margin-top: 6px;
    text-align: center;
    max-width: 200px;
    line-height: 1.45;
    color: {INK};
  }}
  /* offset second row slightly (non-uniform placement) */
  .disc--lift {{ transform: translateY(-12px); }}
  .disc--drop {{ transform: translateY(8px); }}
  /* per-disc label-side variant: put label to the side */
  .disc--side {{ flex-direction: row; align-items: flex-start; gap: 10px; }}
  .disc--side .label-stack {{ text-align: left; margin-top: 18px; }}
  .disc--side .species-jp {{ text-align: left; margin-top: 0; }}
  .disc--side .species-en {{ text-align: left; }}
  .disc--side .species-note {{ text-align: left; max-width: 110px; }}
  .method {{
    margin: 14px 0 0;
  }}
  .method .marker {{
    display: inline-block;
    border-top: 2px solid {ACCENT};
    padding-top: 6px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 9.5px;
    letter-spacing: 0.14em;
    color: {ACCENT};
    margin-bottom: 12px;
    min-width: 80px;
  }}
  .method-text {{
    font-size: 11.5px;
    line-height: 1.7;
    max-width: 720px;
  }}
  .footer {{
    position: absolute;
    bottom: 24px;
    left: 64px;
    right: 64px;
    border-top: 1px solid {MUTE};
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 9.5px;
    letter-spacing: 0.14em;
    color: {MUTE};
  }}
</style>
</head>
<body>
  <section class="rule-top">
    <header class="title-block">
      <div class="title-jp">鳥の声の<br>時刻分布</div>
      <div class="title-en">DIURNAL VOCALIZATION CHART<br>SPECIES &times; HOUR &mdash; FIG. 01—08</div>
    </header>
    <div class="deck">
      <span>都内 / ある一日 / 観測 8 種 / 1 点 = ある時間幅で確認された鳴き声</span>
      <span class="mono">N = 08</span>
    </div>
  </section>

  <div class="grid">
{DISCS}
  </div>

  <div class="method">
    <div class="marker">METHOD</div>
    <div class="method-text">
      ある一日、夜明け前から日暮れまでの間、8 種の鳴き声を確認時刻ごとに記録した架空の観測。
      半径は時間内に確認された鳴き声の量、種ごとに表記様式(塗り / 線 / 点群 / 茎 / 同心三層 / 放射ハッチ)を変えている。
      一日を時計の文字盤に巻き戻したとき、どの種がどの時刻で鳴いているかが版面そのものに残るように設計した。
    </div>
  </div>

  <footer class="footer">
    <span>FICTIONAL DATASET &middot; CREATIVEVAULT 70_DESIGN_EXPERIMENTS &middot; 2026</span>
    <span>都市鳥類観測ノート &middot; 観測者不詳</span>
  </footer>
</body>
</html>
"""


def render_discs():
    # Offset / side-label patterns for non-uniform placement
    placement = [""] * 8  # 整列重視:cell ごとの上下オフセット廃止
    side_label = set()  # side-label外し: 横形式の異質さが浮いていた指摘を受けて削除
    items = []
    for i, sp in enumerate(SPECIES):
        cls = ["disc", placement[i]]
        if i in side_label:
            cls.append("disc--side")
        cls = " ".join(c for c in cls if c)
        svg = disc_svg(sp)
        label_stack = (
            f'<div class="label-stack">'
            f'<div class="species-jp">{sp["jp"]}</div>'
            f'<div class="species-en">{sp["en"]}</div>'
            f'<div class="species-note">{sp["note"]}</div>'
            f'</div>'
        )
        items.append(
            f'<div class="{cls}">'
            f'<span class="disc-no">FIG. {i+1:02d}</span>'
            f'{svg}{label_stack}'
            f'</div>'
        )
    return "\n    ".join(items)


def main():
    html = HTML_TEMPLATE.format(
        PAPER=PAPER, INK=INK, MUTE=MUTE, ACCENT=ACCENT,
        DISCS=render_discs(),
    )
    out = Path(__file__).parent / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
