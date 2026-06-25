# B2B Sales Quickstart

How to use Kolvera skills for a B2B sales workflow — from market mapping to pipeline management.

## The B2B sales workflow

```
Map the market → Enrich contacts → Segment hot lists → Launch campaigns → Manage pipeline
```

## Step 1 — Map your target market

```
Map the market for [your niche]. I sell [product/service] to [buyer titles] at [company types] in [locations].
```

This runs the full `map-the-market` skill with approval gates at each phase.

## Step 2 — Research priority targets

For high-value prospects, run a deep dive:

```
Research [company name]
```

This pulls company details, runs AI research, finds decision-makers, checks hiring signals, and surfaces buying triggers.

## Step 3 — Build and launch campaigns

```
Build a campaign for my [hot list name] hot list. Pain 1: [describe]. Pain 2: [describe]. Social proof: [named customer + metric].
```

This uses the T.I.P.S. framework to build a 7-step email sequence:
→ Two threads, two pains, 21 days
→ Emails 1 and 4 are full T.I.P.S. pitches (new subject lines)
→ Emails 2, 3, 5, 6, 7 are contextual bumps (reply in thread)

## Step 4 — Daily operations

Morning:
```
Morning briefing
```

Campaign check:
```
Check my campaigns
```

## Step 5 — Pipeline review

Weekly:
```
Review my pipeline
```

This flags stale prospects, surfaces next actions, and recommends adjustments.

## Step 6 — Handle replies

When a prospect replies, update their stage:

```
Move [prospect] to replied. Note: "[summary]". Set next action to "[what to do]" on [date].
```

Positive replies → move to `meeting_booked`
Warm replies → set follow-up date, remove from campaign
Referrals → add new contact, mention referral in outreach
Negative → acknowledge, remove from campaign

## Tips

→ **Run Deep Research before campaigns.** It populates buying triggers for email personalisation.
→ **Set clear ICP pain points.** Vague pains produce vague copy.
→ **Add Proof Points.** Named customer results beat soft fallbacks.
→ **Preview per contact.** Check each contact's resolved email in the Kolvera UI before activating.
→ **Companies actively hiring are the highest-intent targets.** Use job scrapes as a buying signal, not just a recruitment tool.
