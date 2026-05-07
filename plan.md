# Calculator 클래스 개발 계획

## 프로젝트 개요

PRD.md에 정의된 요구사항에 따라 Python Calculator 클래스를 구현한다.
개발은 3개 Phase로 나뉘며, 각 Phase 안에서 SubAgent 수행 Cycle을 돌린다.
모든 Phase를 통과해야 개발 완료로 판정한다.

---

## 전체 Phase 흐름

```
┌──────────────────────────────────────────────────────────┐
│  PHASE 1 — 문서 준비                                      │
│  목표: PRD ↔ CLAUDE.md 정합성 확보                        │
│                                                          │
│  ┌──────────────┐  FAIL + 수정   ┌──────────────────┐   │
│  │  SubAgent1   │ ◄──────────── │  CLAUDE.md 수정  │   │
│  │  문서 검증   │                └──────────────────┘   │
│  └──────┬───────┘                                        │
│         │ PASS                                           │
└─────────┼────────────────────────────────────────────────┘
          │
          ▼
┌──────────────────────────────────────────────────────────┐
│  PHASE 2 — 구현                                           │
│  목표: Calculator 클래스 + 테스트 코드 완성               │
│                                                          │
│  ┌──────────────┐                                        │
│  │  SubAgent2   │                                        │
│  │  코드 구현   │  (PRD 기준으로 소스 파일 작성/보완)    │
│  └──────┬───────┘                                        │
│         │ 완료                                           │
└─────────┼────────────────────────────────────────────────┘
          │
          ▼
┌──────────────────────────────────────────────────────────┐
│  PHASE 3 — 검증                                           │
│  목표: 테스트 통과 + 요구사항 충족 동시 확인              │
│                                                          │
│  ┌──────────────┐    ┌──────────────────┐                │
│  │  SubAgent3   │    │    SubAgent4     │  ← 병렬 실행   │
│  │  Test Verify │    │ Compliance Verify│                │
│  └──────┬───────┘    └────────┬─────────┘                │
│         │                    │                           │
│         └──────┬─────────────┘                           │
│                │ 둘 다 PASS                              │
│                │ 하나라도 FAIL → Phase 2 롤백             │
└────────────────┼─────────────────────────────────────────┘
                 │
                 ▼
            개발 완료
```

---

## Phase 1 — 문서 준비

**목표**: 구현 전 문서 기반 확보. 잘못된 문서로 구현하는 위험을 제거한다.

**SubAgent Cycle**:
```
SubAgent1 실행
  → PASS: Phase 2 진입
  → FAIL: 불일치 항목 기준으로 CLAUDE.md 수정 → SubAgent1 재실행
```

**완료 조건**: SubAgent1 PASS

| SubAgent | 역할 | 입력 | 출력 |
|---|---|---|---|
| SubAgent1 | 문서 정합성 검증 | PRD.md, CLAUDE.md | PASS / FAIL + 불일치 목록 |

---

## Phase 2 — 구현

**목표**: PRD 기준으로 소스 코드와 테스트를 완성한다.

**SubAgent Cycle**:
```
SubAgent2 실행
  → 구현 완료: Phase 3 진입
  → (Phase 3 FAIL로 롤백 시) 실패 원인 기반으로 코드 수정 → SubAgent2 재실행
```

**완료 조건**: 모든 소스 파일 작성 완료 + 문법 오류 없음

| SubAgent | 역할 | 입력 | 출력 |
|---|---|---|---|
| SubAgent2 | 코드 구현 + 테스트 생성 | PRD.md, 기존 소스 파일 | 완성된 소스 파일 |

**구현 기준**:
- `calculator/calculator.py`: 사칙연산 4종 + 이력 관리 2종
- `tests/test_calculator.py`: 9개 테스트 케이스
- 반환 타입 `float`, 이력 포맷 `"a op b = result"`
- `ZeroDivisionError("Cannot divide by zero")` / `TypeError("Operands must be numbers")`
- `get_history()` 복사본 반환으로 불변성 보장

---

## Phase 3 — 검증

**목표**: 구현 코드가 실제로 동작하고 PRD 요구사항을 모두 충족하는지 동시에 확인한다.

**SubAgent Cycle**:
```
SubAgent3 || SubAgent4 병렬 실행
  → 둘 다 PASS: 개발 완료
  → 하나라도 FAIL: 실패 원인 보고 → Phase 2 롤백 → SubAgent2 수정 → Phase 3 재진입
```

**완료 조건**: SubAgent3 PASS **AND** SubAgent4 PASS

| SubAgent | 역할 | 실행 방식 | 입력 | 출력 |
|---|---|---|---|---|
| SubAgent3 | Test Verify | 병렬 | 소스 코드, pytest | PASS / FAIL + 실패 원인 |
| SubAgent4 | Compliance Verify | 병렬 | PRD.md, calculator.py | PASS / FAIL + 미충족 항목 |

---

## 롤백 규칙

| 발생 위치 | 원인 | 롤백 대상 |
|---|---|---|
| Phase 1 FAIL | 문서 불일치 | CLAUDE.md 수정 후 Phase 1 재시도 |
| Phase 3 SubAgent3 FAIL | 테스트 실패 | Phase 2로 롤백, 코드 수정 |
| Phase 3 SubAgent4 FAIL | 요구사항 미충족 | Phase 2로 롤백, 코드 수정 |

---

## SubAgent 지침 파일

| 파일 | Phase | 역할 |
|---|---|---|
| `agents/subagent1_doc_validation.md` | Phase 1 | 문서 정합성 검증 |
| `agents/subagent2_ai_action.md` | Phase 2 | 코드 구현 + 테스트 생성 |
| `agents/subagent3_test_verify.md` | Phase 3 | pytest 실행 검증 |
| `agents/subagent4_compliance_verify.md` | Phase 3 | 요구사항 정합성 검증 |

---

## 구현 대상 파일

| 파일 | 담당 | 내용 |
|---|---|---|
| `calculator/calculator.py` | SubAgent2 | Calculator 클래스 본체 |
| `calculator/__init__.py` | SubAgent2 | Calculator export |
| `tests/test_calculator.py` | SubAgent2 | pytest 테스트 9종 |
| `tests/__init__.py` | SubAgent2 | 패키지 파일 |

---

## 파일 구조 (완성 목표)

```
calculator/
├── plan.md
├── PRD.md
├── CLAUDE.md
├── agents/
│   ├── subagent1_doc_validation.md
│   ├── subagent2_ai_action.md
│   ├── subagent3_test_verify.md
│   └── subagent4_compliance_verify.md
├── calculator/
│   ├── __init__.py
│   └── calculator.py
└── tests/
    ├── __init__.py
    └── test_calculator.py
```
