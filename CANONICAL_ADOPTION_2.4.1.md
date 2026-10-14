# OM 2.4.1 — Canonical Adoption

**Status:** CANONICAL_ADOPTED / CURRENT_NORMATIVE_AUTHORITY  
**Effective date:** 2026-10-14  
**Canonical tag:** `om-v2.4.1`  
**Exact canonical commit:** `46deca26c3fb880fb5dc25e75d5d2b87bafd0c72`

## Authorization

Canonical adoption of OM 2.4.1 was explicitly authorized by the human project owner on 2026-10-14.

The adoption is prospective from the corresponding governance-index revision. It does not rewrite historical evidence or reinterpret work performed under earlier Operating Model versions.

## Canonical authority

The current normative authority is the immutable Git tag identity:

`om-v2.4.1 -> 46deca26c3fb880fb5dc25e75d5d2b87bafd0c72`

The immutable annotated tag (tag object `0eaee4d1fc4f2322c2bc4127095b7c47d1b2a73f`) is authoritative. Development and evidence commits on `main` after the tag (including `ACCEPTANCE_2.4.1.md`, `qualification/evidence/OM2-2.4.1_RELEASE_PASS.json` and this record) do not mutate the canonical release bytes and are not part of the canonical authority.

## Acceptance basis

OM 2.4.1 GA acceptance is recorded in `ACCEPTANCE_2.4.1.md`. As a PATCH it has no release candidate (`OM_RELEASE_POLICY.md`: protected PR, structural CI, targeted regression, immutable release identity).

Key machine-grounded evidence:

- PATCH content PR #74 (head `64c6884`): `38555257591 / SUCCESS`;
- protected PR qualification of the promotion (PR #75, head `c7b6718`): `38555600796 / SUCCESS`;
- exact tag-bound qualification: `38556301549 / SUCCESS`;
- targeted regression: the two new `ref` cases and the executable-mode checks of `qualification/git-local/run_qualification.sh` (22 checks) fail against the `om-v2.4.0` hook and pass on 2.4.1;
- GitHub Release `OM 2.4.1` published (Latest).

## Normative delta to OM 2.4.0

PATCH, backward compatible. `platforms/git_local/reference-transaction.example` is committed executable; `platforms/git_local/pre-commit.example` rejects a declared OM `ref` that does not resolve in `OM_ROOT` to the pinned `commit` (fail closed, `ref` and `commit` read separately); `qualification/git-local/run_qualification.sh` has 22 checks (executable mode, disposable OM clone, negative `ref` cases); `templates/DEV/.project/DEVELOPMENT_RULES.md` no longer repeats the OM pin recorded in `PROJECT.yaml`; `COMMON_RULES.md` U5 states both triggers.

Project-state schemas, the project-state validator, the reusable `project-state-conformance.yml` and recovery behavior are unchanged from OM 2.4.0. The two `git_local` findings and the two RC1 frictions recorded as known limits of OM 2.4.0 are resolved in 2.4.1; the interim manual guidance in `CANONICAL_ADOPTION_2.4.0.md` no longer applies to projects that adopt 2.4.1.

## Known limits (carried from acceptance)

- The tag is unsigned; individual clauses of the tag ruleset were not read back.
- The shadow pilot (Q6) of OM 2.4.0 and the RC1 dry runs were not independent of the author of the rules; project records were not read.
- The hosted call of the reusable conformance workflow at the tag was not repeated for `om-v2.4.1`; the called bytes are identical to `om-v2.4.0`.
- The `git_local` hooks are examples; a project shall record them as compensation in its project rules and verify them in its own repository.

## Historical lineage

- OM 2.0.0, 2.1.1, 2.1.2, 2.1.3, 2.2.0, 2.3.0 and 2.4.0 remain immutable accepted historical canonical releases.
- OM 2.1.0 remains immutable historical evidence of a non-accepted GA release-control deviation.
- OM 2.4.1 is the accepted PATCH successor and current canonical normative authority.

Historical records are not rewritten.

## Project adoption boundary

OM-level canonical adoption does not automatically migrate existing child projects.

Each existing project, including DVC, SPC, AAE, DAE, APC and AF portfolio controls, adopts OM 2.4.1 separately at its own explicit safe boundary. Adoption consists of re-pinning `.project/PROJECT.yaml` (`ref: om-v2.4.1`, `commit: 46deca26c3fb880fb5dc25e75d5d2b87bafd0c72`) and the project-state conformance caller (`uses: ...@om-v2.4.1`, `om_ref: om-v2.4.1`), after a complete-tree search for pin-asserting artifacts (`tools/find_pin_references.py`, `playbooks/ADOPTION_MIGRATION.md`), followed by instantiation of `DEVELOPMENT_RULES.md` and review against `COMMON_RULES.md`.

Until such a project-level adoption occurs, that project's recorded OM pin remains authoritative for that project.

## Governance index

The cross-project Google Drive governance index `Projekty/00_OPERATING_MODEL/00_OPERATING_MODEL_INDEX.md` must resolve current canonical authority to:

- version: `2.4.1`;
- tag: `om-v2.4.1`;
- exact commit: `46deca26c3fb880fb5dc25e75d5d2b87bafd0c72`.

This adoption record and the Drive governance index together establish the prospective discovery state; the immutable Git tag remains the normative release body. The Drive index is not changed by this repository change and shall be updated by the project owner at the same boundary.
