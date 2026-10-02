#!/usr/bin/env python3
"""Find artifacts that assert an exact OM pin (read-only).

Usage:
  python tools/find_pin_references.py --repo <path> [--rev <rev>] --needle <text> [--needle <text> ...]
                                      [--exclude <path-prefix> ...] [--fail-on-hits]

Scans ALL tracked paths at a named revision by reading Git objects, not only the working tree, for
each needle (typically the previous OM ref and commit). It is meant to be run before a project
adopts a new OM release, to find tests, workflows, vendored schemas and local governance prechecks
that assert the old pin.

The tool fails closed (exit 2) when it cannot prove that the scan is complete:
- the revision cannot be resolved (for example a shallow history that lacks it);
- tree or blob objects of the revision are missing (partial clone): the tool never fetches.

A sparse checkout does not limit the scan, because the revision is read from Git objects; the tool
reports it as a note. A clean result is always reported together with the number of tracked paths
scanned.

Exit codes: 0 scan complete (hits are listed; with --fail-on-hits, exit 1 when there are hits),
2 usage error or incomplete scan.
"""

import subprocess
import sys

MAX_TEXT = 160


def git(repo, *args, input_bytes=None):
    return subprocess.run(["git", "-C", repo, *args], input=input_bytes, capture_output=True)


def parse_args(argv):
    repo = None
    rev = "HEAD"
    needles = []
    excludes = []
    fail_on_hits = False
    it = iter(argv)
    for arg in it:
        if arg == "--repo":
            repo = next(it, None)
        elif arg == "--rev":
            rev = next(it, None)
        elif arg == "--needle":
            value = next(it, None)
            if value:
                needles.append(value)
        elif arg == "--exclude":
            value = next(it, None)
            if value:
                excludes.append(value)
        elif arg == "--fail-on-hits":
            fail_on_hits = True
        else:
            return None
    if not repo or not rev or not needles:
        return None
    return repo, rev, needles, excludes, fail_on_hits


def main(argv):
    parsed = parse_args(argv)
    if parsed is None:
        print("usage: find_pin_references.py --repo <path> [--rev <rev>] --needle <text> [--needle <text> ...] "
              "[--exclude <path-prefix> ...] [--fail-on-hits]")
        return 2
    repo, rev, needles, excludes, fail_on_hits = parsed

    resolved = git(repo, "rev-parse", "--verify", "--quiet", rev + "^{commit}")
    if resolved.returncode != 0:
        print(f"FAIL: INCOMPLETE: revision '{rev}' cannot be resolved in {repo} (shallow or missing history?)")
        return 2
    commit = resolved.stdout.decode().strip()

    notes = []
    if git(repo, "config", "--bool", "core.sparseCheckout").stdout.decode().strip() == "true":
        notes.append("sparse checkout active; the revision is read from Git objects, not from the working tree")
    if git(repo, "rev-parse", "--is-shallow-repository").stdout.decode().strip() == "true":
        notes.append("shallow repository; the scan covers only the tree of the named revision")

    objects = git(repo, "rev-list", "--objects", "--no-walk", "--missing=print", commit)
    if objects.returncode != 0:
        print(f"FAIL: INCOMPLETE: cannot enumerate objects of {commit}: {objects.stderr.decode().strip()}")
        return 2
    missing = [ln for ln in objects.stdout.decode().splitlines() if ln.startswith("?")]
    if missing:
        print(f"FAIL: INCOMPLETE: {len(missing)} object(s) of {commit} are missing (partial clone?); "
              "the tool does not fetch. Complete the clone or scan a full clone.")
        return 2

    tree = git(repo, "ls-tree", "-r", "-z", "--full-tree", commit)
    if tree.returncode != 0:
        print(f"FAIL: INCOMPLETE: cannot list tracked paths of {commit}: {tree.stderr.decode().strip()}")
        return 2
    entries = []
    submodules = 0
    for raw in tree.stdout.split(b"\0"):
        if not raw:
            continue
        meta, _, path = raw.partition(b"\t")
        mode, kind, sha = meta.decode().split()
        path = path.decode("utf-8", "surrogateescape")
        if kind == "commit":
            submodules += 1
            continue
        if kind == "blob":
            entries.append((sha, path))

    selected = [(sha, path) for sha, path in entries if not any(path.startswith(x) for x in excludes)]
    needles_b = [n.encode() for n in needles]
    hits = []
    binary = 0
    for sha, path in selected:
        blob = git(repo, "cat-file", "blob", sha)
        if blob.returncode != 0:
            print(f"FAIL: INCOMPLETE: cannot read blob {sha} ({path})")
            return 2
        data = blob.stdout
        if b"\0" in data:
            binary += 1
            continue
        for number, line in enumerate(data.splitlines(), 1):
            if any(n in line for n in needles_b):
                text = line.decode("utf-8", "replace").strip()
                hits.append((path, number, text[:MAX_TEXT]))

    for path, number, text in hits:
        print(f"HIT: {path}:{number}: {text}")
    for note in notes:
        print(f"NOTE: {note}")
    files = len({p for p, _, _ in hits})
    print(f"SCANNED: revision {commit}; tracked paths={len(entries)}, scanned={len(selected) - binary}, "
          f"excluded={len(entries) - len(selected)}, binary skipped={binary}, submodules skipped={submodules}")
    print(f"RESULT: COMPLETE; hits={len(hits)} in {files} file(s); needles={len(needles)}")
    return 1 if (hits and fail_on_hits) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
