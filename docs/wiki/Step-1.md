# Step 1: Window and paddle

**English** · [Dansk](Step-1-da) · [Bahasa Malaysia](Step-1-ms)

![Step 1: Window and paddle](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-1.png)

## What we built

- A black 800 by 600 window made with `turtle.Screen`.
- A `Paddle` view: a blue rectangle made from the built-in square shape.
- The left and right arrow keys move the paddle in steps of 30 pixels.
- The paddle can never leave the window. This rule lives in the pure `Paddle` class of the domain layer, not in the view.

## Key code

```python
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)  # we decide when a frame is drawn

def moved_to(self, x: float) -> "Paddle":
    limit = constants.RIGHT_WALL - self.width / 2
    return replace(self, x=max(-limit, min(limit, x)))
```

The full source is in the [repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## What we gained

- **State and drawing are separate.** The domain `Paddle` is a small frozen dataclass; the Turtle view only draws it. This is why the rule can be tested without a window.
- **Manual drawing.** `screen.tracer(0)` switches automatic drawing off, so one call to `screen.update()` per frame draws everything at once and the animation does not flicker.
- **Keyboard input.** `screen.listen()` and `screen.onkeypress(...)` connect a key to a method.
- **Clamping.** `max(-limit, min(limit, x))` keeps a value inside a range, a trick used again and again in games.

[Previous: Getting Started](Getting-Started) · [Next: Step 2](Step-2)
