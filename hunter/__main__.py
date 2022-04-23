"""The main CLI entry point"""
from typing import Tuple

from hunter import core


def consumer(points: Tuple[core.Point, ...]) -> None:
    print(
        "\n".join(
            [
                "".join(
                    [
                        f"\x1b[41m{points.index(core.Point(x, y))}\x1b[0m"
                        if core.Point(x, y) in points
                        else "X"
                        for x in range(4)
                    ]
                )
                for y in range(4)
            ]
        )
    )
    input("--- Continue ---")


def main() -> None:
    """The main CLI entry point"""
    print("\x1b[?25lPress Control-C to quit")
    try:
        core.Bot(consumer).run()
    except KeyboardInterrupt:
        print("\x1b[?25h")


if __name__ == "__main__":
    main()
