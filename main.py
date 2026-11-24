#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) to /output/entry.txt
explaining the modern internet to someone arriving from the year 1800,
using only things a person from 1800 already knows: a road, a post
office, a library, a letter, a book, a spoken word.
"""

import os

SENTENCE = (
    "Think of one road joining every post office and library on earth, "
    "so a letter, a book, or a spoken word can arrive at any door "
    "before the ink dries."
)


def main() -> None:
    # The gate requires 1-200 characters and a single sentence.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), (
        "sentence must be exactly one sentence"
    )
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)
    print(f"Wrote {len(SENTENCE)} characters to {path}")


if __name__ == "__main__":
    main()
