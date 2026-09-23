# Playbook — Candidate and Release

**Trigger:** DEV work is proposed for candidate freeze, candidate qualification, acceptance or release.

1. Confirm applicable lessons/recurrence and pre-candidate controls are satisfied.
2. Freeze an immutable candidate ref bound to exact source commit.
3. Bind distributable package digest when a package exists.
4. Persist a durable candidate-freeze evidence record.
5. Qualify the exact frozen identity; failed candidate evidence remains immutable.
6. If remediation is required, return to development and create a new candidate identity only after readiness is restored.
7. On acceptance, bind release ref, source commit, package digest where applicable, acceptance evidence and known limitations.
8. Use protected tags/releases or equivalent platform-native controls where qualified.
9. Do not rely exclusively on ephemeral CI logs for long-lived acceptance evidence.
