# OM 2.1 — RC1 Candidate Readiness

**Status:** READY_TO_FREEZE — NON-CANONICAL
**Target candidate identity:** `OM2-2.1.0-RC1`
**Target immutable tag:** `om-v2.1.0-rc1`
**Pre-freeze development baseline:** `adb7a106b9538b95690385fa02a1fea2dca693a6`

## Purpose

Determine whether the OM 2.1 line is eligible for its first immutable release candidate after completion of Q0-Q5 pre-candidate qualification.

This record does not make OM 2.1 canonical and does not adopt OM 2.1 in any child project.

## Scope of OM 2.1

OM 2.1 is a backward-compatible MINOR release line introducing:

- optional cross-profile `assurance.mode: solo`;
- Solo Assurance playbook;
- vendor-neutral AI Development Loop;
- proportional DEV lightweight/formal release semantics;
- machine-grounded evidence rules for machine-verifiable claims;
- project-state conformance enforcement;
- governance materiality and efficiency guidance;
- GitHub execution/storage efficiency guidance;
- release-safe template semantics.

The five primary profiles remain unchanged.

## Pre-candidate qualification

Q0-Q5: **PASS**.

Evidence:

- structural/backward compatibility: PASS;
- all-profile solo fixtures: PASS;
- invalid assurance mode negative control: PASS;
- DEV lightweight/formal policy cases: PASS;
- solo/AI assurance policy cases: PASS;
- standard + solo recovery regression: PASS;
- reusable project-bootstrap validator positive/negative controls: PASS;
- representative SPC shadow pilot: PASS.

Representative SPC shadow evidence:

- source SPC main: `599dadc8cc01af419ecf2178e70c31a539d9008c`;
- shadow success commit: `fb8157ce16f627170520747de2d35c1e8c9ea26d`;
- workflow run: `35839945652`;
- project-state conformance: PASS;
- bounded solo recovery: PASS;
- bootstrap files read: 2;
- bootstrap bytes: 2,584;
- historical reconstruction: false;
- legacy handoff: false.

See `OM_2.1_PRE_CANDIDATE_QUALIFICATION.md` and `OM_2.1_Q5_SPC_SHADOW_ACCEPTANCE.md`.

## Recurrence and defect disposition

Known material defect/control classes discovered during development have prospective controls:

1. stale component-local release status -> removed from normative components and guarded by validation;
2. candidate-era release pin in distributed template -> replaced by release-independent sentinel template;
3. uninstantiated template use -> rejected by project bootstrap conformance;
4. post-adoption Active State / external-source drift -> continuous path-scoped project-state conformance;
5. duplicate feature-branch push + PR CI -> ordinary feature/dev branches qualify through PR, while main/candidate/release/tag events retain push coverage;
6. YAML fixture all-zero commit parse defect -> preserved as HARNESS/FIXTURE failure and corrected without weakening schema or expected behavior;
7. project-state overgrowth temptation -> bounded schema retained; history/detail remains outside the recovery index.

No known unresolved recurrence class blocks RC1 freeze.

## Release-safe template qualification

The DEV template no longer embeds an RC or GA release pin.

It contains explicit non-usable sentinels:

- `ref: REPLACE_WITH_ADOPTED_IMMUTABLE_OM_REF`;
- all-zero 40-hex commit sentinel.

The OM structural validator verifies the template sentinel contract.

The project bootstrap conformance validator rejects those sentinels in a real instantiated project.

This prevents promotion of unchanged qualified candidate bytes from leaving a stale RC pin in a GA template.

## Platform integrity

Fresh repository read shows both organization rulesets active:

- `OM2 main protection`;
- `OM2 version tags`.

Protected-main post-merge validation for pre-freeze development baseline `adb7a106...` completed SUCCESS in workflow run `35842776160`.

The connector did not expose detailed ruleset subresources in this readiness pass, so this record does not restate unverified individual rule clauses. Candidate freeze therefore additionally requires physical tag creation and read-back plus tag-triggered hosted validation.

## Candidate source identity

This readiness change changes internal OM identity only:

- `2.1.0-dev` -> `2.1.0-rc1`;
- `non_canonical_development` -> `non_canonical_candidate`.

No normative feature semantics are added in this readiness change.

The exact RC1 source SHA is not known until this readiness change is merged through protected `main`.

## Freeze conditions

RC1 may be frozen only after:

1. this exact readiness change is merged through protected `main`;
2. resulting exact `main` SHA completes hosted validation = SUCCESS;
3. immutable tag `om-v2.1.0-rc1` is created on that exact SHA;
4. fresh read-back confirms tag -> exact SHA;
5. tag-triggered hosted validation succeeds;
6. RC1 freeze evidence records exact source/tag/run identity.

If any condition fails, no RC1 PASS claim is made.

## Candidate qualification after freeze

After successful freeze, qualify the exact immutable RC1 identity.

At minimum:

- structural validation on the tag;
- all-profile regression;
- solo/standard recovery regression;
- project-state conformance positive/negative controls;
- deterministic release/solo/AI policy cases;
- release-safe template checks.

If RC1 fails, preserve it as immutable failed evidence and remediate in RC2 or later. Do not patch RC1 in place.

## Non-canonical boundary

Canonical authority remains:

- `om-v2.0.0`;
- exact canonical commit `769497a3477cfe5cc676d1ba972728404e9b3551`.

No child project is migrated by RC1 freeze.
