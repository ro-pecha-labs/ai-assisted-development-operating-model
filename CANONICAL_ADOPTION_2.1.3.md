# OM 2.1.3 — Canonical Adoption

**Status:** CANONICAL_ADOPTED / CURRENT_NORMATIVE_AUTHORITY  
**Effective date:** 2026-10-02  
**Canonical tag:** `om-v2.1.3`  
**Exact canonical commit:** `ed816aa46694b44b681f9453aaef3d0458ed0d79`

## Authorization

Canonical adoption of OM 2.1.3 was explicitly authorized by the human project owner on 2026-10-02.

The adoption is prospective from the corresponding governance-index revision. It does not rewrite historical evidence or reinterpret work performed under earlier Operating Model versions.

## Canonical authority

The current normative authority is the immutable GitHub release identity:

`om-v2.1.3 -> ed816aa46694b44b681f9453aaef3d0458ed0d79`

The immutable annotated tag (tag object `f5c1d1725d07f19a20375fe8389365beeea08fc4`) is authoritative. Development and evidence commits on `main` after the tag (including post-2.1.1 policy development such as `platforms/github/CI_EFFICIENCY.md` rules 11–12 and the 2.1.3 acceptance record) do not mutate the canonical release bytes and are not part of the canonical authority.

## Acceptance basis

OM 2.1.3 GA acceptance is recorded in `ACCEPTANCE_2.1.3.md`; patch scope in `PATCH_2.1.3.md`.

Key machine-grounded evidence:

- protected PR qualification (PR #33): `36987043407 / SUCCESS`;
- release identity check before tagging: PASS;
- exact tag-bound qualification: `36987775749 / SUCCESS`;
- GitHub Release `OM 2.1.3` (not a pre-release, latest).

## Normative delta to OM 2.1.2

None to OM normative behavior. OM 2.1.3 changes only GitHub tooling and CI: it adds a data map of Node.js 24 majors for 14 official actions (`tools/actions_runtime_map.json`), reports unmapped official actions as `UNJUDGED`, and adds a non-blocking guard step to the reusable `project-state-conformance.yml`. Conformance pass/fail is unchanged. Projects adopting 2.1.3 inherit exactly the OM 2.1.2 normative behavior; their conformance run additionally reports deprecated Node.js action runtimes in the caller's workflows (report only).

## Known limits (carried from acceptance)

- The reusable-workflow report step is qualified by local simulation; a real call from a child repository is not yet evidenced and is to be recorded at the first child-project adoption.
- The runtime map is a bounded list of official actions; third-party actions are not judged.
- The guard is non-blocking; enforcement is a follow-up MINOR objective.

## Historical lineage

- OM 2.0.0 remains an immutable accepted historical canonical release.
- OM 2.1.0 remains immutable historical evidence of a non-accepted GA release-control deviation.
- OM 2.1.1 remains an immutable accepted historical canonical release.
- OM 2.1.2 remains an immutable accepted historical canonical release (2026-09-29 to 2026-10-02).
- OM 2.1.3 is the accepted PATCH successor and current canonical normative authority.

Historical records are not rewritten.

## Project adoption boundary

OM-level canonical adoption does not automatically migrate existing child projects.

Each existing project, including DVC, SPC, AAE, DAE, APC and AF portfolio controls, adopts OM 2.1.3 separately at its own explicit safe boundary. Adoption consists of re-pinning `.project/PROJECT.yaml` (`ref: om-v2.1.3`, `commit: ed816aa46694b44b681f9453aaef3d0458ed0d79`) and the project-state conformance caller (`uses: ...@om-v2.1.3`, `om_ref: om-v2.1.3`).

Until such a project-level adoption occurs, that project's recorded OM pin remains authoritative for that project.

## Governance index

The cross-project Google Drive governance index `Projekty/00_OPERATING_MODEL/00_OPERATING_MODEL_INDEX.md` must resolve current canonical authority to:

- version: `2.1.3`;
- tag: `om-v2.1.3`;
- exact commit: `ed816aa46694b44b681f9453aaef3d0458ed0d79`.

This adoption record and the Drive governance index together establish the prospective discovery state; the immutable Git tag remains the normative release body.
