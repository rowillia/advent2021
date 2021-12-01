import itertools
import math
import sys
from typing import Iterable, Tuple


def count_increases(values: Iterable[int]) -> int:
    result = 0
    last_value = math.inf
    for value in values:
        if value > last_value:
            result += 1
        last_value = value
    return result


def window(values: Iterable[int], window_size: int) -> Iterable[Tuple[int, ...]]:
    values = iter(values)
    current = tuple(itertools.islice(values, window_size))
    if len(current) < window_size:
        return
    for value in values:
        yield current
        current = current[1:] + (value,)
    yield current


def count_window_increases(values: Iterable[int], window_size: int) -> int:
    return count_increases((sum(x) for x in window(values, window_size)))


def main() -> None:
    stdin_as_ints = [int(line.strip()) for line in sys.stdin]
    print(count_increases(stdin_as_ints))
    print(count_window_increases(stdin_as_ints, 3))


if __name__ == "__main__":
    main()
