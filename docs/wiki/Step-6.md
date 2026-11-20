# Step 6: Lives, game over and win

**English** · [Dansk](Step-6-da) · [Bahasa Malaysia](Step-6-ms)

![Step 6: Lives, game over and win](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-6.png)

## What we built

- The player has three lives. A ball that falls out of the bottom costs one life and serves a new ball.
- With no lives left the game shows `GAME OVER`; when the last brick is gone it shows `YOU WIN!`.
- The `space` key starts a new game.
- The scoreboard shows the score on the left and the lives on the right.

## Key code

```python
class GameStatus(Enum):
    PLAYING = "playing"
    WON = "won"
    LOST = "lost"
```

The full source is in the [repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## What we gained

- **A state machine.** `GameStatus` has three values: playing, won and lost. `tick()` does nothing unless the game is being played, so a finished game cannot change by accident.
- **One way to start.** The start of a game and a restart use the same `_reset` method, so there is no way to forget to reset something.
- **Messages from state.** The scoreboard is drawn from `(score, lives, status)`. When the state changes, the picture follows, with no extra bookkeeping.

[Previous: Step 5](Step-5) · [Next: Step 7](Step-7)
