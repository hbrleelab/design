# HBRLRG Slide Components (v1.17)

> Released 2026-11-26 with design system v1.17. One slide per variant in [`hbrlrg-slide-components.pptx`](hbrlrg-slide-components.pptx) — copy the slide you need and replace the example content.
> Tokens: [`tokens-slide-components.json`](tokens-slide-components.json) · Previews: [`preview/`](preview/) (start with [`00_overview.png`](preview/00_overview.png)).
> Lock-up logos, affiliation text and colours are unchanged. All numbers on the example slides are illustrative and only show the layout.

## How to use (students)

1. Look at what you are putting on the slide (a number? a plot? a recipe?).
2. Find that content type in the table below and open the matching slide in the component deck.
3. Duplicate the slide, replace the example content, and keep sizes, colors and positions.

| Content on your slide | Component | Variants |
|---|---|---|
| A value to remember | **C1 Key number** | A number in title + on-data note ★ · B dumbbell vs baseline ★ · C slope chart · D highlighted cell · E reference scale · F small multiples |
| Claims with short reasons | **C2 Bullet statements** | A lead + bullets · B numbered steps · C claim / evidence |
| Measured trends | **C3 Experimental data chart** | A single chart + reading · B panel grid · C highlight one series |
| Exact values | **C4 Data table** | A rule table · B highlight row/column · C check matrix |
| Recipe, sequence | **C5 Process conditions** | A condition rail · B pulse sequence strip · C tags on figure |
| SEM, TEM, AFM, photos | **C6 Micrograph / image** | A image strip · B hero + insets · C condition grid |
| Before/after, A vs B | **C7 Comparison** | A side by side · B comparison table · C overlay |
| How it works | **C8 Mechanism schematic** | A step strip · B layer stack · C closed loop |
| The "so what" | **C9 Take-home** | A bottom bar · B three takeaways · C statement slide |
| Where it came from | **C10 Reference / source** | A source line · B adapted-from tag · C reference list |
| Plans, history | **C11 Timeline / roadmap** | A year bands · B milestone line · C Gantt |
| New part of the talk | **C12 Section divider** | A navy divider · B outline with position |
| A change that leads to a result | **C13 Cause & effect** | A linear chain · B cycle ring · C triangle · D convergent · E divergent · F feedback loop |
| How several things relate | **C14 Relationship map** | A variable → property matrix · B mapping lines · C radial hub · D branching tree |

★ = recommended default.

## Rules every component shares

- **Title = the finding**, written as a full sentence (max 2 lines). Not a topic label ("XRD results").
- **Kicker** (small line above the title) in sentence case, gray. Not uppercase, not letter-spaced, not teal.
- **One teal thing per slide**: the series, value or item the title talks about. Everything else is navy, ink or gray.
- **Square corners, no shadow, no gradient, no glow** on any shape.
- **Fill the slide** (Prof. Lee rule 4): if a figure leaves space, enlarge it or move the text under it.
- **Images keep their aspect ratio and are not cropped** (rule 8). Same size for images in a series.
- **Every published figure carries its source** (C10).

---

## C1 Key number

- **Concept**: the number is emphasized by **where it sits** (in the title, on the data, against a baseline), not by font size. Large stand-alone number tiles read as AI-generated dashboards (Prof. Lee, 2026-11-26) and are no longer a default.
- **Design elements**: the key value appears in the slide title (bold comes from the title); on charts a 14 pt teal note sits next to the point or range it describes; baseline values gray `ctx`, result teal; values in tables use `teal-bg` cell + teal bold; no digit larger than 24 pt on a body slide.
- **Variants**
  - A **Number in the title + on-data note** ★ — default for any measured result.
  - B **Dumbbell against a baseline** ★ — before → after, ours vs reference; gray dot, teal dot, light navy bar between.
  - C **Slope chart** — several conditions between two states; the named condition teal, labeled at both ends.
  - D **Highlighted cell** — the number must be read next to its alternatives; max. two teal cells per slide.
  - E **Reference scale** — the audience cannot judge the size alone; place the value on an axis with known references (e.g. bulk Cu, bulk Ru).
  - F **Small multiples** — the same number across conditions; identical axes, value written small under each panel.
- **Do not**: rows of 40–60 pt number tiles; a teal dash or icon above numbers; numbers without what they are compared with; more than one emphasized number per message.
- **If a big number is unavoidable**: one number, on its own slide, no tile, no icon, with its comparison in the line below (Knaflic's condition).
- **Student use**: "Put your key number in the slide title, then show it on the data."
- **Sources of the principle**: Storytelling with Data (gray + one color, simple text), Datawrapper/EU data-viz guide (annotations, range highlights), Assertion–Evidence (sentence titles), FT Visual Vocabulary and Tufte (slope, small multiples). See `2026-11-26_큰숫자_대체안.md`.

## C2 Bullet statements

- **Concept**: a bold lead states the claim; bullets are the reasons in speaking order.
- **Design elements**: lead 15 pt bold; bullet 15 pt, first words bold navy then an em dash; teal ■ bullet 7 pt; 3–5 bullets; line spacing 1.3; text column 5–6 grid columns with a figure in the rest.
- **Variants**
  - A **Lead + bullets** — default body slide.
  - B **Numbered steps** — order matters (procedure, logic chain); 44 pt teal numerals above a navy rule.
  - C **Claim | evidence** — every point needs its proof next to it; two columns with a thumbnail per row.
- **Do not**: write paragraphs as bullets; nest more than one level; use icons as bullets; leave the right half empty.
- **Student use**: "If you have more than five bullets, split the slide or turn some of them into a figure."

## C3 Experimental data chart

- **Concept**: one chart proves the title; color shows what matters, gray shows context.
- **Design elements**: axis titles with units 10–11 pt muted; axis line ink 1 pt; gridlines hairline 0.5 pt or none; **direct labels** at the line end instead of a legend; highlighted series teal 2.5 pt, others gray `ctx` 1.25–1.75 pt; panel letters (a)–(d) 12 pt bold at the top-left of each panel.
- **Variants**
  - A **Single chart + reading** — the one plot that proves the slide title; three "how to read it" lines beside it.
  - B **Panel grid** — 2–4 measurements of the same samples; same sample order and colors in every panel.
  - C **Highlight one series** — many conditions, one matters.
- **Do not**: use default Excel/Origin colors; 3D charts; legend boxes with borders; more than one teal series; rainbow palettes for categories.
- **Student use**: "Export your plot without a title and legend; put the finding in the slide title and label the lines directly."
- **Source of the principle**: Our World in Data and FT Visual Vocabulary chart grammar (direct labels, one highlight color, chart type by data relation).

## C4 Data table

- **Concept**: horizontal rules only; the eye moves along rows.
- **Design elements**: 1.5 pt navy rule on top, 0.75 pt navy under the header, 0.75 pt hairline between rows, no vertical lines; header 11–12 pt bold muted; numbers right-aligned, text left-aligned; units in the header; 2–3 significant digits.
- **Variants**
  - A **Rule table** — default for exact values.
  - B **Highlight row / column** — the table exists to show one winner; teal-bg row, teal deciding column; optional bar of that column below.
  - C **Check matrix** — capability or literature comparisons with ● ◐ ○.
- **Do not**: grid tables with all borders; colored header bands; zebra stripes; units inside every cell.
- **Student use**: "If the audience must see a difference rather than read a value, add the B bar or move to C3."

## C5 Process conditions

- **Concept**: the recipe sits next to the result it produced, never on a separate slide.
- **Design elements**: label 11 pt muted / value 12 pt bold right-aligned; rail on `surface` 260 pt wide; sequence strip: width ∝ time, navy = precursor, teal = the step being studied, hairline = purge.
- **Variants**
  - A **Condition rail** — the figure needs its recipe beside it.
  - B **Pulse sequence strip** — one ALD/ALE cycle in time.
  - C **Tags on the figure** — data-dense slides; navy tag = fixed condition, teal tag = the variable.
- **Do not**: paste a screenshot of a lab notebook table; list every parameter (keep what changes and what matters).
- **Student use**: "Show the condition that changed in teal; everything that stayed fixed in navy."

## C6 Micrograph / image

- **Concept**: images are evidence — same scale, same crop, labeled outside the image.
- **Design elements**: scale bar inside the image, bottom-right, white, label 10 pt bold; panel letter top-left; condition label 15 pt bold under each image; 8 pt gap between images; teal 1.5 pt frame only for insets or the recommended condition.
- **Variants**
  - A **Image strip** — a series (temperature, cycles, time).
  - B **Hero + insets** — one key image with zoomed details.
  - C **Condition grid** — two variables (rows × columns).
- **Do not**: stretch or crop to fit a box; add drop shadows or rounded corners to images; different magnifications side by side without saying so.
- **Student use**: "Crop all images to the same size before you place them, and keep the original scale bar."

## C7 Comparison

- **Concept**: identical layout on both sides, so the only difference the audience sees is the result.
- **Design elements**: left = reference (ink/gray), right = ours (navy title, teal result line); one teal arrow between; comparison table with teal-bg on the better value per row.
- **Variants**
  - A **Side by side** — before/after or A vs B with images or plots.
  - B **Comparison table** — 2–3 options across several criteria.
  - C **Overlay** — two curves on identical axes.
- **Do not**: "VS" badges, red/green check icons, different image sizes left and right.
- **Student use**: "Put the reference on the left and your result on the right, every time."

## C8 Mechanism schematic

- **Concept**: steps, layers or loops drawn with straight lines and a few shapes; the 3D render does the explaining, the frame stays quiet.
- **Design elements**: step header = 2 pt rule, teal number + navy name 15 pt; one sentence under each picture; straight connectors 1.5 pt with triangle heads; layer stack in navy tints (dark = decision, light = physical); the active step/node in teal.
- **Variants**
  - A **Step strip** — sequence of surface states (ALD/ALE half-cycles).
  - B **Layer stack** — frameworks or device structures; data up, decisions down.
  - C **Closed loop** — feedback (self-limiting reaction, AI-in-the-loop).
- **Do not**: curved glowing arrows, gradient-filled boxes, icon sets, circles with shadows; more than one active step.
- **Student use**: "Use the same picture size for every step; reuse earlier renders before making new ones (rule 7)."
- **Source of the principle**: layered exhibits in public consulting reports (Accenture/Dassault virtual twin, Bain architecture) — structure only, no copied graphics.

## C9 Take-home

- **Concept**: the sentence you want repeated after the talk.
- **Design elements**: navy bar, full content width, 30–34 pt high, text 14 pt bold white, sits above the source line; summary slide = three teal numerals 52 pt + statement 18 pt + "Evidence: Fig. n" 11 pt muted.
- **Variants**
  - A **Bottom bar** — on any evidence slide; one per slide, max.
  - B **Three takeaways** — summary at the end of a part or talk.
  - C **Statement slide** — once or twice per talk for a turning point; navy text on white with a 4 pt teal rule.
- **Do not**: full-bleed teal slides; quotation-mark graphics; light-teal tinted bars (low contrast).
- **Student use**: "If you cannot write the bar in one line, the slide is doing two things — split it."

## C10 Reference / source

- **Concept**: every borrowed figure or number keeps its origin on the slide.
- **Design elements**: source line 8 pt muted, one line above the footer, "Author et al., Journal Vol, first page (Year)"; adapted-from tag 9 pt on a white strip at the figure's bottom-right; reference list 14 pt, teal [n], hairline between entries.
- **Variants**
  - A **Source line** — required on every slide with published data.
  - B **Adapted-from tag** — redrawn or modified figures; the tag travels with the figure.
  - C **Reference list** — last content slide or backup.
- **Do not**: citations only as "[3]" without the list; URLs as citations; dropping the source when reusing a figure.
- **Student use**: "Files in #slide-materials are indexed figure by figure — if the source is not on the figure, it is lost."

## C11 Timeline / roadmap

- **Concept**: time runs left to right; each period says what is done when.
- **Design elements**: year header blocks navy (final goal teal); "Output" and "Done when" labels 10 pt muted bold; milestone line navy 2 pt with 14 pt dots, today/goal teal; Gantt bars navy, critical path teal, reports gray.
- **Variants**
  - A **Year bands** — multi-year research plans.
  - B **Milestone line** — history or project timeline with dates.
  - C **Gantt** — task plans with overlap.
- **Do not**: chevron arrows, 3D ribbons, rounded pill bars, icons per milestone.
- **Student use**: "Every period needs a check that says it is finished."
- **Source of the principle**: maturity-map exhibits (Accenture, Digital Twin Done Right, p.15) and staged frameworks (PwC) — structure only.

## C12 Section divider

- **Concept**: a quiet pause that tells the audience where they are.
- **Design elements**: navy ground, part label 13 pt `navy-3`, title 48 pt bold white, one line 18 pt `navy-4`; outline variant: current part navy bold with a 4 pt teal rule, others gray.
- **Variants**
  - A **Navy divider** — start of each part.
  - B **Outline with position** — long talks.
- **Do not**: teal cap + letter-spaced number (v1.14 habit), background photos with overlays.
- **Student use**: "Use B instead of A when the talk has more than three parts."

## Relationship diagrams: shapes, arrows and fills (C13, C14 — v1.17)

**Exception to "square corners"**: relationship nodes may use rounded rectangles (6 pt radius), capsules and circles. Prof. Lee asked for it on 2026-11-26 (15:1x): causation does not always run in a line, and square boxes with straight arrows looked monotonous. Everything else in the system keeps square corners. Depth comes from line, shape, spacing and colour hierarchy only — **no shadow, gradient or glow**.

| Element | Rule |
|---|---|
| Node shapes | **round** (6 pt radius) for quantities and states · **capsule** for steps, inputs and requirements · **circle** for a single result or hub |
| Fill levels | **outline** (white, 1.25 pt navy) = cause or input → **tint** (`navy-4`) = mechanism or intermediate → **teal fill** = the result the title names (one per slide) · **navy fill** = the actor or source · `teal-bg` = an external input |
| Symbol badge | small white or `teal-bg` circle inside the node for a formula or symbol (Ru, H, OH, θ) |
| Main path | teal 2.5 pt, one per slide |
| Strong / supporting | navy 2.25 pt / `navy-3` 1.25 pt |
| Hypothesis | `ctx` 0.75 pt dashed |
| Arrowhead | stealth (slim), medium, at the end only |
| Two-way | stealth at both ends — only for a real mutual effect |
| Inhibits | ⊣ — short bar across the end, no head |
| Association (no causation) | line with small dot ends (radial hub) |
| Start marker | small dot at the start of mapping lines and tree branches |
| Geometry | straight for chains; **arcs** on rings and loops; gentle curves (2nd-order Bézier) for fan-in, fan-out, triangles and maps; no hand-drawn wiggles |
| Labels | verb on the line, 10 pt `muted`, placed outside the curve; `+` / `−` at the head, 13 pt bold |
| Legend | one legend row (main · supporting · hypothesis · inhibits · two-way) on the first relationship slide of a talk |

**C8 vs C13 vs C14** — C8 shows what the surface or device *physically looks like* at each step (pictures). C13 shows *which quantity causes which* (arrows). C14 shows *how many things relate* without a single path (lines, matrix, hub, tree).

## C13 Cause & effect — six layouts

| Variant | Use it when the causation… | Example in the deck |
|---|---|---|
| A **Linear chain** | runs one step after another to one result | ligand size → steric hindrance → coverage → GPC |
| B **Cycle ring** | returns to its start and repeats | atomic-H Ru ALD cycle: precursor → purge → atomic H → purge |
| C **Triangle** | involves three factors that drive each other (synergy or trade-off) | ALE: Hhfac modification ↔ atomic-H removal ↔ surface –OH, with the synergy in the centre |
| D **Convergent** | has several causes adding up to one result | grain size, RuOₓ, impurities, thickness → Ru resistivity; atomic H ⊣ RuOₓ |
| E **Divergent** | has one cause with several effects, wanted and unwanted | hot-wire atomic H → Ru ALD, Al₂O₃ ALE, O₃ via fill, ⊣ inhibitor |
| F **Feedback loop** | feeds back on itself (balancing = self-limiting, reinforcing = runaway) | coverage ↑ → free sites ↓ → adsorption ↓ (B loop) |

- **Do not**: square boxes with straight arrows for a cycle; circular-arrow clip art; more than one teal path; arrows without a verb or sign; 3D, shadow, glow.
- **Student use**: "Pick the layout by the shape of the cause, not by habit: a loop is a ring, three mutual factors are a triangle, many-to-one converges."
- **Style references (principle only)**: Nature Reviews schematic figures (rounded nodes, two-colour hierarchy, curved arrows), journal TOC graphics (one focal element), consulting framework exhibits (cycle and value-chain diagrams in BCG/McKinsey reports in `_참고자료/컨설팅리포트`), causal-loop diagram notation (system dynamics).

## C14 Relationship map

| Variant | Use it when | Design |
|---|---|---|
| A **Variable → property matrix** | each process knob moves each film property | ▲/▼ in capsules (tint = up, outline = down, teal = the one the title names) |
| B **Mapping lines** | many inputs map to many outputs and strength matters | dot start, stealth end, weight = strength, dashed = hypothesis |
| C **Radial hub** | one core idea connects to several others (association) | circle hub, round satellites at equal angles, dot-ended lines |
| D **Branching tree** | an option is chosen from requirements | curved branches, capsule requirements, round leaves, recommended leaf teal |

- **Student use**: "If lines start to cross in B, switch to the matrix in A."

## Cover and closing — light and dark

- Two versions each: **light** (white ground) and **dark** (navy ground). Both are the system originals (v1.14 `hbrlrg-slides-light.pptx` / `hbrlrg-slides-dark.pptx`, slides 1 and 12) — the dark version uses the system's dark logo files unchanged.
- **Affiliation spacing (fixed in v1.17)**: the Chem. Mater. logo file has transparent padding (≈8 % left/right), so its text sat 23 pt from the visible logo while UNIST sat 12 pt. Now the gap is measured from each logo's visible edge: **12 pt** for both blocks, on light and dark; the dark CM block moves left by the dark emblem's padding so the gap between the two blocks is the same on both grounds. Logos are not cropped or resized. Source: `lockup()` in `tools/build_office.py` and the cover/closing of `slides/slides-en-*.html`.

---

## What changed against v1.14

| Element | v1.14 | v1.17 |
|---|---|---|
| KPI | teal dash above each big number | number in the title and on the data (C1 A–F) |
| Relations | none | C13 (six layouts: chain, ring, triangle, convergent, divergent, loop), C14 (matrix, mapping, hub, tree); node shapes, fill levels, curved arrows |
| Cover/closing | affiliation gaps uneven | light + dark; logo–text 12 pt on both blocks |
| Kicker | 12 pt teal, uppercase, letter-spaced | 11 pt gray, sentence case |
| Title rule | hairline + 44 pt teal cap | hairline only (`rule`) |
| Title | 30 pt, topic label | 24 pt, finding sentence + optional bold lead |
| Statement slide | full-bleed teal | white, navy text, 4 pt teal rule |
| Data colors | not defined | gray context + one teal highlight + navy tints |
| Tables | grid placeholder | rule table spec |
| Source line | not defined | 8 pt line above footer |

Unchanged: lock-up logos and affiliation text, footer, Archivo + Pretendard, navy/teal values, square corners.
