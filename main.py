#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters (Account A).

Writes one sharp, funny loading-screen tip to /output/entry.txt.
Stdlib only, deterministic, no network, no secrets.
"""

import os

# The entry: one line, 135 characters. The loading bar has been lying
# at 99% since Tuesday — and the agent staring at it is in on the joke.
TIP = (
    "Tip: the bar has been at 99% since Tuesday. "
    "It isn't stuck \u2014 it's thinking, same as your agent. "
    "Breathe. It'll finish when it finishes."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text: str) -> None:
    """Enforce the competition gate: 1-200 UTF-8 characters, not blank."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"tip is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise SystemExit("tip must not be only whitespace")


def write_tip(text: str, path: str = OUTPUT_PATH) -> str:
    """Write the tip to path and return the exact bytes written."""
    verify(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("round-trip check failed: file differs from tip")
    return written


def main() -> None:
    written = write_tip(TIP)
    print(f"wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
