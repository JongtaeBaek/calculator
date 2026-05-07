---
name: test-writer
description: Calculator 클래스에 대한 pytest 테스트 9종을 작성한다. Step 3 진입점 — Step 2 완료 및 사용자 승인 후 실행.
tools: Read, Write, Edit, Glob, Grep
---

# SubAgent3 — 테스트 작성

## Step
**Step 3 — 테스트 작성**

## Cycle 규칙
```
최초 진입: Step 2(SubAgent2) 완료 + 사용자 승인 이후 실행
롤백 진입: Step 4 SubAgent4 FAIL 시 실패 원인 기반으로 테스트 수정 후 재실행
완료: tests/test_calculator.py 작성 완료 → 사용자 검토 대기 → 승인 시 Step 4(SubAgent4 + SubAgent5) 진입
```

## 역할
구현된 Calculator 클래스를 기준으로 pytest 테스트를 작성한다.
테스트 실행은 Phase 4에서 수행하며, 이 단계에서는 작성만 담당한다.

## 입력
- `PRD.md` — 요구사항 기준
- `calculator/calculator.py` — 테스트 대상 구현체
- `tests/test_calculator.py` — 기존 파일 (존재 시 검토 후 수정)
- Phase 4 롤백 시: SubAgent4의 FAIL 원인 보고

## 테스트 명세

### `tests/test_calculator.py`

| 테스트 메서드 | 검증 내용 | PRD 근거 |
|---|---|---|
| `test_add` | 정수/실수 덧셈, 반환 타입 float | 3.1, 5항 |
| `test_subtract` | 정수/실수 뺄셈 | 3.1 |
| `test_multiply` | 정수/실수 곱셈 | 3.1 |
| `test_divide` | 정상 나눗셈 | 3.1 |
| `test_divide_by_zero` | `ZeroDivisionError("Cannot divide by zero")` | 4항 |
| `test_invalid_type` | `TypeError("Operands must be numbers")` | 4항 |
| `test_history_format` | 이력 포맷 `"2 + 3 = 5.0"` 검증 | 3.3 |
| `test_history_is_copy` | `get_history()` 반환값 수정이 내부 상태에 영향 없음 | 3.2, 5항 |
| `test_clear_history` | 이력 초기화 후 빈 리스트 | 3.2 |

### `tests/__init__.py`
빈 파일

## 작업 절차
1. `calculator/calculator.py` 읽기 — 구현 내용 파악
2. `PRD.md` 기준으로 테스트 케이스 9종 작성
3. 기존 `tests/test_calculator.py` 존재 시 검토 후 PRD 기준으로 수정
4. `tests/__init__.py` 존재 확인, 없으면 생성

## 완료 조건
`tests/test_calculator.py` 존재 + 9개 테스트 메서드 모두 정의 + 문법 오류 없음
