from itertools import combinations

from breakout import constants
from breakout.domain.brick import build_wall


def test_wall_has_every_row_and_column() -> None:
    wall = build_wall()
    assert len(wall) == len(constants.BRICK_ROW_COLORS) * constants.BRICK_COLUMNS


def test_wall_rows_have_their_colour_and_points() -> None:
    wall = build_wall()
    columns = constants.BRICK_COLUMNS
    for row, color in enumerate(constants.BRICK_ROW_COLORS):
        bricks = wall[row * columns : (row + 1) * columns]
        assert {brick.color for brick in bricks} == {color}
        assert {brick.points for brick in bricks} == {constants.BRICK_ROW_POINTS[row]}


def test_top_row_is_at_the_configured_height() -> None:
    assert build_wall()[0].y == constants.BRICK_TOP_ROW_Y


def test_wall_is_centred_and_inside_the_window() -> None:
    boxes = [brick.box for brick in build_wall()]
    assert min(box.left for box in boxes) == -max(box.right for box in boxes)
    assert min(box.left for box in boxes) >= constants.LEFT_WALL


def test_no_two_bricks_overlap() -> None:
    boxes = [brick.box for brick in build_wall()]
    assert not any(a.overlaps(b) for a, b in combinations(boxes, 2))


def test_rows_are_separated_by_a_gap() -> None:
    wall = build_wall()
    columns = constants.BRICK_COLUMNS
    step = wall[0].y - wall[columns].y
    assert step == constants.BRICK_HEIGHT + constants.BRICK_GAP
