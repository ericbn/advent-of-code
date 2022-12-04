import pytest

from day4 import contains, overlaps


@pytest.mark.parametrize(
    ("a", "expected"),
    [
        pytest.param([[2, 4], [6, 8]], False),
        pytest.param([[4, 5], [2, 3]], False),
        pytest.param([[5, 7], [7, 9]], False),
        pytest.param([[2, 8], [3, 7]], True),
        pytest.param([[6, 6], [4, 6]], True),
        pytest.param([[4, 8], [2, 6]], False),
    ],
)
def test_contains(a, expected):
    assert contains(a) == expected


@pytest.mark.parametrize(
    ("a", "expected"),
    [
        pytest.param([[2, 4], [6, 8]], False),
        pytest.param([[4, 5], [2, 3]], False),
        pytest.param([[5, 7], [7, 9]], True),
        pytest.param([[2, 8], [3, 7]], True),
        pytest.param([[6, 6], [4, 6]], True),
        pytest.param([[4, 8], [2, 6]], True),
    ],
)
def test_overlaps(a, expected):
    assert overlaps(a) == expected
