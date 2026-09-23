# AI-Assisted Development Operating Model

## Current canonical authority

**Canonical version:** `2.0.0`  
**Canonical tag:** `om-v2.0.0`  
**Exact canonical commit:** `769497a3477cfe5cc676d1ba972728404e9b3551`  
**Status:** CURRENT CANONICAL OPERATING MODEL

The immutable GitHub release identified above remains the normative authority until a later release is explicitly adopted prospectively.

## OM 2.1 qualification lineage

Qualified candidate:

- `OM2-2.1.0-RC1`;
- tag `om-v2.1.0-rc1`;
- exact commit `02a4a3f5004fd497b2e4e6402b508c1a29802c35`;
- FROZEN / QUALIFIED PASS / NON-CANONICAL.

RC1 acceptance review passed.

The first GA release attempt `om-v2.1.0` is **not accepted for GA**. Its immutable tag was created on commit `3fa66871aa41b9e677f5ebb6ffb2c473a78673de` rather than the exact G2 promotion commit `3bcc928251286e9988b20afc67bdd7832d135ed3`.

The intervening change affected only `.github/workflows/validate.yml` CI trigger/concurrency behavior. No OM product semantics changed. The release attempt remains immutable historical evidence and is documented in `GA_DISPOSITION_2.1.0.md`.

## OM 2.1.1 patch successor

Current release target: `2.1.1`.

This is a PATCH-class prospective recovery under `OM_RELEASE_POLICY.md` because the recovery addresses tooling/release-control coherence without changing normative behavior.

The patch preserves the qualified OM 2.1 capability scope:

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

Before OM 2.1.1 can be accepted:

1. protected PR and structural CI must pass;
2. exact post-merge promotion SHA must be captured;
3. the final diff must contain no unexpected normative behavior change;
4. immutable tag `om-v2.1.1` must be created on that exact SHA;
5. tag-bound hosted validation must succeed on that exact identity;
6. release acceptance must be recorded.

Canonical adoption remains a separate explicit prospective event. No child-project adoption is implied by release promotion or OM-level adoption.
