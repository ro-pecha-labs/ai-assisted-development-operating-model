# OM 2.4.0 — Canonical Adoption

**Status:** CANONICAL_ADOPTED / CURRENT_NORMATIVE_AUTHORITY  
**Effective date:** 2026-10-14  
**Canonical tag:** `om-v2.4.0`  
**Exact canonical commit:** `88466c2dc9a2033d623d1d9bb4ab7a57aebd3445`

## Authorization

Canonical adoption of OM 2.4.0 was explicitly authorized by the human project owner on 2026-10-14.

The adoption is prospective from the corresponding governance-index revision. It does not rewrite historical evidence or reinterpret work performed under earlier Operating Model versions.

## Canonical authority

The current normative authority is the immutable Git tag identity:

`om-v2.4.0 -> 88466c2dc9a2033d623d1d9bb4ab7a57aebd3445`

The immutable annotated tag (tag object `78d5ead481ea06bc0f0613a454eb282d092d40f1`) is authoritative. Development and evidence commits on `main` after the tag (including `ACCEPTANCE_2.4.0.md`, `qualification/evidence/OM2-2.4.0_RELEASE_PASS.json` and this record) do not mutate the canonical release bytes and are not part of the canonical authority.

## Acceptance basis

OM 2.4.0 GA acceptance is recorded in `ACCEPTANCE_2.4.0.md`; candidate readiness and qualification in `CANDIDATE_READINESS_2.4.0_RC1.md`, `RC1_QUALIFICATION_2.4.0.md` and `OM_2.4_PRE_CANDIDATE_QUALIFICATION.md`.

Key machine-grounded evidence:

- pre-candidate qualification Q0–Q7: PASS (Q6 by owner decision with recorded limitations);
- candidate `om-v2.4.0-rc1` (`9ec7f6a8584b04e6d3483ceb5e7c875be7cf66a8`): frozen and qualified (PASS), promoted unchanged by owner decision;
- protected PR qualification of the promotion (PR #70): `38549241353 / SUCCESS`;
- exact tag-bound qualification: `38550361745 / SUCCESS`;
- GitHub Release `OM 2.4.0` published (Latest).

## Normative delta to OM 2.3.0

MINOR, backward compatible. New: `COMMON_RULES.md` (rule layers and precedence; universal rules U1–U5; default rules D1–D2; applicability table), CORE rule 17 (rule layers), DEV rule 30 (project rules inherit Common Rules; binding, with a justified exception that never touches an invariant), `playbooks/AI_REVIEW_AUDIT.md`, the `git_local` platform (`platforms/git_local/`, example hooks) with `qualification/git-local/`, the DEV rules template skeleton `templates/DEV/.project/DEVELOPMENT_RULES.md`, and the qualification tool `tools/qualify_om24.py` with `qualification/om2.4/`.

Project-state schemas, the project-state validator, the reusable `project-state-conformance.yml` and recovery behavior are unchanged from OM 2.3.0. Conformance pass/fail of a project that does not adopt the new rules is unchanged. The Common Rules apply to a project from its own adoption of OM 2.4.0 and do not reinterpret existing project records.

## Known limits (carried from acceptance and review)

- The tag is unsigned; individual clauses of the tag ruleset were not read back.
- The shadow pilot (Q6) and the RC1 dry runs were not independent of the author of the rules; project records were not read.
- RC1 friction 1: U5 is conditional while the applicability table reads unconditional (clarifying sentence deferred to a PATCH).
- RC1 friction 2: the template skeleton repeats the `<ref>` and `<commit>` placeholders (deferred to a PATCH).
- Codex review of PR #72, finding 1 (P1): `platforms/git_local/reference-transaction.example` is committed with mode `100644`; copied without `chmod +x` Git ignores the hook and accepted tags stay movable. The qualification script masks this with `chmod +x`. Deferred to PATCH 2.4.1.
- Codex review of PR #72, finding 2 (P2): the example `pre-commit` validates only the pinned `commit` against `OM_ROOT` HEAD; a stale or incorrect `ref` is not rejected although `platforms/git_local/README.md` requires `ref` to correspond to `commit`, and the qualification case varies only `commit`. Deferred to PATCH 2.4.1.
- Until 2.4.1, projects using the `git_local` example hooks shall set the executable flag on installed hooks and verify `ref` against `commit` manually.

## Historical lineage

- OM 2.0.0, 2.1.1, 2.1.2, 2.1.3, 2.2.0 and 2.3.0 remain immutable accepted historical canonical releases.
- OM 2.1.0 remains immutable historical evidence of a non-accepted GA release-control deviation.
- OM 2.4.0 is the accepted MINOR successor and current canonical normative authority.

Historical records are not rewritten.

## Project adoption boundary

OM-level canonical adoption does not automatically migrate existing child projects.

Each existing project, including DVC, SPC, AAE, DAE, APC and AF portfolio controls, adopts OM 2.4.0 separately at its own explicit safe boundary. Adoption consists of re-pinning `.project/PROJECT.yaml` (`ref: om-v2.4.0`, `commit: 88466c2dc9a2033d623d1d9bb4ab7a57aebd3445`) and the project-state conformance caller (`uses: ...@om-v2.4.0`, `om_ref: om-v2.4.0`), after a complete-tree search for pin-asserting artifacts (`tools/find_pin_references.py`, `playbooks/ADOPTION_MIGRATION.md`), followed by instantiation of `DEVELOPMENT_RULES.md` and review against `COMMON_RULES.md`.

Until such a project-level adoption occurs, that project's recorded OM pin remains authoritative for that project.

## Governance index

The cross-project Google Drive governance index `Projekty/00_OPERATING_MODEL/00_OPERATING_MODEL_INDEX.md` must resolve current canonical authority to:

- version: `2.4.0`;
- tag: `om-v2.4.0`;
- exact commit: `88466c2dc9a2033d623d1d9bb4ab7a57aebd3445`.

This adoption record and the Drive governance index together establish the prospective discovery state; the immutable Git tag remains the normative release body. The Drive index is not changed by this repository change (connector unavailable) and shall be updated separately.
