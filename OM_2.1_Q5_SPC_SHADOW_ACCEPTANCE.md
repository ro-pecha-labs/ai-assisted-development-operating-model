# OM 2.1 Q5 — SPC Representative Shadow Acceptance

**Status:** PASS / ACCEPTED QUALIFICATION EVIDENCE / NON-AUTHORITATIVE SHADOW
**Date:** 2026-09-23

## Objective

Qualify OM 2.1 solo assurance, bounded recovery and continuous project-state conformance against a real portfolio DEV project without changing that project's authoritative `main`, release identity or current OM 2.0 adoption.

## Source identity

Project:
`ro-pecha-labs/spc-sharepoint-data-foundation-compiler`

SPC `main` at shadow-branch creation:
`599dadc8cc01af419ecf2178e70c31a539d9008c`

Trusted product baseline preserved:
`SPC-1.3.0-GA / SPC-1.3.0-W14-C1 / SPC_W14_ACCEPTED`

OM 2.1 development revision under qualification:
`8a277e103219fffad1ae4dbab5237debdc10dea2`

Shadow branch:
`pilot/om21-q5-solo-conformance`

## First shadow run

Initial shadow commit:
`a67b100f0ffef5dc4188f5cc7cbe202e54dd4ee7`

Workflow:
`35839800586`

Results:

- bounded solo recovery: PASS;
- PROJECT schema: PASS;
- exact OM commit binding: PASS;
- ACTIVE_STATE schema: PASS;
- project-rules locator: PASS;
- EXTERNAL_SOURCES schema: FAIL.

The failure was caused by two pre-existing `purpose` strings exceeding the 160-character v1 schema bound.

Classification:
`PROJECT_STATE / EXTERNAL_SOURCES_TEXT_BOUND_DRIFT`

This was not treated as an OM schema/product failure and the schema was not relaxed.

## Bounded shadow remediation

Successor shadow commit:
`fb8157ce16f627170520747de2d35c1e8c9ea26d`

Only the two over-length `purpose` descriptions were shortened.

Unchanged:

- external-source IDs;
- locators;
- authority classifications;
- pin modes;
- pinned digests;
- SPC trusted baseline;
- SPC runtime/product bytes;
- mutation/PROD authority.

## Successor machine evidence

Workflow:
`35839945652`

Overall:
`SUCCESS`

Jobs:

- recovery `107112359678`: SUCCESS;
- conformance / project-state-conformance `107112360250`: SUCCESS.

Recovery output:

- `bootstrap_files_read: 2`;
- `project_id: SPC`;
- `profile: DEV`;
- `assurance_mode: solo`;
- `objective_id: SPC-W15`;
- trusted baseline: `SPC-1.3.0-GA / SPC-1.3.0-W14-C1 / SPC_W14_ACCEPTED`;
- `legacy_handoff_required: false`;
- `historical_reconstruction_required: false`.

Measured bootstrap size:

- `.project/PROJECT.yaml`: 711 bytes;
- `.project/ACTIVE_STATE.yaml`: 1,873 bytes;
- total: 2,584 bytes.

## Qualification conclusion

Q5 PASS.

The representative shadow pilot demonstrates that the OM 2.1 design can:

- add solo assurance without adding another always-hot recovery document;
- recover a real DEV project from two bounded bootstrap files;
- enforce exact OM commit binding;
- detect pre-existing project-state drift rather than silently accepting it;
- restore conformance without weakening schema bounds;
- preserve external authority/pin semantics;
- avoid historical reconstruction on normal recovery.

## Nonclaims

This acceptance does not:

- merge the shadow branch into SPC `main`;
- adopt OM 2.1 in SPC;
- change SPC 1.3.0 runtime or release bytes;
- create an SPC candidate;
- authorize connected mutation, destructive mutation or PROD;
- make OM 2.1 canonical.

The SPC shadow branch remains qualification evidence only.
