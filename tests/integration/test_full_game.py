"""Headless full games: the real session, no window and no Turtle."""

from breakout import constants
from breakout.application.session import GameSession
from breakout.domain.status import GameStatus

MAX_TICKS = 200_000
TICKS_PER_CATCH_OFFSET = 150
## Where on the paddle the ball is caught, as a share of the half paddle width.
CATCH_OFFSETS = (-0.7, 0.3, -0.3, 0.7)


def _catch_offset(tick: int) -> float:
    return CATCH_OFFSETS[(tick // TICKS_PER_CATCH_OFFSET) % len(CATCH_OFFSETS)]


def _place_paddle_under_the_ball(session: GameSession, tick: int) -> None:
    """Put the paddle so the falling ball lands at the current catch offset."""
    half_width = session.paddle.width / 2
    session.move_paddle_to(session.ball.x - _catch_offset(tick) * half_width)


def _play_to_the_end(session: GameSession) -> int:
    """Tick with a perfect paddle until the game ends; return the ticks used."""
    for tick in range(MAX_TICKS):
        if session.status is not GameStatus.PLAYING:
            return tick
        _place_paddle_under_the_ball(session, tick)
        session.tick()
    raise AssertionError(f"the game did not end within {MAX_TICKS} ticks")


def test_perfect_paddle_clears_the_wall_and_wins() -> None:
    session = GameSession()
    _play_to_the_end(session)
    assert (session.status, session.bricks, session.lives) == (
        GameStatus.WON,
        (),
        constants.STARTING_LIVES,
    )


def test_paddle_parked_in_a_corner_loses_all_lives() -> None:
    session = GameSession()
    session.move_paddle_to(constants.LEFT_WALL)
    for _ in range(MAX_TICKS):
        if session.status is not GameStatus.PLAYING:
            break
        session.tick()
    assert (session.status, session.lives) == (GameStatus.LOST, 0)
