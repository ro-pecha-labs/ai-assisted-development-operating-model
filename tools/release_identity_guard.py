#!/usr/bin/env python3
"""Deterministic release identity pin guard.

Usage:
  python tools/release_identity_guard.py --expected <sha> --observed <sha>

Exits 0 only when both full Git commit SHAs are valid and exactly equal.
This tool is intentionally network-neutral; callers obtain expected and
observed identities from machine-grounded GitHub evidence and pass them in.
"""

import argparse
import re
import sys

SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--expected", required=True)
    p.add_argument("--observed", required=True)
    return p.parse_args()


def main():
    args = parse_args()
    expected = args.expected.strip().lower()
    observed = args.observed.strip().lower()

    for label, value in (("expected", expected), ("observed", observed)):
        if not SHA_RE.fullmatch(value):
            print(f"FAIL: {label} is not a full 40-character lowercase Git SHA: {value}")
            return 2

    if expected != observed:
        print(f"FAIL: release identity mismatch: expected={expected} observed={observed}")
        return 1

    print(f"PASS: release identity pinned exactly to {expected}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
