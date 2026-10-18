# Print-ready logos · 인쇄용 로고

Vector PDFs for business cards, signage and anything that goes to a printer.
Built from the SVG masters by `tools/build_print_logos.py`.

명함 · 사인물 등 인쇄에 넣을 벡터 PDF 입니다. SVG 원본에서
`tools/build_print_logos.py` 로 생성합니다.

## Which file · 어느 파일

| File | Use · 쓰임 |
| --- | --- |
| `hbrlrg-horizontal.pdf` | Light card, full colour · 밝은 명함, 컬러 |
| `hbrlrg-horizontal-reverse.pdf` | Navy or dark card · 네이비 · 어두운 명함 |
| `hbrlrg-horizontal-mono.pdf` | One-colour printing · 먹 1도 인쇄 |
| `hbrlrg-symbol.pdf` | Symbol alone, e.g. card back · 심볼 단독, 명함 뒷면 |

Each has a `-cmyk` twin. **Hand the printer the plain one unless they ask for
CMYK** — see below.

각 파일에 `-cmyk` 짝이 있습니다. **인쇄소가 CMYK 를 요구하지 않는 한 기본
파일을 주세요** — 아래 설명을 보세요.

## Colour · 색

| | Navy | Teal |
| --- | --- | --- |
| Hex | `#14243F` | `#0EA79A` |
| CMYK | 100 / 82 / 38 / 52 | 94 / 0 / 48 / 4 |

**Give the printer the hex and let them convert.** That is the most accurate
route, because their profile knows their press and paper. The CMYK numbers
above are generic process-ink values, correct to within rounding when rendered
back, but not matched to any named profile.

**인쇄소에는 hex 를 주고 변환을 맡기는 편이 가장 정확합니다.** 그쪽 프로파일이
자기 인쇄기와 용지를 압니다. 위 CMYK 는 범용 공정 잉크 기준 값으로, 되돌려
렌더하면 반올림 오차 안에서 브랜드 색과 일치하지만 특정 프로파일에 맞춘 값은
아닙니다.

**The old CMYK values were wrong.** Until 2026-10-18 the logo README carried
Navy 68/43/0/75 and Teal 92/0/8/35 — the textbook arithmetic conversion. That
formula assumes perfect inks, and real process cyan is already around `#00ADEF`,
well towards blue. Printed, the old teal comes out near `#0E7A9F`, which reads
as blue rather than the brand's green-teal. If anything was printed from those
numbers, that is why the colour looked off.

**이전 CMYK 값은 틀렸습니다.** 2026-10-18 까지 로고 README 에 Navy 68/43/0/75,
Teal 92/0/8/35 로 적혀 있었는데, 교과서 산술 변환입니다. 산술식은 완전한 잉크를
전제하지만 실제 공정 사이안은 `#00ADEF` 로 이미 파랑 쪽입니다. 그대로 인쇄하면
Teal 이 `#0E7A9F` 근처, 즉 청록이 아니라 파랑으로 나옵니다. 이전에 인쇄한 것의
색이 이상했다면 이것이 원인입니다.

## Size · 크기

The horizontal files are 40 mm wide, the symbol 12 mm. **These are starting
sizes, not limits** — the artwork is vector and scales without loss. Place it
and scale it to whatever the layout needs.

가로형은 폭 40 mm, 심볼은 12 mm 로 만들어져 있습니다. **기준 크기일 뿐 제한이
아닙니다** — 벡터라 손실 없이 확대 · 축소됩니다.

Minimum legible size: horizontal **25 mm wide**, symbol **6 mm**. Below that the
knot in the symbol closes up.

최소 크기: 가로형 폭 **25 mm**, 심볼 **6 mm**. 그보다 작으면 심볼의 매듭이
뭉갭니다.

**Set one dimension and let the other follow.** The ratio is 3.39 : 1 and giving
both width and height is how it gets stretched.

**한쪽 치수만 지정하세요.** 비율 3.39 : 1 이며, 가로세로를 둘 다 지정하는 것이
로고가 찌그러지는 원인입니다.

## What was checked · 확인한 것

| | Result · 결과 |
| --- | --- |
| Vector, not raster · 벡터 여부 | No image XObjects in any file · 래스터 없음 |
| Lettering outlined · 글자 아웃라인 | No font references · 폰트 참조 없음 |
| Page size · 페이지 크기 | 40.000 mm wide (symbol 12.000 mm), trimmed to the artwork |
| Proportion · 비율 | 3.3915 against the SVG master's 3.3915 |
| Colour, RGB files | Renders exactly `#14243F` and `#0EA79A` |
| Colour, CMYK files | Renders `#13243E` and `#0FA89B` — 1/255 rounding |
| Reverse on navy · 반전본 | White lettering, teal mark, knot gaps open |

**Not checked · 확인하지 않은 것** — nothing here has been through a real press.
Ask the printer for a proof before a full run, especially for the teal.

**실제 인쇄기를 거치지는 않았습니다.** 본 인쇄 전에 교정쇄를 요청하세요. 특히
청록이 그렇습니다.

## Rebuilding · 다시 만들기

```bash
pip install cairosvg pikepdf
python3 tools/build_print_logos.py
```

Edit the SVG masters in `assets/logo/`, never these PDFs. The script verifies
each file as it goes and refuses to write one that is not clean vector.

원본은 `assets/logo/` 의 SVG 입니다. 이 PDF 를 직접 고치지 마세요. 스크립트가
생성하면서 각 파일을 검사하고, 깨끗한 벡터가 아니면 쓰지 않습니다.
