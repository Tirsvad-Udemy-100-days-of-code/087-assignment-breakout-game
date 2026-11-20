# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [PY-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PY-002]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01, who is also the author)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | PEP 8 casing throughout; ruff rule set N clean. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; the one-letter b is in a one-line generator. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff check and format clean, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | mypy strict passes on src, tests and tools. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No except blocks in the code. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults or shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | N-A | No files, locks or connections are handled; capture.py only runs a subprocess with check=True. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Doxygen blocks on every module, class and public function. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print and no logging in src, tests or tools (checked with grep). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram: PP-001 Open Issues records that every task is a plain technical task. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 94 tests, named for behaviour, deterministic, no network; headless full-game tests reach WON and LOST; a test ties BALL_MAX_SPEED to the brick and paddle sizes. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy strict clean; grep finds no Any in code. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Dev tools are not pinned (optional); accepted and tracked as the action item of RC-008. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The top-score rule is now Brick.is_top_scoring; the corner tolerance is a constant (review findings D1 and D2 fixed). |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | lint-imports: both contracts kept; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | GameSession owns the state, the rules are pure functions, Game is the only composition root. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | domain, application and presentation/turtle_ui; tests/unit and tests/integration; the screenshot container covers the window. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English snake_case names without spaces. |

## Overall Verdict

Go - all Mandatory criteria pass; the Optional finding on criterion 13 stays accepted (RC-008). Reviewed by the python-developer subagent; findings D1, D2, D3, T1, T2 and T3 were fixed and all checks re-run.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Pin the dev tool versions (criterion 13) if the project is released; tracked from RC-008 | S01 | 2026-11-23 |

---

[PY-002]: ../../../src
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
