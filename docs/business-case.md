# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed Go in RC-001, stand-in review, not independent | [d4bf2df] |

---

## Executive Summary

Day 87 of the course "100 Days of Code: The Complete Python Pro Bootcamp" asks the participant to build a clone of the 1976 arcade game Breakout with Python Turtle. This project delivers that clone as a small, readable, runnable repository: a paddle, a ball and a wall of coloured bricks, with score, lives and a win/lose end. Each development step is documented with a screenshot in the README and explained in a wiki in English, Danish and Bahasa Malaysia, so that other course participants can learn from and compare with the solution. The project needs no runtime dependency and takes about two hours of building effort. The recommendation is to proceed.

## Methodological and Standards Foundation

- Planning follows the SQA and QC framework mounted at `framework/`: Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code, each step reviewed before the next.
- Quality is assessed with ISO/IEC 25010:2023 characteristics; every QC criterion used in a review carries one.
- Code follows the `coding-conventions` Python rules and the layering of the `clean-architecture` skill (game rules independent of the Turtle library).
- Source comments use Doxygen; tests use pytest.

## Problem Statement

- The course assignment gives a goal and a link to the original game, but no solution structure. Participants struggle to split the game into small steps.
- Solutions shared by participants are often a single long script with no tests, no run instructions and no explanation of the steps.
- A reader who visits a repository to get ideas cannot see how the game grew from an empty window to a finished game.

## Business Opportunity

A clean, step-by-step reference solution lets course participants (S02) compare their approach with another one, and lets repository visitors (S03) borrow ideas. The Product Owner (S01) gets a finished assignment, a worked example of the project framework and a journal of what was learned.

## Objectives

1. O1: Deliver a playable Breakout clone built with Python Turtle, using the function and class names the assignment suggests (paddle, ball, bricks, scoreboard).
2. O2: Keep the game rules independent of Turtle, so they are tested without a window.
3. O3: Document every lecture step with a screenshot in the README and an explanation in the wiki.
4. O4: Publish the wiki in English, Danish and Bahasa Malaysia.
5. O5: Make the repository easy to run: a documented local `.venv`, `pyproject.toml`, tests with pytest and no runtime dependency.
6. O6: Present the repository clearly with a description, topics and README.

## Scope

### In Scope

- Game: window, paddle, ball, bounce on walls and paddle, six rows of bricks in the original's red, orange, green and yellow bands, brick removal, score, lives, win and game over, ball speed-up.
- Project set-up: `pyproject.toml`, `.gitignore`, `.editorconfig`, `constants.py`, Doxyfile and Doxygen comments, README from the framework template.
- Tests with pytest for the game rules.
- Screenshots of each development step, produced in a Docker container.
- Wiki in English, Danish and Bahasa Malaysia.
- Repository description and topics on the git host.
- Local security scan with opengrep before each push.

### Out of Scope

- Sound, power-ups, levels beyond one, a high-score file and a menu.
- Packaging for PyPI or a standalone executable.
- A graphical interface other than Python Turtle.
- Testing the game on the host desktop (the framework forbids it).

## Expected Benefits

### Tangible Benefits

- A finished course assignment in a public repository.
- Tests that run in a few seconds with `python -m pytest`.
- Seven screenshots (one per step) and three language versions of the wiki.

### Intangible Benefits

- A reflection of what was hard and what was learned.
- A worked example of splitting a small game into steps.
- Practice with the planning framework and a clean layering.

## Strategic Alignment

The project supports the Product Owner's learning goal in the 100 Days of Code course and the habit of publishing a readable, documented repository for each assignment.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The game runs | `python -m breakout` opens a window with paddle, ball and bricks | Manual run in a container, screenshot |
| 2 | Tests pass | 100 % of pytest tests pass, 90 % line coverage of the rules package | `python -m pytest` |
| 3 | No runtime dependency | `dependencies = []` in `pyproject.toml` | Read the file |
| 4 | Every step has a screenshot | 7 of 7 steps have a screenshot in the README and the wiki | Count the images |
| 5 | Wiki in three languages | 3 of 3 languages with the same page set | Count the pages |
| 6 | Repository presented | Description and at least 5 topics set | Read the repository page |
| 7 | Security scan clean | 0 opengrep findings of severity error before push | Scan output |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The Turtle window cannot be tested on the host desktop | Screenshots and GUI tests are blocked | Use a Docker container with a virtual display, as `framework/process/gui-testing.md` requires |
| Turtle is slow with many bricks | The game feels laggy | Draw bricks as stamps of one turtle and update the screen by hand with `tracer(0)` |
| Collision maths is wrong at corners | Ball passes through bricks | Keep collision in pure functions and test them |
| The Danish and Malay texts contain errors | Readers are misled | English is the authoritative text; the translation follows page by page and is reviewed |
| A token leaks into the repository | Security incident | `.env` is ignored by git and never read by the project; the scan runs before each push |

## Assumptions

- S01 is Product Owner, developer and reviewer; autonomous work records each review as a stand-in review.
- Python 3.13 or newer, Docker and git are installed on the development machine.
- The git host repository already exists and accepts pushes over SSH.
- The Product Owner's language is English and the domain is IT.
- Course participants (S02) cannot be reached during the project; their needs are taken from the task description.

## Constraints

- Duration: about two hours of building effort, as the assignment states.
- Python greater than or equal to 3.13, a local `.venv`, `pyproject.toml` and pytest.
- Constants are in `constants.py`; the project has no runtime dependency.
- The word for artificial intelligence is not written in any artifact.
- The folder structure is `src/`, `tests/` and `docs/`; one branch and pull request per milestone.
- Tokens are read from `.env` for personal use only; the project does not import or test it.

## Cost–Benefit Assessment

The assessment is qualitative: the project has no budget, and its benefit is learning and a public example, which has no money value.

| Costs | Benefits |
| --- | --- |
| About two hours of build time plus documentation time | A finished assignment and a reusable example |
| Review effort per document | A traceable, reviewed repository |
| Docker and Python on the development machine (already present) | Reproducible screenshots and tests |

## Stakeholders

| ID | Interest in the project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; see [SA-001] |
| S02 | Course participants who compare solutions; see [SA-001] |
| S03 | Repository visitors who browse for ideas; see [SA-001] |

## Recommendation

Proceed.

---

[SA-001]: ./stakeholder-analysis.md
[d4bf2df]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/commit/d4bf2df2d88712f1b4e71c76be15fb497ac94ed4
