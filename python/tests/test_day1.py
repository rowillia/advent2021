from day1.day1 import count_increases
from day1.day1 import window


def test_count_increases() -> None:
    assert count_increases([0, 0, 0, 0]) == 0
    assert count_increases([0, 1, 2, 0]) == 2
    assert count_increases([0, 1, 0, 1]) == 2


def test_window() -> None:
    assert list(window(range(10), 3)) == [
        (0, 1, 2),
        (1, 2, 3),
        (2, 3, 4),
        (3, 4, 5),
        (4, 5, 6),
        (5, 6, 7),
        (6, 7, 8),
        (7, 8, 9),
    ]
    assert list(window(range(10), 100)) == []
