# Playbook — Failure Diagnosis

**Status:** NON-CANONICAL DEVELOPMENT  
**Trigger:** significant failure, connected failure, ambiguous regression or repeated root-cause class.

1. Preserve the failed evidence before remediation.
2. Classify the failure as PRODUCT, HARNESS, ENVIRONMENT, AUTH or INCONCLUSIVE when the source is not already proven.
3. Identify the earliest trusted boundary and the smallest discriminating question.
4. Prefer read-only or least-invasive diagnostics.
5. Distinguish observed runtime behavior from authoritative contract/source truth.
6. Patch only after the failure source is sufficiently discriminated.
7. Re-run from the earliest invalidated prerequisite, not automatically from the beginning.
8. On recurrence, generalize into a guard/test/schema/workflow control where feasible.
9. Never patch an immutable candidate in place; create a successor only after applicable readiness gates.
