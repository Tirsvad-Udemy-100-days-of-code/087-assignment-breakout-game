"""@file game.py
@brief Composition root of the Turtle user interface.
"""

from breakout import constants
from breakout.presentation.turtle_ui.screen import create_screen


class Game:
    """@brief The running game: owns the window and the frame loop."""

    def __init__(self) -> None:
        """@brief Create the window."""
        self.screen = create_screen()

    def tick(self) -> None:
        """@brief Advance the game by one frame and redraw the window."""
        self.screen.update()

    def run(self) -> None:
        """@brief Run the frame loop until the window is closed."""
        self._frame()
        self.screen.mainloop()

    def _frame(self) -> None:
        """@brief Play one frame and ask Tk to call this method again."""
        self.tick()
        self.screen.ontimer(self._frame, round(constants.TICK_SECONDS * 1000))
