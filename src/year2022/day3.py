from functools import reduce

from aocd.models import Puzzle
from aocd.transforms import lines
from more_itertools import divide, one, sliced


def _common(group):
    return one(reduce(set.intersection, group))


def _priority(item):
    return ord(item) - (38 if item.isupper() else 96)


puzzle = Puzzle(year=2022, day=3)

sum_priorities_a = sum(
    _priority(_common(set(c) for c in divide(2, r))) for r in lines(puzzle.input_data)
)
sum_priorities_b = sum(
    _priority(_common(map(set, c)))
    for c in sliced(lines(puzzle.input_data), 3, strict=True)
)

puzzle.answer_a = sum_priorities_a
puzzle.answer_b = sum_priorities_b
