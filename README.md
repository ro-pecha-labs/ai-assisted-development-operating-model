# AI-Assisted Development Operating Model 2.0

**Status:** NON-CANONICAL DEVELOPMENT  
**Development line:** `2.0.0-dev.3`  
**Current milestone:** `OM2-M3 — SPC Shadow Pilot preparation`

This repository is the development surface for Operating Model 2.0. It does **not** supersede the current canonical Operating Model v1.6 until an explicit prospective adoption decision is made.

## Qualification status

- OM2-M0 — DEV Kernel Bootstrap: PASS.
- OM2-M1 — GitHub Control Plane: PASS.
- OM2-M2 — Recovery Qualification: PASS.
- OM2-M3 — SPC Shadow Pilot: PREPARATION BLOCKED pending authoritative SPC state reconciliation.

The qualified normal DEV recovery path is:

`repository discovery → PROJECT.yaml → ACTIVE_STATE.yaml → live platform state → adopted CORE + profile → triggered playbooks only`.

M3 deliberately stops before writing shadow state into SPC because the current authoritative Drive state is older than the live GitHub development state. Reconciliation under OM v1.6 is required before the shadow pilot can begin.
