# Calculator 클래스 PRD (Product Requirements Document)

## 1. 개요

**제품명**: Python Calculator Class  
**버전**: 1.0  
**작성일**: 2026-05-07

간단하고 신뢰성 있는 계산기 클래스를 Python으로 구현한다. 기본 산술 연산과 계산 이력 관리 기능을 제공한다.

---

## 2. 목표

- 사칙연산(+, -, ×, ÷)을 안정적으로 수행하는 클래스 제공
- 예외 상황(0 나누기, 잘못된 입력 등)을 명확한 예외로 처리
- 계산 이력(history) 조회 및 초기화 기능 제공

---

## 3. 기능 요구사항

### 3.1 핵심 연산

| 메서드 | 시그니처 | 설명 |
|---|---|---|
| 덧셈 | `add(a, b) → float` | a + b |
| 뺄셈 | `subtract(a, b) → float` | a - b |
| 곱셈 | `multiply(a, b) → float` | a × b |
| 나눗셈 | `divide(a, b) → float` | a ÷ b |

### 3.2 이력 관리

| 메서드 | 시그니처 | 설명 |
|---|---|---|
| 이력 조회 | `get_history() → list[str]` | 전체 계산 이력 반환 |
| 이력 초기화 | `clear_history() → None` | 이력 전체 삭제 |

### 3.3 이력 포맷

```
"2 + 3 = 5.0"
"10 / 2 = 5.0"
```

---

## 4. 예외 처리 요구사항

| 상황 | 예외 타입 | 메시지 예시 |
|---|---|---|
| 0으로 나누기 | `ZeroDivisionError` | `"Cannot divide by zero"` |
| 숫자가 아닌 입력 | `TypeError` | `"Operands must be numbers"` |

---

## 5. 비기능 요구사항

- **타입 지원**: `int`, `float` 입력 모두 처리
- **반환 타입**: 모든 연산 결과는 `float` 반환
- **불변성**: 연산 메서드는 내부 상태(이력 제외)를 변경하지 않음

---

## 6. 파일 구조

```
calculator/
├── calculator/
│   ├── __init__.py
│   └── calculator.py     ← Calculator 클래스
└── tests/
    └── test_calculator.py
```

---

## 7. 사용 예시

```python
calc = Calculator()

calc.add(2, 3)        # → 5.0
calc.subtract(10, 4)  # → 6.0
calc.multiply(3, 7)   # → 21.0
calc.divide(10, 2)    # → 5.0

calc.get_history()
# ["2 + 3 = 5.0", "10 - 4 = 6.0", "3 * 7 = 21.0", "10 / 2 = 5.0"]

calc.clear_history()
```
