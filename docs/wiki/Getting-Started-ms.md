# Bermula

[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

![Tetingkap permainan kosong, bukti pertama bahawa persediaan berfungsi](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-0.png)

## Apa yang anda perlukan

- Python 3.13 atau lebih baharu dengan Tk. Pemasang dari python.org untuk Windows dan macOS sudah termasuk Tk; pada Debian atau Ubuntu pasang `python3-tk`.
- Git, untuk mendapatkan kod.
- Pilihan: Docker (tangkapan skrin), Doxygen (rujukan kod) dan opengrep (imbasan keselamatan).

## Cipta persekitaran maya setempat

PowerShell pada Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

bash pada Linux, macOS atau Git Bash:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Folder `.venv` hanya milik projek ini dan diabaikan oleh git. Keluar daripadanya dengan `deactivate`.

## Bermain

```bash
python -m breakout
```

Gunakan kekunci anak panah `Left` dan `Right`. Selepas menang atau permainan tamat, tekan `space` untuk bermain semula.

## Jalankan ujian

```bash
python -m pytest --cov
python -m ruff check .
python -m mypy src tests tools
lint-imports
```

Ujian tidak pernah membuka tetingkap. Untuk mengambil tangkapan skrin sesuatu langkah, bekas Docker dengan skrin maya digunakan, jadi tetikus dan papan kekunci anda sendiri tidak pernah disentuh:

```bash
bash tools/screenshots/run.sh 3 HEAD docs/images/step-3.png
```

## Sebelum anda push

```bash
bash scripts/scan.sh
```

[Seterusnya: Langkah 1](Step-1-ms)
