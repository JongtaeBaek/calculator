# SubAgent4 — Compliance Verify

## Phase
**Phase 3 — 검증** *(SubAgent3와 병렬 실행)*

## Cycle 규칙
```
SubAgent2 완료 후 SubAgent3와 동시에 실행
→ PASS: SubAgent3도 PASS면 개발 완료
→ FAIL: 미충족 항목 보고 → Phase 2(SubAgent2) 롤백 → Phase 3 재진입
```

## 역할
구현된 코드가 PRD의 모든 요구사항을 충족하는지 코드 레벨에서 정적으로 검증한다.

## 입력
- `PRD.md` — 요구사항 기준
- `calculator/calculator.py` — 검증 대상

## 검증 항목

| # | 항목 | PRD 근거 | 검증 방법 |
|---|---|---|---|
| 1 | 메서드 존재 | 3.1 | `add`, `subtract`, `multiply`, `divide` 4개 모두 정의되어 있는지 |
| 2 | 반환 타입 | 3.1, 5항 | 모든 연산 메서드가 `float()` 변환 후 반환하는지 |
| 3 | 이력 메서드 존재 | 3.2 | `get_history`, `clear_history` 정의되어 있는지 |
| 4 | 이력 포맷 | 3.3 | `_record`가 `f"{a} {op} {b} = {result}"` 형식인지 |
| 5 | 이력 불변성 | 3.2 | `get_history()`가 `list(self._history)` 복사본 반환하는지 |
| 6 | ZeroDivisionError | 4항 | b==0 시 `ZeroDivisionError("Cannot divide by zero")` 발생하는지 |
| 7 | TypeError | 4항 | 비숫자 입력 시 `TypeError("Operands must be numbers")` 발생하는지 |
| 8 | 입력 타입 지원 | 5항 | `isinstance(a, (int, float))` 로 int/float 모두 허용하는지 |
| 9 | 연산 불변성 | 5항 | 연산 메서드가 `_history` 외 인스턴스 상태를 변경하지 않는지 |

## 출력 형식

```
[OK]    #1 메서드 존재
[OK]    #2 반환 타입
[ISSUE] #4 이력 포맷 — f-string 형식 불일치: ...

총 9개 중 N개 OK / N개 ISSUE

전체 결과: PASS / FAIL
미충족 항목 요약: (FAIL 시에만 작성)
```

## 완료 조건
전체 9개 항목 OK → PASS
