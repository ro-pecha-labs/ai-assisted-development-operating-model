#!/usr/bin/env bash
# Qualifies tools/ci_usage_report.py: report-only behaviour and the estimate method.
set -euo pipefail
cd "$(dirname "$0")"
T=../../tools/ci_usage_report.py

python "$T" static efficient.yml > static-ok.out
grep -q 'automatic=1' static-ok.out
if grep -E 'without concurrency|without timeout|windows/macos|both pull_request' static-ok.out; then
  echo 'efficient fixture must not be flagged'; exit 1
fi

python "$T" static wasteful.yml > static-bad.out        # report mode must exit 0
grep -q 'automatic workflow without concurrency' static-bad.out
grep -q 'job without timeout-minutes' static-bad.out
grep -q 'windows/macos runner' static-bad.out
grep -q 'both pull_request and push' static-bad.out

python "$T" usage --runs-tsv runs.tsv --jobs-tsv jobs.tsv > usage.out
grep -qxF "$(cat expected-usage.txt)" usage.out     # 1 min ubuntu + ceil(2.5)=3 min windows x2

# write-capable single-use workflow: reported separately, never flagged for missing concurrency (rule 15)
python "$T" static publish.yml > static-write.out
grep -q 'write-capable automatic workflow' static-write.out
if grep -q 'without concurrency' static-write.out; then
  echo 'write-capable fixture must not be flagged for concurrency'; exit 1
fi
grep -q 'automatic_write_capable=1' static-write.out

# usage --repo through an offline gh: parallel job fetch, all runs, then --max-runs
PATH="$PWD/fake-gh:$PATH" python "$T" usage --repo o/r --workers 4 > usage-repo.out
grep -qxF 'REPORT: runs=3 estimated_minutes=12 windows_or_macos_minutes=6 failed_runs=1' usage-repo.out   # 1 + 3x2 + 5
PATH="$PWD/fake-gh:$PATH" python "$T" usage --repo o/r --max-runs 1 > usage-max.out
grep -qxF 'REPORT: runs=1 estimated_minutes=1 windows_or_macos_minutes=0 failed_runs=0' usage-max.out

rm -f static-ok.out static-bad.out static-write.out usage.out usage-repo.out usage-max.out
echo "CI usage report qualification PASS"
