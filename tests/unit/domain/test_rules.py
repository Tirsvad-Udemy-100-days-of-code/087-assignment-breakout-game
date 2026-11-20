from breakout import constants
from breakout.domain.ball import Ball
from breakout.domain.rules import bounce_off_walls, has_fallen_out

HALF = constants.BALL_SIZE / 2


def test_ball_in_the_middle_keeps_flying() -> None:
    ball = Ball(x=0, y=0, dx=3, dy=4)
    assert bounce_off_walls(ball) == ball


def test_ball_bounces_off_the_right_wall() -> None:
    ball = Ball(x=constants.RIGHT_WALL - HALF + 1, y=0, dx=3, dy=4)
    bounced = bounce_off_walls(ball)
    assert bounced.dx == -3
    assert bounced.dy == 4
    assert bounced.x + HALF <= constants.RIGHT_WALL


def test_ball_bounces_off_the_left_wall() -> None:
    ball = Ball(x=constants.LEFT_WALL + HALF - 1, y=0, dx=-3, dy=4)
    bounced = bounce_off_walls(ball)
    assert bounced.dx == 3
    assert bounced.x - HALF >= constants.LEFT_WALL


def test_ball_bounces_off_the_top_wall() -> None:
    ball = Ball(x=0, y=constants.TOP_WALL - HALF + 1, dx=3, dy=4)
    bounced = bounce_off_walls(ball)
    assert bounced.dy == -4
    assert bounced.dx == 3
    assert bounced.y + HALF <= constants.TOP_WALL


def test_ball_already_leaving_the_wall_is_not_flipped_again() -> None:
    ball = Ball(x=constants.RIGHT_WALL - HALF + 1, y=0, dx=-3, dy=4)
    assert bounce_off_walls(ball).dx == -3


def test_ball_passes_through_the_open_bottom() -> None:
    ball = Ball(x=0, y=constants.BOTTOM_WALL + 1, dx=3, dy=-4)
    assert bounce_off_walls(ball).dy == -4


def test_ball_has_fallen_out_when_it_is_below_the_window() -> None:
    assert has_fallen_out(Ball(x=0, y=constants.BOTTOM_WALL - HALF - 1, dx=0, dy=-4))


def test_ball_has_not_fallen_out_while_it_is_visible() -> None:
    assert not has_fallen_out(Ball(x=0, y=constants.BOTTOM_WALL, dx=0, dy=-4))
