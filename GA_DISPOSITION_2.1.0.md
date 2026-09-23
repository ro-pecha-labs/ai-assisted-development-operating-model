# OM 2.1.0 — GA Release Attempt Disposition

**Status:** NOT_ACCEPTED_FOR_GA / RELEASE_CONTROL_DEVIATION / IMMUTABLE_EVIDENCE  
**Tag:** `om-v2.1.0`  
**Observed tag commit:** `3fa66871aa41b9e677f5ebb6ffb2c473a78673de`  
**Intended G2 promotion commit:** `3bcc928251286e9988b20afc67bdd7832d135ed3`

## Summary

The immutable GA tag `om-v2.1.0` was created after an unrelated CI-control commit was merged to `main`.

The controlled GA promotion plan required the tag to resolve to the exact G2-validated promotion commit:

`3bcc928251286e9988b20afc67bdd7832d135ed3`

Fresh read-back instead confirmed:

`om-v2.1.0 -> 3fa66871aa41b9e677f5ebb6ffb2c473a78673de`

This is an explicit STOP condition under `GA_PROMOTION_PLAN_2.1.0.md`.

## Intervening change

The only commit between the intended promotion commit and the observed GA tag commit is PR #24:

`CI: contain OM validation to PR and canonical publication boundaries`

Diff scope:

- only `.github/workflows/validate.yml`;
- removal of duplicate candidate/release branch push triggers;
- addition of workflow concurrency / cancel-in-progress;
- no CORE, profile, playbook, schema, template, validator semantics, policy semantics or recovery behavior changed.

The change is classified as release/tooling control-plane, not an OM PRODUCT defect.

## Qualification facts

The observed GA identity itself completed exact tag-bound hosted validation:

- run: `35854145416`;
- head ref: `om-v2.1.0`;
- head SHA: `3fa66871aa41b9e677f5ebb6ffb2c473a78673de`;
- conclusion: `SUCCESS`.

The same commit also passed main-bound hosted validation:

- run: `35854086367`;
- head SHA: `3fa66871aa41b9e677f5ebb6ffb2c473a78673de`;
- conclusion: `SUCCESS`.

These successful validations do not erase the release-control deviation or retroactively satisfy the exact G2 pin requirement.

## Historical integrity

The tag `om-v2.1.0` is protected and shall not be moved, deleted or rewritten.

It remains immutable evidence of a non-accepted GA release attempt.

Canonical authority remains:

- tag: `om-v2.0.0`;
- exact commit: `769497a3477cfe5cc676d1ba972728404e9b3551`.

No child-project adoption is implied.

## Recovery path

The release policy classifies a tooling/coherence correction that does not change normative behavior as PATCH.

Prospective recovery therefore proceeds through OM `2.1.1`:

- no RC is required unless a new product-semantic defect or material cross-profile risk is discovered;
- protected PR and structural CI are required;
- targeted regression for this release-control race is required;
- a new immutable tag `om-v2.1.1` must be created only after an exact promotion commit is frozen and fresh-read;
- the tag-bound hosted run must execute on that exact commit;
- canonical adoption remains a separate explicit event.

OM 2.1.0 shall not be reinterpreted as accepted GA.
