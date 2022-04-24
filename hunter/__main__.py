"""The main CLI entry point"""

from typing import Tuple

import msgpack

from hunter import core


def tui() -> None:
    print("\x1b[?25lPress Control-C to quit")
    try:
        for path in core.Bot():
            if len(path) < 3:
                continue
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


def main() -> None:
    """The main CLI entry point"""
    output = []
    for path in core.Bot():
        if 4 <= len(path) <= 7:
            output.append(path)
        if len(path) > 7:
            break

    with open("generated.msgpack", "wb") as f:
        msgpack.pack(output, f)


if __name__ == "__main__":
    main()
