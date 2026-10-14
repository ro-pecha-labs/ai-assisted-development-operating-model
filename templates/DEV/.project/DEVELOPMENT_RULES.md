# <Project name> — Development Rules

Classification: <organization classification, if applicable>

Authority: `PROJECT.yaml` -> `ACTIVE_STATE.yaml` -> this file.
This file specializes the adopted OM release. It does not repeat OM rules. On conflict, OM invariants win, and a Common Rule wins unless an exception below says otherwise.

## Adopted common rules

OM release: the release pinned in `PROJECT.yaml` (`governance.operating_model`; `ref` and `commit` are recorded there only and not repeated here). The Common Rules of that release (`COMMON_RULES.md`) apply in full, except for the exceptions below.

## Organization rules

<Locator and pinned revision of the organization layer, or "none".>

## Exceptions

Each exception names the Common Rule, the reason, and the scope. An exception shall not touch an OM invariant.

| Rule | Reason | Scope |
|---|---|---|
| <e.g. D1> | <reason> | <scope> |

## Project-specific rules

1. <Rule that exists only for this project: data sources, local environment, naming, tools.>
