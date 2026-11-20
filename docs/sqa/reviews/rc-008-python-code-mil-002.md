# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [PY-001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [3f28458] |

---

## Artifact Under Review

- Instance reviewed: [PY-001]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01, who is also the author)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | PEP 8 casing; ruff rule set N clean. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; short names only in tiny scopes. Views alias the domain classes (BallState, PaddleState). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff check and ruff format clean, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated incl. -> None (src, tests, tools). |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; capture.py re-raises with raise SystemExit from error. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults, no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | N-A | No files, locks or connections in the code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Doxygen blocks on every module, class and public function. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print or logging; no secrets in code. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram: PP-001 Open Issues records that every task is a plain technical task. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 45 tests named for behaviour, with boundary cases; no network or order dependence. Presentation is exercised by the screenshot container, not by unit tests. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy strict clean on src, tests and tools; no Any. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Dev extras use lower bounds only and there is no lock file; dependencies is empty. Optional criterion, recorded as a finding. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | SQUARE_SIZE now defined once in presentation/turtle_ui/shapes.py (was found twice by the review and fixed). |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | lint-imports: layers contract and no-Turtle contract kept; no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Small classes with one reason to change; GameSession is the only orchestrator. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | domain, application and presentation/turtle_ui under src/breakout; tests/unit mirrors it. No infrastructure layer is needed because nothing is stored. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English snake_case names without spaces. |

## Overall Verdict

Go - all Mandatory criteria pass; one Optional finding (criterion 13) is accepted for this learning project. Reviewed by the python-developer subagent; re-checked after fixes with ruff, mypy strict, pytest and lint-imports.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Pin the dev tool versions (criterion 13) if the project is released | S01 | 2026-11-23 |

---

[PY-001]: ../../../src
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[3f28458]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/commit/3f28458cf0bdaf14162c31b074e3b3b675e665f4
