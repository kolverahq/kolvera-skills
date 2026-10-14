---
name: rmp-campaign
description: Take a screened candidate from reviewed Kolvera Reverse Market Profile through target-company fit, buyer sourcing and a consented Float draft or launch.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Candidate reverse marketing

Read [Operations contract](references/operations.md) and [Float runbook](references/float.md). Use current candidate evidence and authority, not inferred availability or a fixed customer's market assumptions.

## Qualify and review
Confirm candidate interest/timeline, capability evidence, compensation currency/period, location, work rights and constraints. Record gaps rather than inventing them. Establish authority for anonymous market testing separately from named profile/CV submission and external sends.
Use `list_reverse_market_profiles` and `get_reverse_market_profile` to select an existing profile; verify candidate purpose and linked desk. Initial profile creation is not exposed by the current MCP tool set: hand off to the supported app workflow and read back the result rather than inventing a creation tool. For an existing legacy profile, `regenerate_reverse_market_profile` with apply=False previews a refresh; applying is paid and requires reviewed scope. Use source-specific private refresh controls for private profiles, not the legacy refresh. Review title variants, buyer story, evidence, exclusions and targets. A role-family pool is not a named candidate's publication authority.

## Build and audit the map
Read desk companies with `list_icp_companies`; compare each against candidate sectors, location, size, engagement type and disqualifiers. Classify direct/adjacent/speculative using evidence. Link through `bulk_link_companies_to_reverse_market_profile` within its current batch limit. Read per-link outcomes.
Buyer titles derive from this candidate's function and the employer's hiring structure. Engineering leaders are valid for engineering roles; HR/TA may be authorised routes. Do not apply a fixed implementation/SaaS title table to every candidate.
Inspect existing prospects and live outreach before enriching. Use explicit title and per-company caps. Preserve uncertain-job receipts and paid budget.

## Optional role intelligence
`generate_role_intel_report` costs 23 credits at this verification date. Generate only within approved scope/budget and inspect the result. Reuse only when role, geography, currency, evidence freshness and sharing authority fit. A report URL is optional and must be client-safe; never insert an internal URL by default.

## Build the Float
Create a draft via `create_campaign` with icp_id, reverse_market_profile_id, candidate_id and framework="float". Creation/get responses expose email_mode, not a privacy selector; template does not distinguish private from legacy. Inspect the response/error from an authorised generation operation: mode="private_float" or private_float_review_required selects the private flow. Preserve source provenance; if mode cannot be established, stop rather than infer privacy or regenerate just to discover it.
Follow the Float runbook for staged copy, private pay versus approved client charge, token semantics, attachment/publication review and recipient fit.
For legacy delivery: attach authorised inbox, enrol reviewed contacts while draft/paused, inspect skips, render previews, then activate preview and confirm only after explicit launch approval.
For private native Float: use reviewed profile_id/profile_revision and stable request_id, exact expected_revision on regeneration, then available private draft/preview/delivery tools. Stop if required capability is absent; never fall back to less private legacy delivery.

## Replies and follow-through
Positive interest: verify scope of candidate disclosure, prepare reviewed pack and obtain any missing submission authority before delivery. Referral: confirm referred identity and permission before new outreach. Negative/opt-out: record preference and stop applicable contact; do not evade it through another channel.
Check current collision/suppression results; do not override them with a made-up scheduling rule. Report campaign/profile IDs, draft or launch receipt, spend, evidence gaps and next action.
