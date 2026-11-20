"""@file brick.py
@brief The bricks of the wall.
"""

from dataclasses import dataclass

from breakout import constants
from breakout.domain.geometry import Box


@dataclass(frozen=True, slots=True)
class Brick:
    """@brief One brick: where it is, its colour and the points it is worth."""

    x: float
    y: float
    color: str
    points: int
    width: float = constants.BRICK_WIDTH
    height: float = constants.BRICK_HEIGHT

    @property
    def box(self) -> Box:
        """@brief The area the brick covers."""
        return Box(self.x, self.y, self.width, self.height)


def build_wall() -> tuple[Brick, ...]:
    """@brief Build the wall of bricks from the layout in constants.

    The rows run from the top down in the colours of BRICK_ROW_COLORS; the
    wall is centred in the window.

    @return The bricks, row by row from the top left.
    """
    columns = constants.BRICK_COLUMNS
    pitch_x = constants.BRICK_WIDTH + constants.BRICK_GAP
    pitch_y = constants.BRICK_HEIGHT + constants.BRICK_GAP
    first_x = -(columns - 1) * pitch_x / 2
    return tuple(
        Brick(
            x=first_x + column * pitch_x,
            y=constants.BRICK_TOP_ROW_Y - row * pitch_y,
            color=color,
            points=constants.BRICK_ROW_POINTS[row],
        )
        for row, color in enumerate(constants.BRICK_ROW_COLORS)
        for column in range(columns)
    )
