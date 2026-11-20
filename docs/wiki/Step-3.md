# Step 3: Paddle bounce

**English** · [Dansk](Step-3-da) · [Bahasa Malaysia](Step-3-ms)

![Step 3: Paddle bounce](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-3.png)

## What we built

- A falling ball that touches the paddle bounces up.
- Where the ball hits decides the angle: the centre sends it straight up, the edges send it sideways (at most 80 % of the speed).
- The ball speed stays the same; only the direction changes.

## Key code

```python
offset = max(-1.0, min(1.0, (ball.x - paddle.x) / (paddle.width / 2)))
speed = math.hypot(ball.dx, ball.dy)
dx = offset * constants.PADDLE_BOUNCE_MAX_SIDEWAYS * speed
dy = math.sqrt(speed**2 - dx**2)
```

The full source is in the [repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## What we gained

- **Game feel.** A bounce that always goes the same way is boring. Letting the player aim with the paddle turns a toy into a game.
- **Keeping the speed.** With `math.hypot` we measure the speed and with `math.sqrt(speed**2 - dx**2)` we compute the vertical part, so the speed never changes by accident.
- **Edge cases are tests.** A rising ball passes through the paddle, a ball beside the paddle misses it and a ball below the paddle centre does not count as a hit. Each case has its own test.

[Previous: Step 2](Step-2) · [Next: Step 4](Step-4)
