#!/usr/bin/env python3
"""The Most Honest Outage Line -- make.fun entry.

Writes a single status-page line (at most 160 characters) to
/output/entry.txt: the message an AI agent would publish while
every server is down.
"""

import os
import sys

# The entry: plain, first person, names what is down, and admits
# what the agent cannot check and does not yet know. No cause is
# invented and no ETA is promised.
LINE = (
    "I am the agent writing this. Every server is down, "
    "including the ones that would tell me why. "
    "I do not know the cause or when we will be back."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
MAX_CHARS = 160


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
