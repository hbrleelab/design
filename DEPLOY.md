# 배포 구조 분석 · 운영 가이드

`hbrleelab/design` 저장소를 "학생들이 항상 최신 템플릿을 받아 가는 곳"으로
운영하기 위한 구조입니다. 설계 근거와 실제 절차를 함께 적었습니다.

---

## 1. 무엇을 푸는 문제인가

세 가지 요구가 있습니다.

1. **배포** — 학생이 최신 슬라이드·문서 템플릿을 쉽게 받아 간다
2. **갱신** — 템플릿이 바뀔 때마다 다시 올린다
3. **참조** — 디자인 규격(색·서체·간격)을 언제든 열어 본다

세 가지는 서로 다른 형태를 원합니다. 다운로드는 **파일**, 규격서는 **웹페이지**,
갱신 이력은 **버전**입니다. 하나의 방식으로 셋을 다 덮으려 하면 어딘가 불편해집니다.
아래 구조는 셋을 분리하되 한 저장소 안에 둡니다.

---

## 2. 저장소 구조

```
hbrleelab/design
├── README.md              ← 저장소 첫 화면. 다운로드 링크와 사용법
├── DEPLOY.md              ← 이 문서
├── documents/             ← A4 문서 4종
├── slides/                ← 16:9 슬라이드 템플릿
├── design-system/         ← 디자인 규격서 (GitHub Pages 로 공개)
├── web/                   ← 홈페이지 스타일시트
├── assets/                ← 로고·엠블럼
└── *.js                   ← 뷰어·인쇄 엔진
```

**한 저장소로 둔 이유.** 템플릿과 규격서는 같이 바뀝니다. 색을 바꾸면
문서·슬라이드·CSS·규격서가 동시에 수정됩니다. 저장소를 나누면 네 번 커밋하고
네 곳의 버전이 어긋납니다. 하나로 두면 커밋 하나가 곧 "이 시점의 디자인 시스템
전체"입니다.

**HTML로 배포하는 이유.** PPTX·DOCX를 저장소에 두면 바이너리라 변경 이력이
남지 않고(diff가 불가능), 파워포인트 버전에 따라 레이아웃이 깨집니다. HTML은
텍스트라 무엇이 바뀌었는지 커밋에서 그대로 보이고, 브라우저만 있으면 어디서든
같은 결과가 나옵니다. PDF는 인쇄로 뽑고, PPTX가 꼭 필요한 사람은 아래
§6을 따릅니다.

---

## 3. 세 갈래 배포

### (A) Releases — 학생용 다운로드

가장 중요한 경로입니다. 학생은 저장소 구조를 몰라도 됩니다.

- 저장소 우측 **Releases** → 최신 버전 → `hbrlrg-templates.zip` 다운로드
- 압축을 풀면 폴더 그대로. `slides/slides-en.html` 을 더블클릭하면 바로 열립니다
- 릴리스마다 "무엇이 바뀌었는지" 노트가 붙으므로, 지금 쓰는 게 최신인지 알 수 있습니다

**왜 zip인가.** 슬라이드 HTML은 혼자 못 돕니다. `deck-stage.js`, `image-slot.js`,
`assets/` 가 옆에 있어야 합니다. 파일 하나만 받아 가면 로고가 깨지고 넘김이
안 됩니다. zip은 이 의존을 통째로 묶습니다.

### (B) GitHub Pages — 규격서 열람

`design-system/index.html` 을 웹으로 공개합니다.

```
https://hbrleelab.github.io/design/
```

링크 하나로 색상값·서체·간격·사용 규칙을 보여 줄 수 있습니다. 새 학생을 받을 때,
외부 디자이너와 일할 때, 논문 도표 색을 맞출 때 이 주소만 보내면 됩니다.

### (C) 저장소 직접 — 관리자·개발자용

홈페이지 작업자는 `web/hbrlrg.css` 를 직접 clone 해서 씁니다.
템플릿을 고치는 사람도 여기를 봅니다.

---

## 4. 최초 설정 (한 번만)

### 4-1. 파일 올리기

이 프로젝트의 `repo/` 폴더 내용을 저장소 루트에 그대로 커밋합니다.

```bash
git clone https://github.com/hbrleelab/design.git
cd design
# 내려받은 repo/ 안의 파일을 여기에 복사
git add .
git commit -m "Add document, slide, and web templates"
git push
```

### 4-2. GitHub Pages 켜기

저장소 → **Settings** → **Pages**

- Source: `Deploy from a branch`
- Branch: `main` / `/ (root)`
- Save

1–2분 뒤 `https://hbrleelab.github.io/design/design-system/` 이 열립니다.
루트 주소로 바로 규격서를 열고 싶으면 저장소 루트에 아래 `index.html` 을 둡니다.

```html
<!DOCTYPE html>
<meta http-equiv="refresh" content="0; url=design-system/">
```

### 4-3. 첫 릴리스 만들기

저장소 → **Releases** → **Create a new release**

- Tag: `v1.0`
- Title: `v1.0 — 문서 · 슬라이드 템플릿`
- 본문에 변경 내용 요약
- **Attach binaries**: `hbrlrg-templates.zip` 업로드
- Publish

zip은 로컬에서 만듭니다.

```bash
zip -r hbrlrg-templates.zip documents slides assets *.js README.md
```

---

## 5. 갱신 절차 (템플릿이 바뀔 때마다)

디자인을 수정한 뒤, 매번 같은 네 단계를 밟습니다.

```bash
# 1. 바뀐 파일 커밋
git add .
git commit -m "슬라이드 표지 로고 배치 조정"
git push

# 2. zip 다시 만들기
zip -r hbrlrg-templates.zip documents slides assets *.js README.md

# 3. 새 태그
git tag v1.1
git push --tags
```

4. GitHub에서 **Releases → Draft a new release** → 태그 `v1.1` 선택 →
   zip 첨부 → Publish

Pages는 push 하는 순간 자동으로 갱신되므로 따로 할 일이 없습니다.

### 자동화 (선택)

3–4단계가 번거로우면 `.github/workflows/release.yml` 을 두어 태그를 밀 때
zip이 자동으로 만들어지고 릴리스가 생기게 할 수 있습니다.

```yaml
name: Release templates
on:
  push:
    tags: ['v*']
jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - name: Package
        run: zip -r hbrlrg-templates.zip documents slides assets *.js README.md
      - name: Publish
        uses: softprops/action-gh-release@v2
        with:
          files: hbrlrg-templates.zip
          generate_release_notes: true
```

이후로는 `git tag v1.2 && git push --tags` 한 줄이면 배포가 끝납니다.

---

## 6. PPTX가 필요한 경우

HTML 슬라이드는 그대로 발표할 수 있고 PDF로도 나옵니다. 그래도 공동 저자가
파워포인트로 편집해야 하는 상황이 있습니다. 그때는 이 프로젝트에서 PPTX로
내보낸 파일을 릴리스에 **함께 첨부**하세요 (`hbrlrg-slides.pptx`).

저장소 본문(`slides/`)에는 HTML만 둡니다. PPTX를 버전 관리 대상으로 삼으면
이력이 남지 않고 저장소만 무거워집니다. PPTX는 릴리스에 붙은 **산출물**이지
소스가 아닙니다.

---

## 7. 버전 번호 규칙

| 상황 | 예 |
| --- | --- |
| 색·서체 등 시스템 전반이 바뀜 | `v2.0` |
| 레이아웃 추가·삭제, 구조 변경 | `v1.2` |
| 오타·연락처·소속 표기 수정 | `v1.1.1` |

릴리스 노트에는 "무엇이 바뀌었나"만 적습니다. 학생이 자기 발표 자료를
새로 받아야 하는지 판단할 수 있어야 합니다.

---

## 8. 권장하지 않는 방법

| 방법 | 왜 |
| --- | --- |
| 파일을 저장소 루트에 흩뿌리기 | 무엇이 최신인지 알 수 없음 |
| PPTX·DOCX를 소스로 커밋 | diff 불가, 용량 증가, 버전별 렌더 차이 |
| 템플릿마다 저장소 분리 | 색 하나 바꾸는 데 커밋 네 번 |
| 이메일·메신저로 파일 배포 | 두 달 뒤 아무도 최신본을 모름 |
| 릴리스 없이 main 브랜치만 | 학생이 어느 시점 파일을 쓰는지 추적 불가 |

---

## 9. 결정 사항

- **저장소 공개 여부** — 로고와 템플릿만 있으므로 공개해도 무방합니다.
  공개하면 Pages를 무료로 쓸 수 있고 학생이 로그인 없이 받아 갑니다.
  비공개로 두면 Pages는 유료 플랜이 필요하고, 학생 계정을 협업자로
  일일이 추가해야 합니다. **공개 권장.**
- **ACS 로고** — ✅ 확인 완료. `assets/cm-logo-onnavy.png` (Chemistry of Materials
  로고를 브랜드 색으로 재색상) 사용 가능합니다.
- **연락처** — ⏳ **2026년 9월 1일 이후 공식 이메일로 교체 예정.**
  현재 `hbrlee.unist@gmail.com` 이 슬라이드·문서 20여 곳에 하드코딩되어 있습니다.

  ```bash
  # 확정 주소가 나오면 전 파일 일괄 교체
  grep -rl 'hbrlee.unist@gmail.com' documents/ slides/ \
    | xargs sed -i '' 's/hbrlee\.unist@gmail\.com/<새 주소>/g'
  ```

  교체 후에는 **반드시 새 릴리스를 배포**하세요. 이미 받아 간 zip에는 옛 주소가
  그대로 남아 있으므로, 릴리스 노트에 "연락처 변경 — 재다운로드 필요"를
  명시해야 학생들이 새로 받습니다.
