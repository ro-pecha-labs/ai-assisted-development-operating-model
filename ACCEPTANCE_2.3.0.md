# OM 2.3.0 — GA Acceptance

**Status:** ACCEPTED_RELEASE / NON-CANONICAL  
**Accepted tag:** `om-v2.3.0` (annotated, tag object `d419a1510a365282fb99af8876f0cc6b9a9ab216`)  
**Exact accepted commit:** `df716c43a8f19ef15ceb5b2bcc3237b393877c90`  
**Release class:** MINOR (`OM_RELEASE_POLICY.md`)  
**Acceptance date:** 2026-10-02

## Basis

OM 2.3.0 is accepted as the MINOR successor of OM 2.2.0. It adds CI efficiency guidance for GitHub-hosted DEV CI: `platforms/github/CI_EFFICIENCY.md` rules 13–19 (parameterized release-line gates, gate closure at acceptance, write-capable single-use workflows keep their narrow trigger, operating system justified by the claim, bounded jobs, governance state churn as a CI input, measurement), a measurement section and a reference pattern for a consolidated gate; `playbooks/CANDIDATE_RELEASE.md` step 14 (gate closure on acceptance); and the read-only measurement tool `tools/ci_usage_report.py` (`static` and `usage`; never blocking).

The accepted identity is the immutable Git tag:

`om-v2.3.0 -> df716c43a8f19ef15ceb5b2bcc3237b393877c90`

The tag is annotated; its commit is the merge of PR #58 (release identity promotion) into `release/om-2.3`, which descends from `om-v2.2.0` (`89de89d0935d61d5442bc8301d9c6c4f2cf7af87`) and from the frozen candidate `om-v2.3.0-rc1` (`e70e97dddeab9a3a941b705c6b478a5e982d8472`).

## Qualification evidence

- Pre-candidate qualification Q0–Q4: PASS (`OM_2.3_PRE_CANDIDATE_QUALIFICATION.md`), including a read-only shadow pilot on DVC, SPC and AAE.
- Candidate `om-v2.3.0-rc1`: frozen (`qualification/evidence/OM2-2.3.0-RC1_FREEZE_PASS.json`) and qualified (`RC1_QUALIFICATION_2.3.0.md`: PASS; the hosted call of the reusable conformance workflow at the tag was not required by owner decision because the called bytes are identical to `om-v2.2.0`).
- Protected PR qualification of the promotion: PR #58, head `1ea3c96`, run `37012927063`, SUCCESS.

Normative equivalence gate (RC1 -> GA): `git diff om-v2.3.0-rc1 om-v2.3.0` lists only `OM.yaml`, `README.md`, `00_INDEX.md`, `RC1_QUALIFICATION_2.3.0.md` and `qualification/evidence/OM2-2.3.0-RC1_FREEZE_PASS.json`. No normative file, tool, workflow, schema or template differs. PASS.

Exact immutable tag-bound qualification:

- tag: `om-v2.3.0`;
- exact head SHA: `df716c43a8f19ef15ceb5b2bcc3237b393877c90`;
- workflow run: `37013239329`;
- event: `push`;
- conclusion: `SUCCESS`.

All 14 `run:` steps of `validate.yml` also passed locally on a checkout of the tag, and `tools/release_identity_guard.py` passed with expected = observed.

Release evidence: `qualification/evidence/OM2-2.3.0_RELEASE_PASS.json`.

## Known limits

- The tag is unsigned.
- Individual clauses of the tag ruleset were not read back in this pass; the connector does not expose ruleset details.
- A GitHub Release `OM 2.3.0` is not published at the time of this record; the latest GitHub release is `om-v2.2.0`. The accepted identity is the tag.
- The hosted call of the reusable conformance workflow was not executed for 2.3.0-rc1 (owner decision, byte identity with `om-v2.2.0`).
- `ci_usage_report.py usage` is an estimate (job minutes rounded up, Windows x2, macOS x10); the Actions `billable` field reports 0 in the pilot repositories.
- OM's own `validate.yml` triggers on `pull_request`, `push` to `main` and `om-v*` tags and is flagged by the new `static` report under rule 6; it is not changed in 2.3 (decision D4).

## Product and semantic disposition

No open OM PRODUCT defect is known. The two findings of the shadow pilot (write-capable workflows flagged for missing concurrency; slow `usage` over about 3 000 runs) were fixed before the candidate. CORE, profiles, schemas of project state, templates, the project-state validator, the reusable conformance workflow and recovery behavior are unchanged from `om-v2.2.0`. Conformance pass/fail of any caller is unchanged.

## Canonical authority

Acceptance of OM 2.3.0 does **not** perform canonical adoption.

Current canonical authority remains:

- version: `2.2.0`;
- tag: `om-v2.2.0`;
- exact commit: `89de89d0935d61d5442bc8301d9c6c4f2cf7af87`.

Prospective canonical adoption of OM 2.3.0 requires a separate explicit human authorization and governance-index update. No child project is migrated or re-pinned by this acceptance record.
