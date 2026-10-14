---
name: deal-pipeline
description: Review Kolvera sales prospects, client relationships and supported activity evidence; update authorised stages and next actions.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Deal Pipeline

Read [Operations contract](references/operations.md) before acting.

Review the sales pipeline, flag stale opportunities, and surface the next best actions.

**Credit cost:** Free.

## Prospect stages

`outreach_stage` (set via `update_contact`) is validated against this vocab — an unknown value is rejected:

`identified` → `enrolled` → `emailed` → `opened` → `replied` → `bounced` → `connection_sent` → `accepted` → `follow_up` → `meeting_ask` → `meeting_booked` → `soft_close` → `won` → `lost`

## Step 1 — Pull the pipeline

→ `list_icp_prospects` on the target ICP to see all prospects
→ Or `search_contacts` with `is_prospect=true` for a filtered view
→ Group by outreach_stage

## Step 2 — Identify stale prospects

Flag prospects that have not moved stages within expected timeframes:

→ **Identified for 7+ days** with no outreach sent — need to be enrolled in a campaign or contacted
→ **Replied 3+ days ago** with no follow-up — need immediate action
→ **Meeting booked 5+ days ago** with no update — confirm meeting happened, update stage
→ **Lost** — review reason. Anything worth re-engaging in 30-60 days?

Check `prospect_next_action_date` on each contact. Flag any overdue. Stage-age claims require dated stage evidence; updated_at is not proof when a stage changed. Mark unknown age explicitly.

## Step 3 — Review active campaigns

→ `list_campaigns` — which campaigns are running against this ICP?
→ `get_campaign_stats` — performance metrics
→ `get_campaign_enrollments` — who is at which step? Anyone completing the sequence with no reply?

Prospects completing the full sequence with no engagement may need:
→ A different channel (LinkedIn, phone)
→ A different message angle
→ To be moved to a nurture list

## Step 4 — Company-level view

→ `search_companies` with `is_client=true` to see active client relationships
→ `get_company` for full details: client tier, fee terms, payment terms, buying triggers, BD recency
→ Flag companies with no recent BD activity (stale client relationships)

## Step 5 — Recommend actions

Present a prioritised action list:
→ Prospects needing immediate follow-up (replied, meeting booked)
→ Stale prospects to re-engage or archive
→ Campaigns to adjust (poor performance)
→ Companies to research or re-approach
→ New prospects to add from recent pipeline matches

## Updating records

→ `update_contact` with `outreach_stage`, `prospect_notes`, `prospect_next_action`, `prospect_next_action_date`
→ `update_company` for client CRM fields (buying triggers, BD timestamps)
→ Use `prospect_notes` (not `notes` or `candidate_notes`) for sales-specific observations
