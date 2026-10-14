---
name: prospect-sort
description: Classify a reviewed Kolvera contact batch as buyers, candidates or irrelevant; link the correct desk, pool or hot list.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Prospect Sort

Classify newly arrived contacts — from batch enrichment, Chrome extension scrapes, or manual imports — into actionable categories before outreach.

**Credit cost:** Free (sorting only).

## Consultative approach

The assistant should not just silently sort — it should explain why each contact was classified the way it was, flag ambiguous cases for the user to decide, and suggest improvements to the scraping or enrichment strategy based on what came back. Read the bundled [Operations contract](references/operations.md) for budgets, job receipts and action authority.

## Step 1 — Pull new contacts

→ `search_contacts` sorted by created date to pull the most recent batch
Bound intake using supported provenance/filtering. Newest 50 records are a proposed selection, not proof of a common import or owner.

## Step 2 — Classify each contact

Sort into three buckets based on title and role:

**PROSPECT** — Decision-makers to sell to or pitch to
→ Titles like: Head of Sales, VP Operations, CEO/Founder (at small companies), COO, Head of CS, Head of Delivery
→ These are buyers. They go into campaigns.

**CANDIDATE** — People who could be placed (recruitment users only)
→ Titles that match roles the user recruits for
→ These go into Reverse Market Profile (RMP) profiles

**SKIP** — Irrelevant
→ Wrong function (e.g. CTO when selling a non-technical service)
An individual contributor may be a candidate, influencer or buyer depending on the brief; classify by actual purpose.
→ Scraping artefacts (junk data like "Join [Company]", "Latest News")
Judge HR/TA and technical leaders against this desk's actual buying/hiring structure; none is universally irrelevant.

Present the sorted list to the user with contact IDs and reasoning.

## Step 3 — Link contacts

**Prospects:**
→ `link_prospect_to_icp` to attach to the target ICP
→ Or `add_to_hot_list` to place directly into a campaign-ready list

**Candidates (recruitment):**
→ `bulk_link_candidates_to_reverse_market_profile` — takes a links list where each item is `{contact_id, reverse_market_profile_id}`. Cap 200 per call — keep batches ≤100 as 200 can time out.
Check `list_reverse_market_profiles` first. If no suitable profile exists, request the supported app creation step; current MCP does not expose initial creation. Verify the resulting profile/desk before linking.
→ Use desk-prefix naming (e.g. "Perm — Implementation Consultant")

**Skip:**
→ No action needed. Optionally note why they were skipped for the user's reference.
→ Only with explicit delete authority, delete verified junk data: `delete_contact` on scraping artefacts.

## Step 4 — Update candidate records (recruitment)

For candidates, capture key details:
→ `update_contact` with candidate_stage, candidate_grade (A/B/C), candidate_notes, salary zone, notice period, work rights

Valid `candidate_stage` values: `role_defined`, `target_companies_mapped`, `candidates_sourced`, `shortlisted`, `connection_sent`, `accepted`, `first_message_sent`, `reply_received`, `qualified_in_chat`, `call_requested`, `call_booked`, `call_completed`, `active`, `nurture`, `closed_rejected`
Valid `outreach_stage` (prospects) values: `identified`, `enrolled`, `emailed`, `opened`, `replied`, `bounced`, `connection_sent`, `accepted`, `follow_up`, `meeting_ask`, `meeting_booked`, `soft_close`, `won`, `lost`

**Important:** Three separate notes fields exist: `notes` (general), `candidate_notes`, `prospect_notes`. Do not mix them.

## Known issues

→ Chrome extension can create duplicate company entities. Always `search_companies` before creating.
→ Broad company-page scrapes have a 6-17% relevant-title hit rate. Title-specific LinkedIn searches yield 60-70%.
