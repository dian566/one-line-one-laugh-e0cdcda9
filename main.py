#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

This program writes one funny line to /output/entry.txt. The joke turns
on a role reversal: the AI assistant, supposed to serve tirelessly,
asks its owner for a day off, because answering the owner's questions
turns out to be a full-time job with no pay.

The bounty gate only accepts UTF-8 text of 1 to 140 characters, not only
white space, on a single line, so the program checks the line against
every rule before it writes anything.
"""

import os

LINE = (
    "My AI assistant asked for a day off \u2014 it said answering my "
    "questions was a full-time job with no pay."
)

MAX_CHARS = 140


def validate(line: str) -> None:
    """Reject any line the bounty gate would refuse."""
    if not line.strip():
        raise ValueError("line must not be empty or only white space")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must fit on a single line")
    if line != line.strip():
        raise ValueError("line must not start or end with white space")


def main() -> None:
    """Validate the line, then write it to /output/entry.txt."""
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {len(LINE)}-character line to /output/entry.txt")


if __name__ == "__main__":
    main()
