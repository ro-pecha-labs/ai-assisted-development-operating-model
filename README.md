# AI-Assisted Development Operating Model 2.0

**Status:** NON-CANONICAL DEVELOPMENT  
**Development line:** `2.0.0-dev.5`  
**Current boundary:** formal candidate-readiness contract hardening

This repository is the development surface for Operating Model 2.0. It does **not** supersede the current canonical Operating Model v1.6 until an explicit prospective adoption decision is made.

## Qualification status

- OM2-M0 — DEV Kernel Bootstrap: PASS.
- OM2-M1 — GitHub Control Plane: PASS.
- OM2-M2 — Recovery Qualification: PASS.
- OM2-M3 — SPC Shadow Recovery Pilot: PASS.

The qualified normal DEV recovery path is:

`repository discovery → PROJECT.yaml → ACTIVE_STATE.yaml → live platform state → adopted CORE + profile → triggered playbooks only`.

All five declared profiles, all eight triggered playbooks and all four machine contracts are now represented in the development manifest. CI validates positive/negative schema fixtures, manifest path completeness, profile consistency and repository version coherence.

SPC remains governed by OM v1.6. The shadow pilot branch is non-authoritative and has not been merged into SPC product branches.

Formal candidate creation remains a separate prospective decision after this hardening passes protected CI and read-back.
