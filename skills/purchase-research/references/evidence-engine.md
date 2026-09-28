# Evidence & Decision Engine

## Evidence states

Every decision-critical claim should carry one state:

- **CONFIRMED** — established by an authoritative primary source such as a manual, certificate, regulation or explicit manufacturer specification.
- **CORROBORATED** — supported by a primary source and at least one suitable independent source.
- **CLAIMED** — stated by manufacturer/seller marketing but definition, method or independent verification is insufficient.
- **CONFLICTING** — credible sources disagree.
- **UNKNOWN** — not documented or not found.

Do not silently upgrade CLAIMED to CONFIRMED.

## Hard constraints

A requirement marked Obligatory is a hard constraint.

For each candidate:
- PASS: explicitly satisfies it.
- FAIL: explicitly violates it; candidate is eliminated for that scenario.
- UNRESOLVED: evidence is insufficient; candidate remains provisional and cannot be declared the final choice if the unresolved fact could cause FAIL.

A strong price, review score or feature set cannot compensate for FAIL on a hard constraint.

## Evidence record

For important facts track conceptually:
- claim
- value
- evidence_state
- source_type
- source/date
- variant/SKU
- notes
- decision_impact

## System cost

Separate:
1. product price;
2. mandatory accessories;
3. installation/infrastructure;
4. recommended usage accessories;
5. recurring subscriptions/consumables;
6. likely maintenance;
7. incentives only when eligibility is established.

Compare configurations that satisfy the requirement, not bare products.

## Decision gate

Before a final recommendation:
- all hard constraints must be PASS, or unresolved constraints must be clearly presented as blockers;
- current price must be dated;
- product variant must be unambiguous;
- critical compatibility must be evidenced;
- important conflicting claims must be disclosed.

## New information

When a requirement changes, recompute the affected PASS/FAIL/UNRESOLVED decisions before preserving any prior ranking.
