# GitHub Project-State Conformance — OM 2.1

**Status:** PROSPECTIVE DEVELOPMENT GUIDANCE

## Purpose

Prevent post-adoption drift of the machine bootstrap in Git-native DEV repositories.

The conformance gate validates the caller repository's:

- `.project/PROJECT.yaml`;
- declared local `ACTIVE_STATE`;
- declared local `EXTERNAL_SOURCES` manifest when present;
- declared local project-rules locator when present;
- exact adopted OM commit binding.

It uses the schemas from the exact adopted OM revision rather than schemas copied into the child repository.

## Reusable workflow

OM provides:

`.github/workflows/project-state-conformance.yml`

The caller passes its immutable adopted OM ref. The reusable workflow checks out that OM revision and the validator additionally verifies that the checked-out OM commit equals the exact commit pinned by the caller's `PROJECT.yaml`.

## Recommended caller

After adoption of an immutable OM 2.1 release, a GitHub DEV project may use:

```yaml
name: OM project-state conformance

on:
  pull_request:
    paths:
      - '.project/**'
  push:
    branches:
      - main
    paths:
      - '.project/**'

permissions:
  contents: read

jobs:
  conformance:
    uses: ro-pecha-labs/ai-assisted-development-operating-model/.github/workflows/project-state-conformance.yml@om-v2.1.0
    with:
      om_ref: om-v2.1.0
```

The immutable ref in the caller and the exact commit in `PROJECT.yaml` must describe the same adopted OM release.

## GitHub Actions runtime check

The reusable workflow also scans the caller's `.github/workflows` for GitHub Actions pinned below the lowest major that runs on Node.js 24 (`tools/actions_runtime_map.json`, official `actions/*` only).

The caller selects the behavior with the optional input `actions_runtime`:

- `report` (default): findings are printed, written to the job summary and raised as a warning; the job result is not affected;
- `enforce`: the job fails when a mapped action is pinned below its Node.js 24 major.

Any other value fails the job. Official actions that are not in the map (`UNJUDGED`) and third-party actions do not fail in either mode. `enforce` requires the adopted OM revision (`om_ref`) to provide `tools/actions_runtime_gate.py`; otherwise the job fails closed. The check runs when the caller workflow runs, so a caller that should catch workflow-only changes must also trigger on them.

```yaml
    with:
      om_ref: om-v2.2.0
      actions_runtime: enforce
```

## Cost model

The gate is intentionally:

- Linux-hosted;
- read-only;
- path-scoped to `.project/**`;
- free of package publication and durable artifact upload;
- independent of product runtime matrices.

Ordinary product-code changes therefore do not trigger this governance check unless their workflow explicitly chooses to do so.

## Failure meaning

A conformance failure does not authorize automatic expansion of schema bounds.

First classify whether the failure is:

- PROJECT_STATE drift;
- schema/product defect;
- harness/tooling defect;
- migration/coherence defect.

For overgrown Active State, prefer moving history/detail into objective/evidence records and keeping the recovery index bounded.
