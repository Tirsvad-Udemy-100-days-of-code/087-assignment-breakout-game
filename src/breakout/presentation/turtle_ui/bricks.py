"""@file bricks.py
@brief The Turtle view of the wall of bricks.
"""

from turtle import Turtle

from breakout.domain.brick import Brick
from breakout.presentation.turtle_ui.shapes import make_block


class Bricks:
    """@brief One turtle per brick; a turtle is hidden when its brick is gone."""

    def __init__(self, bricks: tuple[Brick, ...]) -> None:
        """@brief Draw the wall.

        @param bricks The bricks to show.
        """
        self._turtles: dict[Brick, Turtle] = {}
        for brick in bricks:
            turtle = Turtle()
            make_block(turtle, brick.width, brick.height, brick.color)
            turtle.goto(brick.x, brick.y)
            self._turtles[brick] = turtle

    def render(self, bricks: tuple[Brick, ...]) -> None:
        """@brief Hide the turtles of the bricks that are gone, show the others.

        @param bricks The bricks that are still standing.
        """
        standing = set(bricks)
        for brick, turtle in self._turtles.items():
            if brick in standing:
                if not turtle.isvisible():
                    turtle.showturtle()
            elif turtle.isvisible():
                turtle.hideturtle()
