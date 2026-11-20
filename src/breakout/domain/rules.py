"""@file rules.py
@brief Pure rules of the game: bounces and misses.
"""

import math
from dataclasses import replace

from breakout import constants
from breakout.domain.ball import Ball
from breakout.domain.brick import Brick
from breakout.domain.geometry import Box
from breakout.domain.paddle import Paddle


def bounce_off_walls(ball: Ball) -> Ball:
    """@brief Bounce the ball off the left, right and top walls.

    The ball keeps its speed; only the direction that hit the wall is reversed.
    The bottom is open: a ball that passes it is a miss (see has_fallen_out).

    @param ball The ball after it has moved.
    @return A ball that is inside the walls and flies away from them.
    """
    half = ball.size / 2
    x, y, dx, dy = ball.x, ball.y, ball.dx, ball.dy
    if x - half <= constants.LEFT_WALL:
        x, dx = constants.LEFT_WALL + half, abs(dx)
    elif x + half >= constants.RIGHT_WALL:
        x, dx = constants.RIGHT_WALL - half, -abs(dx)
    if y + half >= constants.TOP_WALL:
        y, dy = constants.TOP_WALL - half, -abs(dy)
    return replace(ball, x=x, y=y, dx=dx, dy=dy)


def has_fallen_out(ball: Ball) -> bool:
    """@brief Tell whether the ball has passed the bottom of the window.

    @param ball The ball.
    @return True when the whole ball is below the bottom wall.
    """
    return ball.box.top < constants.BOTTOM_WALL


def bounce_off_paddle(ball: Ball, paddle: Paddle) -> Ball:
    """@brief Bounce a falling ball off the paddle.

    The ball keeps its speed. Where it hits decides the angle: the centre sends
    it straight up, the edges send it sideways (at most
    PADDLE_BOUNCE_MAX_SIDEWAYS of the speed).

    @param ball The ball after it has moved.
    @param paddle The paddle.
    @return The bounced ball, or the same ball when it does not hit the paddle.
    """
    if ball.dy >= 0 or not ball.box.overlaps(paddle.box):
        return ball
    offset = max(-1.0, min(1.0, (ball.x - paddle.x) / (paddle.width / 2)))
    speed = math.hypot(ball.dx, ball.dy)
    dx = offset * constants.PADDLE_BOUNCE_MAX_SIDEWAYS * speed
    dy = math.sqrt(speed**2 - dx**2)
    return replace(ball, y=paddle.box.top + ball.size / 2, dx=dx, dy=dy)


def _overlap_depth(a: Box, b: Box) -> tuple[float, float]:
    """@brief How far two overlapping boxes reach into each other.

    @return The overlap along x and along y.
    """
    depth_x = min(a.right, b.right) - max(a.left, b.left)
    depth_y = min(a.top, b.top) - max(a.bottom, b.bottom)
    return depth_x, depth_y


def bounce_off_brick(
    ball: Ball, bricks: tuple[Brick, ...]
) -> tuple[Ball, Brick | None]:
    """@brief Bounce the ball off the brick it hits, if any.

    When the ball touches several bricks at once, the one it reaches into
    deepest is hit. The ball is reflected on the axis where it reaches into the
    brick the least: a hit on the side reverses dx, a hit from below or above
    reverses dy.

    @param ball The ball after it has moved.
    @param bricks The bricks that are still standing.
    @return The ball (bounced when a brick was hit) and the brick that was hit,
            or the same ball and None.
    """
    touched = [brick for brick in bricks if ball.box.overlaps(brick.box)]
    if not touched:
        return ball, None

    def depth(brick: Brick) -> float:
        depth_x, depth_y = _overlap_depth(ball.box, brick.box)
        return depth_x * depth_y

    brick = max(touched, key=depth)
    depth_x, depth_y = _overlap_depth(ball.box, brick.box)
    if depth_x < depth_y:
        dx = -abs(ball.dx) if ball.x < brick.x else abs(ball.dx)
        return replace(ball, dx=dx), brick
    dy = -abs(ball.dy) if ball.y < brick.y else abs(ball.dy)
    return replace(ball, dy=dy), brick
