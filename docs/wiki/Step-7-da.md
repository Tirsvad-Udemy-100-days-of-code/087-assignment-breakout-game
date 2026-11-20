# Trin 7: Hastighedsforøgelse og finpudsning

[English](Step-7) · **Dansk** · [Bahasa Malaysia](Step-7-ms)

![Trin 7: Hastighedsforøgelse og finpudsning](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-7.png)

## Hvad vi byggede

- Bolden bliver 10 % hurtigere efter hvert fjerde træf på batten og første gang den rammer en rød klods, op til en maksimal fart.
- En ny bold efter en bold, der gik forbi batten, starter med normal fart.
- To tests uden vindue spiller et helt spil: en styret bat vinder, en parkeret bat taber.
- En test tjekker, at den hurtigste bold stadig er langsommere end den mindste klods eller bat, den ikke må springe over.

## Nøglekode

```python
BALL_SPEEDUP_EVERY = 4
BALL_SPEEDUP_FACTOR = 1.1
BALL_MAX_SPEED = 12.0
```

Hele kildekoden ligger i [repositoriet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Hvad vi fik ud af det

- **En sværhedskurve.** En lille hastighedsforøgelse gør spillet sværere på en måde, spilleren kan mærke. Et loft holder det retfærdigt.
- **Tunnelering.** En hurtig bold kan springe over en tynd genstand mellem to billeder. Vi testede, at maksimalfarten er mindre end det mindste, bolden skal ramme.
- **Test uden vindue.** Fordi reglerne er ren Python, kører et helt spil på brøkdele af et sekund i en test. Selve vinduet kontrolleres ved at tage skærmbilleder i en Docker-container.
- **En scriptet spiller.** En bat, der altid griber bolden i midten, får bolden til at flyve lige op og ned for evigt. Testen varierer, hvor bolden gribes, og det er også sådan en rigtig spiller sigter.

[Forrige: Trin 6](Step-6-da) · [Næste: Refleksion](Reflection-da)
