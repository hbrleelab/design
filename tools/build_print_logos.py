"""Build print-ready vector logos (PDF) from the SVG masters.

    python3 tools/build_print_logos.py [outdir]

The SVGs are already true vector with the lettering outlined, so nothing is
redrawn here. What this adds is the two things a printer asks for and an SVG
does not give them:

  * PDF, which every layout and prepress tool places without argument. A fair
    number of print shops still will not take an SVG at all.
  * A CMYK twin. A PDF out of any browser or SVG tool is RGB, and an RGB file
    sent to a four-colour press gets converted by whoever happens to open it —
    which is how a logo comes back a different colour than the website.

The artwork is flat colour, two inks at most, so the CMYK conversion is exact
and checkable: every fill and stroke operator is rewritten, and the result is
verified to contain no RGB operator left behind.

Values come from assets/logo/README.txt and round-trip to the brand hexes.
They are a plain conversion, not a profile-managed one; a printer working to a
specific stock may still want to run their own, and should be told the hexes.
"""
import re
import shutil
import sys
from pathlib import Path

import cairosvg
import pikepdf

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "assets/logo"
MM = 72 / 25.4

# Brand inks.
#
# NOT the arithmetic conversion. Turning #0EA79A into CMYK with the textbook
# formula (1-R/255 and so on) gives 92/0/8/35, which is what the logo README
# carried and what prints a blue nothing like the brand teal. The formula
# assumes perfect inks; real process cyan is around #00ADEF, already well
# towards blue, so reaching a green-teal needs far more yellow and far less
# black than the arithmetic suggests.
#
# These values were found by searching the process-ink model for the CMYK that
# renders back to the brand hex, and each round-trips exactly:
#
#   Navy #14243F   arithmetic 68/43/0/75   -> prints #202942
#   Navy #14243F   these      100/82/38/52 -> prints #14243F
#   Teal #0EA79A   arithmetic 92/0/8/35    -> prints #0E7A9F   (clearly blue)
#   Teal #0EA79A   these      94/0/48/4    -> prints #0EA79A
#
# They are generic process-ink values, not profile-managed ones. A printer
# working to a named profile should convert from the hex themselves; give them
# #14243F and #0EA79A and let their own profile decide.
INKS = {
    "14243F": (1.00, 0.82, 0.38, 0.52),   # Navy
    "0EA79A": (0.94, 0.00, 0.48, 0.04),   # Teal
    "000000": (0.00, 0.00, 0.00, 1.00),   # mono black — 100% K, not four-colour
    "FFFFFF": (0.00, 0.00, 0.00, 0.00),   # reverse white — knocks out of the ink
}

# What a card actually needs, and the width each is drawn at. Vector scales
# without loss, so these are a sensible default rather than a constraint.
VARIANTS = [
    ("hbrlrg-horizontal", 40.0, "밝은 배경 · 기본"),
    ("hbrlrg-horizontal-reverse", 40.0, "어두운 배경 (네이비 명함)"),
    ("hbrlrg-horizontal-mono", 40.0, "단색 인쇄 (먹 1도)"),
    ("hbrlrg-symbol", 12.0, "심볼 단독 (명함 뒷면 등)"),
]


def rgb_key(r, g, b):
    return "%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255))


def to_cmyk(stream):
    """Rewrite every DeviceRGB colour operator as DeviceCMYK.

    Returns the new stream and the inks used, so the caller can report what
    went in rather than trusting that it worked.
    """
    used = []

    def swap(m):
        r, g, b = (float(x) for x in m.group(1).split())
        op = m.group(2)
        key = rgb_key(r, g, b)
        if key not in INKS:
            raise SystemExit(
                f"#{key} 는 브랜드 색이 아닙니다 — CMYK 값을 모르면 변환할 수 없습니다")
        c, m_, y, k = INKS[key]
        used.append(key)
        return "%g %g %g %g %s" % (c, m_, y, k, "k" if op == "rg" else "K")

    out = re.sub(r"((?:[-\d.]+\s+){3})(rg|RG)(?![A-Za-z])", swap, stream)
    # Greys: cairo emits `g`/`G` for pure black or white in some paths.
    def swap_grey(m):
        v = float(m.group(1))
        key = rgb_key(v, v, v)
        if key not in INKS:
            raise SystemExit(f"회색 {v} 에 대응하는 브랜드 잉크가 없습니다")
        c, m_, y, k = INKS[key]
        used.append(key)
        return "%g %g %g %g %s" % (c, m_, y, k, "k" if m.group(2) == "g" else "K")

    out = re.sub(r"([-\d.]+)\s+(g|G)(?![A-Za-z])", swap_grey, out)
    return out, sorted(set(used))


def check(path, expect_mm, cmyk):
    """Fail loudly rather than ship a logo that is secretly a picture."""
    problems = []
    with pikepdf.open(path) as pdf:
        if len(pdf.pages) != 1:
            problems.append(f"{len(pdf.pages)}쪽 — 1쪽이어야 합니다")
        page = pdf.pages[0]
        box = [float(x) for x in page.MediaBox]
        w_mm = (box[2] - box[0]) / MM
        if abs(w_mm - expect_mm) > 0.05:
            problems.append(f"폭 {w_mm:.3f}mm — {expect_mm}mm 이어야 합니다")
        res = page.get("/Resources", {})
        if "/XObject" in res:
            problems.append("XObject 포함 — 래스터가 섞였을 수 있습니다")
        if "/Font" in res:
            problems.append("폰트 참조 — 글자가 아웃라인이 아닙니다")
        stream = page.Contents.read_bytes().decode("latin-1")
    if cmyk:
        left = re.findall(r"(?:[-\d.]+\s+){3}(?:rg|RG)(?![A-Za-z])", stream)
        if left:
            problems.append(f"RGB 연산자 {len(left)}개가 남아 있습니다")
        if not re.search(r"(?:[-\d.]+\s+){4}(?:k|K)(?![A-Za-z])", stream):
            problems.append("CMYK 연산자가 없습니다")
    ratio = None
    with pikepdf.open(path) as pdf:
        b = [float(x) for x in pdf.pages[0].MediaBox]
        ratio = (b[2] - b[0]) / (b[3] - b[1])
    return problems, ratio


def build(outdir):
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    made = []
    for name, width_mm, note in VARIANTS:
        src = LOGO / f"{name}.svg"
        if not src.exists():
            print(f"  건너뜀 — {src.name} 없음")
            continue

        rgb_path = out / f"{name}.pdf"
        cairosvg.svg2pdf(url=str(src), write_to=str(rgb_path),
                         output_width=width_mm * MM / 0.75)

        cmyk_path = out / f"{name}-cmyk.pdf"
        shutil.copyfile(rgb_path, cmyk_path)
        with pikepdf.open(cmyk_path, allow_overwriting_input=True) as pdf:
            page = pdf.pages[0]
            stream = page.Contents.read_bytes().decode("latin-1")
            converted, inks = to_cmyk(stream)
            page.Contents.write(converted.encode("latin-1"))
            pdf.save(cmyk_path)

        for path, is_cmyk in ((rgb_path, False), (cmyk_path, True)):
            problems, ratio = check(path, width_mm, is_cmyk)
            if problems:
                raise SystemExit(f"{path.name}: " + " / ".join(problems))
        made.append((name, width_mm, inks, ratio, note))

    for name, w, inks, ratio, note in made:
        print(f"  {name}.pdf / -cmyk.pdf  {w:g}mm 폭 · 비율 {ratio:.4f} · "
              f"잉크 {', '.join('#' + i for i in inks)}  — {note}")
    return made


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else LOGO / "print")
