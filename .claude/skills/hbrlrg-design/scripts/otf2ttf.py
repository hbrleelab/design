"""Convert CFF-flavoured OpenType (.otf) to TrueType (.ttf).

PowerPoint only embeds TrueType outlines, so Pretendard's .otf has to be
converted before it can go into ppt/fonts/*.fntdata.
"""
import sys

from fontTools.ttLib import TTFont, newTable
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

MAX_ERR = 1.0


def glyphs_to_quadratic(glyphs, max_err, reverse_direction):
    quad = {}
    for name in glyphs.keys():
        pen = TTGlyphPen(glyphs)
        glyphs[name].draw(Cu2QuPen(pen, max_err, reverse_direction=reverse_direction))
        quad[name] = pen.glyph()
    return quad


def otf_to_ttf(font, max_err=MAX_ERR, post_format=2.0, reverse_direction=True):
    assert font.sfntVersion == "OTTO", font.sfntVersion
    assert "CFF " in font

    glyph_order = font.getGlyphOrder()

    font["loca"] = newTable("loca")
    font["glyf"] = glyf = newTable("glyf")
    glyf.glyphOrder = glyph_order
    glyf.glyphs = glyphs_to_quadratic(font.getGlyphSet(), max_err, reverse_direction)
    del font["CFF "]
    if "VORG" in font:
        del font["VORG"]
    glyf.compile(font)

    font["maxp"].numGlyphs = len(glyf.glyphs)

    post = font["post"]
    post.formatType = post_format
    post.extraNames = []
    post.mapping = {}
    post.glyphOrder = None

    font.sfntVersion = "\000\001\000\000"


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    f = TTFont(src)
    otf_to_ttf(f)
    f.save(dst)
    print(f"{src} -> {dst}", flush=True)
