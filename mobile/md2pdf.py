"""Markdown to a phone-readable PDF in the HBRLRG mobile template.

    python3 mobile/md2pdf.py guide.md guide.pdf

Pass --html to keep the intermediate HTML next to the PDF, which is the quicker
way to see why something laid out oddly.

Two things happen here that CSS alone cannot do.

Tables wider than four columns are rebuilt as one card per row, with each
column heading carried along as the label for its value. On a 124mm measure a
five-column table gives each column about 24mm — two or three Korean syllables
before it wraps — so the table has to become something else, not merely shrink.

Fonts are resolved to real files and declared with @font-face, so Chromium
embeds them in the PDF. Without this the output falls back to whatever the
machine happens to have, and Korean lands on a system face.
"""
import argparse
import html as html_mod
import re
import shutil
import sys
import urllib.request
from pathlib import Path

import markdown
from lxml import etree as ET
from lxml import html as LH

ROOT = Path(__file__).resolve().parent.parent
CSS = Path(__file__).resolve().parent / "hbrlrg-mobile.css"
LOGO = ROOT / "assets/logo/hbrlrg-horizontal.png"

# Above this, a table stops being readable at this measure and becomes cards.
MAX_TABLE_COLS = 4

CHROMIUM_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
    shutil.which("chromium") or "",
    shutil.which("google-chrome") or "",
]

ARCHIVO = "https://raw.githubusercontent.com/Omnibus-Type/Archivo/master/fonts/ttf"
PRETENDARD = ("https://raw.githubusercontent.com/orioncactus/pretendard/main"
              "/packages/pretendard/dist/public/static/alternative")
FONTS = {
    "Archivo-Regular.ttf": f"{ARCHIVO}/Archivo-Regular.ttf",
    "Archivo-Bold.ttf": f"{ARCHIVO}/Archivo-Bold.ttf",
    "Archivo-Italic.ttf": f"{ARCHIVO}/Archivo-Italic.ttf",
    "Pretendard-Regular.ttf": f"{PRETENDARD}/Pretendard-Regular.ttf",
    "Pretendard-SemiBold.ttf": f"{PRETENDARD}/Pretendard-SemiBold.ttf",
    "Pretendard-Bold.ttf": f"{PRETENDARD}/Pretendard-Bold.ttf",
}

FACE = """@font-face{font-family:'Archivo';src:url('{Archivo-Regular.ttf}') format('truetype');font-weight:400;font-style:normal;}
@font-face{font-family:'Archivo';src:url('{Archivo-Bold.ttf}') format('truetype');font-weight:600 700;font-style:normal;}
@font-face{font-family:'Archivo';src:url('{Archivo-Italic.ttf}') format('truetype');font-weight:400;font-style:italic;}
@font-face{font-family:'Pretendard';src:url('{Pretendard-Regular.ttf}') format('truetype');font-weight:400;font-style:normal;}
@font-face{font-family:'Pretendard';src:url('{Pretendard-SemiBold.ttf}') format('truetype');font-weight:500 600;font-style:normal;}
@font-face{font-family:'Pretendard';src:url('{Pretendard-Bold.ttf}') format('truetype');font-weight:700;font-style:normal;}"""

CDN = """<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">"""


# --- front matter ----------------------------------------------------------
def split_front_matter(text):
    """Pull a leading `--- key: value --- ` block off, if there is one."""
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip().strip('"\'')
    return meta, text[m.end():]


# --- tables ----------------------------------------------------------------
def table_to_cards(table, doc):
    """Rebuild one wide table as a stack of cards, one per row.

    The first column becomes the card's title — in a listing it is the name of
    the thing, and reading it as a heading beats reading it as another labelled
    field. Every other column keeps its heading as the label.
    """
    heads = [" ".join(th.text_content().split())
             for th in table.xpath(".//thead//th")]
    if not heads:
        first = table.xpath(".//tr")[:1]
        if not first:
            return None
        heads = [" ".join(c.text_content().split())
                 for c in first[0].xpath("./th|./td")]

    rows = table.xpath(".//tbody/tr") or table.xpath(".//tr")[1:]
    if not rows:
        return None

    wrap = LH.Element("div")
    wrap.set("class", "cards")
    for tr in rows:
        cells = tr.xpath("./td|./th")
        if not cells:
            continue
        card = ET.SubElement(wrap, "div")
        card.set("class", "card")

        title = ET.SubElement(card, "div")
        title.set("class", "card__title")
        title.text = " ".join(cells[0].text_content().split())

        for head, cell in zip(heads[1:], cells[1:]):
            value = " ".join(cell.text_content().split())
            if not value or value in {"-", "—", "–"}:
                continue          # an empty cell is noise as a labelled row
            row = ET.SubElement(card, "div")
            row.set("class", "card__row")
            k = ET.SubElement(row, "span")
            k.set("class", "card__key")
            k.text = head
            v = ET.SubElement(row, "span")
            v.set("class", "card__val")
            v.text = value
    return wrap


def rework_tables(doc):
    """Cards for wide tables; everything else is left as a table."""
    wide = kept = 0
    for table in doc.xpath("//table"):
        header_cells = table.xpath(".//thead//th") or table.xpath(".//tr[1]/*")
        if len(header_cells) > MAX_TABLE_COLS:
            cards = table_to_cards(table, doc)
            if cards is not None:
                table.getparent().replace(table, cards)
                wide += 1
                continue
        kept += 1
    return wide, kept


# --- fonts -----------------------------------------------------------------
def ensure_fonts(font_dir):
    """Return a file:// map of the fonts, downloading any that are missing.

    Returns None when they cannot be obtained, and the caller falls back to the
    CDN — which still renders, but only if the machine is online.
    """
    font_dir = Path(font_dir)
    font_dir.mkdir(parents=True, exist_ok=True)
    out = {}
    for name, url in FONTS.items():
        path = font_dir / name
        if not path.exists():
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    path.write_bytes(r.read())
            except Exception as e:                       # offline, proxy, 404
                print(f"  폰트 {name} 내려받기 실패: {e}", file=sys.stderr)
                return None
        out[name] = path.resolve().as_uri()
    return out


def fill_faces(faces):
    """Substitute by name. The keys contain dots, so str.format cannot do it."""
    out = FACE
    for name, uri in faces.items():
        out = out.replace("{%s}" % name, uri)
    return out


# --- page ------------------------------------------------------------------
def build_html(meta, body_html, faces):
    title = meta.get("title", "")
    subtitle = meta.get("subtitle", "")
    date = meta.get("date", "")
    cover = meta.get("cover", "true").lower() not in {"false", "no", "0"}

    head_fonts = fill_faces(faces) if faces else ""
    cdn = "" if faces else CDN

    cover_html = ""
    if cover and title:
        cover_html = f"""<section class="page cover">
  <img class="cover__logo" src="{LOGO.resolve().as_uri()}" alt="HBRLRG">
  <div class="cover__spacer"></div>
  <h1 class="cover__title">{html_mod.escape(title)}</h1>
  {f'<p class="cover__subtitle">{html_mod.escape(subtitle)}</p>' if subtitle else ''}
  {f'<p class="cover__meta">{html_mod.escape(date)}</p>' if date else ''}
</section>
"""

    return f"""<!doctype html>
<html lang="{meta.get('lang', 'ko')}">
<head>
<meta charset="utf-8">
<title>{html_mod.escape(title) or 'HBRLRG'}</title>
{cdn}
<style>
{head_fonts}
{CSS.read_text(encoding='utf-8')}
</style>
</head>
<body>
{cover_html}<section class="page">
{body_html}
</section>
</body>
</html>
"""


def render(html_text, out_pdf, page_w, page_h, margin):
    from playwright.sync_api import sync_playwright

    exe = next((p for p in CHROMIUM_CANDIDATES if p and Path(p).exists()), None)
    tmp = Path(out_pdf).with_suffix(".render.html")
    tmp.write_text(html_text, encoding="utf-8")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=exe) if exe \
                else p.chromium.launch()
            page = browser.new_page()
            page.goto(tmp.resolve().as_uri(), wait_until="networkidle")
            page.pdf(path=str(out_pdf), width=page_w, height=page_h,
                     print_background=True,
                     margin={"top": margin, "bottom": margin,
                             "left": margin, "right": margin})
            browser.close()
    finally:
        tmp.unlink(missing_ok=True)


def main():
    ap = argparse.ArgumentParser(description="Markdown -> HBRLRG mobile PDF")
    ap.add_argument("source")
    ap.add_argument("output")
    ap.add_argument("--fonts", default=str(ROOT / ".fonts"),
                    help="폰트 캐시 폴더 (없으면 내려받습니다)")
    ap.add_argument("--page", default="148mm x 210mm",
                    help='페이지 크기, 예 "90mm x 195mm"')
    ap.add_argument("--margin", default="12mm")
    ap.add_argument("--html", action="store_true", help="중간 HTML 도 남깁니다")
    args = ap.parse_args()

    text = Path(args.source).read_text(encoding="utf-8")
    meta, body = split_front_matter(text)

    body_html = markdown.markdown(
        body, extensions=["tables", "sane_lists", "attr_list"])
    doc = LH.fragment_fromstring(body_html, create_parent="div")
    wide, kept = rework_tables(doc)
    body_html = "".join(
        LH.tostring(c, encoding="unicode") for c in doc.iterchildren())

    faces = ensure_fonts(args.fonts)
    if faces is None:
        print("  로컬 폰트를 쓰지 못해 CDN 으로 진행합니다 "
              "(오프라인이면 서체가 대체됩니다)", file=sys.stderr)

    page_w, page_h = [s.strip() for s in args.page.lower().split("x")]
    page = build_html(meta, body_html, faces)

    if args.html:
        Path(args.output).with_suffix(".html").write_text(page, encoding="utf-8")

    render(page, args.output, page_w, page_h, args.margin)

    size = Path(args.output).stat().st_size / 1024
    print(f"  {args.output}  {size:.0f} KB · 카드로 바꾼 표 {wide}개 · "
          f"표로 둔 것 {kept}개")


if __name__ == "__main__":
    main()
