# OM2-2.0.0-RC1 — Candidate Qualification

**Candidate:** `om-v2.0.0-rc1`  
**Commit:** `fbb591711ca124ba7dc16914ab4e7a9d176aae4d`  
**Disposition:** **FAILED_QUALIFICATION / PRODUCT / NOT_ACCEPTED / DO_NOT_MODIFY**

## Freeze integrity

PASS.

The candidate tag points to the exact frozen commit and is protected by the active `OM2 version tags` ruleset against update and deletion, with no bypass actors.

## Tag-bound structural qualification

PASS.

Creation of the candidate tag triggered `Validate OM2` directly on `om-v2.0.0-rc1`.

GitHub Actions run:

- run id: `35525071180`;
- head ref: `om-v2.0.0-rc1`;
- head SHA: `fbb591711ca124ba7dc16914ab4e7a9d176aae4d`;
- result: `SUCCESS`.

The candidate tree was read back completely (`truncated=false`).

## Cross-profile semantic qualification

FAIL — PRODUCT.

The frozen `PROJECT.schema.json` requires, for every project profile:

- `repository.platform` to be one of `github`, `gitlab`, `azure_devops`, or `git_other`;
- `state.active` to equal `.project/ACTIVE_STATE.yaml`.

That is valid for the Git-native DEV implementation, but it is not a valid universal contract for all five profiles.

The candidate's own profile semantics permit non-Git authority for durable solution/document/experiment/light work. In particular:

- SOLUTION requires one authoritative control plane, not necessarily Git;
- DOCUMENT allows a declared document/source repository as authority and generated outputs as derivative;
- EXPERIMENT requires one declared authority for persistent experiment state, not necessarily Git;
- LIGHT requires one declared source of truth and minimal persisted state, not necessarily Git.

Therefore the universal machine contract is narrower than the normative profile semantics.

## Root-cause classification

`PRODUCT`

The defect is in the frozen OM2 contract design, not in the qualification harness, environment or authorization.

## Consequence

RC1 remains immutable failed evidence and SHALL NOT be repaired in place.

No canonical adoption of RC1 is permitted.

Development returns to a successor revision where the universal bootstrap contract is separated from DEV/Git-specific implementation constraints. A later candidate, if eligible, receives a new immutable identity (RC2 or later).

## Safety / authority

Canonical Operating Model remains v1.6.

SPC remains governed by OM v1.6.

No SPC authority migration, connected mutation, destructive action or PROD action is authorized by this qualification.
