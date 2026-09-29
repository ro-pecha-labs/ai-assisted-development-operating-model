#!/usr/bin/env python3
"""GitHub Actions runtime guard.

Usage:
  python tools/actions_runtime_guard.py <path> [<path> ...]

Scans workflow files (*.yml, *.yaml) under the given paths and fails when a
`uses:` reference pins a known action to a major version that still runs on a
deprecated Node.js runtime. Unknown actions and non-major refs are reported but
not judged. Exits 0 when no violation is found, 1 on violations, 2 on usage errors.
"""

import re
import sys
from pathlib import Path

# Lowest major of each action that runs on node24 (verified from each version's action.yml).
MIN_NODE24_MAJOR = {
    "actions/checkout": 5,
    "actions/setup-python": 6,
    "actions/setup-dotnet": 5,
    "actions/upload-artifact": 6,
}

USES_RE = re.compile(r"^\s*(?:-\s*)?uses:\s*['\"]?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([A-Za-z0-9_.-]+)")
MAJOR_RE = re.compile(r"^v(\d+)(?:\.\d+){0,2}$")


def workflow_files(paths):
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            yield p
        elif p.is_dir():
            yield from sorted(x for x in p.rglob("*") if x.suffix in (".yml", ".yaml") and x.is_file())
        else:
            raise FileNotFoundError(raw)


def main(argv):
    if not argv:
        print("usage: actions_runtime_guard.py <path> [<path> ...]")
        return 2
    try:
        files = list(workflow_files(argv))
    except FileNotFoundError as missing:
        print(f"FAIL: path not found: {missing}")
        return 2
    violations = 0
    checked = 0
    for f in files:
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            m = USES_RE.match(line)
            if not m:
                continue
            action, ref = m.group(1), m.group(2)
            if action not in MIN_NODE24_MAJOR:
                continue
            checked += 1
            major = MAJOR_RE.fullmatch(ref)
            if not major:
                print(f"NOTE: {f}:{n}: {action}@{ref} is not a major/semver ref; not judged")
                continue
            if int(major.group(1)) < MIN_NODE24_MAJOR[action]:
                violations += 1
                print(f"FAIL: {f}:{n}: {action}@{ref} runs on a deprecated Node.js runtime; "
                      f"use v{MIN_NODE24_MAJOR[action]} or later")
    if violations:
        print(f"FAIL: {violations} deprecated action runtime reference(s) in {len(files)} file(s)")
        return 1
    print(f"PASS: {checked} known action reference(s) in {len(files)} file(s) run on node24")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
