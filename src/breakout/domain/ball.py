"""@file ball.py
@brief The ball that flies around the window.
"""

from dataclasses import dataclass, replace

from breakout import constants
from breakout.domain.geometry import Box


@dataclass(frozen=True, slots=True)
class Ball:
    """@brief The ball: a position and a speed in pixels per tick."""

    x: float
    y: float
    dx: float
    dy: float
    size: float = constants.BALL_SIZE

    @classmethod
    def at_start(cls) -> "Ball":
        """@brief Make a ball at the start position, flying up and to the right."""
        return cls(
            x=constants.BALL_START_X,
            y=constants.BALL_START_Y,
            dx=constants.BALL_START_DX,
            dy=constants.BALL_START_DY,
        )

    @property
    def box(self) -> Box:
        """@brief The area the ball covers."""
        return Box(self.x, self.y, self.size, self.size)

    def advanced(self) -> "Ball":
        """@brief Move the ball one tick along its speed.

        @return A new ball.
        """
        return replace(self, x=self.x + self.dx, y=self.y + self.dy)
