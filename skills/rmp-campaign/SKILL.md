---
name: rmp-campaign
description: Take a screened candidate to market using Kolvera's Reverse Market Profile (RMP) system. End-to-end workflow from candidate qualification through to live campaign — RMP creation, company map building, prospect enrichment, campaign construction, and activation. Trigger when the user says "take [candidate] to market", "build RMP campaign", "launch RMP", "set up outreach for [candidate]", "create reverse market profile", or any variation of building a candidate-led outreach campaign. Recruitment vertical skill.
---

# RMP Campaign

Take a screened candidate to market. The RMP (Reverse Market Profile) is the atomic unit of candidate-led BD — one candidate, one profile, one or more campaigns.

**Target time:** 30-45 minutes with approval gates.
**Credit cost:** RMP generation is free if manual, or costs credits if AI-generated. Contact enrichment: 2 credits per contact found with verified email. Intelligence reports: 15 credits each.

## Core Principle

Lead with candidates, not services. Every campaign starts with a real person, not a pitch.

---

## Phase 1 — Qualify the candidate for an RMP

Not every screened candidate gets an RMP. The gate:

**Build an RMP when:**
→ Candidate is actively looking or open and moveable within 4-8 weeks
→ Candidate has a clear, differentiated story (not generic)
→ You can name at least 5 companies that would realistically hire this person
→ Comp expectation is within market range for the target companies
→ Candidate has given authority to represent (verbal minimum, written preferred before submission)

**Do NOT build an RMP when:**
→ Candidate is "just exploring" with no timeline
→ Profile is too generic to differentiate in a cold email
→ You cannot name 5 realistic target companies
→ Candidate is overpriced for the market they fit

## Phase 2 — Create the RMP

**AI generation (recommended):**
→ `generate_reverse_market_profile` from the candidate's data. Or create manually via `create_reverse_market_profile`.
→ Always pass `linked_icp_id` to group under the parent ICP.
→ Use desk-prefix naming (e.g. "Perm — [Candidate Name] — [Role Title]")

**Post-generation review:**
→ Title and title variants: do they match what hiring managers actually search for?
→ Core capability: does it tell a commercial story, not just list skills?
→ Target employers: are these real, reachable companies?
→ Buyer pitch: would you send this verbatim to a hiring manager? If not, rewrite.
→ Comp band: confirmed with the candidate?
→ Engagement type: perm, contract, or both?
→ Disqualifiers: what would waste everyone's time?

**Generate a Role Intelligence Report** if one does not exist for this role family:
→ `generate_role_intel_report` (15 credits, async)
→ One report per role family (e.g. one for Implementation, one for SE, one for CSM). Reuse across candidates.
→ The report URL goes in Step 1 of every campaign — value-add for the prospect.

## Phase 3 — Build the company map

**Cross-reference the ICP:**
→ Pull the ICP company list: `get_icp_profile`
→ Filter against the RMP's target sectors, target employers, company sizes, and locations
→ Score matches:
  - `direct_fit` — industry and stage match the RMP's sweet spot
  - `adjacent_fit` — related sector, transferable product complexity
  - `speculative` — worth a shot
→ Link companies: `bulk_link_companies_to_reverse_market_profile` with tier classification (cap 200 per call — keep batches ≤100 as 200 can time out)

**Classify engagement type per company:**

| Type | When to use | Campaign framing |
|------|-------------|-----------------|
| Perm | Company building a permanent function | Lead with long-term value |
| Contract | Programme-based, defined delivery | Lead with ramp-time saving |
| Both | Buyer behaviour is mixed | Lead with flexibility |

Check recent job ads, industry norms, and the candidate's preference to determine type.

## Phase 4 — Source and audit prospects

**Audit auto-discovered prospects:**
Every auto-discovered prospect must pass a title alignment check.

| Action | Title examples | Reasoning |
|--------|---------------|-----------|
| ENROL | Head of Implementation, Head of CS, COO, VP CS, Head of Delivery | Own the function the candidate joins |
| ENROL (sub-50 headcount) | CEO, Founder, Co-Founder | At small companies the founder hires |
| ENROL (secondary) | CRO, VP Revenue, VP CX | Worth having if the primary is missing |
| SKIP | CTO, Head of Engineering, VP Product | Wrong function |
| SKIP | Head of People, TA Manager, HR Director | Facilitators, not decision-makers |
| SKIP | Account Executive, SDR, Key Account Manager | Individual contributors |
| DELETE | Scraping artefacts: "Join [Company]", "Latest News" | Bad data |

**Find missing contacts:**
→ Path A: Kolvera enrichment — `find_company_contacts` with target titles. Check results. Enrichment often returns ICs.
→ Path B: LinkedIn Sales Navigator — build a search for gap companies with target titles. Scrape via Chrome extension. Ingest via `ingest_scraped_profiles`. Filter by title alignment.

**Email enrichment:**
→ `bulk_find_emails` on all new prospects
→ Triage: valid/catch-all work email → campaign. No email → LinkedIn-only hot list.

**Create LinkedIn-only hot list** for prospects without usable email:
→ `create_hot_list` with clear naming (e.g. "[Candidate Name] — LinkedIn Only")
→ Tier S/A based on seniority and company fit

## Phase 5 — Determine campaign lanes

**When to split vs single campaign:**

| Scenario | Structure |
|----------|-----------|
| Single engagement type, single pitch | 1 campaign |
| Single engagement type, different verticals needing different hooks | 2-3 campaigns by vertical |
| Mixed engagement types across verticals | 2-4 campaigns by type + vertical |
| Tiny company count in a segment (fewer than 3) | Merge into nearest lane |

**Campaign naming:** `[Engagement Type] — [Candidate Name] RMP — [Vertical/Segment]`

## Phase 6 — Build and launch campaigns

**Create campaign:**
→ `create_campaign` linked to the ICP
→ Set daily limit, send schedule, timezone

**Build the 5-step sequence** (recruitment standard):

| Step | Day | Purpose | CTA | Length |
|------|-----|---------|-----|--------|
| 1 | 0 | Candidate pitch + role intel report link | "Worth a conversation?" | 80-120 words |
| 2 | 3-4 | Depth / vertical-specific proof | "Happy to send their profile" | 60-100 words |
| 3 | 6-7 | Short nudge | "Any thoughts?" | 20-30 words |
| 4 | 11-12 | Transparency (availability, notice, engagement type) + referral redirect | "Happy to be pointed the right way" | 40-60 words |
| 5 | 18-19 | Clean breakup | "I will close the loop" | 30-40 words |

**Copy rules:**
→ Never name the candidate in the email. He/she only. Protect identity until authority is confirmed and a profile is requested.
→ Step 1 includes the role intel report URL
→ All steps end with just "Cheers," — nothing after. Kolvera auto-appends the sender signature.
→ Subject lines: lowercase, no punctuation except commas. Lead with the candidate's headline capability.
→ No bullet points in email bodies. Prose only.

**Pre-activation QA:**
→ All copy rules followed
→ Campaign linked to correct RMP
→ Business context set
→ At least one healthy inbox assigned
→ Every enrolled contact title-audited
→ Every enrolled contact has valid or catch-all work email
→ Preview at least one rendered email

**Activate:**
→ `activate_campaign`
→ Enrol contacts
→ Verify first sends

## Phase 7 — Monitor

**Daily:**
→ Check bounce rates (above 5% = pause and review)
→ Check open rates (below 20% after 10+ sends = subject line issue)
→ Check for replies

**Reply handling:**
→ Positive (wants profile): prepare candidate pack, get written authority, send within 24 hours
→ Warm (not now, later): add to CRM pipeline with follow-up date, remove from campaign
→ Referral (try X person): thank them, add referred contact, mention referral in new outreach
→ Negative: acknowledge gracefully, remove from campaign, do not re-enrol

**Collision management:**
→ Same prospect, different candidates: stagger sends. Never two candidate pitches to the same person in one week.
→ Same company, different prospects: acceptable.

## Known issues

→ Contacts can be enrolled while the campaign is **draft or active**. A **paused** campaign rejects enrolment — **resume it first**, then enrol.
→ `bulk_find_emails` polling via `get_bulk_enrichment_status` can return "idle" prematurely. Verify via `get_contact`.
→ `find_company_contacts` with `icp_id` may error if the website scraper returns zero. Omit `icp_id`, link afterwards.
