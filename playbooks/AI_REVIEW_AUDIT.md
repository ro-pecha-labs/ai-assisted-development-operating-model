# Playbook — AI Review and Audit

**Trigger:** `PROJECT.assurance.mode: solo` and a material change or acceptance boundary; or any profile that requires independent analytical review.

This playbook operationalizes SOLO_ASSURANCE 4–5 and AI_DEVELOPMENT_LOOP 6.

1. **Independence.** The review is performed by a subagent started with a clean context that does not contain the implementation conversation. When available, a different model than the implementation is used.
2. **Brief.** The review prompt is a fixed project document (for example `.project/REVIEW_BRIEF.md`). The implementing agent shall not narrow it for a specific work unit. It changes only with the user's approval.
3. **Scope.** The scope is the full difference against the last accepted baseline (commits, uncommitted and new files) plus the evidence of the work unit. The scope is determined by the difference, not by the implementing agent.
4. **Read-only.** The reviewer changes nothing, commits nothing and does not access remote systems. Compare the working tree status before and after the review.
5. **Output stored unchanged.** The output is saved verbatim before the implementing agent reacts to it.
6. **Disposition of every finding.** Every finding receives a separate decision: fixed, rejected with reason, or deferred. The human approves the dispositions. No finding is dropped.
7. **Evidence.** The evidence records the model, the scope, the finding counts by severity, a link to the output and the line "human self-review of the diff: yes/no".
8. **Fixes and repetition.** A fix is an ordinary change (build, tests). After a material fix, the review is repeated on the new state.
9. **Status.** The record is an AI review. It does not replace human acceptance and does not satisfy an external two-person approval requirement (SOLO_ASSURANCE 2, 4, 7).
