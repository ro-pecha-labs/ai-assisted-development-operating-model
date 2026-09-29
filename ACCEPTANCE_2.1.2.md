# OM 2.1.2 — GA Acceptance

**Status:** ACCEPTED_RELEASE / NON-CANONICAL  
**Accepted tag:** `om-v2.1.2` (annotated)  
**Exact accepted commit:** `78f7390e58ce363c1e734d6beb54c08ac50131c6`  
**Release class:** PATCH (`OM_RELEASE_POLICY.md`)  
**Acceptance date:** 2026-09-29

## Basis

OM 2.1.2 is accepted as the PATCH successor of OM 2.1.1. It moves the OM GitHub workflows to Node.js 24 action majors and adds a deterministic regression guard. Scope and exclusions: `PATCH_2.1.2.md`.

The accepted identity is the immutable Git tag:

`om-v2.1.2 -> 78f7390e58ce363c1e734d6beb54c08ac50131c6`

The tag is annotated; its commit is the merge of PR #30 into `release/om-2.1`, whose first parent is `om-v2.1.1` (`df9812815a3a83c39b49c66035b4795acd777fc7`). Post-2.1.1 policy development on `main` (PR #28, `platforms/github/CI_EFFICIENCY.md` rules 11–12) is **not** contained in the tag.

The GitHub release is:

- title: `OM 2.1.2`;
- tag: `om-v2.1.2`;
- prerelease: `false`;
- latest: `true`.

## Qualification evidence

Pre-tag protected PR qualification:

- PR: #30 (`om212-node24-actions` → `release/om-2.1`);
- head SHA: `8a70ab2`;
- workflow run: `36548955126`;
- event: `pull_request`;
- conclusion: `SUCCESS`, including `Qualify GitHub Actions runtime guard` (positive run over `.github/workflows`, negative rejection of `qualification/actions-runtime/node20-negative.yml`).

Post-merge identity:

- `release/om-2.1` head `78f7390e58ce363c1e734d6beb54c08ac50131c6` has a tree identical to the qualified PR head `8a70ab2`;
- `validate.yml` has no push trigger for `release/om-2.1`; the exact commit is qualified by the tag-bound run below.

Release identity check before tagging (method of `tools/release_identity_guard.py`): expected `78f7390e58ce363c1e734d6beb54c08ac50131c6`, observed `release/om-2.1` head `78f7390e58ce363c1e734d6beb54c08ac50131c6` — PASS.

Exact immutable tag-bound qualification:

- tag: `om-v2.1.2`;
- exact head SHA: `78f7390e58ce363c1e734d6beb54c08ac50131c6`;
- workflow run: `36549211982`;
- event: `push`;
- conclusion: `SUCCESS`.

Both runs carry no Node.js 20 deprecation annotation.

## Tag protection

The organization ruleset `OM2 version tags` (`refs/tags/om-v*`) blocks deletion and update of `om-v2.1.2`.

## Product and semantic disposition

No OM PRODUCT defect. The patch changes only GitHub workflow action majors, adds `tools/actions_runtime_guard.py` with its negative fixture, and updates version/status coherence. CORE, profiles, playbooks, schemas, templates, validator semantics, policies and recovery behavior are unchanged from `om-v2.1.1`.

## Canonical authority

Acceptance of OM 2.1.2 does **not** perform canonical adoption.

Current canonical authority remains:

- version: `2.1.1`;
- tag: `om-v2.1.1`;
- exact commit: `df9812815a3a83c39b49c66035b4795acd777fc7`.

Prospective canonical adoption of OM 2.1.2 requires a separate explicit human authorization and governance-index update. No child project is migrated or re-pinned by this acceptance record.