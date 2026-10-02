# OM 2.1.3 — Patch Release Record

**Release class:** PATCH (`OM_RELEASE_POLICY.md`)
**Intended tag:** `om-v2.1.3`
**Base:** `om-v2.1.2` (`78f7390e58ce363c1e734d6beb54c08ac50131c6`)
**Release branch:** `release/om-2.1`
**Date:** 2026-10-02

## Defect

The OM 2.1.2 Node.js 24 guard covered four actions (`checkout`, `setup-python`, `setup-dotnet`, `upload-artifact`). Findings from the AAE post-adoption review and a portfolio scan:

- `actions/download-artifact` v4–v6 run on `node20` (v7 runs on `node24`) and were not covered;
- the reusable `project-state-conformance.yml` did not run the guard at all, so an adopting project could pin `om-v2.1.2` and keep Node.js 20 workflows unnoticed;
- the `PASS` message could be read as a statement about all actions, although unknown actions were silently not judged.

Classification: guard coverage gap / qualification gap (tooling, CI platform maintenance). OM 2.1.2 is not invalidated: it claimed Node.js 24 majors for OM's own workflows plus a regression guard for the actions it listed.

## Change

- `tools/actions_runtime_map.json` (new): data map of lowest Node.js 24 majors, 14 official actions, verified from each version's upstream `action.yml` on 2026-10-02: `checkout` 5, `setup-python` 6, `setup-dotnet` 5, `upload-artifact` 6, `download-artifact` 7, `cache` 5, `setup-node` 5, `github-script` 8, `setup-java` 5, `setup-go` 6, `deploy-pages` 5, `configure-pages` 6, `stale` 10, `labeler` 6.
- `tools/actions_runtime_guard.py`: reads the map (`--map` to override); an official `actions/*` action absent from the map is printed as `UNJUDGED` (no failure); `PASS` states mapped and unjudged counts; `--report` prints `REPORT:` lines and exits 0; a malformed map exits 2. Third-party actions and non-major refs remain not judged.
- `.github/workflows/project-state-conformance.yml`: new final step runs the guard from the adopted OM revision over the caller's `.github/workflows` in `--report` mode, writes the job summary and a warning annotation, and never changes the job result. The step is skipped when the adopted OM revision has no guard or the caller has no workflows.
- `.github/workflows/validate.yml`: guard qualification extended (positive fixture, unmapped fixture, extended negative fixture that must produce one `FAIL` per mapped action, report mode, invalid map rejection).
- `qualification/actions-runtime/`: `node24-positive.yml`, `node20-negative-extended.yml`, `unmapped-official.yml`, `invalid-map.json`.
- `OM.yaml`: `version: 2.1.3`; `README.md`, `00_INDEX.md`: patch status.

Unchanged: CORE, profiles, playbooks, schemas, templates, validator semantics, policies, recovery behavior, `validate_project_bootstrap.py`, and the pass/fail result of project-state conformance. `platforms/github/CI_EFFICIENCY.md` rules 11–12 on `main` (PR #28) are deliberately **not** part of this patch.

## Why PATCH and why non-blocking

A blocking guard would change conformance results of adopting projects (portfolio scan: DVC still has Node.js 20 references) and therefore normative behavior, which `OM_RELEASE_POLICY.md` assigns to MINOR with RC and shadow pilot. 2.1.3 therefore only reports. Enforcement (for example an `actions_runtime: report|enforce` input) is a follow-up MINOR objective.

## Known limits

- The map is a bounded list of known boundaries for official `actions/*`, not a catalog; unmapped official actions are surfaced as `UNJUDGED`. Third-party actions (for example `anthropics/claude-code-action`) are not judged.
- The map is bound to the release tag; projects receive map updates by re-pinning.
- Upstream facts date from the `verified_on` field of the map.

## Release procedure

1. Protected PR into `release/om-2.1`; structural CI including the extended guard qualification must pass.
2. Capture the exact post-merge head of `release/om-2.1`; verify with `tools/release_identity_guard.py`.
3. Annotated tag `om-v2.1.3` on exactly that commit; tag-bound `validate.yml` run must pass.
4. GitHub Release `OM 2.1.3` from the tag.
5. `ACCEPTANCE_2.1.3.md` on `main` with PR, run and tag identity evidence; merge `release/om-2.1` back into `main`.

## Adoption

Acceptance does not perform canonical adoption. Canonical authority remains `om-v2.1.2` until an explicit, prospective adoption decision. Adopting projects re-pin `.project/PROJECT.yaml` and their `om-project-state-conformance.yml` (`uses: ...@om-v2.1.3`, `om_ref: om-v2.1.3`) at their own safe boundary. After re-pin, AAE removes its local `actions/download-artifact` extension once the canonical map is confirmed to cover it. Historical evidence produced under earlier OM versions keeps its meaning.
