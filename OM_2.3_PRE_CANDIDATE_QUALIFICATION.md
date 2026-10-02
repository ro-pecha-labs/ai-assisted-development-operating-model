# OM 2.3 — Pre-Candidate Qualification Status

**Status:** PRE-CANDIDATE / Q0–Q4 PASS / OWNER DECISIONS D1–D4 CONFIRMED / READY FOR CANDIDATE-READINESS REVIEW
**Development head:** `36ff53212a89b7e62d797d0601c49cb51824a2ab` (`release/om-2.3`)
**Base:** `om-v2.2.0` (`89de89d0935d61d5442bc8301d9c6c4f2cf7af87`)
**Date:** 2026-10-02

## Scope

Development target: `2.3.0-dev — CI Efficiency Portfolio Rules` (MINOR under `OM_RELEASE_POLICY.md`). Plan and rationale: `OM_2.3_CI_EFFICIENCY_PROPOSAL.md`.

Current canonical authority remains `om-v2.2.0`. This record does not freeze a candidate, does not make OM 2.3 canonical and does not adopt it in any child project. `OM.yaml` still declares `2.2.0`; the release identity is promoted only by a later readiness change.

## Work packages (merged into `release/om-2.3`)

| WP | PR | Merge commit | Hosted `Validate OM2` run on the PR head |
|---|---|---|---|
| Draft rules 13–19, step 14, `tools/ci_usage_report.py`, qualification fixtures, proposal | #48 | `1820024eafba17123ef49bb46cf1b148f3b2e2e0` | `37002687374` SUCCESS (`733507c`) |
| Pilot findings: write-capable exclusion, parallel usage fetch, `--max-runs` | #51 | `36ff53212a89b7e62d797d0601c49cb51824a2ab` | `37007244712` SUCCESS (`c59519b`) |

`validate.yml` does not run on pushes to release branches, so there is no hosted run on the development head itself; the head is covered by the PR head runs above and by the local run in Q4. The hosted run on the exact head is produced by the readiness change.

## Q0 — Structural and backward compatibility

**PASS.** The change set touches `platforms/github/CI_EFFICIENCY.md`, `playbooks/CANDIDATE_RELEASE.md`, `GOVERNANCE_EFFICIENCY.md`, one tool, its qualification fixtures, one `validate.yml` step and documentation. CORE, profiles, schemas, templates, `validate_project_bootstrap.py`, the reusable conformance workflow and recovery behavior are unchanged. Conformance pass/fail of any caller is unchanged from 2.2.0.

## Q1 — Tool qualification

**PASS.** `qualification/ci-usage-report/run_qualification.sh` (structural CI step "Qualify CI usage report"): efficient fixture is not flagged; wasteful fixture is flagged for missing concurrency, missing timeout, Windows runner and PR+push; write-capable fixture is reported separately and never flagged for concurrency (rule 15); the usage estimate is checked on fixed data (job rounded up to a whole minute, Windows x2); `usage --repo` is checked through an offline `gh` stand-in with parallel job fetch and `--max-runs`. The tool exits 0 in every mode.

## Q2 — Shadow pilot

**PASS.** Read-only shadow pilot on 2026-10-02, authorized by the owner, on DVC, SPC and AAE. Method: `static` over each repository's `.github/workflows` at its default branch and `usage --since 2026-09-18` through the Actions API. No pull request, branch or workflow change was made in the pilot repositories; their working trees stayed clean.

| Project | Runs | Estimated minutes | Windows/macOS minutes | Failed runs |
|---|---|---|---|---|
| DVC | 3 092 | 4 840 | 1 772 | 756 |
| SPC | 3 105 | 4 443 | 882 | 354 |
| AAE | 621 | 1 834 | 1 364 | 31 |

The `usage` numbers agree with an independent ad-hoc computation of the same data to within 0.05 %. `static` after the pilot fixes (#51), default branch heads:

| Project | Automatic | Without concurrency | Without timeout | PR and push | Write-capable |
|---|---|---|---|---|---|
| DVC | 29 | 2 | 1 | 1 | 17 |
| SPC | 8 | 1 | 1 | 1 | 0 |
| AAE | 14 | 5 | 13 | 3 | 2 |

Pilot findings, both fixed in #51: write-capable workflows were flagged for missing concurrency (DVC 15 -> 2); `usage` over about 3 000 runs took about 30 minutes (now parallel, with `--max-runs`). The `usage` timings after the fix were not re-measured on the live repositories.

## Q3 — Negative controls

**PASS.** The report never changes the result of a workflow: it exits 0 on all fixtures and on the three pilot repositories, which have no modified files after the run. `static` only reads workflow files and never writes them.

## Q4 — Recovery and all-profile regression

**PASS.** All 14 `run:` steps of `validate.yml` were executed locally with `bash -eo pipefail` on the development head and passed (structural validation, minimal and solo recovery, OM 2.1 policy semantics, release identity pin guard, actions runtime guard and gate modes, runtime map maintenance, pin reference finder, CI usage report, project bootstrap conformance including negative and uninstantiated-template controls).

## Disposition of `CI_EFFICIENCY.md` rules 13–19

New normative guidance for GitHub-hosted DEV CI; rules 1–12 are unchanged. Rules 13–19 are prospective and do not reinterpret historical evidence or accepted releases. OM's own `validate.yml` triggers on `pull_request`, `push` to `main` and `om-v*` tags; the new `static` report flags it under rule 6. This is recorded as a known limit and is not changed in 2.3 (decision D4).

## Owner decisions

The decisions open in `OM_2.3_CI_EFFICIENCY_PROPOSAL.md` were confirmed by the owner on 2026-10-02, as stated in the owner's message in the development session, with the content below.

| ID | Question | Decision |
|---|---|---|
| D1 | Release line | New MINOR 2.3 from `om-v2.2.0` (`release/om-2.3` exists) |
| D2 | Governance conformance on pull requests | Unchanged (`PROJECT_STATE_CONFORMANCE.md`) |
| D3 | Non-blocking `static` report step in the reusable conformance workflow | Not in 2.3; candidate for a later MINOR |
| D4 | Apply rules to OM's own `validate.yml` | Not in 2.3; recorded as known limit |

## Known limits

1. The shadow pilot did not use draft pull requests in the child repositories; it was read-only API and checkout based.
2. `usage` is an estimate (job minutes rounded up, Windows x2, macOS x10); the Actions `billable` field was 0 in the pilot repositories.
3. Failed-run counts include all workflows, not only conformance.
4. No child project is migrated; adoption per `playbooks/ADOPTION_MIGRATION.md` follows GA.

## Remaining before RC1 freeze

1. Candidate-readiness change: `OM.yaml` `2.2.0` -> `2.3.0-rc1`, `accepted_release` -> `non_canonical_candidate`, `README.md` and `00_INDEX.md` status, `CANDIDATE_READINESS_2.3.0_RC1.md`, merged through protected `release/om-2.3`.
2. Hosted validation of the exact merged SHA, then the immutable annotated tag `om-v2.3.0-rc1` created by the owner on that SHA, read-back and tag-triggered hosted validation, freeze evidence record.
3. Candidate qualification of the exact frozen identity.
