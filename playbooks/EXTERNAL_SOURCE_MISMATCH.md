# Playbook — External Source Mismatch

**Trigger:** project state, runtime, cache, documentation or an external authoritative source disagree.

1. Identify the content class in dispute and its declared authority.
2. Read the freshest relevant authoritative revision and the conflicting representation.
3. Classify the difference: freshness lag, generated-view drift, runtime divergence, contract mismatch, integrity mismatch or inconclusive.
4. Do not make runtime behavior authoritative merely because it is newer.
5. Do not rewrite authoritative documentation solely to match an observation.
6. Reconcile prospectively only when evidence establishes the intended current state.
7. Preserve historical accepted/failed evidence.
8. Re-read the reconciled state and verify physical/version identity when material.
