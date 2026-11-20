import math

import pytest

from breakout import constants
from breakout.domain.ball import Ball
from breakout.domain.brick import Brick
from breakout.domain.paddle import Paddle
from breakout.domain.rules import (
    bounce_off_brick,
    bounce_off_paddle,
    bounce_off_walls,
    has_fallen_out,
)

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


def _falling_ball(x: float, paddle: Paddle) -> Ball:
    return Ball(x=x, y=paddle.box.top, dx=2, dy=-4)


def test_ball_hitting_the_paddle_centre_goes_straight_up() -> None:
    paddle = Paddle()
    bounced = bounce_off_paddle(_falling_ball(0, paddle), paddle)
    assert bounced.dx == pytest.approx(0)
    assert bounced.dy > 0


def test_ball_hitting_the_right_edge_goes_up_and_right() -> None:
    paddle = Paddle()
    bounced = bounce_off_paddle(_falling_ball(paddle.box.right, paddle), paddle)
    assert bounced.dx > 0
    assert bounced.dy > 0


def test_ball_hitting_the_left_edge_goes_up_and_left() -> None:
    paddle = Paddle()
    bounced = bounce_off_paddle(_falling_ball(paddle.box.left, paddle), paddle)
    assert bounced.dx < 0
    assert bounced.dy > 0


def test_paddle_bounce_keeps_the_speed() -> None:
    paddle = Paddle()
    ball = _falling_ball(20, paddle)
    bounced = bounce_off_paddle(ball, paddle)
    assert math.hypot(bounced.dx, bounced.dy) == pytest.approx(
        math.hypot(ball.dx, ball.dy)
    )


def test_ball_ends_on_top_of_the_paddle_after_the_bounce() -> None:
    paddle = Paddle()
    bounced = bounce_off_paddle(_falling_ball(0, paddle), paddle)
    assert bounced.box.bottom == pytest.approx(paddle.box.top)


def test_ball_beside_the_paddle_is_a_miss() -> None:
    paddle = Paddle()
    ball = Ball(x=paddle.box.right + 50, y=paddle.box.top, dx=2, dy=-4)
    assert bounce_off_paddle(ball, paddle) == ball


def test_rising_ball_passes_through_the_paddle() -> None:
    paddle = Paddle()
    ball = Ball(x=0, y=paddle.y, dx=2, dy=4)
    assert bounce_off_paddle(ball, paddle) == ball


def test_ball_exactly_at_the_right_wall_bounces() -> None:
    ball = Ball(x=constants.RIGHT_WALL - HALF, y=0, dx=3, dy=4)
    assert bounce_off_walls(ball).dx == -3


def test_ball_exactly_at_the_left_wall_bounces() -> None:
    ball = Ball(x=constants.LEFT_WALL + HALF, y=0, dx=-3, dy=4)
    assert bounce_off_walls(ball).dx == 3


def test_ball_exactly_at_the_top_wall_bounces() -> None:
    ball = Ball(x=0, y=constants.TOP_WALL - HALF, dx=3, dy=4)
    assert bounce_off_walls(ball).dy == -4


def test_hit_beyond_the_paddle_edge_uses_the_largest_angle() -> None:
    paddle = Paddle()
    ball = Ball(x=paddle.box.right + 2, y=paddle.box.top, dx=0, dy=-5)
    bounced = bounce_off_paddle(ball, paddle)
    assert bounced.dx == pytest.approx(constants.PADDLE_BOUNCE_MAX_SIDEWAYS * 5)


def _brick() -> Brick:
    return Brick(x=0, y=100, color="red", points=7)


def test_ball_far_from_the_bricks_hits_nothing() -> None:
    ball = Ball(x=0, y=0, dx=3, dy=4)
    assert bounce_off_brick(ball, (_brick(),)) == (ball, None)


def test_ball_hitting_a_brick_from_below_goes_down() -> None:
    brick = _brick()
    ball = Ball(x=0, y=brick.box.bottom - 2, dx=3, dy=4)
    bounced, hit = bounce_off_brick(ball, (brick,))
    assert hit == brick
    assert (bounced.dx, bounced.dy) == (3, -4)


def test_ball_hitting_a_brick_from_above_goes_up() -> None:
    brick = _brick()
    ball = Ball(x=0, y=brick.box.top + 2, dx=3, dy=-4)
    bounced, hit = bounce_off_brick(ball, (brick,))
    assert hit == brick
    assert (bounced.dx, bounced.dy) == (3, 4)


def test_ball_hitting_a_brick_on_the_left_side_goes_left() -> None:
    brick = _brick()
    ball = Ball(x=brick.box.left - 2, y=brick.y, dx=3, dy=1)
    bounced, hit = bounce_off_brick(ball, (brick,))
    assert hit == brick
    assert (bounced.dx, bounced.dy) == (-3, 1)


def test_ball_hitting_a_brick_on_the_right_side_goes_right() -> None:
    brick = _brick()
    ball = Ball(x=brick.box.right + 2, y=brick.y, dx=-3, dy=1)
    bounced, hit = bounce_off_brick(ball, (brick,))
    assert hit == brick
    assert (bounced.dx, bounced.dy) == (3, 1)


def test_ball_touching_two_bricks_hits_the_one_it_reaches_into_deepest() -> None:
    left = Brick(x=-30, y=100, color="red", points=7)
    right = Brick(x=30, y=100, color="green", points=3)
    ball = Ball(x=10, y=100 - 12, dx=0, dy=4)
    _, hit = bounce_off_brick(ball, (left, right))
    assert hit == right
