from enum import Enum

from aocd.models import Puzzle
from aocd.transforms import lines
from bidict import bidict


class Shape(Enum):
    ROCK = A = X = 1
    PAPER = B = Y = 2
    SCISSORS = C = Z = 3


class IdentityDict:
    def __getitem__(self, item):
        return item


WINS = bidict(
    {Shape.ROCK: Shape.SCISSORS, Shape.PAPER: Shape.ROCK, Shape.SCISSORS: Shape.PAPER}
)
DRAWS = IdentityDict()
LOSES = WINS.inverse
OUTCOMES = {
    Shape.X: WINS,
    Shape.Y: DRAWS,
    Shape.Z: LOSES,
}


def _outcome_points_a(opponent, me):
    if LOSES[me] == opponent:
        return 0
    if me == opponent:
        return 3
    return 6


def points_a(opponent, me):
    return me.value + _outcome_points_a(opponent, me)


def points_b(opponent, outcome):
    return points_a(opponent, OUTCOMES[outcome][opponent])


puzzle = Puzzle(year=2022, day=2)

total_a = total_b = 0
for line in lines(puzzle.input_data):
    r = [Shape[s] for s in line.split()]
    total_a += points_a(*r)
    total_b += points_b(*r)

puzzle.answer_a = total_a
puzzle.answer_b = total_b
