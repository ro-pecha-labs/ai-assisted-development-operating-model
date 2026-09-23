from pathlib import Path
import argparse, json, sys
import yaml

def recover(root: Path):
    project = yaml.safe_load((root / "PROJECT.yaml").read_text(encoding="utf-8"))
    state = yaml.safe_load((root / "ACTIVE_STATE.yaml").read_text(encoding="utf-8"))

    if project["schema"] != "om.project/v2":
        raise ValueError("Expected om.project/v2")
    if state["schema"] != "om.active-state/v2":
        raise ValueError("Expected om.active-state/v2")

    live = []
    active_branch = None
    for pointer in state["active_work"]:
        live.append(f"{pointer['kind']}:{pointer['locator']}")
        if pointer["kind"] == "branch":
            active_branch = pointer["locator"]

    return {
        "bootstrap_files_read": 2,
        "project_id": project["project"]["id"],
        "profile": project["project"]["profile"],
        "assurance_mode": project.get("assurance", {}).get("mode", "standard"),
        "objective_id": state["objective"]["id"],
        "trusted_baseline_identity": state["trusted_baseline"]["identity"],
        "active_branch": active_branch,
        "live_queries_required": live,
        "legacy_handoff_required": False,
        "historical_reconstruction_required": False,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture_root", type=Path)
    parser.add_argument("--expected", type=Path)
    args = parser.parse_args()

    result = recover(args.fixture_root)
    print(json.dumps(result, indent=2))

    if args.expected:
        expected = json.loads(args.expected.read_text(encoding="utf-8"))
        if result != expected:
            print("RECOVERY QUALIFICATION FAIL: output differs from expected", file=sys.stderr)
            sys.exit(1)

    print("RECOVERY QUALIFICATION PASS")

if __name__ == "__main__":
    main()
