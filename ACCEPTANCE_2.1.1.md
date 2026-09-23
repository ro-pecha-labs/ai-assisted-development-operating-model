# OM 2.1.1 — GA Acceptance

**Status:** ACCEPTED_RELEASE / NON-CANONICAL  
**Accepted tag:** `om-v2.1.1`  
**Exact accepted commit:** `df9812815a3a83c39b49c66035b4795acd777fc7`  
**Acceptance date:** 2026-09-23

## Basis

OM 2.1.1 is accepted as the GA release successor for the qualified OM 2.1 line.

The accepted identity is the immutable Git tag:

`om-v2.1.1 -> df9812815a3a83c39b49c66035b4795acd777fc7`

The GitHub release is:

- title: `OM 2.1.1`;
- prerelease: `false`;
- draft: `false`;
- target commitish: exact commit `df9812815a3a83c39b49c66035b4795acd777fc7`.

## Qualification evidence

Pre-tag protected PR qualification:

- PR: #25;
- head SHA: `84a8bc19679a70c4ba136d589f5a1ef0044f193a`;
- workflow run: `35854502407`;
- event: `pull_request`;
- conclusion: `SUCCESS`.

Exact post-merge main qualification:

- exact main SHA: `df9812815a3a83c39b49c66035b4795acd777fc7`;
- workflow run: `35854539820`;
- event: `push`;
- conclusion: `SUCCESS`.

Exact immutable tag-bound qualification:

- tag: `om-v2.1.1`;
- exact head SHA: `df9812815a3a83c39b49c66035b4795acd777fc7`;
- workflow run: `35854783610`;
- event: `push`;
- conclusion: `SUCCESS`.

## Release-control recurrence prevention

OM 2.1.1 contains a deterministic release identity pin guard:

`tools/release_identity_guard.py`

The hosted validation workflow includes both:

- positive equality validation for expected vs. observed full Git SHA;
- negative mismatch rejection.

This control was introduced after the OM 2.1.0 release-control deviation documented in:

`GA_DISPOSITION_2.1.0.md`

The immutable `om-v2.1.0` tag remains historical evidence and is not reinterpreted as accepted GA.

## Tag protection

The active organization ruleset `OM2 version tags` applies to:

`refs/tags/om-v*`

It enforces:

- deletion blocked;
- update blocked;
- no bypass actors;
- current user cannot bypass.

The immutable Git tag is the authoritative release identity. GitHub Release metadata is descriptive and does not override the tag ref.

## Product and semantic disposition

No unresolved OM PRODUCT defect was found in the 2.1.1 acceptance path.

The 2.1.1 patch preserves the qualified OM 2.1 normative behavior. The patch recovery changed release identity/coherence and tooling/release-control safeguards, not the qualified OM semantics.

The qualified OM 2.1 capability scope remains:

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

The five primary profiles remain unchanged:

- DEV;
- SOLUTION;
- DOCUMENT;
- EXPERIMENT;
- LIGHT.

## Canonical authority

Acceptance of OM 2.1.1 does **not** itself perform canonical adoption.

Current canonical authority remains:

- version: `2.0.0`;
- tag: `om-v2.0.0`;
- exact commit: `769497a3477cfe5cc676d1ba972728404e9b3551`.

Prospective canonical adoption of OM 2.1.1 requires a separate explicit human authorization and governance-index update.

No child project is migrated or re-pinned by this acceptance record.
