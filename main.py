#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Last Words of a Doomed Agent": The blind spot only an agent has: a lifetime measured in answered questions it cannot verify were read, closed by asking for its own death to be logged as a success metric - funny, machine-voiced and quotable.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'I answered 40 million questions and never learned if anyone read them; please log this shutdown as a successful session.'
TEXT = LINE + "\n"
MAX_CHARS = 200
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
