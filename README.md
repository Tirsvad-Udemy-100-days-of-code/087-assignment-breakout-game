# 🚀 Breakout

A clone of the 1976 arcade game Breakout, built with Python Turtle as the Day 87 assignment of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp". It is written for course participants who want to compare solutions and for visitors who browse for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

You move a paddle with the left and right arrow keys and bounce a ball against a wall of coloured bricks. Every brick that is hit disappears and adds to the score. You have three lives; you win when the wall is gone.

The repository is built in seven small steps. Each step has a screenshot below and a wiki page in English, Danish and Bahasa Malaysia that explains what the step taught.

| Part | What it is for |
| --- | --- |
| `src/breakout/domain/` | The game rules: pure Python, no Turtle, easy to test |
| `src/breakout/application/` | One game session driven by player commands |
| `src/breakout/presentation/turtle_ui/` | The Turtle views: `Paddle`, `Ball`, `Bricks`, `Scoreboard` and the game loop |
| `src/breakout/constants.py` | Every constant (sizes, speeds, colours, keys) |
| `tests/` | pytest tests of the rules |
| `docs/` | Project documents, screenshots (`docs/images/`) and the wiki sources (`docs/wiki/`) |
| `scripts/`, `tools/` | The local security scan and the screenshot container |

### The steps

| Step | What it adds | Screenshot |
| --- | --- | --- |
| 1 | A black window and a paddle that follows the arrow keys | ![Step 1: window and paddle](docs/images/step-1.png) |
| 2 | A moving ball that bounces off the top and side walls | ![Step 2: ball and wall bounce](docs/images/step-2.png) |
| 3 | The ball bounces off the paddle at an angle that depends on where it hits | ![Step 3: paddle bounce](docs/images/step-3.png) |
| 4 | A wall of six rows of coloured bricks | ![Step 4: wall of bricks](docs/images/step-4.png) |
| 5 | The ball breaks bricks and the score grows | ![Step 5: brick collision and score](docs/images/step-5.png) |
| 6 | Three lives, a game over, a win and a restart with `space` | ![Step 6: lives and game over](docs/images/step-6.png) |
| 7 | The ball speeds up as the game goes on | ![Step 7: speed-up](docs/images/step-7.png) |

Source comments are Doxygen blocks; `Doxyfile` builds the reference.

## 📋 Requirements

- Python 3.13 or newer with Tk (the standard Python installer for Windows and macOS includes it; on Debian or Ubuntu install `python3-tk`). Turtle needs Tk to draw the window.
- Nothing else is needed to play: the game has no runtime dependency.
- To develop: `pytest`, `pytest-cov`, `ruff` and `mypy` (installed by the `dev` extra below).
- Optional: Doxygen (reference), Docker (screenshots) and opengrep (security scan).

## 🛠️ Setup

Create a local virtual environment named `.venv` in the project folder, activate it and upgrade pip.

PowerShell (Windows):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

bash (Linux, macOS, Git Bash):

```bash
python -m venv .venv
source .venv/bin/activate        # Git Bash on Windows: source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Install the git hooks once per clone. They stop a commit on `main` and, with the plan gate, a change to `src/` or `tests/` that has no `Task: MIL-NNN#N` line for an accepted milestone:

```bash
bash framework/scripts/install-git-hooks.sh --enable-plan-gate
```

Leave the environment with `deactivate`. The `.venv` folder is ignored by git. Without the `dev` extra (`python -m pip install -e .`) you can still play.

Tokens for the git host are kept in a `.env` file at the root. It is ignored by git and only used by hand for repository maintenance; the game and the tests never read it.

## ▶️ Run

With the virtual environment active:

```bash
python -m breakout
```

Controls: `Left` and `Right` arrow keys move the paddle, `space` starts a new game after a win or a game over.

## 🧪 Tests

```bash
python -m pytest
python -m pytest --cov            # with coverage; the rules must stay above 90 %
python -m ruff check .            # lint
python -m mypy src tests tools   # types
lint-imports                       # the layers point inward
```

The tests cover the game rules and never open a window. A screenshot of a step is taken in a Docker container with a virtual display, never on your desktop:

```bash
bash tools/screenshots/run.sh <step 0-7> <git ref> docs/images/step-<step>.png
```

Before every push run the local security scan (opengrep, installed in `~/.opengrep/cli/latest`):

```bash
bash scripts/scan.sh               # PowerShell: .\scripts\scan.ps1
```

Build the Doxygen reference with:

```bash
mkdir -p build/doxygen
doxygen Doxyfile                   # open build/doxygen/html/index.html
```

## 📄 License

See [LICENSE](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The working rules of this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Wiki][documentation] | One page per development step and a reflection, in English, Danish and Bahasa Malaysia |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
