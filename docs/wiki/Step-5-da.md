# Trin 5: Klodskollision og point

[English](Step-5) · **Dansk** · [Bahasa Malaysia](Step-5-ms)

![Trin 5: Klodskollision og point](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-5.png)

## Hvad vi byggede

- Når bolden rører en klods, forsvinder klodsen, og scoren stiger med rækkens point.
- Bolden reflekteres på den rigtige akse: et træf på siden af en klods vender `dx`, et træf nedefra eller oppefra vender `dy`.
- En `Scoreboard` skriver scoren øverst, og kun når den ændres.

## Nøglekode

```python
depth_x, depth_y = _overlap_depth(ball.box, brick.box)
if depth_x < depth_y:  # the ball hit the side of the brick
    dx = -abs(ball.dx) if ball.x < brick.x else abs(ball.dx)
    return replace(ball, dx=dx), brick
dy = -abs(ball.dy) if ball.y < brick.y else abs(ball.dy)
return replace(ball, dy=dy), brick
```

Hele kildekoden ligger i [repositoriet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Hvad vi fik ud af det

- **Overlap af rektangler.** To rektangler rører hinanden, når de overlapper på begge akser. Den ene test er kernen i næsten ethvert simpelt 2D-spil.
- **Hvilken side blev ramt?** Vi sammenligner, hvor dybt bolden trænger ind i klodsen på hver akse. Den mindste dybde er den side, bolden kom fra. Det er mere pålideligt end at se på boldens retning.
- **Én klods pr. billede.** Hvis bolden rører to klodser, rammes den, den trænger dybest ind i, så ét billede aldrig smadrer to klodser.
- **Billig tegning.** Scoreboardet rydder og skriver kun, når teksten ændres. At tegne tekst i hvert billede ville gøre spillet langsomt.

[Forrige: Trin 4](Step-4-da) · [Næste: Trin 6](Step-6-da)
