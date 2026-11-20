# Step 2: Ball and wall bounce

**English** · [Dansk](Step-2-da) · [Bahasa Malaysia](Step-2-ms)

![Step 2: Ball and wall bounce](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-2.png)

## What we built

- A white square ball that moves a little every frame.
- The ball bounces off the left, right and top walls.
- A ball that falls out of the bottom starts again from the start position.
- The frame loop uses `screen.ontimer(...)` and `mainloop()` instead of `time.sleep()`, so the window stays responsive and can be closed at any time.

## Key code

```python
def advanced(self) -> "Ball":
    return replace(self, x=self.x + self.dx, y=self.y + self.dy)

if x - half <= constants.LEFT_WALL:
    x, dx = constants.LEFT_WALL + half, abs(dx)
```

The full source is in the [repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## What we gained

- **The game loop.** Every frame the game moves things, checks the rules and draws. Everything in the game is built on this rhythm.
- **Speed as a vector.** `dx` and `dy` are pixels per frame. A bounce only reverses the component that hit the wall.
- **No sticking.** After a bounce the ball is placed back inside the wall, so it cannot be caught in the wall for several frames.
- **Immutable values.** `advanced()` returns a new `Ball` instead of changing the old one. Functions that return new values are easy to test.

[Previous: Step 1](Step-1) · [Next: Step 3](Step-3)
