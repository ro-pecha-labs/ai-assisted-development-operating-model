# OM 2.1 Q5 — Portfolio Shadow Conformance Finding

**Status:** FAIL / CONTROL_IMPLEMENTATION / PRE-CANDIDATE FINDING
**Date:** 2026-09-23

## Trigger

Representative OM 2.1 shadow recovery attempted against current real DEV project state.

## Canonical OM 2.0 contract

`om.active-state/v2` under `om-v2.0.0` requires:

- top-level `additionalProperties: false`;
- `active_work maxItems: 8`;
- `blockers maxItems: 5`;
- `next_actions maxItems: 3`;
- `conditional_reads maxItems: 8`.

## Fresh portfolio observations

The following repositories were read at their live `main` refs.

### DVC

- repository: `ro-pecha-labs/dvc-dataverse-data-foundation-compiler`
- commit: `90038bb34bbc9c95da477adfa9ff16affe32a1ae`
- active_work: 39
- next_actions: 6
- result: NON-CONFORMANT

### DAE

- repository: `ro-pecha-labs/dae-design-analysis-engine`
- commit: `e07bbe3eef7da6d1ea8462bf17600cd90cd6be0d`
- active_work: 2
- next_actions: 4
- result: NON-CONFORMANT

### AAE

- repository: `ro-pecha-labs/aae-application-authorization-engine`
- commit: `60cb01662405b99f51d4f258ec1e84f763f2fb76`
- active_work: 8
- blockers: 5
- next_actions: 7
- additional top-level `authority` property present
- result: NON-CONFORMANT

### SPC

- repository: `ro-pecha-labs/spc-sharepoint-data-foundation-compiler`
- commit: `599dadc8cc01af419ecf2178e70c31a539d9008c`
- active_work: 1
- next_actions: 4
- conditional_reads: 10
- result: NON-CONFORMANT

## Classification

This finding is not classified as a reason to relax the bounded Active State contract.

The observed pattern indicates a CONTROL_IMPLEMENTATION gap:

- OM 2.0 defines the bounded contract;
- initial adoption validates the bootstrap;
- child DEV repositories do not yet have a standard continuous conformance gate for subsequent `.project` changes;
- project state therefore drifted after adoption.

Increasing limits would hide the control gap and increase routine recovery context.

## Corrective design

OM 2.1 adds:

- reusable `tools/validate_project_bootstrap.py`;
- reusable GitHub workflow `.github/workflows/project-state-conformance.yml`;
- DEV guidance requiring ongoing bootstrap conformance where platform enforcement is feasible;
- path-scoped execution guidance so the gate runs on `.project/**` changes rather than every product-code change.

## Qualification disposition

Q5 representative pilot remains NOT PASS until at least one real project is reconciled and the new conformance gate proves PASS at a clean prospective boundary.

The four observed project states are not modified by this OM qualification finding.
