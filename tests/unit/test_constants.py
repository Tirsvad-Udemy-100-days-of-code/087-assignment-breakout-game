from breakout import constants


def test_walls_match_window_size() -> None:
    assert constants.RIGHT_WALL - constants.LEFT_WALL == constants.WINDOW_WIDTH
    assert constants.TOP_WALL - constants.BOTTOM_WALL == constants.WINDOW_HEIGHT


def test_brick_wall_fits_in_window() -> None:
    columns = constants.BRICK_COLUMNS
    width = columns * constants.BRICK_WIDTH + (columns - 1) * constants.BRICK_GAP
    assert width <= constants.WINDOW_WIDTH


def test_ball_max_speed_is_smaller_than_the_smallest_overlap_window() -> None:
    window = min(constants.BRICK_HEIGHT, constants.PADDLE_HEIGHT) + constants.BALL_SIZE
    assert constants.BALL_MAX_SPEED < window


def test_every_brick_row_has_points() -> None:
    assert len(constants.BRICK_ROW_COLORS) == len(constants.BRICK_ROW_POINTS)
