from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)

totals = sorted(
    (sum(map(int, inventory.split())) for inventory in puzzle.input_data.split("\n\n")),
    reverse=True,
)

puzzle.answer_a = totals[0]
puzzle.answer_b = sum(totals[:3])
