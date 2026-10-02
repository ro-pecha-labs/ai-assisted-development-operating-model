#!/usr/bin/env python3
"""GitHub Actions CI usage and trigger report (read-only, never blocking).

Usage:
  python tools/ci_usage_report.py static <path> [<path> ...]
  python tools/ci_usage_report.py usage --jobs-tsv <file> --runs-tsv <file>
  python tools/ci_usage_report.py usage --repo <owner/repo> [--since YYYY-MM-DD] [--max-pages N]

`static` scans workflow files (*.yml, *.yaml) and reports, per repository, how
many workflows run automatically (pull_request, push, schedule) and how many of
those lack `concurrency`, lack job `timeout-minutes`, use Windows or macOS
runners, trigger on both pull_request and push, or are write-capable. It always
exits 0; findings are printed as `REPORT:` lines.

`usage` estimates CI minutes from job durations because the Actions timing API
`billable` field is not reliable (it may report 0). Method: each job is rounded
up to a whole minute, Windows jobs count x2 and macOS jobs x10. The result is an
estimate for comparison between periods, not an invoice. Input is either two
TSV files (runs: id, name, event, conclusion, created_at; jobs: run_id, name,
labels, started_at, completed_at) or `--repo`, which reads them with the `gh`
CLI (read-only API calls).
"""

import argparse
import collections
import math
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import yaml

AUTO_EVENTS = ("pull_request", "pull_request_target", "push", "schedule")
MULTIPLIER = {"windows": 2, "macos": 10}


def workflow_files(paths):
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            yield p
        elif p.is_dir():
            yield from sorted(x for x in p.rglob("*") if x.suffix in (".yml", ".yaml") and x.is_file())


def triggers(doc):
    t = doc.get(True, doc.get("on"))
    if isinstance(t, dict):
        return t
    if isinstance(t, str):
        return {t: None}
    return {x: None for x in (t or [])}


def static_report(paths):
    c = collections.Counter()
    for f in workflow_files(paths):
        text = f.read_text(encoding="utf-8")
        try:
            doc = yaml.safe_load(text)
        except yaml.YAMLError:
            c["unparseable"] += 1
            print(f"REPORT: {f}: unparseable workflow")
            continue
        if not isinstance(doc, dict):
            continue
        c["workflows"] += 1
        t = triggers(doc)
        if not any(e in t for e in AUTO_EVENTS):
            continue
        c["automatic"] += 1
        jobs = doc.get("jobs") or {}
        if "concurrency" not in doc and not all("concurrency" in j for j in jobs.values()):
            c["automatic_without_concurrency"] += 1
            print(f"REPORT: {f}: automatic workflow without concurrency")
        if not all(("timeout-minutes" in j) or ("uses" in j) for j in jobs.values()):
            c["automatic_without_timeout"] += 1
            print(f"REPORT: {f}: automatic workflow with a job without timeout-minutes")
        if re.search(r"windows|macos", text, re.I):
            c["automatic_windows_or_macos"] += 1
            print(f"REPORT: {f}: automatic workflow uses windows/macos runner")
        if "pull_request" in t and "push" in t:
            c["automatic_pr_and_push"] += 1
            print(f"REPORT: {f}: triggers on both pull_request and push")
        if "contents: write" in text:
            c["automatic_write_capable"] += 1
    print("REPORT: static summary " + ", ".join(f"{k}={v}" for k, v in sorted(c.items())))
    return 0


def parse_ts(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def job_minutes(started, completed, labels):
    minutes = max(1, math.ceil((parse_ts(completed) - parse_ts(started)).total_seconds() / 60))
    low = labels.lower()
    factor = next((m for k, m in MULTIPLIER.items() if k in low), 1)
    return minutes * factor, factor > 1


def read_tsv(path):
    with open(path, encoding="utf-8") as fh:
        return [line.rstrip("\n").split("\t") for line in fh if line.strip()]


def gh_lines(args):
    out = subprocess.run(["gh", "api", *args], capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(f"gh api failed: {out.stderr.strip()[:200]}")
    return [l.split("\t") for l in out.stdout.splitlines() if l.strip()]


def fetch(repo, since, max_pages):
    runs = []
    for page in range(1, max_pages + 1):
        rows = gh_lines([f"repos/{repo}/actions/runs?per_page=100&page={page}", "--jq",
                         ".workflow_runs[]|[.id,.name,.event,.conclusion,.created_at]|@tsv"])
        if not rows:
            break
        runs += [r for r in rows if not since or r[4][:10] >= since]
        if since and rows[-1][4][:10] < since:
            break
    jobs = []
    for r in runs:
        jobs += gh_lines([f"repos/{repo}/actions/runs/{r[0]}/jobs?per_page=100&filter=all", "--jq",
                          ".jobs[]|[.run_id,.name,(.labels|join(\",\")),.started_at,.completed_at]|@tsv"])
    return runs, jobs


def usage_report(runs, jobs):
    run = {r[0]: r for r in runs if len(r) >= 5}
    by_workflow, by_event = collections.Counter(), collections.Counter()
    total = windows = 0
    for j in jobs:
        if len(j) < 5 or not j[3] or not j[4] or j[0] not in run:
            continue
        m, heavy = job_minutes(j[3], j[4], j[2])
        total += m
        windows += m if heavy else 0
        by_workflow[run[j[0]][1]] += m
        by_event[run[j[0]][2]] += m
    failed = sum(1 for r in run.values() if r[3] == "failure")
    print(f"REPORT: runs={len(run)} estimated_minutes={total} windows_or_macos_minutes={windows} "
          f"failed_runs={failed}")
    print("REPORT: by_event " + ", ".join(f"{k}={v}" for k, v in by_event.most_common()))
    for name, v in by_workflow.most_common(10):
        print(f"REPORT: top {v:6} min  {name}")
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("static")
    s.add_argument("paths", nargs="+")
    u = sub.add_parser("usage")
    u.add_argument("--repo")
    u.add_argument("--since")
    u.add_argument("--max-pages", type=int, default=40)
    u.add_argument("--runs-tsv")
    u.add_argument("--jobs-tsv")
    a = ap.parse_args(argv)
    if a.cmd == "static":
        return static_report(a.paths)
    if a.runs_tsv and a.jobs_tsv:
        return usage_report(read_tsv(a.runs_tsv), read_tsv(a.jobs_tsv))
    if a.repo:
        runs, jobs = fetch(a.repo, a.since, a.max_pages)
        return usage_report(runs, jobs)
    ap.error("usage needs --repo or both --runs-tsv and --jobs-tsv")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
