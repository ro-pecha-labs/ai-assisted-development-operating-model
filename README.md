# AI-Assisted Development Operating Model

## Current canonical authority

**Canonical version:** `2.2.0`  
**Canonical tag:** `om-v2.2.0`  
**Exact canonical commit:** `89de89d0935d61d5442bc8301d9c6c4f2cf7af87`  
**Status:** CURRENT CANONICAL OPERATING MODEL

The immutable GitHub release identified above is the current normative authority. Development and evidence commits on `main` do not mutate the canonical release bytes.

Canonical adoption of OM 2.2.0 was explicitly authorized on 2026-10-02 and is recorded in `CANONICAL_ADOPTION_2.2.0.md`. OM 2.1.3 (`CANONICAL_ADOPTION_2.1.3.md`, 2026-10-02), OM 2.1.2 (`CANONICAL_ADOPTION_2.1.2.md`, 2026-09-29) and OM 2.1.1 (`CANONICAL_ADOPTION_2.1.1.md`, 2026-09-23) remain historical canonical authority.

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

Accepted release: `2.1.2` (tag `om-v2.1.2` → `78f7390e58ce363c1e734d6beb54c08ac50131c6`, released from `release/om-2.1`); see `ACCEPTANCE_2.1.2.md`.

PATCH-class under `OM_RELEASE_POLICY.md`: the GitHub-hosted validation workflow and the reusable project-state conformance workflow move from Node.js 20 action majors (`actions/checkout@v4`, `actions/setup-python@v5`) to Node.js 24 majors (`@v6`), with a deterministic regression guard `tools/actions_runtime_guard.py`. No CORE, profile, playbook, schema, template, validator semantics, policy or recovery behavior changes. See `PATCH_2.1.2.md`.

`om-v2.1.2` is cut from `om-v2.1.1` plus the 2.1.1 acceptance/adoption records, not from `main`: post-2.1.1 policy development on `main` (CI_EFFICIENCY rules 11–12) is not part of this patch.

OM 2.1.2 is historical canonical authority (superseded by 2.1.3 on 2026-10-02; `CANONICAL_ADOPTION_2.1.2.md`). Projects re-pin at their own safe boundary.

## OM 2.1.3 patch release

Accepted release: `2.1.3` (tag `om-v2.1.3` → `ed816aa46694b44b681f9453aaef3d0458ed0d79`, released from `release/om-2.1`); see `ACCEPTANCE_2.1.3.md`.

PATCH-class under `OM_RELEASE_POLICY.md`: `tools/actions_runtime_guard.py` reads a data map of official `actions/*` Node.js 24 majors (`tools/actions_runtime_map.json`, 14 actions), reports unmapped official actions as `UNJUDGED`, and the reusable project-state conformance workflow runs the guard over the caller's workflows in non-blocking `--report` mode. Conformance pass/fail is unchanged; enforcement is deferred to a MINOR release. See `PATCH_2.1.3.md`.

OM 2.1.3 is historical canonical authority (superseded by 2.2.0 on 2026-10-02; `CANONICAL_ADOPTION_2.1.3.md`). Projects re-pin at their own safe boundary.

## OM 2.2.0 minor release (current canonical authority)

Accepted release: `2.2.0` (tag `om-v2.2.0` → `89de89d0935d61d5442bc8301d9c6c4f2cf7af87`, released from `release/om-2.2`; source candidate `om-v2.2.0-rc1` → `f0a8fa5b0c945a6ed684db67bbf21b6baf8328c1`); see `ACCEPTANCE_2.2.0.md`.

MINOR under `OM_RELEASE_POLICY.md`: optional enforcement of the Node.js runtime check in the reusable project-state conformance workflow (`actions_runtime: report|enforce`, default `report`), runtime map maintenance, a pin reference finder for adoptions and hosted conformance caller guidance. Records: `OM_2.2_QUALIFICATION_PLAN.md`, `OM_2.2_PRE_CANDIDATE_QUALIFICATION.md`, `CANDIDATE_READINESS_2.2.0_RC1.md`, `RC1_QUALIFICATION_2.2.0.md`, `ACCEPTANCE_2.2.0.md`.

OM 2.2.0 is the current canonical authority (`CANONICAL_ADOPTION_2.2.0.md`). Projects re-pin at their own safe boundary.

## OM 2.3 candidate line

Release candidate `2.3.0-rc1` (MINOR, non-canonical, target `2.3.0`) on `release/om-2.3`, based on `om-v2.2.0`: CI efficiency portfolio rules for GitHub-hosted DEV CI (`platforms/github/CI_EFFICIENCY.md` rules 13-19, gate closure on acceptance in `playbooks/CANDIDATE_RELEASE.md`), and the read-only measurement tool `tools/ci_usage_report.py` (`static` and `usage`, never blocking). No change to CORE, profiles, schemas, templates, project-state validator semantics or conformance pass/fail. See `OM_2.3_CI_EFFICIENCY_PROPOSAL.md`, `OM_2.3_PRE_CANDIDATE_QUALIFICATION.md` and `CANDIDATE_READINESS_2.3.0_RC1.md`.

`OM.yaml` declares `2.3.0-rc1` (`non_canonical_candidate`). The RC is not frozen until the immutable tag `om-v2.3.0-rc1` exists and is read back. Canonical authority remains `om-v2.2.0`.

## Project adoption boundary

OM-level canonical adoption does not automatically migrate existing projects.

DVC, SPC, AAE, DAE, APC and Application Factory portfolio controls retain their project-recorded OM pins until each performs a separate safe-boundary adoption according to its authoritative project state.
