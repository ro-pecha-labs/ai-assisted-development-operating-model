# Operating Model Release Policy

**Status:** PROSPECTIVE POLICY FOR OM 2.1 DEVELOPMENT

OM release qualification is proportional to the semantic impact of the Operating Model change.

## PATCH

Typical scope:

- typo/editorial correction;
- stale status/coherence correction;
- template pin correction;
- validator/tooling bug that does not change normative behavior.

Minimum:

- protected PR;
- structural CI;
- targeted regression for the defect class;
- immutable release identity;
- explicit prospective adoption when the patch is to become canonical.

A formal RC is not mandatory unless the patch changes a qualified claim or has material cross-profile risk.

## MINOR

Typical scope:

- backward-compatible profile capability;
- new optional project field;
- new triggered playbook;
- backward-compatible release/assurance mode.

Minimum before candidate freeze:

- structural validation;
- affected-profile regression;
- all-profile compatibility/cross-profile qualification;
- recovery regression;
- negative controls for new semantics;
- representative real-project or shadow pilot where behavior materially affects recovery, assurance or lifecycle.

A MINOR release uses an immutable RC candidate before GA.

## MAJOR

Typical scope:

- breaking universal contract/schema semantics;
- removal or redefinition of a primary profile;
- breaking authority model;
- incompatible migration/recovery model.

Minimum:

- full cross-profile qualification;
- explicit migration qualification;
- representative pilots;
- immutable candidate/RC lineage;
- formal release acceptance and prospective canonical adoption.

## Historical integrity

A later release never rewrites the meaning of evidence produced under an earlier effective OM version.
