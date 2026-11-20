# Langkah 1: Tetingkap dan dayung

[English](Step-1) · [Dansk](Step-1-da) · **Bahasa Malaysia**

![Langkah 1: Tetingkap dan dayung](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-1.png)

## Apa yang kami bina

- Tetingkap hitam 800 kali 600 yang dibuat dengan `turtle.Screen`.
- Paparan `Paddle`: segi empat tepat biru yang dibuat daripada bentuk petak terbina dalam.
- Kekunci anak panah kiri dan kanan menggerakkan dayung sebanyak 30 piksel setiap kali.
- Dayung tidak boleh keluar dari tetingkap. Peraturan ini terletak dalam kelas `Paddle` yang tulen di lapisan domain, bukan dalam paparan.

## Kod utama

```python
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)  # we decide when a frame is drawn

def moved_to(self, x: float) -> "Paddle":
    limit = constants.RIGHT_WALL - self.width / 2
    return replace(self, x=max(-limit, min(limit, x)))
```

Kod sumber penuh terdapat dalam [repositori](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Apa yang kami peroleh

- **Keadaan dan lukisan dipisahkan.** `Paddle` dalam domain ialah kelas data kecil yang tidak berubah, dan paparan Turtle hanya melukisnya. Sebab itu peraturan boleh diuji tanpa tetingkap.
- **Lukisan manual.** `screen.tracer(0)` mematikan lukisan automatik, jadi satu panggilan `screen.update()` bagi setiap bingkai melukis segala-galanya serentak dan animasi tidak berkelip.
- **Input papan kekunci.** `screen.listen()` dan `screen.onkeypress(...)` menyambungkan sebuah kekunci kepada sebuah kaedah.
- **Mengehadkan nilai.** `max(-limit, min(limit, x))` mengekalkan nilai dalam julat, helah yang digunakan berulang kali dalam permainan.

[Sebelumnya: Bermula](Getting-Started-ms) · [Seterusnya: Langkah 2](Step-2-ms)
