#!/usr/bin/env bash
# Qualifies the documented behavior of the platforms/git_local example hooks in a throwaway repository.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OM_ROOT="$(cd "$HERE/../.." && pwd)"
PY="${PYTHON:-python3}"
fails=0

ok()   { echo "PASS: $1"; }
bad()  { echo "FAIL: $1"; fails=$((fails + 1)); }
expect_ok()   { local name="$1"; shift; if "$@" >/dev/null 2>&1; then ok "$name"; else bad "$name (expected success)"; fi; }
expect_fail() { local name="$1"; shift; if "$@" >/dev/null 2>&1; then bad "$name (expected rejection)"; else ok "$name"; fi; }

W="$(mktemp -d)"
trap 'rm -rf "$W"' EXIT
cd "$W"
git init -q .
git config user.email q@example.invalid
git config user.name qualification
git config commit.gpgsign false
git config tag.gpgsign false
mkdir .githooks
# The example hooks shall be committed executable: they are installed by copy (mode preserved) without chmod.
expect_ok "example pre-commit is committed executable" test -x "$OM_ROOT/platforms/git_local/pre-commit.example"
expect_ok "example reference-transaction is committed executable" test -x "$OM_ROOT/platforms/git_local/reference-transaction.example"
cp -p "$OM_ROOT/platforms/git_local/pre-commit.example" .githooks/pre-commit
cp -p "$OM_ROOT/platforms/git_local/reference-transaction.example" .githooks/reference-transaction
git config core.hooksPath .githooks

# A disposable clone of the OM checkout stands in for the adopted OM revision: the ref cases need refs that can be created.
OM_SRC="$OM_ROOT"
OM_ROOT="$W/om"
pin="$(git -C "$OM_SRC" rev-parse HEAD)"
git clone -q --no-checkout "$OM_SRC" "$OM_ROOT"
git -C "$OM_ROOT" checkout -q --detach "$pin"
git -C "$OM_ROOT" tag om-test
git -C "$OM_ROOT" -c user.email=q@example.invalid -c user.name=qualification -c commit.gpgsign=false commit -q --allow-empty -m other
git -C "$OM_ROOT" tag om-other
git -C "$OM_ROOT" checkout -q --detach "$pin"
export OM_ROOT PYTHON="$PY"

echo base > README.md
git add README.md .githooks
expect_ok "ordinary commit is accepted" git commit -q -m base

# --- reference-transaction: accepted tags may be created once, never moved or deleted ---
echo two > a.txt; git add a.txt; git commit -q -m second
first=$(git rev-parse HEAD~1)
expect_ok   "accepted tag creation is allowed"            git tag v1-pass HEAD~1
expect_fail "accepted tag move is rejected"               git tag -f v1-pass HEAD
expect_fail "accepted tag deletion is rejected"           git tag -d v1-pass
expect_fail "accepted tag deletion by update-ref is rejected" git update-ref -d refs/tags/v1-pass
[ "$(git rev-parse v1-pass)" = "$first" ] && ok "accepted tag still points to its original commit" || bad "accepted tag moved"
expect_ok   "ordinary tag creation is allowed"            git tag probe HEAD~1
expect_ok   "ordinary tag move is allowed"                git tag -f probe HEAD
expect_ok   "ordinary tag deletion is allowed"            git tag -d probe

# --- pre-commit: forbidden content ---
mkdir -p src test/fixtures
echo 'let x = 1; // TEMP-probe' > src/a.js
git add src/a.js
expect_fail "staged TEMP- marker is rejected" git commit -q -m temp
git reset -q HEAD src/a.js; rm src/a.js

echo 'a,b' > data.csv
git add data.csv
expect_fail "staged data file outside fixtures is rejected" git commit -q -m data
git reset -q HEAD data.csv; rm data.csv

echo 'a,b' > test/fixtures/ok.csv
git add test/fixtures/ok.csv
expect_ok "synthetic fixture data file is accepted" git commit -q -m fixture

# --- pre-commit: project bootstrap validated from the staged copy against the exact OM revision ---
mkdir -p .project
cp "$OM_ROOT/qualification/project-conformance/valid/.project/"*.yaml .project/
sed -i "s/ref: development/ref: om-test/; s/commit: '1111111111111111111111111111111111111111'/commit: '$pin'/" .project/PROJECT.yaml
git add .project
expect_ok "conformant staged bootstrap is accepted" git commit -q -m bootstrap

sed -i "s/commit: '$pin'/commit: '2222222222222222222222222222222222222222'/" .project/PROJECT.yaml
git add .project/PROJECT.yaml
expect_fail "staged ref/commit mismatch is rejected" git commit -q -m mismatch
sed -i "s/commit: '2222222222222222222222222222222222222222'/commit: '$pin'/" .project/PROJECT.yaml
expect_fail "working-tree fix does not mask the staged mismatch" git commit -q -m masked
sed -i "s/ref: om-test/ref: om-missing/" .project/PROJECT.yaml
git add .project/PROJECT.yaml
expect_fail "staged ref that does not resolve in the OM checkout is rejected" git commit -q -m badref
sed -i "s/ref: om-missing/ref: om-other/" .project/PROJECT.yaml
git add .project/PROJECT.yaml
expect_fail "staged ref that resolves to a different commit than the pin is rejected" git commit -q -m otherref
sed -i "s/ref: om-other/ref: om-test/" .project/PROJECT.yaml
sed -i "s/name: Conformance Valid Fixture/name: Conformance Valid Fixture Renamed/" .project/PROJECT.yaml
git add .project/PROJECT.yaml
expect_ok "a conformant staged change of the bootstrap is accepted" git commit -q -m renamed

echo '# change' >> .project/ACTIVE_STATE.yaml
git add .project/ACTIVE_STATE.yaml
expect_fail "missing OM checkout stops the commit (fail closed)" env OM_ROOT="$W/no-om" git commit -q -m noom
git reset -q HEAD .project/ACTIVE_STATE.yaml

if [ "$fails" -ne 0 ]; then
  echo "git_local qualification FAIL ($fails)"
  exit 1
fi
echo "git_local qualification PASS"
