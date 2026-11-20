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
