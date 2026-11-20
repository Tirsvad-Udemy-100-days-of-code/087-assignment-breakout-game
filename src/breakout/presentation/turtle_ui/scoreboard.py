"""@file scoreboard.py
@brief The Turtle view of the score.
"""

from turtle import Turtle

from breakout import constants


class Scoreboard(Turtle):
    """@brief Writes the score at the top of the window."""

    def __init__(self) -> None:
        """@brief Create the scoreboard; it writes on the first render."""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(constants.TEXT_COLOR)
        self._shown: str | None = None

    def render(self, score: int) -> None:
        """@brief Write the score, only when it has changed.

        @param score The points won so far.
        """
        text = f"Score: {score}"
        if text == self._shown:
            return
        self._shown = text
        self.clear()
        self.goto(constants.SCORE_X, constants.SCORE_Y)
        self.write(text, align="center", font=constants.FONT)
