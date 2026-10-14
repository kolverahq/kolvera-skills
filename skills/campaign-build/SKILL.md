---
name: campaign-build
description: Prepare and launch a Kolvera email campaign with explicit framework, reviewed copy, inbox and recipient checks, and user-approved activation.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Campaign Build

Read [Operations contract](references/operations.md). Preparation and sending have different authority. Keep drafts/paused campaigns inactive until recipients, rendered content, inbox and schedule are approved.

## Strategy and framework
Read the desk/business context and audience (`get_hot_list` where applicable). Confirm purpose, evidence-backed trigger, pain, proof and CTA. Never invent customer outcomes or candidate facts.
Choose explicit framework on `create_campaign`:
- tips: structured T.I.P.S. service-selling sequence.
- float: candidate-led sequence, correctly linked through reverse_market_profile_id and candidate_id. Read the bundled [Float runbook](references/float.md).
- freeform: custom structure or step angles.

T.I.P.S. uses trigger, implication, pain, proof, solution and soft CTA. Its standard seven-step/two-thread structure is a starting point for an appropriate audience, not a universal requirement. Respect the user's chosen language, tone and signature.

## Draft and review
Create a draft with icp_id, framework, suitable daily_limit and variant_mode. `generate_campaign_steps` replaces existing steps; confirm that overwrite is intended. step_hints apply only to freeform. Tips/Float use structured data and ignore those hints.
For legacy async generation, retain campaign ID and poll `get_campaign_generation_status` using retry_after_seconds. If the result identifies private Float mode, follow that mode's private receipt/read/edit tools instead of legacy polling.
Manual steps use `create_campaign_step`: step 1 needs a subject; blank later subjects reply in the previous thread. Use `list_campaign_variables` for supported syntax and meaning.
Read `get_campaign`, then refine with `update_campaign_step` while draft/paused. Check factual claims, token fallbacks, sentence fragments, identity disclosure, signature duplication and rendering. Preview real and missing-signal cases. Write concise copy; do not impose one customer's fixed sign-off or claimed conversion guarantees.

## Prepare delivery
Use `update_campaign` for send_timezone (IANA), send_days, hours and delay range. Review recipient timezone and working days rather than assuming AU.
Use `list_inboxes` and `assign_inbox_to_campaign` for an authorised healthy inbox with remaining capacity. Access to a contact never grants permission to use another person's inbox.
Title/fit audit and suppression checks precede `enrol_contacts_in_campaign`. Read per-contact results and verify with `get_campaign_enrollments`. Paused campaigns accept enrolments without scheduling sends. Enrolment into an active campaign needs explicit send authority.

## Launch and verify
Show final campaign, recipients/skips, inbox, rendered preview and schedule. On explicit launch go, call `activate_campaign(campaign_id=...)` for preview, then confirm=True for activation. Use the separate private delivery path when the campaign is private Float; never bridge it into legacy delivery.
Record activation receipt. Verify first sends only when evidence exists; do not claim them from an active flag. Monitor actual replies/bounces/capacity. `get_campaign_stats` is lifetime totals; daily deltas need timestamped evidence or prior snapshots.
