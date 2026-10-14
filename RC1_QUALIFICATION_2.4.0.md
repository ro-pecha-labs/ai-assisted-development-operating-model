# OM 2.4.0-rc1 — Candidate Qualification

**Status:** RC1 QUALIFICATION PASS — NON-CANONICAL
**Candidate identity:** `OM2-2.4.0-RC1`
**Tag:** `om-v2.4.0-rc1` (annotated, tag object `d95a680246b0103ea220953a227998a47b03e14e`) -> commit `9ec7f6a8584b04e6d3483ceb5e7c875be7cf66a8`
**Date:** 2026-10-14

Freeze evidence: `qualification/evidence/OM2-2.4.0-RC1_FREEZE_PASS.json`. GitHub Release `OM 2.4.0 RC1` is published as a pre-release; the latest release is unchanged.

This record does not make OM 2.4 canonical and does not adopt OM 2.4 in any child project.

## A. Local qualification on the immutable tag

Checkout of `om-v2.4.0-rc1` (`9ec7f6a`), all `run` steps of `validate.yml` except the dependency installation (16 `run` steps in total; the interpreter dependencies were already installed) executed with `bash -eo pipefail`: **15 of 15 executed steps exit 0**, including the OM 2.4 AI review and audit policy semantics (21 PASS, 0 FAIL in `tools/qualify_om24.py`, which now includes the Common Rules consistency contract and its 5 negative controls) and the `git_local` hook qualification.

- `OM.yaml` declares `2.4.0-rc1` / `non_canonical_candidate`.
- Difference between the qualified development head `46ec3c0` and the tag: only `OM.yaml`, `README.md`, `00_INDEX.md`, `OM_2.4_PRE_CANDIDATE_QUALIFICATION.md` and the new `CANDIDATE_READINESS_2.4.0_RC1.md`. No normative file, tool, workflow, schema or template differs.
- Tag-triggered `Validate OM2` run `38546881825` on `9ec7f6a`: SUCCESS.

## B. Tag-bound hosted shadow pilot (AAE)

Draft pull request [AAE #73](https://github.com/ro-pecha-labs/aae-application-authorization-engine/pull/73) (`[PILOT RC1 - DO NOT MERGE]`, branch `shadow/om-2.4-rc1-q`, head `5cb26514d88b4be93c9eddc13f542b231ee1fa48`, base `main` @ `117e7f1aff72d246772a63e058ed1de1122aac61`): `.project/PROJECT.yaml` pinned to `om-v2.4.0-rc1` / `9ec7f6a`, and a caller with two jobs calling the reusable workflow `project-state-conformance.yml@om-v2.4.0-rc1`. The source branch of AAE is unchanged.

Run `38548179281`: **success**. The run metadata references `refs/tags/om-v2.4.0-rc1` (`d95a680…`).

| Job | Conclusion | Evidence read |
|---|---|---|
| `conformance-enforce` | success | job log text: `PASS: exact OM commit pin 9ec7f6a8584b04e6d3483ceb5e7c875be7cf66a8`, `PROJECT BOOTSTRAP CONFORMANCE PASS`, `PASS: 36 mapped action reference(s), 0 unjudged official action reference(s) in 22 file(s); no mapped reference is below its Node.js 24 major` |
| `conformance-report` | success | job and step conclusions from the Actions API (all functional steps success, including "GitHub Actions runtime check"); log text not read separately |

The reusable workflow is unchanged from 2.2.0, and the result agrees with the earlier pilots on the same project.

## C. Dry run of the DEV rules template in a project that did not contribute to the rules

Read-only analysis (no write to AAE): the project rules of AAE (`.project/DEVELOPMENT_RULES.md` on `main` @ `117e7f1`, OM 2.3.0) were read in full and mapped onto the template skeleton and onto `COMMON_RULES.md`. AAE did not contribute to the Common Rules and its rules were not written to follow them, so this supplies the independent observation that the Q6 record of the pre-candidate qualification lacked (recommended follow-up there, not a gate).

**Observation (a): what the rules file shrinks to.** The file has 14 sections; 12 are project-specific and stay under "Project-specific rules" (accepted baselines, SSPL provenance and contract discipline, authority and safety, resilience invariants, cross-project boundary, local operator and evidence pattern, distribution-content profile, productization boundary, open review findings). Only duplicates of OM rules can go: two bullets in "Candidate and historical integrity" (DEV 4, 7, 8) and the three bullets of "OM 2.3.0 project-state conformance" (DEV 29, CORE 6). The section "GitHub Actions runtime hygiene" overlaps with the OM actions runtime gate (`actions_runtime: enforce`), whose map covers the same five actions at the same majors; removing it is a separate decision tied to adopting `enforce`, not to the Common Rules. The shrink is therefore small, as expected for a product-specific rules file.

**Observation (b): is an AAE rule lost?** No. Every AAE-specific rule remains; nothing is replaced by a weaker Common Rule. Where both exist, AAE is the same or stricter (for example locked and digest-verified provider bytes against D1).

**Observation (c): exceptions needed.** None. U1 and U2 (personal data, secrets) and U3 (approval before outward actions) are not stated in the AAE file and would be inherited; U4 agrees with its practice; G does not apply (GitHub with platform enforcement); D2 is optional.

**Frictions found (not blocking RC1):**

1. **U5 is conditional, the table reads unconditional.** The applicability table says U5 applies to DEV ("yes"), while `AI_REVIEW_AUDIT.md` is triggered by `assurance.mode: solo` with a material change, or wherever independent analytical review is required. For AAE the second trigger applies even though it declares no `assurance` key: its work is materially AI-delegated, DEV 25 requires the AI Development Loop, and its review step (item 6) requires independent analytical review of material or protected-surface changes where feasible. The table is therefore right for AI-delegated DEV projects; only the unconditional reading for a non-AI, non-solo project is unclear. Suggested remedy: one clarifying sentence in `COMMON_RULES.md` stating the two triggers (documentation, PATCH-class). This was first stated here with an incomplete trigger analysis and corrected after the Codex review of the pull request.
2. **Pin repeated in the skeleton.** The DEV template skeleton asks for the adopted OM `<ref>` and `<commit>` in the rules file, although `PROJECT.yaml` already pins them. AAE's current file already shows the resulting staleness pattern (its title and conformance section name the OM version and must be edited at every re-pin). Suggested remedy: the skeleton refers to the pin in `PROJECT.yaml` instead of repeating it. Because the skeleton is part of the candidate bytes, a change needs a new candidate (RC2) or a PATCH after GA; the owner decides.
3. **Enforcement by review.** The AAE conformance caller already triggers on `.project/DEVELOPMENT_RULES.md`, so adoption needs no workflow change, but the conformance workflow does not read the content of the rules file (known limit of the readiness record).

Limits of this dry run: it is an analysis of the file, not an adoption; the adoption record of AAE, its evidence and its review practice were not read.

## Verdict

**RC1 qualification: PASS.** A, B and C show no PRODUCT defect. Friction 2 is the only candidate-bytes issue and is a usability finding, not a failure of a qualified claim.

Decision for the owner before GA promotion: (i) promote RC1 unchanged and record friction 2 for a later PATCH, or (ii) create RC2 with a corrected skeleton. GA promotion preserves the normative bytes, so choosing (i) means the skeleton text of friction 2 ships in 2.4.0.

Pilot pull request AAE #73 is to be closed without merging; branch `shadow/om-2.4-rc1-q` is retained as an evidence reference until the owner decides otherwise.

## Non-canonical boundary

Canonical authority remains `om-v2.3.0` (`df716c43a8f19ef15ceb5b2bcc3237b393877c90`). No child project is migrated by RC1.
