# Getting Started

**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

![An empty game window, the first proof that the set-up works](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-0.png)

## What you need

- Python 3.13 or newer with Tk. The installer from python.org for Windows and macOS includes Tk; on Debian or Ubuntu install `python3-tk`.
- Git, to get the code.
- Optional: Docker (screenshots), Doxygen (code reference) and opengrep (security scan).

## Create a local virtual environment

PowerShell on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

bash on Linux, macOS or Git Bash:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The `.venv` folder belongs to this project only and is ignored by git. Leave it with `deactivate`.

## Play

```bash
python -m breakout
```

Use the `Left` and `Right` arrow keys. After a win or a game over press `space` to play again.

## Run the tests

```bash
python -m pytest --cov
python -m ruff check .
python -m mypy src tests tools
lint-imports
```

The tests never open a window. To take a screenshot of a step, a Docker container with a virtual display is used, so your own mouse and keyboard are never touched:

```bash
bash tools/screenshots/run.sh 3 HEAD docs/images/step-3.png
```

## Before you push

```bash
bash scripts/scan.sh
```

[Next: Step 1](Step-1)
