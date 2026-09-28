# Structured Research State Protocol

Version 1.0 — used by purchase-research 1.3.x.

## Goal
Make a purchase study portable across ChatGPT, Gemini, Hermes and future hosts without relying on conversation history.

## Files
A portable research bundle may contain:
- `session.json` — stage, pointers, blockers, next actions and skill versions.
- `requirements.json` — durable requirements for this purchase.
- `products.json` — candidates/finalists and constraint results.
- `evidence.json` — decision-critical claims with evidence states and source metadata.
- `configurations.json` — complete systems and costs.
- optional `report.md` or generated PDF.

Validate conceptually against the schemas in repository `schemas/`.

## Lifecycle

Stages:
DISCOVERY → REQUIREMENTS → MARKET_SCAN → SHORTLIST → DEEP_AUDIT → VALIDATION → DECISION → REPORT.

Optional:
WATCH — monitor selected finalists after research.
LEARNING — extract durable domain methodology after the purchase study.

A session may move backward when requirements change.

## Update rules
Update the structured state when:
- a requirement becomes clear or changes priority;
- a candidate is added/eliminated;
- a critical claim is verified or contradicted;
- a hard constraint changes PASS/FAIL/UNRESOLVED;
- a system configuration or price changes;
- a blocker is resolved;
- the study changes stage.

Do not record every conversational sentence.

## Freshness
Portable state is evidence, not eternal truth.

On resume:
- preserve user requirements unless the user changes them;
- preserve historical evidence and its observation date;
- re-check current price, stock, promotions, current product generation, warranty, regulation, incentives and other time-sensitive facts before using them as current;
- never silently rewrite historical observations.

## Cross-platform resume
When a bundle is supplied:
1. read `session.json`;
2. inspect requirements and blockers;
3. verify referenced skill versions;
4. identify stale/time-sensitive evidence;
5. summarize the restored state to the user;
6. continue from `next_actions` rather than restarting discovery.

## Privacy
Do not place secrets, account identifiers, exact private addresses, health data or other unnecessary sensitive personal information in portable state. Store only constraints needed for the purchasing decision.

## IDs
Use stable, human-readable IDs where possible:
- requirement: `req-car-transport`
- product: `garrett-miller-z-2026`
- evidence: `ev-gmz-payload-001`
- configuration: `cfg-gmz-vacation`

## Export
If the host supports files, offer a ZIP or directory containing the structured bundle after a substantial study or when the user asks to continue elsewhere.
