# Langkah 5: Perlanggaran bata dan skor

[English](Step-5) · [Dansk](Step-5-da) · **Bahasa Malaysia**

![Langkah 5: Perlanggaran bata dan skor](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-5.png)

## Apa yang kami bina

- Apabila bola menyentuh bata, bata itu hilang dan skor bertambah dengan mata barisnya.
- Bola dipantulkan pada paksi yang betul: kena di sisi bata membalikkan `dx`, kena dari bawah atau atas membalikkan `dy`.
- `Scoreboard` menulis skor di bahagian atas, dan hanya apabila skor berubah.

## Kod utama

```python
depth_x, depth_y = _overlap_depth(ball.box, brick.box)
if depth_x < depth_y:  # the ball hit the side of the brick
    dx = -abs(ball.dx) if ball.x < brick.x else abs(ball.dx)
    return replace(ball, dx=dx), brick
dy = -abs(ball.dy) if ball.y < brick.y else abs(ball.dy)
return replace(ball, dy=dy), brick
```

Kod sumber penuh terdapat dalam [repositori](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Apa yang kami peroleh

- **Pertindihan segi empat tepat.** Dua segi empat tepat bersentuhan apabila ia bertindih pada kedua-dua paksi. Satu ujian itu ialah teras hampir semua permainan 2D yang mudah.
- **Sisi mana yang terkena?** Kami membandingkan sedalam mana bola masuk ke dalam bata pada setiap paksi. Kedalaman yang lebih kecil ialah sisi tempat bola datang. Ini lebih boleh dipercayai daripada melihat arah bola.
- **Satu bata setiap bingkai.** Jika bola menyentuh dua bata, bata yang paling dalam dimasuki yang terkena, jadi satu bingkai tidak pernah memecahkan dua bata.
- **Lukisan yang murah.** Papan skor hanya memadam dan menulis apabila teks berubah. Melukis teks pada setiap bingkai akan memperlahankan permainan.

[Sebelumnya: Langkah 4](Step-4-ms) · [Seterusnya: Langkah 6](Step-6-ms)
