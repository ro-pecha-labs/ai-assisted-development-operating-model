# Operating Model 2.1 Canonical Index

**Version:** `2.2.0`  
**Status:** CURRENT CANONICAL OPERATING MODEL  
**Canonical tag:** `om-v2.2.0`  
**Exact canonical commit:** `89de89d0935d61d5442bc8301d9c6c4f2cf7af87`

## Canonical entrypoints

- Machine manifest: `OM.yaml`
- Universal kernel: `CORE.md`
- Profiles: `profiles/`
- Triggered playbooks: `playbooks/`
- Universal schemas: PROJECT v2, ACTIVE_STATE v2, EXTERNAL_SOURCES v1, EVIDENCE_RECORD v2
- DEV templates: `templates/DEV/`
- Validator: `tools/validate.py`

The immutable release tag `om-v2.2.0` is the current normative authority. Post-release development and evidence on `main` do not mutate the canonical release bytes.

## OM 2.1 lineage

Qualified source candidate:

- candidate: `OM2-2.1.0-RC1`;
- immutable candidate tag: `om-v2.1.0-rc1`;
- exact candidate commit: `02a4a3f5004fd497b2e4e6402b508c1a29802c35`;
- disposition: FROZEN / QUALIFIED PASS / NON-CANONICAL.

RC1 acceptance review: PASS.

The first GA release attempt `om-v2.1.0` is preserved as **NOT_ACCEPTED_FOR_GA / RELEASE_CONTROL_DEVIATION**. See `GA_DISPOSITION_2.1.0.md`.

OM 2.1.1 is the PATCH successor that preserves the qualified OM 2.1 normative behavior and remedies the release-control identity race prospectively.

## OM 2.1.1 acceptance and adoption

- immutable release tag: `om-v2.1.1`;
- exact release commit: `df9812815a3a83c39b49c66035b4795acd777fc7`;
- tag-bound validation: `35854783610 / SUCCESS`;
- release acceptance: `ACCEPTANCE_2.1.1.md`;
- canonical adoption: `CANONICAL_ADOPTION_2.1.1.md`;
- disposition: **ACCEPTED RELEASE / HISTORICAL CANONICAL AUTHORITY (superseded by 2.1.2 on 2026-09-29)**.

Canonical adoption is prospective. Existing child projects are not migrated automatically and retain their project-recorded OM pins until separate safe-boundary adoption.

## OM 2.1.2 patch (ACCEPTED RELEASE / HISTORICAL CANONICAL AUTHORITY, superseded by 2.1.3 on 2026-10-02)

- release branch: `release/om-2.1` (from `om-v2.1.1` plus 2.1.1 acceptance/adoption records);
- tag: `om-v2.1.2` → `78f7390e58ce363c1e734d6beb54c08ac50131c6`;
- scope: Node.js 24 action majors in `validate.yml` and `project-state-conformance.yml`; regression guard `tools/actions_runtime_guard.py`;
- class: PATCH (tooling/CI only; normative OM 2.1 behavior unchanged);
- tag-bound validation: `36549211982 / SUCCESS`;
- records: `PATCH_2.1.2.md`, `ACCEPTANCE_2.1.2.md`, `CANONICAL_ADOPTION_2.1.2.md`.

Canonical adoption was prospective from 2026-09-29 until superseded on 2026-10-02. Existing child projects are not migrated automatically and retain their project-recorded OM pins until separate safe-boundary adoption.

## OM 2.1.3 patch (ACCEPTED RELEASE / HISTORICAL CANONICAL AUTHORITY, superseded by 2.2.0 on 2026-10-02)

- release branch: `release/om-2.1` (from `om-v2.1.2`);
- tag: `om-v2.1.3` → `ed816aa46694b44b681f9453aaef3d0458ed0d79`;
- scope: data-driven Node.js 24 runtime map for official actions (`tools/actions_runtime_map.json`), `UNJUDGED` reporting, non-blocking guard step in `project-state-conformance.yml`;
- class: PATCH (tooling/CI only; conformance pass/fail and normative OM 2.1 behavior unchanged);
- tag-bound validation: `36987775749 / SUCCESS`;
- records: `PATCH_2.1.3.md`, `ACCEPTANCE_2.1.3.md`, `CANONICAL_ADOPTION_2.1.3.md`.

Canonical adoption was prospective from 2026-10-02 until superseded on 2026-10-02 by 2.2.0. Existing child projects are not migrated automatically and retain their project-recorded OM pins until separate safe-boundary adoption.

## OM 2.2.0 minor release (ACCEPTED RELEASE / CURRENT CANONICAL NORMATIVE AUTHORITY)

- tag: `om-v2.2.0` → `89de89d0935d61d5442bc8301d9c6c4f2cf7af87` (source candidate `om-v2.2.0-rc1` → `f0a8fa5b0c945a6ed684db67bbf21b6baf8328c1`);
- scope: optional enforce mode of the Node.js runtime check, runtime map maintenance, pin reference finder, hosted conformance caller guidance;
- class: MINOR (backward compatible; `actions_runtime` defaults to `report`);
- tag-bound validation: `37000769192 / SUCCESS`;
- records: `OM_2.2_QUALIFICATION_PLAN.md`, `OM_2.2_PRE_CANDIDATE_QUALIFICATION.md`, `CANDIDATE_READINESS_2.2.0_RC1.md`, `RC1_QUALIFICATION_2.2.0.md`, `ACCEPTANCE_2.2.0.md`, `CANONICAL_ADOPTION_2.2.0.md`.

Canonical adoption is prospective from 2026-10-02. Existing child projects are not migrated automatically and retain their project-recorded OM pins until separate safe-boundary adoption.
