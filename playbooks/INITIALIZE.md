# Playbook — Initialize

**Trigger:** creation of a new governed project or prospective adoption of OM by an ungoverned project.

1. Classify the primary profile from the real work objective.
2. Declare an assurance mode only when a non-default topology is needed; `assurance.mode: solo` is orthogonal to the primary profile and triggers the Solo Assurance playbook.
3. Declare the authoritative project control plane.
4. Create the minimum profile-specific bootstrap; for Git-native DEV this is `PROJECT.yaml` plus `ACTIVE_STATE.yaml`. When starting from a distributed template, replace the OM ref and all-zero commit sentinel with the exact immutable OM release actually adopted before validation or use.
5. Declare external authorities rather than copying them when they remain authoritative elsewhere.
6. Establish only the platform protections and CI controls required by the selected profile/risk. For GitHub-hosted DEV CI, apply the GitHub CI efficiency policy in `platforms/github/CI_EFFICIENCY.md` when applicable.
7. Record project-specific rules only where they specialize the profile.
8. Validate the bootstrap structurally.
9. For Git-native DEV, establish an ongoing project-state conformance gate where platform enforcement is feasible; scope it to governance/bootstrap paths rather than unrelated product changes.
10. Start work; do not pre-create historical ledgers, transitions or evidence folders that have no current use.

Reclassification later is prospective.
