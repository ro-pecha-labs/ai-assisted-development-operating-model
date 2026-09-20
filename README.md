# AI-Assisted Development Operating Model 2.0

**Status:** NON-CANONICAL DEVELOPMENT  
**Development line:** `2.0.0-dev.3`  
**Current milestone:** `OM2-M3 — SPC Shadow Recovery Pilot: PASS`

This repository is the development surface for Operating Model 2.0. It does **not** supersede the current canonical Operating Model v1.6 until an explicit prospective adoption decision is made.

## Qualification status

- OM2-M0 — DEV Kernel Bootstrap: PASS.
- OM2-M1 — GitHub Control Plane: PASS.
- OM2-M2 — Recovery Qualification: PASS.
- OM2-M3 — SPC Shadow Recovery Pilot: PASS.

The qualified normal DEV recovery path is:

`repository discovery → PROJECT.yaml → ACTIVE_STATE.yaml → live platform state → adopted CORE + profile → triggered playbooks only`.

The real SPC shadow pilot recovered the current trusted W13 work position from a 2.1 kB project bootstrap and about 10 kB of total static OM2 recovery material before live platform metadata, versus about 46.5 kB for the compared OM v1.6 R0 governance subset before the full canonical OM document.

SPC remains governed by OM v1.6. The shadow pilot branch is non-authoritative and has not been merged into SPC product branches.

The next boundary is a formal OM2 candidate-readiness decision; no additional numbered milestone is declared yet.
