"""@file game.py
@brief Composition root of the Turtle user interface.
"""

from breakout import constants
from breakout.application.session import GameSession
from breakout.presentation.turtle_ui.ball import Ball
from breakout.presentation.turtle_ui.bricks import Bricks
from breakout.presentation.turtle_ui.paddle import Paddle
from breakout.presentation.turtle_ui.screen import create_screen


class Game:
    """@brief The running game: the window, the views and the frame loop."""

    def __init__(self) -> None:
        """@brief Create the window, the views and the key bindings."""
        self.screen = create_screen()
        self.session = GameSession()
        self.bricks = Bricks(self.session.bricks)
        self.paddle = Paddle(self.session.paddle)
        self.ball = Ball(self.session.ball)
        self._bind_keys()

    def _bind_keys(self) -> None:
        """@brief Connect the arrow keys to the paddle."""
        self.screen.listen()
        self.screen.onkeypress(self.go_left, constants.KEY_LEFT)
        self.screen.onkeypress(self.go_right, constants.KEY_RIGHT)

    def go_left(self) -> None:
        """@brief Move the paddle one step to the left."""
        self.session.move_paddle(-1)

    def go_right(self) -> None:
        """@brief Move the paddle one step to the right."""
        self.session.move_paddle(1)

    def tick(self) -> None:
        """@brief Advance the game by one frame and redraw the window."""
        self.session.tick()
        self.bricks.render(self.session.bricks)
        self.paddle.render(self.session.paddle)
        self.ball.render(self.session.ball)
        self.screen.update()

    def run(self) -> None:
        """@brief Run the frame loop until the window is closed."""
        self._frame()
        self.screen.mainloop()

    def _frame(self) -> None:
        """@brief Play one frame and ask Tk to call this method again."""
        self.tick()
        self.screen.ontimer(self._frame, round(constants.TICK_SECONDS * 1000))
