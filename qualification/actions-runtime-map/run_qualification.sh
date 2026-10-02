#!/usr/bin/env bash
# Qualification of the actions runtime map maintenance (Q4): schema validation of the real map and
# of invalid maps, and the advisory refresh tool against recorded upstream fixtures (offline).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
Q="$ROOT/qualification/actions-runtime-map"
REFRESH="$ROOT/tools/actions_runtime_map_refresh.py"

python3 - "$ROOT" <<'PY'
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
root = Path(sys.argv[1])
schema = json.loads((root / "schemas/ACTIONS_RUNTIME_MAP.v1.schema.json").read_text())
validator = Draft202012Validator(schema, format_checker=FormatChecker())
def errors(path):
    return list(validator.iter_errors(json.loads(Path(path).read_text())))
for good in ("tools/actions_runtime_map.json", "qualification/actions-runtime-map/maps/map-ok.json",
             "qualification/actions-runtime-map/maps/map-stale.json"):
    assert not errors(root / good), good
for bad in sorted((root / "qualification/actions-runtime-map/maps").glob("invalid-*.json")):
    assert errors(bad), f"{bad.name} unexpectedly valid"
    print("rejected:", bad.name)
print("Map schema validation PASS")
PY

# refresh tool, current map: no difference
OUT="$(python3 "$REFRESH" --map "$Q/maps/map-ok.json" --fixtures "$Q/fixtures" --max-major 6 --fail-on-diff)"; echo "$OUT"
grep -q '^OK: actions/checkout: min v5' <<<"$OUT"
grep -q '^OK: actions/example: min v2' <<<"$OUT"
grep -q '^SUMMARY: 2 action(s) checked, 0 difference' <<<"$OUT"

# stale map: DIFF and UNRESOLVED; advisory exit 0, exit 1 with --fail-on-diff; proposal is printed, not written
BEFORE="$(sha256sum "$Q/maps/map-stale.json")"
OUT="$(python3 "$REFRESH" --map "$Q/maps/map-stale.json" --fixtures "$Q/fixtures" --max-major 6 --propose --date 2026-10-03)"; echo "$OUT"
grep -q '^DIFF: actions/example: map=v3 observed=v2' <<<"$OUT"
grep -q '^UNRESOLVED: actions/composite' <<<"$OUT"
grep -q '"verified_on": "2026-10-03"' <<<"$OUT"
grep -q '"actions/example": 2' <<<"$OUT"
[ "$BEFORE" = "$(sha256sum "$Q/maps/map-stale.json")" ]
if python3 "$REFRESH" --map "$Q/maps/map-stale.json" --fixtures "$Q/fixtures" --max-major 6 --fail-on-diff >/dev/null; then
  echo "Expected exit 1 with --fail-on-diff"; exit 1
fi

# an action that is not in the map is reported with --add
OUT="$(python3 "$REFRESH" --map "$Q/maps/map-ok.json" --fixtures "$Q/fixtures" --max-major 6 --add actions/composite)"; echo "$OUT"
grep -q '^UNRESOLVED: actions/composite' <<<"$OUT"

# usage and map errors fail with exit 2
set +e
python3 "$REFRESH" --bogus >/dev/null; [ $? -eq 2 ] || { echo "Expected usage exit 2"; exit 1; }
python3 "$REFRESH" --map "$Q/maps/does-not-exist.json" >/dev/null; [ $? -eq 2 ] || { echo "Expected map error exit 2"; exit 1; }
set -e
echo "Actions runtime map maintenance qualification PASS"
