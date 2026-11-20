# Trin 1: Vindue og bat

[English](Step-1) · **Dansk** · [Bahasa Malaysia](Step-1-ms)

![Trin 1: Vindue og bat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-1.png)

## Hvad vi byggede

- Et sort vindue på 800 gange 600 lavet med `turtle.Screen`.
- Et `Paddle`-view: et blåt rektangel lavet af den indbyggede firkantform.
- Venstre- og højrepilene flytter batten 30 pixels ad gangen.
- Batten kan aldrig forlade vinduet. Reglen ligger i den rene `Paddle`-klasse i domænelaget og ikke i viewet.

## Nøglekode

```python
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)  # we decide when a frame is drawn

def moved_to(self, x: float) -> "Paddle":
    limit = constants.RIGHT_WALL - self.width / 2
    return replace(self, x=max(-limit, min(limit, x)))
```

Hele kildekoden ligger i [repositoriet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Hvad vi fik ud af det

- **Tilstand og tegning er adskilt.** Domænets `Paddle` er en lille uforanderlig dataklasse, og Turtle-viewet tegner den kun. Derfor kan reglen testes uden et vindue.
- **Manuel tegning.** `screen.tracer(0)` slår automatisk tegning fra, så ét kald til `screen.update()` pr. billede tegner alt på én gang, og animationen flimrer ikke.
- **Tastaturinput.** `screen.listen()` og `screen.onkeypress(...)` forbinder en tast med en metode.
- **Begrænsning.** `max(-limit, min(limit, x))` holder en værdi inden for et interval, et trick der bruges igen og igen i spil.

[Forrige: Kom i gang](Getting-Started-da) · [Næste: Trin 2](Step-2-da)
