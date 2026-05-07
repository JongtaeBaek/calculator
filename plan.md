# Calculator 클래스 개발 계획

## 프로젝트 개요

PRD.md에 정의된 요구사항에 따라 Python Calculator 클래스를 구현한다.
개발은 하나의 Phase 안에서 4개 Step을 순차적으로 수행한다.
각 Step 완료 후 사용자 검토를 거쳐야 다음 Step으로 진행한다.

---

## 전체 흐름

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE — 개발 사이클                                             │
│                                                                 │
│  ┌──────────────┐                                               │
│  │    Step 1    │  SubAgent1: 문서 정합성 검증                   │
│  │  문서 준비   │  FAIL → CLAUDE.md 수정 후 재실행               │
│  └──────┬───────┘                                               │
│         │ PASS                                                  │
│         ▼                                                       │
│  ┌──────────────────────────────┐                               │
│  │  [사용자 검토] Step 1 결과  │  승인 후 Step 2 진행           │
│  └──────────────────────────────┘                               │
│         │                                                       │
│  ┌──────────────┐                                               │
│  │    Step 2    │  SubAgent2: calculator.py, __init__.py 구현   │
│  │  코드 구현   │                                               │
│  └──────┬───────┘                                               │
│         │ 완료                                                  │
│         ▼                                                       │
│  ┌──────────────────────────────┐                               │
│  │  [사용자 검토] Step 2 결과  │  승인 후 Step 3 진행           │
│  └──────────────────────────────┘                               │
│         │                                                       │
│  ┌──────────────┐                                               │
│  │    Step 3    │  SubAgent3: test_calculator.py 9종 작성       │
│  │  테스트 작성 │                                               │
│  └──────┬───────┘                                               │
│         │ 완료                                                  │
│         ▼                                                       │
│  ┌──────────────────────────────┐                               │
│  │  [사용자 검토] Step 3 결과  │  승인 후 Step 4 진행           │
│  └──────────────────────────────┘                               │
│         │                                                       │
│  ┌──────────────┐    ┌──────────────────┐                       │
│  │    Step 4    │    │     Step 4       │  ← 병렬 실행          │
│  │  SubAgent4   │    │   SubAgent5      │                       │
│  │ Test Verify  │    │Compliance Verify │                       │
│  └──────┬───────┘    └────────┬─────────┘                       │
│         └──────┬──────────────┘                                 │
│                │ 둘 다 PASS                                     │
│                ▼                                                │
│  ┌──────────────────────────────┐                               │
│  │  [사용자 검토] Step 4 결과  │  승인 후 개발 완료             │
│  └──────────────────────────────┘                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step 상세

### Step 1 — 문서 준비

**목표**: 구현 전 문서 기반 확보.

**SubAgent Cycle**:
```
SubAgent1 실행
  → PASS: 사용자 검토 대기
  → FAIL: 불일치 항목 기준으로 CLAUDE.md 수정 → SubAgent1 재실행
```

**사용자 검토 포인트**: SubAgent1 출력 결과 확인 후 Step 2 진행 여부 결정

**완료 조건**: SubAgent1 PASS + 사용자 승인

| SubAgent | 역할 | 입력 | 출력 |
|---|---|---|---|
| SubAgent1 | 문서 정합성 검증 | PRD.md, CLAUDE.md | PASS / FAIL + 불일치 목록 |

---

### Step 2 — 코드 구현

**목표**: PRD 기준으로 Calculator 클래스 소스 파일을 완성한다.

**SubAgent Cycle**:
```
SubAgent2 실행
  → 구현 완료: 사용자 검토 대기
  → (Step 4 SubAgent5 FAIL로 롤백 시) 코드 수정 → SubAgent2 재실행
```

**사용자 검토 포인트**: 구현 코드 확인 후 Step 3 진행 여부 결정

**완료 조건**: 소스 파일 작성 완료 + 문법 오류 없음 + 사용자 승인

| SubAgent | 역할 | 입력 | 출력 |
|---|---|---|---|
| SubAgent2 | 코드 구현 | PRD.md, 기존 소스 파일 | calculator.py, __init__.py |

**구현 기준**:
- 사칙연산 4종 (`add`, `subtract`, `multiply`, `divide`)
- 반환 타입 `float`
- `ZeroDivisionError("Cannot divide by zero")` / `TypeError("Operands must be numbers")`
- `get_history()` 복사본 반환으로 불변성 보장
- `clear_history()` 이력 초기화

---

### Step 3 — 테스트 작성

**목표**: 구현된 Calculator 클래스에 대한 pytest 테스트를 완성한다.

**SubAgent Cycle**:
```
SubAgent3 실행
  → 작성 완료: 사용자 검토 대기
  → (Step 4 SubAgent4 FAIL 중 테스트 코드 오류 롤백 시) 테스트 수정 → SubAgent3 재실행
```

**사용자 검토 포인트**: 테스트 코드 확인 후 Step 4 진행 여부 결정

**완료 조건**: 9개 테스트 메서드 정의 + 문법 오류 없음 + 사용자 승인

| SubAgent | 역할 | 입력 | 출력 |
|---|---|---|---|
| SubAgent3 | 테스트 작성 | PRD.md, calculator.py | test_calculator.py |

**테스트 기준**:
- 9개 테스트 케이스 (사칙연산 × 4, 예외 × 2, 이력 × 3)
- 이력 포맷 `"a op b = result"` 검증 포함
- `get_history()` 불변성 검증 포함

---

### Step 4 — 검증

**목표**: 구현 코드가 실제로 동작하고 PRD 요구사항을 모두 충족하는지 동시에 확인한다.

**SubAgent Cycle**:
```
SubAgent4 || SubAgent5 병렬 실행
  → 둘 다 PASS: 사용자 검토 대기
  → SubAgent4 FAIL (테스트 코드 오류): Step 3 롤백 → Step 4 재진입
  → SubAgent4 FAIL (구현 오류): Step 2 롤백 → Step 3 재진입 → Step 4 재진입
  → SubAgent5 FAIL: Step 2 롤백 → Step 3 재진입 → Step 4 재진입
```

**사용자 검토 포인트**: 검증 결과 확인 후 개발 완료 여부 결정

**완료 조건**: SubAgent4 PASS AND SubAgent5 PASS + 사용자 승인

| SubAgent | 역할 | 실행 방식 | 입력 | 출력 |
|---|---|---|---|---|
| SubAgent4 | Test Verify | 병렬 | 소스 코드, pytest | PASS / FAIL + 실패 원인 + 롤백 대상 |
| SubAgent5 | Compliance Verify | 병렬 | PRD.md, calculator.py | PASS / FAIL + 미충족 항목 |

---

## 롤백 규칙

| 발생 위치 | 원인 | 롤백 대상 | 재진입 경로 |
|---|---|---|---|
| Step 1 FAIL | 문서 불일치 | CLAUDE.md 수정 | Step 1 재시도 |
| Step 4 SubAgent4 FAIL | 테스트 코드 오류 | Step 3 | Step 3 → Step 4 |
| Step 4 SubAgent4 FAIL | 구현 코드 오류 | Step 2 | Step 2 → Step 3 → Step 4 |
| Step 4 SubAgent5 FAIL | 요구사항 미충족 | Step 2 | Step 2 → Step 3 → Step 4 |

---

## SubAgent 지침 파일

| 파일 | Step | SubAgent | 역할 |
|---|---|---|---|
| `agents/subagent1_doc_validation.md` | Step 1 | SubAgent1 | 문서 정합성 검증 |
| `agents/subagent2_ai_action.md` | Step 2 | SubAgent2 | 코드 구현 |
| `agents/subagent3_test_write.md` | Step 3 | SubAgent3 | 테스트 작성 |
| `agents/subagent3_test_verify.md` | Step 4 | SubAgent4 | pytest 실행 검증 |
| `agents/subagent4_compliance_verify.md` | Step 4 | SubAgent5 | 요구사항 정합성 검증 |

---

## 구현 대상 파일

| 파일 | 담당 | 내용 |
|---|---|---|
| `calculator/calculator.py` | SubAgent2 | Calculator 클래스 본체 |
| `calculator/__init__.py` | SubAgent2 | Calculator export |
| `tests/test_calculator.py` | SubAgent3 | pytest 테스트 9종 |
| `tests/__init__.py` | SubAgent3 | 패키지 파일 |

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
│   ├── subagent3_test_write.md
│   ├── subagent3_test_verify.md
│   └── subagent4_compliance_verify.md
├── calculator/
│   ├── __init__.py
│   └── calculator.py
└── tests/
    ├── __init__.py
    └── test_calculator.py
```
