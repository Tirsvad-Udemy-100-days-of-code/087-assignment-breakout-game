"""@file paddle.py
@brief The Turtle view of the paddle.
"""

from turtle import Turtle

from breakout import constants
from breakout.domain.paddle import Paddle as PaddleState

## Size in pixels of the built-in Turtle "square" shape.
SQUARE_SIZE = 20


class Paddle(Turtle):
    """@brief A flat rectangle that shows where the paddle is."""

    def __init__(self, state: PaddleState) -> None:
        """@brief Create the paddle turtle.

        @param state The paddle to show.
        """
        super().__init__(shape="square")
        self.color(constants.PADDLE_COLOR)
        self.shapesize(
            stretch_wid=state.height / SQUARE_SIZE,
            stretch_len=state.width / SQUARE_SIZE,
        )
        self.penup()
        self.render(state)

    def render(self, state: PaddleState) -> None:
        """@brief Move the turtle to where the paddle is.

        @param state The paddle to show.
        """
        self.goto(state.x, state.y)
