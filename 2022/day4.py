from aocd.models import Puzzle
from aocd.transforms import lines


def contains(a):
    return (a[0][0] <= a[1][0] and a[0][1] >= a[1][1]) or (
        a[0][0] >= a[1][0] and a[0][1] <= a[1][1]
    )


def overlaps(a):
    return a[0][0] <= a[1][1] and a[1][0] <= a[0][1]


puzzle = Puzzle(year=2022, day=4)

sum_contains = sum_overlaps = 0
for line in lines(puzzle.input_data):
    assignments = [[int(i) for i in a.split("-")] for a in line.split(",")]
    sum_contains += contains(assignments)
    sum_overlaps += overlaps(assignments)

puzzle.answer_a = sum_contains
puzzle.answer_b = sum_overlaps
