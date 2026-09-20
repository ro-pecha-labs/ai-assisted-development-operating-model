# OM2-M2 — Recovery Qualification

**Status:** IN PROGRESS — NON-CANONICAL DEVELOPMENT

## Objective

Demonstrate that normal DEV recovery can start from the minimal machine bootstrap and does not require legacy handoff/state artifacts.

## Synthetic acceptance criteria

- [x] Recovery fixture uses only PROJECT + ACTIVE_STATE as persistent bootstrap.
- [x] Recovery probe reconstructs project/profile/objective/trusted baseline.
- [x] Recovery probe emits only live platform queries referenced by active state.
- [x] No legacy handoff artifact is required.
- [x] No historical reconstruction is required in the normal path.
- [ ] GitHub-hosted required check PASS on M2 PR.
- [ ] Protected-main PR/merge path proven.
- [ ] Post-merge read-back PASS.

## Real-project acceptance

Real-world recovery accuracy and context reduction are qualified in the SPC shadow pilot; synthetic M2 alone does not authorize SPC adoption.
