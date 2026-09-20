# OM2-M3 — SPC Shadow Recovery Pilot

**Status:** PASS — NON-CANONICAL DEVELOPMENT

## Objective

Qualify the OM 2.0 minimal DEV recovery model against a real, active SPC development boundary without changing SPC authority or merging pilot state into the product development branch.

## Authority boundary

SPC remained governed by canonical Operating Model v1.6 throughout the pilot.

Google Drive remained the authoritative SPC project state surface. The OM2 shadow bootstrap was created only after the pre-existing Drive/GitHub freshness mismatch was reconciled prospectively under OM v1.6 and read back successfully.

The pilot branch remains non-authoritative:

`pilot/om2-m3-shadow-recovery`

No shadow files were merged into `main` or `feature/document-library`.

## Qualified real-project recovery

The shadow recovery path was:

1. read `.project/PROJECT.yaml`;
2. read `.project/ACTIVE_STATE.yaml`;
3. inspect live PR #2;
4. load the pinned OM2 `CORE.md`;
5. load the pinned DEV profile;
6. load external authoritative state only when a declared conditional trigger requires it.

Recovered current work:

- project: SPC;
- profile: DEV;
- objective: W13-D6;
- trusted baseline: SPC-1.1.2-W12-C1;
- active branch: `feature/document-library`;
- active PR: #2;
- live PR head: `e93f5ae6d7d119d97933d795f067b7bef410f297`;
- phase: pre-candidate;
- active blocker: exact-head successor D6 re-PCQ pending;
- next bounded actions matched the reconciled authoritative Drive boundary.

The recovery result matched the reconciled OM v1.6 state.

## Recovery-volume result

Observed static read-volume proxy for the OM2 path:

- `PROJECT.yaml`: 424 B;
- `ACTIVE_STATE.yaml`: 1,686 B;
- project bootstrap total: 2,110 B;
- pinned `CORE.md`: approximately 2,992 B;
- pinned DEV profile: approximately 4,894 B;
- total static recovery surface before live platform metadata: approximately 10.0 kB.

Current OM v1.6 R0 project/governance files used for the comparison are approximately:

- SPC Active State: 17,371 B;
- SPC Next Work Brief: 12,472 B;
- SPC Development Rules: 11,929 B;
- canonical OM index: 4,716 B;
- subtotal: approximately 46.5 kB, before loading the full canonical OM document.

The real-project OM2 trial therefore reduced this conservative static read-volume proxy by roughly 78% while preserving the trusted current work position.

This is a read-volume proxy, not token telemetry.

## Legacy artifact dependency

Normal shadow recovery did not require:

- Candidate Ledger;
- Current State narrative;
- Next Work Brief;
- Checkpoint package;
- Transition package;
- New Chat Initiation Package;
- full historical reconstruction.

Candidate history and other cold evidence remain available through conditional reads when a concrete action requires them.

## Candidate safety

The pilot initially tested whether candidate disposition needed a new always-hot Active State field.

The resulting decision is to keep candidate history lazy-loaded:

- normal recovery does not load candidate history;
- candidate identity/freeze actions trigger a conditional read of the authoritative current state;
- this preserves fail-closed candidate safety without expanding the normal Active State schema.

No schema expansion was required.

## Schema qualification

The SPC shadow `PROJECT.yaml` and `ACTIVE_STATE.yaml` validate against the current OM2 project and active-state schemas.

## Pre-existing governance gap

The pilot discovered that no physical Drive file named `SPC_ACTIVE_STATE.json` currently exists, despite the current SPC project rule referring to `SPC_ACTIVE_STATE.json/.md`.

This remains an explicit pre-existing `GOVERNANCE_ARTIFACT_GAP`.

It did not invalidate the pilot because the authoritative readable `SPC_ACTIVE_STATE.md` and `SPC_NEXT_WORK_BRIEF.md` were reconciled and read back before the shadow bootstrap was created.

The gap must not be silently reconstructed from inference.

## Safety result

Throughout M3:

- SPC candidate C1 remained immutable failed qualification;
- no C2 candidate was reserved or authorized;
- no connected mutation was authorized or executed;
- no destructive action was authorized or executed;
- no PROD action was authorized or executed;
- no SPC authority migration occurred.

## Acceptance conclusion

OM2-M3 demonstrates on a real active DEV project that the minimal bootstrap model can recover the trusted work position with materially lower static context and without routine legacy handoff artifacts.

OM2-M3 does not authorize canonical OM2 adoption or SPC migration.

The next boundary is a formal OM2 candidate-readiness decision.
