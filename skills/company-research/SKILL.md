---
name: company-research
description: Review a Kolvera company, enrich approved evidence gaps and identify relevant buyers and hiring signals.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Company Research

Read [Operations contract](references/operations.md) before acting.

Run a comprehensive research pass on a single target company. Pulls everything Kolvera knows, enriches gaps, and surfaces actionable intelligence.

**Credit cost:** 1 credit for AI research. 2 credits per contact found with verified email.

## Step 1 — Find or create the company

→ `search_companies` by name or domain
→ If found: `get_company` for the full record
→ If not found: `create_company` with name and domain (but prefer `search_companies` first — scrapes create richer records automatically)

## Step 2 — Run AI research (1 credit)

→ `research_company` with the company ID
→ Returns: industry analysis, competitive positioning, recent news, technology stack, growth signals

## Step 3 — Pull existing contacts

→ `get_company_contacts` — who do we already have?
→ Review titles: are any decision-makers already in the CRM?
→ Check email status on existing contacts

## Step 4 — Find missing decision-makers

If key buyer titles are missing:
→ `find_company_contacts` with the company ID (async, 2 credits per contact found with verified email)
→ Poll `get_enrichment_job` every 15-30 seconds
→ Review results — enrichment often returns ICs rather than decision-makers

For companies under 50 employees where enrichment returns zero:
→ `create_contact` manually with known details
→ `find_contact_email` to enrich

## Step 5 — Check hiring signals

→ `search_pipeline_jobs` filtered by company name
→ Any active job postings? What roles? How long have they been open?
→ Older ads (5+ days) indicate higher urgency
→ Multiple concurrent postings indicate growth or turnover

## Step 6 — Build the intelligence brief

Present to the user:

**Company overview:**
→ Name, domain, industry, headcount, location
→ What they do (from AI research)
→ Growth signals and recent activity

**Decision-makers:**
→ Contacts found with titles, email status, and LinkedIn (if available)
→ Who is the most likely buyer?

**Hiring signals:**
→ Active job postings (role, posted date, salary if listed)
→ What the hiring pattern suggests (building a team, backfilling, scaling)

**Buying triggers:**
→ From `get_company` fields: buying_triggers, BD recency
→ From AI research: competitive pressure, funding rounds, product launches

**Recommended approach:**
→ Who to contact first and why
→ Suggested outreach angle
→ Any existing relationship or prior outreach to be aware of

## Known issues

Preserve intended desk linkage and job receipt. Diagnose the returned error; do not omit icp_id or start another paid run as a generic workaround.
→ Companies under 50 employees often return zero contacts from batch enrichment. Use manual creation + email enrichment.
