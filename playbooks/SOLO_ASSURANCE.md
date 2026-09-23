# Playbook — Solo Assurance

**Trigger:** `PROJECT.assurance.mode: solo`.

1. Preserve the selected primary profile. SOLO is an assurance topology, not a governance profile.
2. Do not claim independent human review when the same human owner authored and approved the change.
3. Prefer deterministic platform checks, immutable identities and machine-verifiable evidence over additional narrative ceremony.
4. A separate AI model/session may perform independent analytical review when proportionate. Record it as AI review, not human approval.
5. Material changes require an explicit human self-review of the resulting diff/decision before acceptance.
6. For high-impact changes, temporal separation between implementation and final human acceptance is recommended when practical.
7. If an external policy requires two-person approval and no second eligible human is available, classify the control as unavailable or blocked. Do not satisfy it fictionally with AI review.
8. Connected mutation still requires exact human authorization where required by the active profile/playbook.
9. Destructive and PROD authority are never weakened by solo mode.
10. Candidate immutability, historical integrity and authority boundaries remain unchanged.
11. Use the AI Development Loop for materially AI-delegated DEV implementation.
