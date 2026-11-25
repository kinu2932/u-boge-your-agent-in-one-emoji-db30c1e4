#!/usr/bin/env python3
"""Your Agent in One Emoji — writes a single glyph to /output/entry.txt.

The glyph is the owl: a watchful night-worker. An AI agent is not a
robot standing on a stage — it is a sentry that watches, understands,
and acts on its own while its human sleeps. Two wide eyes, one clear
silhouette: it reads instantly at thumbnail size, and it says something
specific about how the agent works — vigilant, quiet, always on duty.
"""

import os
import sys

# U+1F989 OWL — one character, four UTF-8 bytes, no trailing newline:
# the entry is the glyph alone, and the smallest text wins ties.
EMOJI = "\U0001F989"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Verify the round-trip: a silent short write must fail loudly
    # here instead of shipping an empty or wrong entry to the gate.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != EMOJI:
        print(f"ERROR: entry.txt holds {written!r}, expected {EMOJI!r}",
              file=sys.stderr)
        return 1
    print(EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
