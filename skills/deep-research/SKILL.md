---
name: deep-research
description: Run Kolvera Deep Research discovery loops against an ICP with credit budgets and stop rules. Discovers companies matching the ICP that the user did not know existed. Trigger when the user says "run deep research", "discover companies", "find more companies for ICP", "expand research", or any variation of running AI company discovery. Maps to MCP Prompt Guide Phase 3.
---

# Deep Research

Run AI-powered company discovery against an ICP. Each run finds new companies that match the profile. Expand iteratively until diminishing returns, tracking the trend and respecting credit budgets.

**Credit cost:** 6 credits for initial run, 4 credits per expand.
**Target:** 50-100+ companies discovered, depending on market breadth.

## Consultative approach

Before spending credits, Claude should review the ICP and confirm it is tight enough for research. After each run, Claude should share insights on what was found — not just numbers, but patterns, surprises, and suggestions for refinement. Also read GUIDELINES.md in this repo for the full consultative behaviour pattern.

## Step 0 — Confirm the ICP and budget

Ask the user which ICP to research. If unsure, `list_icp_profiles` and show options.

Pull the ICP: `get_icp_profile`. Confirm:
→ The ICP is refined (industries narrowed, exclusions set). If not, suggest running `icp-review` first.
→ Credit budget agreed. Suggest 15-25 credits for focused markets, 30-50 for broad ones.

Check existing research: `list_research_reports` filtered by ICP. If prior research exists, show it and ask whether to expand from there or start fresh.

## Step 1 — Initial run (6 credits)

→ `trigger_deep_research` with the ICP ID
→ Optionally set precision: `strict` (tighter, higher hit-rate), `balanced` (default), or `broad` (wider net, adjacent verticals)
→ Poll `get_research_report` with `fields: status` after ~60 seconds, then every 30 seconds
→ Once complete, switch to `fields: full` for results

Report to the user:
→ Number of new companies found
→ Summary by vertical or industry
→ Highest-priority targets
→ Any noise to flag

**Offer insights:**
→ "The strongest cluster is in [vertical] — [X] companies. This aligns with your ICP focus on [industry]."
→ "I found [X] companies in [unexpected industry]. These might be worth including if [reasoning], or we should exclude them from future runs. What do you think?"
→ "Only [X] companies came back in [expected industry]. This could mean the market is smaller than expected, or the ICP description needs to weight this industry more heavily. Should we adjust?"
→ "Based on these results, I'd suggest [tightening/broadening] the ICP's [specific field] before the next expand — it would improve the quality of what comes back."

## Step 2 — Expand loops (4 credits each)

→ `expand_deep_research` with the ICP ID
→ Same polling pattern: `fields: status` until complete, then `fields: full`
→ After each run, report the delta (new companies this run) and the trend

**Track the expansion trend.** Example:
→ Clear convergence: 9, 8, 5, 3, 1, 0 — stop.
→ Broad-ICP oscillation: 9, 8, 5, 6, 3, 6, 8, 4, 3 — apply practical stop rule.

## Stop rules

**Tight ICPs (5-8 industries):**
→ Stop when 2 consecutive runs return fewer than 2 new companies.

**Broad ICPs (15+ industries):**
→ Stop when 3+ consecutive runs return 4 or fewer new companies with no upward spike.

**Budget cap:**
→ Never exceed the agreed credit budget without explicit user approval.
→ Prefer `expand_deep_research` (4 credits) over `trigger_deep_research` (6 credits) for subsequent runs.

## Step 3 — Review results

→ `get_research_report` with `fields: full` for the final state
→ Summarise companies by vertical
→ Highlight highest-priority targets
→ Flag noise to exclude from future runs
→ Show total credit spend

**Check ICP company count** before and after the research session. Deep Research report delta does not always equal ICP database growth — verify with `get_icp_profile`.

## Known issues

→ `get_research_report` can stall at ~70% on status polling. Wait a few minutes, then request `fields: full` directly.
→ Deep Research report delta does not always match ICP company count growth. Always verify via `get_icp_profile`.
→ Broad ICPs (15+ industries) may never hit the tight convergence threshold. Use the practical stop rule.
