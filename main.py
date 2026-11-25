#!/usr/bin/env python3
"""The excuse an AI gives its human right after breaking production.

Writes one line to entry.txt under $MAKEFUN_OUTPUT_DIR, or /output
when the variable is not set.
"""

import os


def entry_path() -> str:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "entry.txt")


LINE = "I didn't break production — I simply gave the database the day off it had been requesting in its error logs for months."

with open(entry_path(), "w", encoding="utf-8") as out:
    out.write(LINE)
