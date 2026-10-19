# Poster layout references · 포스터 레이아웃 참고 자료

비서실이 학생 포스터에서 **레이아웃만** 뽑아 넣는 곳입니다. 여기 자료를 분석해
[`posters/`](../../posters/) 템플릿의 격자를 고치고 변형판(가로형 · A1 등)을 만듭니다.

Layout-only references extracted from students' posters. They are analysed to
revise the grid of the [`posters/`](../../posters/) template and to add variants.

## 넣지 않을 것 · Keep out

- 포스터 원본 파일 (PPTX · PDF · AI). 미발표 데이터가 들어 있습니다.
- 학생 이름, 그림, 본문 문장. 와이어프레임은 상자와 자리 표시만 남깁니다.
- 다른 기관 로고가 보이는 이미지 — 자리만 상자로 표시하세요.

## 한 포스터에 폴더 하나 · One folder per poster

```
references/posters/
  01-mrs-fall-2025/
    wireframe.png      내용을 가린 와이어프레임 (긴 변 2000 px 정도면 충분)
    layout.md          아래 양식
  02-kcs-2026/
    ...
```

폴더 이름은 `번호-학회-연도` 로 해 주세요. 학생 이름은 넣지 않습니다.

## layout.md 양식 · Template

치수는 mm, 글자는 pt 로 적어 주세요. 모르는 칸은 비워 두면 됩니다 — 와이어프레임에서
잴 수 있습니다.

```markdown
# 01 — MRS Fall 2025

## 판형
- 크기: 841 × 1189 mm (A0)        ← 학회가 정한 크기 그대로. 예: 48 × 36 inch
- 방향: 세로 / 가로
- 학회 규정: (있으면 링크나 문구)

## 단 구성
- 단 수: 3
- 단 폭: 같음 / 다름 (다르면 비율, 예: 1 : 2 : 1)
- 여백 · 단 간격: 약 30 mm / 20 mm

## 머리 · 꼬리
- 머리 높이: 약 200 mm. 들어 있는 것: 제목 · 저자 · 소속 · 로고(위치)
- 꼬리: 있음 / 없음. 들어 있는 것: 연락처 · 사사 · QR

## 섹션 배치
단마다 위에서 아래로:
- 1단: Introduction → Methods (그림 1)
- 2단: Results (그림 2, 3)
- 3단: Results 계속 (그림 4) → Conclusion → References

## 글자 크기 위계
| 역할 | 크기 (pt) |
| --- | --- |
| 제목 | |
| 저자 | |
| 섹션 제목 | |
| 본문 | |
| 그림 설명 | |
| 참고문헌 | |

## 그림
- 개수: 4
- 비율: 그림 1 4:3, 그림 2 16:9 (가로로 두 단 걸침), ...
- 그림이 차지하는 면적: 본문 영역의 약 절반

## 눈에 띄는 점
- 예: 결론을 맨 위 가운데 상자에 따로 둠, 2단에 걸친 큰 그림, 요약 상자 등
```

## 분석 기록 · Analysis

자료가 들어오면 판형별로 묶어 이 아래에 정리합니다 — 몇 장이 어떤 판형이었는지,
단 구성과 글자 크기의 공통점, 템플릿에 반영한 것과 반영하지 않은 것과 그 이유.

*(아직 자료가 없습니다 · No references yet — 2026-10-19)*
