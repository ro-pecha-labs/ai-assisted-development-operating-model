# OM 2.2 — RC1 Candidate Readiness

**Status:** READY_TO_FREEZE — NON-CANONICAL
**Target candidate identity:** `OM2-2.2.0-RC1`
**Target immutable tag:** `om-v2.2.0-rc1`
**Pre-freeze development baseline:** `a4a068133bf31d98d63ec1a307ce293c2fd82204` (`release/om-2.2`)

## Purpose

Determine whether the OM 2.2 line is eligible for its first immutable release candidate after completion of Q0–Q7 pre-candidate qualification.

This record does not make OM 2.2 canonical and does not adopt OM 2.2 in any child project.

## Scope of OM 2.2

OM 2.2 is a backward-compatible MINOR release line (target `2.2.0`) introducing:

- optional enforcement of the Node.js runtime check in the reusable project-state conformance workflow (`actions_runtime: report|enforce`, default `report`; `tools/actions_runtime_gate.py`);
- fail-closed `enforce` against an adopted OM revision that lacks the gate;
- data-driven runtime map maintenance (`schemas/ACTIONS_RUNTIME_MAP.v1.schema.json`, advisory refresh tool and manual workflow);
- pin reference finder and complete-tree pin search step in the adoption playbook (`tools/find_pin_references.py`);
- hosted conformance caller guidance (`platforms/github/PROJECT_STATE_CONFORMANCE.md`).

Profiles, schemas of project state, templates and recovery behavior are unchanged. Conformance pass/fail of a caller that does not set `actions_runtime` is unchanged from 2.1.3.

## Pre-candidate qualification

Q0–Q7: **PASS** (`OM_2.2_PRE_CANDIDATE_QUALIFICATION.md`).

- structural and backward compatibility, default `report` preserved: PASS;
- enforce mode positive/negative controls and `UNJUDGED` handling: PASS;
- runtime map schema, invalid maps, refresh tool: PASS;
- pin reference finder incl. sparse checkout and partial clone fail-closed: PASS;
- shadow pilot (owner-authorized, read-only): AAE `report` success / `enforce` success; DVC `report` success / `enforce` failure at the runtime check, as designed (216 deprecated references in the local dry run);
- recovery and all-profile regression: PASS.

Work packages merged through protected `release/om-2.2`: PR #36, #37, #38, #39, #40; qualification records PR #41, #42. Latest hosted validation on the baseline: workflow run `36998414211` SUCCESS.

## Known limits (do not block RC1)

1. Q6 job/step conclusions were read from the Actions API; the text of job summaries and annotations was not read.
2. The pilot called the reusable workflow at a commit, not at a release tag. The tag-bound call is evidenced after freeze.
3. A hosted run of the manual runtime map refresh workflow is not evidenced (same command run locally).
4. The pilot pull requests were closed unmerged on 2026-10-02; branches `shadow/om-2.2-pilot-q6` are retained as evidence references.

## Recurrence and defect disposition

1. Pin oracle missed by working-tree search in a partial clone (DVC test oracle) -> `tools/find_pin_references.py` reads Git objects and fails closed on missing objects; adoption playbook step 4 requires a complete-tree pin search.
2. Non-gating runtime report only (2.1.3) -> optional enforce mode with fail-closed behavior.
3. Hardcoded runtime knowledge -> data map with schema, `verified_on` date and advisory refresh.
4. RC/GA byte divergence risk and sparse-clone behavior (Codex review of PR #36) -> fixed and verified before WP1.

No known unresolved recurrence class blocks RC1 freeze.

## Release-safe template qualification

The DEV template is unchanged and still carries explicit non-usable sentinels (`REPLACE_WITH_ADOPTED_IMMUTABLE_OM_REF`, all-zero commit). Project bootstrap conformance rejects them in a real instantiated project.

## Candidate source identity

This readiness change changes internal OM identity and status text only:

- `OM.yaml`: `2.1.3` -> `2.2.0-rc1`; `accepted_release` -> `non_canonical_candidate`;
- `README.md`, `00_INDEX.md`: 2.2 section changed from development line to candidate line;
- `OM_2.2_PRE_CANDIDATE_QUALIFICATION.md`: remaining-items list updated.

No normative semantics, workflow, tool, schema or template is changed in this readiness change.

The exact RC1 source SHA is not known until this change is merged through protected `release/om-2.2`.

## Freeze conditions

RC1 may be frozen only after:

1. this exact readiness change is merged through protected `release/om-2.2`;
2. the resulting exact SHA completes hosted validation = SUCCESS;
3. immutable annotated tag `om-v2.2.0-rc1` is created by the owner on that exact SHA;
4. fresh read-back confirms tag -> exact SHA;
5. tag-triggered hosted validation succeeds;
6. RC1 freeze evidence records exact source/tag/run identity.

If any condition fails, no RC1 PASS claim is made.

## Candidate qualification after freeze

Qualify the exact immutable RC1 identity: structural validation on the tag, all-profile and recovery regression, enforce/report gate controls, pin finder controls, and one hosted call of the reusable workflow at tag `om-v2.2.0-rc1` (closes known limit 2).

If RC1 fails, preserve it as immutable failed evidence and remediate in RC2 or later. Do not patch RC1 in place.

## Non-canonical boundary

Canonical authority remains `om-v2.1.3` (exact commit `ed816aa46694b44b681f9453aaef3d0458ed0d79`). No child project is migrated by RC1 freeze.
