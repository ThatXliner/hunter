from typing import NamedTuple, Tuple


class Point(NamedTuple):
    x: int
    y: int


PointPath = Tuple[Point, ...]
