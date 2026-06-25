---
name: contact-enrichment
description: Turn a company list into a verified contact list using Kolvera enrichment. Batch find contacts, fill missing emails, verify addresses, optional phone enrichment. Includes polling patterns and gap-filling workflows. Trigger when the user says "enrich contacts", "find contacts", "find emails", "enrich my ICP", "get decision-makers", or any variation of contact enrichment. Maps to MCP Prompt Guide Phase 6.
---

# Contact Enrichment

Turn a list of target companies into a list of verified decision-maker contacts with emails and (optionally) phone numbers.

**Credit cost:** 2 credits per contact found with a verified email. Phone: 6 credits fresh direct dial, 2 credits company line, 0 for lines already on file.

## Consultative approach

Before enriching, Claude should confirm the targeting with the user — wrong titles waste credits. After enrichment, Claude should review results, flag title mismatches, and suggest alternative sourcing paths for gap companies. Also read GUIDELINES.md in this repo for the full consultative behaviour pattern.

## Step 1 — Confirm targeting before spending credits

**Ask the user:**
→ "For these companies, who's the right person to reach? Based on your ICP, I'll be looking for [titles]. Should I also look for [additional titles], or does that go too wide?"
→ "Companies under 50 employees rarely have a dedicated [title]. For the smaller ones, should I look for the CEO/Founder instead?"
→ "We're about to enrich [N] companies. At 2 credits per contact found, this could cost [estimated range] credits. Your current balance is [balance]. Want to proceed with all [N], or start with the top [subset]?"

## Step 2 — Batch find contacts

→ `batch_find_contacts` with up to 20 company IDs, linked to the ICP via `icp_id`
→ Start with companies that have 50+ employees for best coverage (smaller companies often return zero)
→ Poll `get_enrichment_job(job_key)` every 15-30 seconds
→ Large batches (20 companies) take 8-12 minutes

**If a batch stalls:** Retry in batches of 10.

**For small companies with zero results:** `create_contact` manually with known details, then `find_contact_email` to enrich.

## Step 3 — Fill missing emails

Find the gaps first:
→ `search_contacts` with `email_status` filter: pull `invalid`, `unverified`, and `unknown` contacts

Fill them:
→ `bulk_find_emails` for batch processing (async — poll `get_bulk_enrichment_status` after 60 seconds)
→ `find_contact_email` for individual contacts
→ `verify_contact_email` on unverified addresses

**Email status triage:**

| Status | Action |
|--------|--------|
| Valid work email | Ready for campaign enrollment |
| Catch-all work email | Usable for campaigns, monitor bounces |
| Personal email only (Gmail, Outlook) | Do NOT enrol in email campaigns. LinkedIn outreach only. |
| No email found | LinkedIn outreach only |
| Invalid / bounced | Find alternative contact at the company |

## Step 4 — Phone enrichment (optional)

Use selectively on high-value targets:
→ `bulk_find_phones` for batch processing
→ `find_contact_phone` for individual contacts
→ Poll `get_bulk_enrichment_status` after 60 seconds

## Step 5 — Report and suggest next steps

Show the user:
→ Total contacts found
→ Breakdown by email status (valid, catch-all, personal-only, no email)
→ Companies with zero usable contacts (gap list)
→ Credit spend

**Offer insights and suggestions:**
→ "Enrichment found mostly [title types]. I'd flag that [N] of these are individual contributors, not decision-makers. Kolvera enrichment often returns ICs — I'd filter those out. Does [filtered list] look right?"
→ "These [N] companies returned zero contacts. For companies this small, Kolvera enrichment often comes up empty. I'd suggest creating contacts manually from LinkedIn for your top priorities, then running `find_contact_email` on each."
→ "Your email hit rate was [X]%. For the [N] contacts without emails, a LinkedIn Sales Nav scrape with the Chrome extension would be the fastest path. Should I build the search parameters for you?"
→ "You now have [N] campaign-ready contacts with valid emails. Should I help build hot lists and segment them for outreach?"

## Known issues

→ `get_bulk_enrichment_status` can return "idle" prematurely. Verify directly via `get_contact`.
→ `find_company_contacts` with `icp_id` may error if the website scraper returns zero results. Workaround: omit `icp_id`, then link prospects afterwards.
→ `batch_find_contacts` job key deduplication within session — only one job runs per session. Run in a fresh chat for new results.
→ Enrichment often returns individual contributors rather than hiring decision-makers. Always audit titles after enrichment.
