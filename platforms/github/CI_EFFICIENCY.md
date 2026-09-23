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
