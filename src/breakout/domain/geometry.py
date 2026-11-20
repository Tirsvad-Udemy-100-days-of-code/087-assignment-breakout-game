"""@file geometry.py
@brief A box centred on a point, used to test whether two things touch.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Box:
    """@brief An axis-aligned rectangle given by its centre and its size."""

    x: float
    y: float
    width: float
    height: float

    @property
    def left(self) -> float:
        """@brief The x of the left edge."""
        return self.x - self.width / 2

    @property
    def right(self) -> float:
        """@brief The x of the right edge."""
        return self.x + self.width / 2

    @property
    def top(self) -> float:
        """@brief The y of the top edge."""
        return self.y + self.height / 2

    @property
    def bottom(self) -> float:
        """@brief The y of the bottom edge."""
        return self.y - self.height / 2

    def overlaps(self, other: "Box") -> bool:
        """@brief Tell whether this box and another one share some area.

        @param other The other box.
        @return True when they overlap; boxes that only touch do not overlap.
        """
        return (
            self.left < other.right
            and self.right > other.left
            and self.bottom < other.top
            and self.top > other.bottom
        )
