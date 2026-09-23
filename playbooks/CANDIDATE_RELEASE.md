# Playbook — Candidate and Release

**Trigger:** DEV work is proposed for release classification, candidate freeze, candidate qualification, acceptance or release.

1. Classify the release assurance mode as `lightweight` or `formal` from the actual release risk and downstream use.
2. Use `formal` when connected mutation authorization binds to the release, destructive/PROD authority is involved, formal downstream adoption requires it, governed external distribution requires candidate semantics, or project policy explicitly requires it.
3. For a lightweight release, bind an immutable release/source identity, run applicable CI/validation, preserve known limitations and bind a package digest where a distributable package is material. Candidate freeze is not required.
4. For a formal release, confirm applicable lessons/recurrence and pre-candidate controls are satisfied.
5. Freeze an immutable candidate ref bound to exact source commit.
6. Bind distributable package digest when a package exists.
7. Persist a durable candidate-freeze evidence record.
8. Qualify the exact frozen identity; failed candidate evidence remains immutable.
9. For machine-verifiable qualification, bind the verdict to the exact execution provider/run, source revision and relevant artifact identity/digest when available. Narrative qualification records summarize and adjudicate evidence; they do not independently establish execution truth.
10. If remediation is required, return to development and create a new candidate identity only after readiness is restored.
11. On acceptance, bind release ref, source commit, package digest where applicable, acceptance evidence and known limitations.
12. Use protected tags/releases or equivalent platform-native controls where qualified.
13. Do not rely exclusively on ephemeral CI logs for long-lived acceptance evidence.

Reclassification from lightweight to formal before release is allowed and does not invalidate prior development work. A release already used as a formal authorization/adoption object shall not be retrospectively downgraded.
