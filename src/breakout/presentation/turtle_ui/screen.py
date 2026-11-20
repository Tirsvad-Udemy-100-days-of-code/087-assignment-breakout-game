"""@file screen.py
@brief Creates the Turtle window.
"""

import turtle

from breakout import constants


def create_screen() -> turtle._Screen:
    """@brief Create the black game window.

    @return The Turtle screen, with automatic redraw switched off so the game
            loop decides when to draw a frame.
    """
    screen = turtle.Screen()
    screen.setup(width=constants.WINDOW_WIDTH, height=constants.WINDOW_HEIGHT)
    screen.bgcolor(constants.BACKGROUND_COLOR)
    screen.title(constants.WINDOW_TITLE)
    screen.tracer(0)
    return screen
