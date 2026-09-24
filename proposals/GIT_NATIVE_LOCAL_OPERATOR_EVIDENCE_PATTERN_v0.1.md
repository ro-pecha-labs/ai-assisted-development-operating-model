# Proposal — Git-native Local Operator & Durable Evidence Pattern v0.1

Status: NON_NORMATIVE_PROPOSAL / PENDING_CROSS_TOOLKIT_PILOT
Date: 2026-09-24
Current canonical OM: 2.1.1 / om-v2.1.1 / df9812815a3a83c39b49c66035b4795acd777fc7

## Motivation

AAE demonstrated a recurring workflow where authoritative GitHub source is synchronized locally, qualification executes on the operator workstation, and durable evidence is returned automatically to GitHub.

Observed benefits:
- no manual Downloads workflow;
- no manual evidence upload;
- exact source commit binding;
- reproducible local runtime;
- isolated workspace and cleanup;
- reusable exact-version tool cache;
- dedicated evidence lineage without merging evidence into product branches;
- reduced Git console noise while preserving failure diagnostics.

## Proposed OM-level concept

A future OM revision may define a vendor-neutral **Local Operator / Evidence Return Pattern** for DEV projects.

Candidate normative requirements:

1. Start script resolves repository from its own location, not caller cwd.
2. Local execution starts from a clean Git state and uses targeted fetch plus fast-forward-only synchronization.
3. Missing local tracking branches may be created; ahead/diverged state fails closed.
4. Exact tested source commit is recorded before execution.
5. Immutable external/provider packages are digest-verified and materialized from exact Git objects or immutable package bytes.
6. Each run uses an isolated workspace; reusable tool caches are separate from evidence.
7. Connected runs explicitly declare read-only versus mutation authority before authentication.
8. Governed offline and connected qualification produce durable machine-readable evidence when proving project state.
9. Evidence is published to a dedicated branch rooted at the tested source commit, without automatic merge.
10. Successful publication cleans transient workspace/return package unless explicit retention is requested.
11. Human-facing output is concise; routine Git transport noise may be suppressed while failures retain diagnostics.
12. Project-specific targets, credentials, mutation plans and authority semantics remain project-owned and are not genericized.

## Evidence available

AAE:
- PR3.5 connected READ_ONLY PASS/CLOSED;
- PR3.6 G2 connected READ_ONLY PASS/CLOSED;
- PR3.6 G3A bounded connected READ_ONLY PASS/CLOSED;
- G3 offline durable-evidence publication rule added before final G3 adjudication.

Application Factory:
- provider-neutral candidate extracted;
- SPC and DVC pilot handoffs issued.

## Promotion condition

Do not modify canonical CORE/DEV or create an OM release solely from AAE evidence.

Before normative adoption:
- at least one non-AAE toolkit pilot returns durable PASS evidence;
- portability gaps are resolved;
- candidate requirements are reviewed against DEV evidence proportionality and platform-native enforcement;
- human owner explicitly authorizes OM adoption/release.

## Current disposition

OM 2.1.1 remains unchanged and authoritative.

This file is development input for a future OM revision only.
