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

Use one real portfolio DEV project at a clean boundary without changing its current OM authority.

Measure:

- recovery surface;
- additional AI context from solo mode;
- review overhead;
- CI overhead;
- lightweight/formal release classification usability.

## Candidate gate

Do not freeze OM 2.1 RC until Q0-Q5 are PASS or any non-applicable gate is explicitly justified.

A failed RC remains immutable and is not patched in place.
