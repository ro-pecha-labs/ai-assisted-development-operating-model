# Playbook — Recovery

**Trigger:** a new session, lost context, explicit continue/recover request, or suspected state drift.

1. Discover the project repository/control plane.
2. Read `PROJECT.yaml` when present.
3. Read the declared active-state pointer.
4. Query only the live platform state referenced by active state.
5. Load the pinned CORE and active profile.
6. Load a conditional source/playbook only when its trigger is present.
7. Compare recovered live state with declared trusted state; classify mismatches before changing anything.
8. Continue from the smallest trusted working set that is sufficient for the objective.
9. Do not reconstruct full history unless a concrete decision, mismatch or audit question requires it.

Normal recovery should not require a transition package or chat history.
