# HBRLRG Design System — house rules · 디자인 시스템 — 문서 작성 지침

The shared specification for documents, slides and web at HBRL Research Group
(Prof. Han-Bo-Ram Lee's laboratory, UNIST). Follow these rules for anything that
goes out under the group's name.

HBRL Research Group (이한보람 교수 연구실, UNIST) 의 문서 · 슬라이드 · 웹 공통
디자인 규격입니다. 이 연구실 이름으로 나가는 문서를 만들 때 아래 규칙을 따르세요.

---

## 1. Colour · 색

| Name · 이름 | Value · 값 | Where it goes · 쓰는 곳 |
| --- | --- | --- |
| Navy | `#14243F` | Headings, names, rules, dark grounds · 제목, 이름, 구분선, 어두운 배경 |
| Teal | `#0EA79A` | **The only accent.** Rule caps, bullets, CTAs · **강조색 하나뿐.** 구분선 캡, 불릿, CTA |
| Ink | `#2B2F36` | Body text · 본문 |
| Muted | `#6B7280` | Contact lines, captions, table labels · 연락처, 캡션, 표 라벨, 보조 설명 |
| Faint | `#9AA1AB` | Document footers · 문서 푸터 |
| Surface | `#F6F7F9` | Table header fill, image slots · 표 헤더 배경, 이미지 자리 |
| Border | `#E4E7EC` | Table rules, dividers · 표 괘선, 구분선 |

**Rules · 규칙**

- One accent colour: teal. Do not add another.<br>강조색은 청록 하나입니다. 다른 색을 추가하지 마세요.
- Only three grounds: white, `#F6F7F9`, Navy.<br>배경은 흰색 · `#F6F7F9` · Navy 세 가지만 씁니다.
- Never set small body text in teal (2.99:1 on white).<br>청록은 작은 본문 글자색으로 쓰지 않습니다 (흰 배경에서 대비 2.99:1).
- Corners stay square (`border-radius: 0`). The one exception is the 6 px teal bullet square (radius 2 px).<br>모서리는 각지게 (`border-radius: 0`). 예외는 6 px 청록 불릿 사각(radius 2 px)뿐.

---

## 2. Type · 서체

| Typeface · 서체 | Weights · 굵기 | Where it goes · 쓰는 곳 |
| --- | --- | --- |
| **Archivo** | 300 / 400 / 500 / 600 | All Latin text, headings, numerals, table labels, the logo · 영문 전체, 제목, 숫자, 표 라벨, 로고 |
| **Pretendard** | 400 / 500 / 600 | Korean body text · 한글 본문 |

Declare the stack in this order:
`'Archivo', 'Pretendard', -apple-system, 'Apple SD Gothic Neo', sans-serif`.
Archivo has no Korean, so Korean falls through to Pretendard automatically.

폰트 스택은 `'Archivo', 'Pretendard', -apple-system, 'Apple SD Gothic Neo', sans-serif`
순서로 지정합니다. Archivo에 한글이 없으므로 한글은 자동으로 Pretendard로 넘어갑니다.

CDN:
```html
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
```

**Never specify** Inter, Roboto, Arial or Malgun Gothic.

**금지 서체** — Inter, Roboto, Arial, 맑은 고딕을 지정하지 마세요.

---

## 3. Document type scale, A4 · 문서 타입 스케일 (A4)

| Role · 역할 | Size · 크기 | Weight · 굵기 | Leading · 행간 | Colour · 색 |
| --- | --- | --- | --- | --- |
| Letterhead name · 레터헤드 이름 | 24 pt | 300 | 1.05 | Navy |
| Document title (H1) · 문서 제목 | 20 pt | 600 | 1.25 | Navy |
| Section heading (H2) · 섹션 제목 | 14 pt | 500 | default · 기본 | Navy |
| Body · 본문 | 11 pt | 400 | 1.7 | Ink |
| Affiliation · 소속 | 9.5 pt | 400 | 1.5 | Navy |
| Table body · 표 본문 | 10 pt | 400 | default · 기본 | Ink |
| Contact line, table caption · 연락처 · 표 캡션 | 8.5 / 9 pt | 400 | 1.5 | Muted |
| Table header label · 표 헤더 라벨 | 8.5 pt | 500 | +0.06em | Muted |
| Footer · 푸터 | 7.5 pt | 400 | +0.07em | Faint |

A4 portrait, 18 mm margins on all sides, single column. The spacing unit is pt
(5 · 6 · 8 · 10 · 16 · 18 · 20 · 22 · 26).

용지 A4 세로, 여백 사방 18 mm, 1단.
간격 단위는 pt (5 · 6 · 8 · 10 · 16 · 18 · 20 · 22 · 26).

---

## 4. The three signature elements · 시그니처 요소 세 가지

These three are what hold the documents, slides and web together as one thing.

이 세 가지가 문서 · 슬라이드 · 웹을 하나로 묶습니다.

### The rule cap · 구분선 캡

A 1.2 px Navy line across the full measure, with a left-aligned **46 × 3 px teal
cap** laid over it. It appears once per document. Never centre it or put it right.

폭 전체를 지나는 1.2 px Navy 선 위에, 좌측 정렬된 **46 × 3 px 청록 캡**을
얹습니다. 문서당 한 번만 등장합니다. 가운데 정렬이나 우측 배치는 하지 않습니다.

```html
<div style="position:relative;height:3px;">
  <div style="position:absolute;left:0;right:0;top:1px;height:1.2px;background:#14243F;"></div>
  <div style="position:absolute;left:0;top:0;width:46px;height:3px;background:#0EA79A;"></div>
</div>
```

### The HBRLRG logo · HBRLRG 로고

Don't draw it — **use the official file**. The default is the horizontal lockup:
the symbol (an interlocking knot) plus the wordmark. All lettering is outlined, so
it renders identically without the font installed.

직접 그리지 말고 **공식 파일을 씁니다**. 심볼(엮힌 고리)과 워드마크가 결합된
가로형이 기본이며, 글자는 모두 아웃라인이라 서체 설치 없이 동일하게 렌더링됩니다.

| Ground · 배경 | File · 파일 |
| --- | --- |
| Light · 밝은 배경 | `assets/logo/hbrlrg-horizontal.svg` (or `.png`) |
| Dark, over photography · 어두운 배경 · 사진 위 | `assets/logo/hbrlrg-horizontal-reverse.svg` |
| Symbol alone · 심볼 단독 | `assets/logo/hbrlrg-symbol.svg` · `-reverse.svg` |
| App icon, avatar · 앱 아이콘 · 프로필 | `assets/logo/hbrlrg-icon.svg` |

```html
<img src="assets/logo/hbrlrg-horizontal.png" alt="HBRLRG" style="height:27px;width:92px;display:block;">
```

**Rules · 규칙**

- The ratio is fixed at **573.5 : 169.1 (3.39 : 1)**. Never stretch or distort it.
  Set the height and state the width as `height × 3.39`.<br>
  비율 **573.5 : 169.1 (3.39 : 1)** 고정. 늘이거나 변형하지 마세요.
  높이만 지정하고 폭은 `높이 × 3.39` 로 계산해 명시합니다.
- On a dark ground, **swap the file, don't recolour** (use the reverse version).<br>
  어두운 배경에서는 **색을 바꾸지 말고 파일을 바꾸세요** (reverse 버전).
- Minimum size: horizontal 120 px / 25 mm wide, symbol alone 24 px / 6 mm.<br>
  최소 크기: 가로형 너비 120 px / 25 mm, 심볼 단독 24 px / 6 mm.
- Heights in use: 27 px in a document header, 42 px in a slide footer, 68 px on a cover or closing slide.<br>
  사용 높이: 문서 머리글 27 px, 슬라이드 푸터 42 px, 표지 · 맺음 68 px.
- The gaps where the strands cross are cut through to transparency, so the knot holds on any ground.<br>
  엮이는 지점의 틈새는 투명하게 뚫려 있어 어떤 배경 위에서도 매듭 구조가 유지됩니다.
- No recolouring, shadows, rotation or effects.<br>
  재색상 · 그림자 · 회전 · 효과 금지.

### The bullet square · 불릿 사각

A **teal square** (radius 2 px) instead of a glyph, aligned to the **centre** of
the first line of text — not to its top.

기호 대신 **청록 사각형**(radius 2px)을 씁니다. 첫 줄 텍스트의 **가운데**에
맞춥니다 — 위쪽에 맞추지 마세요.

`margin-top = (font-size × line-height ÷ 2) − (square ÷ 2)`

11 pt / 1.6 body with a 6 px square → `margin-top: 6.5pt`.

11 pt / 1.6 본문 + 6 px 사각 → `margin-top: 6.5pt`.

```html
<div style="display:flex;gap:8pt;">
  <span style="flex:0 0 auto;width:6px;height:6px;border-radius:2px;background:#0EA79A;margin-top:6.5pt;"></span>
  <p style="margin:0;font-size:11pt;line-height:1.6;color:#2B2F36;">항목 내용</p>
</div>
```

---

## 5. The two document templates · 문서 템플릿 두 종

### Letterhead — outgoing · 레터헤드 (외부 발신용)

Recommendations, invitations, official notices, journal cover letters.

추천서, 초청장, 공문, 저널 커버레터.

Header — the UNIST emblem (88 × 88 px, fixed left) + a 24 px gap + a right-set
text block. The order is **name → affiliation → contact → (concurrent post)**.
The rule sits 16 px below the header.

머리글 구성 — UNIST 엠블럼(88 × 88 px, 좌측 고정) + 24 px 간격 + 우측 정렬
텍스트 블록. 순서는 **이름 → 소속 → 연락처 → (겸직)**. 구분선은 헤더 아래 16 px.

Body order · 본문 순서

1. Date — 26 pt below the rule · 날짜 — 구분선 아래 26 pt
2. Recipient — 16 pt above · 수신처 — 위 16 pt
3. Salutation — 18 pt above · 인사말 — 위 18 pt
4. Body paragraphs — 10 pt between, no indent · 본문 단락 — 단락 간 10 pt, 들여쓰기 없음
5. Closing — 18 pt above · 맺음말 — 위 18 pt
6. Signature block — leave 34 pt for the signature · 서명 블록 — 서명 여백 34 pt 확보

Footer — `phone · email · homepage` centred at 7.5 pt Faint, the items separated
not by a dot but by a 1 px hairline (`#E4E7EC`, 8 pt tall). Repeated on every page.

푸터 — `전화 · 이메일 · 홈페이지` 를 7.5 pt Faint로 가운데 정렬하고, 항목 사이는
점이 아니라 1 px 헤어라인(`#E4E7EC`, 높이 8 pt)으로 나눕니다. 모든 페이지에 반복.

**Don't** — use the emblem and the HBRLRG wordmark together (**letterhead only**;
for slide covers and closings see §7-1), insert tables or charts, or run past
three body paragraphs.

**하지 않을 것** — 엠블럼과 HBRLRG 워드마크 동시 사용(**레터헤드 한정**. 슬라이드 표지 · 맺음은 §7-1 참조),
표 · 차트 삽입, 본문 3단락 초과.

### Plain document — internal · 기본 문서 (내부용)

Experimental reports, process condition sheets, minutes, manuals.

실험 보고, 공정 조건서, 회의록, 매뉴얼.

Header — HBRLRG logo left (27 px tall), contact information right (8.5 pt, web
then email). The rule sits 12 px below the header. The footer repeats on every
page at 7.5 pt uppercase.

머리글 — 좌측 HBRLRG 로고(높이 27 px), 우측 연락 정보(8.5 pt, 웹 · 이메일 순).
구분선은 헤더 아래 12 px. 푸터는 7.5 pt 대문자로 페이지마다 반복.

Body order · 본문 순서

1. Title (H1) — 24 pt below the rule · 제목 (H1) — 구분선 아래 24 pt
2. Meta line — author · date · version · 메타 줄 — 작성자 · 날짜 · 버전
3. Section (H2) — 20–22 pt above, **numbering required** (1. 2. 3.) · 섹션 (H2) — 위 20–22 pt, **번호 필수**
4. Body / table / bullets — 6–8 pt below the heading · 본문 / 표 / 불릿 — 제목 아래 6–8 pt
5. Table caption — 5 pt below the table, 9 pt Muted · 표 캡션 — 표 아래 5 pt, 9 pt Muted

**Don't** — insert the UNIST emblem (letterhead only), give tables vertical rules
or striped backgrounds, subdivide H2 more than one level deep, or use Navy in body
text.

**하지 않을 것** — UNIST 엠블럼 삽입(레터헤드 전용), 표에 수직 괘선 · 줄무늬,
H2를 두 단계 이상 세분화, 본문에 Navy 사용.

---

## 6. Tables · 표

**Never use vertical rules.** · **수직 괘선을 절대 넣지 않습니다.**

- Header: `#F6F7F9` fill, uppercase labels at 8.5 pt / weight 500 / +0.06em / Muted<br>헤더: `#F6F7F9` 배경, 대문자 라벨 8.5 pt / 굵기 500 / 자간 +0.06em / Muted
- Rows: a bottom rule only (`#E4E7EC`)<br>행: 하단 괘선(`#E4E7EC`) 만
- Cell padding: 5 × 8 pt<br>셀 패딩: 5 × 8 pt
- Caption: 5 pt below the table, 9 pt Muted, no terminal punctuation ("Table 1. Condition comparison")<br>캡션: 표 아래 5 pt, 9 pt Muted, 문장부호 없이 ("표 1. 조건 비교")
- Three to five columns · 열은 3–5개 이내

---

## 7. Slides, 1920 × 1080 · 슬라이드

Side margins 120 px. The header starts 56 px from the top, and **the content area
starts at 268 px**. Everything below that is left empty for data and plots.

좌우 여백 120 px. 헤더는 상단 56 px에서 시작하고, **콘텐츠 영역은 268 px부터**
시작합니다. 그 아래는 데이터 · 플롯 자리로 비워 둡니다.

| Role · 역할 | Size · 크기 |
| --- | --- |
| Cover title · 표지 제목 | 108 px / 600 |
| Section title · 섹션 제목 | 104 px / 600 |
| Slide title · 슬라이드 제목 | 60 px / 600 |
| Body bullet · 본문 불릿 | 34 px / 1.4 |
| Large numeral · 큰 수치 | 118 px / 300 |
| Caption, footer · 캡션 · 푸터 | 24 px |

**Never set type below 24 px.** · **24 px 미만 글자를 쓰지 마세요.**

Footer — 44 px from the bottom. Left: the HBRLRG logo (42 px tall), a 1 × 20 px
`#D2D6DD` divider, then the **section title** in 24 px `#2B2F36`, title case.
Right: `hbrlee@unist.ac.kr | https://hbrl-research.group` in 24 px Faint. Nothing
else — the group name is already in the logo, so don't repeat it in the text.
A slide belonging to no section (the agenda) carries the logo alone. The cover
and closing slides are the exception entirely (the logo lockup takes that space).

푸터 — 하단 44 px. 좌측은 HBRLRG 로고(높이 42 px) → 1 × 20 px `#D2D6DD` 구분선 →
**섹션 타이틀**(24 px, `#2B2F36`, 첫 글자만 대문자). 우측은
`hbrlee@unist.ac.kr | https://hbrl-research.group` (24 px, Faint). 그 외에는 넣지
않습니다 — 연구실 이름은 로고에 이미 있으므로 글자로 반복하지 마세요.
섹션에 속하지 않는 슬라이드(목차)는 로고만 둡니다. 표지와 맺음 슬라이드는 아예
예외입니다(로고 로크업이 그 자리를 씁니다).

The section title repeats the eyebrow without its number. The eyebrow is gone
from view the moment someone looks away from the header; the footer is what tells
a listener who joined late where they are.

섹션 타이틀은 아이브로우에서 번호를 뺀 것입니다. 아이브로우는 헤더에서 눈을 떼는
순간 사라지므로, 늦게 들어온 청중에게 현재 위치를 알려 주는 것은 푸터입니다.

The 12 layouts: cover · contents · section break · content · figure (full) ·
figure (two up) · figure + text · table · metrics · full-bleed image · quote ·
closing.

레이아웃 12종: 표지 · 목차 · 섹션 구분 · 본문 · 그림(전면) · 그림(2단) ·
그림+설명 · 표 · 수치 · 전면 이미지 · 인용 · 맺음.

### 7-1. The logo lockup — cover and closing only · 로고 로크업 (표지 · 맺음 전용)

The cover and closing slides carry a **logo lockup** instead of a footer. The
lockup is a left-aligned pair of columns, each one `logo + two lines of title text`.

표지와 맺음 슬라이드는 푸터 대신 **로고 로크업**을 씁니다. 로크업은 좌측 정렬 2단이며,
각 단은 `로고 + 직함 텍스트 2줄` 로 구성합니다.

The cover and the closing use the **same** lockup, at the same coordinates. An
audience photographs the closing slide, so it has to carry both affiliations too.

표지와 맺음은 **같은** 로크업을 같은 좌표에 씁니다. 청중이 사진으로 남기는 것은
맺음 슬라이드이므로, 두 소속이 거기에도 있어야 합니다.

| Element · 요소 | Position · 위치 | Size · 크기 |
| --- | --- | --- |
| Rule (`#2C4066`) · 구분선 | `120, 814` | full measure × 1 px · 폭 전체 × 1 px |
| Name · 이름 | `120, 840` | 30 px / 600 / white, leading 1.15 |
| UNIST emblem · UNIST 엠블럼 | `120, 892` | 84 × 84 px |
| Affiliation · 소속 텍스트 | `228, 892` | width 543, 24 px, leading 1.35, `#93A2BC` |
| Chemistry of Materials logo · CM 로고 | `773, 881` | 218 × 109 px |
| Editorial title · 편집 직함 | `1019, 881` | width 501, 24 px, leading 1.35, `#93A2BC` |
| Last line · 마지막 줄 | `120, 1013` | 24 px, `#6E82A3` — cover: venue and date · 표지: 장소 · 날짜 / closing: contact · 맺음: 연락처 |

- **Set the height and let the width follow the file.** Never state both. The CM
  artwork is **2.0 : 1** and the UNIST emblem **1.0 : 1**; an earlier version
  hard-coded 216 × 59 for CM and stretched it by 1.8×.<br>
  **높이만 지정하고 폭은 파일 비율을 따르게 하세요.** 둘 다 적지 마세요. CM 아트워크는
  **2.0 : 1**, UNIST 엠블럼은 **1.0 : 1** 입니다. 이전 버전이 CM 을 216 × 59 로
  못박아 1.8배 늘려 놓은 적이 있습니다.
- Each text block is vertically centred against the logo beside it, not top-aligned.<br>
  각 텍스트 블록은 옆 로고에 대해 세로 가운데 정렬합니다. 위 맞춤이 아닙니다.
- Neither slide takes the standard footer — the lockup occupies that space. The
  HBRLRG logo sits top-left at `120, 96`, 68 px tall.<br>
  두 슬라이드 모두 일반 푸터를 쓰지 않습니다 — 로크업이 그 자리를 씁니다. HBRLRG
  로고는 좌상단 `120, 96` 에 높이 68 px 로 놓입니다.
- On the cover, the HBRLRG logo (top left, 68 px tall) sits alongside the emblem. Their roles differ — the logo is who is speaking, the emblem and CM are the credentials.<br>
  표지에서는 HBRLRG 로고(좌상단, 높이 68 px)와 엠블럼이 함께 놓입니다. 역할이 다르기 때문입니다 —
  로고는 발신 주체, 엠블럼 · CM은 소속 증빙.

Cover coordinates (on 1920 × 1080; 1 px = 0.5 pt)

표지 좌표 (1920 × 1080 기준, 1 px = 0.5 pt)

| Element · 요소 | x | y |
| --- | --- | --- |
| Rule (`#2C4066`, full width × 1 px) · 구분선 | 120 | 579 |
| Name (48 px / 600 / white) · 이름 | 120 | 619 |
| UNIST emblem · UNIST 엠블럼 | 120 | 691 |
| Affiliation text (648 px wide) · 소속 텍스트 | 270 | 700 |
| CM logo · CM 로고 | 943 | 723 |
| Editorial title text (598 px wide) · 편집 직함 텍스트 | 1202 | 700 |

The closing differs from the cover only in what sits above the rule: "Thank you"
instead of the talk's title, and the contact line instead of the venue and date.

맺음은 구분선 위 내용만 표지와 다릅니다 — 발표 제목 대신 "Thank you", 장소 · 날짜
대신 연락처.

Original ratios — do not distort. UNIST emblem **1.0 : 1**
(`unist-emblem-onnavy.png`, 1000 × 1000), Chemistry of Materials **2.0 : 1**
(`cm-logo-onnavy.png`, 632 × 316).

원본 비율 — 변형하지 마세요. UNIST 엠블럼 **1.0 : 1**
(`unist-emblem-onnavy.png`, 1000 × 1000), Chemistry of Materials **2.0 : 1**
(`cm-logo-onnavy.png`, 632 × 316).

**Don't** — put the emblem or the CM logo on a content slide (footer HBRLRG logo
only), centre the lockup, or lay a logo on a teal or navy ground without a white
box (the CM logo comes with its own white box).

**하지 않을 것** — 본문 슬라이드에 엠블럼 · CM 로고 삽입(푸터의 HBRLRG 로고만),
가운데 정렬, 로고를 청록/네이비 배경 위에 흰 박스 없이 얹기(CM 로고는 자체 흰 박스를 포함한 형태를 씁니다).

---

## 8. Affiliation — exactly as written · 소속 표기 — 정확히 이대로

Never abbreviate it or reorder it. In English, never spell `&` out as `and`.

줄이거나 순서를 바꾸지 마세요. 영문에서 `&` 를 `and` 로 풀지 마세요.

- **English · 영문** Professor, Graduate School of Semiconductor Materials & Devices Engineering, Ulsan National Institute of Science and Technology (UNIST)
- **Korean · 국문** 울산과학기술원(UNIST) 반도체소재부품대학원 교수
- **Editorial title · 편집 직함** Executive Editor, Chemistry of Materials, ACS Publications
- **Address · 주소** 50 UNIST-gil, Ulju-gun, Ulsan 44919, Republic of Korea
- **Email · 이메일** hbrlee@unist.ac.kr
- **Homepage · 홈페이지** https://hbrl-research.group
- **Laboratory · 연구실** HBRL Research Group / HBRLRG
- **Logos accompany the words · 로고 병기** The UNIST emblem and the Chemistry of
  Materials logo are **always** placed together with the affiliation text above.
  Never use a logo on its own.<br>
  UNIST 엠블럼과 Chemistry of Materials 로고는 위 소속 문구와 **항상 함께** 놓습니다.
  로고만 단독으로 쓰지 않습니다.

---

## 9. Writing · 글쓰기

- State the facts. Don't add commentary that inflates them.<br>사실을 그대로 전달합니다. 의미를 부풀리는 해설을 붙이지 않습니다.
- No emoji.<br>이모지를 쓰지 않습니다.
- Avoid heavy emphasis (overused bold and underline).<br>과한 강조(굵게 · 밑줄 남용)를 피합니다.
- Include only the tables and figures you need. Never invent data to fill a gap.<br>표와 수치는 필요한 것만 넣습니다. 빈 칸을 채우려고 데이터를 만들지 않습니다.
- Be generous with white space. Take something out rather than cram a page.<br>여백을 아끼지 않습니다. 한 페이지에 밀어 넣기보다 덜어냅니다.

---

## 10. The files · 이 폴더의 파일

| File · 파일 | Purpose · 용도 |
| --- | --- |
| `documents/letterhead-en.html` / `letterhead-kr.html` | Letterhead markup · 레터헤드 문서 마크업 |
| `documents/plain-en.html` / `plain-kr.html` | Plain document markup · 기본 문서 마크업 |
| `slides/slides-en.html` | Slide template, 12 layouts · 슬라이드 템플릿 12종 |
| `web/hbrlrg.css` | Web stylesheet: tokens + components · 웹용 스타일시트 (토큰 + 컴포넌트) |
| `assets/logo/hbrlrg-horizontal.svg` (+ `.png`) | HBRLRG horizontal logo, light grounds · 가로형 로고 — 밝은 배경용 |
| `assets/logo/hbrlrg-horizontal-reverse.svg` (+ `.png`) | Horizontal logo, dark grounds · 가로형 로고 — 어두운 배경용 |
| `assets/logo/hbrlrg-symbol.svg` · `-reverse.svg` | Symbol alone · 심볼 단독 |
| `assets/logo/hbrlrg-icon.svg` | App icon, avatar · 앱 아이콘 · 프로필 |
| `assets/unist-emblem.png` / `unist-emblem-onnavy.png` | UNIST emblem, light / navy grounds · UNIST 엠블럼 — 밝은 배경용 / 네이비 배경용 |
| `assets/cm-logo-onnavy.png` | Chemistry of Materials logo · Chemistry of Materials 로고 |

The HTML files pull their fonts from a CDN, so each is 3–7 KB. To make a new
document, copy the markup of the matching file and change only the content.

HTML 파일은 서체를 CDN으로 불러오므로 각 3–7 KB입니다. 새 문서를 만들 때
해당 파일의 마크업을 그대로 복제하고 내용만 바꾸세요.
