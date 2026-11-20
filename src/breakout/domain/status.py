"""@file status.py
@brief Whether the game is going on or has ended.
"""

from enum import Enum


class GameStatus(Enum):
    """@brief The state of a game."""

    PLAYING = "playing"
    WON = "won"
    LOST = "lost"
