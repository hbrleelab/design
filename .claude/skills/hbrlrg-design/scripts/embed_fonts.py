"""Embed TrueType families into a .pptx as ppt/fonts/*.fntdata."""
import re
import shutil
import sys
import zipfile
from pathlib import Path

REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font"


def embed(src, dst, families, font_dir):
    work = Path("_embed_tmp")
    if work.exists():
        shutil.rmtree(work)
    with zipfile.ZipFile(src) as z:
        z.extractall(work)

    fonts_out = work / "ppt/fonts"
    fonts_out.mkdir(parents=True, exist_ok=True)

    rels_path = work / "ppt/_rels/presentation.xml.rels"
    rels = rels_path.read_text(encoding="utf-8")
    next_id = max(int(m) for m in re.findall(r'Id="rId(\d+)"', rels)) + 1

    new_rels, entries, index = [], [], 1
    for typeface, pitch, charset, slots in families:
        ids = {}
        for slot, filename in slots.items():
            part = f"font{index}.fntdata"
            shutil.copyfile(Path(font_dir) / filename, fonts_out / part)
            rid = f"rId{next_id}"
            new_rels.append(
                f'<Relationship Id="{rid}" Type="{REL_TYPE}" Target="fonts/{part}"/>'
            )
            ids[slot] = rid
            next_id += 1
            index += 1
        body = "".join(f'<p:{s} r:id="{r}"/>' for s, r in ids.items())
        entries.append(
            f'<p:embeddedFont><p:font typeface="{typeface}" pitchFamily="{pitch}" '
            f'charset="{charset}"/>{body}</p:embeddedFont>'
        )

    rels_path.write_text(
        rels.replace("</Relationships>", "".join(new_rels) + "</Relationships>"),
        encoding="utf-8",
    )

    ct_path = work / "[Content_Types].xml"
    ct = ct_path.read_text(encoding="utf-8")
    if "fntdata" not in ct:
        ct = re.sub(
            r"(<Types[^>]*>)",
            r'\1<Default Extension="fntdata" ContentType="application/x-fontdata"/>',
            ct,
            count=1,
        )
        ct_path.write_text(ct, encoding="utf-8")

    pres_path = work / "ppt/presentation.xml"
    pres = pres_path.read_text(encoding="utf-8")
    assert "<p:embeddedFontLst>" not in pres
    lst = "<p:embeddedFontLst>" + "".join(entries) + "</p:embeddedFontLst>"
    # Schema order: ... notesSz, smartTags, embeddedFontLst, custShowLst, ...
    for anchor in ("<p:custShowLst", "<p:defaultTextStyle", "</p:presentation>"):
        if anchor in pres:
            pres = pres.replace(anchor, lst + anchor, 1)
            break
    pres = pres.replace('saveSubsetFonts="1"', 'saveSubsetFonts="0"')
    if "embedTrueTypeFonts=" not in pres:
        pres = re.sub(
            r"(<p:presentation\b[^>]*?)(\s*>)", r'\1 embedTrueTypeFonts="1"\2', pres, count=1
        )
    if 'saveSubsetFonts=' not in pres:
        pres = re.sub(
            r"(<p:presentation\b[^>]*?)(\s*>)", r'\1 saveSubsetFonts="0"\2', pres, count=1
        )
    pres_path.write_text(pres, encoding="utf-8")

    out = Path(dst)
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for path in sorted(work.rglob("*")):
            if path.is_file():
                z.write(path, path.relative_to(work).as_posix())
    shutil.rmtree(work)
    print(f"  {dst}: {len(new_rels)} font slots embedded")


if __name__ == "__main__":
    ARCHIVO = ("Archivo", "34", "0", {
        "regular": "Archivo-Regular.ttf",
        "bold": "Archivo-Bold.ttf",
        "italic": "Archivo-Italic.ttf",
        "boldItalic": "Archivo-BoldItalic.ttf",
    })
    embed(sys.argv[1], sys.argv[2], [ARCHIVO], sys.argv[3])
