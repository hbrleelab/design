---
name: hbrlrg-design
description: >-
  The HBRL Research Group (UNIST) visual design system — Navy/Teal colour tokens,
  Archivo + Pretendard type, and the lab's slide, document, and web templates.
  Use this whenever you are making or restyling anything that carries the lab's
  identity, including presentation slides and PPTX decks, A4 documents and
  letterheads, posters, figures, and the group homepage, or for any request
  mentioning HBRL, HBRLRG, "our lab design", "연구실 디자인", or "랩 템플릿".
  Also use it when asked to swap fonts or colours in an existing deck to match a
  house style, or to embed fonts into a .pptx — the bundled scripts and recorded
  pitfalls save hours of rediscovery.
---

# HBRLRG Design System

The lab's identity across slides, documents, and web. Everything here is derived
from the canonical templates in `assets/templates/`, which are the same files
students download from https://github.com/hbrleelab/design/releases/latest.

When a task touches an existing artefact, prefer restyling it onto these tokens
over rebuilding it — the layout usually encodes decisions you cannot see.

## The two rules that hold it together

Every other decision is downstream of these:

1. **One accent.** Teal `#0EA79A` is the only accent, and it earns its place —
   divider caps, bullets, one CTA. A second accent colour makes the whole system
   read as generic.
2. **Square corners.** `border-radius: 0` everywhere except the logo bars. Rounded
   cards are the fastest way to make lab material look like a stock template.

## Tokens

| Token | Value | Used for |
|---|---|---|
| Navy | `#14243F` | names, titles, dividers, logo body |
| Teal | `#0EA79A` | the single accent — divider caps, bullets, RG in the wordmark |
| Ink | `#2B2F36` | body text |
| Muted | `#6B7280` | contact lines, captions, metadata |
| Surface | `#F6F7F9` | table header fill, panel fill |
| Hairline | `#E4E7EC` | table rules, divider base |

On a navy ground the text ramp changes: `#93A2BC` for secondary, `#6E82A3` for
tertiary (dates), `#2C4066` for hairlines, white for primary.

**Type.** Archivo for Latin — logo wordmark, English headings, dates, numerals,
table labels. Pretendard for all Korean body text; Korean automatically falls
back to Pretendard even inside a run marked Archivo, so pair them rather than
choosing between them. Weights in use: Archivo 300/400/500/600, Pretendard
400/500/600.

Both are SIL OFL 1.1, free to embed and redistribute:
- Archivo — https://github.com/Omnibus-Type/Archivo (`fonts/ttf/`). The repo also
  ships condensed and expanded widths; the system uses only the normal width.
- Pretendard — https://github.com/orioncactus/pretendard/releases (static `.otf`)

The HTML templates pull both from CDN, so nothing needs installing to open them.
Install locally only for PowerPoint/Word, figure tools, or offline use.

## Affiliation block

Never shortened or reordered — this is how the group is cited:

- **EN** Professor, Graduate School of Semiconductor Materials & Devices Engineering, Ulsan National Institute of Science and Technology (UNIST)
- **KR** 울산과학기술원(UNIST) 반도체소재부품대학원 교수
- **Editorial** Executive Editor, Chemistry of Materials, ACS Publications
- **Address** 50 UNIST-gil, Ulju-gun, Ulsan 44919, Republic of Korea

On slides the affiliation is set one line shorter: `Professor, Graduate School of
Semiconductor Materials & Devices Engineering, UNIST`.

## The HBRLRG wordmark

Four stacked bars plus the word. The top bar is teal; the rest take the
foreground colour (navy on light, white on navy). `RG` is always teal.

```html
<span style="display:inline-flex;align-items:baseline;gap:0.15em;font-size:26px;">
  <svg viewBox="10 15 40 30.5" style="height:0.7em;width:auto;flex:0 0 auto;">
    <rect x="10" y="15" width="40" height="3.5" rx="1.75" fill="#0EA79A"/>
    <rect x="10" y="24" width="40" height="3.5" rx="1.75" fill="#14243F"/>
    <rect x="10" y="33" width="40" height="3.5" rx="1.75" fill="#14243F"/>
    <rect x="10" y="42" width="40" height="3.5" rx="1.75" fill="#14243F"/>
  </svg>
  <span style="font-family:'Archivo',sans-serif;font-weight:300;letter-spacing:-0.033em;">
    <span style="color:#14243F;">HBRL</span><span style="color:#0EA79A;">RG</span>
  </span>
</span>
```

Logos live in `assets/logos/`: `unist-emblem.png` (light grounds),
`unist-emblem-onnavy.png` and `cm-logo-onnavy.png` (navy grounds).

## What to read next

- **`references/slides.md`** — slide anatomy: the 1920×1080 grid, header block,
  teal-capped divider, bullets, footer, and the cover layout. Read this before
  building or restyling any deck.
- **`references/documents.md`** — A4 letterhead and plain-document rules, print
  behaviour, and how the HTML templates are meant to be used.
- **`references/pptx.md`** — restyling a real `.pptx` onto this system: the
  token map, font embedding, and the traps that cost real time (python-pptx
  silently drawing borders, PowerPoint refusing `.otf`). Read this whenever a
  `.pptx` is involved.

## Bundled templates and scripts

`assets/templates/` holds the canonical, working files — open them to see any
rule in context rather than reconstructing it:

`slides-en.html` (12 layouts, 1920×1080) · `letterhead-{kr,en}.html` ·
`plain-{kr,en}.html` · `hbrlrg.css` (homepage) · `deck-stage.js` (deck viewer)
· `image-slot.js` (drag-and-drop figure wells) · `doc-page.js` (A4 print engine)

`scripts/` holds three things worth not rewriting:

| Script | Use |
|---|---|
| `otf2ttf.py in.otf out.ttf` | CFF to TrueType, because PowerPoint embeds TrueType only |
| `embed_fonts.py in.pptx out.pptx <font-dir>` | writes `ppt/fonts/*.fntdata` plus all the package bookkeeping |
| `qa_fit.py deck.pptx` | text-overflow, off-slide and collision check using real font metrics |

`qa_fit.py` exists because a renderer is often unavailable — it measures wrapped
line counts against the actual Archivo advance widths, which catches overflow
more precisely than squinting at a thumbnail.

## Applying the system to something new

Match the medium's own conventions first, then apply the tokens. A poster is not
a slide; a figure caption is not body text. What stays constant across every
medium is the pair of rules at the top, the affiliation block, and the wordmark.

When density fights the template — an industry talk carrying far more per slide
than the template's four bullets — keep the tokens and the page furniture, and
let the type scale down. Do not add a second accent to create hierarchy that
size should be carrying.
