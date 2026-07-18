---
name: map-the-market
description: Build a complete target market in Kolvera from scratch — ICP creation, company discovery via Deep Research, job board scraping, lead triage, contact enrichment, prospect sorting, and hot list segmentation. The output is a scored, campaign-ready desk. Trigger when the user says "map the market", "build a market map", "map [sector/niche/location]", "who's hiring in [market]", "build my ICP", "find companies for [niche]", or any variation of mapping out a target market. Covers MCP Prompt Guide Phases 1-8 as an orchestrated workflow with approval gates.
---

# Map the Market

Turn a one-line market brief into a fully worked, segmented, campaign-ready target market in Kolvera. Walks through ICP creation, company discovery, job board scraping, pipeline filtering, contact enrichment, prospect sorting, and hot list organisation.

**Target time:** 30-60 minutes with approval gates between phases.
**Credit budget:** Set upfront. Typical: 15-30 credits for a focused market, 30-50 for a broad one. Job board scraping uses the monthly scrape allowance, not credits.

## Consultative behaviour (applies to every step)

**Never auto-execute without context.** At every gate, Claude should:
→ Review what exists and show the user what it found
→ Identify gaps, grey areas, or things that look too broad or too narrow
→ Make specific suggestions with reasoning ("I'd recommend narrowing industries from 18 to 10 because Deep Research converges faster on focused ICPs")
→ Ask targeted questions to fill gaps ("You've listed Head of Sales as a buyer — do you also sell to operations leaders, or is this purely a sales-led purchase?")
→ Wait for confirmation before proceeding

**Never change anything without asking.** Suggest changes, explain why, then let the user decide.

## Prerequisites

→ A **Business Context** stored in Kolvera (your company identity — drives AI email tone and ICP targeting). If none exists, create one first:
  - From website: `create_business_context_from_website` with your domain
  - Manual: `create_business_context` with all 7 fields
  - Set as primary: `set_primary_business_context`
  - Check existing: `list_business_contexts`

→ The Kolvera MCP server connected to Claude.

---

## Step 0 — Review business context

Before anything else, pull the user's business contexts: `list_business_contexts` (the only read tool — there is no get-by-id) and read the one flagged as primary from that list.

**Review and question:**
→ Does the company description accurately reflect what they sell right now? (Not what they sold 6 months ago)
→ Are the buyer titles specific enough? "Decision-makers" is too vague. "Heads of Sales at B2B SaaS companies with 50-200 employees" is usable.
→ Is the value proposition clear and differentiated? If it reads like it could apply to any competitor, flag it.
→ Is the voice/tone set? This drives every AI-generated email. If it says "professional" but the user wants "direct and conversational", the campaigns will feel wrong.
→ Are there any missing fields? Blank fields mean the AI fills gaps with generic content.

**Suggest improvements.** Example: "Your business context lists your buyers as 'business leaders' — that's quite broad. Based on what you've told me about your market, would it be more accurate to say 'Heads of Operations and COOs at mid-market logistics companies'? That would make your ICP targeting and campaign copy much sharper."

**Only proceed after the user confirms** the business context is accurate — or after applying their requested changes.

---

## Step 1 — Frame the market

Pin down what "the market" is before spending credits.

**Ask the user these questions** (skip any they have already answered):
→ "Who are you trying to reach? Not just the industry — the specific person. What's their title? What keeps them up at night?"
→ "What size companies? A 10-person startup and a 500-person scale-up are completely different sales conversations."
→ "Where? Are you servicing nationally, or does geography matter for delivery?"
→ "What's the demand signal? How do you know a company needs what you sell right now? Is it a job ad, a funding round, a technology change?"
→ "Who should we exclude? Competitors, companies you already work with, verticals that don't fit?"

**Check for existing ICPs:** `list_icp_profiles`. If one already covers this market:
→ Show it to the user: "You already have an ICP called [name] with [X] companies. Should we build on this, or is this a different market?"
→ `get_icp_profile` and review whether it is still current

**Confirm credit budget** before proceeding. Suggest a range based on market breadth: "For a focused market like this, I'd budget 15-20 credits for discovery. Broader markets can run to 30-50. What's your comfort level?"

---

## Step 2 — Create the ICP (Phase 1)

**Option A — AI generation (recommended, 2 credits):**
→ `generate_icp_profile` with a descriptive title and the user's primary business context
→ The AI populates: target_titles, target_industries, target_company_sizes, target_locations, pain_points, outreach_hooks, objection_handling, disqualifiers, differentiators, value_proposition, linkedin_keyword

**Option B — Manual creation (free):**
→ `create_icp_profile` with explicit fields from Step 1

**Naming convention:** Prefix with desk context if relevant (e.g. "Contract — [Market Name]", "Perm — [Market Name]"). Check `list_icp_profiles` first to avoid duplicates.

**One ICP per audience.** If the user describes two distinct buyer types, suggest splitting: "It sounds like you're targeting both HR Tech companies and Fintech companies. These have different buyers and different pains. I'd recommend two separate ICPs so your campaigns and research stay focused. Want to start with the one that's most urgent?"

---

## Step 3 — Review and tighten the ICP (Phase 2)

**APPROVAL GATE 1** — This is the most important review in the entire workflow. A loose ICP wastes credits on irrelevant companies and produces weak campaigns. Take time here.

Show the user the full ICP, then walk through every field with specific observations and questions:

**Target titles — are these actually the buyers?**
→ "You have 'Head of Sales' listed. Does the Head of Sales actually make this purchasing decision, or does it sit with the CEO at companies this size?"
→ "I notice 'HR Director' is in your titles. In my experience, HR facilitates but rarely owns budget for [this type of purchase]. Should we remove it, or do you find HR is the actual decision-maker in your market?"
→ "For companies under 50 employees, the CEO or founder is often the buyer regardless of the function. Should we add CEO/Founder for the smaller end of your size band?"

**Target industries — specific enough?**
→ If more than 12-15 industries: "You have 18 industries listed. Deep Research converges much faster with 8-12. Which of these are your strongest verticals? I'd suggest leading with those and adding the rest in a second pass if needed."
→ Flag overlaps: "You have both 'Technology' and 'Software' listed — these will pull the same companies. I'd suggest consolidating to 'B2B SaaS' or whatever is most specific to your buyers."
→ Flag vagueness: "'Professional Services' is very broad — it includes everything from accounting firms to management consultancies. Can we narrow this to the specific type of professional services you target?"

**Company sizes — realistic for the offer?**
→ "You're targeting 1-1000 employees. That's a huge range. A 5-person startup and a 800-person company have completely different buying processes, budgets, and decision-makers. What's the sweet spot where your product/service delivers the most value?"
→ "Companies under 20 employees often don't have dedicated [role title] — the founder handles it. Should we set the floor at 20 or 50?"

**Locations — can you actually service these?**
→ "You've listed all of Australia. Are you genuinely able to deliver nationally, or would we get better results focusing on Sydney and Melbourne where the company density is highest?"

**Disqualifiers — complete enough?**
→ "Are there any competitors or companies you've already pitched to that we should exclude?"
→ "Should we exclude recruitment agencies, consulting firms, or government organisations?"
→ "Any companies where you have existing relationships that you'd want to approach separately rather than through a cold campaign?"

**Pain points — specific or generic?**
→ "Your pain points say 'struggling with growth'. Every company is struggling with something. Can we make this sharper? What specifically breaks when your buyers don't have your product/service? What does it cost them in dollars, time, or missed opportunities?"

**Outreach hooks — trigger-based?**
→ "Good hooks reference something observable — a job ad, a funding round, a product launch. 'Interested in improving efficiency' isn't a hook. 'Noticed you just posted for a [role title]' is. Can we make your hooks more trigger-specific?"

**LinkedIn keyword — usable in Sales Navigator?**
→ "Let me check this Boolean string. [Review and suggest improvements.] I'd tighten it by adding [specific terms] and removing [broad terms] that would flood results with irrelevant profiles."

**Apply changes** via `update_icp_profile` only after the user confirms each suggestion.

---

## Step 4 — Run Deep Research (Phase 3)

Discover companies that match the ICP.

**Initial run (3 credits):**
→ `trigger_deep_research` against the ICP ID
→ Poll `get_research_report` with `fields: status` after ~60 seconds, then every 30 seconds
→ Switch to `fields: full` once status shows complete

**Review results and offer insights:**
→ "Deep Research found [X] companies. Here's the breakdown by vertical: [summary]. The strongest cluster is in [vertical] — [X] companies, which makes sense because [reasoning]."
→ Flag surprises: "Interestingly, [X] companies came back in [unexpected vertical]. These might be worth including if [reasoning], or we can exclude them. What do you think?"
→ Flag noise: "I'm seeing [X] companies that look like they might be too large/small/wrong industry for your target. Should I exclude these types from future runs?"
→ Suggest ICP refinements based on what came back: "The research pulled a lot of [industry] companies but very few [other industry]. If [other industry] is important to you, we could tighten the ICP description to weight it more heavily. Or it might just be a smaller market than expected."

**Expand until diminishing returns (2 credits each):**
→ `expand_deep_research` against the ICP ID
→ Track the trend and show it to the user after each run

**Stop rules:**
→ **Tight ICPs (5-8 industries):** Stop at fewer than 2 new companies for 2 consecutive runs
→ **Broad ICPs (15+ industries):** Stop at 3+ consecutive runs at or below 4 new companies with no upward spike
→ **Budget cap:** Never exceed the agreed credit budget without user approval

**APPROVAL GATE 2** — "We've run [X] rounds of research and found [Y] total companies. The last two runs added [Z] and [W] new companies — the returns are tapering off. I'd recommend stopping here and moving to job scraping. Or we can do one more expand for 2 credits if you think there's more to find. What would you prefer?"

---

## Step 5 — Scrape job boards (Phase 4)

Find companies actively hiring — the highest-intent targets.

**Check for existing configs:** `list_scrape_configs`. If one exists:
→ "You already have a scrape config called [name] linked to this ICP. Last run was [date]. Should I re-run it, or do we need to update the keywords first?"
→ Review the config: "Your current keywords are [list]. Based on the ICP we just refined, I'd suggest adding [terms] and removing [terms] that are pulling irrelevant results. The keywords update is a full overwrite, so I'll send the complete list. Does this look right?"

**Create and run scrapes:**
→ `run_job_scrape` with `icp_id` — always pass `icp_id` so discovered companies auto-map
→ Valid sources: `seek`, `indeed`, `linkedin`, `reed` (Reed = UK only)
→ Run sources as separate calls (effectively parallel)
→ Poll `get_scrape_progress` every ~90 seconds

**Quality gate — review and suggest config improvements:**
→ `analyze_scrape_quality` on the config
→ "The scrape returned [X] results with a [Y]% pass rate. Here's what I'd suggest tightening:"
→ "These [Z] companies keep appearing in scrapes but aren't a fit — I'd add them to your exclude list so they stop showing up."
→ "These keywords are pulling irrelevant roles: [list]. Should we narrow them or add negative keywords?"
→ "I'm seeing [location] results that are outside your target geography. Should we tighten the location filter?"
→ Apply excludes via `update_search_config_excludes` only after user confirms

---

## Step 6 — Filter the pipeline (Phase 5)

→ `search_pipeline_jobs` sorted by date
→ `get_pipeline_job` for full details on promising listings

**Cross-reference and suggest:**
→ "Of the [X] roles scraped, [Y] are at companies already in your ICP and [Z] are at new companies I haven't seen before."
→ "These [N] new companies look like strong ICP fits based on their size and industry. Should I add them to the ICP?"
→ "I'd prioritise these roles: [list with reasoning]. The [role] at [company] has been posted for [X] days — the longer it sits open, the more likely they'll engage with an approach."
→ "These roles don't look like a fit because [reasoning]. Should I skip them?"

Shortlist after user confirmation: `update_pipeline_job` with status `shortlisted`, notes, and follow-up dates.

---

## Step 7 — Enrich contacts (Phase 6)

**Before enriching, confirm the targeting:**
→ "For these companies, who's the right person to reach? Based on your ICP, I'll be looking for [titles]. Should I also look for [additional titles], or does that go too wide?"
→ "Companies under 50 employees rarely have a dedicated [title]. For the smaller ones, should I look for the CEO/Founder instead?"

**Batch find contacts (2 credits per contact found with verified email):**
→ `batch_find_contacts` with up to 20 company IDs, linked to the ICP
→ Start with companies that have 50+ employees for best coverage
→ Poll `get_enrichment_job` every 15-30 seconds. Large batches take 8-12 minutes.

**Review enrichment results and flag issues:**
→ "Enrichment found [X] contacts across [Y] companies. [Z] companies returned zero usable contacts."
→ "I'm seeing a lot of individual contributor titles in the results — [examples]. Kolvera enrichment often returns ICs rather than decision-makers. I'd filter these out and keep only [titles]. Does that look right?"
→ "These [N] companies still need contacts. The options are: Kolvera enrichment retry (sometimes picks up different results), LinkedIn Sales Navigator scrape via the Chrome extension, or manual research. Which approach do you want to take?"

**Email enrichment and triage:**
→ `bulk_find_emails` on contacts without valid emails
→ "Email enrichment results: [X] valid work emails, [Y] catch-all (usable but monitor bounces), [Z] personal only (LinkedIn outreach only), [W] no email found."
→ "I'd suggest creating a LinkedIn-only hot list for the [Z+W] contacts without work emails. These are still valuable targets — they just need a different channel. Should I set that up?"

---

## Step 8 — Sort and build hot lists (Phases 7-8)

**Suggest a segmentation strategy:**
→ "Looking at the [X] contacts with valid emails, here's how I'd segment them for campaigns:"
→ "[Segment A] — [N] contacts. These share [characteristic]. They'd respond to a message about [angle]."
→ "[Segment B] — [N] contacts. Different vertical/size/need. They'd need a different hook around [angle]."
→ "Does this segmentation make sense, or would you split it differently?"

**Tier prospects and explain the reasoning:**
→ **S-tier:** "These [N] contacts are at companies with active hiring signals AND strong ICP fit AND valid emails. I'd outreach to these first."
→ **A-tier:** "These [N] contacts have strong fit and valid emails but no active hiring signal. Still worth reaching — they may have needs they haven't posted about yet."
→ **B-tier:** "These [N] contacts are ICP fit but either missing email or weaker signal. Worth enriching further before outreach."

→ `create_hot_list` with `icp_id`, `add_to_hot_list` with tiers

**APPROVAL GATE 3** — Show the final hot lists with counts and tier breakdowns. "Here's your market map summary: [total companies], [total contacts], [S/A/B breakdown]. The S-tier list is ready for a campaign right now. Want me to build one, or do you want to review the lists first?"

## Step 9 — Activate the Desk (keep it working for you)

The map is a one-time build; a **Desk** keeps finding new targets automatically. Activating turns the ICP into a live Desk — it classifies the mapped companies and switches on the discovery Feed (new hiring at matching companies surfaces as "New Leads" going forward).

→ Run `activate_desk` with the ICP ID. It's free and idempotent.
→ Then run `diagnose_desk` once to confirm the discovery queue is clean — it reports the queue by sector and size and flags any noise (e.g. an over-broad accepted sector) with the fix. If it flags junk, tighten `excluded_sectors` / `target_company_sizes` via `update_icp_profile` (the `icp-review` skill walks this).
→ Tell the user: "Your desk is live — I'll keep surfacing new companies that start hiring your target roles. Check `diagnose_desk` any time the New Leads look noisy."

---

## Output

The completed market map includes:
→ A refined ICP with company pool
→ Deep Research discovery results (with insights on market shape)
→ Job board scrape results with pipeline matches
→ Enriched contacts sorted into prospects (and candidates if applicable)
→ Tiered hot lists ready for campaign enrolment
→ Specific recommendations for next steps

**Next step:** Use the `campaign-build` skill to create and launch outreach campaigns against the hot lists.

---

## Known issues

→ `batch_find_contacts` can stall on 20-company batches. Retry in batches of 10.
→ `get_bulk_enrichment_status` can return "idle" prematurely. Verify directly via `get_contact`.
→ Deep Research report delta does not always equal ICP database growth. Check ICP company count before and after each expand.
→ ICP prospect count may differ between UI and API. Pull the ICP directly to verify.
→ Chrome extension can create duplicate company entities. Always `search_companies` before creating.
→ Scrape config keyword updates are full overwrites — always pass the complete desired keyword list.
