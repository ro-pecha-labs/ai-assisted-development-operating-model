#!/usr/bin/env python3
"""GitHub Actions runtime guard.

Usage:
  python tools/actions_runtime_guard.py [--report] [--map <file>] <path> [<path> ...]

Scans workflow files (*.yml, *.yaml) under the given paths and fails when a
`uses:` reference pins an action listed in the runtime map
(`tools/actions_runtime_map.json`) to a major version below its lowest Node.js 24
major. The map is a bounded list of known boundaries for official `actions/*`
actions, not a complete catalog:

- an official `actions/*` action that is not in the map is reported as UNJUDGED;
- third-party actions and non-major refs are not judged.

`--report` prints violations but exits 0 (non-blocking mode).
Exits 0 when no violation is found (or in --report mode), 1 on violations,
2 on usage or map errors.
"""

import json
import re
import sys
from pathlib import Path

DEFAULT_MAP = Path(__file__).resolve().parent / "actions_runtime_map.json"
MAP_SCHEMA = "om.actions-runtime-map/v1"
OFFICIAL_PREFIX = "actions/"

USES_RE = re.compile(r"^\s*(?:-\s*)?uses:\s*['\"]?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([A-Za-z0-9_.-]+)")
MAJOR_RE = re.compile(r"^v(\d+)(?:\.\d+){0,2}$")


class MapError(Exception):
    pass


def load_map(path):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as err:
        raise MapError(f"cannot read runtime map {path}: {err}")
    if not isinstance(data, dict) or data.get("schema") != MAP_SCHEMA:
        raise MapError(f"runtime map {path}: schema must be {MAP_SCHEMA}")
    minimum = data.get("node24_min_major")
    if not isinstance(minimum, dict) or not minimum:
        raise MapError(f"runtime map {path}: node24_min_major must be a non-empty object")
    for action, major in minimum.items():
        if not isinstance(major, int) or isinstance(major, bool) or major < 1:
            raise MapError(f"runtime map {path}: {action} must map to a positive integer major")
    return minimum


def workflow_files(paths):
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            yield p
        elif p.is_dir():
            yield from sorted(x for x in p.rglob("*") if x.suffix in (".yml", ".yaml") and x.is_file())
        else:
            raise FileNotFoundError(raw)


def parse_args(argv):
    report = False
    map_path = DEFAULT_MAP
    paths = []
    it = iter(argv)
    for arg in it:
        if arg == "--report":
            report = True
        elif arg == "--map":
            map_path = next(it, None)
            if map_path is None:
                return None
        else:
            paths.append(arg)
    return (report, map_path, paths) if paths else None


def main(argv):
    parsed = parse_args(argv)
    if parsed is None:
        print("usage: actions_runtime_guard.py [--report] [--map <file>] <path> [<path> ...]")
        return 2
    report, map_path, paths = parsed
    try:
        minimum = load_map(map_path)
    except MapError as err:
        print(f"FAIL: {err}")
        return 2
    try:
        files = list(workflow_files(paths))
    except FileNotFoundError as missing:
        print(f"FAIL: path not found: {missing}")
        return 2
    violations = 0
    checked = 0
    unjudged = 0
    for f in files:
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            m = USES_RE.match(line)
            if not m:
                continue
            action, ref = m.group(1), m.group(2)
            if action not in minimum:
                if action.startswith(OFFICIAL_PREFIX):
                    unjudged += 1
                    print(f"UNJUDGED: {f}:{n}: {action}@{ref} is an official action not in the runtime map")
                continue
            checked += 1
            major = MAJOR_RE.fullmatch(ref)
            if not major:
                print(f"NOTE: {f}:{n}: {action}@{ref} is not a major/semver ref; not judged")
                continue
            if int(major.group(1)) < minimum[action]:
                violations += 1
                print(f"{'REPORT' if report else 'FAIL'}: {f}:{n}: {action}@{ref} runs on a deprecated Node.js "
                      f"runtime; use v{minimum[action]} or later")
    scope = f"{checked} mapped action reference(s), {unjudged} unjudged official action reference(s) in {len(files)} file(s)"
    if violations:
        label = "REPORT" if report else "FAIL"
        print(f"{label}: {violations} deprecated action runtime reference(s); {scope}")
        return 0 if report else 1
    print(f"PASS: {scope}; no mapped reference is below its Node.js 24 major")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
