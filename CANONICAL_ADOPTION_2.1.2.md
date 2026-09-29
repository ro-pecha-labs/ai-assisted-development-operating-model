# OM 2.1.2 — Canonical Adoption

**Status:** CANONICAL_ADOPTED / CURRENT_NORMATIVE_AUTHORITY  
**Effective date:** 2026-09-29  
**Canonical tag:** `om-v2.1.2`  
**Exact canonical commit:** `78f7390e58ce363c1e734d6beb54c08ac50131c6`

## Authorization

Canonical adoption of OM 2.1.2 was explicitly authorized by the human project owner on 2026-09-29.

The adoption is prospective from the corresponding governance-index revision. It does not rewrite historical evidence or reinterpret work performed under earlier Operating Model versions.

## Canonical authority

The current normative authority is the immutable GitHub release identity:

`om-v2.1.2 -> 78f7390e58ce363c1e734d6beb54c08ac50131c6`

The immutable annotated tag is authoritative. Development and evidence commits on `main` after the tag (including post-2.1.1 policy development such as `platforms/github/CI_EFFICIENCY.md` rules 11–12) do not mutate the canonical release bytes and are not part of the canonical authority.

## Acceptance basis

OM 2.1.2 GA acceptance is recorded in `ACCEPTANCE_2.1.2.md`; patch scope in `PATCH_2.1.2.md`.

Key machine-grounded evidence:

- protected PR qualification (PR #30): `36548955126 / SUCCESS`;
- release identity check before tagging: PASS;
- exact tag-bound qualification: `36549211982 / SUCCESS`.

Tag protection remains active for `refs/tags/om-v*`, blocking tag update and deletion.

## Normative delta to OM 2.1.1

None. OM 2.1.2 changes only GitHub workflow action majors (Node.js 24), adds `tools/actions_runtime_guard.py`, and updates version/status coherence. Projects adopting 2.1.2 inherit exactly the OM 2.1.1 normative behavior; their reusable project-state conformance workflow runs on Node.js 24.

## Historical lineage

- OM 2.0.0 remains an immutable accepted historical canonical release.
- OM 2.1.0 remains immutable historical evidence of a non-accepted GA release-control deviation.
- OM 2.1.1 remains an immutable accepted historical canonical release (2026-09-23 to 2026-09-29).
- OM 2.1.2 is the accepted PATCH successor and current canonical normative authority.

Historical records are not rewritten.

## Project adoption boundary

OM-level canonical adoption does not automatically migrate existing child projects.

Each existing project, including DVC, SPC, AAE, DAE, APC and AF portfolio controls, adopts OM 2.1.2 separately at its own explicit safe boundary. Adoption consists of re-pinning `.project/PROJECT.yaml` (`ref: om-v2.1.2`, `commit: 78f7390e58ce363c1e734d6beb54c08ac50131c6`) and the project-state conformance caller (`uses: ...@om-v2.1.2`, `om_ref: om-v2.1.2`).

Until such a project-level adoption occurs, that project's recorded OM pin (currently `om-v2.1.1`) remains authoritative for that project.

## Governance index

The cross-project Google Drive governance index `Projekty/00_OPERATING_MODEL/00_OPERATING_MODEL_INDEX.md` must resolve current canonical authority to:

- version: `2.1.2`;
- tag: `om-v2.1.2`;
- exact commit: `78f7390e58ce363c1e734d6beb54c08ac50131c6`.

This adoption record and the Drive governance index together establish the prospective discovery state; the immutable Git tag remains the normative release body.