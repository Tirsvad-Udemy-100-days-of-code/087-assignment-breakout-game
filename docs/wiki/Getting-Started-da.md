# Kom i gang

[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

![Et tomt spilvindue, det første bevis på at opsætningen virker](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-0.png)

## Det skal du bruge

- Python 3.13 eller nyere med Tk. Installationsprogrammet fra python.org til Windows og macOS indeholder Tk; på Debian eller Ubuntu installeres `python3-tk`.
- Git, for at hente koden.
- Valgfrit: Docker (skærmbilleder), Doxygen (kodereference) og opengrep (sikkerhedsscanning).

## Opret et lokalt virtuelt miljø

PowerShell på Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

bash på Linux, macOS eller Git Bash:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Mappen `.venv` hører kun til dette projekt og ignoreres af git. Forlad miljøet med `deactivate`.

## Spil

```bash
python -m breakout
```

Brug piletasterne `Left` og `Right`. Efter en sejr eller et game over trykker du på `space` for at spille igen.

## Kør testene

```bash
python -m pytest --cov
python -m ruff check .
python -m mypy src tests tools
lint-imports
```

Testene åbner aldrig et vindue. Til et skærmbillede af et trin bruges en Docker-container med en virtuel skærm, så din egen mus og dit tastatur aldrig bruges:

```bash
bash tools/screenshots/run.sh 3 HEAD docs/images/step-3.png
```

## Før du pusher

```bash
bash scripts/scan.sh
```

[Næste: Trin 1](Step-1-da)
