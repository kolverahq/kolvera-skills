---
name: weekly-review
description: Summarise Kolvera pipeline and campaign evidence with explicit period coverage, lifetime totals and next-week actions.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Weekly Review

Read [Operations contract](references/operations.md). Confirm week boundaries and timezone; read-only review does not authorise campaign changes or sending.

## Campaigns
Use `list_campaigns` and `get_campaign_stats`, including variant breakdown where relevant. These are lifetime totals, not date-filtered weekly figures.
Use supported timestamped activity or validated prior snapshots for period counts/deltas. Explain missing coverage, changed definitions and denominator differences. If no period evidence exists, report current totals and explicitly say weekly change is unavailable.
Consider actual replies, bounces and inbox capacity. Machine opens, privacy tools, disabled tracking and small samples limit open-rate conclusions.

## Pipeline and people
Use `search_pipeline_jobs` with supported desk/date filters. Clarify created/imported date versus source posting date; do not count them interchangeably.
Use supported contact/client-job/shortlist/history tools to show dated movement and next actions. Do not infer stage changes from current state alone or claim last week's comparison without a retained baseline.
Read `get_icp_profile` for current desk counts and `get_credit_balance` for balance. Balance change is not weekly spend without transaction evidence (resets, top-ups and refunds can change it).

## Output
- Week/timezone and sources covered.
- Verified weekly activity; separately labelled lifetime/current totals.
- Warm replies, overdue actions and candidate/client decisions needing attention.
- Evidence gaps and unresolved jobs.
- Three concrete priorities for next week, with owner/date where known.

Recommend changes; execute only those already authorised. Preserve suppression and privacy when sharing the review.
