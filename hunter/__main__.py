"""The main CLI entry point"""

from typing import List

import msgpack

from . import backends, core


def generate() -> None:
    output = []
    for path in core.Bot():
        if 4 <= len(path) <= 7:
            output.append(path)
        if len(path) > 7:
            break

    with open("generated.msgpack", "wb") as f:
        msgpack.pack(output, f)


def load() -> List[core.PointPath]:
    with open("generated.msgpack", "rb") as f:
        output = msgpack.unpack(f)
    return [tuple(core.Point(*point) for point in path) for path in output]


def main() -> None:
    """The main CLI entry point"""
    backends.spam_print()


if __name__ == "__main__":
    main()
