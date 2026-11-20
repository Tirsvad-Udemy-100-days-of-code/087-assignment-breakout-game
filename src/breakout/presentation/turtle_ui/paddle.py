"""@file paddle.py
@brief The Turtle view of the paddle.
"""

from turtle import Turtle

from breakout import constants
from breakout.domain.paddle import Paddle as PaddleState
from breakout.presentation.turtle_ui.shapes import make_block


class Paddle(Turtle):
    """@brief A flat rectangle that shows where the paddle is."""

    def __init__(self, state: PaddleState) -> None:
        """@brief Create the paddle turtle.

        @param state The paddle to show.
        """
        super().__init__()
        make_block(self, state.width, state.height, constants.PADDLE_COLOR)
        self.render(state)

    def render(self, state: PaddleState) -> None:
        """@brief Move the turtle to where the paddle is.

        @param state The paddle to show.
        """
        self.goto(state.x, state.y)
