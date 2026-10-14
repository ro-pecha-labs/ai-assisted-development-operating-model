# OM 2.4 — Pre-Candidate Qualification Status

**Status:** PRE-CANDIDATE / Q0–Q7 PASS (Q6 by owner decision on non-independent real-project evidence) / READY FOR CANDIDATE-READINESS REVIEW (not passable with the origin project)  
**Development head:** `e61a8aa8f5f1ffa224d8cd065d03412de7e5461c` (`release/om-2.4`)  
**Date:** 2026-10-14

## Scope

Development target: `2.4.0 — Common Project Rules` (MINOR). Plan: `OM_2.4_QUALIFICATION_PLAN.md`; rationale: `OM_COMMON_RULES_PROPOSAL.md`.

Current canonical authority remains `om-v2.3.0`. This record does not freeze a candidate, does not make OM 2.4 canonical and does not adopt it in any child project. `OM.yaml` still declares `2.3.0`; the identity is promoted at candidate readiness (`2.4.0-rc1`).

## Work packages (merged into `release/om-2.4`)

| WP | PR | Merge commit | Hosted `Validate OM2` run on the PR head |
|---|---|---|---|
| WP1 normative integration, WP2 DEV template, WP5 records, plan | #64 | `61d557c3a98430d7f7cd72110278b3d4f6b28890` | `38542925539` SUCCESS (`c1de995`) |
| WP3 `git_local` hooks, WP4 AI review policy cases | #65 | `e61a8aa8f5f1ffa224d8cd065d03412de7e5461c` | `38543482146` SUCCESS (`7c83845`) |

The Q5 consistency check and one correction (see Q5) are in the change that carries this record.

## Q0 — Structural and backward compatibility

**PASS.** `tools/validate.py` and all `run` steps of `validate.yml` pass; no schema changed; `OM.yaml` adds only `entrypoints.common_rules` and `playbooks.ai_review_audit`. A project pinned to an earlier OM revision reads that revision, not this one, so it is unaffected.

## Q1 — All-profile and recovery regression

**PASS.** The existing all-profile contract checks, minimal and solo recovery qualification and the OM 2.1 policy semantics pass unchanged on the development head. Profiles other than DEV received no change; CORE gained rule 17 and DEV gained rule 30, both additive.

## Q2 — Project bootstrap conformance

**PASS.** Valid, invalid and uninstantiated-DEV-template controls behave as in 2.3.0. The new template `templates/DEV/.project/DEVELOPMENT_RULES.md` is not read by the bootstrap validator, which only checks that a declared `governance.project_rules` locator exists.

## Q3 — `git_local` hooks

**PASS.** `qualification/git-local/run_qualification.sh`: 17 checks in a throwaway repository (accepted tag creation allowed, move and deletion rejected by two routes, ordinary tags unrestricted, `TEMP-` marker and data files outside fixtures rejected, synthetic fixture accepted, staged bootstrap conformant/mismatched, a working-tree fix does not mask the staged copy, missing OM checkout fails closed). Hosted run `38543482146` SUCCESS.

The example `pre-commit` hook originally only printed a notice for staged `.project/*.yaml`; it now validates the staged copy against the OM checkout in `OM_ROOT` and fails closed. This was needed to qualify the documented behavior.

## Q4 — AI review and audit policy cases

**PASS.** `tools/qualify_om24.py` with `qualification/om2.4/ai_review_audit_cases.json`: 15 cases for `playbooks/AI_REVIEW_AUDIT.md` items 1–9 (3 PASS, 12 rejections/blocks). Hosted run `38543482146` SUCCESS.

## Q5 — Negative controls and consistency of the new semantics

**PASS after one correction.**

- Automated (`tools/qualify_om24.py`, `check_common_rules_consistency`): the applicability table has exactly the manifest profiles as columns; all 7 defined rules (U1–U5, D1–D2) and section G appear in the table and vice versa; every `DEV <n>` reference in `COMMON_RULES.md`, `AI_REVIEW_AUDIT.md` and `platforms/git_local/README.md` names an existing DEV rule (1–30); `CORE.md`, `profiles/DEV.md`, `COMMON_RULES.md` and the DEV template each state the invariant limit and the exception requirement. Negative control: a reference to a non-existent rule (`DEV 99`) makes the check fail.
- Manual review of the claims against the profile texts: U4 refines DEV 20 (active state) and DEV 22 (handoff); D2.5 maps to DEV 8 (failed candidates); G compensates DEV 24 and 29; LIGHT 10 excludes transition packages at session end, consistent with D2 not applying to LIGHT; SOLUTION 6 and DOCUMENT 6 (validation/review) are complemented by U5; EXPERIMENT 3 and LIGHT 2 state the single-authority principle behind U4. The invariants listed in `COMMON_RULES.md` map to CORE 1 (authority), 6 (historical integrity), 11 (fail closed: authorization, target identity, mutation scope, destructive semantics) and DEV 7 (candidate identity).
- **Finding (corrected):** `COMMON_RULES.md` D1 and the proposal stated that D1 "refines DEV 25". DEV 25 concerns AI-assisted implementation; DEV has no dependency rule. D1 is a new DEV rule, and the text now says so. The finding shows the value of the reference check, which is part of CI from this change on.

## Q6 — Representative real-project evidence

**PASS by owner decision, on non-independent real-project evidence, with the limits below.**

`OM_RELEASE_POLICY.md` requires, for a MINOR whose behavior affects assurance or lifecycle, a "representative real-project or shadow pilot". The owner declared on 2026-10-14 that work in CRA Business Mapping (OM 2.3.0, DEV, solo) has already been performed under the Common Rules, and decided to take that as the Q6 evidence instead of a separate read-only shadow adoption.

Limits of this evidence (not hidden, and not a gate):

1. **Not independent.** CRA Business Mapping is the project from whose rules the Common Rules were derived. The evidence shows that the rules are workable for that project; it does not show that they fit a project that did not shape them.
2. **Not read in this session.** No shadow adoption pull request was made, and the project's rules file, evidence and review records were not read here. The three observations a pilot would record — what the project rules file shrank to, whether an adopted rule was lost, which Common Rule needed an exception — are therefore not recorded in this document. The basis is the owner's statement.
3. **Recommended follow-up (not part of the candidate gate):** adoption of OM 2.4.0 in a project that did not contribute to the rules (for example AAE) at its own safe boundary, with those three observations recorded in its adoption record.

## Q7 — Disposition of the proposal's open questions

**PASS** (decisions recorded in `OM_2.4_QUALIFICATION_PLAN.md`, accepted by the owner on 2026-10-14 with "per recommendation").

1. Schema `om.project/v2`: no change; organization layer referenced from the project rules file until a later MINOR adds a field.
2. Obligation and versioning: Common Rules are part of the OM release, mandatory for DEV with a recorded justified exception; optional patterns are marked "may" (D2).
3. Owner of the organization layer: open and non-blocking.
4. Applicability: sections U, D and G as in the applicability table, verified in Q5.

Out of scope for 2.4.0: validator without Python; a `governance.organization_rules` schema field.

## Remaining before candidate readiness

1. Candidate readiness record, identity promotion to `2.4.0-rc1`, README/index status for the candidate.
2. Immutable RC tag (owner) and RC qualification.
