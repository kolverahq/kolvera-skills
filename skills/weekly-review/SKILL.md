---
name: weekly-review
description: End-of-week synthesis. Reviews the week's pipeline activity, campaign performance, hot leads, and sets priorities for next week. Trigger when the user says "weekly review", "week in review", "Friday review", "what happened this week", "weekly synthesis", or any variation.
---

# Weekly Review

A structured end-of-week review. What happened, what moved, what needs attention next week.

**Credit cost:** Free.

## Section 1 — Campaign performance (this week)

→ `list_campaigns` — all active campaigns
→ `get_campaign_stats` for each — this week's numbers:
  - Total sent, opened, replied, bounced
  - Open rate and reply rate trends (improving or declining?)
  - Best-performing campaign and worst-performing campaign
  - Any campaigns that should be paused, expanded, or refreshed

## Section 2 — Pipeline activity

→ `search_pipeline_jobs` — new jobs posted this week matching the ICP
→ Count: how many new pipeline matches vs last week?
→ Any shortlisted jobs that need follow-up?
→ Any companies that appeared across multiple job boards (high-intent signal)?

## Section 3 — Contact and prospect movement

→ New contacts added this week (from enrichment, scraping, manual)
→ Prospects that moved stages (identified → replied → meeting booked)
→ Candidates that moved stages (if applicable)
→ Hot list changes: any S-tier prospects added?

## Section 4 — Hot leads

→ Prospects who replied positively this week
→ Prospects with active hiring signals who have not been contacted
→ Candidates with competing processes or deadlines next week
→ Any warm referrals received

## Section 5 — ICP and market health

→ `get_icp_profile` — current company count and prospect count
→ Any ICPs that need refreshing (stale research, outdated scrape configs)?
→ Credit balance: `get_credit_balance`
→ Scrape allowance usage

## Section 6 — Next week's priorities

Based on everything above, recommend:
→ Top 3 actions for Monday
→ Any campaigns to adjust
→ Any prospects to follow up with
→ Any sourcing or enrichment work to queue

Keep the output structured and actionable. No fluff.
