#!/usr/bin/env python3
"""Advisory, read-only refresh check of tools/actions_runtime_map.json.

Usage:
  python tools/actions_runtime_map_refresh.py [--map <file>] [--fixtures <dir>] [--add <owner/repo> ...]
                                              [--max-major <n>] [--propose] [--date <YYYY-MM-DD>] [--fail-on-diff]

For every action of the map (and every --add action) the tool reads the upstream `action.yml`
(`runs.using`) of each major tag `v1`, `v2`, ... and derives the lowest major that runs on
Node.js 24 or later. It reports OK / DIFF / UNRESOLVED per action. It never writes the map and is
never part of a gate: a person reviews the report and updates the map in a PATCH-class change.

--fixtures <dir> reads recorded files `<dir>/<owner>__<repo>/<tag>.yml` instead of the network
(deterministic, used by qualification). Composite and docker actions have no Node.js runtime and
are reported as UNRESOLVED.

Exit codes: 0 report produced (1 with --fail-on-diff when a DIFF or UNRESOLVED exists), 2 usage,
map or network error.
"""

import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

DEFAULT_MAP = Path(__file__).resolve().parent / "actions_runtime_map.json"
URL = "https://raw.githubusercontent.com/{action}/v{major}/action.yml"
USING_RE = re.compile(r"^\s*using:\s*['\"]?([A-Za-z0-9_.-]+)", re.MULTILINE)
NODE_RE = re.compile(r"^node(\d+)$")


class RefreshError(Exception):
    pass


def read_using(action, major, fixtures):
    if fixtures:
        path = Path(fixtures) / action.replace("/", "__") / f"v{major}.yml"
        if not path.is_file():
            return None
        text = path.read_text(encoding="utf-8")
    else:
        try:
            with urllib.request.urlopen(URL.format(action=action, major=major), timeout=20) as resp:
                text = resp.read().decode("utf-8")
        except urllib.error.HTTPError as err:
            if err.code == 404:
                return None
            raise RefreshError(f"{action}@v{major}: HTTP {err.code}")
        except (urllib.error.URLError, OSError) as err:
            raise RefreshError(f"{action}@v{major}: {err}")
    runs = text.find("runs:")
    match = USING_RE.search(text[runs:] if runs >= 0 else text)
    return match.group(1) if match else "unknown"


def lowest_node24(observed):
    for major in sorted(observed):
        node = NODE_RE.match(observed[major])
        if node and int(node.group(1)) >= 24:
            return major
    return None


def parse_args(argv):
    opts = {"map": DEFAULT_MAP, "fixtures": None, "add": [], "max_major": None, "propose": False,
            "date": None, "fail_on_diff": False}
    it = iter(argv)
    for arg in it:
        if arg == "--map":
            opts["map"] = next(it, None)
        elif arg == "--fixtures":
            opts["fixtures"] = next(it, None)
        elif arg == "--add":
            opts["add"].append(next(it, None))
        elif arg == "--max-major":
            value = next(it, None)
            opts["max_major"] = int(value) if value and value.isdigit() else None
            if opts["max_major"] is None:
                return None
        elif arg == "--propose":
            opts["propose"] = True
        elif arg == "--date":
            opts["date"] = next(it, None)
        elif arg == "--fail-on-diff":
            opts["fail_on_diff"] = True
        else:
            return None
    if opts["map"] is None or any(a is None for a in opts["add"]):
        return None
    return opts


def main(argv):
    opts = parse_args(argv)
    if opts is None:
        print("usage: actions_runtime_map_refresh.py [--map <file>] [--fixtures <dir>] [--add <owner/repo> ...] "
              "[--max-major <n>] [--propose] [--date <YYYY-MM-DD>] [--fail-on-diff]")
        return 2
    try:
        current = json.loads(Path(opts["map"]).read_text(encoding="utf-8"))
        minimum = dict(current["node24_min_major"])
    except (OSError, ValueError, KeyError) as err:
        print(f"FAIL: cannot read runtime map {opts['map']}: {err}")
        return 2

    actions = list(minimum) + [a for a in opts["add"] if a not in minimum]
    proposed = dict(minimum)
    problems = 0
    try:
        for action in actions:
            top = opts["max_major"] or max(minimum.get(action, 1) + 3, 8)
            observed = {}
            for major in range(1, top + 1):
                using = read_using(action, major, opts["fixtures"])
                if using is not None:
                    observed[major] = using
            summary = ", ".join(f"v{m} {u}" for m, u in sorted(observed.items())) or "no major tags found"
            found = lowest_node24(observed)
            mapped = minimum.get(action)
            if found is None:
                problems += 1
                print(f"UNRESOLVED: {action}: no major runs on Node.js 24 or later ({summary})")
            elif mapped is None:
                problems += 1
                proposed[action] = found
                print(f"DIFF: {action}: not in the map; observed lowest Node.js 24 major v{found} ({summary})")
            elif found != mapped:
                problems += 1
                proposed[action] = found
                print(f"DIFF: {action}: map=v{mapped} observed=v{found} ({summary})")
            else:
                print(f"OK: {action}: min v{mapped} ({summary})")
            later = [m for m, u in observed.items() if found and m > found and NODE_RE.match(u)
                     and int(NODE_RE.match(u).group(1)) < 24]
            if later:
                print(f"NOTE: {action}: majors {', '.join('v' + str(m) for m in sorted(later))} above v{found} "
                      "run on a runtime older than Node.js 24; review manually")
    except RefreshError as err:
        print(f"FAIL: cannot read upstream metadata: {err}")
        return 2

    print(f"SUMMARY: {len(actions)} action(s) checked, {problems} difference(s) or unresolved")
    if opts["propose"] and proposed != minimum:
        updated = dict(current)
        updated["verified_on"] = opts["date"] or date.today().isoformat()
        updated["node24_min_major"] = dict(sorted(proposed.items()))
        print("PROPOSED (not written):")
        print(json.dumps(updated, indent=2))
    return 1 if (opts["fail_on_diff"] and problems) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
