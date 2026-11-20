"""@file scoreboard.py
@brief The Turtle view of the score, the lives and the end message.
"""

from turtle import Turtle

from breakout import constants
from breakout.domain.status import GameStatus

_MESSAGES = {
    GameStatus.WON: constants.WIN_MESSAGE,
    GameStatus.LOST: constants.LOSE_MESSAGE,
}


class Scoreboard(Turtle):
    """@brief Writes the score and the lives at the top of the window."""

    def __init__(self) -> None:
        """@brief Create the scoreboard; it writes on the first render."""
        super().__init__()
        self.penup()
        self.color(constants.TEXT_COLOR)
        self.hideturtle()
        self._shown: tuple[int, int, GameStatus] | None = None

    def render(self, score: int, lives: int, status: GameStatus) -> None:
        """@brief Write the texts, only when something has changed.

        @param score The points won so far.
        @param lives The lives the player has left.
        @param status Whether the game is going on, won or lost.
        """
        state = (score, lives, status)
        if state == self._shown:
            return
        self._shown = state
        self.clear()
        self._write_at(constants.SCORE_X, constants.SCORE_Y, f"Score: {score}")
        self._write_at(constants.LIVES_X, constants.SCORE_Y, f"Lives: {lives}")
        message = _MESSAGES.get(status)
        if message is not None:
            self._write_at(0, constants.MESSAGE_Y, message, constants.MESSAGE_FONT)
        self.hideturtle()

    def _write_at(
        self,
        x: float,
        y: float,
        text: str,
        font: tuple[str, int, str] = constants.FONT,
    ) -> None:
        """@brief Write one centred text.

        @param x The x of the text centre.
        @param y The y of the text.
        @param text The text to write.
        @param font The font to write it in.
        """
        self.goto(x, y)
        self.write(text, align="center", font=font)
