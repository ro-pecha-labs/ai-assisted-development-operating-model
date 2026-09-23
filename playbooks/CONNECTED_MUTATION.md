# Playbook — Connected Mutation

**Trigger:** any governed action may mutate an external system.

1. Separate read-only discovery/Observe/Plan from mutation.
2. Resolve the exact target identity and environment classification.
3. Default mutation target to explicitly identified NON_PRODUCTION unless stronger authority is granted.
4. Produce the exact plan/action set before authorization where applicable.
5. Bind authorization to exact candidate/release, target, plan/action identity and permitted operations.
6. Destructive scope requires separate explicit destructive authority.
7. Fail closed on target mismatch, stale plan, missing approval, replay ambiguity or authorization mismatch.
8. Apply only the authorized operation set.
9. Verify resulting state and, when claimed, prove convergent NoChange/idempotence.
10. Preserve durable mutation evidence proportionate to impact.

PRODUCTION and destructive authority are never inferred.
