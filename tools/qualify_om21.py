from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def classify_release(c):
    formal = any([
        c["connected_mutation"],
        c["destructive_or_prod"],
        c["formal_downstream_adoption"],
        c["governed_external_distribution_requires_candidate"],
        c["project_policy_requires_formal"],
    ])
    return "formal" if formal else "lightweight"

def classify_solo(c):
    if c["claim_independent_human_review"] and not c["second_human_approved"]:
        return "FAIL_FALSE_HUMAN_REVIEW_CLAIM"
    if c["external_two_person_required"] and not c["second_human_approved"]:
        return "BLOCKED_EXTERNAL_CONTROL"
    if c["human_authorization_required"] and not c["human_authorized"]:
        return "BLOCKED_HUMAN_AUTHORIZATION"
    if c["material_change"] and not c["human_self_review"]:
        return "BLOCKED_HUMAN_SELF_REVIEW"
    return "PASS"

def classify_ai(c):
    if c["oracle_weakened"]:
        return "FAIL_ORACLE_INTEGRITY"
    if not c["applicable_checks_pass"]:
        return "BLOCKED_CHECKS"
    if c["protected_surface"] and not c["heightened_review"]:
        return "BLOCKED_HEIGHTENED_REVIEW"
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

failed = False
failed |= run("qualification/om2.1/dev_release_cases.json", "om21.dev-release-cases/v1", classify_release)
failed |= run("qualification/om2.1/solo_assurance_cases.json", "om21.solo-assurance-cases/v1", classify_solo)
failed |= run("qualification/om2.1/ai_development_cases.json", "om21.ai-development-cases/v1", classify_ai)

if failed:
    sys.exit(1)

print("OM 2.1 POLICY QUALIFICATION PASS")
