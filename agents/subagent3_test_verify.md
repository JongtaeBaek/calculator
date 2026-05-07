# SubAgent4 — Test Verify

## Step
**Step 4 — 검증** *(SubAgent5와 병렬 실행)*

## Cycle 규칙
```
Step 3 완료 + 사용자 승인 후 SubAgent5와 동시에 실행
→ PASS: SubAgent5도 PASS면 사용자 검토 대기
→ FAIL(테스트 코드 오류): 실패 원인 보고 → Step 3(SubAgent3) 롤백 → Step 4 재진입
→ FAIL(구현 오류): 실패 원인 보고 → Step 2(SubAgent2) 롤백 → Step 3 재진입 → Step 4 재진입
```

## 역할
SubAgent3가 작성한 테스트에 대해 pytest를 실행하여 모든 테스트의 통과 여부를 검증한다.
FAIL 시 원인이 테스트 코드 오류인지 구현 오류인지 판별하여 보고한다.

## 입력
- `tests/test_calculator.py`
- `calculator/calculator.py`

## 작업 절차
1. `python -m pytest --version` 으로 pytest 설치 확인
2. 미설치 시 `python -m pip install pytest`
3. `python -m pytest tests/ -v` 실행
4. 전체 테스트 결과 수집
5. 실패 테스트 있을 경우 원인 분석 및 롤백 대상 판별

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
롤백 대상: Phase 2 / Phase 3 (실패 시에만 작성)
```

## 완료 조건
전체 9개 테스트 통과 → PASS
