# TODO: Highly simplify this. Make it so it's just backends.py
from typing import List

import msgpack
from hunter.brute import core


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
