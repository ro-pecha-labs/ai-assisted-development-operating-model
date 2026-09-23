# Materiality Decision Guide

**Status:** PROSPECTIVE GUIDANCE FOR OM 2.1 DEVELOPMENT

Materiality remains a governed judgment because one universal numeric threshold would over-govern some profiles and under-govern others.

A change or event is presumptively material when it can change one or more of:

- accepted or trusted identity;
- authority or source-of-truth boundary;
- public or downstream consumer contract;
- security, safety or authorization posture;
- external mutation semantics or target;
- destructive or production scope;
- reproducibility of an accepted claim;
- release/adoption claim;
- interpretation of historical accepted/failed evidence;
- required human approval;
- a protected validation surface such as schema, golden fixture or CI gate.

A change is presumptively non-material when it is demonstrably presentation-only, editorial, generated-view refresh or equivalent and cannot alter the governed semantics above.

When classification is uncertain, choose the least expensive discriminating review/test that can establish whether a material boundary is affected. Do not default automatically to the heaviest lifecycle.
