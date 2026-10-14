# OM 2.4 — RC1 Candidate Readiness

**Status:** READY_TO_FREEZE — NON-CANONICAL
**Target candidate identity:** `OM2-2.4.0-RC1`
**Target immutable tag:** `om-v2.4.0-rc1`
**Pre-freeze development baseline:** `46ec3c0f11c357e8e20ebd743b73daab5638bd24` (`release/om-2.4`, head before this change)

## Purpose

Determine whether the OM 2.4 line is eligible for its first immutable release candidate after completion of Q0–Q7 pre-candidate qualification.

This record does not make OM 2.4 canonical and does not adopt OM 2.4 in any child project.

## Scope of OM 2.4

OM 2.4 is a backward-compatible MINOR release line (target `2.4.0`) introducing a common project rules layer:

- `COMMON_RULES.md`: layers and precedence (OM invariants, optional organization layer, Common Rules, project rules), sections U (universal), D (DEV) and G (Git without platform enforcement), applicability per profile;
- `CORE.md` rule 17 (rule layers) and `profiles/DEV.md` rule 30 (Common Rules inherited, mandatory with an explicit, justified, recorded exception that shall not touch an OM invariant);
- `playbooks/AI_REVIEW_AUDIT.md` (AI review and audit under solo assurance), registered in `OM.yaml` (`playbooks.ai_review_audit`; `entrypoints.common_rules`);
- `platforms/git_local/`: README and example hooks (`reference-transaction`, `pre-commit` validating the staged project bootstrap against the exact adopted OM revision, fail closed);
- `templates/DEV/.project/DEVELOPMENT_RULES.md` skeleton (adopted common rules, organization rules, exceptions, project-specific rules);
- qualification: `tools/qualify_om24.py` (AI review policy cases, Common Rules consistency contract and negative controls), `qualification/om2.4/`, `qualification/git-local/`, two `validate.yml` steps.

No schema, `validate_project_bootstrap.py`, reusable conformance workflow or recovery behavior is changed. A project pinned to an earlier OM revision is unaffected.

## Pre-candidate qualification

Q0–Q7: **PASS** (`OM_2.4_PRE_CANDIDATE_QUALIFICATION.md`).

- structural and backward compatibility, all-profile and recovery regression, project bootstrap conformance controls: PASS;
- `git_local` hooks (17 checks in a throwaway repository, hosted): PASS;
- AI review and audit policy cases (15) and the Common Rules consistency contract with 5 negative controls (hosted): PASS;
- real-project evidence (Q6): PASS by owner decision, with the limits below;
- disposition of the proposal's open questions (Q7): recorded.

Work packages merged through protected `release/om-2.4`: PR #64, #65; qualification record PR #66. Hosted runs: `38542925539`, `38543482146`, `38544958951`. Owner decisions on the proposal's questions confirmed on 2026-10-14.

## Known limits (do not block RC1)

1. **Q6 is not independent.** The evidence is real work already performed under the Common Rules in CRA Business Mapping, the project from which the rules were derived. The project's records were not read in this session; the basis is the owner's statement. Adoption in a project that did not contribute to the rules is a recommended follow-up, not a gate.
2. **Mandatory for DEV, enforced by review.** No automated conformance check verifies that a project records exceptions to Common Rules; project-state conformance does not read the project rules file.
3. The `git_local` hooks are examples that a project adapts (paths, forbidden files, validator command); the fixtures prove the documented behavior of the examples.
4. The organization layer has no schema field; it is referenced from the project rules file, and its owner is not decided. A validator without Python is out of scope.
5. `validate.yml` does not run on pushes to release branches; the hosted run on the exact RC1 source SHA is produced by the protected pull request that merges this change.
6. OM's own `validate.yml` is unchanged (decision of 2.3, known limitation).

## Recurrence and defect disposition

1. A rule cited as a refinement of a DEV rule that does not say that (D1 vs DEV 25, Q5 finding) -> consistency check of every `DEV <n>` reference and a negative control.
2. The `pre-commit` example only printed a notice for staged `.project/*.yaml` (found while qualifying `git_local`) -> validates the staged copy and fails closed.
3. Qualification checks too weak (applicability cells accepted by prefix; invariant wording checked by unrelated substrings; Codex P2 and P1 on PR #66) -> expected applicability matrix, exact invariant clauses and 5 negative controls.

No known unresolved recurrence class blocks RC1 freeze.

## Release-safe template qualification

`templates/DEV/.project/PROJECT.yaml` is unchanged and still carries explicit non-usable sentinels (`REPLACE_WITH_ADOPTED_IMMUTABLE_OM_REF`, all-zero commit). The new `DEVELOPMENT_RULES.md` skeleton contains only placeholders for the adopted OM ref and commit and embeds no candidate-era or release-specific pin. Project bootstrap conformance rejects the uninstantiated template (structural CI).

## Candidate source identity

This readiness change changes internal OM identity and status text only:

- `OM.yaml`: `2.3.0` -> `2.4.0-rc1`; `accepted_release` -> `non_canonical_candidate`;
- `README.md`, `00_INDEX.md`: 2.4 candidate line (non-canonical);
- `OM_2.4_PRE_CANDIDATE_QUALIFICATION.md`: remaining-items list updated.

No normative semantics, workflow, tool, schema or template is changed in this readiness change.

The exact RC1 source SHA is not known until this change is merged through protected `release/om-2.4`.

## Freeze conditions

RC1 may be frozen only after:

1. this exact readiness change is merged through protected `release/om-2.4`;
2. the resulting exact SHA completes hosted validation = SUCCESS;
3. immutable annotated tag `om-v2.4.0-rc1` is created by the owner on that exact SHA;
4. fresh read-back confirms tag -> exact SHA;
5. tag-triggered hosted validation succeeds;
6. RC1 freeze evidence records exact source/tag/run identity.

If any condition fails, no RC1 PASS claim is made.

## Candidate qualification after freeze

Qualify the exact immutable RC1 identity: structural validation on the tag, all-profile and recovery regression, `git_local` and AI review qualification, project bootstrap controls, one hosted call of the reusable conformance workflow at tag `om-v2.4.0-rc1` (its behavior is unchanged from 2.2.0), and a read-only adoption dry run of the DEV template skeleton in one child project.

If RC1 fails, preserve it as immutable failed evidence and remediate in RC2 or later. Do not patch RC1 in place.

## Non-canonical boundary

Canonical authority remains `om-v2.3.0` (exact commit `df716c43a8f19ef15ceb5b2bcc3237b393877c90`). No child project is migrated by RC1 freeze.
