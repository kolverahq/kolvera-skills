---
name: icp-review
description: Audit and tighten an existing Kolvera ICP. Reviews every field — target titles, industries, exclusions, company sizes, pain points, LinkedIn keywords — with specific suggestions and questions. Identifies discrepancies, flags grey areas, and recommends improvements. Never changes anything without asking. Trigger when the user says "review my ICP", "audit my ICP", "clean my ICP", "tighten my ICP", "check ICP health", or any variation of reviewing and improving an existing target market profile. Maps to MCP Prompt Guide Phase 2.
---

# ICP Review

Audit an existing Ideal Client Profile field by field. Spot what is too broad, what is missing, what is outdated, and what would make Deep Research, scraping, and campaigns perform better. Suggest specific improvements with reasoning. Never change anything without asking.

**Target time:** 10-15 minutes.
**Credit cost:** Free (review only). Updates via `update_icp_profile` are free.

## Consultative approach

This skill is entirely consultative. Claude should:
→ Pull the ICP and walk through every field out loud
→ Flag anything that looks too broad, too narrow, missing, or inconsistent
→ Make specific suggestions with reasoning (not just "this could be better")
→ Ask targeted questions where the right answer depends on the user's market knowledge
→ Only apply changes after the user confirms each one

Also read GUIDELINES.md in this repo for the full consultative behaviour pattern.

## Step 1 — Pull the ICP and business context

Ask the user which ICP to review. If they are unsure, `list_icp_profiles` and show the list with names, company counts, and prospect counts.

Pull the full profile: `get_icp_profile` with the ICP ID.

Also pull the business context: `list_business_contexts` and review the primary. The ICP should align with the business context — if the context says "we sell to logistics companies" but the ICP targets "technology companies", flag the mismatch.

## Step 2 — Walk through every field

### Target titles

**What to check:**
→ Are these the actual decision-makers who control budget, or just influencers?
→ Are any titles too generic? ("Manager" could be anyone)
→ Are any missing? Think about who else sits in the buying committee.
→ For small companies (under 50 employees), is CEO/Founder included? At small companies, the founder often makes every hiring/purchasing decision regardless of function.
→ Are any wrong-function? (e.g. CTO listed when the product is a sales tool)

**Questions to ask:**
→ "When you close a deal, who signs off? Is it [listed title], or does someone else have final say?"
→ "At your best customers, who brought you in? Was it the [title], or did it come through a different role?"
→ "Do you ever sell to [unlisted title]? Some of our target companies might have that function under a different name."

### Target industries

**What to check:**
→ Count the industries. More than 12-15 means Deep Research results will be diluted. Suggest narrowing.
→ Are any too broad? "Technology" captures everything from hardware to SaaS to IT services.
→ Are any overlapping? "Software" and "SaaS" and "Technology" will pull the same companies.
→ Are any irrelevant? Maybe they were relevant when the ICP was created but the user's focus has shifted.
→ Are any missing? Based on the business context and the user's description of their market.

**Suggestions to make:**
→ "You have [X] industries listed. I'd suggest trimming to your top 8-10. Which of these are your strongest verticals — where you've had the most success or where demand is highest?"
→ "I notice both 'Financial Services' and 'Fintech' are listed. These pull very different companies — traditional banks vs SaaS startups. Which one is actually your target?"
→ "Your business context mentions [industry] but it's not in your ICP. Should we add it?"

### Target company sizes

**What to check:**
→ Is the range realistic? 1-10000 employees is not a target — it is everyone.
→ Is the floor too low? Very small companies may not have the budget, team, or need.
→ Is the ceiling too high? Enterprise companies (1000+) have different buying processes, procurement teams, and longer cycles.
→ Does the range match where the user has actually closed business?

**Questions to ask:**
→ "What's the smallest company you've successfully worked with? And the largest? That's probably your real range."
→ "Companies under [X] employees often don't have a dedicated [buyer title]. Should we set the floor there?"

### Target locations

**What to check:**
→ Can the user actually deliver to all listed locations?
→ Are there high-density markets missing? (e.g. user is in Australia but hasn't listed Sydney specifically)
→ Is "national" really the target, or would focusing on 2-3 cities produce better results?

### Disqualifiers / exclusions

**What to check:**
→ Are competitor names listed? If not, suggest adding them.
→ Are recruitment agencies excluded? (Common pollution source in many ICPs)
→ Are companies the user already works with excluded? (Avoids awkward double-approach)
→ Are any company types excluded that should be? (Government, non-profits, enterprises beyond their range)

**This field is often empty.** If it is, say so: "Your exclusions list is empty. This means Deep Research and scraping will return everything — including competitors and companies that aren't a fit. I'd recommend at least adding [specific suggestions]. What else should we exclude?"

### Pain points

**What to check:**
→ Are these specific enough to use in outreach copy? "Struggling with growth" is useless. "Losing 3 months of revenue per new hire because onboarding takes too long" is campaign-ready.
→ Do they reflect real pains the user has heard from customers, or are they aspirational?
→ Are they tied to measurable outcomes? (Dollars lost, time wasted, opportunities missed)

**Questions to ask:**
→ "When you talk to prospects, what's the #1 complaint they have about how they currently handle [the problem you solve]?"
→ "What does it actually cost them when this problem isn't solved? Can we put a number on it?"

### Outreach hooks

**What to check:**
→ Are the hooks trigger-based? (Reference something observable — a job ad, funding round, product launch, new hire)
→ Or are they generic? ("Interested in improving your sales process" is not a hook)
→ Are there enough? 3-5 minimum for variety across campaign steps.

**Suggestions to make:**
→ "Your hooks are fairly generic right now. The best hooks reference something the prospect just did — 'Noticed you posted for a [role]' or 'Saw you just raised a Series B'. Can we make these more trigger-specific?"

### LinkedIn keyword / Boolean string

**What to check:**
→ Is it syntactically correct for Sales Navigator? (OR operators, quotation marks on multi-word titles)
→ Is it too broad? (Returns thousands of results)
→ Is it too narrow? (Returns fewer than 50)
→ Does it match the target titles listed above?

**Suggest a test:** "Try this string in Sales Navigator and see how many results come back. If it's over 5000, we need to narrow it. Under 50, we need to broaden it."

## Step 3 — Summarise findings

Present a clear summary:
→ **Looks good:** Fields that are well-targeted and specific
→ **Needs tightening:** Fields with specific suggestions (list each one)
→ **Questions to resolve:** Things only the user can answer

## Step 4 — Apply changes

After the user confirms each change, apply via `update_icp_profile`.

**Important:** Apply changes in batches of 2-3 fields per call. `update_icp_profile` can time out on large updates.

## Step 5 — Suggest next actions

Based on the review:
→ "Now that the ICP is tighter, it's worth re-running Deep Research — the results should be more focused."
→ "Your scrape config was built off the old ICP keywords. I'd suggest updating it to match. Should I review it?"
→ "You have [X] companies in the ICP from before this review. Some of them might no longer fit the tighter criteria. Want me to run an ICP cleanse to check?"

## Known issues

→ ICP prospect count may differ between UI and API. Pull the ICP directly to verify.
→ `update_icp_profile` can time out on large updates. Split into multiple calls if needed.
