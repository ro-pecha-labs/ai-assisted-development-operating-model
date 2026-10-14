# OM Common Rules

Common Rules are a baseline that every project adopting the exact OM revision inherits. They specialize CORE and the profiles; they do not replace them. A project adds only what is specific to it in its project rules file (`governance.project_rules`).

## Layers and precedence

From highest to lowest:

1. **CORE and profile invariants** (see Invariants). No lower layer may weaken them.
2. **Organization rules** (optional). An organization may refine, specialize or tighten Common Rules. If a rule exists here, it takes precedence over the Common Rule on the same subject.
3. **Common Rules** (this document). They apply when there is no organization layer, and they complement it wherever it is silent or does not conflict.
4. **Project rules.** Project-specific content and explicit, justified exceptions.

A project adopts Common Rules by pinning the OM release (`governance.operating_model`). It does not copy them. A project exception from a Common Rule is recorded in the project rules with its reason and shall not touch an invariant.

## Invariants

No layer below CORE may weaken: authoritative control-plane semantics, historical integrity, fail-closed authorization, exact target identity, destructive and production authorization, immutable candidate identity where formal candidate semantics apply, or explicit human authorization where required.

## Normative wording

"shall" is a requirement. "may" is an optional pattern.

## Section U: Universal (all profiles)

U1. **Personal data.** Personal data shall not be committed to the repository, written into documents, evidence, tests or prompts to external services, or quoted in chat or review text. The agent works with identifiers, counts and pseudonyms. Test fixtures shall be synthetic. The organization may tighten this (scope, named data sources, approval of exceptions).

U2. **Secrets.** Credentials, tokens and keys shall not appear in source, documents or commits. If a secret is pasted into a prompt, the agent warns the user and recommends moving it to the organization's secret store. The organization names that store.

U3. **Outward and irreversible actions.** Commit, tag, push, merge, publishing, sending a message, deleting files and changing a status shall happen only after the user has seen the plan and given explicit approval. Approval for one action does not extend to another. Read-only actions need no approval, but their findings are shown.

U4. **Repository is the source of state.** Decisions, open points and approvals shall be recorded in the project's authoritative state in the session where they arise. An agent's own memory is only a helper; on conflict the repository wins. This refines DEV 20 and 22.

U5. **AI review under solo assurance.** See `playbooks/AI_REVIEW_AUDIT.md`. It applies in two cases: `PROJECT.assurance.mode` is `solo` and the change is material or at an acceptance boundary; or the profile requires independent analytical review (for DEV, materially AI-delegated work under DEV 25 and the review step of `AI_DEVELOPMENT_LOOP.md`). A project without an `assurance` key can still fall under the second case.

## Section D: DEV

D1. **Dependencies.** Libraries shall be installed with locked versions and bundled with the product. A new dependency shall be justified (licence, version, known vulnerabilities). Runtime loading from a CDN or other uncontrolled source is an explicit exception. DEV has no dependency rule today; this is a new DEV rule.

D2. **Work unit lifecycle (may).** An optional convention for AI-delegated work in bounded units (a unit is a project-defined slice of work, e.g. a wave or milestone):

1. A session starts with recovery.
2. The plan is presented and approved before implementation.
3. Evidence, review, human acceptance, then commit, tag and state update, each with approval.
4. At the end of a unit, the agent may recommend whether to continue in the same session or start a new one. This is a recommendation, not a requirement. Because state is persisted and recovery reads only what is needed, switching sessions does not change correctness. The practical reasons are context length (cost and quality) and whether state, evidence and next steps are already in the repository.
5. A failed unit is not overwritten; the repair is a new attempt (see DEV 8).

## Section G: Git control plane without platform enforcement

See `platforms/git_local/README.md`. Applies to Git-native projects whose platform cannot enforce DEV 24 and 29 natively.

## Profile applicability

| Item | DEV | SOLUTION | DOCUMENT | EXPERIMENT | LIGHT |
|---|---|---|---|---|---|
| U1, U2, U3 | yes | yes | yes | yes | yes (U3 where Git or publishing exists) |
| U4 | yes | yes | yes | yes | yes |
| U5 | yes | yes | yes | optional | optional |
| D1 | yes | no | no | optional | no |
| D2 | optional | optional | optional | no | no |
| G | yes | with Git control plane | with Git control plane | no | no |

LIGHT 10 does not want transition packages when a session ends, so D2 does not apply to LIGHT.

## Organization layer and schema

`om.project/v2` has no field for the organization layer. Until a later MINOR release adds one, the project rules file (`governance.project_rules`, which may be a URI) references the organization layer by a pinned revision. Adopting Common Rules needs no `PROJECT.yaml` change beyond pinning the OM release.
