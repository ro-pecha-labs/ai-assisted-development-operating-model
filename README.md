# AI-Assisted Development Operating Model

## Current canonical authority

**Canonical version:** `2.1.1`  
**Canonical tag:** `om-v2.1.1`  
**Exact canonical commit:** `df9812815a3a83c39b49c66035b4795acd777fc7`  
**Status:** CURRENT CANONICAL OPERATING MODEL

The immutable GitHub release identified above is the current normative authority. Development and evidence commits on `main` do not mutate the canonical release bytes.

Canonical adoption was explicitly authorized on 2026-09-23 and is recorded in `CANONICAL_ADOPTION_2.1.1.md`.

## OM 2.1 qualification lineage

Qualified candidate:

- `OM2-2.1.0-RC1`;
- tag `om-v2.1.0-rc1`;
- exact commit `02a4a3f5004fd497b2e4e6402b508c1a29802c35`;
- FROZEN / QUALIFIED PASS / NON-CANONICAL.

RC1 acceptance review passed.

The first GA release attempt `om-v2.1.0` is **not accepted for GA** and remains immutable historical evidence. See `GA_DISPOSITION_2.1.0.md`.

OM 2.1.1 is the accepted PATCH successor. Its exact immutable identity is:

`om-v2.1.1 -> df9812815a3a83c39b49c66035b4795acd777fc7`

Exact tag-bound hosted qualification: `35854783610 / SUCCESS`.

GA acceptance: `ACCEPTANCE_2.1.1.md`.

Canonical adoption: `CANONICAL_ADOPTION_2.1.1.md`.

## OM 2.1 capability scope

The canonical OM 2.1.1 release preserves the qualified OM 2.1 capability scope:

- optional cross-profile solo assurance;
- `SOLO_ASSURANCE`;
- vendor-neutral `AI_DEVELOPMENT_LOOP`;
- proportional DEV lightweight/formal release semantics;
- machine-grounded evidence rules;
- materiality guidance;
- governance-efficiency guidance;
- PATCH/MINOR/MAJOR OM release policy;
- GitHub execution/storage efficiency guidance;
- continuous project-state conformance;
- release-safe DEV template semantics;
- standard and solo bounded recovery.

The five primary profiles remain DEV, SOLUTION, DOCUMENT, EXPERIMENT and LIGHT.

## OM 2.1.2 patch release

Release target on `release/om-2.1`: `2.1.2` (tag `om-v2.1.2`, not yet accepted).

PATCH-class under `OM_RELEASE_POLICY.md`: the GitHub-hosted validation workflow and the reusable project-state conformance workflow move from Node.js 20 action majors (`actions/checkout@v4`, `actions/setup-python@v5`) to Node.js 24 majors (`@v6`), with a deterministic regression guard `tools/actions_runtime_guard.py`. No CORE, profile, playbook, schema, template, validator semantics, policy or recovery behavior changes. See `PATCH_2.1.2.md`.

`om-v2.1.2` is cut from `om-v2.1.1` plus the 2.1.1 acceptance/adoption records, not from `main`: post-2.1.1 policy development on `main` (CI_EFFICIENCY rules 11–12) is not part of this patch.

Canonical authority remains `om-v2.1.1` until OM 2.1.2 is accepted and explicitly adopted. Projects then re-pin at their own safe boundary.

## OM 2.1.3 patch release

Release target on `release/om-2.1`: `2.1.3` (tag `om-v2.1.3`, not yet accepted).

PATCH-class under `OM_RELEASE_POLICY.md`: `tools/actions_runtime_guard.py` reads a data map of official `actions/*` Node.js 24 majors (`tools/actions_runtime_map.json`, 14 actions), reports unmapped official actions as `UNJUDGED`, and the reusable project-state conformance workflow runs the guard over the caller's workflows in non-blocking `--report` mode. Conformance pass/fail is unchanged; enforcement is deferred to a MINOR release. See `PATCH_2.1.3.md`.

Canonical authority remains `om-v2.1.2` until OM 2.1.3 is accepted and explicitly adopted. Projects then re-pin at their own safe boundary.

## Project adoption boundary

OM-level canonical adoption does not automatically migrate existing projects.

DVC, SPC, AAE, DAE, APC and Application Factory portfolio controls retain their project-recorded OM pins until each performs a separate safe-boundary adoption according to its authoritative project state.
