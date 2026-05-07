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
├── agents/
│   ├── subagent1_doc_validation.md      ← 문서 정합성 검증 지침
│   ├── subagent2_ai_action.md           ← 코드 구현 + 테스트 생성 지침
│   ├── subagent3_test_verify.md         ← 테스트 실행 검증 지침
│   └── subagent4_compliance_verify.md  ← 요구사항 정합성 검증 지침
├── calculator/
│   ├── __init__.py
│   └── calculator.py
└── tests/
    ├── __init__.py
    └── test_calculator.py
```

## 개발 워크플로우

개발은 `plan.md`에 정의된 3개 Phase로 진행한다. 각 Phase 안에서 SubAgent Cycle을 수행한다.

| Phase | 목표 | SubAgent | Cycle |
|---|---|---|---|
| Phase 1 — 문서 준비 | PRD ↔ CLAUDE.md 정합성 확보 | SubAgent1 | FAIL 시 CLAUDE.md 수정 후 재실행 |
| Phase 2 — 구현 | 소스 코드 + 테스트 완성 | SubAgent2 | Phase 3 FAIL 시 롤백 후 재실행 |
| Phase 3 — 검증 | 테스트 통과 + 요구사항 충족 | SubAgent3 \|\| SubAgent4 (병렬) | FAIL 시 Phase 2 롤백 |

전체 상세 흐름은 `plan.md` 참고. 각 SubAgent 지침은 `agents/` 디렉토리 참고.

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
