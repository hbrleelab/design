"""Generate the HBRLRG conference poster templates (PPTX).

    python3 tools/build_poster.py [outdir] [--size a0|kcs|all] [--style standard|panel|band|all]
                                  [--fonts DIR]

Writes outdir/hbrlrg-poster-<size>-<style>.pptx — by default all six.

The layout comes from the four student posters in references/posters/ (see the
analysis in its README) put through the design system:

- Portrait, two equal columns. Three of the four references use exactly that.
- The header is 12–16 % of the page height and holds the title, the authors and
  affiliation, and a logo on each side: the UNIST emblem on the left, next to
  the affiliation it stands for, and a slot for the conference or project logo
  on the right.
- Type follows the most orderly reference, 03 (KCS): 80 / 52 / 40 / 28 / 24 pt
  for title / section / subsection / body / caption. Body never goes below
  24 pt and captions never below 20 pt; the A0 workshop poster (02) set its
  body at 14–18 pt, which cannot be read from a step back.
- Columns are 24 mm apart. Reference 03 had 5 mm and the columns ran together.

Three styles share that grid:

  standard  white page, the teal-capped rule under the header (03 type)
  panel     navy page with white section panels (01 · 02 type)
  band      navy header and footer bands framing a white body (04 type)

Two sizes: A0 (841 × 1189 mm) and 900 × 1200 mm, the size KCS asks for.

Each column is a stack of sections and each section a stack of blocks. One
figure per column is "flex" and takes the height the text leaves, so both
columns end on the same line. Text heights are measured, not guessed: every
block is word-wrapped against Archivo's real advance widths, which needs the
font files — the same ones the release workflow fetches into .fonts/.
"""
import argparse
from pathlib import Path

from fontTools.ttLib import TTFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Mm, Pt

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

# --- design tokens (design-system/HBRLRG-design-system.md §1) --------------
NAVY = RGBColor(0x14, 0x24, 0x3F)
TEAL = RGBColor(0x0E, 0xA7, 0x9A)
INK = RGBColor(0x2B, 0x2F, 0x36)
MUTED = RGBColor(0x6B, 0x72, 0x80)
FAINT = RGBColor(0x9A, 0xA1, 0xAB)
SURFACE = RGBColor(0xF6, 0xF7, 0xF9)
BORDER = RGBColor(0xE4, 0xE7, 0xEC)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ON_NAVY = RGBColor(0x93, 0xA2, 0xBC)
NAVY_RULE = RGBColor(0x2C, 0x40, 0x66)
LATIN, HANGUL = "Archivo", "Pretendard"

PT_MM = 25.4 / 72
# Office sets single spacing at 1.2 em for Archivo, and puts the extra of a
# proportional spacing above each line — the first one included. Measured on
# the LibreOffice export, which is what the sample PDFs are.
SINGLE = 1.2
X_HEIGHT = 0.526
LOGO_INK = 307 / 708     # the HBRLRG logo PNG is padded; this is its ink height

# --- sizes and styles ------------------------------------------------------
SIZES = {
    "a0": dict(name="A0", w=841, h=1189, margin=30, gutter=24, emblem=72),
    "kcs": dict(name="900 × 1200 mm (KCS)", w=900, h=1200, margin=30, gutter=24, emblem=72),
}
STYLES = {
    "standard": "white page, teal-capped rule under the header",
    "panel": "navy page, white section panels",
    "band": "navy header and footer bands",
}
TYPE = dict(title=80, section=52, sub=40, authors=40, affil=24, body=28,
            caption=24, small=20, eyebrow=24)
HEADER_SHARE = (0.12, 0.16)


# --- text measurement ------------------------------------------------------
class Measure:
    """Greedy word wrap on Archivo's advance widths. Hangul falls back to a
    flat 0.95 em (Pretendard's syllables are close to square); the wrap width
    keeps 3 % in reserve for kerning and for PowerPoint wrapping a hair
    earlier than LibreOffice."""

    def __init__(self, font_dir):
        self.faces = {}
        for bold, name in ((False, "Archivo-Regular.ttf"), (True, "Archivo-Bold.ttf")):
            f = TTFont(Path(font_dir) / name)
            self.faces[bold] = (f.getBestCmap(), f["hmtx"], f["head"].unitsPerEm)

    def width(self, s, size, bold=False):
        cmap, hmtx, upm = self.faces[bold]
        em = sum(hmtx[cmap[ord(c)]][0] / upm if ord(c) in cmap else 0.95 for c in s)
        return em * size * PT_MM

    def lines(self, s, w, size, bold=False):
        limit = w * 0.97
        n, cur = 1, ""
        for word in s.split(" "):
            trial = f"{cur} {word}" if cur else word
            if cur and self.width(trial, size, bold) > limit:
                n, cur = n + 1, word
            else:
                cur = trial
        return n


def find_fonts(explicit):
    """--fonts, then .fonts/ (where the release workflow puts them), then the
    usual per-user and system font folders."""
    candidates = [Path(explicit)] if explicit else [
        ROOT / ".fonts", Path.home() / ".local/share/fonts",
        Path.home() / "Library/Fonts", Path("/usr/share/fonts"),
    ]
    for c in candidates:
        hits = sorted(c.rglob("Archivo-Regular.ttf")) if c.is_dir() else []
        if hits and (hits[0].parent / "Archivo-Bold.ttf").exists():
            return hits[0].parent
    raise SystemExit(
        "Archivo-Regular.ttf / Archivo-Bold.ttf 를 찾지 못했습니다. --fonts 로 폴더를 "
        "지정하거나, release.yml 의 Fetch fonts 단계처럼 .fonts/ 에 받아 두세요.")


# --- low-level helpers -----------------------------------------------------
def line_pitch(size, spacing):
    return size * SINGLE * spacing * PT_MM


def first_baseline(size, spacing):
    """Distance from a text box's top to its first baseline, in mm."""
    return (SINGLE * spacing - 0.2) * size * PT_MM


def rect(slide, x, y, w, h, fill, line=None, name=None):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Mm(x), Mm(y), Mm(w), Mm(h))
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()      # never read s.line.color: it adds <a:ln>
    else:
        s.line.fill.solid()
        s.line.fill.fore_color.rgb = line
        s.line.width = Pt(1.5)
    s.shadow.inherit = False
    # The theme style reference would still give LibreOffice a drop shadow
    # (it ignores the empty effectLst); every property it supplies is set
    # explicitly above, so drop it.
    style = s._element.find(qn("p:style"))
    if style is not None:
        s._element.remove(style)
    if name:
        s.name = name
    return s


def _run_font(run, size, colour, bold=False, tracking=None, sup=False):
    run.font.name = LATIN
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = colour
    rPr = run._r.get_or_add_rPr()
    rPr.append(rPr.makeelement(qn("a:ea"), {"typeface": HANGUL}))
    if tracking:
        rPr.set("spc", str(int(tracking * size * 100)))
    if sup:
        rPr.set("baseline", "30000")


def text(slide, x, y, w, h, runs, size, colour, *, bold=False, align=PP_ALIGN.LEFT,
         spacing=1.25, tracking=None, anchor=MSO_ANCHOR.TOP, name=None):
    """runs: str, or a list of paragraphs, each a str or a list of
    (text, {overrides}) pieces."""
    box = slide.shapes.add_textbox(Mm(x), Mm(y), Mm(w), Mm(h))
    if name:
        box.name = name
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    paras = [runs] if isinstance(runs, str) else runs
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spacing
        pieces = [(para, {})] if isinstance(para, str) else para
        for t, o in pieces:
            r = p.add_run()
            r.text = t
            _run_font(r, o.get("size", size), o.get("colour", colour),
                      o.get("bold", bold), o.get("tracking", tracking), o.get("sup", False))
    return box


def picture(slide, path, x, y, h=None, w=None, name=None):
    """Set one dimension; the other follows the file."""
    from PIL import Image
    with Image.open(path) as im:
        ratio = im.width / im.height
    if h is not None:
        w = h * ratio
    else:
        h = w / ratio
    pic = slide.shapes.add_picture(str(path), Mm(x), Mm(y), Mm(w), Mm(h))
    if name:
        pic.name = name
    return w, h


# --- placeholder content ---------------------------------------------------
# Written as instructions, so a student who fills the boxes in order has
# followed the advice without reading the README.
EYEBROW = "CONFERENCE NAME 2026  ·  POSTER P-00"
TITLE = "State the finding in the title, not the topic, in two lines at most"
AUTHORS = [("First Author", {}), ("1", {"sup": True}), (",  Second Author", {}),
           ("1", {"sup": True}), (",  Han-Bo-Ram Lee", {}), ("1,*", {"sup": True})]
AFFIL = [[("1 ", {"sup": True}),
          ("Graduate School of Semiconductor Materials & Devices Engineering, "
           "Ulsan National Institute of Science and Technology (UNIST)", {})],
         [("* hbrlee@unist.ac.kr", {})]]

COLUMNS = [
    [("01", "Introduction", [
        ("text", "Two or three sentences: the problem, why it matters, and the gap "
                 "this work fills. Body text is 28 pt and never goes below 24 pt — it "
                 "is read by someone standing a step back from the poster."),
        ("bullets", ["State the question you answered",
                     "Give the one number that frames it",
                     "Say what was missing before"]),
     ]),
     ("02", "Experimental", [
        ("text", "Only what a visitor needs to trust the result: process, precursors, "
                 "conditions. The full recipe belongs in the paper."),
        ("figure", 1, 3.0, "3:1", "Figure 1. Process sequence, one step per panel."),
        ("flex", 2, "Figure 2. Reactor or device schematic."),
     ])],
    [("03", "Results and Discussion", [
        ("sub", "A.  Lead with the main finding"),
        ("text", "One claim per figure, and the claim in the caption, so the poster "
                 "still reads with the text skipped."),
        ("pair", 3, 4 / 3, "4:3",
         "Figure 3. (a) The measurement. (b) The control, on the same axes."),
        ("sub", "B.  Then what supports it"),
        ("text", "Point out what to look at — the axis, the trend, the crossover. "
                 "Visitors will not find it on their own."),
        ("flex", 4, "Figure 4. Supporting data or comparison with prior work."),
     ]),
     ("04", "Conclusion", [
        ("summary", ["The finding, in one sentence",
                     "What it changes for the field",
                     "What comes next"]),
        ("references", ["[1] A. Author et al., Chem. Mater. 36, 1234 (2024).",
                        "[2] B. Author et al., Adv. Mater. 35, 2301234 (2023)."]),
     ])],
]


# --- the poster ------------------------------------------------------------
class Poster:
    BODY_SPACING = 1.35
    SECTION_GAP = 24         # between sections (and between panels)
    AFTER_TEXT = 10          # text -> next block in the same section
    AFTER_FIGURE = 14        # caption -> next block
    BULLET_GAP = 3
    PANEL_PAD = 18
    PAIR_GAP = 12

    def __init__(self, size, style, measure):
        self.S = S = SIZES[size]
        self.size, self.style = size, style
        self.T = TYPE
        self.m = measure
        self.W, self.H, self.M, self.G = S["w"], S["h"], S["margin"], S["gutter"]
        self.col_w = (self.W - 2 * self.M - self.G) / 2
        self.col_x = [self.M, self.M + self.col_w + self.G]
        self.dark = style in ("panel",)          # page ground is navy
        self.pad = self.PANEL_PAD if style == "panel" else 0
        self.inner = self.col_w - 2 * self.pad   # width blocks are set in

    # -- measuring ----------------------------------------------------------
    def text_h(self, s, w, size, spacing, bold=False):
        return self.m.lines(s, w, size, bold) * line_pitch(size, spacing)

    def heading_h(self):
        return self.T["section"] * PT_MM * 1.2 + 6 + 0.8 + 12

    def sub_h(self, t):
        return self.text_h(t, self.inner, self.T["sub"], 1.1, bold=True)

    def bullets_h(self, items, w):
        size = self.T["body"]
        ind = self._indent(size)
        return sum(self.text_h(i, w - ind, size, self.BODY_SPACING) for i in items) \
            + self.BULLET_GAP * (len(items) - 1)

    def _indent(self, size):
        return size * PT_MM * 1.05

    def caption_h(self, caption):
        return 6 + self.text_h(caption, self.inner, self.T["caption"], 1.3)

    def label_h(self):
        return self.T["small"] * PT_MM * 1.3 + 4

    def height(self, b):
        kind, w = b[0], self.inner
        if kind == "sub":
            return self.sub_h(b[1])
        if kind == "text":
            return self.text_h(b[1], w, self.T["body"], self.BODY_SPACING)
        if kind == "bullets":
            return self.bullets_h(b[1], w)
        if kind == "figure":
            return w / b[2] + self.caption_h(b[4])
        if kind == "pair":
            return (w - self.PAIR_GAP) / 2 / b[2] + self.caption_h(b[4])
        if kind == "flex":
            return self.caption_h(b[2])
        if kind == "summary":
            return 2 * 16 + self.bullets_h(b[1], w - 32)
        if kind == "references":
            return self.label_h() + sum(self.text_h(r, w, self.T["small"], 1.3)
                                        for r in b[1])
        raise ValueError(kind)

    def after(self, b, nxt):
        if nxt is None:
            return 0
        if nxt[0] == "sub":
            return 22                          # a subsection is a small section break
        if b[0] == "sub":
            return 8
        if b[0] in ("figure", "pair", "flex"):
            return self.AFTER_FIGURE
        if b[0] == "summary":
            return 18
        return self.AFTER_TEXT

    def section_h(self, blocks, flex_h):
        h = self.heading_h()
        for i, b in enumerate(blocks):
            nxt = blocks[i + 1] if i + 1 < len(blocks) else None
            h += self.height(b) + self.after(b, nxt)
            if b[0] == "flex":
                h += flex_h
        return h + 2 * self.pad

    # -- drawing ------------------------------------------------------------
    @property
    def fg(self):
        return NAVY

    def heading(self, s, x, y, num, title):
        """Teal number, navy title, and a hairline under it. The teal-capped
        rule is the poster's signature and appears once, under the header —
        not under every section (design system §4)."""
        size = self.T["section"]
        h = size * PT_MM * 1.2
        text(s, x, y, self.inner, h, [[(f"{num}  ", {"colour": TEAL}), (title, {})]],
             size, NAVY, bold=True, spacing=1.0, name=f"Section {num} title")
        rect(s, x, y + h + 6, self.inner, 0.8, BORDER, name=f"Section {num} rule")
        return self.heading_h()

    def bullets(self, s, x, y, w, items, colour=INK, name="Bullet"):
        """Teal squares centred on the first line's x-height (design system §4)."""
        size = self.T["body"]
        sq = size * 0.3 * PT_MM
        ind = self._indent(size)
        mid = first_baseline(size, self.BODY_SPACING) - X_HEIGHT / 2 * size * PT_MM
        for i, item in enumerate(items):
            h = self.text_h(item, w - ind, size, self.BODY_SPACING)
            rect(s, x, y + mid - sq / 2, sq, sq, TEAL)
            text(s, x + ind, y, w - ind, h, item, size, colour,
                 spacing=self.BODY_SPACING, name=f"{name} {i + 1}")
            y += h + self.BULLET_GAP

    def well(self, s, x, y, w, h, label, name):
        """A figure well — where a plot or micrograph gets pasted in. The label
        gives the slot's shape and size, so the image can be made to fit."""
        box = rect(s, x, y, w, h, SURFACE, line=BORDER, name=name)
        tf = box.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = Mm(4)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = f"{label}  ·  {w:.0f} × {h:.0f} mm"
        _run_font(r, self.T["caption"], MUTED)

    def caption(self, s, x, y, caption, n):
        h = self.caption_h(caption) - 6
        text(s, x, y + 6, self.inner, h, caption, self.T["caption"], MUTED, spacing=1.3,
             name=f"Figure {n} caption")

    def label(self, s, x, y, w, t, colour=MUTED):
        text(s, x, y, w, self.label_h(), t, self.T["small"], colour, bold=True,
             tracking=0.14, spacing=1.0, name=t.title())

    def section(self, s, x, y, num, title, blocks, flex_h):
        h = self.section_h(blocks, flex_h)
        if self.style == "panel":
            rect(s, x, y, self.col_w, h, WHITE, name=f"Section {num} panel")
        x0, y = x + self.pad, y + self.pad
        y += self.heading(s, x0, y, num, title)
        w = self.inner
        for i, b in enumerate(blocks):
            kind, bh = b[0], self.height(b)
            nxt = blocks[i + 1] if i + 1 < len(blocks) else None
            if kind == "sub":
                text(s, x0, y, w, bh, b[1], self.T["sub"], NAVY, bold=True, spacing=1.1,
                     name="Subsection title")
            elif kind == "text":
                text(s, x0, y, w, bh, b[1], self.T["body"], INK,
                     spacing=self.BODY_SPACING, name="Body")
            elif kind == "bullets":
                self.bullets(s, x0, y, w, b[1])
            elif kind == "figure":
                fh = w / b[2]
                self.well(s, x0, y, w, fh, f"Figure {b[1]}  ·  {b[3]}", f"Figure {b[1]} slot")
                self.caption(s, x0, y + fh, b[4], b[1])
            elif kind == "pair":
                fw = (w - self.PAIR_GAP) / 2
                fh = fw / b[2]
                for j, tag in enumerate("ab"):
                    self.well(s, x0 + j * (fw + self.PAIR_GAP), y, fw, fh,
                              f"Figure {b[1]}{tag}  ·  {b[3]}", f"Figure {b[1]}{tag} slot")
                self.caption(s, x0, y + fh, b[4], b[1])
            elif kind == "flex":
                self.well(s, x0, y, w, flex_h, f"Figure {b[1]}", f"Figure {b[1]} slot")
                self.caption(s, x0, y + flex_h, b[2], b[1])
                bh += flex_h
            elif kind == "summary":
                rect(s, x0, y, w, bh, SURFACE, name="Conclusion box")
                self.bullets(s, x0 + 16, y + 16, w - 32, b[1], NAVY, "Conclusion")
            elif kind == "references":
                self.label(s, x0, y, w, "REFERENCES")
                text(s, x0, y + self.label_h(), w, bh - self.label_h(), b[1],
                     self.T["small"], MUTED, spacing=1.3, name="References")
            y += bh + self.after(b, nxt)
        return h

    def column(self, s, x, top, bottom, sections):
        fixed = sum(self.section_h(blocks, 0) for _, _, blocks in sections) \
            + self.SECTION_GAP * (len(sections) - 1)
        n_flex = sum(1 for _, _, blocks in sections for b in blocks if b[0] == "flex")
        flex_h = (bottom - top - fixed) / max(n_flex, 1)
        if n_flex and flex_h < 100:
            raise SystemExit(f"{self.size}-{self.style}: 그림 자리 높이 {flex_h:.0f} mm — "
                             "이 단에 글이 너무 많습니다")
        y = top
        for num, title, blocks in sections:
            y += self.section(s, x, y, num, title, blocks, flex_h) + self.SECTION_GAP
        return y - self.SECTION_GAP, flex_h

    # -- header -------------------------------------------------------------
    def header(self, s):
        """Emblem left, the text block beside it, a logo slot right. The
        emblem sits next to the affiliation it stands for (§8); the text is
        left-aligned like every other title in the system, rather than centred
        between the logos as the references were."""
        T, W, H, M = self.T, self.W, self.H, self.M
        on_navy = self.style in ("panel", "band")
        E = self.S["emblem"]
        tx = M + E + 26
        tw = W - M - E - 26 - tx
        title_h = self.m.lines(TITLE, tw, T["title"], bold=True) * line_pitch(T["title"], 0.95)
        eyebrow_h = T["eyebrow"] * PT_MM * 1.2
        authors_h = line_pitch(T["authors"], 1.15)
        affil_h = sum(self.m.lines("".join(t for t, _ in p), tw, T["affil"])
                      for p in AFFIL) * line_pitch(T["affil"], 1.25)
        block = eyebrow_h + 8 + title_h + 8 + authors_h + 6 + affil_h
        lo, hi = HEADER_SHARE
        need = block + 2 * 18 + (8 if self.style == "standard" else 0)
        HH = max(need, lo * H)
        if HH > hi * H:
            raise SystemExit(f"{self.size}-{self.style}: 머리 {HH:.0f} mm = {HH / H:.0%} — "
                             "16 % 를 넘습니다. 제목을 줄이세요")
        if self.style == "band":
            rect(s, 0, 0, W, HH, NAVY, name="Header band")
        y = (HH - (8 if self.style == "standard" else 0) - block) / 2
        ey = y + block / 2 - E / 2
        if on_navy:
            picture(s, ASSETS / "unist-emblem-onnavy.png", M, ey, h=E, name="UNIST emblem")
        else:
            picture(s, ASSETS / "unist-emblem.png", M, ey, h=E, name="UNIST emblem")
        # The right slot is for the conference's or the project's own logo,
        # which comes in every colour: on navy it sits in a white box (§7-1).
        slot = rect(s, W - M - E, ey, E, E, WHITE if on_navy else SURFACE,
                    line=None if on_navy else BORDER, name="Conference logo slot")
        tf = slot.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Mm(4)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = "Conference or project logo"
        _run_font(r, T["small"], MUTED)

        fg, sub = (WHITE, ON_NAVY) if on_navy else (NAVY, MUTED)
        text(s, tx, y, tw, eyebrow_h, EYEBROW, T["eyebrow"], TEAL, bold=True,
             tracking=0.14, spacing=1.0, name="Conference · poster number")
        y += eyebrow_h + 8
        text(s, tx, y, tw, title_h, TITLE, T["title"], fg, bold=True, spacing=0.95,
             name="Title")
        y += title_h + 8
        text(s, tx, y, tw, authors_h, [AUTHORS], T["authors"], fg, spacing=1.15,
             name="Authors")
        y += authors_h + 6
        text(s, tx, y, tw, affil_h, AFFIL, T["affil"], sub, spacing=1.25,
             name="Affiliation")
        if self.style == "standard":
            # The signature rule: navy across the measure, teal cap on the left.
            ry = HH - 8
            rect(s, M, ry + 1, W - 2 * M, 1.2, NAVY, name="Rule")
            rect(s, M, ry, 60, 3.2, TEAL, name="Rule cap")
        return HH

    # -- footer -------------------------------------------------------------
    def footer(self, s):
        """HBRLRG logo and contact on the left, acknowledgements, QR right —
        the slide footer's order, with the funding line posters need."""
        T, W, H, M = self.T, self.W, self.H, self.M
        on_navy = self.style in ("panel", "band")
        FH = 74
        fy = H - FH
        if self.style == "band":
            rect(s, 0, fy, W, FH, NAVY, name="Footer band")
        elif self.style == "standard":
            rect(s, 0, fy, W, FH, SURFACE, name="Footer ground")
        fg, sub = (WHITE, ON_NAVY) if on_navy else (INK, MUTED)
        logo = "logo/hbrlrg-horizontal-reverse.png" if on_navy else "logo/hbrlrg-horizontal.png"
        ink = 12                                   # mm of visible logo height
        lh = ink / LOGO_INK
        lw, _ = picture(s, ASSETS / logo, M - lh * 200 / 708, fy + FH / 2 - lh / 2, h=lh,
                        name="HBRLRG logo")
        x = M + lw * (2173 - 200) / 2400 + 14
        rect(s, x, fy + FH / 2 - 10, 0.6, 20, NAVY_RULE if on_navy else BORDER,
             name="Divider")
        x += 14
        cw = 250
        text(s, x, fy + FH / 2 - 14, cw, 28,
             [[("First Author  ·  first.author@unist.ac.kr", {})],
              [("https://hbrl-research.group", {"size": T["small"], "colour": sub})]],
             24, fg, spacing=1.2, anchor=MSO_ANCHOR.MIDDLE, name="Contact")
        qr = 46
        ax = x + cw + 20
        aw = W - M - qr - 20 - ax
        self.label(s, ax, fy + FH / 2 - 16, aw, "ACKNOWLEDGEMENTS",
                   TEAL if on_navy else MUTED)
        text(s, ax, fy + FH / 2 - 16 + self.label_h(), aw, 26,
             "This work was supported by the funding agency (grant no. 0000-0000). "
             "Replace with your own funding statement.",
             T["small"], sub, spacing=1.25, name="Acknowledgements")
        picture(s, ASSETS / "qr/hbrl-research-group.png", W - M - qr, fy + (FH - qr) / 2,
                h=qr, name="QR code")
        return fy

    # -- whole page ---------------------------------------------------------
    def build(self, out):
        prs = Presentation()
        prs.slide_width, prs.slide_height = Mm(self.W), Mm(self.H)
        s = prs.slides.add_slide(prs.slide_layouts[6])
        if self.dark:
            rect(s, 0, 0, self.W, self.H, NAVY, name="Page ground")
        HH = self.header(s)
        fy = self.footer(s)
        gap = 26 if self.style == "standard" else 30
        top = HH + (12 if self.style == "panel" else gap)
        bottom = fy - (self.G if self.style == "panel" else gap)
        ends = [self.column(s, x, top, bottom, secs) for x, secs in zip(self.col_x, COLUMNS)]
        out = Path(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        prs.save(out)
        flex = " · ".join(f"{fh:.0f}" for _, fh in ends)
        print(f"  {out.name:<34} {self.W} × {self.H} mm · 머리 {HH:.0f} mm "
              f"({HH / self.H:.1%}) · 단 끝 {ends[0][0]:.1f} / {ends[1][0]:.1f} "
              f"(본문 하단 {bottom:.1f}) · 가변 그림 {flex} mm")
        return out


def build(size, style, outdir, font_dir, measure=None):
    P = Poster(size, style, measure or Measure(font_dir))
    return P.build(Path(outdir) / f"hbrlrg-poster-{size}-{style}.pptx")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir", nargs="?", default="office")
    ap.add_argument("--size", default="all", choices=sorted(SIZES) + ["all"])
    ap.add_argument("--style", default="all", choices=list(STYLES) + ["all"])
    ap.add_argument("--fonts", help="Archivo-Regular.ttf · Archivo-Bold.ttf 가 있는 폴더")
    a = ap.parse_args()
    m = Measure(find_fonts(a.fonts))
    for size in SIZES if a.size == "all" else [a.size]:
        for style in STYLES if a.style == "all" else [a.style]:
            build(size, style, a.outdir, None, m)
