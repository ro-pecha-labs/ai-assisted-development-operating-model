# OM 2.4 — Qualification Plan

**Status:** DEVELOPMENT / PLAN / NON-CANONICAL  
**Target:** OM 2.4.0 — Common Project Rules (MINOR, `OM_RELEASE_POLICY.md`)  
**Base:** `main` @ `9aa053f14aff59f8dd80df4e69ba778e3181e0d2` (contains OM 2.3.0)  
**Date:** 2026-10-14

Canonical authority remains OM 2.3.0 (`CANONICAL_ADOPTION_2.3.0.md`). This plan is not a release, a candidate or an adoption. Rationale and open questions of the proposal: `OM_COMMON_RULES_PROPOSAL.md`.

## Origin

Analysis of the project rules of an adopting project (CRA Business Mapping, OM 2.3.0, DEV, solo) showed that about half of its 14 project rules are general and would be copied by every further project. OM 2.3.0 has no common rules mechanism: DEV 3 makes project rules conditional and the DEV template holds a placeholder.

## Classification

MINOR: backward-compatible. Projects pinned to an earlier OM revision are not affected. A project that adopts 2.4.0 inherits the Common Rules, with an explicit recorded exception where justified. No change to `om.project/v2` or other schemas.

## Decisions (owner, per the recommendations of the proposal)

| Question | Decision |
|---|---|
| Version number | `2.4.0` |
| Schema `om.project/v2` | no change; the organization layer is referenced from the project rules file (`governance.project_rules`) until a later MINOR adds a field |
| Obligation and versioning | Common Rules are part of the OM release; mandatory for DEV with a justified exception recorded in the project rules; optional patterns are marked "may" |
| Organization layer owner | open, non-blocking (the layer is optional) |
| Applicability to other profiles | as in the applicability table of `COMMON_RULES.md`; sections split into U (universal), D (DEV), G (Git without platform enforcement) |
| Invariants | no lower layer may weaken them, including the organization layer |
| Validator without Python | **out of scope** for 2.4.0 (separate objective) |

## Work packages

### WP1 — Normative integration

- `COMMON_RULES.md` and `playbooks/AI_REVIEW_AUDIT.md` become normative components: no local release status line, registered in `OM.yaml` (`entrypoints.common_rules`, `playbooks.ai_review_audit`) and in `tools/validate.py` (`EXPECTED_PLAYBOOKS`, normative list without local status, entrypoint check).
- `CORE.md` rule 17 (rule layers) and `profiles/DEV.md` rule 30 (Common Rules inherited, exception recorded, invariants untouched).
- `platforms/git_local/README.md`: no local status line.

### WP2 — DEV template

- `templates/DEV/.project/DEVELOPMENT_RULES.md` skeleton (adopted common rules, organization rules, exceptions, project-specific rules). The project bootstrap validator and the uninstantiated-template rejection shall keep passing.

### WP3 — `platforms/git_local` qualification

- Deterministic fixtures in structural CI: `reference-transaction` rejects moving or deleting an accepted tag and allows an ordinary ref update; `pre-commit` rejects a staged forbidden file and a `ref`/`commit` mismatch and accepts a conformant staged bootstrap. The hooks stay examples; the fixtures prove the documented behavior.

### WP4 — AI review and audit playbook

- Deterministic policy cases (extend `qualification/om2.1/` style cases): a record lacking a disposition for a finding, lacking the model/scope/counts, or presented as human acceptance is rejected; a complete record is accepted.

### WP5 — Records

- README and `00_INDEX.md` development-line text; later candidate readiness, qualification and acceptance records.

## Pre-candidate qualification

- **Q0** structural validation and backward compatibility (existing fixtures and schemas unchanged; projects on earlier revisions unaffected).
- **Q1** regression of all profiles and minimal and solo recovery.
- **Q2** project bootstrap conformance: positive, negative and uninstantiated DEV template controls with the new template.
- **Q3** `git_local` fixtures (WP3).
- **Q4** AI review and audit policy cases (WP4).
- **Q5** negative controls of the new semantics: an exception that touches an invariant is not permitted by the documented rules; the layers table and the applicability table are consistent with the profiles.
- **Q6** representative shadow pilot: read-only shadow adoption in a real project that did not contribute to the rules and whose work did not follow them (AAE or another portfolio project; the owner chooses), recording what the project rules file shrinks to, whether any adopted rule is lost and which Common Rule needs an exception. CRA Business Mapping, the origin project, is not independent evidence and cannot pass this step; its experience is recorded as supporting evidence only.
- **Q7** disposition of the proposal's open questions in this plan.

## Release train

Candidate readiness `2.4.0-rc1` → merge → immutable RC tag (owner) → Release as pre-release → RC qualification (tag-bound hosted call) → GA promotion (identity only) → tag `om-v2.4.0` (owner) → GitHub Release → acceptance → merge into `main` → canonical adoption → project adoption.

## Stop conditions

- an unexpected normative diff between RC and GA;
- a failed pre-candidate or RC qualification step: the failed candidate is preserved, a successor RC is created;
- the pilot shows that adopting the Common Rules loses a project rule;
- Q6 is claimed with a project that is not independent of the rules.

## Out of scope

Validator without Python; a `governance.organization_rules` schema field; organization-specific content (data protection officer, secret store, named data sources, commit message language, approved hosting).
