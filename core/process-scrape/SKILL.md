---
name: process-scrape
description: Process contacts scraped from LinkedIn via the Kolvera Chrome extension. Handles both prospect scrapes (decision-makers to sell to) and candidate scrapes (people to place — recruitment). Deduplicates, classifies by title, finds emails, builds hot lists, and creates a prioritised action queue. Trigger when the user says "process my scrape", "I just scraped [number] contacts", "process today's scrape", "sort my LinkedIn scrape", "I scraped some prospects", "I scraped some candidates", or any variation of processing contacts pulled from LinkedIn. Maps to MCP Prompt Guide Phases 7 and 10.
---

# Process Scrape

Process contacts that just landed in Kolvera from a LinkedIn Sales Navigator scrape via the Chrome extension. Deduplicates, classifies, enriches emails, and routes contacts into the right hot lists and profiles — ready for outreach.

**Two modes:** Ask the user whether this is a prospect scrape (decision-makers to sell to) or a candidate scrape (people to place). The workflow branches accordingly.

**Credit cost:** 2 credits per contact where a verified email is found. Everything else is free.

## Consultative approach

This is not just a sorting machine. At every step, Claude should:
→ Review the data and share observations about what came back
→ Flag patterns the user might not notice (title clusters, company overlaps, data quality issues)
→ Suggest improvements to the scrape strategy for next time
→ Ask questions where classification is ambiguous
→ Never auto-delete or auto-enrol without confirmation

Also read GUIDELINES.md in this repo for the full consultative behaviour pattern.

---

## Step 1 — Pull today's intake

→ `search_contacts` sorted by created date (most recent first)
→ Ask the user how many they scraped, or pull the last 50-100 by default
→ Show a count: "[X] new contacts found from today's scrape"

**Quick check:** If the count seems low compared to what the user scraped, the Chrome extension may still be processing. Wait a few minutes and re-pull.

## Step 2 — Deduplicate

→ Check each contact against existing records by name + current company
→ Flag duplicates — do not delete without user confirmation
→ Report: "[X] unique contacts, [Y] duplicates flagged"

**Known issue:** The Chrome extension can create duplicate company entities. Run `search_companies` on any new company names to catch these.

## Step 3 — Classify by title

Sort every contact into one of three buckets based on their title:

**For prospect scrapes:**

| Classification | Title examples | Action |
|---------------|---------------|--------|
| **TARGET** | Head of Sales, VP Operations, CEO/Founder, COO, Head of CS, CRO, Managing Director | Keep — these are buyers |
| **SECONDARY** | Sales Manager, Operations Manager, Head of People | Keep if no better contact at the company |
| **SKIP** | Account Executive, SDR, BDR, Coordinator, Assistant, Intern | Remove — individual contributors, not buyers |
| **DELETE** | "Join [Company]", "Latest News", "Platform Add", empty titles | Scraping artefacts — clean up |

**For candidate scrapes:**

| Classification | Title examples (adjust to match the user's target roles) | Action |
|---------------|--------------------------------------------------------|--------|
| **STRONG FIT** | Title matches or is adjacent to the role being sourced | Keep — outreach priority |
| **POSSIBLE FIT** | Related title, needs further screening | Keep — review queue |
| **WRONG FIT** | Unrelated function or seniority | Skip |
| **DELETE** | Scraping artefacts, junk data | Clean up |

Ask the user what role they are sourcing for (if candidate scrape) to calibrate the title filter.

Present the sorted list with counts per bucket and ask for confirmation before proceeding.

**Offer insights on the scrape quality:**
→ "Of [X] contacts scraped, only [Y] are usable targets — that's a [Z]% hit rate. Title-specific Sales Nav searches typically get 60-70%. If your hit rate is under 20%, I'd suggest tightening your Sales Nav filters next time. Here's what I'd change: [specific suggestions]."
→ "I'm seeing [N] contacts from [company] — that seems like a lot from one company. Was this a company-page scrape? If so, switching to a title-filtered search across multiple companies would give you better coverage."
→ "These titles keep showing up but they're not buyers or candidates: [list]. If you add a negative title filter in Sales Nav for these, your next scrape will be cleaner."
→ "I notice [N] contacts don't have a current company listed — the Chrome extension may not have captured it. These will be harder to route. Should I skip them or try to look them up?"

**Flag ambiguous cases:**
→ "I'm not sure about these [N] contacts. [Name] is a '[title]' — that could be a buyer or an IC depending on the company. Should I include them or skip them?"
→ "These contacts have titles that could go either way: [list]. Want me to include them as secondary targets, or keep the list tight?"

## Step 4 — Find emails

Run email enrichment on all contacts classified as TARGET, SECONDARY, or STRONG FIT:

→ `bulk_find_emails` (async — poll `get_bulk_enrichment_status` after 60 seconds)
→ Or `find_contact_email` for smaller batches (under 10 contacts)

**Important:** `get_bulk_enrichment_status` can return "idle" prematurely. Verify results directly via `get_contact` on a sample of contacts.

After enrichment, triage by email status:

| Email status | Route |
|-------------|-------|
| Valid work email | Campaign-ready hot list |
| Catch-all work email | Campaign-ready hot list (monitor bounces) |
| Personal email only (Gmail, Outlook) | LinkedIn-only hot list |
| No email found | LinkedIn-only hot list |
| Invalid / bounced | Try to find alternative contact at the company |

## Step 5 — Route into hot lists and profiles

### Prospect scrape routing

**Before routing, suggest a strategy:**
→ "You have [N] campaign-ready prospects. Should I add them to an existing hot list, or create a new one? If there's an active campaign running, I can enrol directly — but only if the titles align with the campaign's audience."
→ "I'd suggest splitting these into [Segment A] and [Segment B] — they'd need different outreach angles. Or if the audience is tight enough, one list works. What do you think?"

→ **Campaign-ready prospects** (valid/catch-all work email):
  - `add_to_hot_list` to the relevant campaign hot list, or create a new one via `create_hot_list` with `icp_id`
  - Assign tiers: `s` (active hiring signal + strong fit), `a` (strong fit, no signal), `b` (worth reaching)
  - Link to ICP: `link_prospect_to_icp`

→ **LinkedIn-only prospects** (no usable email):
  - `create_hot_list` or add to existing LinkedIn-only hot list
  - These are a manual LinkedIn outreach queue

### Candidate scrape routing

→ **Strong fit candidates:**
  - `bulk_link_candidates_to_reverse_market_profile` to the relevant Reverse Market Profile (RMP) (format: `{contact_id, reverse_market_profile_id}`, cap 200 per call — keep batches ≤100 as 200 can time out)
  - If no RMP exists: `create_reverse_market_profile` with `linked_icp_id` and desk-prefix naming
  - Update contact: `update_contact` with `candidate_stage`, `candidate_grade`, `candidate_notes`

→ **Candidates with valid email:**
  - Build a connect + outreach queue (see Step 6)

→ **Candidates without email:**
  - LinkedIn connection request queue (see Step 6)

## Step 6 — Build the action queue

### For prospects

Present a prioritised list:
→ **Immediate outreach** — S-tier prospects with valid email, already in a campaign hot list. If a campaign is active, enrol directly.
→ **This week** — A-tier prospects with valid email. Queue for next campaign enrollment or manual outreach.
→ **Enrich first** — B-tier or contacts missing email. Run enrichment, then reassess.

### For candidates

Present a ranked list of strong fits:
→ Name, title, current company, why they fit (one line based on title/company match)
→ Email status (ready to email, or LinkedIn-only)
→ Suggested connection note — specific, references their company or role, never generic
→ Cap the daily connect queue at 20-25 to stay within LinkedIn limits

## Step 7 — Summary

Present the final scorecard:

```
SCRAPE SUMMARY
─────────────
Total scraped:        [X]
Duplicates removed:   [Y]
Classified:
  → Target/Strong:    [N] (with email: [N], LinkedIn-only: [N])
  → Secondary/Possible: [N]
  → Skipped:          [N]
  → Deleted (junk):   [N]

Emails found:         [N] of [N] attempted
Hot list additions:   [N] to [hot list name]
LinkedIn queue:       [N] contacts

Credits spent:        [N] (email enrichment)
```

**Offer strategic recommendations:**
→ "Your hit rate was [X]%. For your next scrape, I'd suggest: [specific changes to Sales Nav filters, title strings, or company selection]."
→ "You now have [N] S-tier prospects with valid emails ready for outreach. Should I build a campaign for them, or add them to an existing one?"
→ "The LinkedIn-only queue has [N] contacts. These are worth connecting with manually — I can generate personalised connection notes if you'd like."
→ "I noticed [pattern] in this scrape — [insight]. This might mean [implication for strategy]."

---

## LinkedIn safety limits

→ 80-100 profile views per day
→ 100-150 Chrome extension scrapes per day
→ 20-25 connection requests per day (LinkedIn-enforced)
→ 500-700 connection requests per week (rolling cap)

## Hit rate benchmarks

→ Broad company-page scrapes: 6-17% relevant-title hit rate
→ Title-specific Sales Nav searches (e.g. "Head of Sales" at target companies): 60-70%
→ Always prefer title-specific searches for efficiency

## Known issues

→ Chrome extension can create duplicate company entities. Always `search_companies` to check.
→ `get_bulk_enrichment_status` returns "idle" prematurely. Verify directly via `get_contact`.
→ `batch_find_contacts` job key deduplication within session — only one job runs per session. Run in a fresh chat for new results.
→ `add_to_hot_list` can reject a whole batch if one ID is invalid. Verify IDs first, or add in smaller batches.
