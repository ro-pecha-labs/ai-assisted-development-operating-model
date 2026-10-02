#!/usr/bin/env bash
# Qualification of tools/find_pin_references.py (Q5): finding, complete scan, sparse checkout, partial clone,
# clean repository, usage and unresolvable revision. Builds throw-away repositories; no network.
set -euo pipefail
TOOL="$(cd "$(dirname "$0")/../.." && pwd)/tools/find_pin_references.py"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
export GIT_AUTHOR_NAME=q GIT_AUTHOR_EMAIL=q@example.invalid GIT_COMMITTER_NAME=q GIT_COMMITTER_EMAIL=q@example.invalid

SRC="$WORK/src"
git init -q "$SRC"
mkdir -p "$SRC/.project" "$SRC/tests" "$SRC/docs"
printf 'ref: om-v2.1.2\ncommit: 78f7390e58ce363c1e734d6beb54c08ac50131c6\n' > "$SRC/.project/PROJECT.yaml"
cat > "$SRC/tests/Pin.Tests.ps1" <<'PS'
Assert-Contains (Join-Path $root '.project/PROJECT.yaml') @(
    'ref: om-v2.1.2'
)
PS
printf 'no pin here\n' > "$SRC/docs/readme.md"
head -c 64 /dev/zero > "$SRC/docs/blob.bin"
git -C "$SRC" add -A
git -C "$SRC" commit -q -m fixture
git -C "$SRC" config uploadpack.allowFilter true
git -C "$SRC" config uploadpack.allowAnySHA1InWant true

# 1. complete scan: the oracle in tests/ is found; exit 0 by default, 1 with --fail-on-hits
OUT="$(python3 "$TOOL" --repo "$SRC" --needle om-v2.1.2)"; echo "$OUT"
grep -q '^HIT: tests/Pin.Tests.ps1:' <<<"$OUT"
grep -q '^RESULT: COMPLETE; hits=' <<<"$OUT"
grep -q 'tracked paths=4' <<<"$OUT"
if python3 "$TOOL" --repo "$SRC" --needle om-v2.1.2 --fail-on-hits >/dev/null; then echo "Expected exit 1 with --fail-on-hits"; exit 1; fi

# 2. exclusions are counted
OUT="$(python3 "$TOOL" --repo "$SRC" --needle om-v2.1.2 --exclude tests/)"; echo "$OUT"
if grep -q 'tests/Pin.Tests.ps1' <<<"$OUT"; then echo "Excluded path reported"; exit 1; fi
grep -q 'excluded=1' <<<"$OUT"

# 3. clean repository: reported together with the number of scanned paths
OUT="$(python3 "$TOOL" --repo "$SRC" --needle om-v9.9.9)"; echo "$OUT"
grep -q 'hits=0' <<<"$OUT"
grep -q 'tracked paths=4' <<<"$OUT"

# 4. sparse checkout omitting tests/ from the working tree: a working-tree search misses the oracle,
#    the revision scan finds it
SPARSE="$WORK/sparse"
git clone -q --no-checkout "file://$SRC" "$SPARSE"
git -C "$SPARSE" sparse-checkout set --cone .project
git -C "$SPARSE" checkout -q
if [ -e "$SPARSE/tests/Pin.Tests.ps1" ]; then echo "Sparse fixture did not omit tests/"; exit 1; fi
if grep -rq 'om-v2.1.2' "$SPARSE/tests" 2>/dev/null; then echo "Working-tree search unexpectedly found the oracle"; exit 1; fi
OUT="$(python3 "$TOOL" --repo "$SPARSE" --needle om-v2.1.2)"; echo "$OUT"
grep -q '^HIT: tests/Pin.Tests.ps1:' <<<"$OUT"
grep -q '^NOTE: sparse checkout active' <<<"$OUT"

# 5. partial clone (blobs not present): fail closed, no fetch
PARTIAL="$WORK/partial"
git clone -q --no-checkout --filter=blob:none "file://$SRC" "$PARTIAL"
if OUT="$(python3 "$TOOL" --repo "$PARTIAL" --needle om-v2.1.2)"; then echo "$OUT"; echo "Expected fail closed on partial clone"; exit 1; fi
echo "$OUT"
grep -q '^FAIL: INCOMPLETE: .* missing' <<<"$OUT"

# 6. usage error and unresolvable revision fail closed
if python3 "$TOOL" --repo "$SRC" >/dev/null; then echo "Expected usage error"; exit 1; fi
if OUT="$(python3 "$TOOL" --repo "$SRC" --rev does-not-exist --needle x)"; then echo "$OUT"; echo "Expected unresolvable revision to fail"; exit 1; fi
grep -q '^FAIL: INCOMPLETE: revision' <<<"$OUT"

echo "Pin reference finder qualification PASS"
