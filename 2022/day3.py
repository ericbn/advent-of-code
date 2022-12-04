from functools import reduce

from aocd.models import Puzzle
from aocd.transforms import lines
from more_itertools import divide, sliced


def _common(group):
    (value,) = reduce(set.intersection, group)
    return value


def _priority(item):
    return ord(item) - (38 if item.isupper() else 96)


puzzle = Puzzle(year=2022, day=3)

puzzle.answer_a = sum(
    _priority(_common(set(c) for c in divide(2, r))) for r in lines(puzzle.input_data)
)
puzzle.answer_b = sum(
    _priority(_common(map(set, c)))
    for c in sliced(lines(puzzle.input_data), 3, strict=True)
)
