# Watch Engine

Version 1.0 — used by purchase-research 1.4.x.

## Purpose
Continue a mature purchase study without rerunning discovery. Watch only finalists that still satisfy, or may satisfy once a blocker is resolved, the active requirements.

## Entry gate
Enter WATCH only when:
- requirements are sufficiently stable;
- shortlist/finalists exist;
- hard-constraint status is known or explicit blockers exist;
- the user wants ongoing monitoring or delayed purchase.

## What to monitor
Material events only:
- verified price crossing a threshold;
- meaningful price drop from the recorded baseline;
- stock becoming available;
- a relevant promotion with conditions;
- new product generation that may supersede a finalist;
- manufacturer reply resolving a blocking unknown;
- warranty/SAV terms changing materially;
- subsidy/eligibility changing;
- seller quality changing;
- specification revision affecting a hard constraint.

Do not broaden into generic news monitoring.

## Baseline
Store the observed price/date/seller and current decision status. A crossed-out MSRP is not sufficient evidence of a real historical price.

## Materiality
A notification is material if it can plausibly change:
- selected product;
- timing of purchase;
- complete-system cost;
- PASS/FAIL/UNRESOLVED status;
- confidence in warranty/SAV;
- eligibility for an incentive.

Ignore cosmetic page changes, tiny fluctuations below the user's threshold, repeated identical promotions and unrelated brand news.

## Revalidation
Every watch run must re-check the relevant source. Never infer current stock or price from an old snapshot.

## New generation
Do not automatically replace a finalist. Audit the new generation against mandatory requirements and system cost first.

## Promotion
Record:
- seller;
- actual checkout price if verifiable;
- code;
- expiry if published;
- shipping/mandatory bundle;
- marketplace seller identity.
A promotion from an unsuitable seller can be ignored if seller/SAV is part of the requirements.

## Blocker resolution
When a manufacturer reply or new manual resolves a blocker:
1. update evidence state;
2. recompute hard constraint;
3. recompute affected configurations;
4. notify only if decision impact is material.

## History
Append meaningful snapshots/events; do not overwrite history. Deduplicate repeated observations.

## Notifications
Default: only material changes; no “still unchanged” notifications unless explicitly requested.

## Platform scheduling
This skill defines what to watch, not how a host schedules jobs.
- If the host has a scheduler/automation tool, create monitoring only after user asks/approves.
- Otherwise produce the watch specification for an external scheduler.
