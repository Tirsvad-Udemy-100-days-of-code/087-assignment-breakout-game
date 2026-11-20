# Langkah 3: Pantulan dayung

[English](Step-3) · [Dansk](Step-3-da) · **Bahasa Malaysia**

![Langkah 3: Pantulan dayung](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-3.png)

## Apa yang kami bina

- Bola yang jatuh dan menyentuh dayung akan memantul ke atas.
- Tempat bola terkena menentukan sudut: bahagian tengah menghantarnya lurus ke atas, bahagian tepi menghantarnya ke sisi (paling banyak 80 % daripada kelajuan).
- Kelajuan bola kekal sama; hanya arah yang berubah.

## Kod utama

```python
offset = max(-1.0, min(1.0, (ball.x - paddle.x) / (paddle.width / 2)))
speed = math.hypot(ball.dx, ball.dy)
dx = offset * constants.PADDLE_BOUNCE_MAX_SIDEWAYS * speed
dy = math.sqrt(speed**2 - dx**2)
```

Kod sumber penuh terdapat dalam [repositori](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Apa yang kami peroleh

- **Rasa permainan.** Pantulan yang sentiasa ke arah yang sama membosankan. Apabila pemain boleh membidik dengan dayung, mainan menjadi permainan.
- **Mengekalkan kelajuan.** Dengan `math.hypot` kami mengukur kelajuan dan dengan `math.sqrt(speed**2 - dx**2)` kami mengira bahagian menegak, jadi kelajuan tidak berubah secara tidak sengaja.
- **Kes tepi ialah ujian.** Bola yang naik melepasi dayung, bola di sebelah dayung terlepas, dan bola di bawah pusat dayung tidak dikira sebagai kena. Setiap kes ada ujiannya sendiri.

[Sebelumnya: Langkah 2](Step-2-ms) · [Seterusnya: Langkah 4](Step-4-ms)
