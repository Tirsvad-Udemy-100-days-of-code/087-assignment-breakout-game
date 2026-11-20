# Trin 2: Bold og vægbounce

[English](Step-2) · **Dansk** · [Bahasa Malaysia](Step-2-ms)

![Trin 2: Bold og vægbounce](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-2.png)

## Hvad vi byggede

- En hvid firkantet bold, der flytter sig lidt i hvert billede.
- Bolden preller af på venstre, højre og øverste væg.
- En bold, der falder ud i bunden, starter forfra fra startpositionen.
- Billedløkken bruger `screen.ontimer(...)` og `mainloop()` i stedet for `time.sleep()`, så vinduet forbliver responsivt og kan lukkes når som helst.

## Nøglekode

```python
def advanced(self) -> "Ball":
    return replace(self, x=self.x + self.dx, y=self.y + self.dy)

if x - half <= constants.LEFT_WALL:
    x, dx = constants.LEFT_WALL + half, abs(dx)
```

Hele kildekoden ligger i [repositoriet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## Hvad vi fik ud af det

- **Spilløkken.** I hvert billede flytter spillet tingene, tjekker reglerne og tegner. Alt i spillet bygger på denne rytme.
- **Fart som vektor.** `dx` og `dy` er pixels pr. billede. Et bounce vender kun den komponent, der ramte væggen.
- **Ingen hængen fast.** Efter et bounce lægges bolden tilbage inde i væggen, så den ikke kan sidde fast i væggen i flere billeder.
- **Uforanderlige værdier.** `advanced()` returnerer en ny `Ball` i stedet for at ændre den gamle. Funktioner, der returnerer nye værdier, er nemme at teste.

[Forrige: Trin 1](Step-1-da) · [Næste: Trin 3](Step-3-da)
