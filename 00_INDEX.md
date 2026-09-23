# Operating Model 2.1 Canonical Index

**Version:** `2.1.1`  
**Status:** CURRENT CANONICAL OPERATING MODEL  
**Canonical tag:** `om-v2.1.1`  
**Exact canonical commit:** `df9812815a3a83c39b49c66035b4795acd777fc7`

## Canonical entrypoints

- Machine manifest: `OM.yaml`
- Universal kernel: `CORE.md`
- Profiles: `profiles/`
- Triggered playbooks: `playbooks/`
- Universal schemas: PROJECT v2, ACTIVE_STATE v2, EXTERNAL_SOURCES v1, EVIDENCE_RECORD v2
- DEV templates: `templates/DEV/`
- Validator: `tools/validate.py`

The immutable release tag `om-v2.1.1` is the current normative authority. Post-release development and evidence on `main` do not mutate the canonical release bytes.

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
- disposition: **ACCEPTED RELEASE / CURRENT CANONICAL NORMATIVE AUTHORITY**.

Canonical adoption is prospective. Existing child projects are not migrated automatically and retain their project-recorded OM pins until separate safe-boundary adoption.
