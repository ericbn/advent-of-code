from year2022.day2 import points_a, points_b, Shape

import pytest

@pytest.mark.parametrize(
    ("opponent", "me", "expected"),
    [
        pytest.param(Shape.A, Shape.Y, 8),
        pytest.param(Shape.B, Shape.X, 1),
        pytest.param(Shape.C, Shape.Z, 6),
    ],
)
def test_points_a(opponent, me, expected):
    assert points_a(opponent, me) == expected

@pytest.mark.parametrize(
    ("opponent", "outcome", "expected"),
    [
        pytest.param(Shape.A, Shape.Y, 4),
        pytest.param(Shape.B, Shape.X, 1),
        pytest.param(Shape.C, Shape.Z, 7),
    ],
)
def test_points_b(opponent, outcome, expected):
    assert points_b(opponent, outcome) == expected