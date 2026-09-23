# OM 2.1.0 — GA Promotion Plan

**Status:** READY_FOR_EXECUTION / NON-CANONICAL  
**Source candidate:** `om-v2.1.0-rc1`  
**Source candidate commit:** `02a4a3f5004fd497b2e4e6402b508c1a29802c35`  
**Current canonical OM:** `om-v2.0.0`

## Objective

Promote the qualified OM 2.1 RC1 semantics to immutable GA identity `om-v2.1.0` without changing qualified normative behavior, without reintroducing stale RC status/pins, and without conflating GA release with canonical adoption.

## Invariants

The promotion shall preserve all RC1 normative bytes for:

- `CORE.md`;
- all files under `profiles/`;
- all normative playbooks under `playbooks/`;
- schemas under `schemas/`;
- DEV distributed templates except release-identity text if any future review proves such text exists;
- validators and qualification tooling;
- deterministic policy fixtures;
- recovery probes and project-state conformance behavior.

No product-semantic change is permitted in the GA promotion commit.

If a PRODUCT defect is found before GA freeze, stop promotion. Preserve RC1 unchanged and prepare RC2 or later.

## Phase G0 — Merge acceptance evidence

1. Merge the acceptance-readiness PR through protected `main`.
2. Require hosted `Validate OM2` SUCCESS on the resulting exact `main` SHA.
3. Fresh-read `main`, RC1 tag, and tag ruleset.
4. Confirm no normative files changed since RC1 other than explicitly allowed release metadata/evidence.

This phase does not create GA identity.

## Phase G1 — Prepare release-identity-only promotion change

Create a fresh promotion branch from the exact validated G0 `main`.

Allowed modifications are bounded to release identity/status and human-readable release-state coherence:

1. `OM.yaml`
   - `operating_model.version: 2.1.0`
   - `operating_model.status: accepted_release`

2. `00_INDEX.md`
   - remove wording that presents `2.1.0-rc1` as the current development target;
   - state that OM 2.1.0 is accepted for release / non-canonical pending GA identity qualification and explicit canonical adoption;
   - keep `om-v2.0.0` as current canonical authority.

3. `README.md`
   - remove stale RC1-development wording;
   - state that OM 2.1.0 is an accepted non-canonical release line pending immutable GA tag qualification and later explicit canonical adoption;
   - keep `om-v2.0.0` as current canonical authority.

4. Optional release/acceptance evidence files only, if needed to record the operation.

Do not insert a guessed GA commit SHA before the promotion commit exists. Do not embed a mutable branch pin as GA authority.

## Phase G2 — Pre-tag promotion validation

1. Merge the release-identity-only PR through protected `main`.
2. Capture the resulting exact promotion commit SHA.
3. Require hosted `Validate OM2` SUCCESS on that exact SHA.
4. Compare frozen RC1 commit to the promotion commit.

The compare gate must show that:
- normative behavior files are unchanged;
- only release identity/status metadata, acceptance/release evidence and human-readable release-state text changed.

Any unexpected normative diff is a STOP condition.

## Phase G3 — Freeze exact GA identity

Only after G2 PASS:

1. Create lightweight or annotated Git tag `om-v2.1.0` on the exact validated promotion commit SHA.
2. Do not move or recreate the tag.
3. Fresh-read `refs/tags/om-v2.1.0` and confirm it resolves to the exact promotion SHA.
4. Re-read ruleset `OM2 version tags` and confirm:
   - target includes `refs/tags/om-v*`;
   - deletion blocked;
   - update blocked;
   - bypass actors empty;
   - current user cannot bypass.
5. Publish GitHub release `OM 2.1.0` for tag `om-v2.1.0` as a normal release, not a pre-release.

The protected tag is the immutable GA identity. Mutable release metadata is not the authority.

## Phase G4 — Exact tag-bound hosted qualification

Creation of `om-v2.1.0` must trigger `Validate OM2` via the existing `push.tags: om-v*` workflow rule.

Require:

- event: `push`;
- head ref: `om-v2.1.0`;
- head SHA: exact G2 promotion SHA;
- conclusion: `success`.

Required gates remain the same as the qualified candidate line:

- structural contracts;
- standard recovery;
- solo recovery;
- OM 2.1 policy semantics;
- reusable project-bootstrap conformance;
- invalid bootstrap rejection;
- uninstantiated DEV-template rejection.

A failed GA tag-bound run means GA acceptance does not pass. Because the tag is immutable, do not patch or move `om-v2.1.0`; diagnose and use a prospective successor identity according to release policy.

## Phase G5 — Persist GA qualification evidence

After exact tag-bound SUCCESS, add post-tag evidence to `main` without mutating the GA tag:

- GA exact tag and commit identity;
- tag ruleset read-back;
- hosted run id, event, head ref, head SHA and conclusion;
- RC1-to-GA normative equivalence review;
- release metadata read-back.

Post-tag evidence commits are not part of the immutable GA release bytes and shall not be represented as such.

## Phase G6 — Separate GA acceptance

Perform an explicit GA acceptance review after G4/G5.

GA acceptance may conclude `ACCEPTED_RELEASE / NON-CANONICAL` only if:

- immutable GA identity is verified;
- tag-bound hosted qualification is SUCCESS;
- normative-equivalence gate is PASS;
- no unresolved PRODUCT defect exists.

GA acceptance still does not make OM 2.1 canonical.

## Phase G7 — Explicit prospective canonical adoption

Canonical adoption is a separate human-authorized event.

Only after explicit authorization:

1. update the Google Drive `Projekty/00_OPERATING_MODEL/00_OPERATING_MODEL_INDEX.md` to point current canonical authority to `om-v2.1.0` and its exact commit;
2. preserve the previous OM 2.0 index state as historical authority evidence as appropriate;
3. persist `CANONICAL_ADOPTION_2.1.0.md`;
4. verify Drive read-back and GitHub immutable identity;
5. keep all child projects on their existing adopted OM until each project performs its own explicit safe-boundary adoption.

No child-project migration is implied by OM-level canonical adoption.

## Explicit stop conditions

Stop and do not create or accept GA if any of the following occurs:

- RC1 tag no longer resolves to `02a4a3f5004fd497b2e4e6402b508c1a29802c35`;
- tag ruleset loses update/deletion protection or gains bypass;
- an unexpected normative diff appears after RC1;
- pre-tag promotion validation fails;
- GA tag read-back does not resolve to the intended promotion commit;
- tag-bound hosted qualification fails;
- a PRODUCT defect is discovered.

A PRODUCT defect requires RC2 or later. RC1 remains immutable.

## Current boundary

This plan is preparatory only. Until G3 is deliberately executed and G4/G6 pass:

- `om-v2.0.0` remains canonical;
- `om-v2.1.0-rc1` remains frozen, qualified and non-canonical;
- no child project adopts OM 2.1.
