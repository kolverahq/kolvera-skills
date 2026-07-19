---
name: work-the-desk
description: The daily runtime loop for live Kolvera Desks — triage New Leads, review what the auto-router filed overnight, clear the Action Inbox, and turn desk signals into outreach. Trigger when the user says "work my desk", "work my desks", "clear my new leads", "triage discovery", "what did the router do", "work the queue", "desk run", or any variation of processing a live desk's daily output. Complements morning-briefing (which reads the day) — this one acts on it.
---

# Work the Desk

An activated Desk produces work every day: New Leads from discovery, auto-routed companies from the router, BD nudges in the Action Inbox. This skill is the loop that turns that output into pipeline — in one pass, most mornings under 15 minutes.

**Target time:** 10-15 minutes daily.
**Credit cost:** Free for the whole loop. Only spend credits if the user asks to enrich or research along the way (contacts 2 cr each, company research 1 cr) — confirm first.

## The shape of the loop

Since the auto-router shipped, discovery is hub-and-spoke: a master intake desk scrapes, the router files single-vertical matches onto the right Desk automatically, and what's left in the intake queue is the residue — ambiguous, unclassified, or genuinely new companies. The daily loop is therefore: **check what the router did → triage the residue → clear the Action Inbox → act on the hottest signal.**

## Step 0 — What happened overnight

→ `get_morning_brief` — the pipeline section includes an "N leads auto-routed to your desks overnight (…)" line when the router acted. That is your receipt: those companies are already filed, do not re-triage them.
→ If the user wants the audit trail, routed companies carry `method: "auto_router"` on the desk's company map.

## Step 1 — Desk health at a glance

→ `list_icp_profiles` — identify the live Desks (desk_activated).
→ `diagnose_desk` on any desk the user calls noisy — it reports the discovery queue AND the company map by sub-sector, with plain-English flags and fixes. If flags fire, offer the `icp-review` skill rather than fixing ad hoc.
→ `get_icp_readiness` if a desk seems inert (no leads at all) — checks the wiring, not the noise.

## Step 2 — Triage the New Leads residue

→ `list_new_leads` on the intake desk (and any vertical desk with a queue). Each lead carries company, role, location, employee_count, ai_sector, ai_subsector.
→ For each lead, one of three moves:
   - **Belongs on a vertical Desk** → `action_new_leads` with `add` on THAT desk's profile_id. Note: adding maps the company on the destination only — also dismiss the lead on the intake desk so it stops resurfacing there (`action_new_leads` dismiss is desk-scoped, it will not hurt the company anywhere else).
   - **Genuine pool resident** (real vertical SaaS, no dedicated desk) → leave it. The pool is a monitor, not a to-do list.
   - **Junk** (recruiter, giant, services firm, marketplace ad posted "@ another company") → `action_new_leads` with `dismiss`.
→ Batch the calls — one add list and one dismiss list per desk, not per-lead calls.
→ Unclassified companies (ai_subsector null) resolve themselves as the background classifier catches up; do not research them just to triage.

## Step 3 — Clear the Action Inbox

→ `list_pending_actions` — review-gated drafts and nudges queued by automations (re-engagement, reference nudges, post-call).
→ For each: `approve_pending_action` or `dismiss_pending_action`. Read before approving — these send on approval.
→ If the inbox is empty and the user wants re-engagement volume, offer `run_reengagement_sweep` (queues drafts for stale candidates — they land back in this inbox for review, nothing sends directly).

## Step 4 — Act on the hottest signal

→ `get_bd_brief` — the desk's BD nudges: which mapped companies are hiring your roles right now, with the angle.
→ Pick the top 1-3 and offer the concrete next move:
   - Candidate on the bench who fits the open role → the `rmp-campaign` skill (candidate-led outreach is the strongest opener).
   - No bench fit but strong signal → `find_company_contacts` for the buyer (2 cr per verified contact — confirm), then a campaign or a one-off approach.
   - Interesting but not now → `add_to_hot_list` so it is queued, not lost.

## Step 5 — Close the loop

One-line summary per desk: routed N / triaged N (added X, dismissed Y) / inbox cleared N / actioned [company]. Flag anything that needs a human call — a lead at a company with a live reply thread, a desk whose flags keep firing, a signal too good to sit on.

## Cadence

Daily: Steps 0, 2, 3 (minutes each). Step 4 whenever there is BD time. Step 1 weekly, or whenever a queue feels off — persistent noise means the desk definition needs the `icp-review` skill, not more triage.

## Known issues

→ Routed leads can linger on the intake desk's queue if they were added manually (the router clears its own; manual adds do not) — the desk-scoped dismiss in Step 2 is the fix.
→ `action_new_leads` dismiss is per-desk by design. To kill a company everywhere, that is a different decision — raise it with the user, never assume.
