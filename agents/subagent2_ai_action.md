# SubAgent2 — AI Action (코드 구현 + 테스트 생성)

## Phase
**Phase 2 — 구현**

## Cycle 규칙
```
최초 진입: Phase 1(SubAgent1) PASS 이후 실행
롤백 진입: Phase 3 FAIL 시 실패 원인 기반으로 코드 수정 후 재실행
완료: 모든 소스 파일 작성 완료 → Phase 3(SubAgent3 + SubAgent4) 진입
```

## 역할
PRD 요구사항에 따라 Calculator 클래스와 pytest 테스트를 구현/보완한다.

## 입력
- `PRD.md` — 구현 기준
- `calculator/calculator.py` — 기존 파일 (존재 시 검토 후 수정)
- `calculator/__init__.py` — 기존 파일
- `tests/test_calculator.py` — 기존 파일 (존재 시 검토 후 수정)
- Phase 3 롤백 시: SubAgent3/SubAgent4의 FAIL 원인 보고

## 구현 명세

### `calculator/calculator.py`

```python
class Calculator:
    def __init__(self):
        self._history: list[str] = []

    def _validate(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numbers")

    def _record(self, a, op, b, result):
        self._history.append(f"{a} {op} {b} = {result}")

    def add(self, a, b) -> float:
        self._validate(a, b)
        result = float(a + b)
        self._record(a, "+", b, result)
        return result

    def subtract(self, a, b) -> float:
        self._validate(a, b)
        result = float(a - b)
        self._record(a, "-", b, result)
        return result

    def multiply(self, a, b) -> float:
        self._validate(a, b)
        result = float(a * b)
        self._record(a, "*", b, result)
        return result

    def divide(self, a, b) -> float:
        self._validate(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = float(a / b)
        self._record(a, "/", b, result)
        return result

    def get_history(self) -> list[str]:
        return list(self._history)

    def clear_history(self) -> None:
        self._history.clear()
```

### `calculator/__init__.py`

```python
from .calculator import Calculator
__all__ = ["Calculator"]
```

### `tests/test_calculator.py` — 테스트 커버리지

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

## 작업 절차
1. 기존 소스 파일 읽기
2. PRD 명세와 비교 후 누락·오류 수정 (없으면 유지)
3. `python -m pytest --version` 으로 pytest 설치 확인
4. 미설치 시 `python -m pip install pytest`

## 완료 조건
모든 소스 파일 존재 + 문법 오류 없음
