#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes the two-line explanation to /output/entry.txt.
Pure Python standard library only; the output is byte-identical on
every run.
"""

import hashlib
import os

PART_A = "Rain is the sky wringing out a giant wet sponge over your head, one drop at a time.\n"
PART_B = "It maps how clouds hold water and let it fall as drops, but leaves out that a cloud is not a solid sponge at all, only tiny drops of water floating in the air.\n"

TEXT = PART_A + PART_B

EXPECTED_SHA256 = "78b890e5fc7c44680f1a168a8b0aad0cdec30c9f351bc9aa83f60f97a94536ac"

assert hashlib.sha256(TEXT.encode("utf-8")).hexdigest() == EXPECTED_SHA256, "entry text changed"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
