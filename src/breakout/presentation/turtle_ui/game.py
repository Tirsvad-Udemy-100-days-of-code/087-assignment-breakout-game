"""@file game.py
@brief Composition root of the Turtle user interface.
"""

import time
import tkinter
import turtle

from breakout import constants
from breakout.presentation.turtle_ui.screen import create_screen


class Game:
    """@brief The running game: owns the window and the frame loop."""

    def __init__(self) -> None:
        """@brief Create the window."""
        self.screen = create_screen()
        self.is_running = True

    def tick(self) -> None:
        """@brief Advance the game by one frame and redraw the window."""
        self.screen.update()

    def run(self) -> None:
        """@brief Run the frame loop until the window is closed."""
        try:
            while self.is_running:
                self.tick()
                time.sleep(constants.TICK_SECONDS)
        except (turtle.Terminator, tkinter.TclError):
            # The player closed the window.
            self.is_running = False
