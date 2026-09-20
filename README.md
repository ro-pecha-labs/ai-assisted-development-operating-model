# AI-Assisted Development Operating Model 2.0

**Status:** NON-CANONICAL DEVELOPMENT — READY TO FREEZE FORMAL CANDIDATE  
**Development line:** `2.0.0-dev.5`  
**Target candidate:** `OM2-2.0.0-RC1` / tag `om-v2.0.0-rc1`

This repository is the development surface for Operating Model 2.0. It does **not** supersede the current canonical Operating Model v1.6 until an explicit prospective adoption decision is made.

## Qualification status

- OM2-M0 — DEV Kernel Bootstrap: PASS.
- OM2-M1 — GitHub Control Plane: PASS.
- OM2-M2 — Recovery Qualification: PASS.
- OM2-M3 — SPC Shadow Recovery Pilot: PASS.
- Formal candidate readiness: READY_TO_FREEZE, pending immutable tag creation after exact post-merge CI.

The qualified normal DEV recovery path is:

`repository discovery → PROJECT.yaml → ACTIVE_STATE.yaml → live platform state → adopted CORE + profile → triggered playbooks only`.

All five declared profiles, all eight triggered playbooks and all four machine contracts are represented in the development manifest. CI validates positive/negative schema fixtures, manifest path completeness, profile consistency and repository version coherence.

SPC remains governed by OM v1.6. The shadow pilot branch is non-authoritative and has not been merged into SPC product branches.

Creating the formal candidate does not make OM2 canonical and does not authorize project adoption.
