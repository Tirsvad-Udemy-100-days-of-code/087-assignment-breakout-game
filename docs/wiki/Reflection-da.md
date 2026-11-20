# Refleksion

[English](Reflection) · **Dansk** · [Bahasa Malaysia](Reflection-ms)

## Sådan greb vi projektet an

Vi startede med en liste over, hvad spillet skal kunne, og delte den i syv trin, som hver kan køres og ses: vindue og bat, bold, batbounce, klodser, kollisioner og point, liv og afslutning, hastighedsforøgelse. Før vi skrev kode, skrev vi ned, hvem projektet er til, hvad det skal levere, og i hvilken rækkefølge. Derefter blev hvert trin bygget, testet, gennemgået og fotograferet, før det næste begyndte.

## Hvad var svært

- **Kollisionssider.** At afgøre, om en bold ramte siden eller toppen af en klods, krævede mest eftertanke. Svaret var at sammenligne, hvor dybt bolden trænger ind på hver akse, og hjørnetræf krævede endnu en regel.
- **Tunnelering.** En hurtig bold kan springe over en tynd genstand. Vi måtte bevise, at maksimalfarten er mindre end det mindste, bolden skal ramme.
- **Skærmbilleder uden at røre skrivebordet.** At køre et vindue i en container med en virtuel skærm krævede noget opsætning, men gav os gentagelige billeder af den præcise kode fra hvert trin.
- **Små værktøjsproblemer.** Linjeskift, der er forskellige på Windows og Linux, fik kontrollen af shell-scripts til at fejle i pipelinen, indtil vi rettede det.

## Hvad var nemt

- Turtle er hurtig at komme i gang med: et vindue og en bevægelig figur kræver kun få linjer.
- Fordi reglerne ikke afhænger af Turtle, var testene korte og hurtige.

## Den største læring

Hold reglerne og tegningen adskilt. Da spillets regler var almindelige Python-funktioner på små uforanderlige værdier, kunne næsten alle fejl fanges af en test på millisekunder, og vi kunne spille et helt spil uden et vindue.

## Hvad vi ville gøre anderledes

- Skrive kollisionstestene før kollisionskoden for at finde hjørnetilfældet tidligere.
- Vælge billedløkken med `ontimer` fra starten i stedet for `time.sleep`.
- Tilføje lyd, baner og en highscore-liste. Det lå uden for denne opgave.

[Tilbage til Hjem](Home-da)
