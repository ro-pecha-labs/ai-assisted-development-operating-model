from pathlib import Path
import json
import re
import sys

try:
    import yaml
    from jsonschema import Draft202012Validator, FormatChecker
except Exception as exc:
    print(f"DEPENDENCY ERROR: {exc}")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]

CASES = [
    ("schemas/PROJECT.schema.json", "fixtures/positive/PROJECT.yaml", True),
    ("schemas/PROJECT.schema.json", "fixtures/negative/PROJECT_BAD_RULES_PATH.yaml", False),
    ("schemas/ACTIVE_STATE.schema.json", "fixtures/positive/ACTIVE_STATE.yaml", True),
    ("schemas/ACTIVE_STATE.schema.json", "fixtures/negative/ACTIVE_STATE_DUPLICATED_PLATFORM_STATE.yaml", False),
    ("schemas/EXTERNAL_SOURCES.schema.json", "fixtures/positive/EXTERNAL_SOURCES.yaml", True),
    ("schemas/EXTERNAL_SOURCES.schema.json", "fixtures/negative/EXTERNAL_SOURCES_BAD_DIGEST.yaml", False),
    ("schemas/EVIDENCE_RECORD.schema.json", "fixtures/positive/EVIDENCE_RECORD.json", True),
    ("schemas/EVIDENCE_RECORD.schema.json", "fixtures/positive/EVIDENCE_FAIL_CLASSIFIED.json", True),
    ("schemas/EVIDENCE_RECORD.schema.json", "fixtures/negative/EVIDENCE_FAIL_WITHOUT_CLASSIFICATION.json", False),
]

EXPECTED_PROFILES = {"DEV", "SOLUTION", "DOCUMENT", "EXPERIMENT", "LIGHT"}
EXPECTED_PLAYBOOKS = {
    "recovery",
    "initialize",
    "failure_diagnosis",
    "candidate_release",
    "connected_mutation",
    "external_source_mismatch",
    "exceptional_handoff",
    "adoption_migration",
}
EXPECTED_SCHEMAS = {"project", "active_state", "external_sources", "evidence_record"}


def load(path):
    p = ROOT / path
    if p.suffix.lower() == ".json":
        return json.loads(p.read_text(encoding="utf-8"))
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def fail(message):
    print(f"FAIL: {message}")
    return True


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

manifest = load("OM.yaml")
version = manifest.get("operating_model", {}).get("version")
if not version:
    failed |= fail("OM.yaml has no operating_model.version")

entrypoints = manifest.get("entrypoints") or {}
core = entrypoints.get("core")
if not core or not (ROOT / core).is_file():
    failed |= fail(f"missing CORE entrypoint: {core}")
else:
    print(f"PASS: CORE entrypoint exists: {core}")

profiles = manifest.get("profiles") or {}
if set(profiles) != EXPECTED_PROFILES:
    failed |= fail(f"profile set mismatch: {sorted(profiles)}")
for name, path in profiles.items():
    if not (ROOT / path).is_file():
        failed |= fail(f"profile {name} path missing: {path}")
    else:
        print(f"PASS: profile {name} -> {path}")

playbooks = manifest.get("playbooks") or {}
if set(playbooks) != EXPECTED_PLAYBOOKS:
    failed |= fail(f"playbook set mismatch: {sorted(playbooks)}")
for name, path in playbooks.items():
    if not (ROOT / path).is_file():
        failed |= fail(f"playbook {name} path missing: {path}")
    else:
        print(f"PASS: playbook {name} -> {path}")

schemas = manifest.get("schemas") or {}
if set(schemas) != EXPECTED_SCHEMAS:
    failed |= fail(f"schema set mismatch: {sorted(schemas)}")
for name, path in schemas.items():
    if not (ROOT / path).is_file():
        failed |= fail(f"schema {name} path missing: {path}")
    else:
        print(f"PASS: schema {name} -> {path}")

project_schema = load("schemas/PROJECT.schema.json")
profile_enum = set(project_schema["properties"]["project"]["properties"]["profile"]["enum"])
if profile_enum != set(profiles):
    failed |= fail(f"PROJECT profile enum does not match OM.yaml profiles: {sorted(profile_enum)}")
else:
    print("PASS: PROJECT profile enum matches OM.yaml")

for doc in ("README.md", "00_INDEX.md"):
    text = (ROOT / doc).read_text(encoding="utf-8")
    if version not in text:
        failed |= fail(f"{doc} does not declare current OM.yaml version {version}")
    else:
        print(f"PASS: {doc} version matches {version}")

core_text = (ROOT / core).read_text(encoding="utf-8")
declared = set(re.findall(r"DEV|SOLUTION|DOCUMENT|EXPERIMENT|LIGHT", core_text))
if not EXPECTED_PROFILES.issubset(declared):
    failed |= fail("CORE does not declare all manifest profiles")
else:
    print("PASS: CORE declares all manifest profiles")

if failed:
    sys.exit(1)

print("ALL STRUCTURAL AND MANIFEST CONTRACTS PASS")
