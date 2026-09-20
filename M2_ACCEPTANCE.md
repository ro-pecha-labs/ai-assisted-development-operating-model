# OM2-M2 — Recovery Qualification

**Status:** PASS — NON-CANONICAL DEVELOPMENT

## Objective

Demonstrate that normal DEV recovery can start from the minimal machine bootstrap and does not require legacy handoff/state artifacts.

## Synthetic acceptance criteria

- [x] Recovery fixture uses only PROJECT + ACTIVE_STATE as persistent bootstrap.
- [x] Recovery probe reconstructs project/profile/objective/trusted baseline.
- [x] Recovery probe emits only live platform queries referenced by active state.
- [x] No legacy handoff artifact is required.
- [x] No historical reconstruction is required in the normal path.
- [x] GitHub-hosted required check PASS on M2 PR.
- [x] Protected-main PR/merge path proven.
- [x] Post-merge read-back PASS.

## Qualified recovery result

Normal synthetic DEV recovery requires only two persistent bootstrap files:

1. PROJECT.yaml
2. ACTIVE_STATE.yaml

The recovered state identifies project/profile/objective/trusted baseline and only the live platform pointers required for continuation.

No Current State narrative, Next Work Brief, Candidate Ledger, Checkpoint package, Transition package, New Chat Initiation Package or full historical reconstruction is required in the normal path.

## Scope boundary

M2 proves the recovery contract and hosted enforcement path.

Real-world recovery accuracy, context reduction and project-specific migration are qualified separately in the SPC shadow pilot.

M2 does not authorize SPC adoption or canonical OM 2.0 adoption.
