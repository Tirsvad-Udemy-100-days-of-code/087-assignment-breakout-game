from breakout import constants
from breakout.domain.ball import Ball


def test_ball_starts_at_the_start_position_flying_up() -> None:
    ball = Ball.at_start()
    assert (ball.x, ball.y) == (constants.BALL_START_X, constants.BALL_START_Y)
    assert ball.dy > 0


def test_advanced_moves_the_ball_by_its_speed() -> None:
    ball = Ball(x=0, y=0, dx=3, dy=4).advanced()
    assert (ball.x, ball.y) == (3, 4)


def test_ball_box_is_centred_on_the_ball() -> None:
    box = Ball(x=10, y=20, dx=0, dy=0, size=14).box
    assert (box.x, box.y, box.width, box.height) == (10, 20, 14, 14)
