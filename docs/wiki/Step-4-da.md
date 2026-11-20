# Trin 4: Mur af klodser

[English](Step-4) · **Dansk** · [Bahasa Malaysia](Step-4-ms)

![Trin 4: Mur af klodser](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-4.png)

## Hvad vi byggede

- Seks rækker med 14 klodser: to røde, en orange, to grønne og en gul.
- Hver klods giver point efter farve (7, 7, 5, 3, 3, 1).
- Muren er centreret i vinduet, og alle mål kommer fra `constants.py`.
- `Bricks`-viewet laver én turtle pr. klods og skjuler turtlen, når klodsen er væk.

## Nøglekode

```python
first_x = -(columns - 1) * pitch_x / 2
Brick(
    x=first_x + column * pitch_x,
    y=constants.BRICK_TOP_ROW_Y - row * pitch_y,
    color=color,
    points=constants.BRICK_ROW_POINTS[row],
)
```

Hele kildekoden ligger i [repositoriet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Hvad vi fik ud af det

- **Datastyret layout.** `build_wall()` laver muren ud fra nogle få konstanter. For at ændre antal rækker, farver eller point ændrer vi én fil og ikke koden.
- **Centrering med regning.** Første kolonne starter ved `-(columns - 1) * pitch / 2`, så muren er symmetrisk uanset antal kolonner.
- **Ét sted til konstanter.** En regel om, at intet tal skrives to gange (heller ikke `20`, størrelsen på Turtle-firkanten), gør koden nem at ændre.

[Forrige: Trin 3](Step-3-da) · [Næste: Trin 5](Step-5-da)
