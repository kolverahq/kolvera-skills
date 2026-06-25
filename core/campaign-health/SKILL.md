---
name: campaign-health
description: Daily campaign and inbox health check. Flags bounce spikes, low open rates, dead campaigns, inbox health issues, and capacity problems. Trigger when the user says "check my campaigns", "campaign health", "how are my campaigns doing", "inbox health", or any variation. Run daily or on-demand.
---

# Campaign Health Check

Quick diagnostic across all active campaigns and connected inboxes. Flags problems that need action.

**Credit cost:** Free.

## Step 1 — Pull active campaigns

→ `list_campaigns` to get all campaigns
→ Filter for active campaigns (status = active)

## Step 2 — Check campaign stats

For each active campaign:
→ `get_campaign_stats` — pull sent, opened, replied, bounced counts

**Flag thresholds:**

| Metric | Healthy | Warning | Action needed |
|--------|---------|---------|---------------|
| Bounce rate | Below 2% | 2-5% | Above 5% — pause and review inbox/list quality |
| Open rate | Above 40% | 20-40% | Below 20% after 10+ sends — subject line or deliverability issue |
| Reply rate | Above 3% | 1-3% | Below 1% after 20+ sends — copy or targeting issue |

→ Check for campaigns with zero sends in the last 48 hours (may be stuck)
→ Check for campaigns with stop-on-reply contacts that need manual follow-up

## Step 3 — Check inbox health

→ `list_inboxes` — review each inbox:
  - `is_active`: should be true for inboxes assigned to campaigns
  - `health_state`: should be `ok`. If `paused`, flag immediately.
  - `sends_today` vs `daily_limit`: check remaining capacity
  - `current_daily_limit`: ramp-up-adjusted limit may be lower than the set daily_limit during warmup

**Flag:**
→ Any inbox with `health_state: paused`
→ Any inbox at or near daily capacity
→ Any inbox not assigned to any campaign (orphaned)

## Step 4 — Report

Present a summary:
→ Campaigns performing well (green)
→ Campaigns with warnings (amber) — note the issue and suggested action
→ Campaigns needing immediate action (red) — note the issue and recommended fix
→ Inbox health summary
→ Total sends today across all inboxes

Keep it scannable. The user should be able to act on this in under 2 minutes.
