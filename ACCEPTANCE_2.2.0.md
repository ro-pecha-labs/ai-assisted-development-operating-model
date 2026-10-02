# OM 2.2.0 — GA Acceptance

**Status:** ACCEPTED_RELEASE / NON-CANONICAL  
**Accepted tag:** `om-v2.2.0` (annotated, tag object `b0cd70d84d228deed5631706130ea65fca70c6ca`)  
**Exact accepted commit:** `89de89d0935d61d5442bc8301d9c6c4f2cf7af87`  
**Release class:** MINOR (`OM_RELEASE_POLICY.md`)  
**Acceptance date:** 2026-10-02

## Basis

OM 2.2.0 is accepted as the MINOR successor of OM 2.1.3. It adds optional enforcement of the Node.js runtime check in the reusable project-state conformance workflow (`actions_runtime: report|enforce`, default `report`, fail-closed `enforce` against an OM revision without the gate), runtime map maintenance, a pin reference finder with a complete-tree pin search in the adoption playbook, and hosted conformance caller guidance. Plan and scope: `OM_2.2_QUALIFICATION_PLAN.md`.

The accepted identity is the immutable Git tag:

`om-v2.2.0 -> 89de89d0935d61d5442bc8301d9c6c4f2cf7af87`

The tag is annotated; its commit is the merge of PR #46 (release identity promotion) into `release/om-2.2`, which descends from `main` @ `84763cb1d3b6e1fe36f14ac98762d3782e947d9a` and from the frozen candidate `om-v2.2.0-rc1` (`f0a8fa5b0c945a6ed684db67bbf21b6baf8328c1`).

The GitHub release is:

- title: `OM 2.2.0`;
- tag: `om-v2.2.0`;
- prerelease: `false`;
- latest: `true`.

## Qualification evidence

- Pre-candidate qualification Q0–Q7: PASS (`OM_2.2_PRE_CANDIDATE_QUALIFICATION.md`).
- Candidate `om-v2.2.0-rc1`: frozen (`qualification/evidence/OM2-2.2.0-RC1_FREEZE_PASS.json`) and qualified (`RC1_QUALIFICATION_2.2.0.md`), including a tag-bound hosted call of the reusable workflow from AAE (run `36999806715`, report and enforce success).
- Protected PR qualification of the promotion: PR #46, head `7b41a0a82ea10bc5cc7727b6f192d1df5931cf50`, run `37000621051`, SUCCESS.

Normative equivalence gate (RC1 -> GA): `git diff om-v2.2.0-rc1 om-v2.2.0` lists only `OM.yaml`, `README.md`, `00_INDEX.md`, `RC1_QUALIFICATION_2.2.0.md` and `qualification/evidence/OM2-2.2.0-RC1_FREEZE_PASS.json`. No normative file, tool, workflow, schema or template differs. PASS.

Exact immutable tag-bound qualification:

- tag: `om-v2.2.0`;
- exact head SHA: `89de89d0935d61d5442bc8301d9c6c4f2cf7af87`;
- workflow run: `37000769192`;
- event: `push`;
- conclusion: `SUCCESS`.

Release evidence: `qualification/evidence/OM2-2.2.0_RELEASE_PASS.json`.

## Known limits

- The tag is unsigned.
- Individual clauses of the tag ruleset were not read back in this pass; the connector does not expose ruleset details.
- Hosted run of the manual runtime map refresh workflow is not evidenced (the same command was run locally); it is advisory and not a release gate.
- The enforce failure on a project with deprecated references is evidenced by the Q6 pilot in DVC (216 deprecated references in the local dry run) on a pre-candidate commit; the gate bytes are identical in the release.
- The runtime map covers 14 official actions (verified 2026-10-02); third-party actions are not judged.

## Product and semantic disposition

No OM PRODUCT defect. CORE, profiles, schemas of project state, templates and recovery behavior are unchanged from `om-v2.1.3`. Conformance pass/fail of a caller that does not set `actions_runtime` is unchanged (non-blocking report).

## Canonical authority

Acceptance of OM 2.2.0 does **not** perform canonical adoption.

Current canonical authority remains:

- version: `2.1.3`;
- tag: `om-v2.1.3`;
- exact commit: `ed816aa46694b44b681f9453aaef3d0458ed0d79`.

Prospective canonical adoption of OM 2.2.0 requires a separate explicit human authorization and governance-index update. No child project is migrated or re-pinned by this acceptance record.
