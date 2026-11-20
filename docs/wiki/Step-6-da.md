# Trin 6: Liv, game over og sejr

[English](Step-6) · **Dansk** · [Bahasa Malaysia](Step-6-ms)

![Trin 6: Liv, game over og sejr](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-6.png)

## Hvad vi byggede

- Spilleren har tre liv. En bold, der falder ud i bunden, koster et liv og giver en ny bold.
- Uden flere liv viser spillet `GAME OVER`; når den sidste klods er væk, viser det `YOU WIN!`.
- Mellemrumstasten starter et nyt spil.
- Scoreboardet viser point til venstre og liv til højre.

## Nøglekode

```python
class GameStatus(Enum):
    PLAYING = "playing"
    WON = "won"
    LOST = "lost"
```

Hele kildekoden ligger i [repositoriet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Hvad vi fik ud af det

- **En tilstandsmaskine.** `GameStatus` har tre værdier: i gang, vundet og tabt. `tick()` gør intet, medmindre spillet er i gang, så et afsluttet spil ikke kan ændre sig ved et uheld.
- **Én vej til start.** Start af et spil og en genstart bruger den samme `_reset`-metode, så man ikke kan glemme at nulstille noget.
- **Beskeder ud fra tilstand.** Scoreboardet tegnes ud fra `(score, lives, status)`. Når tilstanden ændres, følger billedet med, uden ekstra bogføring.

[Forrige: Trin 5](Step-5-da) · [Næste: Trin 7](Step-7-da)
