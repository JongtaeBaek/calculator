# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python 기반 Calculator 클래스 프로젝트. `.venv` 가상환경이 준비되어 있음.

요구사항 전체 스펙은 `PRD.md` 참고.

### 핵심 기능 요약

- 사칙연산: `add`, `subtract`, `multiply`, `divide` — 입력 `int`/`float` 모두 지원, 반환 타입 항상 `float`
- 이력 관리: `get_history() → list[str]`, `clear_history() → None`
  - 이력 포맷: `"2 + 3 = 5.0"` (피연산자 그대로, 결과는 float 문자열)
- 예외 처리:
  - `ZeroDivisionError("Cannot divide by zero")` — 0으로 나누기 시
  - `TypeError("Operands must be numbers")` — 숫자가 아닌 입력 시
- 불변성: 연산 메서드는 `_history` 외 내부 상태를 변경하지 않음

### 파일 구조

```
calculator/
├── plan.md                              ← 개발 계획 및 SubAgent 파이프라인
├── PRD.md                               ← 요구사항 명세
├── CLAUDE.md                            ← Claude Code 가이드 (현재 파일)
├── .claude/
│   └── agents/
│       ├── subagent1_doc_validation.md      ← [Phase 1] 문서 정합성 검증 지침
│       ├── subagent2_ai_action.md           ← [Phase 2] 코드 구현 지침
│       ├── subagent3_test_write.md          ← [Phase 3] 테스트 작성 지침
│       ├── subagent3_test_verify.md         ← [Phase 4] 테스트 실행 검증 지침 (SubAgent4)
│       ├── subagent4_compliance_verify.md   ← [Phase 4] 요구사항 정합성 검증 지침 (SubAgent5)
│       ├── ai-action.md                     ← Verify Harness: AI Action 레이어
│       ├── compliance-verifier.md           ← Verify Harness: Compliance Verifier
│       ├── consistency-verifier.md          ← Verify Harness: Consistency Verifier
│       └── test-verifier.md                 ← Verify Harness: Test Verifier
├── calculator/
│   ├── __init__.py
│   └── calculator.py
└── tests/
    ├── __init__.py
    └── test_calculator.py
```

## 개발 워크플로우

개발은 `plan.md`에 정의된 하나의 Phase 안에서 4개 Step을 순차적으로 수행한다.
각 Step 완료 후 **사용자 검토**를 거쳐야 다음 Step으로 진행한다.

| Step | 목표 | SubAgent | 사용자 검토 |
|---|---|---|---|
| Step 1 — 문서 준비 | PRD ↔ CLAUDE.md 정합성 확보 | SubAgent1 | Step 1 결과 확인 후 Step 2 승인 |
| Step 2 — 코드 구현 | `calculator.py` 소스 완성 | SubAgent2 | Step 2 결과 확인 후 Step 3 승인 |
| Step 3 — 테스트 작성 | `test_calculator.py` 완성 | SubAgent3 | Step 3 결과 확인 후 Step 4 승인 |
| Step 4 — 검증 | 테스트 통과 + 요구사항 충족 | SubAgent4 \|\| SubAgent5 (병렬) | Step 4 결과 확인 후 완료 승인 |

전체 상세 흐름은 `plan.md` 참고. 각 SubAgent 지침은 `.claude/agents/` 디렉토리 참고.

## Environment

- Python 3.13.3 (`python` 명령어로 직접 실행)
- pytest: `python -m pip install pytest`

## Commands

```bash
# 테스트 실행
python -m pytest tests/ -v

# 단일 테스트 실행
python -m pytest tests/test_calculator.py::TestCalculator::test_add -v

# 린트
python -m flake8 calculator/
```
