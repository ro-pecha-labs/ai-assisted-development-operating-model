# OM 2.3.0 — Canonical Adoption

**Status:** CANONICAL_ADOPTED / CURRENT_NORMATIVE_AUTHORITY  
**Effective date:** 2026-10-02  
**Canonical tag:** `om-v2.3.0`  
**Exact canonical commit:** `df716c43a8f19ef15ceb5b2bcc3237b393877c90`

## Authorization

Canonical adoption of OM 2.3.0 was explicitly authorized by the human project owner on 2026-10-02.

The adoption is prospective from the corresponding governance-index revision. It does not rewrite historical evidence or reinterpret work performed under earlier Operating Model versions.

## Canonical authority

The current normative authority is the immutable Git tag identity:

`om-v2.3.0 -> df716c43a8f19ef15ceb5b2bcc3237b393877c90`

The immutable annotated tag (tag object `d419a1510a365282fb99af8876f0cc6b9a9ab216`) is authoritative. Development and evidence commits on `main` after the tag (including `ACCEPTANCE_2.3.0.md`, `qualification/evidence/OM2-2.3.0_RELEASE_PASS.json` and this record) do not mutate the canonical release bytes and are not part of the canonical authority.

## Acceptance basis

OM 2.3.0 GA acceptance is recorded in `ACCEPTANCE_2.3.0.md`; candidate readiness and qualification in `CANDIDATE_READINESS_2.3.0_RC1.md`, `RC1_QUALIFICATION_2.3.0.md` and `OM_2.3_PRE_CANDIDATE_QUALIFICATION.md`.

Key machine-grounded evidence:

- pre-candidate qualification Q0–Q4: PASS, including a read-only shadow pilot on DVC, SPC and AAE;
- candidate `om-v2.3.0-rc1` (`e70e97dddeab9a3a941b705c6b478a5e982d8472`): frozen (tag-triggered run `37011289261 / SUCCESS`) and qualified (PASS; the hosted call of the reusable conformance workflow at the tag was not required by owner decision because the called bytes are identical to `om-v2.2.0`);
- protected PR qualification of the promotion (PR #58): `37012927063 / SUCCESS`;
- exact tag-bound qualification: `37013239329 / SUCCESS`;
- post-merge hosted validation of `main` (not part of the canonical bytes): `37013863381 / SUCCESS`.

## Normative delta to OM 2.2.0

MINOR, backward compatible. `platforms/github/CI_EFFICIENCY.md` gains rules 13–19 (parameterized release-line gates, gate closure at acceptance, write-capable single-use workflows keep their narrow trigger, operating system justified by the claim, bounded jobs, governance state churn as a CI input, measurement), a measurement section and a reference pattern for a consolidated gate; `playbooks/CANDIDATE_RELEASE.md` gains step 14 (gate closure on acceptance); `tools/ci_usage_report.py` is a new read-only measurement tool (`static` and `usage`; never blocking).

CORE, profiles, schemas of project state, templates, the project-state validator, the reusable `project-state-conformance.yml` and recovery behavior are unchanged from OM 2.2.0 (byte-identical gate and validator). A project that adopts OM 2.3.0 inherits exactly the OM 2.2.0 conformance behavior. Rules 13–19 are prospective policy for new and changed GitHub workflows; they do not reinterpret existing workflows or evidence.

## Known limits (carried from acceptance)

- The tag is unsigned; individual clauses of the tag ruleset were not read back.
- A GitHub Release `OM 2.3.0` is not published at the time of this record; the latest GitHub release is `om-v2.2.0`. The canonical identity is the tag.
- The hosted call of the reusable conformance workflow was not executed for `om-v2.3.0-rc1` (owner decision, byte identity with `om-v2.2.0`).
- `ci_usage_report.py usage` is an estimate (job minutes rounded up, Windows x2, macOS x10); the Actions `billable` field reports 0 in the pilot repositories.
- OM's own `validate.yml` triggers on `pull_request`, `push` to `main` and `om-v*` tags and is flagged by the new `static` report under rule 6; it is not changed in 2.3.

## Historical lineage

- OM 2.0.0, 2.1.1, 2.1.2, 2.1.3 and 2.2.0 remain immutable accepted historical canonical releases.
- OM 2.1.0 remains immutable historical evidence of a non-accepted GA release-control deviation.
- OM 2.3.0 is the accepted MINOR successor and current canonical normative authority.

Historical records are not rewritten.

## Project adoption boundary

OM-level canonical adoption does not automatically migrate existing child projects.

Each existing project, including DVC, SPC, AAE, DAE, APC and AF portfolio controls, adopts OM 2.3.0 separately at its own explicit safe boundary. Adoption consists of re-pinning `.project/PROJECT.yaml` (`ref: om-v2.3.0`, `commit: df716c43a8f19ef15ceb5b2bcc3237b393877c90`) and the project-state conformance caller (`uses: ...@om-v2.3.0`, `om_ref: om-v2.3.0`), after a complete-tree search for pin-asserting artifacts (`tools/find_pin_references.py`, `playbooks/ADOPTION_MIGRATION.md`), followed by a CI review against `platforms/github/CI_EFFICIENCY.md` rules 13–19.

Until such a project-level adoption occurs, that project's recorded OM pin remains authoritative for that project.

## Governance index

The cross-project Google Drive governance index `Projekty/00_OPERATING_MODEL/00_OPERATING_MODEL_INDEX.md` must resolve current canonical authority to:

- version: `2.3.0`;
- tag: `om-v2.3.0`;
- exact commit: `df716c43a8f19ef15ceb5b2bcc3237b393877c90`.

This adoption record and the Drive governance index together establish the prospective discovery state; the immutable Git tag remains the normative release body. The Drive index is not changed by this repository change.
