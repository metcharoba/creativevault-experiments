#!/usr/bin/env python3
"""RFM screenshot helper — auto-default for workflow_v0_2 GATE 2.

Captures a real rendered screenshot of a reference URL with headless Chrome,
then validates it so we can tell a real render from a blank/consent-wall/blocked
page. If it reports SUSPECT/FAIL, capture the page manually instead and drop the
PNG into the build's screenshots/refs/ folder (manual fallback).

Usage:
  python3 tools/rfm_shot.py <url> <out.png> [--width 1440] [--height 2400]
                                            [--scale 2] [--timeout 60]

Boundaries: CreativeVault only. Read-only web fetch (no posting/sending).
No secrets, no login, no MedicalVault / LocalOnlyProjects.
"""
import argparse
import os
import subprocess
import sys

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def main() -> int:
    ap = argparse.ArgumentParser(description="RFM reference screenshot (auto-default).")
    ap.add_argument("url")
    ap.add_argument("out", help="output PNG path, e.g. screenshots/refs/lead_firstview.png")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=2400, help="tall viewport grabs first-view + below the fold")
    ap.add_argument("--scale", type=float, default=2.0, help="device scale factor (2 = retina-ish)")
    ap.add_argument("--timeout", type=int, default=60)
    a = ap.parse_args()

    if not os.path.exists(CHROME):
        print(f"FAIL: Chrome not found at {CHROME} — capture manually.")
        return 2

    out_dir = os.path.dirname(os.path.abspath(a.out))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    cmd = [
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--no-first-run", "--no-default-browser-check",
        f"--force-device-scale-factor={a.scale}",
        f"--window-size={a.width},{a.height}",
        "--virtual-time-budget=8000",  # let JS render briefly before capture
        f"--screenshot={a.out}", a.url,
    ]
    try:
        subprocess.run(cmd, timeout=a.timeout,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        print("FAIL: Chrome timed out — capture manually.")
        return 2

    if not os.path.exists(a.out):
        print("FAIL: no file produced — capture manually.")
        return 2

    # Validate: a real page has pixel variety; blank/consent walls are near-uniform.
    try:
        import numpy as np
        from PIL import Image
        im = Image.open(a.out).convert("RGB")
        arr = np.asarray(im)
        std = float(arr.std())
        w, h = im.size
        print(f"file: {a.out}  size: {w}x{h}  bytes: {os.path.getsize(a.out)}  pixel_std: {std:.1f}")
        if std < 8.0:
            print("SUSPECT: image is near-uniform (likely blank / cookie wall / blocked). "
                  "Verify it, or capture manually and replace the file.")
            return 1
        print("OK: real-looking screenshot captured. (Still eyeball it before observing.)")
        return 0
    except Exception as e:  # validation is best-effort; the file still exists
        print(f"WARN: could not validate ({e}); file exists — eyeball it.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
