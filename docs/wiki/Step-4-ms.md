# Langkah 4: Dinding bata

[English](Step-4) · [Dansk](Step-4-da) · **Bahasa Malaysia**

![Langkah 4: Dinding bata](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-4.png)

## Apa yang kami bina

- Enam baris dengan 14 bata: dua merah, satu jingga, dua hijau dan satu kuning.
- Setiap bata bernilai mata mengikut warna (7, 7, 5, 3, 3, 1).
- Dinding diletakkan di tengah tetingkap dan semua saiz datang daripada `constants.py`.
- Paparan `Bricks` membuat satu turtle bagi setiap bata dan menyembunyikan turtle itu apabila batanya sudah tiada.

## Kod utama

```python
first_x = -(columns - 1) * pitch_x / 2
Brick(
    x=first_x + column * pitch_x,
    y=constants.BRICK_TOP_ROW_Y - row * pitch_y,
    color=color,
    points=constants.BRICK_ROW_POINTS[row],
)
```

Kod sumber penuh terdapat dalam [repositori](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Apa yang kami peroleh

- **Susun atur berasaskan data.** `build_wall()` membuat dinding daripada beberapa pemalar. Untuk menukar bilangan baris, warna atau mata, kami menukar satu fail dan bukan kod.
- **Memusatkan dengan aritmetik.** Lajur pertama bermula pada `-(columns - 1) * pitch / 2`, jadi dinding simetri walau berapa pun bilangan lajur.
- **Satu tempat untuk pemalar.** Peraturan bahawa tiada nombor ditulis dua kali (termasuk `20`, saiz petak Turtle) memudahkan kod diubah.

[Sebelumnya: Langkah 3](Step-3-ms) · [Seterusnya: Langkah 5](Step-5-ms)
