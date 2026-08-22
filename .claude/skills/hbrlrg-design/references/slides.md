# Slide anatomy

The master is **1920 × 1080 px** on a 13.333 × 7.5 in stage, which makes the
conversion arithmetic worth memorising:

- **144 px per inch** → `inches = px / 144`
- **1 px of type = 0.5 pt** → `pt = px / 2`

So the 60 px heading below is 30 pt in PowerPoint, and the 120 px side margin is
0.833 in.

> ⚠️ Those two divisions apply when moving to a **13.333 in stage** (PowerPoint).
> Keynote documents set to 1920 × 1080 use those numbers as their own unit, so
> type sizes go in **1:1** there — halving them renders everything at half size.

`../assets/templates/slides-en.html` is the working reference — 12 layouts:
Title · Agenda · Section · Content · Figure (full) · Figure (two up) ·
Figure + text · Data · Metrics · Full-bleed image · Statement · Closing.

**These coordinates were measured from a delivered deck** (2026-08-21, Applied
Materials invited talk) rather than authored in the abstract. Where the deck and
an earlier draft of this document disagreed, the deck won.

## Content slide

Side margins are **120 px** left and right on every slide. Four bands:

**Eyebrow row** — at `top: 52px`. An **88 × 5 px teal cap at x=120** and the
eyebrow label **beside it at x=232** (24 px gap), on one line:

- *Eyebrow* — 24 px, weight 500, `letter-spacing: 0.14em`, teal, uppercase.
  Reads like `03 · PROCESS OPTIMIZATION` or `FRAMEWORK 01 · IDEAL`. It is what
  tells the audience where they are in the talk; without it a run of content
  slides feels undifferentiated. Separator is a **middle dot**, not an em dash.

The teal cap is the system's signature. It sits *left of the eyebrow* — not
under the heading as a full-width rule.

**Heading** — at `top: 98px`, Archivo 600, 60 px, `line-height: 1.1`,
`letter-spacing: -0.018em`, navy, `max-width: 34ch`. One line is the design
intent; two lines collide with the subtitle.

**Subtitle** — at `top: 192px`, 28 px, muted `#6B7280`, `max-width: 52ch`.
One sentence that unpacks the heading. Used on **21 of 24 slides** in the
reference deck — treat it as standard, not optional decoration.

**Body** — starts at `top: 268px`, bottom margin 132 px (so the band is
1680 × 680). Bullets are a 14 × 14 px teal square (the one place a 4 px radius
is allowed) with a 22 px gap, against 34 px text at `line-height: 1.4` in ink,
`max-width: 52ch`.

The body deliberately leaves the lower half open on text slides. Research slides
get a plot or micrograph pasted in later, and reserving that space beats
reflowing text around a figure after the fact.

**Footer** — at `top: 1004px`, spanning the same 120 px margins:

| Element | Position | Type |
|---|---|---|
| Wordmark | bars at `120`, text at `158` | 26 px |
| Contact | `972` | 24 px, `#9AA1AB`, separator dot `#D2D6DD` |
| Page number | `1728`, right-aligned | 24 px, `#9AA1AB` |

## Cover slide

Navy `#14243F` full bleed. Positions are from the top-left:

| Element | Position | Type |
|---|---|---|
| Eyebrow | `120, 226` | 24 px, teal, uppercase, `letter-spacing: 0.14em`. **Carries venue and date** — `INVITED TALK · APPLIED MATERIALS · AUGUST 21, 2026` |
| Teal bar | `120, 290` | 130 × 8 px |
| Heading | `120, 328` | Archivo 600, 68 px, `line-height: 1.02`, `letter-spacing: -0.025em`, white, `max-width: 42ch` |
| Subtitle | `120, 434` | 50 px, `#93A2BC` |
| Hairline | `120, 578` | 2 px, `#2C4066`, full column |
| Name | `120, 626` | 48 px, weight 600, white |
| UNIST emblem | `120, 692` | 116 × 120 px |
| Affiliation | `270, 720` | 26 px `#93A2BC`, width 648 |
| CM logo | `944, 722` | 216 × 60 px |
| Editorial | `1202, 720` | 26 px `#93A2BC`, width 598 |
| Wordmark | `120, 960` | 26 px, bars white, RG teal |
| Contact line | `792, 972` | 24 px `#6E82A3` |

There is **no separate date element** — the date lives in the eyebrow.

A heading longer than roughly 42 characters per line wraps; check it clears the
subtitle at 434 rather than trusting the nominal box height. 68 px was chosen
over something larger precisely because conference titles run long — at 108 px a
typical talk title breaks to two lines.

## The wordmark

Four stacked bars plus the word, laid out as **28 × 2 px bars with 6 px vertical
pitch**, the word starting **38 px** right of the bars. The top bar is teal; the
rest take the foreground colour (navy on light, white on navy). `RG` is always
teal.

In HTML use the SVG in `SKILL.md`. When drawing through an API with no SVG
support — Keynote AppleScript, for instance — four filled rectangles at the
pitch above reproduce it exactly.

## Figures

Figure wells (`image-slot.js`) accept a dragged-in plot or micrograph and keep
the aspect ratio. Text inside a figure stays English even on Korean slides, so
the same figure can be reused in papers and talks.

**Fit research figures with `contain`, not `cover`.** The well's default framing
crops to fill, which silently cuts axes, legends and scale bars off a plot.
Letterboxing is the correct behaviour for data; the Surface fill `#F6F7F9`
absorbs the margins cleanly. Reserve `cover` for photographs and full-bleed
imagery.

Slot rectangles in `slides-en.html` (1680 × 680 content band):

| Layout | Slot | Aspect |
|---|---|---|
| Figure — full | 1680 × 630 (caption 34 + gap 16 below) | 2.67 |
| Figure — two up | 816 × 630, columns at x=120 and x=984 | 1.30 |
| Figure + text | 1084 × 680, text column x=1252 w=548 | 1.59 |
| Full-bleed | 1920 × 1080 | 1.78 |

A real deck places figures freely rather than snapping to these; the rectangles
are a starting point, not a constraint. Note that **Figure — full at 2.67:1 is
much wider than most research figures** — a 4:3 plot letterboxed into it leaves
large side margins. Two-up and Figure + text fit ordinary plots better.
