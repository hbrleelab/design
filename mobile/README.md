# Mobile document template · 휴대폰용 문서 템플릿

For documents that get sent over KakaoTalk and read on a phone. A5 portrait
instead of A4, and far less template than the A4 documents carry.

카톡으로 보내 휴대폰에서 읽는 문서용입니다. A4 대신 A5 세로이고, A4 문서
템플릿보다 요소를 많이 덜어냈습니다.

**Get a PDF · PDF 만들기** → `python3 mobile/md2pdf.py 원고.md 결과.pdf`
**Edit in a browser · 브라우저에서 고치기** → `mobile/hbrlrg-mobile.html`
**Sample · 샘플** → [`sample/hbrlrg-mobile-sample.pdf`](sample/hbrlrg-mobile-sample.pdf)

---

## What is different from the A4 templates · A4 템플릿과 다른 점

| | A4 documents · A4 문서 | Mobile · 휴대폰용 |
| --- | --- | --- |
| Page · 판형 | 210 × 297 mm, 18 mm margins | **148 × 210 mm (A5), 12 mm** |
| Body type · 본문 | 11 pt | **11.5 pt** — not reduced · 줄이지 않음 |
| Logo · 로고 | Header, every page · 머리글, 모든 쪽 | **Cover only · 표지에만** |
| Running header · 머리말 | Yes · 있음 | **None · 없음** |
| Running footer · 꼬리말 | Affiliation, every page · 소속, 모든 쪽 | **None · 없음** |
| Rule device · 장식선 | Teal-capped rule · 청록 캡 구분선 | **None · 없음** |
| Wide tables · 넓은 표 | Table · 표 그대로 | **Cards · 카드** |

What carries the identity here is three things only: the logo on the cover, the
two brand colours, and the heading typeface. That is the whole template.

여기서 정체성을 지탱하는 것은 세 가지뿐입니다 — 표지의 로고, 브랜드 두 색,
제목 서체. 템플릿은 그게 전부입니다.

**Type is not scaled down for the smaller page.** The same words take more
pages, which is the right trade on a phone: scrolling is free, squinting is not.

**쪽이 작아졌다고 글자를 줄이지 않았습니다.** 같은 분량이 더 많은 쪽을 차지하는데,
휴대폰에서는 그 편이 맞습니다. 넘기는 것은 공짜지만 눈을 찌푸리는 것은 아닙니다.

---

## Markdown to PDF · 마크다운에서 PDF

```bash
pip install playwright markdown lxml        # 최초 1회
python3 mobile/md2pdf.py 원고.md 결과.pdf
```

Front matter sets the cover. Everything is optional; with no `title` the cover
page is skipped entirely.

앞머리(front matter)가 표지를 만듭니다. 모두 선택 사항이고, `title` 이 없으면
표지 자체를 넣지 않습니다.

```markdown
---
title: 하와이 오아후 식당 안내
subtitle: 학회 출장 중 걸어서 갈 만한 곳과, 차를 빌려야 하는 곳
date: 2026년 10월 · HBRL Research Group
lang: ko
cover: true
---

# 첫 번째 장

본문...
```

Useful flags · 쓸 만한 옵션

| Flag | Effect · 하는 일 |
| --- | --- |
| `--page "90mm x 195mm"` | A phone-shaped page instead of A5 · A5 대신 휴대폰 비율 |
| `--margin 10mm` | Narrower margins · 여백 조정 |
| `--html` | Keep the intermediate HTML · 중간 HTML 을 남김 |
| `--fonts DIR` | Font cache folder · 폰트 캐시 폴더 |

The first run downloads Archivo and Pretendard into `.fonts/` and reuses them
afterwards. They are embedded into the PDF, so the document reads correctly on
a phone that has neither installed — which is every phone.

처음 실행할 때 Archivo 와 Pretendard 를 `.fonts/` 에 받아 두고 이후 재사용합니다.
PDF 에 임베드되므로 두 서체가 없는 휴대폰에서도 제대로 보입니다 — 사실상 모든
휴대폰이 그렇습니다.

---

## Tables · 표

The rule is the column count, decided when the PDF is built.

열 수로 정해지며, PDF 를 만드는 시점에 결정됩니다.

**Four columns or fewer — left as a table.** It will not be cut across a page
boundary. If a table is simply taller than one page it has to split, and then
the header row repeats on the next page.

**4열 이하 — 표 그대로 둡니다.** 쪽 경계에서 잘리지 않습니다. 표 자체가 한 쪽보다
길면 나뉠 수밖에 없는데, 그때는 머리글 줄이 다음 쪽에 다시 나옵니다.

**Five columns or more — one card per row.** On a 124 mm measure, five columns
leave about 24 mm each: two or three Korean syllables before the text wraps. The
table has to become something else, not merely get smaller. The first column
becomes the card's title, and every other column heading follows its value as a
label.

**5열 이상 — 한 행이 카드 한 장이 됩니다.** 124 mm 폭에서 5열이면 한 칸이 약
24 mm, 한글 두세 글자에서 줄이 바뀝니다. 표를 줄이는 게 아니라 다른 것으로
바꿔야 합니다. 첫 열이 카드 제목이 되고, 나머지 열의 머리글은 값의 라벨로
따라갑니다.

Writing cards by hand (when not going through `md2pdf.py`) · 손으로 쓸 때

```html
<div class="cards">
  <div class="card">
    <div class="card__title">항목 이름</div>
    <div class="card__row"><span class="card__key">라벨</span><span class="card__val">값</span></div>
  </div>
</div>
```

---

## The logo · 로고

This template exists because a logo came out stretched, so the rule is worth
stating twice.

이 템플릿은 로고가 늘어나서 만들어졌으므로, 규칙을 두 번 적어 둡니다.

**Set one dimension only.** `height: 11mm; width: auto`. The artwork is
2400 × 708 (3.39 : 1) and supplies the other dimension itself. Giving both is
what flattens it.

**한쪽 치수만 지정하세요.** `height: 11mm; width: auto`. 원본이 2400 × 708
(3.39 : 1)이라 나머지는 파일이 알아서 정합니다. 둘 다 적으면 찌그러집니다.

**That is not sufficient on its own.** If the parent is a flexbox or a grid, the
image stretches across the cross axis and `width: auto` does nothing to stop it.
The cover here is a column flexbox, and before `align-self: flex-start` was
added the logo measured **232% wider than its true proportion** — the same fault
the A4 attempt had. The stylesheet therefore pins the logo's own alignment
rather than trusting whatever container it lands in, and adds
`object-fit: contain` as a last-resort net.

**그것만으로는 부족합니다.** 부모가 flexbox 나 grid 면 이미지가 교차축으로
늘어나고, `width: auto` 로는 막지 못합니다. 이 표지가 세로 flexbox 인데,
`align-self: flex-start` 를 넣기 전에는 로고가 **원본 비율보다 232% 넓게**
측정됐습니다. A4 에서 났던 것과 같은 문제입니다. 그래서 스타일시트는 컨테이너를
믿지 않고 로고 자신의 정렬을 못박고, `object-fit: contain` 을 최후의 안전망으로
둡니다.

To check it in any document · 어떤 문서에서든 확인하는 법

```bash
python3 -c "
from PIL import Image
im = Image.open('assets/logo/hbrlrg-horizontal.png')
print('원본 비율 %.4f' % (im.width / im.height))"   # 3.3898
```

Then compare against the rendered box. Anything beyond about 1% is a bug.

렌더된 박스와 비교하세요. 1% 를 넘으면 버그입니다.

---

## What has been checked · 검증한 것

The sample PDF in `sample/` was generated by this pipeline and inspected:

`sample/` 의 샘플 PDF 는 이 파이프라인으로 만들어 확인한 것입니다.

| Checked · 확인 | Result · 결과 |
| --- | --- |
| Logo proportion · 로고 비율 | Rendered 3.3895 vs 3.3898 original — 0.011% off · 오차 0.011% |
| Page size · 판형 | 420 × 595.92 pt (A5 portrait) |
| Embedded fonts · 임베드 서체 | Archivo Regular/Bold, Pretendard Regular/SemiBold — all subset with unicode maps |
| Wide table · 넓은 표 | 6 columns → 5 cards, none split across a page · 6열 → 카드 5장, 쪽 경계에서 안 잘림 |
| Narrow tables · 좁은 표 | 3 columns → kept as tables, not split · 3열 → 표 유지, 안 잘림 |
| Oversized table · 한 쪽 넘는 표 | 45 rows → splits with the header repeated · 45행 → 머리글 반복하며 분할 |

**Not checked · 확인하지 않은 것** — the PDF has not been opened on an actual
phone. It was rendered and inspected page by page here, but how KakaoTalk's
built-in viewer presents it is untested. Send yourself one before sending it to
anyone else.

**실제 휴대폰에서 열어 보지는 않았습니다.** 여기서 쪽마다 렌더해 확인했을 뿐,
카톡 기본 뷰어가 어떻게 보여 주는지는 시험하지 못했습니다. 남에게 보내기 전에
본인에게 먼저 한 번 보내 보세요.
