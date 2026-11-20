# Trin 3: Batbounce

[English](Step-3) · **Dansk** · [Bahasa Malaysia](Step-3-ms)

![Trin 3: Batbounce](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-3.png)

## Hvad vi byggede

- En faldende bold, der rører batten, preller opad.
- Hvor bolden rammer, bestemmer vinklen: midten sender den lige op, kanterne sender den ud til siden (højst 80 % af farten).
- Boldens fart er den samme; kun retningen ændres.

## Nøglekode

```python
offset = max(-1.0, min(1.0, (ball.x - paddle.x) / (paddle.width / 2)))
speed = math.hypot(ball.dx, ball.dy)
dx = offset * constants.PADDLE_BOUNCE_MAX_SIDEWAYS * speed
dy = math.sqrt(speed**2 - dx**2)
```

Hele kildekoden ligger i [repositoriet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Hvad vi fik ud af det

- **Spilfølelse.** Et bounce, der altid går samme vej, er kedeligt. Når spilleren kan sigte med batten, bliver legetøj til et spil.
- **Fartens bevarelse.** Med `math.hypot` måler vi farten, og med `math.sqrt(speed**2 - dx**2)` beregner vi den lodrette del, så farten aldrig ændres ved et uheld.
- **Grænsetilfælde er tests.** En stigende bold går igennem batten, en bold ved siden af batten rammer forbi, og en bold under battens midte tæller ikke som et træf. Hvert tilfælde har sin egen test.

[Forrige: Trin 2](Step-2-da) · [Næste: Trin 4](Step-4-da)
