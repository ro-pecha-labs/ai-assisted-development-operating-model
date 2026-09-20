# AI-Assisted Development Operating Model 2.0

**Status:** NON-CANONICAL DEVELOPMENT  
**Development line:** `2.0.0-dev.5`  
**Frozen candidate:** `OM2-2.0.0-RC1` — **FAILED_QUALIFICATION / PRODUCT / NOT_ACCEPTED / DO_NOT_MODIFY**  
**Candidate tag:** `om-v2.0.0-rc1`

This repository is the development surface for Operating Model 2.0. It does **not** supersede canonical Operating Model v1.6.

## Qualification status

- OM2-M0 — DEV Kernel Bootstrap: PASS.
- OM2-M1 — GitHub Control Plane: PASS.
- OM2-M2 — Recovery Qualification: PASS.
- OM2-M3 — SPC Shadow Recovery Pilot: PASS.
- RC1 freeze integrity: PASS.
- RC1 tag-bound structural validation: PASS.
- RC1 cross-profile semantic qualification: **FAIL / PRODUCT**.

RC1 remains immutable failed evidence. It must not be patched in place.

The blocking defect is that the frozen universal `PROJECT.schema.json` requires Git repository semantics and `.project/ACTIVE_STATE.yaml` for every profile, while SOLUTION, DOCUMENT, EXPERIMENT and LIGHT allow non-Git authoritative control planes.

Development must produce a successor universal bootstrap contract before any new candidate freeze.

Canonical OM remains v1.6 and SPC remains governed by v1.6.
