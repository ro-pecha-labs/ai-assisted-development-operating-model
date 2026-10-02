# OM 2.2 — Qualification Plan

**Status:** DEVELOPMENT / PLAN / NON-CANONICAL  
**Target:** OM 2.2.0 — Actions Runtime Enforcement & Adoption Hygiene (MINOR, `OM_RELEASE_POLICY.md`)  
**Base:** `main` (contains OM 2.1.3 and the post-2.1.1 `platforms/github/CI_EFFICIENCY.md` rules 11–12)  
**Date:** 2026-10-02

Canonical authority remains OM 2.1.3 (`CANONICAL_ADOPTION_2.1.3.md`). This plan is not a release, a candidate or an adoption.

## Origin

- AAE post-adoption review found `actions/download-artifact@v4` (Node.js 20) that the OM 2.1.2 guard did not cover; resolved in OM 2.1.3 (data map of 14 official actions, `UNJUDGED` reporting, non-blocking report step in the reusable conformance workflow).
- OM 2.1.3 only **reports**. A project that wants enforcement has to keep a local guard (AAE does).
- Portfolio adoption of 2.1.3 showed that a pin-asserting test oracle can be missed (DVC `tests/Dvc310.Spa.PcqPrerequisites.Tests.ps1`, found by an automated review, not by the adoption search, because `git grep` in a partial clone does not search missing blobs), and that a project without a hosted conformance caller can keep a non-conformant `ACTIVE_STATE.yaml` unnoticed (Application Factory).
- Today's conformance callers trigger on `.project/**` only, so a workflow-only change that reintroduces a Node.js 20 action is not seen by the reusable workflow.

## Classification

MINOR: backward-compatible optional capability. Default behavior of the reusable workflow does not change; no existing adopter changes result unless it opts in.

## Work packages

### WP1 — Enforce mode

- New input `actions_runtime` of the reusable `project-state-conformance.yml`: `report` (default, current behavior) or `enforce`. Any other value fails the job.
- In `enforce`, the guard step fails when a mapped action is pinned below its Node.js 24 major. `UNJUDGED` official actions and third-party actions stay non-failing (no `strict_unmapped` option in 2.2.0).
- Files: `.github/workflows/project-state-conformance.yml`, `tools/actions_runtime_guard.py` (no change of existing flags), `profiles/DEV.md` (rule 29: optional enforcement), `platforms/github/PROJECT_STATE_CONFORMANCE.md`.

### WP2 — Runtime map maintenance

- Rule in `OM_RELEASE_POLICY.md`: updating `tools/actions_runtime_map.json` to match upstream facts is PATCH-class; `verified_on` is mandatory.
- Advisory, read-only refresh tool that reads upstream `action.yml` and proposes map updates; manual (`workflow_dispatch`), never part of a gate.
- Map schema validation in structural CI.

### WP3 — Adoption hygiene

- `playbooks/ADOPTION_MIGRATION.md`: before adoption, search the **complete** project tree for artifacts that assert the exact OM pin (tests, workflows, vendored schemas, local governance prechecks), and record the result in the adoption record.
- `tools/find_pin_references.py` (read-only): scans a working tree for a ref and commit; fails closed when the repository is a partial clone with missing blobs.

### WP4 — Hosted conformance caller guidance

- `platforms/github/PROJECT_STATE_CONFORMANCE.md`: every Git-native GitHub project should have a hosted conformance caller.
- For enforcement the caller shall also trigger on `.github/workflows/**` (otherwise workflow-only changes are not scanned). Guidance only; no template file in 2.2.0.

### WP5 — Coherence

`OM.yaml` 2.2.0, `README.md`, `00_INDEX.md`, release records. Review of `CI_EFFICIENCY.md` rules 11–12 before RC freeze (they enter the release; they are not changed by this plan).

## Out of scope

Changes to PROJECT / ACTIVE_STATE / EVIDENCE schemas; changing the default to `enforce`; an online resolver in any gate; any change in child repositories; canonical adoption.

## Qualification

| Q | Scope | Expected |
|---|---|---|
| Q0 | Structural and backward compatibility (`tools/validate.py`, `tools/qualify_om21.py`); existing adopters with the default input | unchanged results |
| Q1 | `enforce` with a compliant caller project | PASS |
| Q2 | `enforce` with a Node.js 20 fixture; `report` with the same fixture; invalid input value | enforce FAIL, report PASS, invalid value FAIL |
| Q3 | `UNJUDGED` and third-party semantics | unchanged |
| Q4 | Map schema validation; refresh tool against recorded upstream fixtures (offline, deterministic) | PASS |
| Q5 | `find_pin_references.py`: fixture with an oracle asserting the old pin; fixture simulating a partial clone | finding / fail closed |
| Q6 | Shadow pilot, read-only, no merge: DVC (worst case, ~212 Node.js 20 references) and AAE (clean) with `enforce` and `report` on shadow branches | DVC enforce fails with a list, AAE passes, report passes in both |
| Q7 | Recovery and all-profile regression on existing qualification fixtures | unchanged |

Q6 needs explicit authorization to push a shadow branch to each pilot repository; nothing is merged.

## Release sequence

1. Protected PRs into `release/om-2.2`; structural CI green.
2. RC1: annotated tag `om-v2.2.0-rc1` on the exact commit, `tools/release_identity_guard.py` PASS, RC qualification record (Q0–Q7).
3. Acceptance review and GA promotion plan; no byte changes between RC and GA.
4. Tag `om-v2.2.0` on the same bytes, tag-bound validation, GitHub Release, `ACCEPTANCE_2.2.0.md`, merge back to `main`.
5. Canonical adoption as a separate explicit decision.

## Adoption after GA (non-binding)

Projects adopt at their own safe boundary. `enforce` is opt-in after a project has migrated its Node.js 20 references: APC, AAE, DAE and Application Factory immediately; SPC after its connected-mutation gates; DVC after its workflow migration. AAE may then retire its local guard.

## Decisions taken for this plan

- Input shape `actions_runtime: report|enforce`, no `strict_unmapped`.
- `CI_EFFICIENCY.md` rules 11–12 are reviewed before RC freeze.
- Hosted caller template is guidance in `platforms/github/PROJECT_STATE_CONFORMANCE.md`, not a template file.
