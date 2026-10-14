---
name: process-scrape
description: Reconcile a known LinkedIn contact-import batch in Kolvera, classify buyers/candidates, enrich approved gaps and organise reviewed lists.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Process Scrape

Read [Operations contract](references/operations.md). Establish prospect versus candidate purpose, intended account/desk and actual import batch before acting.

1. Use `search_contacts` with supported filters and provenance to identify intake. A newest-50 list is a candidate set, not proof all belong to today's import. If provenance is insufficient, show ambiguity and obtain a bounded selection.
2. Resolve duplicates using stable identifiers, current company and history. Same name/company alone is not proof of duplicate identity. Flag merges/deletes for explicit approval; preserve notes and existing relationships.
3. Derive buyer and candidate criteria from the selected desk/RMP. A contact can be commercially relevant in different ways; avoid blanket rejection of HR, engineering leaders or individual contributors. Present ambiguous classifications.
4. Link reviewed buyers with `link_prospect_to_icp`; use `bulk_link_candidates_to_reverse_market_profile` only for the correct candidate pool/profile purpose. Check existing profiles before creating one and inspect per-link outcomes.
5. For approved email gaps use `bulk_find_emails`, retain job_id, then `get_bulk_enrichment_status(job_id=...)`. Read affected records with `get_contact` before claiming completion. If company sourcing is needed, use explicit titles/caps and retain `batch_find_contacts` job_key; reconcile terminal outcomes and never replay uncertain companies.
6. Inspect existing hot lists, then use `create_hot_list`/`add_to_hot_list` as authorised. Explain fit and S/A/B tiering.
7. Propose a queue: ready for reviewed outreach, needs evidence/enrichment, or not relevant. Enrolling into an active campaign can send, so requires explicit send authority covering recipients/content/inbox. Do not route opt-outs to another channel as a workaround.

Report selected batch/provenance, counts by classification, duplicates left untouched, actual spend, terminal receipts and remaining uncertainty. Keep private screening notes out of client-facing summaries.
