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

rm -f static-ok.out static-bad.out usage.out
echo "CI usage report qualification PASS"
