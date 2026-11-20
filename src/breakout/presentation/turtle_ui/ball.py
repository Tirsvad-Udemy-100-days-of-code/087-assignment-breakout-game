"""@file ball.py
@brief The Turtle view of the ball.
"""

from turtle import Turtle

from breakout import constants
from breakout.domain.ball import Ball as BallState

## Size in pixels of the built-in Turtle "square" shape.
SQUARE_SIZE = 20


class Ball(Turtle):
    """@brief A small square that shows where the ball is."""

    def __init__(self, state: BallState) -> None:
        """@brief Create the ball turtle.

        @param state The ball to show.
        """
        super().__init__(shape="square")
        self.color(constants.BALL_COLOR)
        self.shapesize(
            stretch_wid=state.size / SQUARE_SIZE, stretch_len=state.size / SQUARE_SIZE
        )
        self.penup()
        self.render(state)

    def render(self, state: BallState) -> None:
        """@brief Move the turtle to where the ball is.

        @param state The ball to show.
        """
        self.goto(state.x, state.y)
