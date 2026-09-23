# OM 2.1 — Qualification Plan

**Status:** DEVELOPMENT / PRE-CANDIDATE / NON-CANONICAL

## Proposed target

OM 2.1.0 — Solo Assurance & Proportional DEV

## Q0 — Structural/backward compatibility

- PROJECT v2 remains valid for projects without `assurance`.
- Optional `assurance.mode` accepts `standard` and `solo` only.
- Existing five profiles remain unchanged as the complete primary-profile set.
- Existing ACTIVE_STATE, EXTERNAL_SOURCES and EVIDENCE_RECORD contracts remain readable.

## Q1 — Solo cross-profile qualification

Positive fixtures for:

- DEV + solo;
- SOLUTION + solo;
- DOCUMENT + solo;
- EXPERIMENT + solo;
- LIGHT + solo.

Negative fixture:

- invalid assurance mode rejected.

Verify solo mode does not change authority, mutation, destructive or historical-integrity semantics.

## Q2 — DEV release-mode qualification

Scenario review:

- low-risk internal utility may use lightweight release;
- connected mutation binding requires formal;
- PROD/destructive scope requires formal;
- formal downstream adoption requires formal;
- project-specific policy may force formal;
- lightweight release still binds immutable source/release identity and applicable CI.

## Q3 — AI development/evidence qualification

Verify:

- implementation agent cannot weaken protected oracle surfaces solely to get PASS;
- machine-verifiable PASS is bound to underlying execution/artifact evidence when available;
- AI review is not represented as independent human approval;
- material/protected surface review triggers are bounded.

## Q4 — Recovery regression

Existing minimal PROJECT + ACTIVE_STATE recovery remains sufficient.
Solo assurance does not add an always-hot recovery document.
Triggered playbooks remain lazy-loaded.

## Q5 — Representative shadow pilot

**PASS**

Initial portfolio audit on 2026-09-23 found structural project-state drift in DVC, DAE, AAE and SPC and was preserved as **FAIL / CONTROL_IMPLEMENTATION** in `OM_2.1_Q5_PORTFOLIO_SHADOW_FINDING.md`.

Corrective OM 2.1 control:

- reusable project-bootstrap validator;
- reusable GitHub project-state conformance workflow;
- DEV rule for ongoing path-scoped conformance.

Successor representative pilot used SPC from live `main` commit `599dadc8cc01af419ecf2178e70c31a539d9008c` in a non-authoritative shadow branch.

The first shadow run correctly exposed two over-length `EXTERNAL_SOURCES.purpose` values while PROJECT, exact OM pin and bounded ACTIVE_STATE already passed. The shadow-only text was reconciled without changing source locator, authority or pin semantics.

Successor run `35839945652` at SPC shadow commit `fb8157ce16f627170520747de2d35c1e8c9ea26d` passed both:

- reusable project-state conformance;
- bounded solo recovery.

Recovery read exactly two bootstrap files totaling 2,584 bytes, recovered `assurance_mode=solo`, the exact SPC 1.3.0 trusted baseline, and required neither legacy handoff nor historical reconstruction.

See `OM_2.1_Q5_SPC_SHADOW_ACCEPTANCE.md`.

The shadow branch is qualification evidence only and is not merged into SPC `main`; no SPC OM 2.1 adoption is implied.

## Candidate gate

Do not freeze OM 2.1 RC until Q0-Q5 are PASS or any non-applicable gate is explicitly justified.

A failed RC remains immutable and is not patched in place.
