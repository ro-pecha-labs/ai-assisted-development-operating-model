# Playbook — AI Development Loop

**Trigger:** DEV implementation is materially delegated to an AI coding agent.

1. **Bound the work unit.** State the objective, allowed change surface, invariants and acceptance criteria before implementation.
2. **Establish the oracle.** Expected semantics shall come from accepted requirements, contracts, existing invariants or an explicitly reviewed new decision. Do not infer the expected result solely from the implementation being written.
3. **Protect verification.** An implementation agent shall not weaken tests, schemas, fixtures, golden data or expected results merely to make its implementation pass.
4. **Implement the bounded change.** Avoid unrelated refactoring unless it is required to satisfy the accepted objective.
5. **Run deterministic checks.** Execute applicable parser/static/schema/unit/regression and test-the-tests controls.
6. **Review proportionately.** Material or protected-surface changes receive independent analytical review where feasible. A separate AI model/session may provide analytical independence but does not replace human authorization where human approval is required.
7. **Heightened surfaces.** Schemas, golden fixtures, CI/workflows, dependencies, security-sensitive code, authorization logic and mutation logic require explicit scope and heightened review. A separate PR is preferred when it materially improves review independence; it is not an unconditional requirement.
8. **Adjudicate failures before patching.** Distinguish PRODUCT, HARNESS, ENVIRONMENT, AUTH or INCONCLUSIVE failure where material.
9. **Persist proportionately.** Preserve durable evidence only when the result materially changes or proves governance state.
10. **Merge/accept only after the applicable evidence and review boundary is satisfied.**

Changing AI agent, model or chat does not by itself create governance state.
