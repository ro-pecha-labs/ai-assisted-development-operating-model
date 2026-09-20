# RC1 Root Cause and Successor Contract Decision

**RC1:** `om-v2.0.0-rc1`  
**Disposition:** FAILED_QUALIFICATION / PRODUCT

## Root cause

RC1 separated normative profiles at the prose level, but its machine contracts encoded the Git-native DEV implementation as universal structure.

Affected contracts:

- PROJECT v1 required a Git repository control plane and `.project/ACTIVE_STATE.yaml`;
- ACTIVE_STATE v1 encoded Git commit/branch/PR/issue fields;
- EVIDENCE_RECORD v1 required a Git commit for every evidence subject.

## Successor decision

The successor development line introduces universal v2 contracts while preserving v1 unchanged as historical RC1 contracts.

Universal v2 uses:

- a generic `control_plane` that may be Git or an external authoritative system;
- locator-based active-state pointers;
- generic baseline identity plus typed revision;
- generic active-work pointers;
- generic evidence subject identity plus typed revision.

DEV retains stronger Git semantics in the DEV profile and DEV template rather than in universal schema.

This is a prospective contract change. RC1 evidence and v1 schemas are not reinterpreted.
