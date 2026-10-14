# OM — Common Project Rules Proposal

**Status:** DEVELOPMENT PROPOSAL / NON-CANONICAL
**Target:** next OM minor release (proposed 2.4.0; the number is assigned by the OM owner)
**Origin:** analysis of the project rules (`.project/DEVELOPMENT_RULES.md`) of an adopting project, CRA Business Mapping (OM 2.3.0, DEV, solo), 2026-10-14
**Candidate files:** `COMMON_RULES.md`, `playbooks/AI_REVIEW_AUDIT.md`, `platforms/git_local/`, `templates/DEV/.project/DEVELOPMENT_RULES.md`
**Decision status:** the proposer accepted the recommendations in section 8 (questions 1, 2 and 4) and the invariant rule; the OM owner has not yet decided.

## 1. Problem

OM 2.3.0 has no mechanism for common project rules. The DEV profile (item 3) makes project rules "conditional, not mandatory", and the template contains only a placeholder. A project that wants operating rules beyond the profile therefore writes and maintains all of them itself. The adopting project produced a set of 14 rules; about half are general, and every further project would copy or reinvent them.

## 2. Proposal

Introduce a **common rules layer** and keep the project rules file as a supplement, not a replacement.

Layers and precedence (highest first):

1. OM core and profile (`CORE.md`, `profiles/DEV.md`): the invariants of section 6, which no lower layer may weaken.
2. **Organization rules**, an **optional layer**. If it exists, it takes precedence over the OM Common Rules: it may refine, specialize and tighten them.
3. **OM Common Rules** (new): a general baseline issued with OM, with no organization-specific or project-specific content. They apply when no organization layer exists, and complement it wherever it does not conflict.
4. The project's `DEVELOPMENT_RULES.md`: only what is specific to the project, and explicit exceptions.

Conflict rule: on conflict the higher layer wins, except for the invariants of layer 1. A rule the organization layer does not address is completed from the OM Common Rules.

A project adopts the common rules by pinning an exact OM revision (already pinned in `governance.operating_model`). It does not copy them. An exception to a common rule shall be recorded in `DEVELOPMENT_RULES.md` with its reason.

## 3. Content of the Common Rules (promoted from the adopting project)

Numbering = the rules in the adopting project's `DEVELOPMENT_RULES.md`.

| # | Rule | Proposed form in OM | Note |
|---|---|---|---|
| 14 | AI review and audit | new playbook `AI_REVIEW_AUDIT.md`, builds on SOLO 4–5 and AI loop 6 | see 3.1 |
| 12 | The repository is the single source of state; agent memory is only a helper | refinement of DEV 20 and 22 | decisions and open points are recorded in the session where they arise |
| 10 | Work unit lifecycle (wave) | optional pattern | see 3.2 |
| 1–4 | Local compensation without platform enforcement | new platform `platforms/git_local/` | see 3.3 |
| 7 | Personal data: not in the repository, documents, evidence, tests or external services; the agent works with identifiers, counts and pseudonyms; fixtures are synthetic | general baseline in OM Common Rules | no organization specifics (data protection officer, named files); the organization may tighten |
| 8 | Secrets: no credentials or tokens in source, documents or commits | general baseline in OM Common Rules | the secret store and the leak procedure are set by the organization |
| 13 | Git: commit, tag and push after user approval; push only to an approved host | general baseline in OM Common Rules | commit message language and the concrete host are set by the organization or project |
| 9 | Dependencies: locked versions, justification for new ones | new DEV rule (DEV has no dependency rule; DEV 25 concerns AI-assisted implementation) | a ban on CDN loading stays project-specific |
| 11 | A failed unit is not overwritten | no OM change | already covered by DEV 8; map the pattern to DEV 8 |

### 3.1 AI review and audit playbook

Trigger: `assurance.mode: solo` and a material change, or any profile that requires independent analytical review.

- The review is performed by a subagent with a clean context, without the implementation conversation. When available, a different model than the implementation is used.
- The brief is a fixed project document (`REVIEW_BRIEF.md`). The implementing agent does not narrow it for a specific work unit, and it changes only with the user's approval.
- The scope is the difference against the last accepted point (commits, uncommitted and new files), not what the implementing agent chooses.
- The subagent is read-only: it changes nothing, commits nothing and does not access remote systems.
- The output is stored unchanged, before the implementation reacts to it. Every finding receives a decision (fixed / rejected with reason / deferred) approved by a human. No finding is dropped.
- The evidence records the model, the scope, the counts by severity, a link, and the line "human self-review of the diff: yes/no".
- After a material fix, the review is repeated.
- The record is an "AI review". It does not replace human acceptance (SOLO 2, 4, 7).

### 3.2 Work unit and session (optional pattern)

OM 22 says that changing the session does not itself create governance state. The pattern therefore prescribes nothing and only offers an optional convention:

1. A new session starts with recovery (PROJECT → ACTIVE_STATE → conditional reads).
2. The plan of the unit is presented and approved; without approval nothing is implemented.
3. Evidence of the unit, review, human acceptance, then commit, tag and ACTIVE_STATE update, each with approval.
4. At the end of a unit the agent **recommends** whether to continue in the same session or start a new one. This is not a requirement. By OM principles (persist state continuously, load minimal context, discover what is needed) switching sessions is irrelevant to correctness. The practical factors are context length (token cost and quality) and whether state, evidence and next steps are recorded in the repository. Decision of the proposer, 2026-10-14; it replaces the hard "one wave = one session" rule of the adopting project.

The terms "wave" and roadmap stay project-specific. OM uses the neutral "work unit".

### 3.3 Platform `git_local` (local enforcement)

For projects without platform enforcement (DEV 24):

- an example `reference-transaction` hook that rejects moving or deleting accepted tags,
- an example `pre-commit` hook that validates staged `.project/*.yaml` against the schemas of the exact OM revision and checks that `ref` matches `commit`,
- the project supplies only its list of forbidden paths and extensions,
- backup by a verified `git bundle` of all refs with a SHA256 sum, without overwriting or deleting existing backups,
- procedural checks (build, tests) that replace missing CI are explicitly recorded as compensation.

## 4. OM changes beyond the rules

- **Validator without Python.** The OM validator currently requires Python. The adopting project replaces it with its own Node validator for that reason. Recommendation: OM provides a validator with no dependency on Python, or a reference implementation independent of the environment, so that project-specific validators become unnecessary.
- **Template.** Replace `templates/DEV/.project/DEVELOPMENT_RULES.md` with a skeleton with the sections "Adopted common rules (OM revision)", "Exceptions" and "Project-specific rules".

## 5. What does not belong in OM

- Organization-specific content in rules 7, 8 and 13 (data protection officer, secret store, concrete files with personal data, commit message language, approved hosting). OM contains only the general wording; the organization supplies the concrete form.
- Project content: data sources (6), the brief (5), backups to a concrete SharePoint location (4), a CDN ban (9), the list of forbidden files (2).

## 6. Invariants

The common layer shall not weaken: authoritative control-plane semantics, historical integrity, fail-closed authorization, exact target identity, destructive and production authorization, or explicit human authorization. A project exception to a common rule shall never cancel anything on this list.

## 7. Impact on projects

- Existing projects do not change until they adopt a new OM revision (`PROJECT.yaml` is pinned).
- Adopting the common layer means changing `governance.operating_model` to the new revision and reducing `DEVELOPMENT_RULES.md` to the project specifics. Backward compatibility is preserved because a project rule may be stricter than a common one.

## 8. Open questions

**Decided by the proposer (2026-10-14):** the OM invariants (section 6) shall not be weakened by any lower layer, including the higher-precedence organization layer. The organization layer may only refine or tighten the common rules.

Questions 1, 2 and 4: assessed, and the proposer accepted the recommendations. Question 3 remains open. The OM owner decides on all of them.

1. **Schema `om.project/v2`: assessed.**
   - `PROJECT.v2.schema.json` has `additionalProperties: false` at every level, including `governance`. A new field in `PROJECT.yaml` would therefore be a schema change, and an older validator would reject a project that has it.
   - **No field is needed to adopt the Common Rules.** They are part of the OM release that the project already pins through `governance.operating_model` (`ref`, `commit`).
   - **The organization layer** does need a field, but there is a workaround without a schema change. `governance.project_rules.locator` may be a URI (for `://`, `validate_project_bootstrap.py` does not check that the file exists), and the project rules file may reference the organization layer by a pinned revision.
   - Recommendation: Common Rules **without a schema change**. For the organization layer optionally add `governance.organization_rules` (`repository`, `ref`, `commit`) as an extension of the v2 schemas in the next minor OM release. Until the owner of the layer is decided (question 3), use the workaround via `project_rules`.
2. **Obligation and versioning: assessed.**
   - For DEV, OM already states some rules as "shall" (e.g. DEV 25, SOLO 4–5). The common rules refine them and are not a new burden.
   - Recommendation: the Common Rules are **part of the OM release** (not versioned separately) and **mandatory for DEV with a justified exception** recorded in `DEVELOPMENT_RULES.md`. An exception shall not touch the invariants of section 6.
   - Rules that are an optional pattern (work unit and session, 3.2) are marked "may", not "shall".
   - Reason: without an obligation the layer would not be used and every project would keep writing its own rules. Separate versioning would add a second pinning dimension to `PROJECT.yaml` without benefit.
3. **Owner of the organization layer.** The owner of an organization layer is not yet known. The layer is optional, and without it the OM Common Rules apply, so the question does not block. It remains open whether and where an organization layer will be created (e.g. a separate repository referenced from `PROJECT.yaml`).
4. **Applicability to other profiles: assessed from the text of the DEV, SOLUTION, DOCUMENT, EXPERIMENT and LIGHT profiles.**

   | Rule / item | DEV | SOLUTION | DOCUMENT | EXPERIMENT | LIGHT |
   |---|---|---|---|---|---|
   | 7 personal data, 8 secrets | yes | yes | yes | yes | yes |
   | 13 approval before commit/tag/push | yes | yes | yes | yes | yes, only where Git exists |
   | 14 AI review and audit (solo) | yes | yes, complements SOLUTION 6 | yes, complements DOCUMENT 6 | optional | optional |
   | 12 repository is the source of state | yes (DEV 20) | yes (SOLUTION 3) | yes (DOCUMENT 3) | yes (EXPERIMENT 3) | yes (LIGHT 2) |
   | 1–4 `git_local` | yes | only with a Git control plane | only with a Git control plane | no | no |
   | 9 dependencies | yes | no | no | optional | no |
   | 10 work unit and session | optional | optional | optional | no | no |

   - The AI review and audit playbook is tied to `assurance.mode: solo` (SOLO_ASSURANCE is independent of the profile), so it applies across profiles wherever solo mode is used.
   - Reason for "no" on LIGHT: LIGHT 10 explicitly does not want transition packages at the end of a session. A work unit and session convention would contradict the spirit of the profile.
   - Recommendation: split the Common Rules into **universal** (7, 8, 12, 13, AI review for solo), **DEV** (9, 10) and **Git** (1–4), with each profile referring only to the relevant section.

## 9. Next steps (require approval)

1. Review of this proposal and the candidate files by the OM owner.
2. Decision on the recommendations to questions 1, 2 and 4, and on question 3 (owner of the organization layer).
3. Validate on a machine with Python (`tools/validate.py`) or in CI on the branch. Registering `AI_REVIEW_AUDIT.md` in `OM.yaml` requires changing `EXPECTED_PLAYBOOKS` in `tools/validate.py`; this is intentionally not part of this branch.
4. Only then, adapt the adopting project's `DEVELOPMENT_RULES.md`.
