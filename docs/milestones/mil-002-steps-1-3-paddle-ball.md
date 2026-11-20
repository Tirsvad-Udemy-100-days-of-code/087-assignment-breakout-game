# MIL-002 G2 Paddle and ball

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed Go in RC-005, stand-in review, not independent | pending |

---

## Purpose

Decides whether the first three lecture steps (window and paddle, moving ball with wall bounce, paddle bounce) work, are tested and are documented with screenshots.

## Deliverable

A playable window with a paddle moved by the left and right keys, a ball that moves and bounces on the top and side walls, and a ball that bounces off the paddle with an angle that depends on where it hits. Pure game rules are covered by pytest; a screenshot of each step is in the README.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes, and the rules package has at least 90 % line coverage | Met | Not met |
| 2 | The game runs in the screenshot container for 5 seconds without an exception | Met | Not met |
| 3 | Screenshots of steps 1, 2 and 3 are in `docs/images/` and in the README | Met | Not met |
| 4 | The code is reviewed against `QC-PY-001` with a Go | Met | Not met |
| 5 | The opengrep scan reports 0 findings of severity error | Met | Not met |
| 6 | Pull request opened with `Closes #N` lines for every task, and its checks are green | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The skeleton, constants, tests, scan and screenshot container exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O3 | [BC-001] Objectives |
| CN-001, CN-002, CN-003 | [SA-001] concern register |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-21 — one day after G1.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Step 1: screen and paddle | Create the black 800 by 600 window, the `Paddle` class and the left and right key bindings; the paddle stays inside the window. Paddle position and limits are a pure function so they are tested without a window. Screenshot `step-1`. | No | [BC-001] |
| 2 | Step 2: ball movement and wall bounce | Add the `Ball` class and the game loop with manual screen updates; the ball moves every tick and reverses direction on the top and side walls. The bounce rule is a pure function with tests. Screenshot `step-2`. | No | [BC-001] |
| 3 | Step 3: paddle bounce | Bounce the ball off the paddle and change the horizontal speed by the hit position (centre goes straight up, edges give a sharper angle). The collision test is a pure function with tests for centre, edge and miss. Screenshot `step-3`. | No | [BC-001] |
| 4 | Capture and add screenshots of steps 1 to 3 | Run each step in the screenshot container, save `docs/images/step-N.png` and add the three images to the README with one line each. | No | [BC-001] |
| 5 | Review code against QC-PY-001 | Review `src/` and `tests/` against `framework/qc/code/qc-programming-python.md`, write the `RC-*` record and fix any finding before the pull request. | No | [BC-001] |

---

[BC-001]: ../business-case.md
