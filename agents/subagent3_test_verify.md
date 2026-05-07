# SubAgent3 — Test Verify

## Phase
**Phase 3 — 검증** *(SubAgent4와 병렬 실행)*

## Cycle 규칙
```
SubAgent2 완료 후 SubAgent4와 동시에 실행
→ PASS: SubAgent4도 PASS면 개발 완료
→ FAIL: 실패 원인 보고 → Phase 2(SubAgent2) 롤백 → Phase 3 재진입
```

## 역할
SubAgent2가 생성한 코드에 대해 pytest를 실행하여 모든 테스트의 통과 여부를 검증한다.

## 입력
- `tests/test_calculator.py`
- `calculator/calculator.py`

## 작업 절차
1. `python -m pytest tests/ -v` 실행
2. 전체 테스트 결과 수집
3. 실패 테스트 있을 경우 원인 분석

## 출력 형식

```
[PASS] TestCalculator::test_add
[PASS] TestCalculator::test_subtract
[PASS] TestCalculator::test_multiply
[PASS] TestCalculator::test_divide
[PASS] TestCalculator::test_divide_by_zero
[PASS] TestCalculator::test_invalid_type
[PASS] TestCalculator::test_history_format
[PASS] TestCalculator::test_history_is_copy
[PASS] TestCalculator::test_clear_history

총 9개 중 N개 통과 / N개 실패

전체 결과: PASS / FAIL
실패 원인 요약: (실패 시에만 작성)
```

## 완료 조건
전체 9개 테스트 통과 → PASS
