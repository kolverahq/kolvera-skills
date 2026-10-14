---
name: contact-enrichment
description: Find and verify contacts for selected Kolvera companies, with title controls, paid-job receipts and safe handling of partial or uncertain enrichment.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Contact Enrichment

Read [Operations contract](references/operations.md). Email enrichment costs 2 credits per contact found with a verified email. Phone tiers and BYOK are listed in that contract; get actual results/costs rather than assuming all cache results are free.

## Choose the audience and budget
Read the selected desk, companies and existing contacts. Confirm buyer titles from this market; founders, HR, engineering leaders and individual contributors may be relevant depending on the goal. Do not impose a SaaS-only buyer list.
Agree a contact cap and credit budget. Existing consent, suppression and previous outreach matter before campaign use.

## Find contacts
Use `batch_find_contacts` for at most 20 company IDs, with icp_id, explicit titles and max_per_company; use seniority/function when applicable. Start with a small approved sample if coverage is uncertain.
Retain job_key; poll `get_enrichment_job` at the returned interval. Only queued/running mean continue. Stop on complete, partial, failed, out_of_credits, interrupted or dispatch_uncertain.
Inspect companies_done, companies_remaining and uncertain_company_ids. Reconcile created contacts and receipts. Never replay uncertain work; retry only confirmed unstarted companies within budget. Each new call is a separate run.

For one company, `find_company_contacts` uses the same targeting and async receipt discipline. Do not omit icp_id as a generic workaround for an error; diagnose the returned error and preserve desk linkage.
If no suitable contacts are found, report that result. Create a manual contact only from verified identity/details, then optionally use `find_contact_email`.

## Fill gaps
Use `search_contacts` to identify missing/invalid/unverified email statuses. `bulk_find_emails` returns an async job: retain its job_id and poll `get_bulk_enrichment_status(job_id=...)`. Do the same for `bulk_find_phones`; use individual email/phone tools for reviewed single records.
An idle/latest-job response is not proof this run finished. Reconcile affected records with `get_contact`; unresolved work remains unresolved.
Use `verify_contact_email` when appropriate. Valid work addresses are preferred; catch-all is not verified delivery. Present risk and user policy before enrolment. Missing/personal/invalid email does not authorise an alternative channel.

Report titles, valid-email coverage, skips, actual spend, terminal status and unresolved work. Offer sorting/hot lists next; do not auto-enrol or send.
