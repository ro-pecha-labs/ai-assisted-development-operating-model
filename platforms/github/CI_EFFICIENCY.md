# GitHub CI Efficiency Policy — OM 2.0

**Status:** PROSPECTIVE DEVELOPMENT POLICY

This policy specializes the DEV profile for GitHub-hosted CI. It governs new workflows and prospective workflow changes; it does not reinterpret historical evidence or accepted releases.

## Principles

1. **Least-cost capable runner.** Use `ubuntu-latest` by default. Use `windows-latest`, macOS, larger or specialized runners only when a required gate depends on that operating system, architecture or capability.
2. **Runtime and operating system are separate concerns.** A pinned PowerShell, Python, Node or other runtime does not by itself justify a more expensive operating system. Exact-runtime gates shall pin or verify the required runtime independently of runner selection where feasible.
3. **Dependency-scoped triggers.** Expensive workflows shall use the narrowest maintainable `paths`/event surface that covers their actual executable, test, contract and workflow dependencies. Governance- or documentation-only changes shall not trigger unrelated runtime qualification unless those files materially affect the gate.
4. **Cancel superseded PR work.** Mutable PR qualification should normally use workflow concurrency with `cancel-in-progress: true`. Do not apply cancellation where every execution is itself governed evidence or a required publication event.
5. **Separate qualification from publication.** PR workflows qualify mutable candidate changes. Canonical packages and release-like artifacts should normally be produced once from the accepted immutable revision on the authoritative branch or release ref.
6. **Avoid duplicate gates.** Do not repeat the same expensive qualification on both PR and post-merge push unless the post-merge state changes the claim being proved or a platform control requires requalification.
7. **Proportional artifacts.** Routine successful qualification need not upload durable artifacts when the platform result is sufficient. Persist artifacts/evidence when they establish a material accepted identity, package digest, connected qualification, release or other governed event.
8. **Cumulative gates require trigger design.** Where a higher-level gate re-executes lower-level suites, trigger topology should avoid unnecessary parallel execution of all cumulative gates while preserving required regression coverage.
9. **Cost-aware initialization.** New DEV repositories shall review runner type, expected trigger frequency, path scope, PR/push duplication, artifact retention and cumulative test structure before CI is treated as qualified platform enforcement.
10. **Qualification before reliance.** A CI optimization that changes runner, trigger topology, packaging or gate decomposition shall be qualified before it replaces the prior control.
11. **Candidate/checkpoint is the cumulative qualification boundary.** Intermediate development commits, including AI-assisted commits, shall not each independently invoke cumulative candidate, release or historical qualification merely because they were pushed. Routine development should use the lightest sufficient PR validation; cumulative qualification belongs at an explicit candidate/checkpoint boundary, unless a safety-critical dependency requires earlier execution.
12. **Retire closed lifecycle gates from automatic execution.** Once a candidate/wave gate is accepted, closed or superseded, its workflow should normally become explicit/manual historical requalification or be replaced by the successor gate. Closed gates shall not remain on broad automatic PR/push triggers without a documented current control purpose.
13. **Parameterize release-line gates; do not duplicate them per release or wave.** A profile should keep one pre-candidate gate and one candidate/readiness gate whose candidate identity (source commit, release tag, expected package digest) is supplied by a tracked manifest or by dispatch inputs. Creating a new set of automatic workflows for each patch release or wave multiplies CI cost and leaves closed gates behind. Where a project already has per-release workflows, rule 12 applies to the closed ones.
14. **Gate closure is part of acceptance.** The acceptance or checkpoint record of a candidate/wave shall state which gates were converted to explicit/manual execution or removed from automatic triggers. Closure is performed in the same or the immediately following change, not left for a later cleanup.
15. **Write-capable single-use workflows keep their narrow trigger.** Publication, tagging and freeze workflows that hold write permission and are meant to run once shall keep their narrowly path-filtered trigger, shall not receive a new manual entry point unless that entry point has a read-only verification path, shall not use `cancel-in-progress`, and shall declare `timeout-minutes`. A manual run of such a workflow after the release exists would fail its own empty-namespace check and cannot requalify the release.
16. **Require the operating system the claim needs, and say so.** Windows and macOS runners are justified by a gate's claim (for example an exact Windows runtime), not by a pinned runtime version alone (rule 2). A gate that uses a non-Linux runner shall record that claim in the workflow or its review record, so it can be reviewed when the claim changes.
17. **Every job is bounded.** Every job shall declare `timeout-minutes`, and every mutable PR gate shall use workflow concurrency (rule 4). A job that runs on Windows or macOS is billed at a higher rate, so its bound shall be proportionate to its measured duration.
18. **Governance state churn is a CI input.** Files that trigger governance conformance (for example `.project/ACTIVE_STATE.yaml`) shall be updated at checkpoints, not with every intermediate commit, where the project uses the conformance gate on pull requests. A bounded state that exceeds its schema bounds is PROJECT_STATE drift: fix it in the next change instead of leaving the gate red, because each red run is also a billed run.
19. **Measure before and after.** A project should record estimated CI minutes (by workflow, event and runner OS) at each candidate/checkpoint boundary and before and after a CI optimization (rule 10). Use `tools/ci_usage_report.py`; the Actions `billable` timing field is not a reliable source.

## Recommended PR concurrency baseline

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true
```

The baseline is a default, not a universal invariant. Publication, mutation and durable-evidence workflows may require different concurrency semantics.

## Review questions

Before enabling or materially changing a GitHub Actions workflow, determine:

- Does this gate genuinely require its selected operating system?
- Is the exact runtime pinned or explicitly verified where the claim requires it?
- Do event and path filters correspond to actual dependencies?
- Can superseded mutable PR runs be cancelled safely?
- Are PR qualification and accepted-revision publication unnecessarily duplicating work?
- Is every uploaded artifact required by evidence or delivery semantics?
- Does a cumulative gate cause lower-level suites to execute multiple times for one change?
- Has the changed CI configuration itself been qualified?

## Execution and storage hierarchy

1. **Do not persist routine successful output.** Platform logs/job summaries are sufficient unless a material claim requires durable evidence.
2. **Use cache for reproducible dependency/tool reuse.** Prefer cache for downloaded SDKs, package-manager caches and deterministic toolchain reuse rather than rebuilding an image or uploading the same dependency as an artifact.
3. **Use Actions artifacts for bounded temporary output.** Upload artifacts only when cross-job transfer, bounded diagnostics or temporary qualification evidence requires them; configure retention proportionately.
4. **Use GitHub Release assets for accepted immutable distributions.** Do not use transient Actions artifacts as the primary long-lived distribution surface for an accepted release.
5. **Use Packages only for package-manager consumption.** Publish to GitHub Packages when the artifact is intended to be consumed as a package/container dependency, not merely because storage is available.
6. **Use custom runner images only after measurement.** Custom images are appropriate only when measured repeated setup cost justifies the paid larger-runner execution and image-storage model. A large toolchain download alone is not sufficient justification.
7. **Prefer standard hosted runners by default.** Do not move to larger/specialized runners solely to avoid a setup step that can be handled efficiently by setup actions or cache.

Before adopting a storage optimization, measure both execution savings and the new storage/runner cost. A cost optimization shall not weaken exact-runtime or evidence claims.

## Measurement and reporting

`tools/ci_usage_report.py` is read-only and never blocks:

- `static <path>...` reports, per repository, automatic workflows without concurrency or `timeout-minutes`, automatic workflows that use Windows or macOS runners, workflows that trigger on both `pull_request` and `push`, and write-capable automatic workflows;
- `usage` estimates minutes from job durations (each job rounded up to a whole minute, Windows x2, macOS x10) by workflow and by event. The result is an estimate for comparing periods, not an invoice.

Small, frequent jobs matter: a 20-second job is counted as one minute, so very frequent cheap gates (for example governance conformance on every commit) can dominate usage.

## Reference pattern: consolidated gate

A single offline gate per profile (for example one Linux-hosted `offline-all` workflow with `paths-ignore` for documentation and governance files, PR concurrency and a job timeout) replaces many per-slice workflows. Slice-level or exact-runtime variants that are needed only at a candidate boundary stay explicit/manual (rule 11).
