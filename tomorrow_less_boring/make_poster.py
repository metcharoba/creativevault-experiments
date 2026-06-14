#!/usr/bin/env python3
# "Tomorrow Less Boring" — a Soft Empiricism poster.
# Render at 2x supersample, downscale with LANCZOS for crisp, print-quality output.

import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(11)
np.random.seed(11)

# ----- canvas -------------------------------------------------------------
SS = 2
WD, HD = 2480, 3508                 # A4 @ ~300dpi, portrait (design coords)
W,  H  = WD * SS, HD * SS           # render coords
def s(v): return v * SS             # design -> render

FD = "/Users/metcharoba/CreativeVault/.claude/skills/canvas-design/canvas-fonts/"
def F(name, size):
    if not name.endswith(".ttf"):
        name += ".ttf"
    return ImageFont.truetype(FD + name, int(round(size * SS)))

# ----- palette ------------------------------------------------------------
PAPER = (231, 225, 209)
INK   = (28, 26, 22)
VERM  = (211, 70, 38)

MARG_L, MARG_R, MARG_T, MARG_B = 215, 215, 215, 215
CW_L, CW_R = MARG_L, WD - MARG_R   # content left / right edges (design)

# ==========================================================================
# 1. PAPER  (warm bone with low-freq mottle + fine grain)
# ==========================================================================
paper = np.zeros((H, W, 3), np.float32)
for i, c in enumerate(PAPER):
    paper[..., i] = c

# low-frequency mottle (uneven sheet tone)
lf = np.random.normal(0, 1, (max(2, H // 60), max(2, W // 60))).astype(np.float32)
lf_img = Image.fromarray(((lf - lf.min()) / (lf.ptp() + 1e-6) * 255).astype('uint8'))
lf_img = lf_img.resize((W, H), Image.BICUBIC)
lf_arr = (np.asarray(lf_img, np.float32) / 255.0 - 0.5)[..., None]
paper += lf_arr * 11.0

# fine paper grain
paper += np.random.normal(0, 3.2, (H, W, 1)).astype(np.float32)

base = Image.fromarray(np.clip(paper, 0, 255).astype('uint8'), 'RGB')

# layers
ink   = Image.new('RGBA', (W, H), (0, 0, 0, 0))   # everything ink-colored
verm  = Image.new('RGBA', (W, H), (0, 0, 0, 0))   # vermilion accent
di = ImageDraw.Draw(ink)
dv = ImageDraw.Draw(verm)

def ink_rgba(a):  return (INK[0], INK[1], INK[2], int(a))
def verm_rgba(a): return (VERM[0], VERM[1], VERM[2], int(a))

# ==========================================================================
# 2. GHOST GRAPH-PAPER  (whisper-faint measured dot grid, full field)
# ==========================================================================
step = 58
for gx in range(MARG_L, CW_R + 1, step):
    for gy in range(MARG_T, HD - MARG_B + 1, step):
        di.ellipse([s(gx) - 1.6, s(gy) - 1.6, s(gx) + 1.6, s(gy) + 1.6],
                   fill=ink_rgba(13))

# ==========================================================================
# 3. TOP REGISTER  (hairline + clinical corner labels)
# ==========================================================================
mono  = F("GeistMono-Regular", 25)
monob = F("GeistMono-Bold", 25)

hl_y = 262
di.line([s(CW_L), s(hl_y), s(CW_R), s(hl_y)], fill=ink_rgba(205), width=int(1.6 * SS))

def tx(draw, xy, text, font, fill, anchor="ls", tracking=0.0):
    """draw text with optional letter tracking (design px)."""
    if tracking == 0:
        draw.text((s(xy[0]), s(xy[1])), text, font=font, fill=fill, anchor=anchor)
        return
    # manual tracking, left/baseline only
    x = xy[0]
    for ch in text:
        draw.text((s(x), s(xy[1])), ch, font=font, fill=fill, anchor="ls")
        x += font.getlength(ch) / SS + tracking

tx(di, (CW_L, hl_y - 22), "FIG. 01", monob, ink_rgba(220), tracking=2.4)
tx(di, (CW_L + 150, hl_y - 22), "— A FORECAST OF TEDIUM", mono, ink_rgba(150), tracking=2.4)
di.text((s(CW_R), s(hl_y - 22)), "OBS.  MMXXVI", font=mono, fill=ink_rgba(170), anchor="rs")
# tiny line below rule, left + right
di.text((s(CW_L), s(hl_y + 40)), "INSTRUMENT — SOFT EMPIRICISM", font=mono, fill=ink_rgba(120), anchor="ls")
di.text((s(CW_R), s(hl_y + 40)), "PLATE  I / I", font=mono, fill=ink_rgba(120), anchor="rs")

# ==========================================================================
# 4. HEADLINE  (fit two lines flush to a measure; inky texture)
# ==========================================================================
HEAD_W = 1985                      # measure for the type block
def fit_size(text, fontfile, target_w, probe=200):
    f = F(fontfile, probe)
    return probe * (target_w / (f.getlength(text) / SS))

kick = F("InstrumentSerif-Italic", 50)
tx(di, (CW_L + 6, 1018), "a quiet forecast —", kick, ink_rgba(165), tracking=0.6)

line1, line2 = "Tomorrow,", "less boring"
sz1 = fit_size(line1, "Italiana-Regular", HEAD_W)
sz2 = fit_size(line2, "Italiana-Regular", HEAD_W)
f1, f2 = F("Italiana-Regular", sz1), F("Italiana-Regular", sz2)

# headline drawn to its own mask, then given a faint printed unevenness
hmask = Image.new('L', (W, H), 0)
dh = ImageDraw.Draw(hmask)
y1, y2 = 1330, 1660
dh.text((s(CW_L), s(y1)), line1, font=f1, fill=255, anchor="ls")
dh.text((s(CW_L), s(y2)), line2, font=f2, fill=255, anchor="ls")

m = np.asarray(hmask, np.float32) / 255.0
# coarse ink grain (upscaled noise) -> subtle plate unevenness
cg = np.random.normal(1.0, 1.0, (H // 6, W // 6)).astype(np.float32)
cg = np.asarray(Image.fromarray(((np.clip(cg, -3, 3) + 3) / 6 * 255).astype('uint8'))
                .resize((W, H), Image.BICUBIC), np.float32) / 255.0
tex = 0.90 + 0.10 * cg                       # 0.90..1.00
m = m * np.clip(tex, 0, 1)
htex = Image.fromarray((m * 255).astype('uint8'), 'L')
ink.paste(Image.new('RGBA', (W, H), ink_rgba(255)), (0, 0), htex)

# single vermilion accent #1: the period after "boring"
end_x = CW_L + f2.getlength(line2) / SS
dot_r = 13
dv.ellipse([s(end_x + 16) - s(dot_r), s(y2 - 8) - s(dot_r),
            s(end_x + 16) + s(dot_r), s(y2 - 8) + s(dot_r)], fill=verm_rgba(255))

# quiet bridge: short rule + mono caption tying headline -> figure
br_y = 1855
di.line([s(CW_L + 2), s(br_y), s(CW_L + 78), s(br_y)], fill=ink_rgba(170), width=int(1.4 * SS))
tx(di, (CW_L + 96, br_y + 8), "THE TEDIUM INDEX, OBSERVED ACROSS A SINGLE NIGHT",
   F("GeistMono-Regular", 23), ink_rgba(150), tracking=1.4)

# ==========================================================================
# 5. THE FORECAST  (axis, ghost hatch, descending curve, marker, fragments)
# ==========================================================================
ax_l, ax_r = 332, 2178             # plot box (design)
ax_t, ax_b = 1995, 2930            # top / baseline
trend_top, trend_bot = 2095, 2820  # curve high (today) .. low (tomorrow)

# axis baseline + left axis
di.line([s(ax_l), s(ax_b), s(ax_r), s(ax_b)], fill=ink_rgba(210), width=int(1.6 * SS))
di.line([s(ax_l), s(ax_t), s(ax_l), s(ax_b)], fill=ink_rgba(150), width=int(1.4 * SS))

# Y ticks + labels (tedium index 100..0)
for i, val in enumerate([100, 75, 50, 25, 0]):
    yy = ax_t + (ax_b - ax_t) * i / 4
    di.line([s(ax_l) - s(9), s(yy), s(ax_l), s(yy)], fill=ink_rgba(150), width=int(1.3 * SS))
    di.text((s(ax_l) - s(20), s(yy)), str(val), font=F("GeistMono-Regular", 22),
            fill=ink_rgba(130), anchor="rm")
# rotated Y title
yt = Image.new('RGBA', (s(560), s(60)), (0, 0, 0, 0))
ImageDraw.Draw(yt).text((0, s(30)), "I N D E X   O F   T E D I U M",
                        font=F("GeistMono-Regular", 22), fill=ink_rgba(150), anchor="lm")
yt = yt.rotate(90, expand=True)
ink.alpha_composite(yt, (s(ax_l) - s(96), s(ax_t) - s(8)))

# X ticks (5) with end labels
xpos = [ax_l + (ax_r - ax_l) * i / 4 for i in range(5)]
for i, xx in enumerate(xpos):
    di.line([s(xx), s(ax_b), s(xx), s(ax_b) + s(10)], fill=ink_rgba(150), width=int(1.3 * SS))
tx(di, (ax_l, ax_b + 56), "TODAY", F("GeistMono-Regular", 23), ink_rgba(150), tracking=1.6)
di.text((s(ax_r), s(ax_b + 56)), "TOMORROW", font=F("GeistMono-Bold", 23),
        fill=ink_rgba(210), anchor="rs")

# the curve (eased descent + faint hand-plotted wobble)
def ease(t):  # easeInOutCubic
    return 4 * t**3 if t < 0.5 else 1 - (-2 * t + 2)**3 / 2
N = 320
xs = np.linspace(ax_l + 35, ax_r, N)
wob = np.random.normal(0, 1, N)
wob = np.convolve(wob, np.ones(22) / 22, mode='same')   # smoothed jitter
ys = []
for i in range(N):
    t = i / (N - 1)
    y = trend_top + (trend_bot - trend_top) * ease(t)
    y += wob[i] * 5.0 * (1 - t)                          # wobble fades toward the marker
    ys.append(y)
pts = [(s(xs[i]), s(ys[i])) for i in range(N)]

# ghost hatch fill under the curve (patient repetition)
for i in range(0, N, 3):
    di.line([pts[i][0], pts[i][1], pts[i][0], s(ax_b)], fill=ink_rgba(16), width=int(1.0 * SS))

# the ink curve (single pass, crisp)
di.line(pts, fill=ink_rgba(238), width=int(3.0 * SS), joint="curve")

# end marker at "tomorrow" low point  (vermilion accent #2 — the punchline)
ex, ey = pts[-1]
dv.ellipse([ex - s(13) + s(5), ey - s(13) - s(4), ex + s(13) + s(5), ey + s(13) - s(4)],
           fill=verm_rgba(70))                      # faint riso ghost on the accent
dv.ellipse([ex - s(13), ey - s(13), ex + s(13), ey + s(13)], fill=verm_rgba(255))
di.ellipse([ex - s(24), ey - s(24), ex + s(24), ey + s(24)], outline=ink_rgba(150), width=int(1.3 * SS))
di.text((ex - s(40), ey - s(36)), "PROJECTED LOW", font=F("GeistMono-Regular", 21),
        fill=ink_rgba(160), anchor="rs")
di.text((ex - s(40), ey + s(2)), "−61%", font=F("GeistMono-Bold", 23),
        fill=verm_rgba(255), anchor="rs")

# two plotted "fragments" above the curve (+ marks with micro labels)
def plus(draw, x, y, r, col, w=1.3):
    draw.line([s(x - r), s(y), s(x + r), s(y)], fill=col, width=int(w * SS))
    draw.line([s(x), s(y - r), s(x), s(y + r)], fill=col, width=int(w * SS))

frag = [(0.30, "frag. 04", -150), (0.62, "obs. —", -130)]
for tf, lab, dy in frag:
    fx = ax_l + 35 + (ax_r - (ax_l + 35)) * tf
    # height a bit above the curve at that t
    fy = (trend_top + (trend_bot - trend_top) * ease(tf)) - 150
    plus(di, fx, fy, 9, ink_rgba(170))
    di.text((s(fx) + s(16), s(fy)), lab, font=F("GeistMono-Regular", 21),
            fill=ink_rgba(150), anchor="lm")

# ==========================================================================
# 6. FOOTER  (hairline + supporting line + catalogue mark)
# ==========================================================================
fy_ = 3168
di.line([s(CW_L), s(fy_), s(CW_R), s(fy_)], fill=ink_rgba(205), width=int(1.6 * SS))
sup = "Creative experiments, visual notes, and future fragments."
di.text((s(CW_L), s(fy_ + 72)), sup, font=F("InstrumentSerif-Italic", 51),
        fill=ink_rgba(210), anchor="ls")
di.text((s(CW_R), s(fy_ + 66)), "N°35.6′  E139.7′", font=mono,
        fill=ink_rgba(130), anchor="rs")

# ==========================================================================
# 7. COMPOSITE + final texture
# ==========================================================================
base = base.convert('RGBA')
# vermilion ghost already inside verm layer; composite ink then verm
base.alpha_composite(ink)
base.alpha_composite(verm)
img = base.convert('RGB')

# faint global vignette
arr = np.asarray(img, np.float32)
yy, xx = np.mgrid[0:H, 0:W]
cx, cy = W / 2, H / 2
d = np.sqrt(((xx - cx) / (W / 2))**2 + ((yy - cy) / (H / 2))**2)
vig = (1 - np.clip((d - 0.55) * 0.085, 0, 0.05))[..., None]
arr *= vig
# final unifying grain over the whole field
arr += np.random.normal(0, 2.0, (H, W, 1)).astype(np.float32)
img = Image.fromarray(np.clip(arr, 0, 255).astype('uint8'), 'RGB')

# downscale -> crisp
img = img.resize((WD, HD), Image.LANCZOS)
out_png = "/Users/metcharoba/CreativeVault/70_design_experiments/tomorrow_less_boring/tomorrow_less_boring.png"
img.save(out_png, "PNG")
img.convert('RGB').save(out_png.replace('.png', '.pdf'), "PDF", resolution=300)
print("saved", out_png, img.size)
