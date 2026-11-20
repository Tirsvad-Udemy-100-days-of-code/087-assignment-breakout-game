# Step 7: Speed-up and polish

**English** · [Dansk](Step-7-da) · [Bahasa Malaysia](Step-7-ms)

![Step 7: Speed-up and polish](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-7.png)

![A whole game played from start to win](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/game.gif)

## What we built

- The ball gets 10 % faster after every fourth paddle hit and the first time it hits a red brick, up to a maximum speed.
- A new ball after a missed catch starts at the normal speed.
- Two headless tests play a whole game without a window: one scripted paddle wins, one parked paddle loses.
- A test checks that the fastest ball is still slower than the smallest brick or paddle it must not skip.

## Key code

```python
BALL_SPEEDUP_EVERY = 4
BALL_SPEEDUP_FACTOR = 1.1
BALL_MAX_SPEED = 12.0
```

The full source is in the [repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## What we gained

- **A difficulty curve.** A small speed-up makes the game harder in a way the player feels. A cap keeps it fair.
- **Tunnelling.** A fast ball can jump over a thin object between two frames. We tested that the maximum speed is smaller than the smallest thing it must hit.
- **Testing without a window.** Because the rules are pure Python, a whole game runs in a fraction of a second in a test. The window itself is checked by taking screenshots in a Docker container.
- **A scripted player.** A paddle that always catches the ball in the centre makes the ball fly straight up and down forever. The test varies where the ball is caught, which is also how a real player aims.

[Previous: Step 6](Step-6) · [Next: Reflection](Reflection)
