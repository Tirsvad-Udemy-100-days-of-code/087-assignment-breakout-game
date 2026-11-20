"""@file __main__.py
@brief Entry point: ``python -m breakout``.
"""

from breakout.presentation.turtle_ui.game import Game


def main() -> None:
    """@brief Start the game."""
    Game().run()


if __name__ == "__main__":
    main()
