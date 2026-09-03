# Documents

Two A4 templates, each in Korean and English:
`letterhead-{kr,en}.html` for outgoing correspondence, `plain-{kr,en}.html` for
everything else. Both live in `../assets/kit/documents/`.

## How they are meant to be used

Open the file in a browser, edit the text directly on the page, then print
(⌘P / Ctrl+P) and **Save as PDF**. There is no build step and no Word round-trip.

`doc-page.js` owns the A4 geometry — an 18 mm margin and automatic page breaks.
Do not add `@page` rules of your own; the engine already sets them, and a second
set produces margins that disagree between screen and print.

## Type

Pretendard carries Korean body text, Archivo carries Latin, and the two are
declared together so mixed text resolves per-character rather than forcing one
font onto both scripts. Set body at the template's size — documents are read at
arm's length, so the slide scale does not transfer.

Tables use `#F6F7F9` for the header fill and `#E4E7EC` for rules. Square corners,
as everywhere.

## Letterhead

The letterhead block carries the name, the affiliation, and the editorial title
for *Chemistry of Materials*, plus the phone/e-mail/URL line in muted grey. Treat
the affiliation strings in `SKILL.md` as fixed text — they are how the group is
cited, and shortening them on a letter is a real error rather than a style choice.

The UNIST emblem on a light ground is `assets/kit/assets/unist-emblem.png`.

## When a Word or PowerPoint file is unavoidable

Collaborators sometimes need an editable Office file. Export from the HTML rather
than maintaining a parallel `.docx` — a binary source cannot be diffed, bloats the
repository, and renders differently across Office versions. The Office file is an
output, not the source.
