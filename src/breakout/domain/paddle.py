"""@file paddle.py
@brief The paddle the player moves along the bottom of the window.
"""

from dataclasses import dataclass, replace

from breakout import constants
from breakout.domain.geometry import Box


@dataclass(frozen=True, slots=True)
class Paddle:
    """@brief The paddle: it moves sideways and never leaves the window."""

    x: float = 0.0
    y: float = constants.PADDLE_Y
    width: float = constants.PADDLE_WIDTH
    height: float = constants.PADDLE_HEIGHT

    @property
    def box(self) -> Box:
        """@brief The area the paddle covers."""
        return Box(self.x, self.y, self.width, self.height)

    def moved_to(self, x: float) -> "Paddle":
        """@brief Put the paddle at x, kept inside the side walls.

        @param x The wanted x of the paddle centre.
        @return A new paddle.
        """
        limit = constants.RIGHT_WALL - self.width / 2
        return replace(self, x=max(-limit, min(limit, x)))

    def moved_by(self, dx: float) -> "Paddle":
        """@brief Move the paddle sideways, kept inside the side walls.

        @param dx Distance in pixels, negative to the left.
        @return A new paddle.
        """
        return self.moved_to(self.x + dx)
