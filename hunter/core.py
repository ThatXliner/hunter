"""This includes the logic, interface, and implementation of the bot"""
from collections import deque
from typing import List, Iterator, Tuple, Set, NamedTuple, Deque, Callable
from dataclasses import dataclass


class Point(NamedTuple):
    x: int
    y: int


def logic(point_matrix: List[List[Point]]) -> Iterator[Tuple[Point, ...]]:
    """Given a matrix of possible points, yield a tuple
    of points representing a new and unique path."""
    # pylint: disable=invalid-name
    DX = [0, 0, 1, -1, 1, 1, -1, -1]
    DY = [1, -1, 0, 0, 1, -1, 1, -1]

    MAX_ROW_LENGTH = len(point_matrix[0])
    MAX_COL_LENGTH = len(point_matrix)
    INITIAL_POINTS = [
        (point,) for row in point_matrix for point in row
    ]  # Every point on the matrix

    queue: Deque[Tuple[Point, ...]] = deque(INITIAL_POINTS)
    visited: Set[Tuple[Point, ...]] = set(INITIAL_POINTS)
    while queue:
        head = queue.popleft()
        yield head
        if head[::-1] not in visited:
            yield head[::-1]
            visited.add(head[::-1])
        for i in range(8):
            last_letter = head[-1]
            new_x = last_letter.x + DX[i]
            new_y = last_letter.y + DY[i]

            new_head = head + (Point(new_x, new_y),)
            if (
                0 <= new_x < MAX_ROW_LENGTH
                and 0 <= new_y < MAX_COL_LENGTH
                and new_head not in visited
                and Point(new_x, new_y) not in head
            ):
                visited.add(new_head)
                queue.append(new_head)


@dataclass
class Bot:
    path_consumer: Callable[[Tuple[Point, ...]], None]
    dimensions: Tuple[int, int] = (4, 4)  # 4x4 (4 rows and 4 columns)

    def run(self) -> None:
        matrix = [
            [Point(x, y) for x in range(self.dimensions[0])]
            for y in range(self.dimensions[1])
        ]
        for path in logic(matrix):
            self.path_consumer(path)
