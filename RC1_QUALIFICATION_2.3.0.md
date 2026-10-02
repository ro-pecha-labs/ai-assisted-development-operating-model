# OM 2.3.0-rc1 — Candidate Qualification

**Status:** RC1 QUALIFICATION PASS (A and C PASS; B not required by owner decision) — NON-CANONICAL
**Candidate identity:** `OM2-2.3.0-RC1`
**Tag:** `om-v2.3.0-rc1` (annotated, tag object `0802e505ca133a88be86c6988ba5b7c1b97a43f3`) -> commit `e70e97dddeab9a3a941b705c6b478a5e982d8472`
**Date:** 2026-10-02

Freeze evidence: `qualification/evidence/OM2-2.3.0-RC1_FREEZE_PASS.json`. No GitHub Release for `om-v2.3.0-rc1` is published at the time of this record.

This record does not make OM 2.3 canonical and does not adopt OM 2.3 in any child project.

## A. Local qualification on the immutable tag

Checkout of `om-v2.3.0-rc1` (`e70e97d`), all 14 `run:` steps of `validate.yml` executed with `bash -eo pipefail`: **14 of 14 steps exit 0** (dependency install, structural contracts, minimal and solo recovery, OM 2.1 policy semantics, release identity pin guard, runtime guard, runtime gate modes, runtime map maintenance, CI usage report qualification, pin reference finder, reusable project bootstrap conformance, invalid bootstrap rejection, uninstantiated DEV template rejection).

- `OM.yaml` declares `2.3.0-rc1` / `non_canonical_candidate`.
- Difference between the qualified development head `57708a0` and the tag: only `OM.yaml`, `README.md`, `00_INDEX.md`, `OM_2.3_PRE_CANDIDATE_QUALIFICATION.md` and the new `CANDIDATE_READINESS_2.3.0_RC1.md`. No normative file, tool, workflow, schema or template differs.
- `git diff om-v2.2.0 om-v2.3.0-rc1` is empty for `.github/workflows/project-state-conformance.yml`, `tools/validate_project_bootstrap.py`, `tools/actions_runtime_gate.py` and `schemas/`: the reusable conformance workflow, the project bootstrap validator, the runtime gate and the schemas are byte-identical to OM 2.2.0.
- Tag-triggered `Validate OM2` run `37011289261` on `e70e97d`: SUCCESS.

## B. Hosted call of the reusable conformance workflow at the tag

**NOT REQUIRED — owner decision.** `CANDIDATE_READINESS_2.3.0_RC1.md` planned one hosted call of `project-state-conformance.yml` at tag `om-v2.3.0-rc1`. The owner decided on 2026-10-02 (in the development session) to record its omission, because the called bytes are identical to OM 2.2.0.

- The reusable workflow validates the **caller repository** root (`python .om/tools/validate_project_bootstrap.py . --om-root .om`), including that the caller's `.project/PROJECT.yaml` pins the exact OM commit of the checked-out tag. The OM repository has no `.project/PROJECT.yaml`, so a call from the OM repository itself would not evidence the candidate; evidencing it needs a never-merged draft pull request in a child repository, as for 2.2.0-rc1.
- `git diff om-v2.2.0 om-v2.3.0-rc1` is empty for `.github/workflows/project-state-conformance.yml`, `tools/validate_project_bootstrap.py`, `tools/actions_runtime_gate.py` and `schemas/` (section A). The hosted call would therefore exercise bytes that were already qualified at `om-v2.2.0` (hosted shadow pilot and tag-bound call of 2.2.0-rc1).
- No hosted call was executed for `om-v2.3.0-rc1`; no child repository was modified.

This is a decision to omit, not a pass of the call. If any of the files above ever differs between a future candidate and `om-v2.2.0`, the hosted call is required again.

## C. Tag-bound tool qualification on a child repository (read-only)

`tools/ci_usage_report.py` at the tag, run read-only over AAE (default branch head `393bc16`, no modification of the repository):

- `static`: `automatic=14, automatic_pr_and_push=3, automatic_without_concurrency=5, automatic_without_timeout=13, automatic_write_capable=2, workflows=22`; exit 0.
- `usage --max-runs 40 --workers 8`: `runs=40 estimated_minutes=42 windows_or_macos_minutes=0 failed_runs=1`; exit 0; wall time about 7 seconds. The pre-pilot sequential implementation needed about 6 minutes for 621 runs of the same repository, which closes known limit 3 of `CANDIDATE_READINESS_2.3.0_RC1.md` (parallel-fetch speed not re-measured) for this sample; full-history timings on DVC and SPC were not re-measured.

## Known limits of this record

1. Section B is not executed; its omission is an owner decision based on byte identity with `om-v2.2.0` (see above).
2. The `usage` timing was measured on a 40-run sample of one repository.
3. No GitHub Release is published; ruleset clauses of tag protection were not verified (see the freeze evidence).

## Verdict

**RC1 qualification: PASS.** Sections A and C pass; section B is not required by the owner decision recorded above. OM 2.3.0 may proceed to GA promotion planning. GA promotion shall preserve the normative bytes and change only release identity and status text, as for OM 2.2.0.

## Non-canonical boundary

Canonical authority remains `om-v2.2.0` (`89de89d0935d61d5442bc8301d9c6c4f2cf7af87`). No child project is migrated by RC1.
