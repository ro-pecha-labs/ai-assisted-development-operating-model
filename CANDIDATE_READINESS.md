# OM 2.0 — Formal Candidate Readiness

**Status:** READY_TO_FREEZE — NON-CANONICAL  
**Target candidate identity:** `OM2-2.0.0-RC1`  
**Target immutable tag:** `om-v2.0.0-rc1`

## Scope

This record determines whether the current OM 2.0 development line is eligible for formal immutable candidate freeze. It does not make OM 2.0 canonical and does not authorize SPC adoption.

## Qualified development evidence

- M0 — DEV Kernel Bootstrap: PASS.
- M1 — GitHub Control Plane: PASS.
- M2 — Recovery Qualification: PASS.
- M3 — real SPC Shadow Recovery Pilot: PASS.
- Protected-main development path: qualified.
- Required `structural-validation`: qualified.
- Real SPC recovery matched reconciled authoritative OM v1.6 state.
- Real recovery used approximately 10 kB static OM2 material versus approximately 46.5 kB for the compared OM v1.6 R0 subset before the full canonical OM document.

## Universal contract completeness

The development manifest contains:

- one universal CORE;
- five profiles: DEV, SOLUTION, DOCUMENT, EXPERIMENT, LIGHT;
- eight triggered playbooks;
- four machine contracts: PROJECT, ACTIVE_STATE, EXTERNAL_SOURCES and EVIDENCE_RECORD.

Normal recovery remains lazy-loaded: CORE + active profile + only triggered playbooks.

## Lessons / recurrence disposition

Material lesson classes found during rebaseline have been generalized:

1. authority freshness drift → Recovery, External Source Mismatch and Adoption/Migration playbooks;
2. missing universal surfaces → manifest-enforced profile/playbook completeness;
3. schema path escaping defect → positive and negative fixtures plus CI contract validation;
4. candidate-history hot-path pressure → conditional candidate-safety reads instead of always-hot candidate history.

No unresolved recurrence class blocks freeze.

## PCQ / test-the-tests

The exact development line uses hosted CI to validate:

- positive PROJECT fixture;
- negative invalid project-rules path;
- positive and negative ACTIVE_STATE fixtures;
- positive and negative EXTERNAL_SOURCES fixtures;
- positive PASS EvidenceRecord;
- positive classified FAIL EvidenceRecord;
- negative unclassified FAIL EvidenceRecord;
- manifest CORE path;
- exact five-profile set and physical paths;
- exact eight-playbook set and physical paths;
- exact four-schema set and physical paths;
- PROJECT profile enum = manifest profiles;
- README/index version = OM.yaml version;
- CORE declares all manifest profiles.

The hardening PR and the exact post-merge `main` commit both passed hosted validation before this readiness record was prepared.

## Candidate identity control

GitHub organization ruleset `OM2 version tags` is active for `refs/tags/om-v*`.

It blocks:

- tag deletion;
- tag update.

There are no bypass actors and the current user cannot bypass the rule.

The formal candidate shall therefore be frozen only by creating `om-v2.0.0-rc1` on the exact candidate-eligible commit. A branch is not an equivalent substitute.

## Freeze condition

After this readiness record is merged through protected `main` and the resulting exact `main` commit passes hosted `structural-validation`, that resulting commit is eligible to become `OM2-2.0.0-RC1`.

Formal freeze requires creation and read-back of the immutable tag:

`om-v2.0.0-rc1`

Until that tag physically exists, status remains READY_TO_FREEZE rather than FROZEN.

## Non-canonical boundary

Canonical Operating Model remains v1.6 until a separate explicit prospective adoption decision.

SPC remains governed by OM v1.6. No SPC authority migration is authorized by candidate freeze.
