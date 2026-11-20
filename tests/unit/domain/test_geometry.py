from breakout.domain.geometry import Box


def test_box_edges() -> None:
    box = Box(x=10, y=20, width=4, height=6)
    assert (box.left, box.right, box.bottom, box.top) == (8, 12, 17, 23)


def test_boxes_that_share_area_overlap() -> None:
    assert Box(0, 0, 10, 10).overlaps(Box(5, 5, 10, 10))


def test_boxes_that_only_touch_do_not_overlap() -> None:
    assert not Box(0, 0, 10, 10).overlaps(Box(10, 0, 10, 10))


def test_far_boxes_do_not_overlap() -> None:
    assert not Box(0, 0, 10, 10).overlaps(Box(100, 100, 10, 10))
