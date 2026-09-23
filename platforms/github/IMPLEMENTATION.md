# GitHub Platform Implementation — OM 2.0

**Status:** NON-CANONICAL DEVELOPMENT

GitHub is a platform implementation, not part of universal OM semantics.

A GitHub repository is conformant only to the extent that the concrete account/repository capabilities actually enforce the DEV controls on which the project relies.

## Capability tiers

### GH-FULL
Required controls are enforceable by platform-native mechanisms.

### GH-CONDITIONAL
One or more platform controls are unavailable. Missing controls must be identified explicitly and compensated where the project risk permits. Production/destructive connected mutation is blocked by default.

### GH-BLOCKED
Required safety or integrity controls cannot be enforced or acceptably compensated.

## Evidence and connector distinction

AI connector limitations are separate from GitHub platform limitations and must be classified separately. Actions logs/artifacts are not the sole long-term acceptance evidence.

## CI efficiency

GitHub-hosted DEV workflows should apply `CI_EFFICIENCY.md` prospectively. Efficiency controls do not weaken required qualification, evidence, mutation authorization or historical integrity.

## Project-state conformance

For OM 2.1 Git-native DEV projects, use the reusable project-state conformance control described in `PROJECT_STATE_CONFORMANCE.md` to prevent post-adoption drift of `.project` bootstrap records. Scope the caller workflow to governance/bootstrap paths where feasible.
