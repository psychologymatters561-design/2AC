"""
Render the scroll-scrubbed hero sequence and the still photography for
experience.html.

The hero is a real push-in: every frame is a progressively tighter crop of one
high-resolution rooftop photograph, so the sequence never upscales and stays
sharp at the tightest framing. Travelling along the sequence also travels along
a colour grade, from the amber of a 45 degree rooftop to the steel blue of a
room held at 22. That is the same journey the page's temperature HUD reports,
so the footage and the instrument are reading off one number.

Sources are licensed Adobe Stock originals. They are 4-7 MB each and live
outside the repository; only the derived frames are committed. Point SRC at a
directory holding rooftop/gauge/repair/install/room .jpg to re-render.
"""

import os
import sys
from PIL import Image, ImageEnhance, ImageFilter, ImageChops

SRC = sys.argv[1] if len(sys.argv) > 1 else "src_photos"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "media")

FRAMES = 28
FW, FH = 1200, 675
ZOOM_END = 0.60          # tightest crop, as a fraction of the widest 16:9 window
QUALITY = 52


def smootherstep(x):
    """Ease that leaves and arrives with zero velocity, so the push settles."""
    return x * x * x * (x * (x * 6 - 15) + 10)


def lerp(a, b, t):
    return a + (b - a) * t


def grade_lut(t):
    """
    Per-channel curves blended between a hot and a cold look.

    Hot crushes blue in the shadows and lifts red through the midtones, which
    is what heat haze actually does to a photograph. Cold lifts blue and pulls
    red back, and slightly lifts the black point so the cool end reads as calm
    rather than merely darker.
    """
    lut = []
    for ch in range(3):
        for i in range(256):
            v = i / 255.0
            if ch == 0:                                    # red
                hot = min(1.0, v ** 0.90 * 1.06 + 0.015)
                cold = v ** 1.10 * 0.90
            elif ch == 1:                                  # green
                hot = min(1.0, v ** 0.96 * 1.02)
                cold = v ** 1.02 * 0.95 + 0.01
            else:                                          # blue
                hot = max(0.0, v ** 1.16 * 0.92 - 0.01)
                cold = min(1.0, v ** 0.86 * 1.06 + 0.04)
            lut.append(int(max(0, min(255, round(lerp(hot, cold, t) * 255)))))
    return lut


def vignette(size, strength):
    """
    Built small and scaled up: a vignette is smooth, so the upscale is
    invisible and it costs a fraction of a per-pixel loop at full size.
    """
    sw, sh = 160, 90
    m = Image.new("L", (sw, sh))
    px = m.load()
    cx, cy = (sw - 1) / 2.0, (sh - 1) / 2.0
    for y in range(sh):
        for x in range(sw):
            dx = (x - cx) / cx
            dy = (y - cy) / cy
            d = min(1.0, (dx * dx + dy * dy) ** 0.5 / 1.32)
            px[x, y] = int(255 * (1.0 - strength * d ** 2.1))
    return m.resize(size, Image.BICUBIC)


def glare(im, amount):
    """Blurred bright-pass screened back over the frame — rooftop sun bloom."""
    if amount <= 0.001:
        return im
    bright = im.point(lambda v: max(0, (v - 168)) * 3)
    bright = bright.filter(ImageFilter.GaussianBlur(im.width / 26.0))
    return Image.blend(im, ImageChops.screen(im, bright), amount)


def render_sequence(src):
    base = Image.open(src).convert("RGB")
    W, H = base.size
    win_w = min(W, int(H * 16 / 9))
    win_h = int(win_w * 9 / 16)

    # Start centred, finish drawn left and low, onto the condenser bank.
    x0, y0 = W / 2.0, H / 2.0
    x1, y1 = W * 0.40, H * 0.53

    vig_hot = vignette((FW, FH), 0.50)
    vig_cold = vignette((FW, FH), 0.26)

    for i in range(FRAMES):
        p = i / (FRAMES - 1.0)
        e = smootherstep(p)

        scale = lerp(1.0, ZOOM_END, e)
        cw, ch = win_w * scale, win_h * scale
        cx, cy = lerp(x0, x1, e), lerp(y0, y1, e)

        left = max(0.0, min(W - cw, cx - cw / 2))
        top = max(0.0, min(H - ch, cy - ch / 2))
        f = base.resize((FW, FH), Image.LANCZOS,
                        box=(left, top, left + cw, top + ch))

        f = f.point(grade_lut(e))
        f = ImageEnhance.Brightness(f).enhance(lerp(0.94, 1.0, e))
        f = ImageEnhance.Contrast(f).enhance(lerp(1.20, 1.04, e))
        f = ImageEnhance.Color(f).enhance(lerp(0.92, 1.05, e))
        f = glare(f, lerp(0.18, 0.05, e))

        vig = Image.blend(vig_hot, vig_cold, e)
        f = Image.composite(f, Image.new("RGB", (FW, FH), (6, 10, 18)), vig)

        f.save(os.path.join(OUT, "roof-%02d.webp" % i),
               "WEBP", quality=QUALITY, method=6)

    return FRAMES


def render_still(src, name, width, t, ratio=None, focus=0.5):
    """One graded still, sat at position t along the same hot-to-cold journey."""
    im = Image.open(src).convert("RGB")
    W, H = im.size
    if ratio:
        want_h = int(W / ratio)
        if want_h <= H:
            top = max(0, min(H - want_h, int(H * focus - want_h / 2)))
            im = im.crop((0, top, W, top + want_h))
        else:
            want_w = int(H * ratio)
            left = max(0, min(W - want_w, int(W * focus - want_w / 2)))
            im = im.crop((left, 0, left + want_w, H))
    h = int(im.height * width / im.width)
    im = im.resize((width, h), Image.LANCZOS)
    im = im.point(grade_lut(t))
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(0.97)
    im = Image.composite(im, Image.new("RGB", im.size, (8, 12, 20)),
                         vignette(im.size, 0.22))
    im.save(os.path.join(OUT, name), "WEBP", quality=72, method=6)
    return im.size


def main():
    os.makedirs(OUT, exist_ok=True)
    n = render_sequence(os.path.join(SRC, "rooftop.jpg"))
    print("sequence: %d frames" % n)
    for src, name, w, t, ratio, focus in [
        ("gauge.jpg",   "diagnose.webp", 1280, 0.32, 16 / 10, 0.50),
        ("repair.jpg",  "repair.webp",   1120, 0.44, 4 / 3,   0.50),
        ("install.jpg", "install.webp",  1120, 0.40, 4 / 3,   0.50),
        ("room.jpg",    "arrive.webp",   1600, 0.96, 16 / 9,  0.50),
    ]:
        print(name, render_still(os.path.join(SRC, src), name, w, t, ratio, focus))


if __name__ == "__main__":
    main()
