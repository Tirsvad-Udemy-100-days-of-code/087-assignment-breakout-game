from breakout import constants
from breakout.application.session import GameSession


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
    session = GameSession()
    for _ in range(300):
        session.tick()
    assert constants.BOTTOM_WALL <= session.ball.y <= constants.TOP_WALL
