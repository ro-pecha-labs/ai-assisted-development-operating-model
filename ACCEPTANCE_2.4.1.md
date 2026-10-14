# OM 2.4.1 — GA Acceptance

**Status:** ACCEPTED_RELEASE / NON-CANONICAL  
**Accepted tag:** `om-v2.4.1` (annotated, tag object `0eaee4d1fc4f2322c2bc4127095b7c47d1b2a73f`)  
**Exact accepted commit:** `46deca26c3fb880fb5dc25e75d5d2b87bafd0c72`  
**Release class:** PATCH (`OM_RELEASE_POLICY.md`)  
**Acceptance date:** 2026-10-14

## Basis

OM 2.4.1 is accepted as the PATCH successor of OM 2.4.0 (`om-v2.4.0` -> `88466c2dc9a2033d623d1d9bb4ab7a57aebd3445`, current canonical authority). It resolves the two findings recorded as known limits of OM 2.4.0 and the two frictions of the RC1 qualification:

- `platforms/git_local/reference-transaction.example` is committed executable (`100755`); the qualification no longer masks the mode with `chmod +x`.
- `platforms/git_local/pre-commit.example` rejects a declared OM `ref` that does not resolve in `OM_ROOT` to the pinned `commit` (fail closed); the `ref` and the `commit` are read separately, so a `ref` containing whitespace is checked as a whole.
- `qualification/git-local/run_qualification.sh`: 22 checks (was 17); hooks installed by `cp -p`, executable-mode checks, a disposable OM clone with test refs, and negative cases for an unresolvable `ref`, a `ref` resolving to a different commit and a `ref` containing whitespace.
- `templates/DEV/.project/DEVELOPMENT_RULES.md`: the skeleton no longer repeats the OM pin recorded in `PROJECT.yaml`.
- `COMMON_RULES.md` U5: states both triggers, including projects without an `assurance` key.

The accepted identity is the immutable Git tag:

`om-v2.4.1 -> 46deca26c3fb880fb5dc25e75d5d2b87bafd0c72`

The tag is annotated; its commit is the merge of PR #75 (release identity promotion) into `release/om-2.4`, which descends from `om-v2.4.0` and contains PR #74 (the PATCH content).

## Qualification evidence

- No release candidate (PATCH policy: protected PR, structural CI, targeted regression for the defect class, immutable release identity).
- PATCH content PR #74: head `64c6884`, run `38555257591`, SUCCESS; identity promotion PR #75: head `c7b6718`, run `38555600796`, SUCCESS; Codex review without open findings on both.
- Targeted regression: with the `om-v2.4.0` hook the new `ref` cases and the executable-mode checks FAIL; with 2.4.1 all 22 checks PASS (also on a `--depth 1` clone, as in CI).

Normative delta against `om-v2.4.0` (`git diff om-v2.4.0 om-v2.4.1`): `COMMON_RULES.md`, `platforms/git_local/pre-commit.example`, `platforms/git_local/reference-transaction.example` (mode only), `qualification/git-local/run_qualification.sh`, `templates/DEV/.project/DEVELOPMENT_RULES.md` and the identity in `OM.yaml`; the other differences are the non-normative records `README.md`, `00_INDEX.md`, `ACCEPTANCE_2.4.0.md`, `CANONICAL_ADOPTION_2.4.0.md` and `qualification/evidence/OM2-2.4.0_RELEASE_PASS.json`. No schema, validator, workflow or tool of project-state conformance differs.

Exact immutable tag-bound qualification:

- tag: `om-v2.4.1`;
- exact head SHA: `46deca26c3fb880fb5dc25e75d5d2b87bafd0c72`;
- workflow run: `38556301549`;
- event: `push`;
- conclusion: `SUCCESS`.

All 16 `run:` steps of `validate.yml` were also executed locally on a checkout of the tag with `bash -eo pipefail`: 15 executed steps exit 0; the dependency installation step was not re-executed (interpreter dependencies already installed).

Release evidence: `qualification/evidence/OM2-2.4.1_RELEASE_PASS.json`.

## Known limits

- The tag is unsigned; individual clauses of the tag ruleset were not read back in this pass (the connector does not expose ruleset details).
- The shadow pilot (Q6) of OM 2.4.0 and the RC1 dry runs were not independent of the author of the rules; this is unchanged.
- The hosted call of the reusable conformance workflow at the tag was not repeated for `om-v2.4.1`; the called bytes are identical to `om-v2.4.0`.
- The `git_local` hooks are examples; a project shall still record them as compensation in its project rules and verify them in its own repository.

## Product and semantic disposition

No open OM PRODUCT defect is known. The only normative text change is the clarification of `COMMON_RULES.md` U5, which states triggers already defined by `playbooks/AI_REVIEW_AUDIT.md`. Project-state schemas, the project-state validator, the reusable `project-state-conformance.yml` and recovery behavior are unchanged from OM 2.4.0; conformance pass/fail of any caller is unchanged.

## GitHub Release

GitHub Release `OM 2.4.1` is published (not a pre-release, marked Latest) on tag `om-v2.4.1`.

## Canonical authority

Acceptance of OM 2.4.1 does **not** perform canonical adoption.

Current canonical authority remains:

- version: `2.4.0`;
- tag: `om-v2.4.0`;
- exact commit: `88466c2dc9a2033d623d1d9bb4ab7a57aebd3445`.

Prospective canonical adoption of OM 2.4.1 requires a separate explicit human authorization and governance-index update. No child project is migrated or re-pinned by this acceptance record.
