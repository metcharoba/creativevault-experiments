#!/usr/bin/env python3
# "Creative Signal Night" — a Pulp Voltage comic-book event flyer.
# Render at 2x supersample, downscale with LANCZOS for crisp ink + halftone.

import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(20)
np.random.seed(20)

SS = 2
WD, HD = 2480, 3508
W, H   = WD * SS, HD * SS
def s(v): return v * SS

FD = "/Users/metcharoba/CreativeVault/.claude/skills/canvas-design/canvas-fonts/"
def F(name, size):
    if not name.endswith(".ttf"): name += ".ttf"
    return ImageFont.truetype(FD + name, int(round(size * SS)))

# ---- four-color comic palette -------------------------------------------
NEWS   = (244, 234, 206)
INK    = (24, 21, 19)
RED    = (228, 44, 50)
BLUE   = (33, 86, 168)
NAVY   = (26, 41, 92)
YELLOW = (250, 198, 24)
WHITE  = (250, 246, 235)

img = Image.new("RGB", (W, H), NEWS)
dr  = ImageDraw.Draw(img, "RGBA")

# =========================================================================
# helpers
# =========================================================================
def centroid(pts):
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))

def inset(pts, d):
    cx, cy = centroid(pts)
    out = []
    for x, y in pts:
        vx, vy = x - cx, y - cy
        L = math.hypot(vx, vy) or 1
        out.append((x - vx / L * d, y - vy / L * d))
    return out

def ink_poly(pts, fill, ink=9, misreg=(5, -5)):
    """black body + inset color fill, slightly off-register (comic print look)."""
    dr.polygon([(s(x), s(y)) for x, y in pts], fill=INK)
    ip = inset(pts, ink)
    ip = [(x + misreg[0], y + misreg[1]) for x, y in ip]
    dr.polygon([(s(x), s(y)) for x, y in ip], fill=fill)
    return ip

def starburst(cx, cy, r_out, r_in, n, rot=0, jitter=0.0, ry_scale=1.0):
    pts = []
    for i in range(n * 2):
        ang = rot + i * math.pi / n
        r = r_out if i % 2 == 0 else r_in
        if jitter:
            r *= 1 + random.uniform(-jitter, jitter)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang) * ry_scale))
    return pts

def halftone(bbox, color, spacing=24, radius=7, stagger=True, alpha=255,
             grad=None):
    """RGBA dot field inside bbox (design coords). grad=(cx,cy,r0,r1,minf,maxf)
       scales radius by distance for radial tone."""
    x0, y0, x1, y1 = bbox
    layer = Image.new("RGBA", (s(int(x1 - x0)), s(int(y1 - y0))), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    col = (color[0], color[1], color[2], alpha)
    row = 0
    yy = 0
    while yy < (y1 - y0):
        off = (spacing / 2) if (stagger and row % 2) else 0
        xx = -off
        while xx < (x1 - x0):
            r = radius
            if grad:
                gcx, gcy, r0, r1, mnf, mxf = grad
                dist = math.hypot((x0 + xx) - gcx, (y0 + yy) - gcy)
                t = max(0.0, min(1.0, (dist - r0) / (r1 - r0 + 1e-6)))
                r = radius * (mnf + (mxf - mnf) * t)
            if r > 0.4:
                d.ellipse([s(xx) - s(r), s(yy) - s(r), s(xx) + s(r), s(yy) + s(r)], fill=col)
            xx += spacing
        yy += spacing * (0.5 if stagger else 1.0) if False else spacing
        row += 1
    img.paste(layer, (s(int(x0)), s(int(y0))), layer)

def speed_lines(cx, cy, r0, r1, n, clip_bbox, color=INK, wmin=2, wmax=16):
    """radiating wedges from (cx,cy); clipped to clip_bbox via mask."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    for i in range(n):
        a = 2 * math.pi * i / n + random.uniform(-0.01, 0.01)
        w = random.uniform(wmin, wmax)
        # wedge as thin triangle
        ax, ay = cx + r0 * math.cos(a), cy + r0 * math.sin(a)
        perp = a + math.pi / 2
        bx = cx + r1 * math.cos(a) + math.cos(perp) * w
        by = cy + r1 * math.sin(a) + math.sin(perp) * w
        ccx = cx + r1 * math.cos(a) - math.cos(perp) * w
        ccy = cy + r1 * math.sin(a) - math.sin(perp) * w
        d.polygon([(s(ax), s(ay)), (s(bx), s(by)), (s(ccx), s(ccy))], fill=color)
    mask = Image.new("L", (W, H), 0)
    md = ImageDraw.Draw(mask)
    md.rectangle([s(clip_bbox[0]), s(clip_bbox[1]), s(clip_bbox[2]), s(clip_bbox[3])], fill=255)
    img.paste(layer, (0, 0), Image.composite(layer.split()[3], Image.new("L", (W, H), 0), mask))

def tx(xy, text, font, fill, anchor="la", tracking=0.0, draw=dr):
    if tracking == 0:
        draw.text((s(xy[0]), s(xy[1])), text, font=font, fill=fill, anchor=anchor)
        return font.getlength(text) / SS
    x = xy[0]
    for ch in text:
        draw.text((s(x), s(xy[1])), ch, font=font, fill=fill, anchor="la" if "a" in anchor else "ls")
        x += font.getlength(ch) / SS + tracking
    return x - xy[0]

def outline_text(xy, text, font, fill, ow=8, outline=INK, shadow=None,
                 sh_off=(16, 16), anchor="la", tracking=0.0):
    x, y = xy
    if shadow:
        _stamp((x + sh_off[0], y + sh_off[1]), text, font, shadow, anchor, tracking)
    # outline ring
    for ang in range(0, 360, 24):
        ox = math.cos(math.radians(ang)) * ow
        oy = math.sin(math.radians(ang)) * ow
        _stamp((x + ox, y + oy), text, font, outline, anchor, tracking)
    _stamp((x, y), text, font, fill, anchor, tracking)

def _stamp(xy, text, font, fill, anchor, tracking):
    if tracking == 0:
        dr.text((s(xy[0]), s(xy[1])), text, font=font, fill=fill, anchor=anchor)
    else:
        x = xy[0]
        for ch in text:
            dr.text((s(x), s(xy[1])), ch, font=font, fill=fill, anchor=anchor)
            x += font.getlength(ch) / SS + tracking

def measure(text, font, tracking=0.0):
    base = font.getlength(text) / SS
    return base + tracking * max(0, len(text) - 1)

# =========================================================================
# 0. background tone + page border
# =========================================================================
# faint full-page newsprint halftone in red, very light, lower band
halftone((70, 2050, 2410, 3380), RED, spacing=30, radius=3.2, alpha=34)

B = 60   # border inset
dr.rectangle([s(B), s(B), s(WD - B), s(HD - B)], outline=INK, width=int(11 * SS))
dr.rectangle([s(B + 26), s(B + 26), s(WD - B - 26), s(HD - B - 26)], outline=INK, width=int(2.5 * SS))

ML, MR, MT = 120, 120, 120
CL, CR = ML, WD - MR

# =========================================================================
# 1. top corner tabs + masthead banner
# =========================================================================
# left issue tab
ink_poly([(CL, 150), (CL + 360, 150), (CL + 360, 232), (CL, 232)], INK, ink=0, misreg=(0, 0))
tx((CL + 26, 165), "ISSUE No.01", F("BigShoulders-Bold", 50), YELLOW, tracking=2)
# right "TOYAMA / 2026" tab
tab_w = 360
ink_poly([(CR - tab_w, 150), (CR, 150), (CR, 232), (CR - tab_w, 232)], RED, ink=6)
tx((CR - tab_w + 26, 167), "TOYAMA · MMXXVI", F("BigShoulders-Bold", 44), WHITE, tracking=1)

# masthead transmission banner (slanted parallelogram)
by = 262
sl = 36
ink_poly([(CL, by), (CR, by - sl), (CR, by + 96 - sl), (CL, by + 96)], BLUE, ink=8, misreg=(6, 6))
halftone((CL, by - sl, CR, by + 100), WHITE, spacing=22, radius=2.4, alpha=40)
# banner text follows slant roughly (single line, mid)
tx((CL + 40, by + 14), "// INCOMING TRANSMISSION  —  ONE NIGHT ONLY //",
   F("JetBrainsMono-Bold", 38), WHITE, tracking=3)

# =========================================================================
# 2. TITLE LOCKUP  (CREATIVE / [burst] SIGNAL / NIGHT)
# =========================================================================
# speed-line + halftone "night" energy field behind the hero word
burst_cx, burst_cy = WD / 2, 1000
speed_lines(burst_cx, burst_cy, 120, 1500, 96, (80, 380, WD - 80, 1640),
            color=(*INK, 24), wmin=2, wmax=9)

# big yellow starburst behind SIGNAL (sized to clear banner + bubbles)
bpts = starburst(burst_cx, burst_cy, 648, 504, 24, rot=0.05, jitter=0.045)
ink_poly(bpts, YELLOW, ink=10, misreg=(7, 7))
halftone((burst_cx - 648, burst_cy - 470, burst_cx + 648, burst_cy + 470), RED,
         spacing=26, radius=3.0, alpha=42,
         grad=(burst_cx, burst_cy, 120, 660, 0.1, 1.0))

# CREATIVE (top, condensed, black on yellow)
fc = F("BigShoulders-Bold", 176)
wc = measure("CREATIVE", fc, tracking=10)
tx(((WD - wc) / 2, 560), "CREATIVE", fc, INK, tracking=10)

# SIGNAL (hero — huge, outlined, shadowed)
fs = F("BigShoulders-Bold", 432)
ws = measure("SIGNAL", fs, tracking=6)
outline_text(((WD - ws) / 2, 728), "SIGNAL", fs, RED, ow=14, outline=INK,
             shadow=BLUE, sh_off=(20, 20), tracking=6)

# NIGHT (lower, blue bar behind)
fn = F("BigShoulders-Bold", 196)
wn = measure("NIGHT", fn, tracking=22)
nb_y = 1248
ink_poly([(WD/2 - wn/2 - 70, nb_y), (WD/2 + wn/2 + 70, nb_y - 14),
          (WD/2 + wn/2 + 70, nb_y + 196), (WD/2 - wn/2 - 70, nb_y + 210)], NAVY, ink=8)
halftone((WD/2 - wn/2 - 70, nb_y - 14, WD/2 + wn/2 + 70, nb_y + 206), WHITE,
         spacing=20, radius=2.0, alpha=34)
outline_text(((WD - wn) / 2, nb_y + 18), "NIGHT", fn, YELLOW, ow=7, outline=INK,
             shadow=None, tracking=22)

# =========================================================================
# 3. CONCEPT speech bubbles (4)  — controlled zigzag cascade
# =========================================================================
def bubble(cx, cy, rw, rh, text, font, fill, tailto, txtcol=INK, kind="oval"):
    # clean directional tail: two base points on the shape edge -> apex
    ang = math.atan2(tailto[1] - cy, tailto[0] - cx)
    da = 0.26
    e1 = (cx + rw * math.cos(ang - da), cy + rh * math.sin(ang - da))
    e2 = (cx + rw * math.cos(ang + da), cy + rh * math.sin(ang + da))
    dr.polygon([(s(e1[0]), s(e1[1])), (s(e2[0]), s(e2[1])), (s(tailto[0]), s(tailto[1]))], fill=INK)
    tcx, tcy = (e1[0]+e2[0]+tailto[0])/3, (e1[1]+e2[1]+tailto[1])/3
    ct = inset([e1, e2, tailto], 8)
    ct = [(x+4, y+4) for x, y in ct]
    dr.polygon([(s(x), s(y)) for x, y in ct], fill=fill)
    # body
    if kind == "burst":
        bp = starburst(cx, cy, rw*1.04, rw*0.78, 17, jitter=0.05, ry_scale=rh/rw)
        ink_poly(bp, fill, ink=8, misreg=(5, 5))
    else:
        dr.ellipse([s(cx-rw), s(cy-rh), s(cx+rw), s(cy+rh)], fill=INK)
        dr.ellipse([s(cx-rw+9)+s(4), s(cy-rh+9)+s(4), s(cx+rw-9)+s(4), s(cy+rh-9)+s(4)], fill=fill)
    w = measure(text, font, tracking=1)
    tx((cx - w/2, cy - font.size/SS*0.40), text, font, txtcol, tracking=1)

# four concept bubbles — controlled 2x2; bottom-right cell left for FREE! burst
bubble(610, 1728, 372, 140, "VISUAL EXPERIMENTS", F("Outfit-Bold", 58), WHITE,
       (470, 1880), txtcol=INK, kind="oval")
bubble(1838, 1712, 300, 150, "AI FRAGMENTS", F("Outfit-Bold", 60), YELLOW,
       (1980, 1556), txtcol=INK, kind="burst")
bubble(600, 2035, 320, 135, "STRANGE NOTES", F("Outfit-Bold", 56), BLUE,
       (470, 2188), txtcol=WHITE, kind="oval")
bubble(1300, 2035, 300, 135, "FUTURE IDEAS", F("Outfit-Bold", 58), RED,
       (1200, 2188), txtcol=WHITE, kind="oval")

# =========================================================================
# 4. INFO caption panels (date / time / venue)  — comic narration boxes
# =========================================================================
panel_y = 2250
ph = 460
# big black panel
dr.rectangle([s(CL), s(panel_y), s(CR), s(panel_y + ph)], fill=INK)
dr.rectangle([s(CL+14), s(panel_y+14), s(CR-14), s(panel_y+ph-14)], outline=YELLOW, width=int(3*SS))
halftone((CL, panel_y, CR, panel_y+ph), BLUE, spacing=26, radius=2.6, alpha=46)

# left column: DATE big
tx((CL+60, panel_y+44), "DATE", F("JetBrainsMono-Bold", 40), YELLOW, tracking=4)
tx((CL+56, panel_y+96), "2026.07.20", F("BigShoulders-Bold", 196), WHITE, tracking=2)
tx((CL+60, panel_y+328), "MONDAY EVENING", F("JetBrainsMono-Bold", 34), (214,214,210), tracking=3)

# divider
dr.line([s(CL+1120), s(panel_y+48), s(CL+1120), s(panel_y+ph-48)], fill=YELLOW, width=int(3*SS))

# right column: TIME + VENUE
tx((CL+1180, panel_y+44), "TIME", F("JetBrainsMono-Bold", 40), YELLOW, tracking=4)
tx((CL+1176, panel_y+92), "19:00", F("BigShoulders-Bold", 150), WHITE)
tx((CL+1176, panel_y+234), "–21:00", F("BigShoulders-Bold", 92), RED)
tx((CL+1180, panel_y+344), "VENUE", F("JetBrainsMono-Bold", 36), YELLOW, tracking=3)
tx((CL+1180, panel_y+392), "TOYAMA CREATIVE ROOM", F("Outfit-Bold", 50), WHITE, tracking=1)

# FREE! starburst badge bursting out of the panel's top-right corner
fcx, fcy = 1992, 2150
fp = starburst(fcx, fcy, 218, 142, 15, rot=0.16, jitter=0.04)
ink_poly(fp, RED, ink=9, misreg=(6, 6))
fp2 = starburst(fcx, fcy, 168, 110, 15, rot=0.16)
dr.polygon([(s(x), s(y)) for x, y in fp2], fill=YELLOW)
tx((fcx - measure("ENTRY", F("Outfit-Bold", 38), 2)/2, fcy-104), "ENTRY",
   F("Outfit-Bold", 38), INK, tracking=2)
tx((fcx - measure("FREE!", F("BigShoulders-Bold", 132))/2, fcy-58), "FREE!",
   F("BigShoulders-Bold", 132), INK)

# =========================================================================
# 5. CTA ribbon banner (bring one idea)
# =========================================================================
ry = 2800
rh = 150
# ribbon body + folded ends
dr.polygon([(s(CL-30), s(ry)), (s(CR+30), s(ry)), (s(CR+30), s(ry+rh)), (s(CL-30), s(ry+rh))], fill=INK)
ink_poly([(CL-30, ry+8), (CR+30, ry+8), (CR+30, ry+rh-8), (CL-30, ry+rh-8)], RED, ink=0, misreg=(0,0))
# folded triangles
dr.polygon([(s(CL-30), s(ry-32)), (s(CL+90), s(ry+8)), (s(CL-30), s(ry+8))], fill=NAVY)
dr.polygon([(s(CR+30), s(ry-32)), (s(CR-90), s(ry+8)), (s(CR+30), s(ry+8))], fill=NAVY)
cta = "BRING ONE IDEA, NOTE, OR IMAGE FRAGMENT"
fct = F("BigShoulders-Bold", 92)
tx(((WD - measure(cta, fct, tracking=3))/2, ry+22), cta, fct, WHITE, tracking=3)

# =========================================================================
# 6. footer micro + fake barcode
# =========================================================================
tx((CL, 3210), "CREATIVE SIGNAL NIGHT", F("BigShoulders-Bold", 50), INK, tracking=3)
tx((CL, 3268), "A GATHERING FOR VISUAL EXPERIMENTS & FUTURE FRAGMENTS",
   F("JetBrainsMono-Bold", 26), INK, tracking=1)
# barcode
bx, byc = CR - 340, 3208
dr.rectangle([s(bx-14), s(byc-8), s(CR+4), s(byc+96)], fill=WHITE)
xx = bx
random.seed(5)
while xx < CR - 20:
    w = random.choice([2, 2, 4, 6])
    dr.rectangle([s(xx), s(byc), s(xx+w), s(byc+78)], fill=INK)
    xx += w + random.choice([3, 4, 6])
tx((bx-14, byc+82), "0 71820 19002 1", F("JetBrainsMono-Bold", 22), INK, tracking=1)

# =========================================================================
# 7. print finishing — misregistration grain + paper texture
# =========================================================================
arr = np.asarray(img, np.float32)
arr += np.random.normal(0, 3.0, (H, W, 1)).astype(np.float32)        # paper grain
# faint cyan/red channel jitter for offset feel
arr[..., 2] = np.clip(arr[..., 2] + 2.5, 0, 255)
img = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"), "RGB")

# subtle vignette
a2 = np.asarray(img, np.float32)
yy, xx = np.mgrid[0:H, 0:W]
d = np.sqrt(((xx - W/2)/(W/2))**2 + ((yy - H/2)/(H/2))**2)
a2 *= (1 - np.clip((d - 0.7)*0.09, 0, 0.06))[..., None]
img = Image.fromarray(np.clip(a2, 0, 255).astype("uint8"), "RGB")

img = img.resize((WD, HD), Image.LANCZOS)
out = "/Users/metcharoba/CreativeVault/70_design_experiments/creative_signal_night/creative_signal_night.png"
img.save(out, "PNG")
img.save(out.replace(".png", ".pdf"), "PDF", resolution=300)
print("saved", out, img.size)
