from breakout.domain.status import GameStatus


def test_game_status_values() -> None:
    assert [status.value for status in GameStatus] == ["playing", "won", "lost"]
