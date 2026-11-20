# Step 4: Wall of bricks

**English** · [Dansk](Step-4-da) · [Bahasa Malaysia](Step-4-ms)

![Step 4: Wall of bricks](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-4.png)

## What we built

- Six rows of 14 bricks: two red, one orange, two green and one yellow.
- Each brick is worth points by colour (7, 7, 5, 3, 3, 1).
- The wall is centred in the window and every size comes from `constants.py`.
- The `Bricks` view makes one turtle per brick and hides the turtle when its brick is gone.

## Key code

```python
first_x = -(columns - 1) * pitch_x / 2
Brick(
    x=first_x + column * pitch_x,
    y=constants.BRICK_TOP_ROW_Y - row * pitch_y,
    color=color,
    points=constants.BRICK_ROW_POINTS[row],
)
```

The full source is in the [repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## What we gained

- **Data-driven layout.** `build_wall()` makes the wall from a few constants. To change the number of rows, the colours or the points we change one file, not the code.
- **Centring with arithmetic.** The first column starts at `-(columns - 1) * pitch / 2`, so the wall is symmetric whatever the number of columns.
- **One place for constants.** A rule that no number is written twice (not even `20`, the size of the Turtle square) keeps the code easy to change.

[Previous: Step 3](Step-3) · [Next: Step 5](Step-5)
