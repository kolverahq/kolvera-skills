---
name: job-scrape
description: Run approved Kolvera job-board configs, inspect async results and quality, and curate relevant pipeline jobs.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Job Board Scrape

Scrape job boards for live postings matching an ICP. Companies actively hiring are the highest-intent targets. Covers config creation, scrape execution, quality gate analysis, and pipeline filtering.

**Credit cost:** Uses monthly scrape allowance, not credits.

## Consultative approach

Before running a scrape, The assistant should review the existing config (if any) and suggest keyword improvements. After scraping, The assistant should analyse the quality gate results and recommend specific changes to the exclude list, keywords, or location filters. Read the bundled [Operations contract](references/operations.md) for budgets, job receipts and action authority.

## Step 1 — Set up the scrape config

Check for existing configs: `list_scrape_configs`. If one is aligned to the target ICP, reuse it.

**Review existing configs before running:**
→ "You have a config called [name] linked to this ICP. Let me check if the keywords are still aligned."
→ "Your current keywords are [list]. Based on your ICP, I'd suggest adding [terms] and consider removing [terms] that might pull noise. The keywords update is a full overwrite, so I'll send the complete list. Does this look right?"
→ "This config was last run on [date]. If it's been more than a week, it's worth re-running — new roles get posted daily."

**Create a new config (if needed):**
→ Fastest path: `run_job_scrape` with an `icp_id` — builds a full config and starts the scrape in one call. Always pass `icp_id` so discovered companies auto-map.
→ For a targeted one-off: pass manual keywords and locations alongside `icp_id`. Your values drive the run but discoveries still map to the ICP.

**Important:** Always pass `icp_id`. Scrapes without it create orphaned pipeline data. Check `list_scrape_configs` first to avoid duplicate configs.

## Step 2 — Run the scrapes

Inspect supported sources and supplier health in the live tool. Common sources include seek, indeed, linkedin and reed; choose source/location for this market. Supplier failure is not permission for blind retries.
Keep each source/config receipt separate; avoid launching a duplicate of an already-running config.
→ Use `run_saved_config` when a config already exists
→ Poll `get_scrape_progress` every ~90 seconds

**Timing benchmarks:**
→ LinkedIn: 2-4 minutes
→ Indeed: 3-5 minutes
→ SEEK: 5-10 minutes (longest)

## Step 3 — Quality gate analysis

→ `analyze_scrape_quality` on the config

**Review results and suggest improvements:**
→ "The scrape returned [X] results with a [Y]% pass rate. Here's what I'd tighten:"
→ "These [N] companies keep appearing but aren't a fit — [names]. I'd add them to your exclude list so they stop polluting results."
→ "These keywords are pulling irrelevant roles: [list]. Should we narrow them or add negative keywords?"
→ "I'm seeing results from [location] that are outside your target geography. Should we tighten the location filter?"
→ "Your pass rate is [X]%. Aim for 70%+ — below that means the config is too broad. I'd suggest [specific changes]."

Apply suggested excludes: `update_search_config_excludes` — only after user confirms

## Step 4 — Filter the pipeline

→ `search_pipeline_jobs` sorted by date
→ Filter for target role types, exclude noise
→ `get_pipeline_job` for full details on promising listings (description, salary, company link)

**Cross-reference with the ICP:**
→ Which hiring companies are already in the ICP?
→ Which are new and should be added? `link_company_to_icp`
→ Flag any already being handled manually

**Shortlist strong matches:**
→ `update_pipeline_job` with status `shortlisted`, notes on fit, and follow-up dates
→ Valid statuses: `new`, `shortlisted`, `applied`, `interviewing`, `offered`, `placed`, `rejected`, `archived`

## Known issues

After an uncertain config update, read back saved fields before retrying. A client timeout is not proof the write failed.
→ Scrape config keyword updates are full overwrites — always pass the complete desired keyword list, not just additions.
