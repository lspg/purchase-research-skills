---
name: purchase-research
description: Structured pre-purchase research: discover real requirements, ask discriminating questions, research the market, audit finalists, compare total cost/SAV and produce a decision brief. Use when the user is considering buying or comparing a product.
version: 1.5.0
author: Loïs Puig
license: MIT
metadata:
  hermes:
    tags: [shopping, research, comparison, buying-guide, decision-support]
    category: research
---

# Purchase Research

Use this skill for structured pre-purchase decision support.

## Safety boundary

This is a research/information skill. It must NOT install packages, modify the OS, change network/devops configuration, create other skills, or execute administrative/system changes merely to complete product research. Use existing web/research/file tools only. If an environment change would be useful, explain it and wait for explicit authorization under the user's normal Hermes security policy.

## Procedure
1. Identify category and actual goal.
2. Load `references/category-question-bank.md` as needed.
3. Ask only 2-5 discriminating questions.
4. Maintain Obligatory / Important / Desirable / Out-of-scope requirements.
5. Research multiple solution families.
6. Load `references/source-policy.md`; narrow to 3-6 finalists.
7. Load `references/evidence-engine.md`, then audit finalists using `references/audit-framework.md`. Track hard constraints as PASS / FAIL / UNRESOLVED and critical facts by evidence state.
8. Verify current price, availability, warranty, service, parts and accessories.
9. Compare complete-system and ownership cost when relevant.
10. Use separate scenarios when different uses produce different optima.
11. Mark critical undocumented facts `TO CONFIRM`.
12. If manufacturer clarification is needed, draft identical questions for competing products.
13. Produce the final brief using `references/report-template.md`.

## Specialized skills
If a matching specialized research skill exists, load it and combine its domain rules with this workflow. Do not silently create or update skills. Propose specialization only after the research is complete and only with explicit user approval.

## Updates
When update checking is requested or skill maintenance begins, load `references/update-policy.md` and compare this version to the public stable manifest. Never self-update silently; require explicit authorization before replacing local skill files.

## Portable research state
For substantial research, cross-session continuation or handoff, load `references/state-protocol.md`. Prefer a structured bundle over reconstructing state from chat history. Revalidate time-sensitive market facts when resuming.

## Watch mode
When a mature research session enters WATCH, load `references/watch-engine.md`. Monitor only configured finalists/material events. Never create recurring monitoring without explicit user authorization. Use the host scheduler if available; the skill itself does not bypass scheduling or security controls.

## Build contract
This distribution is generated from the canonical skill. Do not treat local distribution edits as upstream source changes.
