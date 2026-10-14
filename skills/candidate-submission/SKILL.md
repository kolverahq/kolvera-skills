---
name: candidate-submission
description: Review Kolvera client-job shortlists, candidate evidence and scoped submission consent, then record authorised submission and interview outcomes.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Kolvera shortlist and submission

Read [Operations contract](references/operations.md). Use [Audience-safe documents](references/documents.md) only when preparing material derived from this Kolvera shortlist. Sending and e-signing need separate explicit authority.

## Shortlist and evidence
Read `get_client_job`, approved role brief, `get_contact` and `list_client_job_shortlist`. Confirm exact company/job and contact identity; a candidate ID returned by shortlist tools may differ from contact_id; retain each correctly.
Assess all candidates against the same job-related criteria. Separate verified evidence, candidate statements, recruiter inference and unanswered questions. Screening notes remain private.
Add through `add_client_job_shortlist_candidate` only as authorised. Update notes with `update_client_job_shortlist_notes`, preserving prior evidence; inspect history/events for duplicate submission or previous withdrawal.

## Consent and material
Confirm named employer/role, recipient/channel, exact CV/profile/material version, date, expiry/withdrawal scope and previous applications/representation. Generic interest or anonymous Float authority is not named submission consent. Recording consent is separate.
If e-sign is appropriate, use the agency's approved jurisdiction-specific template: `list_esign_templates`, `create_esign_document`, `preview_esign_document`. Verify signers, fields, linked records and exact document revision. `send_esign_document` requires expected_revision, review_hash and idempotency_key plus explicit send approval. Draft creation is not a send. Do not draft universal legal terms or substitute an unapproved master.
Read signed/current status with `get_esign_document`; delivery/open status alone is not acceptance.

## Submit and record
Preview final recipients and current attachments. Actual submission uses an available authorised delivery tool or manual channel; shortlist mutation itself does not transmit a pack. Stop if delivery capability or authority is missing.
After confirmed transmission, record `update_client_job_shortlist_status` as submitted with supporting receipt/notes. Never mark submitted from intention alone. Use `withdraw_client_job_shortlist_candidate` for explicit withdrawal rather than treating it as ordinary rejection.
Valid current stages: shortlisted, internal_iv, submitted, screening, client_interview, offer_presented, accepted, placed, declined, withdrawn. Read live schema; offer_presented needs offer_amount, placed needs start_date, backward corrections need correction_reason. Do not equate accepted with placed or invent financial values to satisfy gates.

## Interview and follow-through
Read the job/shortlist before preparation. Confirm stage, participants, timezone and existing meeting link. Prepare truthful candidate examples and a separate private interviewer scorecard. Calendar invitations depend on the available authorised connector; this skill does not assume native interview automation.
Capture client and candidate feedback separately, unresolved decisions, next owner/date and evidence source. Update client-job shortlist stage rather than candidate_stage for client interview/offer/placement outcomes. Read back all changes and report pending external steps.
