"""@file session.py
@brief One game session: the state of the game and what the player can do.
"""

from breakout import constants
from breakout.domain.ball import Ball
from breakout.domain.paddle import Paddle
from breakout.domain.rules import bounce_off_paddle, bounce_off_walls, has_fallen_out


class GameSession:
    """@brief The game state, driven by player commands and by ticks."""

    def __init__(self) -> None:
        """@brief Start a new game."""
        self.paddle = Paddle()
        self.ball = Ball.at_start()

    def move_paddle(self, direction: int) -> None:
        """@brief Move the paddle one step.

        @param direction -1 for left, 1 for right.
        """
        self.paddle = self.paddle.moved_by(direction * constants.PADDLE_STEP)

    def move_paddle_to(self, x: float) -> None:
        """@brief Put the paddle at x (kept inside the window).

        @param x The wanted x of the paddle centre.
        """
        self.paddle = self.paddle.moved_to(x)

    def tick(self) -> None:
        """@brief Advance one frame: move the ball and bounce it."""
        ball = bounce_off_walls(self.ball.advanced())
        self.ball = bounce_off_paddle(ball, self.paddle)
        if has_fallen_out(self.ball):
            self.ball = Ball.at_start()
