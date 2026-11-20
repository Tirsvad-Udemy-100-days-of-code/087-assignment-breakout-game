# MIL-001 G1 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed Go in RC-004, stand-in review, not independent | [d4bf2df] |

---

## Purpose

Decides whether the repository is ready to receive game code: it is presented on the git host, configured, documented and equipped with the tools the later gateways use (tests, scan, screenshots).

## Deliverable

A configured Python 3.13 project skeleton (`pyproject.toml`, `.gitignore`, `.editorconfig`, `src/breakout/constants.py`, `tests/`), a README from the framework template with `.venv` instructions, a Doxyfile, a local opengrep scan command, a Docker image that takes screenshots, and the repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pip install -e ".[dev]"` and `python -m pytest` succeed in a fresh `.venv` (one smoke test passes) | Met | Not met |
| 2 | `pyproject.toml` has `requires-python = ">=3.13"` and `dependencies = []` | Met | Not met |
| 3 | `bash framework/scripts/check-editorconfig.sh` and `bash framework/scripts/check-readme.sh` pass | Met | Not met |
| 4 | The opengrep scan reports 0 findings of severity error | Met | Not met |
| 5 | The repository page shows a description and at least 5 topics | Met | Not met |
| 6 | The screenshot container produces a PNG of an empty Turtle window | Met | Not met |
| 7 | Pull request opened with `Closes #N` lines for every task, and its checks are green | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First gateway; the Business Case, Stakeholder Analysis and Project Plan are accepted |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O5, O6 | [BC-001] Objectives |
| CN-004, CN-005, CN-006 | [SA-001] concern register |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-20 — the first day of the project; no earlier than the Business Case acceptance.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Write a one-sentence description and at least five topics (for example python, turtle, breakout, arcade-game, 100-days-of-code) on the git host through its API, using the token from `.env`. The token is read from the environment for this one call and is never put into the project. Serves objective O6 and concern CN-005. | No | [BC-001] |
| 2 | Create pyproject.toml, .gitignore and .editorconfig | Add `pyproject.toml` (Python 3.13 or newer, no runtime dependency, pytest in a `dev` extra, `src` layout), a Python `.gitignore` that also ignores `.env` and `.venv`, and the root `.editorconfig` from the framework baseline template. Checked by `check-editorconfig.sh`. | No | [BC-001] |
| 3 | Create the package skeleton and constants.py | Add `src/breakout/` with `__init__.py`, `__main__.py` and `constants.py` (window size, colours, speeds, brick layout) and the empty layer packages, plus `tests/` with a smoke test. All constants live in `constants.py` so the later steps have no magic numbers. | No | [BC-001] |
| 4 | Add Doxyfile and Doxygen comment convention | Add a `Doxyfile` that reads `src/` and writes to `build/doxygen/`, and use Doxygen comment blocks (`@brief`, `@param`, `@return`) in every source file from the start. The generated output is ignored by git. | No | [BC-001] |
| 5 | Write the README from the framework template | Fill the framework README template: overview, requirements, how to create and use a local `.venv`, `python -m pip install --upgrade pip`, how to run the game and the tests, the license and the document appendix. The step screenshots are added by the later gateways. Checked by `check-readme.sh`. | No | [BC-001] |
| 6 | Add the local opengrep scan command | Add a documented command and a small script that runs `opengrep.exe` from the user profile against `src/` and `tests/` and fails on error-severity findings. It is run before every push. | No | [BC-001] |
| 7 | Build the screenshot container | Add a Docker image with Python, Tk, a virtual display and an image-capture tool, and a script that runs the game in it and saves a PNG. The GUI is never run on the host desktop (`framework/process/gui-testing.md`). Proven here with an empty window. | No | [BC-001] |
| 8 | Install git hooks and the plan gate | Run `framework/scripts/install-git-hooks.sh --enable-plan-gate` so a commit that changes `src/` or `tests/` needs a `Task: MIL-NNN#N` trailer, and record the commands in the README. | No | [BC-001] |

---

[BC-001]: ../business-case.md
[d4bf2df]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/commit/d4bf2df2d88712f1b4e71c76be15fb497ac94ed4
