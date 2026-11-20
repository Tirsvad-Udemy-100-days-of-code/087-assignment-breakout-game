# Langkah 6: Nyawa, permainan tamat dan menang

[English](Step-6) · [Dansk](Step-6-da) · **Bahasa Malaysia**

![Langkah 6: Nyawa, permainan tamat dan menang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-6.png)

## Apa yang kami bina

- Pemain mempunyai tiga nyawa. Bola yang jatuh keluar dari bawah mengurangkan satu nyawa dan memberi bola baharu.
- Apabila nyawa habis, permainan menunjukkan `GAME OVER`; apabila bata terakhir hilang, ia menunjukkan `YOU WIN!`.
- Kekunci `space` memulakan permainan baharu.
- Papan skor menunjukkan skor di sebelah kiri dan nyawa di sebelah kanan.

## Kod utama

```python
class GameStatus(Enum):
    PLAYING = "playing"
    WON = "won"
    LOST = "lost"
```

Kod sumber penuh terdapat dalam [repositori](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Apa yang kami peroleh

- **Mesin keadaan.** `GameStatus` mempunyai tiga nilai: sedang bermain, menang dan kalah. `tick()` tidak berbuat apa-apa melainkan permainan sedang berjalan, jadi permainan yang sudah tamat tidak boleh berubah secara tidak sengaja.
- **Satu cara untuk bermula.** Permulaan permainan dan permulaan semula menggunakan kaedah `_reset` yang sama, jadi tiada cara untuk terlupa menetapkan semula sesuatu.
- **Mesej daripada keadaan.** Papan skor dilukis daripada `(score, lives, status)`. Apabila keadaan berubah, gambar mengikutinya tanpa pencatatan tambahan.

[Sebelumnya: Langkah 5](Step-5-ms) · [Seterusnya: Langkah 7](Step-7-ms)
