from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
DISPOSITIONS = {"fixed", "rejected_with_reason", "deferred"}


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def classify_ai_review(c):
    """Deterministic reading of playbooks/AI_REVIEW_AUDIT.md (items 1-9)."""
    if c["presented_as_human_acceptance"]:
        return "FAIL_PRESENTED_AS_HUMAN_ACCEPTANCE"
    if not (c["clean_context"] and c["brief_fixed"] and c["scope_is_difference"]):
        return "FAIL_INDEPENDENCE"
    if not c["read_only_verified"]:
        return "FAIL_NOT_READ_ONLY"
    if not c["output_stored_unchanged_before_reaction"]:
        return "FAIL_OUTPUT_NOT_PRESERVED"
    findings = c["findings"]
    for f in findings:
        d = f.get("disposition")
        if d not in DISPOSITIONS:
            return "BLOCKED_FINDING_DISPOSITION"
        if d == "rejected_with_reason" and not f.get("reason"):
            return "BLOCKED_FINDING_DISPOSITION"
    if findings and not c["dispositions_human_approved"]:
        return "BLOCKED_FINDING_DISPOSITION"
    ev = c["evidence"]
    if not all(ev.get(k) for k in ("model", "scope", "counts_by_severity", "link", "human_self_review_line")):
        return "BLOCKED_EVIDENCE_INCOMPLETE"
    if c["material_fix"] and not c["review_repeated_after_fix"]:
        return "BLOCKED_REVIEW_NOT_REPEATED"
    return "PASS"


def check_common_rules_consistency():
    """Q5: the layers/applicability tables of COMMON_RULES.md agree with the manifest, the profiles and the rule texts."""
    import re
    import yaml

    text = (ROOT / "COMMON_RULES.md").read_text(encoding="utf-8")
    manifest = yaml.safe_load((ROOT / "OM.yaml").read_text(encoding="utf-8"))
    profiles = list(manifest["profiles"])
    problems = []

    defined = set(re.findall(r"^([UD]\d+)\. ", text, flags=re.MULTILINE))
    table = text[text.index("## Profile applicability"):]
    rows = [ln for ln in table.splitlines() if ln.startswith("|")]
    header = [c.strip() for c in rows[0].strip("|").split("|")]
    if header[1:] != profiles:
        problems.append(f"applicability columns {header[1:]} differ from manifest profiles {profiles}")
    listed = set()
    for ln in rows[2:]:
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) != len(profiles) + 1:
            problems.append(f"row has {len(cells)} cells: {ln}")
            continue
        for label in re.findall(r"[UDG]\d*", cells[0]):
            listed.add(label)
        if not all(re.match(r"(yes|no|optional|with|only)", v) for v in cells[1:]):
            problems.append(f"unexpected cell value in row: {ln}")
    for item in sorted(defined - listed):
        problems.append(f"{item} is defined but missing in the applicability table")
    for item in sorted(listed - defined - {"G"}):
        problems.append(f"{item} is in the applicability table but not defined")
    if "## Section G" not in text:
        problems.append("section G missing")

    dev = (ROOT / "profiles/DEV.md").read_text(encoding="utf-8")
    dev_max = max(int(n) for n in re.findall(r"^(\d+)\. \*\*", dev, flags=re.MULTILINE))
    for doc in ("COMMON_RULES.md", "playbooks/AI_REVIEW_AUDIT.md", "platforms/git_local/README.md"):
        body = (ROOT / doc).read_text(encoding="utf-8")
        for n in re.findall(r"\bDEV (\d+)\b", body):
            if not 1 <= int(n) <= dev_max:
                problems.append(f"{doc}: DEV {n} does not exist (DEV has {dev_max} rules)")

    contract = {
        "CORE.md": ("invariant", "exception"),
        "profiles/DEV.md": ("invariant", "exception"),
        "COMMON_RULES.md": ("invariant", "exception"),
        "templates/DEV/.project/DEVELOPMENT_RULES.md": ("invariant", "exception"),
    }
    for doc, words in contract.items():
        body = (ROOT / doc).read_text(encoding="utf-8").lower()
        for w in words:
            if w not in body:
                problems.append(f"{doc} does not mention '{w}'")

    for p in problems:
        print(f"FAIL: common rules consistency: {p}")
    if not problems:
        print(f"PASS: common rules consistency ({len(defined)} rules, {len(profiles)} profiles, DEV references within 1-{dev_max})")
    return bool(problems)


def run(path, schema, fn):
    doc = load(path)
    if doc.get("schema") != schema:
        raise AssertionError(f"{path}: unexpected schema {doc.get('schema')}")
    failed = False
    for c in doc["cases"]:
        actual = fn(c)
        ok = actual == c["expected"]
        print(f"{'PASS' if ok else 'FAIL'}: {path}:{c['id']} expected={c['expected']} actual={actual}")
        failed |= not ok
    return failed


failed = run("qualification/om2.4/ai_review_audit_cases.json", "om24.ai-review-audit-cases/v1", classify_ai_review)
failed |= check_common_rules_consistency()

if failed:
    sys.exit(1)

print("OM 2.4 POLICY QUALIFICATION PASS")
