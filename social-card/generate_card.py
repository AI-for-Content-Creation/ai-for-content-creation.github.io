#!/usr/bin/env python3
"""
Generate the social / Open Graph "link preview" card for the AI for Content
Creation workshop (the image that expands when the site URL is posted to
social media, Slack, etc.).

The card is a CVPR promo styled to match the website (white background,
Quicksand font, maroon #a31f33 accent). It shows the workshop name, date/time,
room, topics, a strip of graphics from featured papers, and a row of the
invited speakers with their photos.

USAGE
-----
    python social-card/generate_card.py            # uses YEAR below (2026)
    python social-card/generate_card.py 2027        # generate for another year

INPUTS (per year)
-----------------
  * _data/speakers_<YEAR>.csv          speaker name + affiliation (+ talk time
                                       for ordering). Already used by the site.
  * social-card/<YEAR>/speakers/*.jpg  one headshot per speaker, filename =
                                       speaker LAST NAME lower-cased
                                       (e.g. "Saining Xie" -> xie.png).
  * social-card/<YEAR>/papers/*.jpg    teaser graphics from papers on display.
                                       Shown in the strip in filename order;
                                       prefix with 01_, 02_, ... to order them.
  * social-card/fonts/Quicksand-VF.ttf bundled font (matches the website).
  * the EVENT config block below       date / time / room / topics for the year.

OUTPUT
------
  * images/sm-card.jpg                 1200x630, referenced by the og:image /
                                       twitter:image meta tags in index.html.
  * social-card/<YEAR>/sm-card-<YEAR>.jpg   archived copy for that year.

Only dependency is Pillow:  pip install pillow
See README.md for how to make next year's card.
"""

import csv
import os
import sys

from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None  # some source images are large

# --------------------------------------------------------------------------
# Per-year event configuration -- EDIT THIS for a new year.
# --------------------------------------------------------------------------
YEAR = int(sys.argv[1]) if len(sys.argv) > 1 else 2026

EVENT = {
    2026: {
        "date": "3 June 2026",
        "time": "8:25 AM MDT",
        "room": "Room 610/612, Colorado Convention Center, Denver",
        "topics": [
            "Generative models",
            "Image / Video / 3D editing",
            "Domain transfer",
            "Multi-modal creation",
        ],
        # Optional: bias the square face-crop vertically per speaker.
        # 0.0 = top, 0.5 = centre, 1.0 = bottom. Default 0.42.
        "focus": {"theobalt": 0.16},
    },
}

# --------------------------------------------------------------------------
# Theme -- matches the website (css/theme_1610153848925.css).
# --------------------------------------------------------------------------
W, H = 1200, 630
SS = 2                          # supersample, then downscale for crisp output
BG = (255, 255, 255)
INK = (33, 37, 41)             # #212529 body text
GRAY = (73, 80, 87)            # #495057
MUTED = (108, 117, 125)        # #6c757d
MAROON = (163, 31, 51)         # #a31f33 site primary
BORDER = (222, 226, 230)       # #dee2e6

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_PATH = os.path.join(ROOT, "social-card", "fonts", "Quicksand-VF.ttf")


def qfont(size, weight=700):
    """Quicksand at a given weight (300-700). Falls back to default font."""
    try:
        f = ImageFont.truetype(FONT_PATH, int(size * SS))
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
        return f
    except Exception:
        return ImageFont.load_default()


def px(v):
    return int(round(v * SS))


def last_name_slug(name):
    return name.strip().split()[-1].lower()


def short_affiliation(aff):
    repl = {
        "University of Chicago": "U Chicago",
        "Johns Hopkins University": "Johns Hopkins",
        "Max-Planck-Institute for Informatics": "MPI Informatics",
        "Max Planck Institute for Informatics": "MPI Informatics",
        "New York University": "NYU",
        "New York University, AMI Labs": "NYU / AMI Labs",
        "Carnegie Mellon University": "CMU",
        "University of Pennsylvania": "UPenn",
    }
    return repl.get(aff.strip(), aff.strip())


def load_speakers(year):
    path = os.path.join(ROOT, "_data", f"speakers_{year}.csv")
    photo_dir = os.path.join(ROOT, "social-card", str(year), "speakers")
    speakers = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            name = (row.get("name") or "").strip()
            if not name:
                continue
            slug = last_name_slug(name)
            photo = next((os.path.join(photo_dir, f"{slug}.{e}")
                          for e in ("jpg", "jpeg", "png", "webp")
                          if os.path.exists(os.path.join(photo_dir, f"{slug}.{e}"))), None)
            if photo is None:
                print(f"  WARNING: no headshot for {name} (expected {slug}.jpg)")
                continue
            speakers.append({
                "name": name,
                "affiliation": short_affiliation(row.get("affiliation") or ""),
                "time": (row.get("time") or "").strip(),
                "slug": slug,
                "photo": photo,
            })
    speakers.sort(key=lambda s: s["time"] or "99:99")
    return speakers


def load_paper_graphics(year, limit=4):
    d = os.path.join(ROOT, "social-card", str(year), "papers")
    if not os.path.isdir(d):
        return []
    files = sorted(f for f in os.listdir(d)
                   if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")))
    return [os.path.join(d, f) for f in files][:limit]


def cover(im, tw, th, focus_y=0.5):
    im = im.convert("RGB")
    w, h = im.size
    s = max(tw / w, th / h)
    im = im.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)
    x = (im.size[0] - tw) // 2
    y = int((im.size[1] - th) * focus_y)
    y = max(0, min(im.size[1] - th, y))
    return im.crop((x, y, x + tw, y + th))


def rounded_mask(size, radius):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1),
                                        radius=radius, fill=255)
    return m


def circle_headshot(path, diameter, focus_y=0.42):
    d = px(diameter)
    im = cover(Image.open(path), d, d, focus_y)
    mask = Image.new("L", (d, d), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, d - 1, d - 1), fill=255)
    out = Image.new("RGBA", (d, d), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out


def fit_font(draw, text, weight, max_size, max_width):
    size = max_size
    while size > 8:
        f = qfont(size, weight)
        if draw.textlength(text, font=f) <= px(max_width):
            return f
        size -= 1
    return qfont(8, weight)


def centered(draw, cx, y, text, f, fill):
    w = draw.textlength(text, font=f)
    draw.text((px(cx) - w / 2, y), text, font=f, fill=fill)


def main():
    cfg = EVENT.get(YEAR)
    if cfg is None:
        sys.exit(f"No EVENT config for {YEAR}. Add an entry to the EVENT dict.")
    speakers = load_speakers(YEAR)
    if not speakers:
        sys.exit("No speakers with headshots found.")
    papers = load_paper_graphics(YEAR)

    card = Image.new("RGB", (px(W), px(H)), BG)
    d = ImageDraw.Draw(card)

    # top accent rule (site primary)
    d.rectangle((0, 0, px(W), px(6)), fill=MAROON)

    # ---- header -------------------------------------------------------
    centered(d, W / 2, px(34), f"CVPR {YEAR}  ·  WORKSHOP", qfont(19, 700), MAROON)
    tf = fit_font(d, "AI for Content Creation", 700, 58, W - 120)
    centered(d, W / 2, px(58), "AI for Content Creation", tf, INK)
    centered(d, W / 2, px(126), f"{cfg['date']}   ·   {cfg['time']}", qfont(22, 600), GRAY)
    centered(d, W / 2, px(156), cfg["room"], qfont(18, 500), MUTED)
    topics = "      ".join(cfg["topics"])
    tpf = fit_font(d, topics, 600, 18, W - 90)
    centered(d, W / 2, px(188), topics, tpf, MAROON)

    # ---- featured paper graphics strip --------------------------------
    strip_y, strip_h = 220, 150
    if papers:
        margin, gap = 40, 14
        n = len(papers)
        cw = (W - 2 * margin - gap * (n - 1)) / n
        for i, p in enumerate(papers):
            x = margin + i * (cw + gap)
            tile = cover(Image.open(p), px(cw), px(strip_h))
            mask = rounded_mask(tile.size, px(12))
            card.paste(tile, (px(x), px(strip_y)), mask)
            # thin border
            d.rounded_rectangle(
                (px(x), px(strip_y), px(x + cw) - 1, px(strip_y + strip_h) - 1),
                radius=px(12), outline=BORDER, width=SS)

    # ---- speakers -----------------------------------------------------
    centered(d, W / 2, px(390), "INVITED SPEAKERS", qfont(16, 700), MAROON)
    n = len(speakers)
    diameter = 116
    col_w = W / n
    circle_top = 414
    name_y = circle_top + diameter + 12
    aff_y = name_y + 26
    for i, sp in enumerate(speakers):
        cx = col_w * (i + 0.5)
        focus_y = cfg.get("focus", {}).get(sp["slug"], 0.42)
        head = circle_headshot(sp["photo"], diameter, focus_y)
        card.paste(head, (px(cx) - head.width // 2, px(circle_top)), head)
        r = px(diameter) // 2
        d.ellipse((px(cx) - r, px(circle_top), px(cx) + r, px(circle_top) + px(diameter)),
                  outline=MAROON, width=SS * 2)
        nf = fit_font(d, sp["name"], 700, 21, col_w - 14)
        centered(d, cx, name_y * SS, sp["name"], nf, INK)
        if sp["affiliation"]:
            af = fit_font(d, sp["affiliation"], 500, 16, col_w - 10)
            centered(d, cx, aff_y * SS, sp["affiliation"], af, MUTED)

    # ---- downscale + save --------------------------------------------
    card = card.resize((W, H), Image.LANCZOS)
    main_out = os.path.join(ROOT, "images", "sm-card.jpg")
    card.save(main_out, quality=90, optimize=True)
    archive = os.path.join(ROOT, "social-card", str(YEAR), f"sm-card-{YEAR}.jpg")
    card.save(archive, quality=90, optimize=True)
    print(f"Saved {main_out} ({W}x{H}, {os.path.getsize(main_out)//1024} KB) and {archive}")
    print(f"Papers featured: {len(papers)} | Speakers: {', '.join(s['name'] for s in speakers)}")


if __name__ == "__main__":
    main()
