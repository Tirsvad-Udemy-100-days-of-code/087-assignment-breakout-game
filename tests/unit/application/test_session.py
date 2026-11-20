import math

import pytest

from breakout import constants
from breakout.application.session import GameSession
from breakout.domain.ball import Ball
from breakout.domain.brick import Brick, build_wall
from breakout.domain.paddle import Paddle
from breakout.domain.status import GameStatus


def test_move_paddle_right_by_one_step() -> None:
    session = GameSession()
    session.move_paddle(1)
    assert session.paddle.x == constants.PADDLE_STEP


def test_move_paddle_left_by_one_step() -> None:
    session = GameSession()
    session.move_paddle(-1)
    assert session.paddle.x == -constants.PADDLE_STEP


def test_move_paddle_to_a_position() -> None:
    session = GameSession()
    session.move_paddle_to(-120)
    assert session.paddle.x == -120


def test_paddle_cannot_leave_the_window() -> None:
    session = GameSession()
    for _ in range(100):
        session.move_paddle(1)
    assert session.paddle.box.right == constants.RIGHT_WALL


def test_tick_moves_the_ball() -> None:
    session = GameSession()
    start = session.ball
    session.tick()
    assert session.ball.y == start.y + start.dy


def test_ball_that_falls_out_starts_again() -> None:
    session = GameSession(
        paddle=Paddle().moved_to(-300),
        ball=Ball(x=300, y=constants.BOTTOM_WALL - 20, dx=0, dy=-4),
    )
    session.tick()
    assert session.ball == Ball.at_start()


def test_ball_dropped_on_the_paddle_bounces_up() -> None:
    paddle = Paddle()
    session = GameSession(
        paddle=paddle, ball=Ball(x=0, y=paddle.box.top + 2, dx=0, dy=-4)
    )
    session.tick()
    assert session.ball.dy > 0


def test_paddle_moves_several_steps_at_once() -> None:
    session = GameSession()
    session.move_paddle(2)
    assert session.paddle.x == 2 * constants.PADDLE_STEP


def test_new_session_has_a_full_wall() -> None:
    session = GameSession()
    assert len(session.bricks) == len(build_wall())


def _session_with_one_brick() -> tuple[GameSession, Brick]:
    brick = Brick(x=0, y=0, color="red", points=7)
    ball = Ball(x=0, y=brick.box.bottom - 5, dx=0, dy=4)
    return GameSession(ball=ball, bricks=(brick,)), brick


def test_hitting_a_brick_removes_it() -> None:
    session, _ = _session_with_one_brick()
    session.tick()
    assert session.bricks == ()


def test_hitting_a_brick_adds_its_points() -> None:
    session, brick = _session_with_one_brick()
    session.tick()
    assert session.score == brick.points


def test_score_starts_at_zero() -> None:
    assert GameSession().score == 0


def test_new_session_starts_with_all_lives_and_is_playing() -> None:
    session = GameSession()
    assert (session.lives, session.status) == (
        constants.STARTING_LIVES,
        GameStatus.PLAYING,
    )


def _far_brick() -> Brick:
    return Brick(x=0, y=constants.TOP_WALL - 100, color="red", points=7)


def _session_about_to_miss() -> GameSession:
    return GameSession(
        paddle=Paddle().moved_to(-300),
        ball=Ball(x=300, y=constants.BOTTOM_WALL - 20, dx=0, dy=-4),
        bricks=(_far_brick(),),
    )


def _miss_again(session: GameSession) -> None:
    """Move the paddle away and tick until the lives change."""
    lives = session.lives
    session.move_paddle_to(-300)
    for _ in range(10_000):
        session.tick()
        if session.lives != lives:
            return
    raise AssertionError("the ball never fell out")


def test_a_miss_costs_one_life_and_serves_a_new_ball() -> None:
    session = _session_about_to_miss()
    session.tick()
    assert (session.lives, session.ball, session.status) == (
        constants.STARTING_LIVES - 1,
        Ball.at_start(),
        GameStatus.PLAYING,
    )


def test_third_miss_loses_the_game() -> None:
    session = _session_about_to_miss()
    session.tick()
    _miss_again(session)
    _miss_again(session)
    assert (session.lives, session.status) == (0, GameStatus.LOST)


def test_ticks_after_losing_change_nothing() -> None:
    session = _session_about_to_miss()
    session.tick()
    _miss_again(session)
    _miss_again(session)
    ball = session.ball
    session.tick()
    assert (session.ball, session.lives, session.status) == (
        ball,
        0,
        GameStatus.LOST,
    )


def test_hitting_the_last_brick_wins_the_game() -> None:
    session, _ = _session_with_one_brick()
    session.tick()
    assert session.status is GameStatus.WON


def test_ticks_after_winning_change_nothing() -> None:
    session, brick = _session_with_one_brick()
    session.tick()
    ball = session.ball
    session.tick()
    assert (session.ball, session.score, session.status) == (
        ball,
        brick.points,
        GameStatus.WON,
    )


def test_restart_restores_wall_score_lives_and_status() -> None:
    session, _ = _session_with_one_brick()
    session.tick()
    session.restart()
    assert (
        session.bricks,
        session.score,
        session.lives,
        session.status,
        session.ball,
        session.paddle,
    ) == (
        build_wall(),
        0,
        constants.STARTING_LIVES,
        GameStatus.PLAYING,
        Ball.at_start(),
        Paddle(),
    )


def _speed(session: GameSession) -> float:
    return math.hypot(session.ball.dx, session.ball.dy)


def _normal_speed() -> float:
    return math.hypot(constants.BALL_START_DX, constants.BALL_START_DY)


def _corner_brick() -> Brick:
    return Brick(x=300, y=constants.TOP_WALL - 100, color="green", points=3)


def _brick_above_the_window() -> Brick:
    """A brick the ball can never reach, so the wall is not empty."""
    return Brick(x=0, y=constants.TOP_WALL + 100, color="green", points=3)


def _session_bouncing_on_the_paddle() -> GameSession:
    """A ball that drops straight onto the centred paddle, over and over."""
    paddle = Paddle()
    ball = Ball(x=0, y=paddle.box.top + 10, dx=0, dy=-_normal_speed())
    return GameSession(paddle=paddle, ball=ball, bricks=(_brick_above_the_window(),))


def _tick_and_count_paddle_hit(session: GameSession) -> int:
    """Tick once; return 1 when the ball turned from falling to rising."""
    falling = session.ball.dy < 0
    session.tick()
    return 1 if falling and session.ball.dy > 0 else 0


def _tick_until_paddle_hit(session: GameSession) -> None:
    for _ in range(10_000):
        if _tick_and_count_paddle_hit(session):
            return
    raise AssertionError("the ball never hit the paddle")


def _hits_until_faster(session: GameSession) -> int:
    """Count paddle hits until the ball is faster than at the start."""
    hits = 0
    for _ in range(10_000):
        hits += _tick_and_count_paddle_hit(session)
        if _speed(session) > _normal_speed() + 1e-9:
            return hits
    raise AssertionError("the ball never sped up")


def test_ball_speeds_up_on_every_nth_paddle_hit() -> None:
    session = _session_bouncing_on_the_paddle()
    assert _hits_until_faster(session) == constants.BALL_SPEEDUP_EVERY


def test_ball_speed_grows_by_the_factor_on_a_paddle_hit() -> None:
    session = _session_bouncing_on_the_paddle()
    _hits_until_faster(session)
    assert _speed(session) == pytest.approx(
        _normal_speed() * constants.BALL_SPEEDUP_FACTOR
    )


def _session_below_top_bricks() -> GameSession:
    """A ball that hits a top-scoring brick, then a second one below it."""
    top = Brick(x=0, y=0, color="red", points=constants.BRICK_TOP_POINTS)
    second = Brick(x=0, y=-60, color="red", points=constants.BRICK_TOP_POINTS)
    ball = Ball(x=0, y=top.box.bottom - 5, dx=0, dy=constants.BALL_START_DY)
    return GameSession(
        paddle=Paddle().moved_to(-300),
        ball=ball,
        bricks=(top, second, _corner_brick()),
    )


def test_first_top_row_brick_speeds_the_ball_up() -> None:
    session = _session_below_top_bricks()
    session.tick()
    assert _speed(session) == pytest.approx(
        constants.BALL_START_DY * constants.BALL_SPEEDUP_FACTOR
    )


def test_second_top_row_brick_does_not_speed_the_ball_up_again() -> None:
    session = _session_below_top_bricks()
    while len(session.bricks) > 1:
        session.tick()
    assert _speed(session) == pytest.approx(
        constants.BALL_START_DY * constants.BALL_SPEEDUP_FACTOR
    )


def test_lower_row_brick_does_not_speed_the_ball_up() -> None:
    brick = Brick(x=0, y=0, color="green", points=constants.BRICK_TOP_POINTS - 1)
    ball = Ball(x=0, y=brick.box.bottom - 5, dx=0, dy=constants.BALL_START_DY)
    session = GameSession(ball=ball, bricks=(brick, _corner_brick()))
    session.tick()
    assert _speed(session) == pytest.approx(constants.BALL_START_DY)


def _session_after_a_fast_ball_missed() -> GameSession:
    """A session whose ball sped up on a top brick and then fell out."""
    top = Brick(x=0, y=0, color="red", points=constants.BRICK_TOP_POINTS)
    next_top = Brick(x=60, y=-130, color="red", points=constants.BRICK_TOP_POINTS)
    ball = Ball(x=0, y=top.box.bottom - 5, dx=0, dy=constants.BALL_START_DY)
    session = GameSession(
        paddle=Paddle().moved_to(-300),
        ball=ball,
        bricks=(top, next_top, _corner_brick()),
    )
    _miss_again(session)
    return session


def test_new_ball_after_a_miss_starts_at_the_normal_speed() -> None:
    session = _session_after_a_fast_ball_missed()
    assert session.ball == Ball.at_start()


def test_top_row_speed_up_is_available_again_after_a_miss() -> None:
    session = _session_after_a_fast_ball_missed()
    for _ in range(100):
        if len(session.bricks) < 2:
            break
        session.tick()
    assert _speed(session) == pytest.approx(
        _normal_speed() * constants.BALL_SPEEDUP_FACTOR
    )


def test_paddle_hit_count_starts_again_after_a_miss() -> None:
    session = _session_bouncing_on_the_paddle()
    for _ in range(constants.BALL_SPEEDUP_EVERY - 1):
        _tick_until_paddle_hit(session)
    session.move_paddle_to(-300)
    lives = session.lives
    while session.lives == lives:
        session.tick()
    hits = 0
    while _speed(session) <= _normal_speed() + 1e-9:
        session.move_paddle_to(session.ball.x)
        hits += _tick_and_count_paddle_hit(session)
    assert hits == constants.BALL_SPEEDUP_EVERY


def test_restart_serves_a_ball_at_the_normal_speed() -> None:
    session = _session_below_top_bricks()
    session.tick()
    session.restart()
    assert _speed(session) == pytest.approx(_normal_speed())
