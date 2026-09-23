# Operating Model 2.0 Canonical Index

**Version:** `2.0.0`  
**Status:** CURRENT CANONICAL OPERATING MODEL  
**Canonical tag:** `om-v2.0.0`  
**Exact canonical commit:** `769497a3477cfe5cc676d1ba972728404e9b3551`

## Canonical entrypoints

- Machine manifest: `OM.yaml`
- Universal kernel: `CORE.md`
- Profiles: `profiles/`
- Triggered playbooks: `playbooks/`
- Universal schemas: PROJECT v2, ACTIVE_STATE v2, EXTERNAL_SOURCES v1, EVIDENCE_RECORD v2
- DEV templates: `templates/DEV/`
- Validator: `tools/validate.py`

## Qualification and adoption

- RC1 qualification: `RC1_QUALIFICATION.md`
- RC1 root cause: `RC1_ROOT_CAUSE.md`
- Cross-profile qualification: `CROSS_PROFILE_QUALIFICATION.md`
- DEV evidence parity qualification: `DEV_PARITY_QUALIFICATION.md`
- RC2 qualification: `RC2_QUALIFICATION.md`
- Release acceptance: `ACCEPTANCE_2.0.0.md`
- Canonical adoption record: `CANONICAL_ADOPTION_2.0.0.md`

The immutable release tag `om-v2.0.0` is normative authority. Post-release evidence on `main` does not mutate the canonical release bytes.

## OM 2.1 release promotion

OM 2.1.0 has passed RC1 acceptance review and is being promoted as an accepted non-canonical release line.

Qualified source candidate:

- candidate: `OM2-2.1.0-RC1`;
- immutable candidate tag: `om-v2.1.0-rc1`;
- exact candidate commit: `02a4a3f5004fd497b2e4e6402b508c1a29802c35`;
- disposition: FROZEN / QUALIFIED PASS / NON-CANONICAL.

Promotion is controlled by:

- `ACCEPTANCE_2.1.0.md`;
- `GA_PROMOTION_PLAN_2.1.0.md`.

The current canonical authority remains `om-v2.0.0` until OM 2.1.0 receives its own immutable GA identity, passes exact tag-bound hosted qualification and GA acceptance, and is then explicitly adopted prospectively.
