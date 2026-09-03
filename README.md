# HBRLRG Design

HBRL Research Group (UNIST) 의 문서 · 슬라이드 · 웹 디자인 시스템 저장소.
연구실 구성원이라면 누구나 여기서 최신 템플릿을 받아 쓸 수 있습니다.

**최신 템플릿 받기** → [Releases](../../releases/latest) 에서 `hbrlrg-templates.zip` 다운로드
**디자인 규격 보기** → https://hbrleelab.github.io/design/

---

## 무엇이 들어 있나

```
documents/          A4 문서 템플릿
  letterhead-kr.html    레터헤드 (국문)
  letterhead-en.html    레터헤드 (영문)
  plain-kr.html         기본 문서 (국문)
  plain-en.html         기본 문서 (영문)

slides/             16:9 슬라이드 템플릿 (1920×1080)
  slides-en.html        12종 레이아웃

design-system/      디자인 규격서 (색 · 서체 · 간격 · 사용 규칙)
  index.html                              브라우저로 보는 규격서
  HBRLRG-design-system.md                 같은 내용의 텍스트 판
                                          (클로드 등 AI 도구에 읽히는 용도)

web/                홈페이지
  hbrlrg.css                              스타일시트 (토큰 + 컴포넌트)
  index.html                              참조 구현
  HANDOFF.md                              개발자용 적용 안내서

assets/
  logo/                                   HBRLRG 로고 전체 세트
    hbrlrg-horizontal.svg / .png            가로형 (기본)
    hbrlrg-horizontal-reverse.svg / .png    가로형 · 어두운 배경용
    hbrlrg-horizontal-mono.svg / .png       가로형 · 단색
    hbrlrg-horizontal-reverse-on-navy.*     네이비 배경 포함 (미리보기용)
    hbrlrg-vertical.svg / -mono.svg         세로형
    hbrlrg-symbol.svg / -reverse / -mono    심볼 단독
    hbrlrg-icon.svg / -icon.png / -icon-512.png   앱 아이콘 · 프로필
    hbrlrg-favicon-64.png                   파비콘
    README.txt                              로고 규격 (색 · 서체 · 최소 크기)
  unist-emblem.png                        UNIST 엠블럼 (밝은 배경)
  unist-emblem-onnavy.png                 UNIST 엠블럼 (네이비 배경)
  cm-logo-onnavy.png                      Chemistry of Materials 로고

deck-stage.js       슬라이드 뷰어 (탐색 · 발표자 노트 · 인쇄)
image-slot.js       이미지 자리표시자 (드래그 앤 드롭)
doc-page.js         A4 인쇄 레이아웃 엔진
```

---

## 쓰는 법

### 문서

1. `documents/` 에서 필요한 파일을 브라우저로 엽니다
2. 화면에서 바로 글자를 고칩니다
3. 인쇄(⌘P / Ctrl+P) → **PDF로 저장**

A4 여백(18 mm)과 페이지 나눔은 자동입니다. `@page` 설정을 따로 만들지 마세요.

### 슬라이드

1. `slides/slides-en.html` 을 브라우저로 엽니다
2. ← → 키로 넘기고, 하단 썸네일에서 슬라이드를 고르거나 순서를 바꿉니다
3. 필요 없는 레이아웃은 썸네일에서 우클릭 → 삭제
4. 회색 이미지 영역에 플롯·현미경 사진을 **끌어다 놓으면** 채워집니다
5. 인쇄 → PDF로 저장 (슬라이드당 한 장)

레이아웃 12종: 표지 · 목차 · 섹션 구분 · 본문 · 그림(전면) · 그림(2단) ·
그림+설명 · 표 · 수치 · 전면 이미지 · 인용 · 맺음.

발표 데이터가 중심이므로 모든 본문 슬라이드는 상단 268 px 아래를
**비워 두도록** 설계했습니다. 플롯을 붙일 자리입니다.

### 홈페이지

`web/hbrlrg.css` 를 기존 스타일시트 **뒤에** 불러오면 됩니다. 빌드 도구 불필요.
`web/index.html` 을 브라우저로 열면 모든 컴포넌트의 올바른 마크업을 볼 수 있고,
적용 절차와 주의사항은 `web/HANDOFF.md` 에 정리돼 있습니다.

### AI 도구에 규격 전달

`design-system/HBRLRG-design-system.md` 한 파일이면 됩니다. 색·서체·간격·로고 규칙과
소속 표기가 모두 텍스트로 정리돼 있어, 클로드 프로젝트 지식이나 대화에 그대로 넣어
쓸 수 있습니다. 문서 마크업까지 참고시키려면 `documents/` 의 HTML을 함께 넣으세요.

---

## 브랜드 기본값

| 항목 | 값 |
| --- | --- |
| Navy (주색) | `#14243F` |
| Teal (강조색) | `#0EA79A` |
| 본문 텍스트 | `#2B2F36` |
| 보조 텍스트 | `#6B7280` |
| 표 헤더 배경 | `#F6F7F9` |
| 로고 · 영문 제목 서체 | Archivo |
| 한글 본문 서체 | Pretendard |

로고는 가로형이 기본이며 비율 573.5 : 169.1을 유지합니다. 어두운 배경에는 반드시
reverse 파일을 씁니다 (색을 바꾸지 말고 파일을 바꿉니다). 최소 크기는 가로형 너비
120 px / 25 mm 입니다.

강조색은 **하나뿐**입니다. 구분선 캡, 불릿, CTA에만 씁니다.
모서리는 각지게 유지합니다(radius 0). 이 두 가지가 문서 · 슬라이드 · 웹을
하나로 묶는 규칙입니다.

---

## 소속 표기

줄이거나 순서를 바꾸지 마세요.

- **영문** Professor, Graduate School of Semiconductor Materials & Devices Engineering, Ulsan National Institute of Science and Technology (UNIST)
- **국문** 울산과학기술원(UNIST) 반도체소재부품대학원 교수
- **편집 직함** Executive Editor, Chemistry of Materials, ACS Publications
- **주소** 50 UNIST-gil, Ulju-gun, Ulsan 44919, Republic of Korea

---

## 기여 · 수정 요청

템플릿에 문제가 있거나 새 레이아웃이 필요하면
[Issues](../../issues) 에 남겨 주세요. 수정은 관리자가 반영한 뒤
새 릴리스로 배포합니다.

배포 절차는 [`DEPLOY.md`](DEPLOY.md) 참고.
