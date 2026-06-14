#!/usr/bin/env python3
# "Hospital Year-End Party 2026" — a Quiet Lacquer modern-Japanese poster.
# Dark sumi ground, antique gold hairlines, one vermilion seal, drifting snow.
# Render at 2x supersample, downscale with LANCZOS. No halftone / no misregistration.

import math, random, datetime
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(31); np.random.seed(31)

SS = 2
WD, HD = 2480, 3508
W, H = WD * SS, HD * SS
def s(v): return v * SS

LAT = "/Users/metcharoba/CreativeVault/.claude/skills/canvas-design/canvas-fonts/"
JMIN = "/System/Library/Fonts/ヒラギノ明朝 ProN.ttc"
JSAN = "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"
JSAN4 = "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc"

def FL(name, size):
    if not name.endswith(".ttf"): name += ".ttf"
    return ImageFont.truetype(LAT + name, int(round(size * SS)))
def FJ(path, size, index=0):
    return ImageFont.truetype(path, int(round(size * SS)), index=index)

# ---- Quiet Lacquer palette ----------------------------------------------
SUMI  = (33, 30, 27)
IVORY = (236, 229, 214)
GOLD  = (198, 162, 96)
GOLDD = (150, 120, 70)      # dimmer gold
RED   = (190, 54, 44)

def rgba(c, a): return (c[0], c[1], c[2], int(a))

# =========================================================================
# ground: warm sumi with vertical tonal breath + washi grain
# =========================================================================
base = np.zeros((H, W, 3), np.float32)
for i, c in enumerate(SUMI): base[..., i] = c
# subtle vertical lightening toward upper-center (a quiet glow)
yy, xx = np.mgrid[0:H, 0:W]
glow = np.exp(-(((xx - W*0.5)/(W*0.62))**2 + ((yy - H*0.30)/(H*0.42))**2))
base += glow[..., None] * np.array([13, 11, 8])
# washi fiber grain (fine + a few longer fibers via low-freq)
base += np.random.normal(0, 2.6, (H, W, 1)).astype(np.float32)
lf = np.random.normal(0, 1, (H//70, W//70)).astype(np.float32)
lf = np.asarray(Image.fromarray(((lf-lf.min())/(lf.ptp()+1e-6)*255).astype('uint8'))
                .resize((W, H), Image.BICUBIC), np.float32)/255.0
base += (lf - 0.5)[..., None] * 7.0
img = Image.fromarray(np.clip(base, 0, 255).astype('uint8'), 'RGB').convert('RGBA')
dr = ImageDraw.Draw(img, 'RGBA')

MT = 250
CX = WD/2

# soft warm winter-moon glow behind the focal motif (hospitality warmth)
_rcx, _rcy, _sig = WD/2*SS, 800*SS, 300*SS
ga = (np.exp(-(((xx-_rcx)**2 + (yy-_rcy)**2)/(2*_sig**2))) * 46).astype('uint8')
glow = Image.merge("RGBA", (Image.new("L",(W,H),224), Image.new("L",(W,H),202),
                            Image.new("L",(W,H),150), Image.fromarray(ga)))
img.alpha_composite(glow)

# =========================================================================
# fine gold frame (double hairline — the invitation border)
# =========================================================================
def rect(x0, y0, x1, y1, col, w):
    dr.rectangle([s(x0), s(y0), s(x1), s(y1)], outline=col, width=int(w*SS))
rect(150, 150, WD-150, HD-150, rgba(GOLD, 150), 1.6)
rect(168, 168, WD-168, HD-168, rgba(GOLDD, 110), 1.0)
# small corner ticks for craft
for cx_, cy_ in [(150,150),(WD-150,150),(150,HD-150),(WD-150,HD-150)]:
    dr.line([s(cx_-20), s(cy_), s(cx_+20), s(cy_)], fill=rgba(GOLD,160), width=int(1.4*SS))
    dr.line([s(cx_), s(cy_-20), s(cx_), s(cy_+20)], fill=rgba(GOLD,160), width=int(1.4*SS))

# =========================================================================
# snow-ring (雪輪) — fine scalloped gold line, the quiet focal motif
# =========================================================================
ring_cx, ring_cy, R = CX, 800, 320
def snowring(cx, cy, R, depth, lobes, col, width, phase=0.0):
    pts = []
    for i in range(721):
        th = math.radians(i*0.5)
        r = R - depth*0.5*(1+math.cos(lobes*(th+phase)))
        pts.append((s(cx + r*math.cos(th)), s(cy + r*math.sin(th))))
    dr.line(pts, fill=col, width=int(width*SS), joint="curve")
snowring(ring_cx, ring_cy, R, 34, 6, rgba(GOLD, 185), 2.4)
snowring(ring_cx, ring_cy, R-16, 30, 6, rgba(GOLDD, 95), 1.1)

# a few delicate snow crystals (6-fold) inside/around the ring
def crystal(cx, cy, r, col, w=1.1):
    for k in range(3):
        a = math.radians(60*k)
        dr.line([s(cx-r*math.cos(a)), s(cy-r*math.sin(a)),
                 s(cx+r*math.cos(a)), s(cy+r*math.sin(a))], fill=col, width=int(w*SS))
        for sgn in (1,-1):
            bx, by = cx+ r*0.55*math.cos(a)*sgn, cy+ r*0.55*math.sin(a)*sgn
            for bb in (a+math.radians(35), a-math.radians(35)):
                dr.line([s(bx), s(by), s(bx+r*0.28*math.cos(bb)), s(by+r*0.28*math.sin(bb))],
                        fill=col, width=int(w*SS))
crystal(ring_cx, ring_cy, 30, rgba(IVORY, 150))
crystal(ring_cx-150, ring_cy-90, 18, rgba(GOLD, 150))
crystal(ring_cx+165, ring_cy+70, 15, rgba(GOLD, 130))

# drifting snow (sparse fine dots, upper field)
for _ in range(90):
    sx = random.uniform(220, WD-220); sy = random.uniform(240, 1500)
    rr = random.uniform(1.2, 3.2); a = random.uniform(40, 150)
    dr.ellipse([s(sx)-s(rr), s(sy)-s(rr), s(sx)+s(rr), s(sy)+s(rr)], fill=rgba(IVORY, a))

# =========================================================================
# vertical Japanese accent on the right margin  (忘年会 / 二〇二六)
# =========================================================================
def vtext(cx, y0, chars, font, fill, gap):
    y = y0
    for ch in chars:
        bb = font.getbbox(ch)
        chh = (bb[3]-bb[1]) / SS
        dr.text((s(cx), s(y)), ch, font=font, fill=fill, anchor="ma")
        y += chh + gap
    return y
vtext(2120, 430, "忘年会", FJ(JMIN, 104, 1), rgba(IVORY, 235), 46)
vtext(2120, 905, "二〇二六", FJ(JMIN, 50), rgba(GOLD, 210), 30)
# a thin gold rule beside the vertical column
dr.line([s(2192), s(440), s(2192), s(1130)], fill=rgba(GOLDD, 120), width=int(1.0*SS))

# =========================================================================
# title lockup (centered)  HOSPITAL / Year-End Party / 2026
# =========================================================================
def ctext(cx, y_base, text, font, fill, tracking=0.0):
    if tracking == 0:
        dr.text((s(cx), s(y_base)), text, font=font, fill=fill, anchor="ms")
        return
    w = sum(font.getlength(ch)/SS for ch in text) + tracking*(len(text)-1)
    x = cx - w/2
    for ch in text:
        dr.text((s(x), s(y_base)), ch, font=font, fill=fill, anchor="ls")
        x += font.getlength(ch)/SS + tracking

# overline
ctext(CX, 1320, "HOSPITAL", FL("Italiana-Regular", 60), rgba(IVORY, 210), tracking=22)
dr.line([s(CX-150), s(1356), s(CX+150), s(1356)], fill=rgba(GOLD,140), width=int(1.0*SS))
# hero line
ctext(CX, 1560, "Year-End Party", FL("Italiana-Regular", 210), rgba(IVORY, 248))
# year in gold
ctext(CX, 1760, "2026", FL("Italiana-Regular", 150), rgba(GOLD, 235), tracking=14)

# short italic line
ctext(CX, 1900, "A warm gathering to close the year.",
      FL("CrimsonPro-Italic", 56), rgba(IVORY, 200))

# =========================================================================
# central seal divider:  hairline — vermilion seal (宴) — hairline
# =========================================================================
seal_cy = 2040
# flanking hairlines
dr.line([s(360), s(seal_cy), s(CX-110), s(seal_cy)], fill=rgba(GOLD,150), width=int(1.2*SS))
dr.line([s(CX+110), s(seal_cy), s(WD-360), s(seal_cy)], fill=rgba(GOLD,150), width=int(1.2*SS))
# seal: rounded square, vermilion, slightly imperfect, carved ivory char
sl = 78
sealbox = [s(CX-sl), s(seal_cy-sl), s(CX+sl), s(seal_cy+sl)]
dr.rounded_rectangle(sealbox, radius=s(16), fill=rgba(RED, 255))
# subtle ink texture on the seal (slightly uneven)
seal_layer = Image.new("L", (W, H), 0)
sd = ImageDraw.Draw(seal_layer)
sd.rounded_rectangle(sealbox, radius=s(16), fill=255)
# carve the character out (draw char in ground color)
ch_font = FJ(JMIN, 116, 1)
dr.text((s(CX), s(seal_cy+4)), "宴", font=ch_font, fill=rgba(SUMI, 255), anchor="mm")
# thin inner keyline on seal
dr.rounded_rectangle([s(CX-sl+10), s(seal_cy-sl+10), s(CX+sl-10), s(seal_cy+sl-10)],
                     radius=s(10), outline=rgba(IVORY, 70), width=int(1.0*SS))

# =========================================================================
# information block (bilingual, calm, gold labels + ivory values)
# =========================================================================
info = [
    ("DATE",     "日付", "2026.12.18  (Fri)"),
    ("TIME",     "時間", "18:30 – 21:00"),
    ("VENUE",    "会場", "The Grand Hotel — Hall “Suiren”"),
    ("ADDRESS",  "住所", "1-2-3 Marunouchi, Toyama City"),
    ("FEE",      "会費", "¥6,000"),
    ("DEADLINE", "締切", "RSVP by 2026.12.05"),
    ("CONTACT",  "幹事", "Year-End Party Committee · ext. 1234"),
]
iy = 2230
row_h = 132
lab_x = 470
val_x = 880
flab = FL("Jura-Medium", 33)
fjlab = FJ(JSAN, 24)
fval = FL("CrimsonPro-Regular", 50)
fjval = FJ(JMIN, 40)
for i, (lab, jlab, val) in enumerate(info):
    y = iy + i*row_h
    # label (EN small caps gold + JP tiny)
    x = lab_x
    for ch in lab:
        dr.text((s(x), s(y)), ch, font=flab, fill=rgba(GOLD, 225), anchor="ls")
        x += flab.getlength(ch)/SS + 5
    dr.text((s(lab_x), s(y+40)), jlab, font=fjlab, fill=rgba(GOLDD, 200), anchor="ls")
    # value — JP glyphs via mincho fallback, latin via CrimsonPro
    vx = val_x
    for ch in val:
        if ord(ch) > 0x2000 and not (0x2018 <= ord(ch) <= 0x201F):  # CJK / JP
            f = fjval; yoff = 6
        else:
            f = fval; yoff = 0
        dr.text((s(vx), s(y+yoff)), ch, font=f, fill=rgba(IVORY, 238), anchor="ls")
        vx += f.getlength(ch)/SS + 1
    # row hairline
    if i < len(info)-1:
        dr.line([s(lab_x), s(y+row_h-46), s(WD-470), s(y+row_h-46)],
                fill=rgba(GOLDD, 70), width=int(1.0*SS))

# =========================================================================
# faint seigaiha (青海波) band at the hem — seasonal texture, very quiet
# =========================================================================
band_y = HD-300
arc_r = 64
for row in range(3):
    ry_ = band_y + row*30
    off = (arc_r) if row % 2 else 0
    x = 200 - arc_r
    while x < WD-160:
        for k in (0, 1, 2):
            rr = arc_r - k*18
            dr.arc([s(x-rr+off), s(ry_-rr), s(x+rr+off), s(ry_+rr)],
                   start=200, end=340, fill=rgba(GOLDD, 80), width=int(1.0*SS))
        x += arc_r*2

# =========================================================================
# finishing — washi grain pass + gentle vignette
# =========================================================================
img = img.convert("RGB")
arr = np.asarray(img, np.float32)
arr += np.random.normal(0, 2.2, (H, W, 1)).astype(np.float32)
d = np.sqrt(((xx - W/2)/(W/2))**2 + ((yy - H/2)/(H/2))**2)
arr *= (1 - np.clip((d-0.62)*0.12, 0, 0.10))[..., None]
img = Image.fromarray(np.clip(arr, 0, 255).astype('uint8'), 'RGB')

img = img.resize((WD, HD), Image.LANCZOS)
out = "/Users/metcharoba/CreativeVault/70_design_experiments/hospital_year_end_party_2026/hospital_year_end_party_2026.png"
img.save(out, "PNG")
img.save(out.replace(".png", ".pdf"), "PDF", resolution=300)
print("saved", out, img.size, "| 2026-12-18 is", datetime.date(2026,12,18).strftime("%A"))
