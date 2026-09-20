from pathlib import Path
import argparse, json, sys
import yaml

def recover(root: Path):
    project_path = root / "PROJECT.yaml"
    state_path = root / "ACTIVE_STATE.yaml"

    project = yaml.safe_load(project_path.read_text(encoding="utf-8"))
    state = yaml.safe_load(state_path.read_text(encoding="utf-8"))

    if project["project"]["profile"] != "DEV":
        raise ValueError("Recovery fixture must use DEV profile.")
    if project["state"]["active"] != ".project/ACTIVE_STATE.yaml":
        raise ValueError("Unexpected active-state contract.")

    active = state["active_work"]
    live = []
    if "issue" in active:
        live.append(f"issue:{active['issue']}")
    if "branch" in active:
        live.append(f"branch:{active['branch']}")
    if "pull_request" in active:
        live.append(f"pull_request:{active['pull_request']}")

    result = {
        "bootstrap_files_read": 2,
        "project_id": project["project"]["id"],
        "profile": project["project"]["profile"],
        "objective_id": state["objective"]["id"],
        "trusted_baseline_ref": state["trusted_baseline"]["ref"],
        "active_branch": active.get("branch"),
        "live_queries_required": live,
        "legacy_handoff_required": False,
        "historical_reconstruction_required": False,
    }
    return result

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
