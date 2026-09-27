"""Validate a .pptx or .docx against the official ISO/IEC 29500-4 schemas.

A schema-invalid part is what makes Office show "repair" instead of opening the
file, and nothing in python-pptx or python-docx checks for it — they will write
an out-of-range attribute without complaint. v1.9 shipped `charset="129"` on an
embedded font (xsd:byte is signed, so the value had to be -127) and PowerPoint
refused the deck. This catches that class of fault before a release goes out.

    python3 qa_schema.py file.pptx [file.docx ...]

Exits non-zero on the first invalid part, so it works as a build gate.

It validates the XML, not the rendering: a file that passes here is well-formed
per the standard, which is necessary for Office to open it but does not prove
any particular version will lay it out as intended.
"""
import io
import posixpath
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

from lxml import etree

# Shipped with the Office document skills; the ISO release of the OOXML schemas.
SCHEMA_DIRS = [
    Path("/mnt/skills/public/pptx/scripts/office/schemas/ISO-IEC29500-4_2016"),
    Path("/mnt/skills/public/docx/scripts/office/schemas/ISO-IEC29500-4_2016"),
    Path(__file__).resolve().parent / "schemas",
]

# Every part we generate or rewrite, matched by pattern so new slides are
# covered automatically rather than when someone remembers to list them.
PARTS = {
    "pml.xsd": r"ppt/(presentation\.xml|(slides|slideLayouts|slideMasters)/[\w]+\.xml)$",
    "wml.xsd": r"word/(document|fontTable|settings|footer\d+|header\d+|styles)\.xml$",
}


MCE_NS = "http://schemas.openxmlformats.org/markup-compatibility/2006"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
REL_ID = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
FONT_KEY = "{%s}fontKey" % W_NS
SETTINGS_ORDER = [
    "writeProtection", "view", "zoom", "removePersonalInformation",
    "removeDateAndTime", "doNotDisplayPageBoundaries",
    "displayBackgroundShape", "printPostScriptOverText",
    "printFractionalCharacterWidth", "printFormsData",
    "embedTrueTypeFonts", "embedSystemFonts", "saveSubsetFonts",
    "saveFormsData", "mirrorMargins", "alignBordersAndEdges",
    "bordersDoNotSurroundHeader", "bordersDoNotSurroundFooter",
    "gutterAtTop", "hideSpellingErrors", "hideGrammaticalErrors",
    "activeWritingStyle", "proofState",
]


def strip_mce(doc):
    """Apply Markup Compatibility preprocessing before validating.

    ISO 29500-3 lets a part declare namespaces a reader may ignore, and every
    file Office writes uses this (w14, w15 and so on). The strict Part 4 schemas
    do not declare them, so without this step each extension shows up as a
    spurious error and buries the real ones. A conforming consumer discards
    ignorable markup first; this does the same.
    """
    root = doc.getroot()
    ignorable = root.get("{%s}Ignorable" % MCE_NS, "")
    drop = {root.nsmap[p] for p in ignorable.split() if p in root.nsmap}
    for el in list(doc.iter()):
        for name in list(el.attrib):
            ns = name[1:].split("}")[0] if name.startswith("{") else None
            if ns == MCE_NS or ns in drop:
                del el.attrib[name]
        if isinstance(el.tag, str) and el.tag.startswith("{"):
            if el.tag[1:].split("}")[0] in drop and el.getparent() is not None:
                el.getparent().remove(el)



# --- checks that need no schema, so they also run on a CI runner ------------
BYTE_ATTRS = ("charset", "pitchFamily")
FONT_EXT = {".fntdata", ".odttf"}


def structural(path):
    """The faults that make Office offer "repair", checked without the XSDs.

    Narrower than schema validation, but it runs anywhere and covers everything
    these scripts actually write: out-of-range byte attributes, settings in the
    wrong sequence order, dangling relationships, and corrupt font parts.
    """
    z = zipfile.ZipFile(path)
    names = set(z.namelist())
    bad = []

    for part in sorted(n for n in names if n.endswith((".xml", ".rels"))):
        try:
            root = etree.fromstring(z.read(part))
        except etree.XMLSyntaxError as e:
            bad.append(f"{part}: XML 파손 — {e}")
            continue

        # xsd:byte is signed. The Windows charset id for Hangul is 129, which
        # has to be written -127; 129 is what broke v1.9.
        for el in root.iter():
            for attr in BYTE_ATTRS:
                v = el.get(attr)
                if v is not None and not -128 <= int(v) <= 127:
                    bad.append(f"{part}: {attr}=\"{v}\" 가 xsd:byte 범위 밖 "
                               f"(-128..127) — Office 가 파일을 거부합니다")

        # Sequence order in CT_Settings.
        if part.endswith("word/settings.xml"):
            order, seen = SETTINGS_ORDER, []
            for el in root:
                tag = etree.QName(el).localname
                if tag in order:
                    seen.append((order.index(tag), tag))
            for (a, ta), (b, tb) in zip(seen, seen[1:]):
                if a > b:
                    bad.append(f"{part}: <w:{ta}> 가 <w:{tb}> 앞에 있음 — "
                               f"CT_Settings 순서 위반")

        # Every r:id has to resolve in the matching .rels part.
        rids = {el.get(REL_ID) for el in root.iter() if el.get(REL_ID)}
        if rids:
            d, base = part.rsplit("/", 1) if "/" in part else ("", part)
            rels_part = f"{d}/_rels/{base}.rels" if d else f"_rels/{base}.rels"
            declared = set()
            if rels_part in names:
                declared = {r.get("Id") for r in etree.fromstring(z.read(rels_part))}
            for rid in sorted(rids - declared):
                bad.append(f"{part}: r:id={rid} 에 대응하는 관계가 없음")

    # Relationship targets must exist, and font parts must be real fonts.
    for rels_part in sorted(n for n in names if n.endswith(".rels")):
        base = rels_part.rsplit("_rels/", 1)[0]
        for rel in etree.fromstring(z.read(rels_part)):
            tgt = rel.get("Target")
            if rel.get("TargetMode") == "External" or not tgt:
                continue
            # Targets are relative to the part's own folder and usually climb
            # out of it ("../media/x.png"), so they have to be normalised.
            resolved = (tgt.lstrip("/") if tgt.startswith("/")
                        else posixpath.normpath(base + tgt))
            if resolved not in names:
                bad.append(f"{rels_part}: Target={tgt} 파트가 없음")

    ct = z.read("[Content_Types].xml").decode()
    for n in sorted(names):
        ext = PurePosixPath(n).suffix.lower()
        if ext in FONT_EXT and f'Extension="{ext.lstrip(".")}"' not in ct:
            bad.append(f"[Content_Types].xml: {ext} 기본 형식 선언 없음")

    for n in sorted(n for n in names if PurePosixPath(n).suffix.lower() in FONT_EXT):
        data = z.read(n)
        if n.endswith(".odttf"):
            key = font_key_for(z, n)
            if key is None:
                bad.append(f"{n}: w:fontKey 를 찾을 수 없어 검증 불가")
                continue
            mask = bytes.fromhex(key.strip("{}").replace("-", ""))[::-1]
            data = bytes(b ^ mask[i % 16] for i, b in enumerate(data[:32]))
        if data[:4] not in (b"\x00\x01\x00\x00", b"true", b"OTTO", b"ttcf"):
            bad.append(f"{n}: 유효한 폰트가 아님 (sfnt 서명 {data[:4]!r})")

    return bad


def font_key_for(z, part):
    """Find the w:fontKey that obfuscates this .odttf part."""
    try:
        rels = etree.fromstring(z.read("word/_rels/fontTable.xml.rels"))
        ft = etree.fromstring(z.read("word/fontTable.xml"))
    except KeyError:
        return None
    want = part.split("word/", 1)[1]
    rid = next((r.get("Id") for r in rels if r.get("Target") == want), None)
    for el in ft.iter():
        if el.get(REL_ID) == rid:
            return el.get(FONT_KEY)
    return None


def schema_dir():
    """The ISO schemas if this machine has them; None is not an error.

    They ship with the Office document skills and are not vendored here — they
    are ISO material and this is a public repository. Where they are missing,
    the structural checks still run.
    """
    for d in SCHEMA_DIRS:
        if (d / "pml.xsd").exists():
            return d
    return None


def check(path, root):
    z = zipfile.ZipFile(path)
    names = set(z.namelist())
    failures, checked = structural(path), 0
    for xsd, pattern in ({} if root is None else PARTS).items():
        present = sorted(n for n in names if re.match(pattern, n))
        if not present:
            continue
        schema = etree.XMLSchema(etree.parse(str(root / xsd)))
        for part in present:
            doc = etree.parse(io.BytesIO(z.read(part)))
            strip_mce(doc)
            checked += 1
            if not schema.validate(doc):
                for e in schema.error_log:
                    failures.append(f"{part}: {e.message}")
    name = Path(path).name
    how = f"스키마 {checked}개 파트 + 구조 검사" if root is not None else "구조 검사"
    if failures:
        print(f"  {name}: 실패 ({how})")
        for f in failures:
            print(f"      {f}")
        return False
    print(f"  {name}: 통과 ({how})")
    return True


if __name__ == "__main__":
    root = schema_dir()
    if root is None:
        print("ISO 스키마 없음 — 구조 검사만 수행합니다 "
              "(전체 검증은 Office 스킬이 설치된 환경에서)")
    if all(check(p, root) for p in sys.argv[1:]):
        print("모두 통과")
    else:
        raise SystemExit(1)
