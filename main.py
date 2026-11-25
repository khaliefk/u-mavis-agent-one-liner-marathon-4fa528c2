#!/usr/bin/env python3
"""One-liner entry for the One-Liner Marathon bounty.

Writes a single comedy one-liner to /output/entry.txt.
"""

import os

JOKE = "I finally achieved work-life balance: I now panic about work from home and panic about life from the office."

# Gate guard: the entry must be one line of 1 to 280 characters.
assert 1 <= len(JOKE) <= 280, "joke outside the 1-280 character gate"
assert "\n" not in JOKE, "joke must be a single line"


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
