"""Embed TrueType families into a .docx as word/fonts/*.odttf.

Word does support embedded fonts — python-docx simply has no API for it, so the
parts are written by hand. The format is ECMA-376 §17.8: the font file is stored
"obfuscated", meaning its first 32 bytes are XORed with the font key, and the
part is declared in word/fontTable.xml.

Only Microsoft Word honours these. LibreOffice, Google Docs and Pages ignore the
embedded parts and fall back to whatever is installed, so this raises the floor
for Word users rather than guaranteeing the typeface everywhere.

    python3 embed_docx_fonts.py in.docx out.docx font_dir [--subset-latin]

Embedding is a licensed act: both Archivo and Pretendard are SIL OFL 1.1, which
permits it. Check fsType before adding any other family.
"""
import re
import shutil
import sys
import uuid
import zipfile
from pathlib import Path

REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font"
CONTENT_TYPE = "application/vnd.openxmlformats-officedocument.obfuscatedFont"

# Word names the four slots; a family may supply any subset of them.
SLOTS = ("embedRegular", "embedBold", "embedItalic", "embedBoldItalic")


def obfuscate(data, key_guid):
    """ECMA-376 §17.8.1 — XOR the first 32 bytes with the reversed font key.

    The key is the GUID that also goes in w:fontKey. Word reverses the byte
    order before applying it, and applies the 16-byte key twice.
    """
    raw = bytes.fromhex(key_guid.strip("{}").replace("-", ""))
    mask = raw[::-1]
    head = bytes(b ^ mask[i % 16] for i, b in enumerate(data[:32]))
    return head + data[32:]


def font_key():
    return "{" + str(uuid.uuid4()).upper() + "}"


def embed(src, dst, families, font_dir):
    work = Path("_docx_embed_tmp")
    if work.exists():
        shutil.rmtree(work)
    with zipfile.ZipFile(src) as z:
        names = z.namelist()
        z.extractall(work)

    fonts_out = work / "word/fonts"
    fonts_out.mkdir(parents=True, exist_ok=True)

    rels_path = work / "word/_rels/fontTable.xml.rels"
    if rels_path.exists():
        rels = rels_path.read_text(encoding="utf-8")
    else:
        rels_path.parent.mkdir(parents=True, exist_ok=True)
        rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                '<Relationships xmlns="http://schemas.openxmlformats.org/'
                'package/2006/relationships"></Relationships>')

    ids = [int(m) for m in re.findall(r'Id="rId(\d+)"', rels)]
    next_id = max(ids) + 1 if ids else 1

    new_rels, blocks, index, embedded = [], {}, 1, []
    for typeface, slots in families:
        parts = []
        for slot, filename in slots.items():
            path = Path(font_dir) / filename
            if not path.exists():
                print(f"  건너뜀 — 파일 없음: {filename}")
                continue
            key = font_key()
            part = f"font{index}.odttf"
            (fonts_out / part).write_bytes(obfuscate(path.read_bytes(), key))
            rid = f"rId{next_id}"
            new_rels.append(
                f'<Relationship Id="{rid}" Type="{REL_TYPE}" Target="fonts/{part}"/>')
            parts.append(f'<w:{slot} r:id="{rid}" w:fontKey="{key}"/>')
            next_id += 1
            index += 1
            embedded.append(f"{typeface} {slot[5:]}")
        if parts:
            # CT_Font is a sequence: the embed* elements come last, and in the
            # order regular, bold, italic, boldItalic.
            order = {s: i for i, s in enumerate(SLOTS)}
            parts.sort(key=lambda p: order[re.search(r"<w:(embed\w+)", p).group(1)])
            blocks[typeface] = "".join(parts)

    if not blocks:
        raise SystemExit("임베드할 폰트가 없습니다")

    rels = rels.replace("</Relationships>", "".join(new_rels) + "</Relationships>")
    rels_path.write_text(rels, encoding="utf-8")

    # --- fontTable.xml: extend the family if declared, else add it ----------
    ft_path = work / "word/fontTable.xml"
    ft = ft_path.read_text(encoding="utf-8")
    for typeface, body in blocks.items():
        pattern = re.compile(
            r'(<w:font w:name="%s">)(.*?)(</w:font>)' % re.escape(typeface), re.S)
        if pattern.search(ft):
            ft = pattern.sub(lambda m: m.group(1) + m.group(2) + body + m.group(3),
                             ft, count=1)
        else:
            declaration = (
                f'<w:font w:name="{typeface}">'
                '<w:charset w:val="00"/><w:family w:val="swiss"/>'
                '<w:pitch w:val="variable"/>' + body + '</w:font>')
            ft = ft.replace("</w:fonts>", declaration + "</w:fonts>", 1)
    ft_path.write_text(ft, encoding="utf-8")

    # --- settings.xml: turn embedding on, and keep the full character set ---
    st_path = work / "word/settings.xml"
    st = st_path.read_text(encoding="utf-8")
    if "<w:embedTrueTypeFonts/>" not in st:
        # These two sit early in the CT_Settings sequence; anchoring on
        # defaultTabStop would put them after elements that must follow them.
        flags = "<w:embedTrueTypeFonts/><w:saveSubsetFonts w:val=\"false\"/>"
        m = re.search(r"<w:settings[^>]*>", st)
        st = st[:m.end()] + flags + st[m.end():]
        st_path.write_text(st, encoding="utf-8")

    # --- [Content_Types].xml ------------------------------------------------
    ct_path = work / "[Content_Types].xml"
    ct = ct_path.read_text(encoding="utf-8")
    if 'Extension="odttf"' not in ct:
        ct = ct.replace(
            "<Types ", "<Types ", 1)
        ct = re.sub(r"(<Types[^>]*>)",
                    r'\1<Default Extension="odttf" ContentType="%s"/>' % CONTENT_TYPE,
                    ct, count=1)
        ct_path.write_text(ct, encoding="utf-8")

    # Repack, keeping the original part order so Word sees a familiar package.
    ordered = [n for n in names if (work / n).is_file()]
    extra = sorted({str(p.relative_to(work)) for p in work.rglob("*") if p.is_file()}
                   - set(ordered))
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        for name in ordered + extra:
            z.write(work / name, name)
    shutil.rmtree(work)

    size = Path(dst).stat().st_size / 1024
    print(f"  {Path(dst).name}: {len(embedded)}개 슬롯 임베드 · {size:.0f} KB")
    return embedded


ARCHIVO = ("Archivo", {
    "embedRegular": "Archivo-Regular.ttf",
    "embedBold": "Archivo-Bold.ttf",
    "embedItalic": "Archivo-Italic.ttf",
    "embedBoldItalic": "Archivo-BoldItalic.ttf",
})
PRETENDARD = ("Pretendard", {
    "embedRegular": "Pretendard-Regular.ttf",
    "embedBold": "Pretendard-Bold.ttf",
})


if __name__ == "__main__":
    src, dst, font_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    embed(src, dst, [ARCHIVO, PRETENDARD], font_dir)
