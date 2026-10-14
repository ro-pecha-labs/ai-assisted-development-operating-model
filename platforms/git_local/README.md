# Platform: `git_local` (compensation without platform enforcement)

For Git-native projects whose control plane is a local repository or any Git host that cannot enforce protected refs and required checks (`control_plane.platform: git_other`). These controls compensate for DEV 24 and 29 until native enforcement exists, and shall be recorded in the project rules as compensation.

## Controls

1. **Versioned hooks.** Hooks live in `.githooks/` and are enabled per clone with `git config core.hooksPath .githooks`. They are committed with the executable flag. After cloning, verify they run (for example, a staged probe file of a forbidden type shall be rejected).
2. **`reference-transaction`.** Rejects moving or deleting accepted tags (a project-defined pattern, for example `*-pass`). Example: `reference-transaction.example`.
3. **`pre-commit`.** Rejects staged forbidden content (temporary markers, data files outside fixtures) and validates the staged project bootstrap against the exact adopted OM revision. Example: `pre-commit.example`. The project lists its own paths and extensions.
4. **Bootstrap validation.** Staged `.project/*.yaml` is validated against the schemas of the exact OM revision in `PROJECT.yaml`, and `ref` shall correspond to the pinned `commit`. A missing OM repository or validator dependency stops the commit. A validator that does not need a particular runtime is preferred.
5. **Backup outside the machine.** Without a remote, the repository exists only on one disk. Back up by a verified `git bundle` of all refs plus a SHA256 file, into a location outside the machine. Existing backups are never overwritten or deleted. Back up after each accepted tag and after each change of `.project/`.
6. **Procedural checks.** Build and tests before a commit of code are a procedure instead of required CI. The evidence binds the commit hash.
7. **No bypass.** `--no-verify` requires the user's explicit approval. Test hooks by running them directly, not by trial commits. Do not name probe tags with the accepted-tag pattern (the hook then forbids deleting them).

## Not allowed

These compensations do not weaken any invariant or replace human approval where it is required.
