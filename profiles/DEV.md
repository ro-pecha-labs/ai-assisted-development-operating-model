# AI-Assisted Development Project Operating Model 2.0
## Profile: DEV

**Status:** NON-CANONICAL DEVELOPMENT

1. **DEV control plane.** DEV normally requires a Git-based authoritative project control plane. A non-Git exception must demonstrate equivalent source identity, history, candidate immutability, release identity, recoverability and evidence integrity.
2. **Git-native bootstrap specialization.** A normal Git-native DEV project uses `om.project/v2` with `control_plane.kind: git`, an active-state locator such as `.project/ACTIVE_STATE.yaml`, and `om.active-state/v2`. Trusted DEV baselines should bind a `git_commit` revision; live work pointers normally identify branch, pull request and/or issue as applicable.
3. **Minimum bootstrap.** A Git-native DEV project shall provide PROJECT and ACTIVE_STATE bootstrap records. Project-specific rules and external-source manifests are conditional, not mandatory by default.
4. **Development iterations.** Ordinary engineering revisions remain mutable development work. Candidate identity is reserved for a gate-ready revision intended to enter candidate qualification.
5. **Pre-candidate readiness.** Applicable syntax/parser, schema/static, unit/regression, recurrence, provenance, packaging and harness-self-validation controls shall pass before candidate creation where technically relevant.
6. **Test-the-tests.** Critical validators and harnesses shall demonstrate known-good PASS and relevant known-bad FAIL behavior, plus success-path orchestration where reasonable.
7. **Candidate identity.** Candidate identity shall bind an immutable candidate reference, exact source commit and durable candidate evidence record; distributable packages also bind their digest.
8. **Candidate qualification.** Failed candidates remain historically failed and are not patched in place. A revised gate-ready product receives a new candidate identity.
9. **Failure diagnosis.** Significant failures use at least PRODUCT, HARNESS, ENVIRONMENT, AUTH or INCONCLUSIVE classification when source is not self-evident, with least-invasive discriminating diagnosis preferred.
10. **Recurrence control.** A second confirmed occurrence of the same root-cause class triggers generalization into reusable prevention where feasible. A third occurrence after prevention is a control-process failure until resolved or disproven as the same class.
11. **Lessons.** Recurring lessons should preferentially become executable guards, tests, schemas or workflow controls. Fully enforced lessons need not be manually re-assessed at every candidate freeze.
12. **External input identity.** Material external sources used for immutable candidate/release claims shall be pinned strongly enough to reproduce or audit those claims; floating references normally require explicit exception.
13. **Durable evidence.** Routine successful CI does not require durable EvidenceRecords. Material events such as candidate freeze, significant candidate failure, connected qualification, acceptance, release, risk acceptance and governed mutation do.
14. **Release identity.** Accepted releases bind release reference, source commit, package/artifact digest where applicable and acceptance evidence. Long-lived acceptance shall not depend exclusively on ephemeral CI logs.
15. **Connected lifecycle.** Connected work shall separate read-only understanding from mutation; a typical lifecycle is `Validate → Observe → Plan → Authorize → Apply → Verify → NoChange`.
16. **Mutation authorization.** Mutation authorization shall bind exact candidate/release, exact target, exact plan/action identity where applicable, exact operation scope and required human approval. Authorization is fail-closed and should resist unintended replay.
17. **Destructive operations.** Destructive actions require explicit destructive scope and authorization; production destructive operations require explicit production and destructive authority.
18. **Environment safety.** Connected qualification/mutation shall strongly identify target environment. NON_PRODUCTION is the default mutation target unless explicitly authorized otherwise. Production authority is never inferred.
19. **Verification and idempotence.** Where convergent/idempotent behavior is claimed, qualification shall include appropriate Apply/Verify/NoChange or equivalent proof.
20. **Active state.** ACTIVE_STATE is a concise semantic recovery index and shall not duplicate project history or live platform state that is authoritatively queryable.
21. **Recovery.** Normal DEV recovery requires project discovery, PROJECT, ACTIVE_STATE, relevant live platform state, the DEV profile and only triggered playbooks.
22. **Handoff.** Changing chat/session does not itself create governance state. Separate handoff records are exceptional.
23. **Closure.** Accepted DEV baselines preserve exact accepted identity, relevant acceptance evidence, known limitations and sufficient lineage without loading full development history into active context.
24. **Platform implementation.** Git-platform protections, CI, reviews, protected refs, releases and environments should enforce these requirements natively where feasible, and configuration shall be qualified before replacing manual controls.
