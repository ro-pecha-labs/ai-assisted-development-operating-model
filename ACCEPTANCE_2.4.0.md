# OM 2.4.0 — GA Acceptance

**Status:** ACCEPTED_RELEASE / NON-CANONICAL  
**Accepted tag:** `om-v2.4.0` (annotated, tag object `78d5ead481ea06bc0f0613a454eb282d092d40f1`)  
**Exact accepted commit:** `88466c2dc9a2033d623d1d9bb4ab7a57aebd3445`  
**Release class:** MINOR (`OM_RELEASE_POLICY.md`)  
**Acceptance date:** 2026-10-14

## Basis

OM 2.4.0 is accepted as the MINOR successor of OM 2.3.0. It adds a common project rules layer (`COMMON_RULES.md`: precedence, universal rules U1–U5, default rules D1–D2, applicability table; CORE rule 17 and DEV rule 30), the AI review and audit playbook (`playbooks/AI_REVIEW_AUDIT.md`), the `git_local` platform (example hooks and their qualification script), the DEV rules template skeleton (`templates/DEV/.project/DEVELOPMENT_RULES.md`) and the qualification tool `tools/qualify_om24.py`.

The accepted identity is the immutable Git tag:

`om-v2.4.0 -> 88466c2dc9a2033d623d1d9bb4ab7a57aebd3445`

The tag is annotated; its commit is the squash merge of PR #70 (release identity promotion) into `release/om-2.4`, which descends from `om-v2.3.0` and from the frozen candidate `om-v2.4.0-rc1` (`9ec7f6a8584b04e6d3483ceb5e7c875be7cf66a8`).

## Qualification evidence

- Pre-candidate qualification Q0–Q7: PASS (`OM_2.4_PRE_CANDIDATE_QUALIFICATION.md`); Q6 (shadow pilot) PASS by owner decision with recorded limitations (independence, project records not read).
- Candidate `om-v2.4.0-rc1`: frozen (`qualification/evidence/OM2-2.4.0-RC1_FREEZE_PASS.json`) and qualified (`RC1_QUALIFICATION_2.4.0.md`: PASS). Owner decision: RC1 promoted unchanged.
- Protected PR qualification of the promotion: PR #70, head `7fca89f`, run `38549241353`, SUCCESS; Codex review without findings.

Normative equivalence gate (RC1 -> GA): `git diff om-v2.4.0-rc1 om-v2.4.0` lists only `OM.yaml`, `README.md`, `00_INDEX.md`, `RC1_QUALIFICATION_2.4.0.md` and `qualification/evidence/OM2-2.4.0-RC1_FREEZE_PASS.json`. No normative file, tool, workflow, schema or template differs. PASS.

Exact immutable tag-bound qualification:

- tag: `om-v2.4.0`;
- exact head SHA: `88466c2dc9a2033d623d1d9bb4ab7a57aebd3445`;
- workflow run: `38550361745`;
- event: `push`;
- conclusion: `SUCCESS`.

All 16 `run:` steps of `validate.yml` were also executed locally on a checkout of the tag with `bash -eo pipefail`: 15 executed steps exit 0; the dependency installation step was not re-executed (interpreter dependencies already installed).

Release evidence: `qualification/evidence/OM2-2.4.0_RELEASE_PASS.json`.

## Known limits

- The tag is unsigned.
- Individual clauses of the tag ruleset were not read back in this pass; the connector does not expose ruleset details.
- Friction 1 (RC1 qualification): U5 is conditional while the applicability table reads unconditional; a clarifying sentence is deferred to a PATCH.
- Friction 2 (RC1 qualification): the template skeleton repeats the `<ref>` and `<commit>` placeholders; deferred to a PATCH.
- The shadow pilot (Q6) and the RC1 dry runs were not independent of the author of the rules.
- The hosted call of the reusable conformance workflow at the tag was executed for `om-v2.4.0-rc1` (RC1 qualification B) and not repeated for `om-v2.4.0`; the called bytes are identical.

## Product and semantic disposition

No open OM PRODUCT defect blocks acceptance. CORE rule 17 and DEV rule 30 are the only normative semantic additions; project-state schemas, the project-state validator, the reusable conformance workflow and recovery behavior are unchanged from `om-v2.3.0`. Conformance pass/fail of any caller that does not adopt the new rules is unchanged.

## GitHub Release

GitHub Release `OM 2.4.0` is published (not a pre-release, marked Latest) on tag `om-v2.4.0`.

## Canonical authority

Acceptance of OM 2.4.0 does **not** perform canonical adoption.

Current canonical authority remains:

- version: `2.3.0`;
- tag: `om-v2.3.0`;
- exact commit: `df716c43a8f19ef15ceb5b2bcc3237b393877c90`.

Prospective canonical adoption of OM 2.4.0 requires a separate explicit human authorization and governance-index update. No child project is migrated or re-pinned by this acceptance record.
