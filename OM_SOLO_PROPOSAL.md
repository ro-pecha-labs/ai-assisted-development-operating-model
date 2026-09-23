# OM 2.1 — Solo Assurance & Proportional DEV Proposal

**Status:** DEVELOPMENT PROPOSAL / NON-CANONICAL
**Target:** OM 2.1.0

## Decision

OM Solo is not a new governance profile and is not a fork.

Solo development is an assurance topology orthogonal to the governed work type. OM 2.1 introduces an optional project assurance mode:

```yaml
assurance:
  mode: solo
```

The five existing profiles remain DEV, SOLUTION, DOCUMENT, EXPERIMENT and LIGHT.

Absence of `assurance` preserves the existing standard/default behavior.

## Invariants

Solo mode may alter review and assurance mechanisms but shall not weaken:

- authoritative control-plane semantics;
- historical integrity;
- fail-closed authorization;
- exact target identity;
- destructive/PROD authorization;
- immutable candidate identity where formal candidate semantics apply;
- explicit human authorization where a human authorization is required.

A separate AI model/session may provide analytical independence. It does not become a second human approver and shall not satisfy an external two-person approval requirement unless that external policy explicitly permits it.

## DEV release proportionality

DEV gains two release assurance modes selected per release:

- `lightweight`;
- `formal`.

A lightweight release may omit candidate freeze only when no formal trigger applies.

Formal release semantics are required when the release is used to bind connected mutation authorization, destructive/PROD authority, formal downstream adoption, governed external distribution requiring candidate semantics, or when project policy explicitly requires a candidate.

## Evidence

Machine-verifiable PASS/ACCEPTED claims shall be grounded in machine-addressable execution/artifact evidence when such evidence exists.

Human acceptance remains a decision over evidence and does not substitute for execution truth.

Routine successful CI remains platform telemetry and need not be duplicated as a durable EvidenceRecord unless the event materially changes or proves governance state.

## AI-assisted implementation

OM 2.1 adds a vendor-neutral AI development loop. It bounds implementation scope, establishes the oracle before implementation, protects tests/schemas/fixtures from being weakened to make code pass, and applies independent review proportionately to material/protected surfaces.

Vendor-specific instruction files may specialize the loop but are not universal OM authority.

## Authority model

OM 2.1 does not replace explicit external authority with GitHub-only authority.

Different content classes may have different natural authorities when they are explicitly declared. The no-duplicate-authority rule applies to duplicate authority over the same governed state, not to legitimate separation such as Git source authority plus external immutable evidence/source-input authority.

## Prospective boundary

These changes apply only to projects explicitly adopting a future immutable OM 2.1 release.

OM 2.0.0 projects and historical RC1/RC2/GA evidence are not reinterpreted.
