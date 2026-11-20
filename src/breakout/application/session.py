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
from breakout.domain.status import GameStatus


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
        self._reset(
            paddle or Paddle(),
            ball or Ball.at_start(),
            build_wall() if bricks is None else bricks,
        )

    def _reset(self, paddle: Paddle, ball: Ball, bricks: tuple[Brick, ...]) -> None:
        """@brief Set the whole state of a new game.

        @param paddle The paddle to start with.
        @param ball The ball to start with.
        @param bricks The wall to start with.
        """
        self._paddle = paddle
        self._ball = ball
        self._bricks = bricks
        self._score = 0
        self._lives = constants.STARTING_LIVES
        self._status = GameStatus.PLAYING

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
    def lives(self) -> int:
        """@brief The lives the player has left."""
        return self._lives

    @property
    def status(self) -> GameStatus:
        """@brief Whether the game is going on, won or lost."""
        return self._status

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

    def restart(self) -> None:
        """@brief Start a new game with a full wall, all lives and no score."""
        self._reset(Paddle(), Ball.at_start(), build_wall())

    def tick(self) -> None:
        """@brief Advance one frame: move the ball, bounce it, score and judge."""
        if self._status is not GameStatus.PLAYING:
            return
        ball = bounce_off_walls(self._ball.advanced())
        ball = bounce_off_paddle(ball, self._paddle)
        ball, brick = bounce_off_brick(ball, self._bricks)
        if brick is not None:
            self._bricks = tuple(b for b in self._bricks if b is not brick)
            self._score += brick.points
        self._ball = ball
        if not self._bricks:
            self._status = GameStatus.WON
        elif has_fallen_out(ball):
            self._lose_a_life()

    def _lose_a_life(self) -> None:
        """@brief Take a life and serve a new ball, or end the game."""
        self._lives -= 1
        if self._lives == 0:
            self._status = GameStatus.LOST
        else:
            self._ball = Ball.at_start()
