# OM 2.3 — RC1 Candidate Readiness

**Status:** READY_TO_FREEZE — NON-CANONICAL
**Target candidate identity:** `OM2-2.3.0-RC1`
**Target immutable tag:** `om-v2.3.0-rc1`
**Pre-freeze development baseline:** `57708a0a3ee63e8ab5228214c261792bd6d98f41` (`release/om-2.3`, head after the sync of `main` and before this change)

## Purpose

Determine whether the OM 2.3 line is eligible for its first immutable release candidate after completion of Q0–Q4 pre-candidate qualification.

This record does not make OM 2.3 canonical and does not adopt OM 2.3 in any child project.

## Scope of OM 2.3

OM 2.3 is a backward-compatible MINOR release line (target `2.3.0`) introducing CI efficiency guidance for GitHub-hosted DEV CI:

- `platforms/github/CI_EFFICIENCY.md` rules 13–19 (parameterized release-line gates, gate closure at acceptance, write-capable single-use workflows keep their narrow trigger, operating system justified by the claim, bounded jobs, governance state churn as a CI input, measurement), a measurement section and a reference pattern for a consolidated gate;
- `playbooks/CANDIDATE_RELEASE.md` step 14 (gate closure on acceptance);
- `tools/ci_usage_report.py` (`static` and `usage`; read-only, never blocking, exits 0), with qualification fixtures `qualification/ci-usage-report/` and one `validate.yml` step.

CORE, profiles, schemas of project state, templates, `validate_project_bootstrap.py`, the reusable project-state conformance workflow and recovery behavior are unchanged. Conformance pass/fail of any caller is unchanged from 2.2.0.

## Pre-candidate qualification

Q0–Q4: **PASS** (`OM_2.3_PRE_CANDIDATE_QUALIFICATION.md`).

- structural and backward compatibility, conformance behavior unchanged: PASS;
- tool qualification (efficient, wasteful and write-capable fixtures; usage estimate on fixed data; `usage --repo` through an offline `gh` stand-in with parallel fetch and `--max-runs`): PASS;
- read-only shadow pilot on DVC, SPC and AAE (usage estimates agree with an independent computation to within 0.05 %; static report before and after the pilot fixes): PASS;
- negative controls (report never changes a workflow result; pilot repositories unmodified): PASS;
- recovery and all-profile regression (all 14 `validate.yml` run steps, local, `bash -eo pipefail`): PASS.

Work packages merged through protected `release/om-2.3`: PR #48, #51; qualification record PR #52. Owner decisions D1–D4 confirmed on 2026-10-02 (see the pre-candidate record).

## Known limits (do not block RC1)

1. The shadow pilot was read-only API and checkout based; no draft pull requests were opened in child repositories.
2. `usage` is an estimate (job minutes rounded up, Windows x2, macOS x10); the Actions `billable` field reports 0 in the pilot repositories.
3. The `usage` run time after the parallel-fetch fix was not re-measured on the live repositories.
4. `validate.yml` does not run on pushes to release branches; the hosted run on the exact RC1 source SHA is produced by the protected pull request that merges this change.
5. OM's own `validate.yml` triggers on `pull_request`, `push` to `main` and `om-v*` tags and is flagged by the new `static` report under rule 6; it is not changed in 2.3 (decision D4).

## Recurrence and defect disposition

1. Write-capable single-use workflows flagged for missing concurrency by the first tool version (pilot finding) -> rule 15 and the tool exclusion (#51).
2. Slow `usage` over about 3 000 runs (pilot finding) -> parallel job fetch with `--workers` and `--max-runs` (#51).
3. A manual dispatch added to a write-capable single-use workflow cannot requalify a released version and adds a write-capable entry point (found in review of a DVC change) -> rule 15.

No known unresolved recurrence class blocks RC1 freeze.

## Release-safe template qualification

The DEV template is unchanged and still carries explicit non-usable sentinels (`REPLACE_WITH_ADOPTED_IMMUTABLE_OM_REF`, all-zero commit). Project bootstrap conformance rejects them in a real instantiated project (checked by the structural CI step on the uninstantiated template).

## Candidate source identity

This readiness change changes internal OM identity and status text only:

- `OM.yaml`: `2.2.0` -> `2.3.0-rc1`; `accepted_release` -> `non_canonical_candidate`;
- `README.md`, `00_INDEX.md`: 2.3 candidate line (non-canonical);
- `OM_2.3_PRE_CANDIDATE_QUALIFICATION.md`: remaining-items list updated.

No normative semantics, workflow, tool, schema or template is changed in this readiness change.

The exact RC1 source SHA is not known until this change is merged through protected `release/om-2.3`.

## Freeze conditions

RC1 may be frozen only after:

1. this exact readiness change is merged through protected `release/om-2.3`;
2. the resulting exact SHA completes hosted validation = SUCCESS;
3. immutable annotated tag `om-v2.3.0-rc1` is created by the owner on that exact SHA;
4. fresh read-back confirms tag -> exact SHA;
5. tag-triggered hosted validation succeeds;
6. RC1 freeze evidence records exact source/tag/run identity.

If any condition fails, no RC1 PASS claim is made.

## Candidate qualification after freeze

Qualify the exact immutable RC1 identity: structural validation on the tag, all-profile and recovery regression, `ci_usage_report.py` fixtures, one hosted call of the reusable conformance workflow at tag `om-v2.3.0-rc1` (its behavior is unchanged from 2.2.0), and a read-only run of `static` over one child repository.

If RC1 fails, preserve it as immutable failed evidence and remediate in RC2 or later. Do not patch RC1 in place.

## Non-canonical boundary

Canonical authority remains `om-v2.2.0` (exact commit `89de89d0935d61d5442bc8301d9c6c4f2cf7af87`). No child project is migrated by RC1 freeze.
