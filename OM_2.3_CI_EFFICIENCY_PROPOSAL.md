# OM 2.3 — CI Efficiency Portfolio Rules (PROPOSAL)

**Status:** DRAFT — NON-CANONICAL, not adopted by any project
**Proposed release class:** MINOR (`OM_RELEASE_POLICY.md`): new normative guidance for GitHub-hosted DEV CI
**Proposed base:** `om-v2.2.0`

## Why

A read-only portfolio audit (2026-10-02, period 2026-09-18 to 2026-10-02) of six child repositories estimated about 11 200 CI minutes. Two repositories account for 83 %. The estimate uses job durations rounded up to whole minutes, Windows x2; the Actions `billable` field reported 0.

| Repository | Automatic / total workflows | Estimated minutes | Windows share |
|---|---|---|---|
| DVC | 29 / 159 | 4 842 | 36 % |
| SPC | 8 / 27 | 4 441 | 19 % |
| AAE | 14 / 22 | 1 834 | 74 % |
| APC | 1 / 1 | 51 | 0 % |
| DAE | 2 / 2 | 23 | 0 % |

Patterns that repeated across repositories and are not yet covered by `platforms/github/CI_EFFICIENCY.md` rules 1-12:

1. A new set of automatic gates was created for every patch release or wave (DVC 3.4.1-3.4.3, AAE `exact-runtime-e3/e4/e5`, earlier SPC slices) while closed gates stayed automatic.
2. Governance conformance runs on every `.project` change and is 14-17 % of usage in DVC and SPC; in DVC about one run in five failed because the bounded Active State exceeded its schema bounds during a release cycle and stayed red.
3. A manual dispatch added to a write-capable single-use publication workflow cannot requalify a closed release (its empty-namespace check rejects the existing tag) and creates a new write-capable entry point. This was found in review of a DVC change, not by policy.
4. Windows runners are used where a pinned runtime, not the operating system, is the claim.
5. Jobs without `timeout-minutes` and PR gates without concurrency remain common.

## Proposed changes (this branch)

- `platforms/github/CI_EFFICIENCY.md`: rules 13-19, a measurement section and a reference pattern for a consolidated gate.
- `playbooks/CANDIDATE_RELEASE.md`: step 14, gate closure on acceptance.
- `GOVERNANCE_EFFICIENCY.md`: pointer to the measurement tool.
- `tools/ci_usage_report.py`: read-only `static` and `usage` reports; never blocks.
- `qualification/ci-usage-report/` and one `validate.yml` step.

No change to CORE, profiles, schemas, project-state validator semantics or conformance pass/fail.

## Open decisions for the OM owner (confirmed 2026-10-02, see `OM_2.3_PRE_CANDIDATE_QUALIFICATION.md`)

1. Fold into a next MINOR (2.3) or into a re-opened 2.2 line. This draft assumes 2.3 from `om-v2.2.0`.
2. Whether governance conformance on pull requests should remain as in `PROJECT_STATE_CONFORMANCE.md`. This draft does not change it; rule 18 only addresses state churn.
3. Whether a later MINOR should add a non-blocking `report` step of `ci_usage_report.py static` to the reusable conformance workflow, following the `actions_runtime: report|enforce` pattern.
4. OM's own `validate.yml` triggers on both `pull_request` and `push` to `main`, which the new `static` report flags under rule 6; decide whether to apply the new rules to OM itself.

## Qualification plan (before candidate freeze)

- structural validation and recovery regression (existing `validate.yml`);
- `qualification/ci-usage-report/run_qualification.sh` (positive and negative fixtures, estimate method);
- shadow pilot, read-only, on DVC, SPC and AAE: run `static` and `usage` and compare with the audit above;
- negative control: confirm that the report never changes a workflow result.

## Adoption

Per project and prospective: bump the adopted OM pin per `playbooks/ADOPTION_MIGRATION.md`, then run a CI review against rules 13-19. Historical workflows and evidence are not reinterpreted. Order of value: AAE (Windows exact-runtime gates), DVC (per-release gates), SPC (conformance cadence). APC and DAE have negligible usage.
