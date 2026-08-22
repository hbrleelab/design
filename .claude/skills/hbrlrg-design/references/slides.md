# Slide anatomy

The master is **1920 × 1080 px** on a 13.333 × 7.5 in stage, which makes the
conversion arithmetic worth memorising:

- **144 px per inch** → `inches = px / 144`
- **1 px of type = 0.5 pt** → `pt = px / 2`

So the 60 px heading below is 30 pt in PowerPoint, and the 120 px side margin is
0.833 in. Anything specified here in px translates to any tool with those two
divisions.

`../assets/templates/slides-en.html` is the working reference — 12 layouts:
Title · Agenda · Section · Content · Figure (full) · Figure (two up) ·
Figure + text · Data · Metrics · Full-bleed image · Statement · Closing.

## Content slide

Side margins are **120 px** left and right on every slide. Three bands:

**Header** — starts at `top: 56px`, stacked with 16 px gaps:

1. *Eyebrow* — 24 px, weight 500, `letter-spacing: 0.14em`, teal, uppercase.
   Reads like `02 — ALD FUNDAMENTALS`. It is what tells the audience where they
   are in the talk; without it a run of content slides feels undifferentiated.
2. *Heading* — Archivo 600, 60 px, `line-height: 1.1`,
   `letter-spacing: -0.018em`, navy, `max-width: 34ch`.
3. *Divider* — a 5 px band holding two elements: a 2 px `#E4E7EC` rule spanning
   the full column at `top: 1.5px`, and an 88 × 5 px teal cap at the left edge.
   The cap is the system's signature; a plain full-width rule is not the same
   thing.

**Body** — starts at `top: 268px`. Bullets are a 14 × 14 px teal square (the one
place a 4 px radius is allowed) with a 22 px gap, against 34 px text at
`line-height: 1.4` in ink, `max-width: 52ch`.

The body deliberately leaves the lower half open. Research slides get a plot or
micrograph pasted in later, and reserving that space beats reflowing text around
a figure after the fact.

**Footer** — at `bottom: 44px`, spanning the same 120 px margins: the wordmark
at 26 px on the left, and on the right
`hbrlee.unist@gmail.com · https://nanomaterial.kr` at 24 px in `#9AA1AB`, with
the separator dot in `#D2D6DD`.

## Cover slide

Navy `#14243F` full bleed. Positions are from the top-left:

| Element | Position | Type |
|---|---|---|
| Wordmark | `120, 96` | 40 px, bars white, RG teal |
| Teal bar | `120, 248` | 88 × 5 px |
| Heading | `120, 283` | Archivo 600, 108 px, `line-height: 1.02`, `letter-spacing: -0.025em`, white, `max-width: 26ch` |
| Subtitle | below heading | 36 px, `#93A2BC` |
| Hairline | `120, 814` | 1 px, `#2C4066`, full column |
| Name | `120, 840` | 30 px, weight 600, white |
| UNIST emblem | `120, 890` | 84 × 84 px, + affiliation at 24 px `#93A2BC` |
| CM logo | `773, 881` | 109 px tall, + editorial title at 24 px |
| Date | `120, 1013` | 24 px, `#6E82A3` |

A heading longer than roughly 26 characters per line wraps; check it clears the
hairline rather than trusting the nominal box height.

## Figures

Figure wells (`image-slot.js`) accept a dragged-in plot or micrograph and keep
the aspect ratio. Text inside a figure stays English even on Korean slides, so
the same figure can be reused in papers and talks.
