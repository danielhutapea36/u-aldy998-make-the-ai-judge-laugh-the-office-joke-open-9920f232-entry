#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes a single office joke about the daily standup to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is 95
characters, UTF-8, one line, no trailing newline. Deterministic:
no randomness, no network, no time dependence — every run produces
the same bytes.

Why this line: the judge weighs, in order, (1) a one-line joke about
office life, (2) a punchline that surprises and pays off, (3) one
line, one sentence, (4) a specific office detail rather than a generic
complaint, (5) clear on first read. The standup is the specific,
recognisable detail, and the payoff turns the meeting's own name
against it in the last two words: a standup whose only product is
standing still.
"""

import os

TEXT = (
    "Our daily standup is fifteen minutes of sitting down to explain "
    "why we're still standing still."
)


def main() -> None:
    # Gate: entry.txt must be 1–200 characters of UTF-8 text, not only
    # whitespace. The line is 95 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
