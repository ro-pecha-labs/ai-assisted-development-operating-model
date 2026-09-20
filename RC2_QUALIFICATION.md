# OM2-2.0.0-RC2 — Candidate Qualification

**Candidate:** `om-v2.0.0-rc2`  
**Commit:** `c5eee28bd8c8765824ac7f699be828018b92f5fb`  
**Disposition:** **FROZEN / QUALIFIED PASS / NON-CANONICAL**

## Freeze integrity

PASS.

Fresh GitHub read-back confirms:

- tag `om-v2.0.0-rc2` points directly to exact commit `c5eee28bd8c8765824ac7f699be828018b92f5fb`;
- release title is `OM2-2.0.0-RC2`;
- release is published as Pre-release;
- the active `OM2 version tags` ruleset applies to `refs/tags/om-v*`;
- tag update is blocked;
- tag deletion is blocked;
- there are no bypass actors;
- current user cannot bypass the ruleset.

## Candidate source identity

PASS.

The frozen candidate bytes already declare:

- version: `2.0.0-rc2`;
- status: `non_canonical_candidate`.

The candidate source was merged through protected `main` before tag creation.

## Protected-main validation

PASS.

The exact candidate source commit completed hosted `structural-validation = SUCCESS` before freeze.

## Tag-bound hosted qualification

PASS.

Creating `om-v2.0.0-rc2` triggered `Validate OM2` directly on the candidate tag.

GitHub Actions:

- run id: `35526350361`;
- event: `push`;
- head ref: `om-v2.0.0-rc2`;
- head SHA: `c5eee28bd8c8765824ac7f699be828018b92f5fb`;
- result: `SUCCESS`.

## Cross-profile qualification

PASS before freeze.

The universal v2 contracts were qualified against all five normative profiles:

- DEV;
- SOLUTION;
- DOCUMENT;
- EXPERIMENT;
- LIGHT.

The qualification includes non-Git control-plane scenarios for non-DEV profiles and negative controls for invalid mixed authority declarations, duplicated ACTIVE_STATE history and unclassified FAIL evidence.

See `CROSS_PROFILE_QUALIFICATION.md`.

## DEV regression / parity qualification

PASS before freeze.

The v2 successor preserves profile-neutral evidence identity while retaining DEV evidence capabilities for:

- artifacts + digest identity;
- semantic plan digest;
- authorized operation set;
- durable evidence archive.

See `DEV_PARITY_QUALIFICATION.md`.

## RC1 lineage

RC1 remains immutable failed evidence:

- tag: `om-v2.0.0-rc1`;
- commit: `fbb591711ca124ba7dc16914ab4e7a9d176aae4d`;
- disposition: `FAILED_QUALIFICATION / PRODUCT / NOT_ACCEPTED / DO_NOT_MODIFY`.

RC2 is a prospective successor. RC1 is not repaired or reinterpreted.

## Verdict

**QUALIFIED PASS.**

RC2 is a valid frozen non-canonical candidate for prospective OM 2.0 acceptance/adoption review.

This verdict does not by itself make OM 2.0 canonical.

## Authority boundary

Canonical Operating Model remains v1.6 until an explicit prospective adoption decision is completed.

SPC remains governed by OM v1.6 until its own explicit adoption boundary is authorized and persisted.
