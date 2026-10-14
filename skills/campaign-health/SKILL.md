---
name: campaign-health
description: Review Kolvera campaign totals, inbox capacity and delivery evidence; recommend authorised fixes without inventing time-window metrics.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Campaign Health

Read [Operations contract](references/operations.md). This is a diagnostic by default; pausing, resuming, changing limits or sending needs user scope covering that action.

1. Use `list_campaigns` and inspect relevant active campaigns. Read `get_campaign_stats` and per-variant figures for ab/abc campaigns.
2. Label these as lifetime campaign totals. A 48-hour stall or recent reply trend requires timestamped activity, schedule evidence or a validated earlier snapshot. If unavailable, state that the period cannot be assessed.
3. Check enrolled/contacted/sent denominators, bounces, genuine replies, suppression and queue state. Account for machine opens and disabled tracking; low opens alone do not prove poor subject lines or deliverability. Small samples are inconclusive. Apply the customer's/provider's current bounce policy rather than universal tiny-sample thresholds.
4. Use `list_inboxes`: active state, health_state, remaining capacity and warmup-adjusted current_daily_limit. Read errors/reasons before inferring the campaign is stuck; working hours, weekends, recipient state and limits can explain no sends.
5. Report healthy/warning/action-needed with evidence and uncertainty. Propose bounded fixes such as reviewing source quality, repairing inbox configuration or holding a campaign. Do not resume a paused campaign just to add contacts.
6. After an authorised change, read back the state. Track a later check as pending; an activation flag is not proof that messages were delivered.
