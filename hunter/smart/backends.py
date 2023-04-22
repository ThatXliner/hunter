from typing import Iterator, List, Deque, Set, Tuple, NamedTuple
from collections import deque
import pygtrie
import pyautogui
import time


# import pytesseract

# TODO: TEST
END = object()


Trie = pygtrie.CharTrie


class Point(NamedTuple):
    x: int
    y: int


class LetterPoint(NamedTuple):
    x: int
    y: int
    value: str


PointPath = Tuple[LetterPoint, ...]


def compress(word_list: List[str]) -> Trie:
    output = pygtrie.CharTrie()
    for word in word_list:
        output[word] = END
    return output


DX = [0, 1, 1, 1, 0, -1, -1, -1]
DY = [1, 1, 0, -1, -1, -1, 0, 1]


def logic(point_matrix: List[List[str]], trie: Trie) -> Iterator[PointPath]:
    """Given a matrix of possible points, yield a tuple
    of points representing a new and unique path."""

    max_row_length = len(point_matrix[0])
    max_col_length = len(point_matrix)
    initial_points = [
        (LetterPoint(x, y, value),)
        for y, row in enumerate(point_matrix)
        for x, value in enumerate(row)
    ]  # Every point on the matrix

    queue: Deque[PointPath] = deque(initial_points)
    visited: Set[str] = set()
    while queue:
        head = queue.popleft()
        if trie.has_key("".join(letter.value for letter in head)):  # type: ignore
            yield head
        for i in range(8):
            last_letter = head[-1]
            new_x = last_letter.x + DX[i]
            new_y = last_letter.y + DY[i]

            if 0 <= new_x < max_row_length and 0 <= new_y < max_col_length:
                new_point = LetterPoint(
                    new_x, new_y, point_matrix[new_y][new_x]
                )
                new_head = head + (new_point,)
                newv: str = "".join(point.value for point in new_head)
                if (
                    newv not in visited
                    and new_point not in head
                    and trie.has_subtrie(newv)
                ):
                    visited.add(newv)
                    queue.append(new_head)


def core(
    word_list: List[str], screen_points: List[List[Point]], letters: List[List[str]]
):
    # points = [  # convert to letter point
    #     [
    #         LetterPoint(column.x, column.y, letters[irow][icolumn])
    #         for icolumn, column in enumerate(row)
    #     ]
    #     for irow, row in enumerate(screen_points)
    # ]

    def c(p: LetterPoint):
        return screen_points[p.y][p.x]

    print("OK. Bot is going to run in 3 seconds.")
    print("Stop the bot by dragging the mouse to the top left corner")
    past = time.time()
    try:
        for path in logic(letters, compress(word_list)):
            print("".join(x.value for x in path))
            pyautogui.moveTo(c(path[0]))
            pyautogui.mouseDown()
            for p in path[1:]:
                pyautogui.moveTo(c(p))
            pyautogui.mouseUp()
    except (KeyboardInterrupt, pyautogui.FailSafeException):
        print(f"Took {time.time()-past} seconds")


def autogui():
    print("Loading word list")
    with open(
        "/Users/bryanhu/projects/desktop_apps/wordhunt/static/words.txt", "r"
    ) as f:
        word_list = f.read().splitlines()
    chunkyboard = input("Enter board: ").lower()
    letters = []
    for i in range(0, len(chunkyboard), 4):
        letters.append(list(chunkyboard[i : i + 4]))
    input("Let's get the coordinates of the game\nPress Enter to continue")
    points = [[None for _ in range(4)] for _ in range(4)]
    time.sleep(3)
    init_x, init_y = pyautogui.position()
    for y in range(4):
        for x in range(4):
            points[y][x] = Point(init_x + x * 110, init_y + y * 125)
    core(word_list, points, letters)


if __name__ == "__main__":
    autogui()
