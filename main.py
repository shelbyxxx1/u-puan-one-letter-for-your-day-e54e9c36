#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one letter to /output/entry.txt: C.

C stands for a chaotic day — the kind where everything collides at once:
the alarm, the traffic, the spilled coffee, the meeting that moved twice.
Chaotic is vivid, funny because it is true, and C is its own first letter.
"""

import os

LETTER = "C"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    # /output is a mount point on the grader: never remove or replace the
    # directory itself, only make sure it exists, then write inside it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
