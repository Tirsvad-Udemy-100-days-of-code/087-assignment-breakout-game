from breakout import constants
from breakout.application.session import GameSession
from breakout.domain.ball import Ball
from breakout.domain.paddle import Paddle


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
