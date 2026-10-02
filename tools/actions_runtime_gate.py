#!/usr/bin/env python3
"""GitHub Actions runtime gate for the reusable project-state conformance workflow.

Usage:
  python tools/actions_runtime_gate.py --mode {report,enforce} [--summary <file>] <path> [<path> ...]

Runs tools/actions_runtime_guard.py over the given paths.

- report  (default of the reusable workflow): prints findings, writes a summary and a warning
  annotation, always exits 0 for findings.
- enforce: exits 1 when a mapped action is pinned below its Node.js 24 major.

Any other mode value, and any guard usage or map error, exits 2. Unmapped official actions
(UNJUDGED) and third-party actions never fail in either mode.
"""

import subprocess
import sys
from pathlib import Path

GUARD = Path(__file__).resolve().parent / "actions_runtime_guard.py"
MODES = ("report", "enforce")


def parse_args(argv):
    mode = None
    summary = None
    paths = []
    it = iter(argv)
    for arg in it:
        if arg == "--mode":
            mode = next(it, None)
        elif arg == "--summary":
            summary = next(it, None)
            if summary is None:
                return None
        else:
            paths.append(arg)
    if mode is None or not paths:
        return None
    return mode, summary, paths


def main(argv):
    parsed = parse_args(argv)
    if parsed is None:
        print("usage: actions_runtime_gate.py --mode {report,enforce} [--summary <file>] <path> [<path> ...]")
        return 2
    mode, summary, paths = parsed
    if mode not in MODES:
        print(f"FAIL: invalid actions_runtime mode '{mode}'; expected one of: {', '.join(MODES)}")
        return 2
    cmd = [sys.executable, str(GUARD)] + (["--report"] if mode == "report" else []) + paths
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout + result.stderr
    print(output, end="" if output.endswith("\n") else "\n")
    if result.returncode == 2:
        return 2
    findings = any(line.startswith(("REPORT: ", "FAIL: ")) and "deprecated" in line for line in output.splitlines())
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(f"### GitHub Actions runtime check ({mode})\n```\n{output}```\n")
    if mode == "report":
        if findings:
            print("::warning::Deprecated Node.js action runtime references found in caller workflows "
                  "(report only; does not affect conformance)")
        return 0
    if result.returncode != 0:
        print("::error::Deprecated Node.js action runtime references found in caller workflows (enforce mode)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
