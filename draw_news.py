#!/usr/bin/env python3
"""Draw the front page for Monday 23 November 2026.

One 1024x1024 PNG that sums up the day's world news: the COP31 collapse,
Houthi strikes on Saudi Arabia, the FBI NCIC database hack, the Shenzhen
trilateral declaration, and a dozen more stories, plus a numbers strip.
Deterministic: same input, same bytes, every run.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (25, 25, 25)
RED = (179, 38, 30)
BLUE = (29, 78, 216)
TEAL = (15, 118, 110)
GOLD = (180, 83, 9)
GREY = (110, 105, 95)
LIGHT = (233, 226, 210)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36  # margin

    # ---- masthead ----
    d.text((mx, 26), "THE DAY IN ONE PICTURE", font=SERIF_B(44), fill=INK)
    d.text((W - mx - d.textlength("make.fun", font=SANS_B(22)), 40),
           "make.fun", font=SANS_B(22), fill=RED)
    d.line([(mx, 92), (W - mx, 92)], fill=INK, width=3)
    d.line([(mx, 97), (W - mx, 97)], fill=INK, width=1)
    d.text((mx, 106), "MONDAY, 23 NOVEMBER 2026  ·  WORLD NEWS IN ONE IMAGE",
           font=SANS_B(19), fill=INK)

    # ---- lead story ----
    y = 148
    d.rectangle([mx, y, mx + 330, y + 30], fill=RED)
    d.text((mx + 12, y + 4), "CLIMATE SUMMIT FAILS", font=SANS_B(19), fill=(255, 255, 255))
    d.text((W - mx - d.textlength("0 DEALS", font=SERIF_B(40)), y - 6),
           "0 DEALS", font=SERIF_B(40), fill=RED)
    y += 44
    d.text((mx, y), "COP31 COLLAPSES", font=SERIF_B(76), fill=INK)
    y += 92
    lead = ("First failed climate summit since Copenhagen. No deal as "
            "fossil-fuel language is dropped from the text; the EU walks "
            "away and the UN chief calls it deeply disappointing.")
    for line in wrap(d, lead, SERIF(24), W - 2 * mx):
        d.text((mx, y), line, font=SERIF(24), fill=INK)
        y += 32
    y += 10
    d.line([(mx, y), (W - mx, y)], fill=GREY, width=1)

    # ---- second row: two stories ----
    y += 16
    col_w = (W - 2 * mx - 24) // 2
    stories = [
        ("HOUTHIS STRIKE SAUDI", RED,
         "Missiles and drones hit a Saudi oil refinery and radar; at least "
         "6 injured. 25 tankers hit in and around the Strait of Hormuz in "
         "seven days as Gulf oil flow drops sharply."),
        ("FBI DATABASE HACK", BLUE,
         "Trump calls the NCIC breach \u201cnot good\u201d \u2014 then hints it "
         "may expose the \u201cRussia hoax\u201d. The second FBI hack in "
         "months; scope still unclear."),
    ]
    top = y
    for i, (head, color, body) in enumerate(stories):
        x = mx + i * (col_w + 24)
        d.text((x, y), head, font=SANS_B(22), fill=color)
        by = y + 32
        for line in wrap(d, body, SANS(19), col_w):
            d.text((x, by), line, font=SANS(19), fill=INK)
            by += 26
    y = top + 32 + 4 * 26 + 8
    d.line([(mx, y), (W - mx, y)], fill=GREY, width=1)

    # ---- briefs: two columns x six ----
    y += 14
    briefs = [
        ("SHENZHEN", RED, "Trump, Xi and Putin sign a four-point declaration."),
        ("MERCURY", TEAL, "BepiColombo enters Mercury orbit after 8 years."),
        ("LAS VEGAS", GOLD, "Verstappen wins the Grand Prix; 352 overtakes."),
        ("FINLAND", BLUE, "Russian ship ablaze; Kyiv drone strike, 14 missing."),
        ("ISRAEL", RED, "Netanyahu-Eisenkot unity talks end with no deal."),
        ("SEOUL", TEAL, "Education minister quits over AI cheating scandal."),
        ("SINALOA", GOLD, "Mexico captures FBI most-wanted El Chapo Isidro."),
        ("KEPCO", BLUE, "Data breach exposes records of 1.52 million people."),
        ("UAP", RED, "Pentagon releases 43 more declassified UAP files."),
        ("GENEVA", TEAL, "UN talks on lethal AI go on; no binding rules yet."),
        ("MARKETS", GOLD, "Gold falls 8.5% in a week; S&P 500 enters correction."),
        ("JAKARTA", BLUE, "Factory fire: seven dead, 50 missing after the blaze."),
    ]
    row_h = 52
    for i, (tag, color, text) in enumerate(briefs):
        col = i % 2
        row = i // 2
        x = mx + col * (col_w + 24)
        by = y + row * row_h
        d.rectangle([x, by + 3, x + 10, by + 13], fill=color)
        d.text((x + 18, by), tag, font=SANS_B(16), fill=color)
        body_lines = wrap(d, text, SANS(16), col_w - 18)
        ly = by + 22
        for line in body_lines[:1]:
            d.text((x + 18, ly), line, font=SANS(16), fill=INK)
    y = y + 6 * row_h + 6
    d.line([(mx, y), (W - mx, y)], fill=INK, width=2)

    # ---- numbers strip ----
    y += 12
    nums = [("0", "COP31 deals"), ("25", "tankers hit"),
            ("1.52M", "records exposed"), ("352", "overtakes"),
            ("43", "UAP files"), ("8 yrs", "to Mercury")]
    cell = (W - 2 * mx) // len(nums)
    for i, (num, label) in enumerate(nums):
        x = mx + i * cell
        d.text((x, y), num, font=SERIF_B(30), fill=RED)
        d.text((x, y + 40), label, font=SANS(15), fill=GREY)
    y += 72
    d.line([(mx, y), (W - mx, y)], fill=INK, width=2)

    # ---- footer ----
    y += 10
    d.text((mx, y), "Drawn from Reuters · AP · AFP · BBC · The Hindu",
           font=SANS(15), fill=GREY)
    d.text((W - mx - d.textlength("23 NOV 2026", font=SANS_B(15)), y),
           "23 NOV 2026", font=SANS_B(15), fill=GREY)

    img.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
