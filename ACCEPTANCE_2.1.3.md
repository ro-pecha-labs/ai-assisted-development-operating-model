# OM 2.1.3 — GA Acceptance

**Status:** ACCEPTED_RELEASE / NON-CANONICAL  
**Accepted tag:** `om-v2.1.3` (annotated, tag object `f5c1d1725d07f19a20375fe8389365beeea08fc4`)  
**Exact accepted commit:** `ed816aa46694b44b681f9453aaef3d0458ed0d79`  
**Release class:** PATCH (`OM_RELEASE_POLICY.md`)  
**Acceptance date:** 2026-10-02

## Basis

OM 2.1.3 is accepted as the PATCH successor of OM 2.1.2. It extends the Node.js 24 runtime guard with a data map of 14 official actions, reports unmapped official actions as `UNJUDGED` and runs the guard in non-blocking report mode in the reusable project-state conformance workflow. Scope and exclusions: `PATCH_2.1.3.md`.

The accepted identity is the immutable Git tag:

`om-v2.1.3 -> ed816aa46694b44b681f9453aaef3d0458ed0d79`

The tag is annotated; its commit is the merge of PR #33 into `release/om-2.1`, whose first parent is `om-v2.1.2` (`78f7390e58ce363c1e734d6beb54c08ac50131c6`). Post-2.1.1 policy development on `main` (PR #28, `platforms/github/CI_EFFICIENCY.md` rules 11–12) is **not** contained in the tag.

The GitHub release is:

- title: `OM 2.1.3`;
- tag: `om-v2.1.3`;
- prerelease: `false`;
- latest: `true`.

## Qualification evidence

Pre-tag protected PR qualification:

- PR: #33 (`claude/festive-cannon-x3lo6o` → `release/om-2.1`);
- head SHA: `7890a0a379c1c3a13640afd9154502c2311ce164`;
- workflow run: `36987043407`;
- event: `pull_request`;
- conclusion: `SUCCESS`, including the extended `Qualify GitHub Actions runtime guard` step (positive, unmapped, extended negative, report mode and invalid map fixtures).

Release identity check before tagging (method of `tools/release_identity_guard.py`): expected `ed816aa46694b44b681f9453aaef3d0458ed0d79`, observed `release/om-2.1` head `ed816aa46694b44b681f9453aaef3d0458ed0d79` — PASS.

Exact immutable tag-bound qualification:

- tag: `om-v2.1.3`;
- exact head SHA: `ed816aa46694b44b681f9453aaef3d0458ed0d79`;
- workflow run: `36987775749`;
- event: `push`;
- conclusion: `SUCCESS`.

Remote tag check: `refs/tags/om-v2.1.3^{}` resolves to `ed816aa46694b44b681f9453aaef3d0458ed0d79`.

## Known limits

- The reusable-workflow report step was qualified by local simulation; a real call from a child repository is not yet evidenced.
- The runtime map is a bounded list of official actions (verified 2026-10-02); third-party actions are not judged.
- The guard is non-blocking; enforcement is a follow-up MINOR objective.

## Product and semantic disposition

No OM PRODUCT defect. The patch changes only GitHub tooling and CI (guard, map, reusable-workflow report step, qualification fixtures) and version/status coherence. Conformance pass/fail, CORE, profiles, playbooks, schemas, templates, validator semantics, policies and recovery behavior are unchanged from `om-v2.1.2`.

## Canonical authority

Acceptance of OM 2.1.3 does **not** perform canonical adoption.

Current canonical authority remains:

- version: `2.1.2`;
- tag: `om-v2.1.2`;
- exact commit: `78f7390e58ce363c1e734d6beb54c08ac50131c6`.

Prospective canonical adoption of OM 2.1.3 requires a separate explicit human authorization and governance-index update. No child project is migrated or re-pinned by this acceptance record.
