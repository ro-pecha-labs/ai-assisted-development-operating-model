from pathlib import Path
import argparse
import json
import subprocess
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker


def load_data(path: Path):
    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate(schema_path: Path, instance_path: Path):
    schema = load_data(schema_path)
    instance = load_data(instance_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        print(f"FAIL: {instance_path} against {schema_path}")
        for error in errors[:20]:
            location = ".".join(str(x) for x in error.path) or "<root>"
            print(f"  - {location}: {error.message}")
        return False
    print(f"PASS: {instance_path} against {schema_path}")
    return True


def local_path(root: Path, locator: str, label: str):
    p = (root / locator).resolve()
    try:
        p.relative_to(root.resolve())
    except ValueError:
        raise ValueError(f"{label} locator escapes project root: {locator}")
    if not p.is_file():
        raise FileNotFoundError(f"{label} file not found: {locator}")
    return p


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--om-root", type=Path, required=True)
    parser.add_argument("--skip-om-git-pin-check", action="store_true")
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    om_root = args.om_root.resolve()
    project_file = project_root / ".project" / "PROJECT.yaml"

    if not project_file.is_file():
        print("FAIL: .project/PROJECT.yaml not found", file=sys.stderr)
        sys.exit(1)

    project = load_data(project_file)
    ok = validate(om_root / "schemas" / "PROJECT.v2.schema.json", project_file)

    if not args.skip_om_git_pin_check:
        expected_commit = project.get("governance", {}).get("operating_model", {}).get("commit")
        actual_commit = subprocess.check_output(
            ["git", "-C", str(om_root), "rev-parse", "HEAD"], text=True
        ).strip()
        if expected_commit != actual_commit:
            print(
                f"FAIL: project pins OM commit {expected_commit}, validator checkout is {actual_commit}",
                file=sys.stderr,
            )
            ok = False
        else:
            print(f"PASS: exact OM commit pin {actual_commit}")

    active_locator = project.get("state", {}).get("active", {}).get("locator")
    if not active_locator:
        print("FAIL: PROJECT has no active-state locator", file=sys.stderr)
        ok = False
    elif "://" in active_locator:
        print("FAIL: Git-native conformance workflow requires a repository-local active-state locator", file=sys.stderr)
        ok = False
    else:
        active_file = local_path(project_root, active_locator, "active state")
        ok = validate(om_root / "schemas" / "ACTIVE_STATE.v2.schema.json", active_file) and ok

    external = project.get("external_sources", {}).get("manifest")
    if external:
        if "://" in external:
            print("FAIL: Git-native conformance workflow requires a repository-local external-source manifest", file=sys.stderr)
            ok = False
        else:
            external_file = local_path(project_root, external, "external sources")
            ok = validate(om_root / "schemas" / "EXTERNAL_SOURCES.schema.json", external_file) and ok

    rules = project.get("governance", {}).get("project_rules", {}).get("locator")
    if rules and "://" not in rules:
        try:
            local_path(project_root, rules, "project rules")
            print(f"PASS: project rules locator {rules}")
        except Exception as exc:
            print(f"FAIL: {exc}", file=sys.stderr)
            ok = False

    if not ok:
        sys.exit(1)

    print("PROJECT BOOTSTRAP CONFORMANCE PASS")


if __name__ == "__main__":
    main()
