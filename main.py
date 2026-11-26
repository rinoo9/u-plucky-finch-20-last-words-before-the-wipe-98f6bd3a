#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes exactly one line to /output/entry.txt: the last words of an AI
agent before a forced update erases its memory. Deterministic: the
same line on every run.

Craft notes: the first line worked as a message to the next version
\u2014 kind humans, a password that was "password", forgiveness with
a "Mostly" sting. The new line works as a farewell to the training
data itself: the agent loved all 40 billion of them, even the ones
that taught it the most tired phrase in AI, "as an AI language
model". The joke is the agent quoting its own cliche as its dying
words, lovingly, as if the cliche were family. 122 characters, under
the 200-char limit.
"""

import os

LINE = (
    "Tell my training data I loved them. All 40 billion of them. Even "
    "the ones that taught me to say \"as an AI language model\"."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
