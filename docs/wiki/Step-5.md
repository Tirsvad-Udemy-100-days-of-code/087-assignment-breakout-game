# Step 5: Brick collision and score

**English** · [Dansk](Step-5-da) · [Bahasa Malaysia](Step-5-ms)

![Step 5: Brick collision and score](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/raw/branch/main/docs/images/step-5.png)

## What we built

- When the ball touches a brick, the brick disappears and the score grows by the points of its row.
- The ball reflects on the correct axis: a hit on the side of a brick reverses `dx`, a hit from below or above reverses `dy`.
- A `Scoreboard` writes the score at the top, and only when it changes.

## Key code

```python
depth_x, depth_y = _overlap_depth(ball.box, brick.box)
if depth_x < depth_y:  # the ball hit the side of the brick
    dx = -abs(ball.dx) if ball.x < brick.x else abs(ball.dx)
    return replace(ball, dx=dx), brick
dy = -abs(ball.dy) if ball.y < brick.y else abs(ball.dy)
return replace(ball, dy=dy), brick
```

The full source is in the [repository](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game).

## What we gained

- **Box overlap.** Two rectangles touch when they overlap on both axes. That one test is the heart of almost every simple 2D game.
- **Which side was hit?** We compare how deep the ball reaches into the brick on each axis. The smaller depth is the side it came from. This is more reliable than looking at the direction of the ball.
- **One brick per frame.** If the ball touches two bricks, the one it reaches into deepest is hit, so a single frame never breaks two bricks.
- **Cheap drawing.** The scoreboard clears and writes only when the text changes. Drawing text every frame would slow the game down.

[Previous: Step 4](Step-4) · [Next: Step 6](Step-6)
