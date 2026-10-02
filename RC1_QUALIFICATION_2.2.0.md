# OM 2.2.0-rc1 — Candidate Qualification

**Status:** RC1 QUALIFICATION PASS — NON-CANONICAL
**Candidate identity:** `OM2-2.2.0-RC1`
**Tag:** `om-v2.2.0-rc1` (annotated, tag object `7779f7fc6f0d7f55dc67b26a748fca97a75c723b`) -> commit `f0a8fa5b0c945a6ed684db67bbf21b6baf8328c1`
**Date:** 2026-10-02

Freeze evidence: `qualification/evidence/OM2-2.2.0-RC1_FREEZE_PASS.json`. GitHub Release `OM 2.2.0 RC1` is published as Pre-release; `OM 2.1.3` remains the latest release.

This record does not make OM 2.2 canonical and does not adopt OM 2.2 in any child project.

## A. Local qualification on the immutable tag

Checkout of `om-v2.2.0-rc1` (`f0a8fa5`), all `run` steps of `validate.yml` executed with `bash -eo pipefail`: **12 of 12 steps exit 0** (structural contracts, minimal and solo recovery, OM 2.1 policy semantics, release identity pin guard, runtime guard, runtime gate modes, runtime map maintenance, pin reference finder, bootstrap conformance positive/negative controls, uninstantiated DEV template rejection).

- `OM.yaml` declares `2.2.0-rc1` / `non_canonical_candidate`.
- Difference between the qualified development head `a4a0681` and the tag: only `OM.yaml`, `README.md`, `00_INDEX.md`, `OM_2.2_PRE_CANDIDATE_QUALIFICATION.md` and the new `CANDIDATE_READINESS_2.2.0_RC1.md`. No normative file, tool, workflow, schema or template differs.
- Tag-triggered `Validate OM2` run `36999398621` on `f0a8fa5`: SUCCESS.

## B. Tag-bound hosted shadow pilot (AAE)

Draft pull request [AAE #70](https://github.com/ro-pecha-labs/aae-application-authorization-engine/pull/70) (`[PILOT RC1 - DO NOT MERGE]`, branch `shadow/om-2.2-rc1-q6`, head `7969d76fb569e9080b15010141a27d77de8f74e2`, base `393bc16`): `.project/PROJECT.yaml` pinned to `om-v2.2.0-rc1` / `f0a8fa5` and a caller with two jobs calling the reusable workflow `project-state-conformance.yml@om-v2.2.0-rc1`.

Run `36999806715`: **success**. The run metadata references `refs/tags/om-v2.2.0-rc1` (`7779f7fc…`); the job log of the enforce job states the same reference and the inputs `om_ref: om-v2.2.0-rc1`, `actions_runtime: enforce`, and the checkout of the adopted OM at `f0a8fa5`.

| Job | Conclusion | Evidence read |
|---|---|---|
| `conformance-enforce` | success | job log text: `PASS: exact OM commit pin f0a8fa5…`, `PROJECT BOOTSTRAP CONFORMANCE PASS`, `PASS: 36 mapped action reference(s), 0 unjudged official action reference(s) in 22 file(s); no mapped reference is below its Node.js 24 major` |
| `conformance-report` | success | job and step conclusions from the Actions API (all steps success, including "GitHub Actions runtime check"); log text not read separately |

The numbers (36 mapped references, 22 files, no deprecated reference) agree with the Q6 local dry run of the same AAE base.

## Closed limits from the readiness record

- Limit 1 (summary/annotation text not read): closed for the enforce job through the job log text above. Not closed for the `conformance-report` job and for DVC; the job summary file itself was not read.
- Limit 2 (workflow called at a commit, not at a tag): **closed** (called at `om-v2.2.0-rc1`).
- Limit 3 (hosted run of the manual runtime map refresh workflow): remains open; it is a manual advisory workflow and not part of the candidate gate.

DVC (216 deprecated references) was not repeated on the tag. Its enforce failure is evidenced by Q6 on the pre-candidate commit; the gate and workflow bytes are identical on the tag.

## Verdict

**RC1 qualification: PASS.** OM 2.2.0 may proceed to GA promotion planning. GA promotion shall preserve the normative bytes and change only release identity and status text, as for OM 2.1.0.

Pilot pull request AAE #70 is to be closed without merging; branches `shadow/om-2.2-pilot-q6` and `shadow/om-2.2-rc1-q6` are retained as evidence references until the owner decides otherwise.

## Non-canonical boundary

Canonical authority remains `om-v2.1.3` (`ed816aa46694b44b681f9453aaef3d0458ed0d79`). No child project is migrated by RC1.
