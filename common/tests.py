from . import OrthogonalPolygon
from pytest import fixture


@fixture
def square():
    return OrthogonalPolygon(coords=(
        (0, 0),
        (0, 4),
        (4, 4),
        (4, 0),
    ))


@fixture
def square_with_notch():
    return OrthogonalPolygon(coords=(
        (0, 0),
        (0, 8),
        (2, 8),
        (2, 4),
        (4, 4),
        (4, 8),
        (8, 8),
        (8, 0),
    ))


def test_orthogonal_polygon_notch_line_inside(square_with_notch):
    assert square_with_notch.line_is_inside_polygon((0, 3), (8, 3)) is True
    assert square_with_notch.line_is_inside_polygon((1, 0), (1, 8)) is True


def test_orthogonal_polygon_notch_inside_even_if_overlaps_with_line(square_with_notch):
    assert square_with_notch.line_is_inside_polygon((0, 4), (8, 4)) is True
    assert square_with_notch.line_is_inside_polygon((2, 0), (2, 8)) is True
    assert square_with_notch.line_is_inside_polygon((2, 4), (4, 4)) is True
    assert square_with_notch.line_is_inside_polygon((2, 4), (2, 8)) is True


def test_orthogonal_polygon_notch_inside_when_overlapping_and_defining_square(square_with_notch):
    assert square_with_notch.line_is_inside_polygon((4, 8), (4, 0)) is True
    assert square_with_notch.line_is_inside_polygon((4, 0), (8, 0)) is True
    assert square_with_notch.line_is_inside_polygon((8, 0), (8, 8)) is True
    assert square_with_notch.line_is_inside_polygon((8, 8), (4, 8)) is True


def test_orthogonal_polygon_notch_crosses_segments(square_with_notch):
    assert square_with_notch.line_is_inside_polygon((1, 5), (5, 5)) is False


def test_orthogonal_polygon_notch_ends_up_outside_in_notch_(square_with_notch):
    assert square_with_notch.line_is_inside_polygon((1, 5), (3, 5)) is False


def test_orthogonal_polygon_simple_inside_tests(square):
    assert square.line_is_inside_polygon((1, 1), (3, 1)) is True
    assert square.line_is_inside_polygon((1, 1), (1, 3)) is True
    assert square.line_is_inside_polygon((0, 2), (4, 2)) is True


def test_orthogonal_polygon_simple_overlap_tests(square):
    assert square.line_is_inside_polygon((0, 0), (0, 2)) is True
    assert square.line_is_inside_polygon((0, 0), (0, 4)) is True
    assert square.line_is_inside_polygon((0, 4), (4, 4)) is True
    assert square.line_is_inside_polygon((0, 0), (4, 0)) is True


def test_orthogonal_polygon_overlaps_from_outside(square):
    assert square.line_is_inside_polygon((0, 0), (0, 6)) is False
    assert square.line_is_inside_polygon((0, -4), (0, 4)) is False
    assert square.line_is_inside_polygon((0, 6), (0, 8)) is False
    assert square.line_is_inside_polygon((6, 0), (8, 0)) is False


def test_orthogonal_polygon_line_starts_inside_goes_outside(square):
    assert square.line_is_inside_polygon((2, 2), (6, 2)) is False
    assert square.line_is_inside_polygon((2, 2), (2, 6)) is False
