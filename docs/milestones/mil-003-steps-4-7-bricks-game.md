# MIL-003 G3 Bricks and game

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed Go in RC-006, stand-in review, not independent | [d4bf2df] |

---

## Purpose

Decides whether the game is complete: a wall of bricks that breaks, score, lives, a win and a game over, and a ball that gets faster, all tested and documented with screenshots.

## Deliverable

The finished Breakout game: six rows of bricks in red, orange, green and yellow bands that disappear when hit, a scoreboard with score and lives, a game-over and a you-win message, and a ball speed-up. Pure rules are covered by pytest; screenshots of steps 4 to 7 are in the README.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes, and the rules package has at least 90 % line coverage | Met | Not met |
| 2 | A test plays a full game headlessly: all bricks removed gives a win, three misses give a game over | Met | Not met |
| 3 | Screenshots of steps 4, 5, 6 and 7 are in `docs/images/` and in the README | Met | Not met |
| 4 | The code is reviewed against `QC-PY-001` with a Go | Met | Not met |
| 5 | The opengrep scan reports 0 findings of severity error | Met | Not met |
| 6 | Pull request opened with `Closes #N` lines for every task, and its checks are green | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The paddle, the ball and the bounce rules are accepted and merged |

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

2026-11-22 — one day after G2.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Step 4: wall of bricks | Build the grid of bricks (six rows in red, orange, green and yellow bands) from the layout in `constants.py` with the `Bricks` class. The layout is data, produced by a pure function and tested. Screenshot `step-4`. | No | [BC-001] |
| 2 | Step 5: brick collision and score | Detect a hit between the ball and a brick, remove the brick, reverse the ball on the right axis and add points by row colour to the `Scoreboard`. The side of the hit is decided by a pure function with tests. Screenshot `step-5`. | No | [BC-001] |
| 3 | Step 6: lives, game over and win | Lose a life when the ball passes the paddle, show game over at zero lives, show a win when the last brick is removed and let the player restart with a key. The state machine is pure and tested. Screenshot `step-6`. | No | [BC-001] |
| 4 | Step 7: speed-up and polish | Raise the ball speed after a number of paddle hits and when a top-row brick is hit, tune the constants and finish the final screenshot `step-7`. | No | [BC-001] |
| 5 | Capture and add screenshots of steps 4 to 7 | Run each step in the screenshot container, save `docs/images/step-N.png` and add the four images to the README with one line each. | No | [BC-001] |
| 6 | Add a headless full-game test | Drive the rules engine with a scripted paddle through a whole game, once to a win and once to a game over, so the end states are proven without a window. | No | [BC-001] |
| 7 | Review code against QC-PY-001 | Review the new `src/` and `tests/` against `framework/qc/code/qc-programming-python.md`, write the `RC-*` record and fix any finding before the pull request. | No | [BC-001] |

---

[BC-001]: ../business-case.md
[d4bf2df]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/commit/d4bf2df2d88712f1b4e71c76be15fb497ac94ed4
