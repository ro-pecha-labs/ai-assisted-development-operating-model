# OM 2.0 — Formal Candidate Readiness RC2

**Status:** READY_TO_FREEZE — NON-CANONICAL  
**Target candidate identity:** `OM2-2.0.0-RC2`  
**Target immutable tag:** `om-v2.0.0-rc2`  
**Predecessor:** `OM2-2.0.0-RC1` — FAILED_QUALIFICATION / PRODUCT / NOT_ACCEPTED / DO_NOT_MODIFY

## Purpose

Determine whether the successor OM 2.0 line is eligible for immutable RC2 freeze after the RC1 cross-profile PRODUCT failure.

This record does not make OM 2.0 canonical and does not authorize SPC adoption.

## RC1 disposition and root-cause closure

RC1 remains immutable failed evidence at:

- tag `om-v2.0.0-rc1`;
- commit `fbb591711ca124ba7dc16914ab4e7a9d176aae4d`.

RC1 failed because its machine contracts encoded Git-native DEV semantics as universal requirements.

The successor closes that root cause prospectively:

- PROJECT v2 uses a generic Git-or-external `control_plane`;
- ACTIVE_STATE v2 uses generic baseline identity/revision and active-work locators;
- EVIDENCE_RECORD v2 uses generic subject identity and typed revision;
- Git-specific requirements remain in the DEV profile/template;
- historical v1 schemas remain present for RC1 interpretation and are not redefined.

## Cross-profile pre-freeze qualification

PASS.

Before RC2 freeze, hosted qualification covers all five profiles:

- DEV — Git control plane, Git baseline, branch/PR/issue style live pointers;
- SOLUTION — external SharePoint control plane, solution decision/review state, non-Git acceptance evidence;
- DOCUMENT — Google Drive authority, document revision/review state, document approval evidence;
- EXPERIMENT — external OneDrive authority, hypothesis/run state, experiment conclusion evidence;
- LIGHT — external Google Drive authority and minimal persistent work state.

Negative controls prove:

- inconsistent external/Git control-plane declaration is rejected;
- undeclared ACTIVE_STATE history is rejected;
- unclassified FAIL evidence is rejected.

The semantic review is recorded in `CROSS_PROFILE_QUALIFICATION.md`.

## DEV parity regression qualification

PASS.

After generalizing the v2 evidence subject, candidate-readiness regression review found that v1 DEV evidence capabilities for artifacts, semantic plans and durable evidence archives had been omitted.

They were restored before RC2 freeze.

Current EVIDENCE_RECORD v2 supports:

- profile-neutral subject identity + typed revision;
- `artifacts[]` with digest identity;
- `plan.semantic_digest`;
- `plan.authorized_operations`;
- `evidence_archive` with digest identity.

A positive `mutation_execution` fixture verifies the combined structure.

The review is recorded in `DEV_PARITY_QUALIFICATION.md`.

## Existing qualification lineage

- M0 — DEV Kernel Bootstrap: PASS.
- M1 — GitHub Control Plane: PASS.
- M2 — Recovery Qualification: PASS.
- M3 — real SPC Shadow Recovery Pilot: PASS.
- RC1 freeze integrity: PASS.
- RC1 tag-bound structural validation: PASS.
- RC1 cross-profile semantic qualification: FAIL / PRODUCT.
- RC1 failure evidence: durable and preserved.
- v2 successor structural qualification: PASS.
- v2 cross-profile qualification: PASS.
- v2 DEV evidence parity qualification: PASS.

## Lessons / recurrence disposition

Material lesson classes have executable or durable controls:

1. authority freshness drift → Recovery, External Source Mismatch and Adoption/Migration playbooks;
2. incomplete universal surface → manifest-enforced profile/playbook completeness;
3. schema escaping/path defect → positive/negative contract fixtures;
4. candidate-history hot-path pressure → lazy conditional candidate-safety reads;
5. RC1 Git-overreach → universal v2 contracts + DEV specialization + cross-profile tests before freeze;
6. v2 DEV evidence regression → explicit mutation-evidence parity fixture and hosted validation.

No unresolved recurrence class is known to block RC2 freeze.

## Platform integrity

The GitHub organization ruleset for `main` is Active and requires:

- pull request before merge;
- `structural-validation`;
- strict up-to-date policy;
- no deletion;
- no non-fast-forward update;
- no bypass actor.

The version-tag ruleset is Active for `refs/tags/om-v*` and blocks:

- deletion;
- update.

There are no bypass actors and the current user cannot bypass it.

## Candidate source identity

This readiness change intentionally changes the internal OM version from development `2.0.0-dev.7` to candidate `2.0.0-rc2` with status `non_canonical_candidate`.

The exact candidate source commit is not known until this readiness change is merged through protected `main`.

## Freeze condition

RC2 may be frozen only after:

1. this exact candidate-ready source is merged through protected `main`;
2. the resulting exact `main` SHA completes hosted `structural-validation = SUCCESS`;
3. `om-v2.0.0-rc2` is created on that exact SHA;
4. fresh read-back confirms tag → exact SHA and active immutable-tag rules;
5. tag-triggered hosted validation on `om-v2.0.0-rc2` succeeds.

Until the physical tag exists and is read back, status remains READY_TO_FREEZE.

## Non-canonical boundary

Canonical Operating Model remains v1.6.

SPC remains governed by OM v1.6.

RC2 freeze does not itself authorize OM2 canonical adoption or SPC migration.
