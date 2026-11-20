"""@file constants.py
@brief Every constant of the Breakout game, in one place.

Coordinates follow Turtle: the origin is the centre of the window, x grows to the
right and y grows upwards. Lengths are in pixels, speeds in pixels per tick.
"""

from typing import Final

## @name Window
## @{
WINDOW_WIDTH: Final[int] = 800
WINDOW_HEIGHT: Final[int] = 600
WINDOW_TITLE: Final[str] = "Breakout"
BACKGROUND_COLOR: Final[str] = "black"
LEFT_WALL: Final[float] = -WINDOW_WIDTH / 2
RIGHT_WALL: Final[float] = WINDOW_WIDTH / 2
TOP_WALL: Final[float] = WINDOW_HEIGHT / 2
BOTTOM_WALL: Final[float] = -WINDOW_HEIGHT / 2
## @}

## @name Timing
## @{
FRAMES_PER_SECOND: Final[int] = 60
TICK_SECONDS: Final[float] = 1 / FRAMES_PER_SECOND
## @}

## @name Paddle
## @{
PADDLE_WIDTH: Final[float] = 100.0
PADDLE_HEIGHT: Final[float] = 16.0
PADDLE_Y: Final[float] = -260.0
PADDLE_STEP: Final[float] = 30.0
PADDLE_COLOR: Final[str] = "deepskyblue"
## @}

## @name Ball
## @{
BALL_SIZE: Final[float] = 14.0
BALL_START_X: Final[float] = 0.0
BALL_START_Y: Final[float] = -230.0
BALL_START_DX: Final[float] = 3.0
BALL_START_DY: Final[float] = 4.0
BALL_COLOR: Final[str] = "white"
## Share of the ball speed that goes sideways when the ball hits the paddle edge.
PADDLE_BOUNCE_MAX_SIDEWAYS: Final[float] = 0.8
## Speed-up: every BALL_SPEEDUP_EVERY paddle hits the speed grows by this factor.
BALL_SPEEDUP_EVERY: Final[int] = 4
BALL_SPEEDUP_FACTOR: Final[float] = 1.1
BALL_MAX_SPEED: Final[float] = 12.0
## Below this difference (px) of the two overlap depths a brick hit is a corner hit.
BRICK_CORNER_TOLERANCE: Final[float] = 1.0
## @}

## @name Bricks
## @{
BRICK_COLUMNS: Final[int] = 14
BRICK_WIDTH: Final[float] = 52.0
BRICK_HEIGHT: Final[float] = 20.0
BRICK_GAP: Final[float] = 4.0
BRICK_TOP_ROW_Y: Final[float] = 190.0
## One entry per row from the top: red, red, orange, green, green, yellow.
BRICK_ROW_COLORS: Final[tuple[str, ...]] = (
    "red",
    "red",
    "orange",
    "green",
    "green",
    "yellow",
)
## Points per row, same order as BRICK_ROW_COLORS.
BRICK_ROW_POINTS: Final[tuple[int, ...]] = (7, 7, 5, 3, 3, 1)
## Points of the top-scoring rows; the first hit on one speeds the ball up.
BRICK_TOP_POINTS: Final[int] = max(BRICK_ROW_POINTS)
## @}

## @name Game
## @{
STARTING_LIVES: Final[int] = 3
KEY_LEFT: Final[str] = "Left"
KEY_RIGHT: Final[str] = "Right"
KEY_RESTART: Final[str] = "space"
## @}

## @name Scoreboard
## @{
SCORE_X: Final[float] = -300.0
LIVES_X: Final[float] = 300.0
SCORE_Y: Final[float] = 250.0
TEXT_COLOR: Final[str] = "white"
FONT: Final[tuple[str, int, str]] = ("Courier", 24, "bold")
MESSAGE_FONT: Final[tuple[str, int, str]] = ("Courier", 36, "bold")
MESSAGE_Y: Final[float] = -60.0
WIN_MESSAGE: Final[str] = "YOU WIN!  Press space"
LOSE_MESSAGE: Final[str] = "GAME OVER  Press space"
## @}
