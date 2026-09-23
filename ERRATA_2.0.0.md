# OM 2.0.0 — Release Packaging Errata

**Status:** DOCUMENTED / NON-MUTATING / PROSPECTIVE FIX ON DEVELOPMENT MAIN

## Scope

The immutable canonical release remains:

- version: `2.0.0`
- tag: `om-v2.0.0`
- exact commit: `769497a3477cfe5cc676d1ba972728404e9b3551`

No release bytes are modified by this errata record.

## Observed coherence issue

The accepted OM 2.0.0 release was promoted from the qualified RC2 bytes without modifying the normative candidate payload. That preserved exact RC2 qualification integrity, but it also preserved two pieces of candidate-era packaging metadata:

1. local `**Status:** NON-CANONICAL ...` lines inside CORE, profile and playbook documents;
2. the DEV project template pin to `om-v2.0.0-rc2`.

After explicit canonical adoption, those local component status lines are stale as release-state descriptions and the template pin is not appropriate for a new project adopting GA.

## Interpretation

The stale component-local status text does not override canonical authority.

Canonical release status is resolved by:

1. the immutable version/tag/commit identity;
2. `OM.yaml`;
3. the canonical index and explicit adoption record.

The component-local status text is packaging metadata inherited from the frozen qualified candidate.

Historical M0-M3, RC1, RC2, acceptance and adoption records retain their original status statements because those statements describe historical events, not the current status of a normative component.

## Prospective maintenance correction

Development `main` corrects the packaging/coherence issue by:

- removing release/candidate status lines from normative CORE/profile/playbook components so they cannot become a second status authority;
- updating the DEV template to the accepted `om-v2.0.0` tag and exact canonical commit;
- extending structural validation so accepted-release templates cannot retain an RC pin and normative components cannot reintroduce local release-status declarations.

## Historical integrity

This correction:

- does not modify `om-v2.0.0`;
- does not reinterpret RC1 failure;
- does not reinterpret RC2 qualification;
- does not alter GA acceptance or canonical adoption;
- does not change project behavior, safety semantics, profile semantics, schemas or evidence meaning.

A future immutable maintenance or minor release may include the corrected files prospectively.
