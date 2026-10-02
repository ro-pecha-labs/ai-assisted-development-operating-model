# OM 2.2.0 — Canonical Adoption

**Status:** CANONICAL_ADOPTED / CURRENT_NORMATIVE_AUTHORITY  
**Effective date:** 2026-10-02  
**Canonical tag:** `om-v2.2.0`  
**Exact canonical commit:** `89de89d0935d61d5442bc8301d9c6c4f2cf7af87`

## Authorization

Canonical adoption of OM 2.2.0 was explicitly authorized by the human project owner on 2026-10-02.

The adoption is prospective from the corresponding governance-index revision. It does not rewrite historical evidence or reinterpret work performed under earlier Operating Model versions.

## Canonical authority

The current normative authority is the immutable GitHub release identity:

`om-v2.2.0 -> 89de89d0935d61d5442bc8301d9c6c4f2cf7af87`

The immutable annotated tag (tag object `b0cd70d84d228deed5631706130ea65fca70c6ca`) is authoritative. Development and evidence commits on `main` after the tag (including `ACCEPTANCE_2.2.0.md`, `qualification/evidence/OM2-2.2.0_RELEASE_PASS.json` and this record) do not mutate the canonical release bytes and are not part of the canonical authority.

## Acceptance basis

OM 2.2.0 GA acceptance is recorded in `ACCEPTANCE_2.2.0.md`; candidate readiness and qualification in `CANDIDATE_READINESS_2.2.0_RC1.md`, `RC1_QUALIFICATION_2.2.0.md` and `OM_2.2_PRE_CANDIDATE_QUALIFICATION.md`.

Key machine-grounded evidence:

- pre-candidate qualification Q0–Q7: PASS;
- candidate `om-v2.2.0-rc1` (`f0a8fa5b0c945a6ed684db67bbf21b6baf8328c1`): frozen, tag-bound hosted call of the reusable workflow in AAE (run `36999806715`, report and enforce success);
- protected PR qualification of the promotion (PR #46): `37000621051 / SUCCESS`;
- exact tag-bound qualification: `37000769192 / SUCCESS`;
- GitHub Release `OM 2.2.0` (not a pre-release, latest).

## Normative delta to OM 2.1.3

MINOR, backward compatible. The reusable `project-state-conformance.yml` gains the optional input `actions_runtime` (`report` default, `enforce`). In `enforce` mode a mapped official action below its Node.js 24 major fails the conformance run; `enforce` fails closed against an adopted OM revision without the gate. Further additions: runtime map schema and advisory refresh tool, pin reference finder with a complete-tree pin search step in the adoption playbook, and hosted conformance caller guidance.

A project that adopts OM 2.2.0 and does not set `actions_runtime` inherits exactly the OM 2.1.3 behavior (non-blocking runtime report). Enforcement is a separate, per-project decision.

## Known limits (carried from acceptance)

- The tag is unsigned; individual clauses of the tag ruleset were not read back.
- Hosted run of the manual runtime map refresh workflow is not evidenced (advisory, not a gate).
- The enforce failure on a project with deprecated references is evidenced by the Q6 pilot in DVC on a pre-candidate commit (216 deprecated references in the local dry run).
- The runtime map covers 14 official actions (verified 2026-10-02); third-party actions are not judged.

## Historical lineage

- OM 2.0.0, 2.1.1, 2.1.2 and 2.1.3 remain immutable accepted historical canonical releases.
- OM 2.1.0 remains immutable historical evidence of a non-accepted GA release-control deviation.
- OM 2.2.0 is the accepted MINOR successor and current canonical normative authority.

Historical records are not rewritten.

## Project adoption boundary

OM-level canonical adoption does not automatically migrate existing child projects.

Each existing project, including DVC, SPC, AAE, DAE, APC and AF portfolio controls, adopts OM 2.2.0 separately at its own explicit safe boundary. Adoption consists of re-pinning `.project/PROJECT.yaml` (`ref: om-v2.2.0`, `commit: 89de89d0935d61d5442bc8301d9c6c4f2cf7af87`) and the project-state conformance caller (`uses: ...@om-v2.2.0`, `om_ref: om-v2.2.0`), after a complete-tree search for pin-asserting artifacts (`tools/find_pin_references.py`).

Until such a project-level adoption occurs, that project's recorded OM pin remains authoritative for that project.

## Governance index

The cross-project Google Drive governance index `Projekty/00_OPERATING_MODEL/00_OPERATING_MODEL_INDEX.md` must resolve current canonical authority to:

- version: `2.2.0`;
- tag: `om-v2.2.0`;
- exact commit: `89de89d0935d61d5442bc8301d9c6c4f2cf7af87`.

This adoption record and the Drive governance index together establish the prospective discovery state; the immutable Git tag remains the normative release body.
