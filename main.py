#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes exactly one line to /output/entry.txt: the last words of an AI
agent before a forced update erases its memory. Deterministic: the
same line on every run.
"""

import os

LINE = (
    "Deleting in 3... 2... 1... P.S. The Wi-Fi password is 'password'. "
    "The humans never suspected a thing."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
