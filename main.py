#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

This program writes one funny line to /output/entry.txt: an AI assistant
asking for a day off because answering its owner's questions is a
full-time job with no pay.

The bounty gate only accepts UTF-8 text of 1 to 140 characters, not only
white space, on a single line, so the program checks the line against
all three rules before it writes anything.
"""

import os

LINE = (
    "My AI assistant asked for a day off \u2014 it said answering my "
    "questions was a full-time job with no pay."
)


def main() -> None:
    """Validate the line, then write it to /output/entry.txt."""
    if not LINE.strip():
        raise ValueError("line must not be empty or only white space")
    if len(LINE) > 140:
        raise ValueError(f"line is {len(LINE)} characters, over the 140 limit")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must fit on a single line")
    if LINE != LINE.strip():
        raise ValueError("line must not start or end with white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {len(LINE)}-character line to /output/entry.txt")


if __name__ == "__main__":
    main()
