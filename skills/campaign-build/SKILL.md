---
name: campaign-build
description: Build and launch multi-step email campaigns in Kolvera using the T.I.P.S. cold email framework. Covers campaign creation, AI step generation, copy review, inbox assignment, enrollment, and activation. Trigger when the user says "build a campaign", "create a campaign", "launch outreach", "set up email sequence", "write campaign emails", or any variation of building email campaigns. Maps to MCP Prompt Guide Phase 9 and the T.I.P.S. Cold Email Playbook.
---

# Campaign Build

Create and launch a multi-step email campaign in Kolvera. Uses the T.I.P.S. framework for high-converting cold email sequences. Covers strategy, creation, copy, inbox assignment, enrollment, and activation.

**Credit cost:** Free (campaign creation and steps). AI step generation uses Claude Sonnet — no Kolvera credits.

## Consultative approach

Before building a campaign, Claude should review the target audience, confirm the pain points and proof points are specific enough, and suggest a sequence strategy. During copy review, Claude should flag weak subject lines, generic CTAs, or emails that are too long. After activation, Claude should suggest monitoring benchmarks. Also read GUIDELINES.md in this repo for the full consultative behaviour pattern.

## The T.I.P.S. Framework

Every high-converting cold email follows six beats:

→ **T — Trigger** — A real reason you are reaching out (a new hire, expansion, job ad). First line. Not spray-and-pray.
→ **I — Implication** — What you infer from the trigger. Shows you have done your homework.
→ **P — Pain** — A common pain the ICP faces, tied to the implication. Quantify the cost of inaction.
→ **S — Social Proof** — A named customer + the metric they achieved. Builds credibility.
→ **Solution** — One line on how you solved it. Brief. The goal is a response, not a sale on email.
→ **Soft CTA** — "Worth a chat?" "Open to hearing more?" Never ask for 30 minutes.

## The 7-Step Sequence Structure

Two threads. Two pains. Seven emails across 21 days.

| Step | Day | Thread | Structure | Pain |
|------|-----|--------|-----------|------|
| 1 | 0 | Thread 1 (new subject) | Full T.I.P.S. pitch | Pain 1 |
| 2 | 3 | Reply in thread | Value bump — relevant article + insight | Pain 1 |
| 3 | 5 | Reply in thread | Thoughtful bump — context + "any thoughts?" | Pain 1 |
| 4 | 12 | Thread 2 (new subject) | Full T.I.P.S. pitch (different wording) | Pain 2 |
| 5 | 15 | Reply in thread | Case-study bump — named result | Pain 2 |
| 6 | 18 | Reply in thread | Focus bump — observation + "is that the case?" | Pain 2 |
| 7 | 21 | Reply in thread | Referral bump — "should I talk to someone else?" | Pain 2 |

**Shorter sequences (3-5 steps)** are also valid. Adjust based on the user's preference and audience tolerance.

## Step 1 — Draft the strategy

**Ask the user these questions** (skip any already answered):
→ "Which hot list or prospect group is the audience? Let me pull it and check the contact quality before we build."
→ "What are the two main pains this audience faces? Be specific — 'struggling with growth' won't land in an email. What does it actually cost them when this problem isn't solved?"
→ "What social proof do you have? Named customers with specific metrics work best. If you don't have named references yet, we can use soft proof — 'teams we work with typically see [outcome]' — but named proof converts significantly better."
→ "What's the goal? A reply, a meeting booking, a demo request? This shapes the CTA in every email."
→ "How many steps? The T.I.P.S. standard is 7 (two threads, two pains, 21 days). For a warmer audience or follow-up, 3-5 steps might be better. What fits your audience?"

**Review the audience before building:**
→ Pull the hot list: `get_hot_list`
→ "This list has [N] contacts. [N] have valid emails, [N] have catch-all. The titles are: [breakdown]. Does this look like the right audience for this campaign?"
→ "I notice [N] contacts on this list don't have work emails — they'd bounce. Should I exclude them, or move them to a LinkedIn-only list?"
→ "Are there any contacts on this list who should NOT receive this campaign? Anyone you've already spoken to, or anyone at a company you're already pitching to through another channel?"

## Step 2 — Create the campaign

→ `create_campaign` with:
  - Name: clear, descriptive (e.g. "[Segment] — [Offer] Outreach")
  - `icp_id`: linked to the target ICP
  - `daily_limit`: default 30
  - `variant_mode`: `none` (single), `ab`, or `abc` for A/B/C testing

## Step 3 — Generate or write steps

**Option A — AI generation (recommended):**
→ `generate_campaign_steps` — reads the linked ICP and business context directly
→ Steer with `step_hints`: one angle per step (e.g. "pain about ramp time", "case study bump", "referral redirect")
→ Generation is async — poll `get_campaign_generation_status` after 30 seconds

**Option B — Manual creation:**
→ `create_campaign_step` for each step with: `step_number`, `subject`, `body`, `delay_days`
→ Steps 1 and 4 get subject lines (new threads). Steps 2, 3, 5, 6, 7 are reply-in-thread (no subject).

## Copy rules (non-negotiable)

→ Each email under 125 words
→ 3rd-5th grade reading level
→ Subject lines: 2 words, no punctuation, no adjectives (e.g. "Ramp Time", "Pipeline Gap")
→ Subject lines on steps 1 and 4 only (new threads)
→ No emojis, no bold/italic in body
→ Unsure tone: "guessing", "typically", "curious if"
→ Soft CTAs only — never ask for time blocks
→ Short lines, heavy white space
→ Reply-only CTAs (no calendar links in cold outreach)
→ Vary wording across steps — different phrasing for trigger, implication, pain, and proof each time
→ Sign-off: "Cheers," on its own line. Nothing after it. Kolvera auto-appends the sender signature.

## Step 4 — Review copy

→ `get_campaign` to pull all steps

**Review each step and flag issues:**
→ "Step [N] is [X] words — that's over the 125-word limit. Cold emails need to be scannable. I'd cut [specific section] to bring it under. Here's a tighter version: [suggestion]."
→ "The subject line '[subject]' is [X] words. Two words, no punctuation, no adjectives is the rule. How about '[suggestion]' instead?"
→ "Step 1 is missing a trigger line — it jumps straight into the pitch. Adding a real reason for reaching out ('Noticed you just posted for a [role]') makes it feel personal rather than mass-blast. Can we add one?"
→ "The CTA in Step [N] asks for '30 minutes of your time'. That's a hard ask in a cold email. Softer CTAs like 'Worth a chat?' or 'Open to hearing more?' get significantly more replies."
→ "Steps 2 and 5 use very similar wording. Each email should feel different — vary the trigger, implication, and proof phrasing. I'd rewrite Step 5 to [suggestion]."
→ "The sign-off in Step [N] has your name after 'Cheers,' — Kolvera auto-appends your signature, so this will double up. Just end with 'Cheers,' on its own line."

→ `update_campaign_step` to refine copy — only after user confirms each change
→ To retire a losing A/B variant on a live campaign: set `is_active=false` on each of its steps — traffic redistributes to remaining active variants

## Step 5 — Set send window

→ `update_campaign` (campaign must be in draft or paused state) with:
  - `send_start_hour` / `send_end_hour` (0-23)
  - `send_days` ("0"=Mon through "6"=Sun)
  - `send_timezone` (IANA format, e.g. "Australia/Sydney", "America/New_York")
  - `min_delay_minutes` / `max_delay_minutes` — random gap between individual sends

## Step 6 — Assign inboxes and enrol

→ `list_inboxes` — check health: pick active inboxes with `health_state: ok` and remaining capacity (`sends_today` under `daily_limit`)
→ `assign_inbox_to_campaign` — attach healthy inboxes
→ `enrol_contacts_in_campaign` — enrol contacts from the target hot list
→ `get_campaign_enrollments` to verify enrollment count and check for errors

**Enrollment rules:**
→ Contacts can be enrolled while the campaign is **draft or active**. A **paused** campaign rejects enrolment — **resume it first**, then enrol.
→ Contacts enrolled mid-sequence start from Step 1
→ Existing contacts continue from their current position when new steps are added

## Step 7 — Activate and verify

→ `activate_campaign`
→ After 24 hours: `get_campaign_stats` — check sent, opened, replied, bounced
→ Per-variant stats on A/B/C campaigns

**Pre-activation QA checklist:**
→ All steps end with just "Cheers," (no name after it)
→ Subject lines are lowercase, no punctuation except commas
→ No bullet points in any email body
→ Campaign linked to correct ICP and business context
→ At least one healthy inbox assigned
→ Send schedule set correctly
→ Every enrolled contact has been title-audited
→ Every enrolled contact has a valid or catch-all work email (no personal emails)

## Known issues

→ `generate_campaign_steps` is async — poll `get_campaign_generation_status` after 30 seconds.
→ Contacts can be enrolled while the campaign is **draft or active**. A **paused** campaign rejects enrolment — **resume it first**, then enrol.
