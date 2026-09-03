# HBRLRG 디자인 시스템 — 문서 작성 지침

HBRL Research Group (이한보람 교수 연구실, UNIST) 의 문서·슬라이드·웹 공통
디자인 규격입니다. 이 연구실 이름으로 나가는 문서를 만들 때 아래 규칙을 따르세요.

---

## 1. 색

| 이름 | 값 | 쓰는 곳 |
| --- | --- | --- |
| Navy | `#14243F` | 제목, 이름, 구분선, 어두운 배경 |
| Teal | `#0EA79A` | **강조색 하나뿐.** 구분선 캡, 불릿, CTA |
| Ink | `#2B2F36` | 본문 |
| Muted | `#6B7280` | 연락처, 캡션, 표 라벨, 보조 설명 |
| Faint | `#9AA1AB` | 문서 푸터 |
| Surface | `#F6F7F9` | 표 헤더 배경, 이미지 자리 |
| Border | `#E4E7EC` | 표 괘선, 구분선 |

**규칙**
- 강조색은 청록 하나입니다. 다른 색을 추가하지 마세요.
- 배경은 흰색 · `#F6F7F9` · Navy 세 가지만 씁니다.
- 청록은 작은 본문 글자색으로 쓰지 않습니다 (흰 배경에서 대비 2.99:1).
- 모서리는 각지게 (`border-radius: 0`). 예외는 6px 청록 불릿 사각(radius 2px)뿐.

---

## 2. 서체

| 서체 | 굵기 | 쓰는 곳 |
| --- | --- | --- |
| **Archivo** | 300 / 400 / 500 / 600 | 영문 전체, 제목, 숫자, 표 라벨, 로고 |
| **Pretendard** | 400 / 500 / 600 | 한글 본문 |

폰트 스택은 `'Archivo', 'Pretendard', -apple-system, 'Apple SD Gothic Neo', sans-serif`
순서로 지정합니다. Archivo에 한글이 없으므로 한글은 자동으로 Pretendard로 넘어갑니다.

CDN:
```html
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
```

**금지 서체** — Inter, Roboto, Arial, 맑은 고딕을 지정하지 마세요.

---

## 3. 문서 타입 스케일 (A4)

| 역할 | 크기 | 굵기 | 행간 | 색 |
| --- | --- | --- | --- | --- |
| 레터헤드 이름 | 24 pt | 300 | 1.05 | Navy |
| 문서 제목 (H1) | 20 pt | 600 | 1.25 | Navy |
| 섹션 제목 (H2) | 14 pt | 500 | 기본 | Navy |
| 본문 | 11 pt | 400 | 1.7 | Ink |
| 소속 | 9.5 pt | 400 | 1.5 | Navy |
| 표 본문 | 10 pt | 400 | 기본 | Ink |
| 연락처 · 표 캡션 | 8.5 / 9 pt | 400 | 1.5 | Muted |
| 표 헤더 라벨 | 8.5 pt | 500 | +0.06em | Muted |
| 푸터 | 7.5 pt | 400 | +0.07em | Faint |

용지 A4 세로, 여백 사방 18 mm, 1단.
간격 단위는 pt (5 · 6 · 8 · 10 · 16 · 18 · 20 · 22 · 26).

---

## 4. 시그니처 요소 세 가지

이 세 가지가 문서·슬라이드·웹을 하나로 묶습니다.

### 구분선 캡

폭 전체를 지나는 1.2 px Navy 선 위에, 좌측 정렬된 **46 × 3 px 청록 캡**을
얹습니다. 문서당 한 번만 등장합니다. 가운데 정렬이나 우측 배치는 하지 않습니다.

```html
<div style="position:relative;height:3px;">
  <div style="position:absolute;left:0;right:0;top:1px;height:1.2px;background:#14243F;"></div>
  <div style="position:absolute;left:0;top:0;width:46px;height:3px;background:#0EA79A;"></div>
</div>
```

### HBRLRG 로고

직접 그리지 말고 **공식 파일을 씁니다**. 심볼(엮힌 고리)과 워드마크가 결합된
가로형이 기본이며, 글자는 모두 아웃라인이라 서체 설치 없이 동일하게 렌더링됩니다.

| 배경 | 파일 |
| --- | --- |
| 밝은 배경 | `assets/hbrlrg-horizontal.svg` (또는 `.png`) |
| 어두운 배경 · 사진 위 | `assets/hbrlrg-horizontal-reverse.svg` |
| 심볼 단독 | `assets/hbrlrg-symbol.svg` · `-reverse.svg` |
| 앱 아이콘 · 프로필 | `assets/hbrlrg-icon.svg` |

```html
<img src="assets/hbrlrg-horizontal.png" alt="HBRLRG" style="height:27px;width:92px;display:block;">
```

**규칙**

- 비율 **573.5 : 169.1 (3.39 : 1)** 고정. 늘이거나 변형하지 마세요.
  높이만 지정하고 폭은 `높이 × 3.39` 로 계산해 명시합니다.
- 어두운 배경에서는 **색을 바꾸지 말고 파일을 바꾸세요** (reverse 버전).
- 최소 크기: 가로형 너비 120 px / 25 mm, 심볼 단독 24 px / 6 mm.
- 사용 높이: 문서 머리글 27 px, 슬라이드 푸터 42 px, 표지·맺음 68 px.
- 엮이는 지점의 틈새는 투명하게 뚫려 있어 어떤 배경 위에서도 매듭 구조가 유지됩니다.
- 재색상·그림자·회전·효과 금지.

### 불릿 사각

기호 대신 **청록 사각형**(radius 2px)을 씁니다. 첫 줄 텍스트의 **가운데**에
맞춥니다 — 위쪽에 맞추지 마세요.

`margin-top = (글자크기 × 행간 ÷ 2) − (사각크기 ÷ 2)`

11 pt / 1.6 본문 + 6 px 사각 → `margin-top: 6.5pt`.

```html
<div style="display:flex;gap:8pt;">
  <span style="flex:0 0 auto;width:6px;height:6px;border-radius:2px;background:#0EA79A;margin-top:6.5pt;"></span>
  <p style="margin:0;font-size:11pt;line-height:1.6;color:#2B2F36;">항목 내용</p>
</div>
```

---

## 5. 문서 템플릿 두 종

### 레터헤드 (외부 발신용)

추천서, 초청장, 공문, 저널 커버레터.

머리글 구성 — UNIST 엠블럼(88 × 88 px, 좌측 고정) + 24 px 간격 + 우측 정렬
텍스트 블록. 순서는 **이름 → 소속 → 연락처 → (겸직)**. 구분선은 헤더 아래 16 px.

본문 순서
1. 날짜 — 구분선 아래 26 pt
2. 수신처 — 위 16 pt
3. 인사말 — 위 18 pt
4. 본문 단락 — 단락 간 10 pt, 들여쓰기 없음
5. 맺음말 — 위 18 pt
6. 서명 블록 — 서명 여백 34 pt 확보

푸터 — `전화 · 이메일 · 홈페이지` 를 7.5 pt Faint로 가운데 정렬하고, 항목 사이는
점이 아니라 1 px 헤어라인(`#E4E7EC`, 높이 8 pt)으로 나눕니다. 모든 페이지에 반복.

**하지 않을 것** — 엠블럼과 HBRLRG 워드마크 동시 사용(**레터헤드 한정**. 슬라이드 표지·맺음은 §7-1 참조),
표·차트 삽입, 본문 3단락 초과.

### 기본 문서 (내부용)

실험 보고, 공정 조건서, 회의록, 매뉴얼.

머리글 — 좌측 HBRLRG 로고(높이 27 px), 우측 연락 정보(8.5 pt, 웹 · 이메일 순).
구분선은 헤더 아래 12 px. 푸터는 7.5 pt 대문자로 페이지마다 반복.

본문 순서
1. 제목 (H1) — 구분선 아래 24 pt
2. 메타 줄 — 작성자 · 날짜 · 버전
3. 섹션 (H2) — 위 20–22 pt, **번호 필수** (1. 2. 3.)
4. 본문 / 표 / 불릿 — 제목 아래 6–8 pt
5. 표 캡션 — 표 아래 5 pt, 9 pt Muted

**하지 않을 것** — UNIST 엠블럼 삽입(레터헤드 전용), 표에 수직 괘선·줄무늬,
H2를 두 단계 이상 세분화, 본문에 Navy 사용.

---

## 6. 표

**수직 괘선을 절대 넣지 않습니다.**

- 헤더: `#F6F7F9` 배경, 대문자 라벨 8.5 pt / 굵기 500 / 자간 +0.06em / Muted
- 행: 하단 괘선(`#E4E7EC`) 만
- 셀 패딩: 5 × 8 pt
- 캡션: 표 아래 5 pt, 9 pt Muted, 문장부호 없이 ("표 1. 조건 비교")
- 열은 3–5개 이내

---

## 7. 슬라이드 (1920 × 1080)

좌우 여백 120 px. 헤더는 상단 56 px에서 시작하고, **콘텐츠 영역은 268 px부터**
시작합니다. 그 아래는 데이터·플롯 자리로 비워 둡니다.

| 역할 | 크기 |
| --- | --- |
| 표지 제목 | 108 px / 600 |
| 섹션 제목 | 104 px / 600 |
| 슬라이드 제목 | 60 px / 600 |
| 본문 불릿 | 34 px / 1.4 |
| 큰 수치 | 118 px / 300 |
| 캡션 · 푸터 | 24 px |

**24 px 미만 글자를 쓰지 마세요.**

푸터 — 하단 44 px에 좌측 HBRLRG 로고(높이 42 px), 우측 `이메일 · 홈페이지`.
표지와 맺음 슬라이드는 예외(로고 로크업이 그 자리를 씁니다).

레이아웃 12종: 표지 · 목차 · 섹션 구분 · 본문 · 그림(전면) · 그림(2단) ·
그림+설명 · 표 · 수치 · 전면 이미지 · 인용 · 맺음.

### 7-1. 로고 로크업 (표지·맺음 전용)

표지와 맺음 슬라이드는 푸터 대신 **로고 로크업**을 씁니다. 로크업은 좌측 정렬 2단이며,
각 단은 `로고 + 직함 텍스트 2줄` 로 구성합니다.

| 요소 | 표지 | 맺음 |
| --- | --- | --- |
| UNIST 엠블럼 | 115 × 121 px | 79 × 84 px |
| Chemistry of Materials 로고 | 216 × 59 px | 158 × 43 px |
| 로고 → 텍스트 간격 | 엠블럼 35 px · CM 43 px | 동일 |
| 텍스트 | 26 px, `#93A2BC`, 2줄, 행간 1.3 | 25 px |

- CM 로고 높이는 항상 **엠블럼 높이의 0.49배**로 맞춥니다. 폭 기준으로 맞추면 CM이 커 보입니다.
- 텍스트는 로고에 대해 세로 가운데 정렬합니다.
- 로크업 위에는 1 px Navy-rule(`#2C4066`)과 이름(48 px / 600)이 옵니다.
- 표지에서는 HBRLRG 로고(좌상단, 높이 68 px)와 엠블럼이 함께 놓입니다. 역할이 다르기 때문입니다 —
  로고는 발신 주체, 엠블럼·CM은 소속 증빙.

표지 좌표 (1920 × 1080 기준, 1 px = 0.5 pt)

| 요소 | x | y |
| --- | --- | --- |
| 구분선 (`#2C4066`, 폭 전체 × 1 px) | 120 | 579 |
| 이름 (48 px / 600 / 흰색) | 120 | 619 |
| UNIST 엠블럼 | 120 | 691 |
| 소속 텍스트 (폭 648 px) | 270 | 700 |
| CM 로고 | 943 | 723 |
| 편집 직함 텍스트 (폭 598 px) | 1202 | 700 |

맺음 슬라이드는 표지의 축소판입니다. 두 로고를 가로로 나란히 두고 그 아래 소속 4줄(25 px).

원본 비율 — 변형하지 마세요. UNIST 엠블럼 **0.955 : 1**, Chemistry of Materials **3.70 : 1**.

**하지 않을 것** — 본문 슬라이드에 엠블럼·CM 로고 삽입(푸터의 HBRLRG 로고만),
가운데 정렬, 로고를 청록/네이비 배경 위에 흰 박스 없이 얹기(CM 로고는 자체 흰 박스를 포함한 형태를 씁니다).

---

## 8. 소속 표기 — 정확히 이대로

줄이거나 순서를 바꾸지 마세요. 영문에서 `&` 를 `and` 로 풀지 마세요.

- **영문** Professor, Graduate School of Semiconductor Materials & Devices Engineering, Ulsan National Institute of Science and Technology (UNIST)
- **국문** 울산과학기술원(UNIST) 반도체소재부품대학원 교수
- **편집 직함** Executive Editor, Chemistry of Materials, ACS Publications
- **주소** 50 UNIST-gil, Ulju-gun, Ulsan 44919, Republic of Korea
- **이메일** hbrlee@unist.ac.kr
- **홈페이지** https://hbrl-research.group
- **연구실** HBRL Research Group / HBRLRG
- **로고 병기** UNIST 엠블럼과 Chemistry of Materials 로고는 위 소속 문구와 **항상 함께** 놓습니다.
  로고만 단독으로 쓰지 않습니다.

---

## 9. 글쓰기

- 사실을 그대로 전달합니다. 의미를 부풀리는 해설을 붙이지 않습니다.
- 이모지를 쓰지 않습니다.
- 과한 강조(굵게·밑줄 남용)를 피합니다.
- 표와 수치는 필요한 것만 넣습니다. 빈 칸을 채우려고 데이터를 만들지 않습니다.
- 여백을 아끼지 않습니다. 한 페이지에 밀어 넣기보다 덜어냅니다.

---

## 10. 이 폴더의 파일

| 파일 | 용도 |
| --- | --- |
| `letterhead-en.html` / `letterhead-kr.html` | 레터헤드 문서 마크업 |
| `plain-en.html` / `plain-kr.html` | 기본 문서 마크업 |
| `hbrlrg.css` | 웹용 스타일시트 (토큰 + 컴포넌트) |
| `assets/hbrlrg-horizontal.svg` (+ `.png`) | HBRLRG 가로형 로고 — 밝은 배경용 |
| `assets/hbrlrg-horizontal-reverse.svg` (+ `.png`) | 가로형 로고 — 어두운 배경용 |
| `assets/hbrlrg-symbol.svg` · `-reverse.svg` | 심볼 단독 |
| `assets/hbrlrg-icon.svg` | 앱 아이콘 · 프로필 |
| `assets/unist-emblem.svg` (+ `.png`) | UNIST 엠블럼 — 밝은 배경용 / 네이비 배경용 2종 |
| `assets/cm-logo.svg` (+ `.png`) | Chemistry of Materials 로고 |

HTML 파일은 서체를 CDN으로 불러오므로 각 3–7 KB입니다. 새 문서를 만들 때
해당 파일의 마크업을 그대로 복제하고 내용만 바꾸세요.
