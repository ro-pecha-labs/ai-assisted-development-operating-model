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


# Expected applicability per rule and profile (first word of the cell), in manifest profile order:
# DEV, SOLUTION, DOCUMENT, EXPERIMENT, LIGHT. This is the applicability contract of COMMON_RULES.md.
EXPECTED_APPLICABILITY = {
    "U1": ["yes", "yes", "yes", "yes", "yes"],
    "U2": ["yes", "yes", "yes", "yes", "yes"],
    "U3": ["yes", "yes", "yes", "yes", "yes"],
    "U4": ["yes", "yes", "yes", "yes", "yes"],
    "U5": ["yes", "yes", "yes", "optional", "optional"],
    "D1": ["yes", "no", "no", "optional", "no"],
    "D2": ["optional", "optional", "optional", "no", "no"],
    "G": ["yes", "with", "with", "no", "no"],
}

# Normative clauses that bound exceptions by the invariants (lowercase, whitespace-normalized).
INVARIANT_CLAUSES = {
    "CORE.md": ("no lower layer may weaken an invariant",),
    "profiles/DEV.md": ("no exception may touch an om invariant",),
    "COMMON_RULES.md": ("shall not touch an invariant", "no layer below core may weaken"),
    "templates/DEV/.project/DEVELOPMENT_RULES.md": ("shall not touch an om invariant",),
}
DOCS = ("CORE.md", "profiles/DEV.md", "COMMON_RULES.md", "templates/DEV/.project/DEVELOPMENT_RULES.md",
        "playbooks/AI_REVIEW_AUDIT.md", "platforms/git_local/README.md")


def read_docs():
    return {d: (ROOT / d).read_text(encoding="utf-8") for d in DOCS}


def common_rules_problems(docs):
    """Q5: the layers/applicability contract of COMMON_RULES.md agrees with the manifest, the profiles and the rule texts."""
    import re
    import yaml

    text = docs["COMMON_RULES.md"]
    manifest = yaml.safe_load((ROOT / "OM.yaml").read_text(encoding="utf-8"))
    profiles = list(manifest["profiles"])
    problems = []

    defined = set(re.findall(r"^([UD]\d+)\. ", text, flags=re.MULTILINE))
    table = text[text.index("## Profile applicability"):]
    rows = [ln for ln in table.splitlines() if ln.startswith("|")]
    header = [c.strip() for c in rows[0].strip("|").split("|")]
    if header[1:] != profiles:
        problems.append(f"applicability columns {header[1:]} differ from manifest profiles {profiles}")
    listed = {}
    for ln in rows[2:]:
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) != len(profiles) + 1:
            problems.append(f"row has {len(cells)} cells: {ln}")
            continue
        values = [c.split()[0].lower() if c.split() else "" for c in cells[1:]]
        for label in re.findall(r"[UDG]\d*", cells[0]):
            listed[label] = values
    for item in sorted(defined - set(listed)):
        problems.append(f"{item} is defined but missing in the applicability table")
    for item in sorted(set(listed) - defined - {"G"}):
        problems.append(f"{item} is in the applicability table but not defined")
    if "## Section G" not in text:
        problems.append("section G missing")
    for item, expected in EXPECTED_APPLICABILITY.items():
        if item in listed and listed[item] != expected:
            problems.append(f"{item} applicability {listed[item]} differs from the contract {expected}")
    for item in sorted(set(listed) - set(EXPECTED_APPLICABILITY)):
        problems.append(f"{item} has no expected applicability in the contract")

    dev = (ROOT / "profiles/DEV.md").read_text(encoding="utf-8")
    dev_max = max(int(n) for n in re.findall(r"^(\d+)\. \*\*", dev, flags=re.MULTILINE))
    for doc in ("COMMON_RULES.md", "playbooks/AI_REVIEW_AUDIT.md", "platforms/git_local/README.md"):
        for n in re.findall(r"\bDEV (\d+)\b", docs[doc]):
            if not 1 <= int(n) <= dev_max:
                problems.append(f"{doc}: DEV {n} does not exist (DEV has {dev_max} rules)")

    for doc, clauses in INVARIANT_CLAUSES.items():
        body = " ".join(docs[doc].lower().split())
        for clause in clauses:
            if clause not in body:
                problems.append(f"{doc} lacks the clause '{clause}'")
        if re.search(r"(?<!no )exceptions? (may|can|shall be allowed to) (touch|weaken|override)", body):
            problems.append(f"{doc} allows an exception to touch or weaken an invariant")
    return problems, len(defined), len(profiles), dev_max


def check_common_rules_consistency():
    problems, n_rules, n_profiles, dev_max = common_rules_problems(read_docs())
    for p in problems:
        print(f"FAIL: common rules consistency: {p}")
    if not problems:
        print(f"PASS: common rules consistency ({n_rules} rules, {n_profiles} profiles, applicability contract, "
              f"invariant clauses, DEV references within 1-{dev_max})")
    return bool(problems)


def check_common_rules_negative_controls():
    """Each mutation of the documents shall be detected by the consistency check."""
    mutations = {
        "D1 not applicable to DEV": ("COMMON_RULES.md", "| D1 | yes |", "| D1 | no |"),
        "universal rule optional": ("COMMON_RULES.md", "| U1, U2, U3 | yes |", "| U1, U2, U3 | optional |"),
        "exception may weaken an invariant": ("COMMON_RULES.md", "shall not touch an invariant", "may touch an invariant, and an exception may weaken it"),
        "DEV rule rewritten to allow exceptions": ("profiles/DEV.md", "no exception may touch an OM invariant", "an exception may touch an OM invariant"),
        "reference to a non-existent DEV rule": ("COMMON_RULES.md", "see DEV 8", "see DEV 99"),
    }
    failed = False
    for name, (doc, old, new) in mutations.items():
        docs = read_docs()
        if old not in docs[doc]:
            print(f"FAIL: negative control '{name}': pattern not found in {doc}")
            failed = True
            continue
        docs[doc] = docs[doc].replace(old, new, 1)
        problems = common_rules_problems(docs)[0]
        print(f"{'PASS' if problems else 'FAIL'}: negative control '{name}' {'detected' if problems else 'NOT detected'}")
        failed |= not problems
    return failed


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
failed |= check_common_rules_negative_controls()

if failed:
    sys.exit(1)

print("OM 2.4 POLICY QUALIFICATION PASS")
