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

The immutable release tag `om-v2.0.0` remains normative authority. Post-release development and evidence on `main` do not mutate the current canonical release bytes.

## OM 2.1 lineage

Qualified source candidate:

- candidate: `OM2-2.1.0-RC1`;
- immutable candidate tag: `om-v2.1.0-rc1`;
- exact candidate commit: `02a4a3f5004fd497b2e4e6402b508c1a29802c35`;
- disposition: FROZEN / QUALIFIED PASS / NON-CANONICAL.

RC1 acceptance review: PASS.

The first GA release attempt `om-v2.1.0` is preserved as **NOT_ACCEPTED_FOR_GA / RELEASE_CONTROL_DEVIATION** because its immutable tag resolved to a later commit than the exact G2 promotion pin. See `GA_DISPOSITION_2.1.0.md`.

This was not an OM product defect. The only intervening change was CI trigger/concurrency topology in `.github/workflows/validate.yml`.

## OM 2.1.1 patch successor

Current release target on `main`: `2.1.1`.

The 2.1.1 patch preserves the qualified OM 2.1 normative behavior and remedies the release-control identity race prospectively.

Required before acceptance:

- protected PR;
- structural CI;
- exact post-merge promotion commit capture;
- no unexpected normative diff from the qualified OM 2.1 line;
- new immutable identity `om-v2.1.1` created only on that exact commit;
- exact tag-bound hosted validation on `om-v2.1.1`;
- separate release acceptance.

The current canonical authority remains `om-v2.0.0` until a later accepted immutable release is explicitly adopted prospectively.
