# AI-Assisted Development Operating Model 2.0

**Status:** NON-CANONICAL DEVELOPMENT  
**Development line:** `2.0.0-dev.4`  
**Current boundary:** formal candidate-readiness blocker closure

This repository is the development surface for Operating Model 2.0. It does **not** supersede the current canonical Operating Model v1.6 until an explicit prospective adoption decision is made.

## Qualification status

- OM2-M0 — DEV Kernel Bootstrap: PASS.
- OM2-M1 — GitHub Control Plane: PASS.
- OM2-M2 — Recovery Qualification: PASS.
- OM2-M3 — SPC Shadow Recovery Pilot: PASS.

The qualified normal DEV recovery path is:

`repository discovery → PROJECT.yaml → ACTIVE_STATE.yaml → live platform state → adopted CORE + profile → triggered playbooks only`.

All five declared governance profiles and the bounded triggered playbook set now exist in the development repository. They are lazy-loaded; their existence does not expand the normal recovery working set.

SPC remains governed by OM v1.6. The shadow pilot branch is non-authoritative and has not been merged into SPC product branches.

Formal OM2 candidate creation remains blocked until schema/CI contract hardening is qualified.
