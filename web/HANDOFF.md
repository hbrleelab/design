# Handoff: HBRLRG Homepage

> 이 문서는 `hbrleelab/design` 저장소의 `web/` 폴더에 있습니다.
> 스타일시트는 `hbrlrg.css`, 참조 구현은 `index.html`, 로고·엠블럼은 `../assets/`.

## Overview

A redesign of **hbrl-research.group** (HBRL Research Group, UNIST) that shares one
visual system with the group's A4 document templates and 1920×1080 slide
template. The tagline and subject matter are unchanged; the point of the work is
to make the website, the letterhead, and the deck look like they came from the
same lab.

The page is a single scrolling homepage: hero → metrics → research → publications
→ people → facilities → news → recruiting CTA → footer.

## About the design files

**The HTML and CSS in this bundle are design references, not a drop-in build.**
`index.html` is a fully working static reference implementation — open it in a
browser and you see the intended result at every width. But the task is to
**recreate this design inside the existing hbrl-research.group codebase**, using
whatever framework, templating, and CMS it already runs on.

`hbrlrg.css` is the exception: it is written to be adopted more or less as-is.
It is plain CSS with custom properties, no build step, no preprocessor, no
framework assumptions. Import it, keep the class names, and feed it the site's
real content. If the site already has a stylesheet, load `hbrlrg.css` **after**
it and expect to delete competing rules rather than fight them with specificity.

## Fidelity

**High fidelity.** Colors, typography, spacing, and responsive behavior are
final and derived from the existing document/slide system. Copy is placeholder
where noted (§Content status). Recreate the visual result exactly; do not
re-interpret the palette or type scale.

## Files in this bundle

| File | What it is |
| --- | --- |
| `hbrlrg.css` | The design system. Tokens + components + responsive rules. Adopt as-is. |
| `index.html` | Reference implementation showing correct markup for every component. |
| `../assets/unist-emblem-onnavy.png` | UNIST emblem for navy backgrounds (official, white + teal on transparent). |
| `../assets/cm-logo-onnavy.png` | Chemistry of Materials logo (official). |



## Design tokens

All tokens are CSS custom properties on `:root` in `hbrlrg.css`. Use the
variables, not the literal values.

### Color

| Token | Value | Use |
| --- | --- | --- |
| `--hb-navy` | `#14243F` | Headings, rules, dark sections, primary text on light |
| `--hb-teal` | `#0EA79A` | The single accent: rule caps, bullets, CTA background, list indices |
| `--hb-teal-bright` | `#12C0B1` | Teal button hover only |
| `--hb-teal-deep` | `#0B6F66` | Caps and rules that sit *on* teal |
| `--hb-ink` | `#2B2F36` | Body copy on light |
| `--hb-muted` | `#6B7280` | Captions, meta, secondary copy on light |
| `--hb-faint` | `#9AA1AB` | Doc/slide footers. Shared token; unused on web. |
| `--hb-on-navy-muted` | `#93A2BC` | Secondary copy on navy — 6.01:1, the smallest allowed |
| `--hb-on-navy-rule` | `#2C4066` | Hairlines inside navy sections. **Never text.** |
| `--hb-surface` | `#F6F7F9` | Alternating section band, table headers, image wells |
| `--hb-border` | `#E4E7EC` | Standard hairline |
| `--hb-border-soft` | `#F0F1F4` | Nested list dividers |

Only **three section backgrounds** exist: white, `--hb-surface`, and
`--hb-navy` — plus `--hb-teal` used exactly once, for the recruiting CTA. Do
not add a fourth.

**Dark contexts.** Four selectors carry a navy background: `.hb-section--navy`,
`.hb-section--teal`, `.hb-hero`, and `.hb-bleed`. All four appear in the
inversion rules for headings, leads, eyebrows, and the wordmark. If you add a
fifth dark container, add it to those selector lists too — otherwise the base
`h1–h4 { color: var(--hb-navy) }` wins and the heading disappears.

### Typography

Two families, strictly divided:

- **Archivo** (300/400/500/600) — Latin text, all headings, numerals, eyebrows,
  table labels, the wordmark.
- **Pretendard** (400/500/600) — Korean body text.

Archivo carries no Hangul, so Korean falls through to Pretendard automatically
via the font stack. Add `.hb-kr` only when you want Pretendard's metrics to
drive a whole block (a Korean heading, a mixed paragraph).

The scale is fluid via `clamp()` and is applied directly to `h1`–`h4`, so
semantic headings size themselves — no class needed. `.hb-display` is only for
the hero, which needs the display size on an `h1` that also caps its measure at
22ch. Mobile value on the left, desktop on the right:

| Token | Range | Role |
| --- | --- | --- |
| `--hb-fs-display` | 38 → 76px | Hero H1 |
| `--hb-fs-h2` | 32 → 52px | Section headings |
| `--hb-fs-h3` | 23 → 30px | Card and list headings |
| `--hb-fs-lead` | 17 → 23px | Lead paragraphs |
| `--hb-fs-body` | 16 → 18px | Body copy |
| `--hb-fs-metric` | 38 → 56px | Big numerals (weight 300) |
| `--hb-fs-eyebrow` | 13 → 14px | Section eyebrows |
| `--hb-fs-xs` | 14px | Smallest size allowed on light backgrounds |

Letter-spacing tightens as size grows: `-0.025em` on display, `-0.02em` on H2,
`0` on body. Eyebrows go the other way: `+0.16em`, uppercase.

### Spacing

4px base. Tokens `--hb-1` (4px) through `--hb-26` (104px). Section padding and
gutters are themselves tokens that change at breakpoints:

| Token | 390px | 768px | 1200px |
| --- | --- | --- | --- |
| `--hb-gutter` | 20px | 32px | 56px |
| `--hb-section-y` | 56px | 80px | 104px |
| `--hb-header-h` | 56px | 68px | 76px |
| `--hb-cap-w` × `--hb-cap-h` | 64×4px | 76×5px | 88×5px |

### Geometry

`--hb-radius: 0`. **Square corners everywhere** — buttons, cards, chips, image
wells, photos. The one exception is `--hb-radius-dot: 2px` on the small teal
bullet squares, and the wordmark bars' own `rx`. This is deliberate and is what
ties the site to the printed templates; do not soften it.

## The signature elements

Three marks carry the identity across web, document, and slide. Get these right
and the rest follows.

### 1. The rule cap

A hairline spanning the measure with a teal cap at its left end.

```html
<div class="hb-rule"></div>       <!-- full rule with cap -->
<div class="hb-cap"></div>         <!-- cap alone, above a heading -->
```

`.hb-rule` draws a 2px navy line (`::before`) with an 88×5px teal block at its
left end (`::after`). `.hb-rule--soft` swaps the navy line for `--hb-border`.

**Appears once per section band.** Never twice in one band, never centered,
never mirrored to the right.

### 2. The wordmark

The supplied logo file — an interlocking symbol plus the HBRLRG wordmark. **Never
re-draw it in markup.**

```html
<a class="hb-wordmark" href="/" aria-label="HBRL Research Group — home">
  <img src="assets/logo/hbrlrg-horizontal.png" alt="HBRLRG">
</a>
```

Two variants, and you pick by **swapping the source, not the colour**:

| Context | File |
| --- | --- |
| Light backgrounds | `hbrlrg-horizontal.png` (or `.svg`) |
| Navy sections, footer, photography | `hbrlrg-horizontal-reverse.png` |

Aspect ratio is fixed at **573.5 : 169.1** (3.39 : 1) — set `height` only; the CSS
carries a matching `aspect-ratio` so an unresolved intrinsic size can't collapse
the image. Minimum width is 120 px. Do not recolour, rotate, add effects, or place
the mark on a busy area of a photograph.

`assets/logo/` also carries vertical, mono, symbol-only, icon, and favicon
variants; `assets/logo/README.txt` has the construction spec.

### 3. The bullet square

A teal square (9–16px, `border-radius: 2px`) aligned to the **center of the
first text line**, not to its top.

```html
<div class="hb-bullets">
  <div class="hb-bullet"><p>…</p></div>
</div>
```

The `margin-top` on `.hb-bullet::before` is computed as
`(font-size × line-height ÷ 2) − (dot ÷ 2)`. If you change a bullet's font
size, recompute it — a bullet that sits a few pixels high is the most visible
way this system breaks.

## Components

Each is documented inline in `hbrlrg.css` with a numbered section comment.
`index.html` shows correct markup for all of them.

| Section | Class | Notes |
| --- | --- | --- |
| 4 | `.hb-page`, `.hb-section`, `.hb-section--surface/navy/teal` | Layout shells. Dark variants auto-invert headings and leads. |
| 5 | `.hb-rule`, `.hb-cap` | Signature rule. |
| 6 | `.hb-eyebrow`, `.hb-section-head`, `.hb-lead`, `.hb-display` | Section headers. |
| 7 | `.hb-btn` + `--primary/navy/outline/invert/block`, `.hb-link-more` | 52px min-height; `--block` is full-width on mobile only. |
| 8 | `.hb-header`, `.hb-wordmark`, `.hb-nav`, `.hb-burger` | Sticky, blurred. Nav appears at 900px; burger below. |
| 9 | `.hb-hero`, `.hb-affil` | Mobile: image band on top, text overlapping up by 16px. Desktop (900px+): CSS grid, text left, image in a 39.3% right column with a horizontal gradient. |
| 10 | `.hb-metrics`, `.hb-metric` | 2-up → 4-up at 900px. Numerals are weight 300, tabular. |
| 11 | `.hb-numlist`, `.hb-tag` | Mobile: divider rows. Desktop: 2-up grid using a 1px `--hb-border` background with white cells — the hairlines *are* the grid gap. |
| 12 | `.hb-pubs`, `.hb-pub` | Mobile: year · journal, title, authors stacked. Desktop (1000px+): 3 columns via `display:contents` on `.hb-pub__meta`. The inline journal is hidden and the third-column one shown. |
| 13 | `.hb-pi`, `.hb-credential`, `.hb-linklist`, `.hb-members` | PI block goes 1-col → 392px + fluid at 1000px. Members 2-up → 4-up. |
| 14 | `.hb-bleed` | Full-bleed image with gradient; vertical on mobile, horizontal on desktop. |
| 15 | `.hb-bullets`, `.hb-bullet` | See §Signature elements. |
| 16 | `.hb-news` | Divider rows → 3-up hairline grid at 900px. |
| 17 | `.hb-table`, `.hb-caption`, `.hb-table-scroll` | **No vertical rules, ever.** Header on `--hb-surface` with uppercase labels; rows carry a bottom hairline only. Wrap wide tables in `.hb-table-scroll`. |
| 18 | `.hb-footer` | Mobile: stacked, link columns 2-up. Desktop: `1fr 200px 200px` — `.hb-footer__cols` becomes `display:contents` so the columns join the parent grid. |
| 19 | `.hb-well` | Image placeholder. `.hb-well--empty` renders its `data-label` as centered gray text. **Remove `--empty` once a real `<img>` is inside.** |
| 20 | `.hb-measure`, `.hb-tnum`, `.hb-visually-hidden`, `.hb-skip` | Utilities. `.hb-skip` is the keyboard skip link — keep it first in `<body>`. |
| 21 | `@media print` | Strips chrome and dark backgrounds so any page prints legibly. |

## Responsive behavior

Mobile-first. Base rules are the 390px layout; three breakpoints up.

| Breakpoint | What changes |
| --- | --- |
| **768px** | Gutter 20→32px, section padding 56→80px, cap 64×4→76×5px, hero actions go horizontal, `.hb-btn--block` stops being full-width. |
| **900px** | Nav replaces burger. Hero becomes a 2-column grid with the image bleeding right. Metrics 2-up→4-up, research 1-col→2-up, news 1-col→3-up, members 2-up→4-up. Bleed gradient turns horizontal. |
| **1000px** | Publications become a 3-column table. PI block becomes 392px + fluid. Footer becomes `1fr 200px 200px`. |
| **1200px** | Gutter 32→56px, section padding 80→104px, cap 76→88px wide, wordmark 19→23px. |

Content is capped at `--hb-max: 1440px` and centered. Verify at 390, 768, 1024,
1440, and 1920px.

## Accessibility

These were fixed during review — please don't regress them.

- **Every interactive element is at least 44px tall.** Link stacks (PI contacts,
  footer columns, nav items, the wordmark) use
  `display:flex; align-items:center; min-height:var(--hb-tap)` with reduced
  column `gap` to keep the visual rhythm. Bare 15px text in a `gap`-spaced
  stack gives an 18px hit box — that was the original bug.
- **`#0EA79A` teal is 2.99:1 on white.** It is fine for rule caps, bullets, and
  large numerals, but **not for small text**. Eyebrows and news dates are navy
  and `--hb-muted` respectively. Teal eyebrows are allowed only on navy.
- **`#2C4066` is a hairline color, not a text color** (3.98:1 on navy). Small
  text on navy uses `--hb-on-navy-muted` (6.01:1).
- **`#D6F2EF` on teal is 2.54:1** — decorative only. The CTA paragraph is white.
- `:focus-visible` gives a 2px teal outline at 3px offset on every link and
  button. Keep it.
- `prefers-reduced-motion` collapses all transitions.
- Section landmarks carry `id`s matching the nav anchors; `.hb-skip` targets
  `#main`.

## Assets

| File | Origin | Notes |
| --- | --- | --- |
| `unist-emblem-onnavy.png` | UNIST official emblem, recolored | Navy ground removed to transparency; cyan elements shifted to `--hb-teal`; letterforms knocked out white. **Use only on navy or dark photography.** For light backgrounds, request the official emblem in its standard colors from the university. 1000×1000. |
| `cm-logo-onnavy.png` | Chemistry of Materials (ACS) logo, recolored | Gray box → `--hb-teal`, "cm" letters → `--hb-navy` knockout, wordmark → white. 632×316. |

Photography is **not** included. Seven image wells are marked with
`.hb-well--empty` and a `data-label` describing what belongs there:

1. Hero — wafer or reactor photograph
2. PI portrait
3.–6. Four member portraits
7. Facilities — reactor cluster or cleanroom

Ship real photography before launch; the gray wells are scaffolding, not a
design choice.

> **Note on the ACS logo:** confirm with ACS that a recolored form of the
> *Chemistry of Materials* mark is acceptable for use on a personal/lab site
> before publishing. If not, use the unmodified official logo on a white plate.

## Content status

| Section | Status |
| --- | --- |
| Hero H1 + tagline | Tagline is the site's real meta description. H1 is proposed copy — confirm. |
| Metrics (120+, 18, 6, 2011) | **Placeholder.** Replace with real figures. |
| Research areas (4) | Titles and framing proposed; verify they match the group's actual thrusts. |
| Publications (4) | **Placeholder — fabricated titles, authors, journals.** Replace with real records and DOIs before launch. |
| People (PI + 4 members) | PI role and affiliation are correct. The four members are **placeholder names**. |
| Facilities (4 bullets) | **Placeholder.** Verify reactor count and instrument list. |
| News (3) | **Placeholder.** |
| Contact / recruiting | Proposed copy; confirm tone and positions. |
| Affiliation string | Correct and canonical — see below. |

### Affiliation — exact strings

Do not abbreviate or reorder these.

- **English:** Professor, Graduate School of Semiconductor Materials & Devices Engineering, Ulsan National Institute of Science and Technology (UNIST)
- **Korean:** 울산과학기술원(UNIST) 반도체소재부품대학원 교수
- **Editorial role:** Executive Editor, Chemistry of Materials, ACS Publications
- **Address:** 50 UNIST-gil, Ulju-gun, Ulsan 44919, Republic of Korea
- **Email:** hbrlee@unist.ac.kr

## Interactions

Deliberately restrained — this is a research site, not a product page.

- **Hover:** links go navy → teal; grid cells (research, news, publications) go
  white → `--hb-surface`; buttons swap background. All at 160ms
  `cubic-bezier(0.4, 0, 0.2, 1)`.
- **Header:** `position: sticky` with `backdrop-filter: blur(12px)` over
  `rgb(255 255 255 / 0.95)`.
- **Mobile menu:** the burger is markup-only in this bundle. Wire it to whatever
  pattern the site already uses (full-screen overlay recommended, navy
  background, 44px rows, reuse `.hb-nav__link`). Toggle `aria-expanded`.
- **Current page:** set `aria-current="page"` on the active `.hb-nav__link` —
  the CSS already styles it with the teal underline.
- No scroll animations, parallax, or reveal effects. Don't add them.

## Suggested implementation order

1. Load the two fonts and `hbrlrg.css`; confirm tokens resolve
   (`getComputedStyle(document.body).getPropertyValue('--hb-navy')`).
2. Header + footer — they appear on every page and exercise the wordmark,
   nav, tap targets, and dark-section inversion.
3. Homepage sections top to bottom, checking each at 390 / 900 / 1440px before
   moving on.
4. Replace image wells with real photography; drop `.hb-well--empty`.
5. Wire publications, news, and people to the CMS or data source.
6. Mobile menu behavior.
7. Audit: tap targets ≥44px, contrast, keyboard tab order, print preview.

## Reference

- Live site: https://hbrl-research.group
- Design system reference (documents + slides): `Document Design System.dc.html`
  in the parent project
- Sibling templates that must stay visually consistent:
  `Letterhead Document (KR/EN)`, `Plain Document (KR/EN)`, `Slide Template (KR/EN)`
