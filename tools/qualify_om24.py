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

if failed:
    sys.exit(1)

print("OM 2.4 POLICY QUALIFICATION PASS")
