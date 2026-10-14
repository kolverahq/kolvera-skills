---
name: map-the-market
description: Build a Kolvera desk from a market brief through targeting, research, job signals, contact enrichment and reviewed hot lists.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Map the Market

Read [Operations contract](references/operations.md). This is an orchestration workflow; execute only the phases the user requested. Agree separate discovery and enrichment caps, because contact volume can exceed a research-only estimate.

## 1. Context and criteria
Read existing business contexts and desks before creating duplicates: `list_business_contexts`, `list_icp_profiles`, `get_icp_profile`.
Confirm geography, target industries, size bands, recruited roles (if recruitment), buyer titles, evidence-backed pain/proof and exclusions. Roles being recruited and people buying the service are different filters.
Use `create_business_context` or `create_business_context_from_website` only when needed; changing the primary context affects other workflows and requires scope covering it.
Use `generate_icp_profile` or `create_icp_profile`; review output before activation. Generation is a paid action; inspect current cost. Apply authorised corrections with `update_icp_profile` and read back. Do not activate ongoing monitoring unless included in user scope.

## 2. Wiring and discovery
Use `diagnose_desk` for targeting noise and `activate_desk` only when ongoing desk operation is intended.
Call `trigger_deep_research(icp_id=...)`, retain returned report_id and read mode/cost/reason. Smart mode can expand an existing report. Poll `get_research_report` using that report ID and returned timing hints.
For another approved round use `expand_deep_research(report_id=...)`. Stop on budget, recommendation="stop", incomplete evidence needing review, or diminishing qualified desk additions. Raw report growth is not useful fit by itself.

## 3. Hiring signals
Inspect `list_scrape_configs` before creating duplicates. Use `run_saved_config` for existing configs or `run_job_scrape` with explicit desk linkage and appropriate source/location. Available sources and supplier health can change; inspect live tool response.
Retain run/config IDs and poll `get_scrape_progress`. Use `analyze_scrape_quality` and `search_pipeline_jobs` for fit, with dates and geography explicitly scoped.
Propose keyword/exclusion changes; authorised keyword replacement uses the complete desired list. Do not auto-dismiss a live client relationship because it misses a new desk criterion.

## 4. Enrich and classify
Read existing contacts first. `batch_find_contacts` takes at most 20 company IDs plus titles, max_per_company and relevant seniority/function. Poll returned job_key with `get_enrichment_job`.
Only queued/running continue. On any terminal status, reconcile done/remaining/uncertain companies. Never replay uncertain work. Retry only confirmed unstarted work inside the approved cap.
For `bulk_find_emails`, retain job_id and use `get_bulk_enrichment_status(job_id=...)`; verify affected records rather than treating idle as success.
Classify contacts as buyer, candidate, both where supported, or irrelevant against this desk. Do not use a fixed SaaS title list. Deleting records needs explicit destructive scope.

## 5. Organise and close
Inspect existing lists, then `create_hot_list` and `add_to_hot_list` as authorised. Explain S/A/B tiers using fit, current signals and contact quality; preserve active ICP target scoring.
Report desk/report/job IDs, useful additions, actual spend, unresolved jobs, skips and list counts. A campaign-ready list is not permission to enrol into active outreach or send. Offer a reviewed campaign draft as the next step.
