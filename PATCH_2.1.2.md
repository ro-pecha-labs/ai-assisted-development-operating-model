# OM 2.1.2 — Patch Release Record

**Release class:** PATCH (`OM_RELEASE_POLICY.md`)
**Intended tag:** `om-v2.1.2`
**Base:** `om-v2.1.1` (`df9812815a3a83c39b49c66035b4795acd777fc7`) plus the OM 2.1.1 acceptance and canonical-adoption records
**Release branch:** `release/om-2.1`
**Date:** 2026-09-29

## Defect

GitHub deprecated the Node.js 20 runtime for JavaScript actions. OM 2.1.1 workflows still use Node.js 20 majors:

- `.github/workflows/validate.yml`: `actions/checkout@v4`, `actions/setup-python@v5`;
- `.github/workflows/project-state-conformance.yml` (reusable, called by adopting projects as `...@om-v<version>`): `actions/checkout@v4` (2×), `actions/setup-python@v5`.

Classification: tooling / CI platform maintenance. Not an OM PRODUCT defect.

## Change

- `actions/checkout@v4` → `@v6` and `actions/setup-python@v5` → `@v6` in both workflows (lowest majors running on `node24`, verified from each version's `action.yml`); only `uses:` lines change.
- `tools/actions_runtime_guard.py`: fails when a known action is pinned below its Node.js 24 major.
- `validate.yml`: positive guard run over `.github/workflows` and negative rejection of `qualification/actions-runtime/node20-negative.yml`.
- `OM.yaml`: `version: 2.1.2`; `README.md`, `00_INDEX.md`: patch status.

Unchanged: CORE, profiles, playbooks, schemas, templates, validator semantics, policies, recovery behavior. `platforms/github/CI_EFFICIENCY.md` rules 11–12 on `main` (PR #28) are post-2.1.1 policy development and are deliberately **not** part of this patch.

## Why not from `main`

A tag cut from `main` would include PR #28 (normative policy additions), which exceeds PATCH scope and would repeat the OM 2.1.0 release-control deviation class (`GA_DISPOSITION_2.1.0.md`). The patch is therefore qualified and tagged on `release/om-2.1`.

## Release procedure

1. Protected PR into `release/om-2.1`; structural CI including the new guard must pass.
2. Capture the exact post-merge head of `release/om-2.1`; verify it with `tools/release_identity_guard.py` against the qualified commit.
3. Create annotated tag `om-v2.1.2` on exactly that commit; tag-bound `validate.yml` run must pass.
4. GitHub Release `OM 2.1.2` from the tag.
5. `ACCEPTANCE_2.1.2.md` on `main` with PR, run and tag identity evidence; merge `release/om-2.1` back into `main`.

## Adoption

Acceptance does not perform canonical adoption. Canonical authority remains `om-v2.1.1` until an explicit, prospective adoption decision. Adopting projects re-pin `.project/PROJECT.yaml` and their `om-project-state-conformance.yml` (`uses: ...@om-v2.1.2`, `om_ref: om-v2.1.2`) at their own safe boundary. Historical evidence produced under earlier OM versions keeps its meaning.