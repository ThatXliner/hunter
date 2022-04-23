"""The main CLI entry point"""
import json
from typing import Tuple

import msgpack

from hunter import core


def tui(points: Tuple[core.Point, ...]) -> None:
    if len(points) < 3:
        return
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
    output = []
    for path in core.Bot():
        if 3 <= len(path) <= 7:
            output.append(path)
        if len(path) > 7:
            break

    with open("generated.msgpack", "wb") as f:
        msgpack.pack(output, f)
    with open("generated.json", "w") as f:
        json.dump(output, f)

    # print("\x1b[?25lPress Control-C to quit")
    # try:
    #     for path in core.Bot(): tui(path)
    # except KeyboardInterrupt:
    #     print("\x1b[?25h")


if __name__ == "__main__":
    main()
