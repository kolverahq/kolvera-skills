---
name: hot-list-build
description: Segment ICP prospects into tiered hot lists ready for campaign enrollment. Organises by segment so each campaign speaks to one audience with one message. Trigger when the user says "build hot lists", "segment my prospects", "tier my contacts", "organise for campaigns", or any variation. Maps to MCP Prompt Guide Phase 8.
---

# Hot List Build

Segment prospects into campaign-ready hot lists. Each list should be tight enough for a single campaign message — one audience, one hook.

**Credit cost:** Free.

## Consultative approach

Claude should suggest segmentation strategies based on what it sees in the data — not just ask the user how to split. After building lists, Claude should flag contacts that might be in the wrong segment and suggest tier adjustments with reasoning. Also read GUIDELINES.md in this repo for the full consultative behaviour pattern.

## Step 1 — Review available prospects

→ `list_icp_prospects` or `get_icp_profile` to see the full prospect pool
→ Ask the user: what segments make sense for this market? (e.g. by vertical, by company size, by engagement type, by geography)
→ Or suggest segments based on the ICP's target industries and company distribution

**Proactive segmentation suggestions:**
→ "Looking at your [N] prospects, I can see natural clusters: [X] in [vertical A], [Y] in [vertical B], and [Z] that don't fit neatly into either. I'd suggest creating separate lists for each — they'd need different outreach angles. The [vertical A] list could lead with [pain], while [vertical B] cares more about [different pain]."
→ "You have [N] prospects at companies with fewer than 50 employees and [N] at companies with 200+. These are very different conversations. Worth splitting?"
→ "I notice [N] contacts at companies with active job postings (hiring signal). These are your highest-intent targets — I'd put them in their own S-tier list for priority outreach."

## Step 2 — Create segment hot lists

→ `create_hot_list` with `icp_id` or `reverse_market_profile_id` linked to a parent project
→ Use clear naming (e.g. "[Vertical] — [Audience]", "[Engagement Type] — [Segment]")
→ Check `list_hot_lists` first to avoid duplicates
→ Or use `build_target_hotlist` to auto-segment an ICP's members into tier-labelled hot lists based on ICP scoring — the fastest path when you just want the split done for you

## Step 3 — Tier prospects

Assign tiers based on signal strength and data quality:

→ **S-tier** — Active hiring signal + strong ICP fit + valid work email. Outreach immediately.
→ **A-tier** — Strong fit + valid email, no active hiring signal. Outreach this week.
→ **B-tier** — ICP fit but missing email or weaker signal. Enrich first, then queue.

→ `add_to_hot_list` with `tier` = `s`, `a`, or `b` (lowercase only — not "tier_1" or "TIER 1")
→ `update_hot_list_member` to adjust tiers after review

## Step 4 — LinkedIn-only list

Create a companion hot list for prospects who cannot be reached by email:
→ Personal email only (Gmail, Outlook)
→ No email found
→ Invalid/bounced email

These go on a LinkedIn-only outreach list. Name it clearly (e.g. "[Segment] — LinkedIn Only").

## Step 5 — Review and confirm

Show the user:
→ Each hot list with contact count and tier breakdown
→ Total S-tier prospects across all lists (the immediate outreach pool)
→ Total contacts without email (LinkedIn-only queue)

**Next step:** Use the `campaign-build` skill to create campaigns against the hot lists.

## Known issues

→ `add_to_hot_list` can reject a whole batch if one ID is invalid. Verify IDs first, or add in smaller batches.
→ The `tier` field accepts `s`, `a`, or `b` only (lowercase).
