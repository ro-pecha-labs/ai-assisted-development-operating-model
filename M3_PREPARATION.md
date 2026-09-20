# OM2-M3 — SPC Shadow Pilot Preparation

**Status:** BLOCKED — AUTHORITY_FRESHNESS_RECONCILIATION REQUIRED  
**Mode:** READ-ONLY PREPARATION  
**OM2 status:** NON-CANONICAL DEVELOPMENT

## Objective

Prepare an SPC shadow pilot that compares OM v1.6 recovery with OM 2.0 minimal recovery without changing current SPC authority.

## Current authority

SPC remains governed by canonical Operating Model v1.6.

Under the current SPC project rules, Google Drive is the authoritative project repository/state surface. GitHub is a development/runtime evidence source and does not automatically override Drive state.

## Fresh recovery result

The current authoritative Drive state reaches:

- W13 late-candidate PRODUCT re-entry after C1 failed qualification before D9 execution;
- C1 remains immutable `FROZEN_FAILED_QUALIFICATION / NOT_ACCEPTED / DO_NOT_MODIFY`;
- W13-D3 reopened for bounded PRODUCT remediation;
- the canonical unsupported-template semantics decision was accepted;
- Drive current state/brief end with bounded remediation in progress on `fix/w13-unsupported-observed-template-sentinel`.

Live GitHub is materially newer:

- child PR #8 for the unsupported-template sentinel remediation is already merged;
- `feature/document-library` advanced through successor D6 package rebuild and additional HARNESS hardening;
- current live parent PR #2 head is newer than the authoritative Drive tail;
- PR #2 metadata itself contains at least one stale embedded HEAD value relative to its live API head.

## Classification

`AUTHORITY_FRESHNESS_MISMATCH / DOCUMENTATION_LAG`

Confidence: HIGH that the primary mismatch is freshness/synchronization rather than an unresolved product semantic conflict.

This classification does not promote GitHub to authority and does not authorize rewriting Drive state from runtime observations.

## Pilot implication

Do **not** create SPC shadow `.project/PROJECT.yaml` or `.project/ACTIVE_STATE.yaml` while the authoritative Drive state and live GitHub state are materially out of sync.

A shadow bootstrap must be derived from a trusted reconciled boundary, otherwise the pilot could falsely demonstrate successful recovery from stale or mixed authority.

## Required unblock

Before SPC shadow files are created:

1. reconcile current SPC authoritative state under OM v1.6;
2. verify the reconciled Drive state against the intended live GitHub development boundary;
3. establish one trusted shadow-pilot base without changing canonical authority;
4. only then create shadow `.project` files on a non-authoritative pilot branch.

Historical accepted/failed evidence remains immutable.

No candidate, connected mutation, PROD, destructive action, or SPC authority migration is authorized by this preparation record.
