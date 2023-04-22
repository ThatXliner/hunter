import time
from typing import List, Optional

import pyautogui
from rich.progress import Progress

from hunter.brute import core

__all__ = ["spam_print", "tui", "autogui"]
LOWER_BOUND = 3
UPPER_BOUND = 7


def spam_print(paths: Optional[List[core.PointPath]] = None) -> None:
    try:
        for path in paths or core.Bot():
            if len(path) < LOWER_BOUND:
                continue
            if len(path) > UPPER_BOUND:
                break
            print(path)
    except KeyboardInterrupt:
        return


def tui(paths: Optional[List[core.PointPath]] = None) -> None:
    # TODO: use rich
    print("\x1b[?25lPress Control-C to quit")
    try:
        for path in paths or core.Bot():
            if len(path) < LOWER_BOUND:
                continue
            if len(path) > UPPER_BOUND:
                break
            print(
                "\n".join(
                    [
                        "".join(
                            [
                                f"\x1b[41m{path.index(core.Point(x, y))}\x1b[0m"
                                if core.Point(x, y) in path
                                else "X"
                                for x in range(4)
                            ]
                        )
                        for y in range(4)
                    ]
                )
            )
            input("--- Continue ---")
    except KeyboardInterrupt:
        print("\x1b[?25h")


def autogui(paths: Optional[List[core.PointPath]] = None) -> None:
    input("Let's get the coordinates of the game\nPress Enter to continue")
    points = [[None for _ in range(4)] for _ in range(4)]
    for y in range(4):
        for x in range(4):
            print(
                f"Please move your mouse to the {y} row, {x} column:",
                end=" ",
                flush=True,
            )
            time.sleep(3)
            pos = pyautogui.position()
            print(f"Recorded: {pos}")
            points[y][x] = pos

    def c(p: core.Point):
        return points[p.y][p.x]

    print("OK. Bot is going to run in 5 seconds.")
    print("Stop the bot by dragging the mouse to the top left corner")

    time.sleep(5)
    past = time.time()
    try:
        with Progress() as progress:
            task = progress.add_task("Running...", total=99829)
            for path in paths or core.Bot():
                if len(path) < LOWER_BOUND:
                    continue
                if len(path) > UPPER_BOUND:
                    break
                progress.update(task, advance=1)
                print(path)
                pyautogui.moveTo(c(path[0]))
                pyautogui.mouseDown()
                for p in path[1:]:
                    pyautogui.moveTo(c(p))
                pyautogui.mouseUp()
    except (KeyboardInterrupt, pyautogui.FailSafeException):
        print(f"Took {time.time()-past} seconds")
