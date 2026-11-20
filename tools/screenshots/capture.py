"""@file capture.py
@brief Run one development step of the game on a virtual display and save a PNG.

Runs inside the container of tools/screenshots/Dockerfile, never on the host
desktop. The source tree of the step is on PYTHONPATH.

Usage: python capture.py <step 0-7> <output.png>
"""

import subprocess
import sys
import tkinter

from breakout import constants
from breakout.presentation.turtle_ui.game import Game

## Where the paddle stands in the picture of step 1.
STEP_1_PADDLE_X = -150

## Frames to play before the picture is taken, per step (0 is the empty window).
FRAMES_BY_STEP = {0: 0, 1: 0, 2: 70, 3: 270, 4: 20, 5: 400, 6: 2600, 7: 900}


def autopilot(game: Game) -> None:
    """@brief Move the paddle under the ball, when the step has a ball."""
    session = game.session
    if hasattr(session, "ball"):
        session.move_paddle_to(session.ball.x)


def prepare(game: Game, step: int) -> None:
    """@brief Put the game in a state that shows the step well."""
    if step == 1:
        game.session.move_paddle_to(STEP_1_PADDLE_X)


def save_png(game: Game, path: str) -> None:
    """@brief Save the game window as a PNG with ImageMagick."""
    canvas = game.screen.getcanvas()
    canvas.update()
    root = canvas.winfo_toplevel()
    x, y = root.winfo_rootx(), root.winfo_rooty()
    width, height = constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT
    geometry = f"{width}x{height}+{x}+{y}"
    subprocess.run(
        ["import", "-window", "root", "-crop", geometry, "+repage", path],
        check=True,
    )


def main() -> None:
    """@brief Play the frames of the step and save the picture."""
    step, path = int(sys.argv[1]), sys.argv[2]
    game = Game()
    prepare(game, step)
    try:
        for _ in range(FRAMES_BY_STEP[step]):
            autopilot(game)
            game.tick()
        game.tick()
        save_png(game, path)
    except tkinter.TclError as error:
        raise SystemExit(f"window closed early: {error}") from error


if __name__ == "__main__":
    main()
