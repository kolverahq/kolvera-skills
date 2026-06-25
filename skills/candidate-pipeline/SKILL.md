---
name: candidate-pipeline
description: Manage candidate stages, grades, notes, and next actions across Reverse Market Profile (RMP) profiles in Kolvera. Move candidates through the recruitment pipeline, update records after calls, track competing processes. Trigger when the user says "update candidate pipeline", "move [candidate] to [stage]", "update [candidate]", "candidate status", or any variation of managing the candidate pipeline. Recruitment vertical skill.
---

# Candidate Pipeline

Manage candidates through the recruitment pipeline in Kolvera. Update stages, grades, notes, and next actions from chat.

**Credit cost:** Free.

## Candidate stages

`candidate_stage` (set via `update_contact`) is validated against this vocab — an unknown value is rejected:

`role_defined` → `target_companies_mapped` → `candidates_sourced` → `shortlisted` → `connection_sent` → `accepted` → `first_message_sent` → `reply_received` → `qualified_in_chat` → `call_requested` → `call_booked` → `call_completed` → `active` → `nurture` → `closed_rejected`

**Client-side (client-job) stages are separate** — `submitted`, `client_interview`, `offered`, `placed` are NOT `candidate_stage` values. They live on the client-job pipeline and are tracked via `list_client_jobs` (which shows shortlist counts per stage and placement revenue). Do not try to set these as `candidate_stage` via `update_contact`.

## Update a candidate

→ `search_contacts` by name to find the contact
→ `get_contact` for the full record
→ `update_contact` with any combination of:
  - `candidate_stage` — pipeline position
  - `candidate_grade` — A (top), B (solid), C (backup)
  - `candidate_notes` — screening notes, call summaries, observations
  - `salary_zone` — comp expectations
  - `notice_period` — availability timeline
  - `work_rights` — visa status, work authorisation
  - `candidate_next_action` — what to do next
  - `candidate_next_action_date` — when to do it (ISO date, e.g. "2026-06-15")

**Important:** Three separate notes fields exist:
→ `notes` — general notes
→ `candidate_notes` — recruitment-specific notes
→ `prospect_notes` — sales/BD-specific notes

Do not mix them. Use `candidate_notes` for screening data, call summaries, and placement-related observations.

## Batch operations

→ `list_reverse_market_profile_candidates` — see everyone in an RMP pool
→ `bulk_link_candidates_to_reverse_market_profile` — assign candidates to pools (cap 200 per call — keep batches ≤100 as 200 can time out; format: `{contact_id, reverse_market_profile_id}`)
→ `unlink_candidate_from_reverse_market_profile` — remove from a pool

## Client-side tracking

→ `list_client_jobs` — shows client jobs with fee terms, status, shortlist counts per stage, and placement revenue
→ Filter by company or view all

## Common workflows

**After a screening call:**
→ Update `candidate_stage` to `active` or `nurture`
→ Set `candidate_grade`
→ Add call summary to `candidate_notes`
→ Set `candidate_next_action` and `candidate_next_action_date`

**Candidate has a competing process:**
→ Note the competing company and timeline in `candidate_notes`
→ Set `candidate_next_action_date` to the decision deadline
→ Flag urgency — speed may be critical

**Candidate placed:**
→ Mark the candidate placed on the client-job pipeline (`placed` is a client-job stage, tracked via `list_client_jobs` — not a `candidate_stage`)
→ Update `candidate_notes` with start date, final comp, and any conditions
