# Playbook — Adoption and Migration

**Status:** NON-CANONICAL DEVELOPMENT  
**Trigger:** a project or the Operating Model itself is proposed to change governance version, authority model or control plane.

1. Identify the last trusted pre-adoption boundary.
2. Define the prospective effective ref/commit/time boundary.
3. Preserve all pre-boundary accepted/failed evidence under the governance effective when it was created.
4. Qualify the new control plane and required enforcement before making it authoritative.
5. Migrate only current state needed for future operation; do not mass-rewrite historical artifacts for cosmetic consistency.
6. Declare external sources that remain authoritative outside the new control plane.
7. Verify recovery from the new bootstrap before adoption.
8. Record the explicit adoption decision and exact immutable OM/project revision.
9. Rollback, if needed, is another prospective boundary rather than erasure of the adoption event.
