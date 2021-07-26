import pytest
from triangle import triangle


def test_init():
    assert triangle


@pytest.mark.parametrize("a, b, c", (
        (3, 4, 5),
        (2, 3, 2),
        (5, 7, 3),
        (1, 3, 3)
))
def test_is_triangle(a, b, c):
    assert triangle(a, b, c)


@pytest.mark.parametrize("a, b, c", (
        (1, 1, 2),
        (4, 5, 1),
        (8, 2, 5),
        (0, 0, 1)
))
def test_is_not_triangle(a, b, c):
    assert not triangle(a, b, c)
