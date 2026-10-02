# OM 2.2 — Pre-Candidate Qualification Status

**Status:** PRE-CANDIDATE / Q0–Q5 AND Q7 PASS / Q6 PENDING / NOT READY FOR CANDIDATE-READINESS REVIEW  
**Development head:** `ae9217c23a1adacbee9fa6b20887574904286670` (`release/om-2.2`)  
**Date:** 2026-10-02

## Scope

Development target: `2.2.0-dev — Actions Runtime Enforcement & Adoption Hygiene` (MINOR). Plan: `OM_2.2_QUALIFICATION_PLAN.md`.

Current canonical authority remains `om-v2.1.3`. This record does not freeze a candidate, does not make OM 2.2 canonical and does not adopt it in any child project. `OM.yaml` still declares `2.1.3`; the release identity is promoted at candidate readiness (`2.2.0-rc1`, non-canonical candidate) and at GA (`2.2.0`), as for OM 2.1.

## Work packages (merged into `release/om-2.2`)

| WP | PR | Merge commit | Hosted `Validate OM2` run on the PR head |
|---|---|---|---|
| Plan | #36 | `fd9485948651c944a75e054fb477d0a4e352cd09` | `36995700865` SUCCESS (`782ea07`) |
| WP1 enforce mode | #37 | `76262ff32520550ddaaf899b882a9f262f37ffcc` | `36996401952` SUCCESS (`2ed6cc0`) |
| WP3 pin reference finder | #38 | `d8f27d474f53487612c8a4b26e54b81ebbce865e` | `36996731895` SUCCESS (`9d2b021`) |
| WP4 hosted caller guidance | #39 | `6ca3bb3dd52a3a8df8f5f8a8280cde8be16021c8` | `36997081238` SUCCESS (`357b1c8`) |
| WP2 runtime map maintenance | #40 | `ae9217c23a1adacbee9fa6b20887574904286670` | `36997423995` SUCCESS (`5e87e06`) |

## Q0 — Structural and backward compatibility

**PASS.** `tools/validate.py` and `tools/qualify_om21.py` pass; the reusable workflow keeps the non-failing default (`actions_runtime: report`, input not required), asserted in structural CI; project bootstrap conformance fixtures (valid, invalid, uninstantiated DEV template) behave as in 2.1.3.

## Q1–Q3 — Enforce mode

**PASS.** Structural CI step "Qualify GitHub Actions runtime gate modes": enforce passes a compliant workflow (Q1); enforce rejects a Node.js 20 workflow, report does not, an invalid mode fails (Q2); `UNJUDGED` official actions never fail in either mode (Q3). The step logic of the reusable workflow was additionally simulated in eight situations, including a fail-closed `enforce` against an adopted OM revision without the gate.

Not yet evidenced: a hosted run of the reusable workflow in `enforce` mode (Q6).

## Q4 — Runtime map maintenance

**PASS.** The map and fixture maps are valid against `schemas/ACTIONS_RUNTIME_MAP.v1.schema.json`; five invalid maps (missing `verified_on`, bad date, non-integer major, empty, non-official key) are rejected; the advisory refresh tool reports no difference / DIFF / UNRESOLVED against recorded upstream fixtures, proposes without writing, and fails with exit 2 on usage and map errors. A live read-only run against upstream on 2026-10-02 found all 14 mapped actions `OK` (no differences).

Not yet evidenced: a hosted run of the manual refresh workflow (the same command was run locally).

## Q5 — Pin reference finder

**PASS.** Structural CI step "Qualify pin reference finder": a pin-asserting test oracle is found; exclusions are counted; a clean repository is reported with its scanned path count; a sparse checkout omitting the oracle from the working tree is found by the revision scan (a working-tree search misses it); a partial clone fails closed; usage errors and an unresolvable revision fail closed. A real partial clone of a portfolio project failed closed as designed.

## Q6 — Shadow pilot

**PENDING.** Read-only pilot on shadow branches without merge: DVC (worst case, about 212 Node.js 20 references) and AAE (clean) with `enforce` and `report`. Requires explicit authorization to push a shadow branch to each pilot repository.

## Q7 — Recovery and all-profile regression

**PASS.** Minimal and solo recovery qualification, OM 2.1 policy semantics, release identity pin guard and all-profile contract checks pass on the development head (all steps of `validate.yml` run locally with `bash -eo pipefail`: 0 failures).

## Disposition of `CI_EFFICIENCY.md` rules 11–12

Rules 11 and 12 entered `main` after OM 2.1.1 and were excluded from the PATCH releases; they enter OM 2.2.0 for the first time and were reviewed against the 2.2 scope.

- Rule 11 (cumulative qualification at the candidate/checkpoint boundary): consistent. OM's own `validate.yml` runs on pull requests and `om-v*` tags only; the new 2.2 steps are lightweight structural checks.
- Rule 12 (retire closed lifecycle gates from automatic execution): consistent. The only new workflow, `actions-runtime-map-refresh.yml`, is manual (`workflow_dispatch`); the enforcing caller recommended in `PROJECT_STATE_CONFORMANCE.md` is path-scoped to `.project/**` and `.github/workflows/**`, a documented current control purpose.
- No change to the rules is required for 2.2.0. The document keeps its existing status (`PROSPECTIVE DEVELOPMENT POLICY`).

## Manifest decision

The new schema `schemas/ACTIONS_RUNTIME_MAP.v1.schema.json` is **not** added to `OM.yaml`. The manifest `schemas` section lists the project-facing contracts and `tools/validate.py` requires it to match the expected set exactly; the runtime map is a tooling artifact validated in structural CI.

## Remaining before candidate readiness

1. Q6 shadow pilot (needs authorization).
2. Candidate readiness record, release identity promotion to `2.2.0-rc1` and README/index status for the candidate.
3. Immutable RC tag, created by the owner, and RC qualification record.
