# Operating Model 2.1 Canonical Index

**Version:** `2.1.2`  
**Status:** CURRENT CANONICAL OPERATING MODEL  
**Canonical tag:** `om-v2.1.2`  
**Exact canonical commit:** `78f7390e58ce363c1e734d6beb54c08ac50131c6`

## Canonical entrypoints

- Machine manifest: `OM.yaml`
- Universal kernel: `CORE.md`
- Profiles: `profiles/`
- Triggered playbooks: `playbooks/`
- Universal schemas: PROJECT v2, ACTIVE_STATE v2, EXTERNAL_SOURCES v1, EVIDENCE_RECORD v2
- DEV templates: `templates/DEV/`
- Validator: `tools/validate.py`

The immutable release tag `om-v2.1.2` is the current normative authority. Post-release development and evidence on `main` do not mutate the canonical release bytes.

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

## OM 2.1.2 patch (ACCEPTED RELEASE / CURRENT CANONICAL NORMATIVE AUTHORITY)

- release branch: `release/om-2.1` (from `om-v2.1.1` plus 2.1.1 acceptance/adoption records);
- tag: `om-v2.1.2` → `78f7390e58ce363c1e734d6beb54c08ac50131c6`;
- scope: Node.js 24 action majors in `validate.yml` and `project-state-conformance.yml`; regression guard `tools/actions_runtime_guard.py`;
- class: PATCH (tooling/CI only; normative OM 2.1 behavior unchanged);
- tag-bound validation: `36549211982 / SUCCESS`;
- records: `PATCH_2.1.2.md`, `ACCEPTANCE_2.1.2.md`, `CANONICAL_ADOPTION_2.1.2.md`.

Canonical adoption is prospective from 2026-09-29. Existing child projects are not migrated automatically and retain their project-recorded OM pins until separate safe-boundary adoption.

## OM 2.1.3 patch (ACCEPTED RELEASE / NON-CANONICAL)

- release branch: `release/om-2.1` (from `om-v2.1.2`);
- tag: `om-v2.1.3` → `ed816aa46694b44b681f9453aaef3d0458ed0d79`;
- scope: data-driven Node.js 24 runtime map for official actions (`tools/actions_runtime_map.json`), `UNJUDGED` reporting, non-blocking guard step in `project-state-conformance.yml`;
- class: PATCH (tooling/CI only; conformance pass/fail and normative OM 2.1 behavior unchanged);
- tag-bound validation: `36987775749 / SUCCESS`;
- records: `PATCH_2.1.3.md`, `ACCEPTANCE_2.1.3.md`.

Canonical authority remains `om-v2.1.2`. Acceptance of 2.1.3 is not canonical adoption; no child project is migrated or re-pinned.
