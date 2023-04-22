from typing import Tuple, NamedTuple


class Point(NamedTuple):
    x: int
    y: int


PointPath = Tuple[Point, ...]
