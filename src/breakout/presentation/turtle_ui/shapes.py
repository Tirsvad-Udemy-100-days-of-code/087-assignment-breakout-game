"""@file shapes.py
@brief Helpers shared by the Turtle views.
"""

from turtle import Turtle

## Size in pixels of the built-in Turtle "square" shape.
SQUARE_SIZE = 20


def make_block(turtle: Turtle, width: float, height: float, color: str) -> None:
    """@brief Turn a turtle into a coloured rectangle that does not draw lines.

    @param turtle The turtle to change.
    @param width Width in pixels.
    @param height Height in pixels.
    @param color Fill colour.
    """
    turtle.shape("square")
    turtle.color(color)
    turtle.shapesize(stretch_wid=height / SQUARE_SIZE, stretch_len=width / SQUARE_SIZE)
    turtle.penup()
