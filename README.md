# HBRLRG Design

The shared design system — documents, slides, web — for the HBRL Research Group
(UNIST). Anyone in the group can take the latest templates from here.

HBRL Research Group (UNIST) 의 문서 · 슬라이드 · 웹 공통 디자인 시스템 저장소입니다.
연구실 구성원이라면 누구나 여기서 최신 템플릿을 받아 쓸 수 있습니다.

**Get the templates · 최신 템플릿 받기** → [Releases](../../releases/latest)
· everything `hbrlrg-templates.zip` · PowerPoint `hbrlrg-slides.pptx` · Word `hbrlrg-*.docx`
**Read the spec · 디자인 규격 보기** → https://hbrleelab.github.io/design/
(the page has a KO / EN switch · 페이지에 한글 · 영문 전환 버튼이 있습니다)

---

## What's inside · 무엇이 들어 있나

```
documents/          A4 document templates · A4 문서 템플릿
  letterhead-kr.html    Letterhead, Korean · 레터헤드 (국문)
  letterhead-en.html    Letterhead, English · 레터헤드 (영문)
  plain-kr.html         Plain document, Korean · 기본 문서 (국문)
  plain-en.html         Plain document, English · 기본 문서 (영문)

slides/             16:9 slide template, 1920×1080 · 16:9 슬라이드 템플릿
  slides-en.html        12 layouts · 12종 레이아웃

design-system/      The specification · 디자인 규격서
  index.html            Read it in a browser (KO / EN) · 브라우저로 보는 규격서
  HBRLRG-design-system.md   The same in plain text, for AI tools
                            같은 내용의 텍스트 판 (클로드 등 AI 도구용)

web/                Homepage · 홈페이지
  hbrlrg.css            Stylesheet: tokens + components · 스타일시트 (토큰 + 컴포넌트)
  index.html            Reference implementation · 참조 구현
  HANDOFF.md            Developer's guide · 개발자용 적용 안내서

assets/
  logo/                 The full HBRLRG logo set · HBRLRG 로고 전체 세트
    hbrlrg-horizontal.svg / .png            Horizontal, the default · 가로형 (기본)
    hbrlrg-horizontal-reverse.svg / .png    For dark grounds · 어두운 배경용
    hbrlrg-horizontal-mono.svg / .png       One colour · 단색
    hbrlrg-horizontal-reverse-on-navy.*     Navy ground baked in · 네이비 배경 포함
    hbrlrg-vertical.svg / -mono.svg         Vertical · 세로형
    hbrlrg-symbol.svg / -reverse / -mono    Symbol alone · 심볼 단독
    hbrlrg-icon.svg / -icon.png / -icon-512.png   App icon, avatar · 앱 아이콘 · 프로필
    hbrlrg-favicon-64.png                   Favicon · 파비콘
    README.txt                              Logo spec · 로고 규격 (색 · 서체 · 최소 크기)
  unist-emblem.png        UNIST emblem, light ground · UNIST 엠블럼 (밝은 배경)
  unist-emblem-onnavy.png UNIST emblem, navy ground · UNIST 엠블럼 (네이비 배경)
  cm-logo-onnavy.png      Chemistry of Materials logo · Chemistry of Materials 로고

office/             PowerPoint and Word, built by each release
                    파워포인트 · 워드 판 (릴리스에서 자동 생성)
  hbrlrg-slides.pptx              12 layouts, Archivo embedded · 슬라이드 12종
  hbrlrg-letterhead-kr / -en.docx Letterhead · 레터헤드
  hbrlrg-plain-kr / -en.docx      Plain document · 기본 문서

deck-stage.js       Slide viewer: navigation, notes, print · 슬라이드 뷰어
image-slot.js       Image placeholder, drag and drop · 이미지 자리표시자
doc-page.js         A4 print layout engine · A4 인쇄 레이아웃 엔진
```

---

## How to use it · 쓰는 법

### Documents · 문서

1. Open the file you need from `documents/` in a browser<br>`documents/` 에서 필요한 파일을 브라우저로 엽니다
2. Edit the text directly on screen<br>화면에서 바로 글자를 고칩니다
3. Print (⌘P / Ctrl+P) → **Save as PDF**<br>인쇄(⌘P / Ctrl+P) → **PDF로 저장**

The A4 margins (18 mm) and the page breaks are automatic. Don't write your own
`@page` rules.

A4 여백(18 mm)과 페이지 나눔은 자동입니다. `@page` 설정을 따로 만들지 마세요.

### Slides · 슬라이드

1. Open `slides/slides-en.html` in a browser<br>`slides/slides-en.html` 을 브라우저로 엽니다
2. Move with ← →; pick or reorder slides in the thumbnail strip below<br>← → 키로 넘기고, 하단 썸네일에서 슬라이드를 고르거나 순서를 바꿉니다
3. Right-click a thumbnail to delete a layout you don't need<br>필요 없는 레이아웃은 썸네일에서 우클릭 → 삭제
4. **Drag and drop** a plot or a micrograph onto any grey image area<br>회색 이미지 영역에 플롯 · 현미경 사진을 **끌어다 놓으면** 채워집니다
5. Print → Save as PDF, one page per slide<br>인쇄 → PDF로 저장 (슬라이드당 한 장)

The 12 layouts: cover · contents · section break · content · figure (full) ·
figure (two up) · figure + text · table · metrics · full-bleed image · quote · closing.

레이아웃 12종: 표지 · 목차 · 섹션 구분 · 본문 · 그림(전면) · 그림(2단) ·
그림+설명 · 표 · 수치 · 전면 이미지 · 인용 · 맺음.

Your data is the point of the talk, so every content layout deliberately leaves
everything below the top 268 px **empty**. That space is for your plots.

발표 데이터가 중심이므로 모든 본문 슬라이드는 상단 268 px 아래를
**비워 두도록** 설계했습니다. 플롯을 붙일 자리입니다.

### If you'd rather work in PowerPoint or Word · 파워포인트 · 워드로 쓰고 싶다면

For the times HTML won't do — co-editing with someone, a conference submission
form — the same spec is also built as `.pptx` and `.docx`. Download them
individually from [Releases](../../releases/latest).

HTML 을 쓰기 어려운 상황(공동 편집, 학회 제출 양식 등)을 위해 같은 규격을
`.pptx` · `.docx` 로도 만들어 둡니다. [Releases](../../releases/latest) 에서
파일을 따로 받으면 됩니다.

- `hbrlrg-slides.pptx` **carries Archivo inside the file**, so the Latin type
  survives on a machine where the font isn't installed. Korean is set in
  Pretendard, which is *not* embedded — if you write Korean slides, install
  [Pretendard](https://github.com/orioncactus/pretendard) once.<br>
  `hbrlrg-slides.pptx` 는 **Archivo 를 파일 안에 심어** 두어, 폰트가 설치되지 않은
  PC 에서도 영문 서체가 유지됩니다. 한글은 Pretendard 로 지정돼 있으나 임베드되지
  **않았으니**, 한글 슬라이드를 쓴다면
  [Pretendard](https://github.com/orioncactus/pretendard) 를 설치하세요.
- Word can't embed fonts at all. Anything you send outside the group should go
  as a **PDF**, or it will reflow on the recipient's machine.<br>
  워드 파일은 폰트를 심을 수 없습니다. 밖으로 보내는 문서는 **PDF 로 내보내야**
  받는 사람 PC 에서 모양이 유지됩니다.
- HTML remains the source. The Office files are rebuilt on every release, so
  don't keep a hand-edited copy and reuse it.<br>
  원본은 어디까지나 HTML 입니다. 규격이 바뀌면 릴리스마다 다시 만들어지므로,
  Office 파일을 직접 고쳐 두고 재사용하지 마세요.

### Homepage · 홈페이지

Load `web/hbrlrg.css` **after** your existing stylesheet. No build tooling needed.
Open `web/index.html` in a browser to see the correct markup for every component;
`web/HANDOFF.md` covers how to apply it and what to watch out for.

`web/hbrlrg.css` 를 기존 스타일시트 **뒤에** 불러오면 됩니다. 빌드 도구 불필요.
`web/index.html` 을 브라우저로 열면 모든 컴포넌트의 올바른 마크업을 볼 수 있고,
적용 절차와 주의사항은 `web/HANDOFF.md` 에 정리돼 있습니다.

### Handing the spec to an AI tool · AI 도구에 규격 전달

One file does it: `design-system/HBRLRG-design-system.md`. Colour, type, spacing,
logo rules and the affiliation wording are all there as plain text, ready to drop
into Claude project knowledge or a conversation. Add the HTML from `documents/`
if you also want it to follow the document markup.

`design-system/HBRLRG-design-system.md` 한 파일이면 됩니다. 색 · 서체 · 간격 · 로고
규칙과 소속 표기가 모두 텍스트로 정리돼 있어, 클로드 프로젝트 지식이나 대화에 그대로
넣어 쓸 수 있습니다. 문서 마크업까지 참고시키려면 `documents/` 의 HTML을 함께 넣으세요.

---

## Brand defaults · 브랜드 기본값

| Item · 항목 | Value · 값 |
| --- | --- |
| Navy — primary · 주색 | `#14243F` |
| Teal — accent · 강조색 | `#0EA79A` |
| Body text · 본문 텍스트 | `#2B2F36` |
| Secondary text · 보조 텍스트 | `#6B7280` |
| Table header fill · 표 헤더 배경 | `#F6F7F9` |
| Logo and Latin headings · 로고 · 영문 제목 서체 | Archivo |
| Korean body · 한글 본문 서체 | Pretendard |

The horizontal lockup is the default, at a fixed 573.5 : 169.1 ratio. On a dark
ground always use the reverse file — swap the file, never recolour the artwork.
Minimum size is 120 px / 25 mm wide.

로고는 가로형이 기본이며 비율 573.5 : 169.1을 유지합니다. 어두운 배경에는 반드시
reverse 파일을 씁니다 (색을 바꾸지 말고 파일을 바꿉니다). 최소 크기는 가로형 너비
120 px / 25 mm 입니다.

There is **exactly one** accent colour, used only for rule caps, bullets and CTAs.
Corners stay square (radius 0). These two rules are what hold the documents,
slides and website together as one thing.

강조색은 **하나뿐**입니다. 구분선 캡, 불릿, CTA에만 씁니다.
모서리는 각지게 유지합니다(radius 0). 이 두 가지가 문서 · 슬라이드 · 웹을
하나로 묶는 규칙입니다.

---

## Affiliation · 소속 표기

Never abbreviate it or reorder it. · 줄이거나 순서를 바꾸지 마세요.

- **English · 영문** Professor, Graduate School of Semiconductor Materials & Devices Engineering, Ulsan National Institute of Science and Technology (UNIST)
- **Korean · 국문** 울산과학기술원(UNIST) 반도체소재부품대학원 교수
- **Editorial title · 편집 직함** Executive Editor, Chemistry of Materials, ACS Publications
- **Address · 주소** 50 UNIST-gil, Ulju-gun, Ulsan 44919, Republic of Korea

---

## Requests and fixes · 기여 · 수정 요청

If a template is wrong or you need a new layout, open an
[Issue](../../issues). The maintainer applies the change and ships it in the
next release.

템플릿에 문제가 있거나 새 레이아웃이 필요하면
[Issues](../../issues) 에 남겨 주세요. 수정은 관리자가 반영한 뒤
새 릴리스로 배포합니다.

Release procedure: [`DEPLOY.md`](DEPLOY.md) · 배포 절차는 [`DEPLOY.md`](DEPLOY.md) 참고.
