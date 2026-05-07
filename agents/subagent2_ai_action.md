# SubAgent2 — 코드 구현

## Step
**Step 2 — 코드 구현**

## Cycle 규칙
```
최초 진입: Step 1(SubAgent1) PASS + 사용자 승인 이후 실행
롤백 진입: Step 4 SubAgent5 FAIL 시 실패 원인 기반으로 코드 수정 후 재실행
완료: 소스 파일 작성 완료 → 사용자 검토 대기 → 승인 시 Step 3(SubAgent3) 진입
```

## 역할
PRD 요구사항에 따라 Calculator 클래스를 구현한다.
테스트 코드 작성은 Phase 3(SubAgent3)에서 담당하며, 이 단계에서는 소스 코드만 작성한다.

## 입력
- `PRD.md` — 구현 기준
- `calculator/calculator.py` — 기존 파일 (존재 시 검토 후 수정)
- `calculator/__init__.py` — 기존 파일
- Phase 4 롤백 시: SubAgent5의 FAIL 원인 보고

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

## 작업 절차
1. 기존 소스 파일 읽기
2. PRD 명세와 비교 후 누락·오류 수정 (없으면 유지)

## 완료 조건
`calculator/calculator.py`, `calculator/__init__.py` 존재 + 문법 오류 없음
