import pytest

from breakout import constants
from breakout.domain.paddle import Paddle


def test_paddle_starts_in_the_middle_near_the_bottom() -> None:
    paddle = Paddle()
    assert paddle.x == 0
    assert paddle.y == constants.PADDLE_Y


def test_paddle_moves_by_a_distance() -> None:
    assert Paddle().moved_by(30).x == 30
    assert Paddle().moved_by(-30).x == -30


def test_paddle_stops_at_the_right_wall() -> None:
    paddle = Paddle().moved_to(10_000)
    assert paddle.box.right == constants.RIGHT_WALL


def test_paddle_stops_at_the_left_wall() -> None:
    paddle = Paddle().moved_to(-10_000)
    assert paddle.box.left == constants.LEFT_WALL


def test_moving_does_not_change_the_original() -> None:
    paddle = Paddle()
    paddle.moved_by(50)
    assert paddle.x == 0


@pytest.mark.parametrize("x", [-200.0, 0.0, 123.0])
def test_paddle_inside_the_window_goes_exactly_where_asked(x: float) -> None:
    assert Paddle().moved_to(x).x == x
