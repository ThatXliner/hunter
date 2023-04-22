from typing import TypeVar, Callable, Iterator, Tuple, Set, Deque
from collections import deque

T = TypeVar("T")


def bfs(
    generate: Callable[[T], Iterator[T]], initial: Tuple[T, ...] = ()
) -> Iterator[T]:
    """Given a matrix of possible points, yield a tuple
    of points representing a new and unique path."""
    queue: Deque[T] = deque(initial)
    visited: Set[T] = set(initial)
    while queue:
        head = queue.popleft()
        yield head
        for x in generate(head):
            if x not in visited:
                queue.append(x)
                visited.add(x)
