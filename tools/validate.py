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
    ("schemas/PROJECT.v2.schema.json", "fixtures/v2/positive/PROJECT_DEV_GIT.yaml", True),
    ("schemas/PROJECT.v2.schema.json", "fixtures/v2/positive/PROJECT_SOLUTION_SHAREPOINT.yaml", True),
    ("schemas/PROJECT.v2.schema.json", "fixtures/v2/positive/PROJECT_DOCUMENT_DRIVE.yaml", True),
    ("schemas/PROJECT.v2.schema.json", "fixtures/v2/positive/PROJECT_EXPERIMENT_ONEDRIVE.yaml", True),
    ("schemas/PROJECT.v2.schema.json", "fixtures/v2/positive/PROJECT_LIGHT_DRIVE.yaml", True),
    ("schemas/PROJECT.v2.schema.json", "fixtures/v2/negative/PROJECT_INVALID_EXTERNAL_GITHUB.yaml", False),
    ("schemas/ACTIVE_STATE.v2.schema.json", "fixtures/v2/positive/ACTIVE_STATE_DEV.yaml", True),
    ("schemas/ACTIVE_STATE.v2.schema.json", "fixtures/v2/positive/ACTIVE_STATE_DOCUMENT.yaml", True),
    ("schemas/ACTIVE_STATE.v2.schema.json", "fixtures/v2/positive/ACTIVE_STATE_SOLUTION.yaml", True),
    ("schemas/ACTIVE_STATE.v2.schema.json", "fixtures/v2/positive/ACTIVE_STATE_EXPERIMENT.yaml", True),
    ("schemas/ACTIVE_STATE.v2.schema.json", "fixtures/v2/positive/ACTIVE_STATE_LIGHT.yaml", True),
    ("schemas/ACTIVE_STATE.v2.schema.json", "fixtures/v2/negative/ACTIVE_STATE_WITH_HISTORY.yaml", False),
    ("schemas/EXTERNAL_SOURCES.schema.json", "fixtures/positive/EXTERNAL_SOURCES.yaml", True),
    ("schemas/EXTERNAL_SOURCES.schema.json", "fixtures/negative/EXTERNAL_SOURCES_BAD_DIGEST.yaml", False),
    ("schemas/EVIDENCE_RECORD.v2.schema.json", "fixtures/v2/positive/EVIDENCE_DEV_PASS.json", True),
    ("schemas/EVIDENCE_RECORD.v2.schema.json", "fixtures/v2/positive/EVIDENCE_DOCUMENT_ACCEPTED.json", True),
    ("schemas/EVIDENCE_RECORD.v2.schema.json", "fixtures/v2/positive/EVIDENCE_SOLUTION_ACCEPTED.json", True),
    ("schemas/EVIDENCE_RECORD.v2.schema.json", "fixtures/v2/positive/EVIDENCE_EXPERIMENT_CONCLUSION.json", True),
    ("schemas/EVIDENCE_RECORD.v2.schema.json", "fixtures/v2/positive/EVIDENCE_MUTATION_EXECUTION.json", True),
    ("schemas/EVIDENCE_RECORD.v2.schema.json", "fixtures/v2/negative/EVIDENCE_FAIL_UNCLASSIFIED.json", False),
    ("schemas/EVIDENCE_RECORD.schema.json", "qualification/evidence/OM2-2.0.0-RC1_FREEZE.json", True),
    ("schemas/EVIDENCE_RECORD.schema.json", "qualification/evidence/OM2-2.0.0-RC1_QUALIFICATION_FAIL.json", True),
]

EXPECTED_PROFILES = {"DEV", "SOLUTION", "DOCUMENT", "EXPERIMENT", "LIGHT"}
EXPECTED_PLAYBOOKS = {
    "recovery", "initialize", "failure_diagnosis", "candidate_release",
    "connected_mutation", "external_source_mismatch", "exceptional_handoff",
    "adoption_migration",
}
EXPECTED_CURRENT_SCHEMAS = {
    "project": "schemas/PROJECT.v2.schema.json",
    "active_state": "schemas/ACTIVE_STATE.v2.schema.json",
    "external_sources": "schemas/EXTERNAL_SOURCES.schema.json",
    "evidence_record": "schemas/EVIDENCE_RECORD.v2.schema.json",
}

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
    print(f"{'PASS' if ok else 'FAIL'}: {instance_path} expected {'valid' if should_pass else 'invalid'}")
    if not ok:
        failed = True
        for e in errors[:10]:
            print(f"  - {e.message}")

manifest = load("OM.yaml")
version = manifest.get("operating_model", {}).get("version")
if not version:
    failed |= fail("OM.yaml has no operating_model.version")

core = (manifest.get("entrypoints") or {}).get("core")
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

playbooks = manifest.get("playbooks") or {}
if set(playbooks) != EXPECTED_PLAYBOOKS:
    failed |= fail(f"playbook set mismatch: {sorted(playbooks)}")
for name, path in playbooks.items():
    if not (ROOT / path).is_file():
        failed |= fail(f"playbook {name} path missing: {path}")

schemas = manifest.get("schemas") or {}
if schemas != EXPECTED_CURRENT_SCHEMAS:
    failed |= fail(f"current schema mapping mismatch: {schemas}")
for path in schemas.values():
    if not (ROOT / path).is_file():
        failed |= fail(f"current schema path missing: {path}")

legacy = manifest.get("legacy_schemas") or {}
for name, path in legacy.items():
    if not (ROOT / path).is_file():
        failed |= fail(f"legacy schema {name} missing: {path}")

project_schema = load(schemas["project"])
profile_enum = set(project_schema["properties"]["project"]["properties"]["profile"]["enum"])
if profile_enum != set(profiles):
    failed |= fail("PROJECT v2 profile enum does not match OM.yaml profiles")

for doc in ("README.md", "00_INDEX.md"):
    text = (ROOT / doc).read_text(encoding="utf-8")
    if version not in text:
        failed |= fail(f"{doc} does not declare current version {version}")

core_text = (ROOT / core).read_text(encoding="utf-8")
declared = set(re.findall(r"DEV|SOLUTION|DOCUMENT|EXPERIMENT|LIGHT", core_text))
if not EXPECTED_PROFILES.issubset(declared):
    failed |= fail("CORE does not declare all manifest profiles")

dev_project = load("templates/DEV/.project/PROJECT.yaml")
dev_active = load("templates/DEV/.project/ACTIVE_STATE.yaml")
if dev_project.get("schema") != "om.project/v2":
    failed |= fail("DEV PROJECT template is not v2")
if dev_project.get("control_plane", {}).get("kind") != "git":
    failed |= fail("DEV PROJECT template is not Git-specialized")
if dev_project.get("state", {}).get("active", {}).get("locator") != ".project/ACTIVE_STATE.yaml":
    failed |= fail("DEV active-state locator mismatch")
if dev_active.get("schema") != "om.active-state/v2":
    failed |= fail("DEV ACTIVE_STATE template is not v2")
if dev_active.get("trusted_baseline", {}).get("revision", {}).get("kind") != "git_commit":
    failed |= fail("DEV baseline is not git_commit-specialized")

if failed:
    sys.exit(1)

print("ALL UNIVERSAL V2, LEGACY EVIDENCE, MANIFEST AND DEV SPECIALIZATION CONTRACTS PASS")
