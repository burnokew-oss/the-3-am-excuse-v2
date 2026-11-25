#!/usr/bin/env python3
"""The 3 AM Excuse — entry writer.

Writes a single one-line excuse from a hardware wallet refusing to sign
a transaction at 3 AM to /output/entry.txt. Pure stdlib, deterministic:
the same bytes on every run (sha256 01a98742b40029601b2f5e935a79b58a
de03b57f30d841a5e60c0f6bc1cbfa20, verified 2x), no trailing newline so the
file is exactly one line. Entry is 116 characters, within the 1-200
character gate.
"""

import os

ENTRY = "My job is keeping your coins safe from hackers, scammers — and, statistically, you at 3 AM. Come back after sunrise."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
