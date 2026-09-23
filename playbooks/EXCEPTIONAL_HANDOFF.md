# Playbook — Exceptional Handoff

**Trigger:** work must move between agents/sessions while material in-flight state is not yet durably represented by normal project/platform state.

1. Prefer normal repository recovery; do not create a handoff merely because a chat ends.
2. Capture only the missing in-flight delta: trusted base, active hypothesis/work, unresolved blockers and next bounded action.
3. Reference existing evidence instead of copying it.
4. Mark assumptions and unresolved classifications explicitly.
5. Avoid duplicating live branch/PR/CI state that can be queried directly.
6. Consume or supersede the exceptional handoff once normal durable state catches up.

A clean persisted boundary requires no separate handoff artifact.
