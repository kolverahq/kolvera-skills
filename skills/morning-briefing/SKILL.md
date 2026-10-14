---
name: morning-briefing
description: Read Kolvera's daily brief, review supported meeting and follow-up evidence, and prioritise the day.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Morning Briefing

Read [Operations contract](references/operations.md) before acting.

A scannable daily digest. Everything the user needs to know before the day starts.

**Credit cost:** Free.

## Fastest path — `get_morning_brief`

Lead with the purpose-built tool. `get_morning_brief` (param `force_refresh`) returns today's prioritised digest in one call — calendar/day, the replies and people that need a response, follow-ups due, pipeline movement, campaign flags, and tracked ICPs/RMPs — as both markdown and a structured payload. Set `force_refresh=true` to recompose from the latest data.

Use this first. The manual tools below are a fallback or supplement — pull them only to fill a gap the brief doesn't cover (e.g. deeper campaign-health drill-down or a specific calendar the brief didn't surface).

## What to pull (manual fallback / supplement)

### 1. Today's calendar
→ Use the calendar tool (if connected) to pull today's events
→ Deduplicate across calendars
→ Flag any meetings that need prep (new prospect, candidate call)

### 2. Campaign activity (last 24 hours)
→ `list_campaigns` — filter for active campaigns
`get_campaign_stats` gives lifetime totals. For replies since yesterday use supported timestamped activity or a validated prior snapshot; otherwise label period coverage unavailable.
→ Flag any replies that need immediate response
→ Flag any bounce spikes or health issues (run the campaign-health checks)

### 3. Pipeline activity
→ `search_pipeline_jobs` — any new jobs posted matching the ICP since yesterday?
→ Flag high-priority new listings (exact role match, high-intent company)

### 4. Follow-ups due today
→ Get follow-ups from `get_morning_brief` — it returns the due/overdue next-actions directly. (Note: `search_contacts` has NO next-action or date filter, so it cannot surface follow-ups by date.)
→ `list_meetings` — any meetings with follow-up tasks due
→ Flag overdue follow-ups from previous days

### 5. Upcoming deadlines
→ Candidates with competing processes or notice period deadlines
→ Campaign enrolments completing their sequence (last step sent)
→ Scrape configs due for a re-run

## Output format

Keep it short and scannable. Structure as:

**Today's Meetings** (count)
→ [Time] — [Meeting] with [Who]

**Replies Needing Action** (count)
→ [Contact] at [Company] replied to [Campaign] — [summary]

**Follow-ups Due** (count)
→ [Contact] — [Action needed]

**Pipeline Alerts** (count)
→ [New job] at [Company] — [relevance]

**Campaign Health**
→ All green / [Specific issues]

**Priority Actions** (top 3)
→ 1. [Most urgent thing]
→ 2. [Second most urgent]
→ 3. [Third]
