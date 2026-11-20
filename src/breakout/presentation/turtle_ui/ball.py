"""@file ball.py
@brief The Turtle view of the ball.
"""

from turtle import Turtle

from breakout import constants
from breakout.domain.ball import Ball as BallState
from breakout.presentation.turtle_ui.shapes import make_block


class Ball(Turtle):
    """@brief A small square that shows where the ball is."""

    def __init__(self, state: BallState) -> None:
        """@brief Create the ball turtle.

        @param state The ball to show.
        """
        super().__init__()
        make_block(self, state.size, state.size, constants.BALL_COLOR)
        self.render(state)

    def render(self, state: BallState) -> None:
        """@brief Move the turtle to where the ball is.

        @param state The ball to show.
        """
        self.goto(state.x, state.y)
