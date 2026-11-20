# Langkah 7: Peningkatan kelajuan dan kemasan

[English](Step-7) · [Dansk](Step-7-da) · **Bahasa Malaysia**

![Langkah 7: Peningkatan kelajuan dan kemasan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-7.png)

![Satu permainan penuh dari mula hingga menang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/game.gif)

## Apa yang kami bina

- Bola menjadi 10 % lebih laju selepas setiap pukulan dayung yang keempat dan kali pertama ia terkena bata merah, sehingga kelajuan maksimum.
- Bola baharu selepas bola terlepas bermula dengan kelajuan biasa.
- Dua ujian tanpa tetingkap memainkan satu permainan penuh: dayung berskrip menang, dayung yang diparkir kalah.
- Satu ujian menyemak bahawa bola yang paling laju masih lebih perlahan daripada bata atau dayung terkecil yang tidak boleh dilangkaunya.

## Kod utama

```python
BALL_SPEEDUP_EVERY = 4
BALL_SPEEDUP_FACTOR = 1.1
BALL_MAX_SPEED = 12.0
```

Kod sumber penuh terdapat dalam [repositori](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Apa yang kami peroleh

- **Lengkung kesukaran.** Peningkatan kelajuan yang kecil menjadikan permainan lebih sukar dengan cara yang dirasai pemain. Had maksimum menjadikannya adil.
- **Terowongan.** Bola yang laju boleh melompati objek nipis antara dua bingkai. Kami menguji bahawa kelajuan maksimum lebih kecil daripada benda terkecil yang mesti dikenanya.
- **Ujian tanpa tetingkap.** Oleh sebab peraturan ialah Python tulen, satu permainan penuh berjalan dalam masa kurang satu saat dalam ujian. Tetingkap itu sendiri disemak dengan mengambil tangkapan skrin dalam bekas Docker.
- **Pemain berskrip.** Dayung yang sentiasa menyambut bola di tengah menyebabkan bola terbang lurus ke atas dan ke bawah selama-lamanya. Ujian mengubah tempat bola disambut, dan itulah juga cara pemain sebenar membidik.

[Sebelumnya: Langkah 6](Step-6-ms) · [Seterusnya: Refleksi](Reflection-ms)
