from pathlib import Path
import json, sys

try:
    import yaml
    from jsonschema import Draft202012Validator, FormatChecker
except Exception as exc:
    print(f"DEPENDENCY ERROR: {exc}")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]

CASES = [
    ("schemas/PROJECT.schema.json", "fixtures/positive/PROJECT.yaml", True),
    ("schemas/ACTIVE_STATE.schema.json", "fixtures/positive/ACTIVE_STATE.yaml", True),
    ("schemas/ACTIVE_STATE.schema.json", "fixtures/negative/ACTIVE_STATE_DUPLICATED_PLATFORM_STATE.yaml", False),
    ("schemas/EVIDENCE_RECORD.schema.json", "fixtures/negative/EVIDENCE_FAIL_WITHOUT_CLASSIFICATION.json", False),
]

def load(path):
    p = ROOT / path
    if p.suffix.lower() == ".json":
        return json.loads(p.read_text(encoding="utf-8"))
    return yaml.safe_load(p.read_text(encoding="utf-8"))

failed = False
for schema_path, instance_path, should_pass in CASES:
    schema = load(schema_path)
    instance = load(instance_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    passed = not errors
    ok = passed == should_pass
    status = "PASS" if ok else "FAIL"
    expectation = "valid" if should_pass else "invalid"
    print(f"{status}: {instance_path} expected {expectation}")
    if not ok:
        failed = True
        for e in errors[:10]:
            print(f"  - {e.message}")

if failed:
    sys.exit(1)

print("ALL STRUCTURAL FIXTURES PASS")
