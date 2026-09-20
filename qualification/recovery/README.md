# OM2-M2 Recovery Qualification

**Status:** NON-CANONICAL QUALIFICATION

This fixture tests the smallest normal DEV recovery path without requiring chat history or legacy handoff artifacts.

Expected bootstrap:

1. `PROJECT.yaml`
2. `ACTIVE_STATE.yaml`
3. live platform queries only for pointers declared by active state
4. adopted OM CORE + DEV profile
5. no historical reads unless a concrete trigger requires them

The fixture deliberately does not contain:

- Current State narrative
- Next Work Brief
- Candidate Ledger
- Checkpoint package
- Transition package
- New Chat Initiation Package
- session history

M2 synthetic qualification proves the contract and CI harness. Real-project qualification is deferred to the SPC shadow pilot.
