# Deployment and maintenance · 배포 구조 · 운영 가이드

How `hbrleelab/design` is run as "the place students always get the latest
templates from" — the reasoning behind the structure, and the actual procedures.

`hbrleelab/design` 저장소를 "학생들이 항상 최신 템플릿을 받아 가는 곳"으로
운영하기 위한 구조입니다. 설계 근거와 실제 절차를 함께 적었습니다.

---

## 1. The problem · 무엇을 푸는 문제인가

Three separate needs. · 세 가지 요구가 있습니다.

1. **Distribution** — a student gets the current slide and document templates easily<br>**배포** — 학생이 최신 슬라이드 · 문서 템플릿을 쉽게 받아 간다
2. **Updating** — each time a template changes, it is republished<br>**갱신** — 템플릿이 바뀔 때마다 다시 올린다
3. **Reference** — the spec (colour, type, spacing) can be opened at any time<br>**참조** — 디자인 규격(색 · 서체 · 간격)을 언제든 열어 본다

Each wants a different shape: downloads want **files**, the spec wants a **web
page**, the history wants **versions**. Force all three through one mechanism and
one of them becomes awkward. The structure below keeps them separate but in a
single repository.

세 가지는 서로 다른 형태를 원합니다. 다운로드는 **파일**, 규격서는 **웹페이지**,
갱신 이력은 **버전**입니다. 하나의 방식으로 셋을 다 덮으려 하면 어딘가 불편해집니다.
아래 구조는 셋을 분리하되 한 저장소 안에 둡니다.

---

## 2. Repository layout · 저장소 구조

```
hbrleelab/design
├── README.md              Landing page: downloads and usage · 첫 화면. 다운로드와 사용법
├── DEPLOY.md              This document · 이 문서
├── index.html             Redirect to the spec · 규격서로 보내는 리다이렉트
├── .nojekyll              Serve files as-is on Pages · Pages 가 파일을 그대로 내보내게
├── documents/             Four A4 documents · A4 문서 4종
├── slides/                16:9 slide template · 16:9 슬라이드 템플릿
├── design-system/         The spec, published via Pages · 디자인 규격서 (Pages 로 공개)
├── web/                   Homepage stylesheet · 홈페이지 스타일시트
├── assets/                Logos and emblems · 로고 · 엠블럼
├── tools/                 PPTX / DOCX generator · 파워포인트 · 워드 생성기
├── .claude/skills/        The design system as a Claude Code skill · 클로드 코드 스킬 판
└── *.js                   Viewer and print engines · 뷰어 · 인쇄 엔진
```

**Why one repository.** The templates and the spec change together. Change a
colour and the documents, the slides, the CSS and the spec all move at once. Split
the repository and that is four commits and four versions drifting apart. Kept
together, one commit *is* "the whole design system at this moment".

**한 저장소로 둔 이유.** 템플릿과 규격서는 같이 바뀝니다. 색을 바꾸면
문서 · 슬라이드 · CSS · 규격서가 동시에 수정됩니다. 저장소를 나누면 네 번 커밋하고
네 곳의 버전이 어긋납니다. 하나로 두면 커밋 하나가 곧 "이 시점의 디자인 시스템
전체"입니다.

**Why HTML is the source.** A `.pptx` or `.docx` in the repository is a binary:
no diff, no visible history, and the layout shifts between PowerPoint versions.
HTML is text, so a commit shows exactly what changed, and a browser is all anyone
needs to get the same result. The Office files still get made — but at release
time, from the HTML (§5).

**HTML로 배포하는 이유.** PPTX · DOCX를 저장소에 두면 바이너리라 변경 이력이
남지 않고(diff가 불가능), 파워포인트 버전에 따라 레이아웃이 깨집니다. HTML은
텍스트라 무엇이 바뀌었는지 커밋에서 그대로 보이고, 브라우저만 있으면 어디서든
같은 결과가 나옵니다. Office 파일은 릴리스 시점에 HTML 로부터 생성합니다 (§5).

---

## 3. Three delivery paths · 세 갈래 배포

### (A) Releases — for students · 학생용 다운로드

The path that matters most. A student never needs to understand the repository.

가장 중요한 경로입니다. 학생은 저장소 구조를 몰라도 됩니다.

- **Releases** on the right → the latest version → download<br>저장소 우측 **Releases** → 최신 버전 → 다운로드
- `hbrlrg-templates.zip` is everything; unzip and double-click `slides/slides-en.html`<br>`hbrlrg-templates.zip` 은 전체 묶음. 압축을 풀고 `slides/slides-en.html` 을 더블클릭하면 바로 열립니다
- Or take a single Office file — `hbrlrg-slides.pptx`, `hbrlrg-plain-kr.docx` and so on<br>또는 Office 파일 하나만 — `hbrlrg-slides.pptx`, `hbrlrg-plain-kr.docx` 등
- Each release carries notes on what changed, so it's clear whether your copy is current<br>릴리스마다 "무엇이 바뀌었는지" 노트가 붙으므로, 지금 쓰는 게 최신인지 알 수 있습니다

**Why a zip as well as loose files.** The slide HTML can't stand alone — it needs
`deck-stage.js`, `image-slot.js` and `assets/` beside it. Take only the one file
and the logos break and navigation stops working. The zip bundles that dependency
whole. The Office files, by contrast, are self-contained, so they are offered
individually.

**왜 zip 과 개별 파일을 함께 두는가.** 슬라이드 HTML은 혼자 못 돕니다.
`deck-stage.js`, `image-slot.js`, `assets/` 가 옆에 있어야 합니다. 파일 하나만
받아 가면 로고가 깨지고 넘김이 안 됩니다. zip은 이 의존을 통째로 묶습니다.
반면 Office 파일은 자체로 완결되므로 하나씩 받을 수 있게 두었습니다.

### (B) GitHub Pages — reading the spec · 규격서 열람

`design-system/index.html` published on the web, with the root redirecting to it.

`design-system/index.html` 을 웹으로 공개하고, 루트는 그곳으로 보냅니다.

```
https://hbrleelab.github.io/design/
```

One link shows the colour values, type, spacing and usage rules, and the page has
a KO / EN switch. Send this address when a new student joins, when working with an
outside designer, or when matching figure colours for a paper.

링크 하나로 색상값 · 서체 · 간격 · 사용 규칙을 보여 줄 수 있고, 페이지에 한글 · 영문
전환 버튼이 있습니다. 새 학생을 받을 때, 외부 디자이너와 일할 때, 논문 도표 색을
맞출 때 이 주소만 보내면 됩니다.

### (C) The repository itself — maintainers and developers · 관리자 · 개발자용

Whoever builds the homepage clones `web/hbrlrg.css` directly. Whoever edits a
template works here too.

홈페이지 작업자는 `web/hbrlrg.css` 를 직접 clone 해서 씁니다.
템플릿을 고치는 사람도 여기를 봅니다.

---

## 4. One-time setup · 최초 설정 (한 번만)

Already done — recorded here in case the repository is ever rebuilt.

이미 완료된 항목입니다. 저장소를 다시 만들 경우를 위해 기록해 둡니다.

### 4-1. GitHub Pages

**Settings** → **Pages**

- Source: `Deploy from a branch`
- Branch: `main` / `/ (root)`
- Save

The repository must be **public**, or Pages needs a paid plan. Making the
repository private silently switches Pages off and the address starts 404-ing.

저장소가 **공개**여야 합니다. 비공개면 Pages 는 유료 플랜이 필요합니다. 공개를
비공개로 바꾸면 Pages 가 조용히 꺼지고 주소가 404 를 냅니다.

`.nojekyll` in the root tells Pages to serve the files as they are instead of
running them through Jekyll. Don't delete it.

루트의 `.nojekyll` 은 Pages 가 Jekyll 을 거치지 않고 파일을 그대로 내보내게 합니다.
지우지 마세요.

### 4-2. The release workflow · 릴리스 워크플로

`.github/workflows/release.yml` does the whole release. Nothing to set up beyond
the file itself; it runs with the repository's own `GITHUB_TOKEN`.

`.github/workflows/release.yml` 이 릴리스 전체를 처리합니다. 파일 외에 준비할 것은
없고, 저장소의 `GITHUB_TOKEN` 으로 동작합니다.

---

## 5. Releasing a new version · 갱신 절차

Two steps. · 두 단계입니다.

```bash
# 1. commit the change · 바뀐 파일 커밋
git add .
git commit -m "슬라이드 표지 로고 배치 조정"
git push -u origin main
```

2. **Actions** → **Release templates** → **Run workflow** → type the version
   (e.g. `v1.4`) → **Run**<br>
   **Actions** → **Release templates** → **Run workflow** → 버전 입력
   (예: `v1.4`) → **Run**

That's it. The workflow creates the tag, so there is no `git tag` to push.

끝입니다. 태그는 워크플로가 만들어 주므로 `git tag` 를 밀 필요가 없습니다.

Pages updates itself the moment you push, so there is nothing separate to do for
the spec page.

Pages 는 push 하는 순간 자동으로 갱신되므로 규격서는 따로 할 일이 없습니다.

### What the workflow does · 워크플로가 하는 일

1. Checks the version looks like `v` + a number, so a typo can't create a strange tag<br>버전이 `v` + 숫자 형식인지 검사 — 오타로 엉뚱한 태그가 생기는 것을 막습니다
2. Fetches Archivo (SIL OFL) from its own repository at build time<br>Archivo(SIL OFL)를 빌드 시점에 원 저장소에서 받아 옵니다
3. Runs `tools/build_office.py` to generate one `.pptx` and four `.docx` from the design tokens<br>`tools/build_office.py` 로 디자인 토큰에서 `.pptx` 1개와 `.docx` 4개를 생성합니다
4. Embeds the four Archivo styles into the `.pptx`<br>`.pptx` 에 Archivo 4종을 임베드합니다
5. Zips everything and publishes the release, attaching the zip and the five Office files<br>전체를 zip 으로 묶고 릴리스를 발행하면서 zip 과 Office 파일 5개를 첨부합니다

Archivo is fetched rather than committed because it is a third-party font under
SIL OFL; keeping it out of the repository keeps the licence boundary clean and the
repository small.

Archivo 는 SIL OFL 의 외부 폰트라 커밋하지 않고 받아 옵니다. 라이선스 경계가
분명해지고 저장소도 가벼워집니다.

**A trap.** Pushing a tag from inside a Claude Code cloud session is blocked by
the egress proxy (403), and `git push --dry-run` passes anyway — so it looks like
it will work and then doesn't. That is why the workflow takes a version as an
input instead of triggering on a tag push. A tag push still works from a normal
machine.

**함정.** 클라우드 세션에서 태그를 푸시하면 프록시가 차단합니다(403). 게다가
`git push --dry-run` 은 통과하므로 될 것처럼 보이다 실패합니다. 그래서 워크플로가
태그 푸시 대신 버전을 입력으로 받습니다. 일반 PC 에서는 태그 푸시도 그대로 됩니다.

---

## 6. Office files · Office 파일

The HTML slides present as they are and print to PDF. Still, a co-author sometimes
has to edit in PowerPoint, and some conferences only accept a Word form. Each
release therefore attaches Office versions built from the same HTML.

HTML 슬라이드는 그대로 발표할 수 있고 PDF로도 나옵니다. 그래도 공동 저자가
파워포인트로 편집해야 하거나, 학회가 워드 양식만 받는 경우가 있습니다. 그래서
릴리스마다 같은 HTML 에서 만든 Office 판을 첨부합니다.

| | Font embedding · 폰트 임베드 | Sending it outside · 외부 발송 |
| --- | --- | --- |
| `hbrlrg-slides.pptx` | Archivo, 4 styles · Archivo 4종 | Latin type holds; Korean needs Pretendard installed<br>영문은 유지됨, 한글은 Pretendard 설치 필요 |
| `hbrlrg-*.docx` | None — not possible via `python-docx`<br>불가 (`python-docx` 한계) | **Export to PDF** · **PDF 로 내보내기** |

Only HTML lives under `slides/` and `documents/`. Version-controlling the Office
files would leave no usable history and only make the repository heavy. They are
release **artefacts**, not sources — which also means a hand-edited copy will be
overwritten by the next release.

저장소 본문(`slides/`, `documents/`)에는 HTML만 둡니다. Office 파일을 버전 관리
대상으로 삼으면 이력이 남지 않고 저장소만 무거워집니다. Office 파일은 릴리스에 붙은
**산출물**이지 소스가 아닙니다 — 직접 고쳐 둔 사본은 다음 릴리스에서 덮입니다.

---

## 7. Version numbers · 버전 번호 규칙

| Situation · 상황 | Example · 예 |
| --- | --- |
| The system as a whole changes — colour, type · 색 · 서체 등 시스템 전반이 바뀜 | `v2.0` |
| A layout is added or removed, structure changes · 레이아웃 추가 · 삭제, 구조 변경 | `v1.2` |
| A typo, a contact detail, the affiliation wording · 오타 · 연락처 · 소속 표기 수정 | `v1.1.1` |

Release notes say only *what changed*. A student has to be able to tell whether
they need to re-download for their own talk.

릴리스 노트에는 "무엇이 바뀌었나"만 적습니다. 학생이 자기 발표 자료를
새로 받아야 하는지 판단할 수 있어야 합니다.

---

## 8. What not to do · 권장하지 않는 방법

| Approach · 방법 | Why not · 왜 |
| --- | --- |
| Scatter files in the repository root · 파일을 저장소 루트에 흩뿌리기 | Nobody can tell what is current · 무엇이 최신인지 알 수 없음 |
| Commit `.pptx` / `.docx` as sources · PPTX · DOCX를 소스로 커밋 | No diff, growing size, renders differently per version · diff 불가, 용량 증가, 버전별 렌더 차이 |
| A repository per template · 템플릿마다 저장소 분리 | One colour change becomes four commits · 색 하나 바꾸는 데 커밋 네 번 |
| Hand files out by email or messenger · 이메일 · 메신저로 파일 배포 | Two months later nobody has the current one · 두 달 뒤 아무도 최신본을 모름 |
| `main` only, no releases · 릴리스 없이 main 브랜치만 | No way to tell which state a student is using · 학생이 어느 시점 파일을 쓰는지 추적 불가 |

---

## 9. Decisions on record · 결정 사항

- **Repository visibility · 저장소 공개 여부** — **public**. It holds only logos
  and templates, Pages is then free, and students download without signing in.
  Note that switching to private turns Pages off.<br>
  **공개**입니다. 로고와 템플릿만 있고, 공개하면 Pages 를 무료로 쓰며 학생이 로그인
  없이 받아 갑니다. 비공개로 바꾸면 Pages 가 꺼진다는 점에 주의하세요.
- **ACS logo · ACS 로고** — ✅ cleared. `assets/cm-logo-onnavy.png` (the Chemistry
  of Materials logo recoloured to the brand) may be used.<br>
  ✅ 확인 완료. `assets/cm-logo-onnavy.png` (Chemistry of Materials 로고를 브랜드
  색으로 재색상) 사용 가능합니다.
- **Contact address · 연락처** — ✅ done. `hbrlee@unist.ac.kr` throughout; the old
  `hbrlee.unist@gmail.com` no longer appears anywhere. The web address is
  `https://hbrl-research.group`.<br>
  ✅ 교체 완료. 전 파일이 `hbrlee@unist.ac.kr` 이고 옛 주소
  `hbrlee.unist@gmail.com` 은 남아 있지 않습니다. 웹 주소는
  `https://hbrl-research.group` 입니다.
- **Fonts in Word · 워드의 폰트** — ⏳ open. `.docx` can't embed fonts, so a
  recipient without Archivo and Pretendard sees substituted type. The current
  answer is "export to PDF". If it becomes a real problem, the options are to
  ship the Office files as PDF as well, or to move to a `.dotx` template that
  assumes the fonts are installed on lab machines.<br>
  ⏳ 미해결. `.docx` 는 폰트를 심을 수 없어 Archivo · Pretendard 가 없는 상대는
  대체 서체로 봅니다. 현재 답은 "PDF 로 내보내기"입니다. 문제가 커지면 Office
  파일의 PDF 판을 함께 배포하거나, 연구실 PC 에 폰트 설치를 전제한 `.dotx`
  템플릿으로 가는 방법이 있습니다.

Whenever a contact detail or the affiliation changes, **publish a new release**.
A zip already downloaded still carries the old wording, so the release note has to
say "contact changed — download again" for students to actually refresh.

연락처나 소속 표기가 바뀌면 **반드시 새 릴리스를 배포**하세요. 이미 받아 간 zip에는
옛 내용이 그대로 남아 있으므로, 릴리스 노트에 "연락처 변경 — 재다운로드 필요"를
명시해야 학생들이 새로 받습니다.
