# Langkah 2: Bola dan pantulan dinding

[English](Step-2) · [Dansk](Step-2-da) · **Bahasa Malaysia**

![Langkah 2: Bola dan pantulan dinding](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-2.png)

## Apa yang kami bina

- Bola petak putih yang bergerak sedikit pada setiap bingkai.
- Bola memantul pada dinding kiri, kanan dan atas.
- Bola yang jatuh keluar dari bahagian bawah bermula semula dari kedudukan permulaan.
- Gelung bingkai menggunakan `screen.ontimer(...)` dan `mainloop()` dan bukan `time.sleep()`, jadi tetingkap kekal responsif dan boleh ditutup pada bila-bila masa.

## Kod utama

```python
def advanced(self) -> "Ball":
    return replace(self, x=self.x + self.dx, y=self.y + self.dy)

if x - half <= constants.LEFT_WALL:
    x, dx = constants.LEFT_WALL + half, abs(dx)
```

Kod sumber penuh terdapat dalam [repositori](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Apa yang kami peroleh

- **Gelung permainan.** Pada setiap bingkai permainan menggerakkan benda, menyemak peraturan dan melukis. Segala-galanya dalam permainan dibina atas rentak ini.
- **Kelajuan sebagai vektor.** `dx` dan `dy` ialah piksel setiap bingkai. Pantulan hanya membalikkan komponen yang terkena dinding.
- **Tidak melekat.** Selepas pantulan, bola diletakkan semula di dalam dinding, jadi ia tidak tersangkut pada dinding selama beberapa bingkai.
- **Nilai yang tidak berubah.** `advanced()` mengembalikan `Ball` baharu dan bukan mengubah yang lama. Fungsi yang mengembalikan nilai baharu mudah diuji.

[Sebelumnya: Langkah 1](Step-1-ms) · [Seterusnya: Langkah 3](Step-3-ms)
