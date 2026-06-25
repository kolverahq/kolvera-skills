---
name: prospect-sort
description: Sort newly enriched or scraped contacts into prospects (decision-makers to sell to), candidates (people to place — recruitment), and skip (irrelevant). Links sorted contacts to the correct ICP, Reverse Market Profile (RMP), or hot list profiles. Trigger when the user says "sort my contacts", "sort new contacts", "classify contacts", "triage my contacts", or any variation. Maps to MCP Prompt Guide Phase 7.
---

# Prospect Sort

Classify newly arrived contacts — from batch enrichment, Chrome extension scrapes, or manual imports — into actionable categories before outreach.

**Credit cost:** Free (sorting only).

## Consultative approach

Claude should not just silently sort — it should explain why each contact was classified the way it was, flag ambiguous cases for the user to decide, and suggest improvements to the scraping or enrichment strategy based on what came back. Also read GUIDELINES.md in this repo for the full consultative behaviour pattern.

## Step 1 — Pull new contacts

→ `search_contacts` sorted by created date to pull the most recent batch
→ Ask the user how many to process, or default to the last 50

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
→ Individual contributors (Account Executives, SDRs — not buyers)
→ Scraping artefacts (junk data like "Join [Company]", "Latest News")
→ HR/TA titles (facilitators, not decision-makers for most sales)

Present the sorted list to the user with contact IDs and reasoning.

## Step 3 — Link contacts

**Prospects:**
→ `link_prospect_to_icp` to attach to the target ICP
→ Or `add_to_hot_list` to place directly into a campaign-ready list

**Candidates (recruitment):**
→ `bulk_link_candidates_to_reverse_market_profile` — takes a links list where each item is `{contact_id, reverse_market_profile_id}`. Cap 200 per call — keep batches ≤100 as 200 can time out.
→ Check `list_reverse_market_profiles` first. If no RMP exists for the role family, `create_reverse_market_profile` with `linked_icp_id`.
→ Use desk-prefix naming (e.g. "Perm — Implementation Consultant")

**Skip:**
→ No action needed. Optionally note why they were skipped for the user's reference.
→ Delete obvious junk data: `delete_contact` on scraping artefacts.

## Step 4 — Update candidate records (recruitment)

For candidates, capture key details:
→ `update_contact` with candidate_stage, candidate_grade (A/B/C), candidate_notes, salary zone, notice period, work rights

Valid `candidate_stage` values: `role_defined`, `target_companies_mapped`, `candidates_sourced`, `shortlisted`, `connection_sent`, `accepted`, `first_message_sent`, `reply_received`, `qualified_in_chat`, `call_requested`, `call_booked`, `call_completed`, `active`, `nurture`, `closed_rejected`
Valid `outreach_stage` (prospects) values: `identified`, `enrolled`, `emailed`, `opened`, `replied`, `bounced`, `connection_sent`, `accepted`, `follow_up`, `meeting_ask`, `meeting_booked`, `soft_close`, `won`, `lost`

**Important:** Three separate notes fields exist: `notes` (general), `candidate_notes`, `prospect_notes`. Do not mix them.

## Known issues

→ Chrome extension can create duplicate company entities. Always `search_companies` before creating.
→ Broad company-page scrapes have a 6-17% relevant-title hit rate. Title-specific LinkedIn searches yield 60-70%.
