"""@file session.py
@brief One game session: the state of the game and what the player can do.
"""

from breakout import constants
from breakout.domain.ball import Ball
from breakout.domain.brick import Brick, build_wall
from breakout.domain.paddle import Paddle
from breakout.domain.rules import (
    bounce_off_brick,
    bounce_off_paddle,
    bounce_off_walls,
    has_fallen_out,
)


class GameSession:
    """@brief The game state, driven by player commands and by ticks."""

    def __init__(
        self,
        paddle: Paddle | None = None,
        ball: Ball | None = None,
        bricks: tuple[Brick, ...] | None = None,
    ) -> None:
        """@brief Start a new game.

        @param paddle The paddle to start with (default: in the middle).
        @param ball The ball to start with (default: at the start position).
        @param bricks The wall to start with (default: the full wall).
        """
        self._paddle = paddle or Paddle()
        self._ball = ball or Ball.at_start()
        self._bricks = build_wall() if bricks is None else bricks
        self._score = 0

    @property
    def paddle(self) -> Paddle:
        """@brief The paddle."""
        return self._paddle

    @property
    def ball(self) -> Ball:
        """@brief The ball."""
        return self._ball

    @property
    def score(self) -> int:
        """@brief The points won so far."""
        return self._score

    @property
    def bricks(self) -> tuple[Brick, ...]:
        """@brief The bricks that are still standing."""
        return self._bricks

    def move_paddle(self, direction: int) -> None:
        """@brief Move the paddle one step.

        @param direction -1 for left, 1 for right.
        """
        self._paddle = self._paddle.moved_by(direction * constants.PADDLE_STEP)

    def move_paddle_to(self, x: float) -> None:
        """@brief Put the paddle at x (kept inside the window).

        @param x The wanted x of the paddle centre.
        """
        self._paddle = self._paddle.moved_to(x)

    def tick(self) -> None:
        """@brief Advance one frame: move the ball, bounce it and score."""
        ball = bounce_off_walls(self._ball.advanced())
        ball = bounce_off_paddle(ball, self._paddle)
        ball, brick = bounce_off_brick(ball, self._bricks)
        if brick is not None:
            self._bricks = tuple(b for b in self._bricks if b is not brick)
            self._score += brick.points
        self._ball = Ball.at_start() if has_fallen_out(ball) else ball
