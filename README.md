<div align="center">

# Kolvera Skills for Claude

**Pre-built workflows that turn Claude into your Kolvera operating system.**

Say a trigger phrase — *"map the market for AU fintech"* — and Claude runs the whole workflow: the right Kolvera tools, in the right order, with the right stop rules and approval gates.

No prompt engineering. No clicking around the app. Just talk to Claude.

</div>

---

## ⚡ Quick start (about 5 minutes, no coding)

Two things: **connect Kolvera to Claude once**, then **add the skills you want**. Both are done inside Claude — no terminal required.

### Step 1 — Connect Kolvera to Claude (once)

This lets Claude actually run things in your Kolvera account.

**In the Claude web app ([claude.ai](https://claude.ai)) or Claude Desktop:**
1. Click your name (bottom-left) → **Customize** → **Connectors**
2. Click **＋ Add custom connector**
3. Paste this URL: `https://mcp.kolvera.io/mcp`
4. Click **Add**, then sign in to Kolvera when prompted
5. In any chat, open the **＋** menu → **Connectors** → switch **Kolvera** on

> Prefer the guided version with screenshots? → **[kolvera.io/guide/claude](https://kolvera.io/guide/claude)**

### Step 2 — Turn on Skills (one-time, if you haven't)

Skills run in Claude's code sandbox and are available on Claude's **paid plans (Pro, Max, Team, Enterprise)** — they aren't available on Free.
- **Settings → Capabilities → "Code execution and file creation" → On** (Pro and Max).
- On **Team / Enterprise**, an admin enables *Code execution* + *Skills* for the workspace first.

### Step 3 — Add a skill and use it

1. **Download a skill** — click **⬇ Download** next to any skill below (one file).
2. In Claude, go to **Customize → Skills → ＋** and **upload the `.zip`**. Toggle it **on**.
3. **Say the trigger phrase** — e.g. *"Map the market for commercial cleaning in Melbourne."*

That's it. Claude runs the whole workflow, pausing at each gate to check in with you.

> **New here? Start with these three:** **map-the-market**, **icp-review**, and **campaign-build**. They cover most of the work.

---

## 📦 The skills

Every skill lives in the [`skills/`](skills/) folder. They group into three jobs — **Find → Organize → Engage** — the same shape as working a market in Kolvera.

Each is consultative by design: it **reviews your setup, flags what's weak, suggests improvements, and confirms before spending credits** (that behaviour ships as the `kolvera-guidelines` skill — add it once and it applies to all of them).

### 🔍 Find — build your market and surface the right targets

| Skill | Say this to Claude | What it does | Get it |
|---|---|---|---|
| **map-the-market** | *"Map the market for [your niche]"* | The full pipeline end-to-end: ICP → Deep Research → job scraping → contacts → hot lists. ~30–60 min with approval gates. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/map-the-market.zip) |
| **icp-review** | *"Review my ICP"* or *"Why is my desk noisy?"* | Runs the desk health check (`diagnose_desk`) to pinpoint discovery-queue noise, then audits your targeting — tightens industries, sharpens exclusions, fixes the sector/size gates that let junk through. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/icp-review.zip) |
| **deep-research** | *"Run deep research on my ICP"* | Discovers companies you didn't know existed, with smart stop rules so you don't waste credits. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/deep-research.zip) |
| **job-scrape** | *"Scrape job boards for my ICP"* | Runs SEEK / LinkedIn / Indeed scrapes, filters results, finds who's actively hiring. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/job-scrape.zip) |
| **company-research** | *"Research [company name]"* | Single-company deep dive: AI research, decision-makers, hiring signals, buying triggers, recommended approach. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/company-research.zip) |

### 🗂️ Organize — enrich, sort, segment, and keep records clean

| Skill | Say this to Claude | What it does | Get it |
|---|---|---|---|
| **contact-enrichment** | *"Enrich contacts for my ICP"* | Finds decision-makers at your targets, with verified emails and phone numbers. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/contact-enrichment.zip) |
| **prospect-sort** | *"Sort my new contacts"* | Classifies contacts into prospects, candidates, and junk; links them to the right profiles. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/prospect-sort.zip) |
| **process-scrape** | *"I just scraped 50 contacts from LinkedIn"* | Dedupes, classifies by title, finds emails, builds hot lists. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/process-scrape.zip) |
| **hot-list-build** | *"Build hot lists for my ICP"* | Segments people into S/A/B tiers, ready for outreach. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/hot-list-build.zip) |
| **candidate-pipeline** | *"Move [name] to [stage]"* | Manage stages, grades, notes, and next actions across your candidate pipeline. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/candidate-pipeline.zip) |
| **deal-pipeline** | *"Review my pipeline"* | Flags stale records, surfaces next actions, recommends adjustments. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/deal-pipeline.zip) |

### 📣 Engage — run outreach and keep momentum

| Skill | Say this to Claude | What it does | Get it |
|---|---|---|---|
| **campaign-build** | *"Build a campaign for [hot list]"* | Multi-step email campaigns with the T.I.P.S. framework — copy, inboxes, enrolment, activation. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/campaign-build.zip) |
| **rmp-campaign** | *"Take [name] to market"* | Take one person to market end-to-end: build their profile → match companies → find buyers → launch the campaign. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/rmp-campaign.zip) |
| **campaign-health** | *"Check my campaigns"* | Fast health check — flags bounces, low opens, inbox problems, dead campaigns. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/campaign-health.zip) |
| **morning-briefing** | *"Morning briefing"* | Daily digest: meetings, replies, follow-ups, pipeline alerts, top 3 priorities. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/morning-briefing.zip) |
| **work-the-desk** | *"Work my desk"* | The daily desk loop: review what the auto-router filed overnight, triage New Leads, clear the Action Inbox, act on the hottest hiring signal. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/work-the-desk.zip) |
| **weekly-review** | *"Weekly review"* | End-of-week synthesis: what moved, what's hot, where to focus next week. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/weekly-review.zip) |

> **➕ Add the behaviour layer:** [⬇ **guidelines.zip**](https://github.com/kolverahq/kolvera-skills/releases/latest/download/guidelines.zip) — makes every skill consultative (review → suggest → confirm → run). Upload it once.
>
> **Don't want to pick?** [⬇ **Download everything**](https://github.com/kolverahq/kolvera-skills/releases/latest/download/kolvera-skills-all.zip) (one zip per skill inside — unzip, then upload the ones you want).

---

## 🎯 Tune a Desk — the alignment workflow

A **Desk** is an activated target market: Kolvera watches job boards for companies hiring your roles and surfaces them as "New Leads". When that queue fills with off-target companies, it's almost always the desk's *definition* that's too broad — not the engine. The `icp-review` skill runs this whole sequence; the order matters, because you fix the definition before the filters.

Say **"review my desk"** or **"why is my desk noisy?"** and Claude will:

1. **Diagnose first** — `diagnose_desk` reads the live queue and reports what's dragging it off-target (accepted sectors, unsized companies, and buyer-titles that leaked into your scrape net), each with a fix. Baseline before changing anything.
2. **Roles you recruit for** — the job titles you *place*, and the widest lever on noise. Broad or junior titles (e.g. "SDR", a generic "Manager") match at nearly every company. Keep them specialist. *These are separate from…*
3. **Buyer titles** — the people you *sell to* (Head of…, VP…, Founder). Kept apart from the roles above — a buyer title sitting in your scrape net is the single biggest noise source, because it matches everywhere. Claude flags any overlap.
4. **Sectors** — the industries you accept, plus the ones to **veto** (recruitment agencies, consultancies, and other off-target sectors that share a keyword with you).
5. **Company sizes** — sets the ceiling that filters out enterprises far bigger than your sweet spot. No size range = mega-caps slip through.
6. **Locations** — the geography you can actually deliver to.
7. **Re-diagnose** — confirm the flags cleared and the queue tightened.
8. **Clean what's left** — leads from the old, broad settings linger; Claude dismisses the junk and routes anything that belongs to a *different* desk over to it.
9. **Audit the company map** — the queue isn't the whole story: companies added under the old, broad settings are already *on* the desk. Claude lists the map (`list_icp_companies`), judges each against the desk's "who fits", then removes what never belonged (`bulk_unlink_companies_from_icp`), routes wrong-vertical companies to the desk they *do* fit (`move_companies_between_icps`), and runs `research_company` (1 cr) on any it can't judge before deciding. **Companies with live BD state — a reply, a meeting, an active sequence — are never removed automatically; those stay your call.**

The point: **roles ≠ buyers, and both are separate from sectors and sizes.** Getting those four right — in that order — is what makes a desk surface the right companies and nothing else. Then the map audit clears out what the old settings let in.

---

## 💡 Get better results

Add the **Kolvera MCP Prompt Guide PDF** to your Claude **Project knowledge** (next to the skills). It gives Claude the full tool reference (every Kolvera tool), polling timings, and known workarounds, so workflows run more reliably.

→ Download it from **[kolvera.io/guide/claude](https://kolvera.io/guide/claude)**.

If you have the **T.I.P.S. Cold Email Playbook** PDF, add that too — it powers the email framework in `campaign-build`.

---

## 💳 What things cost

Most actions are free. Credits are only spent on data and AI generation, and **every skill confirms with you before spending them.**

| What | Cost |
|---|---|
| Generate an ICP (AI) | 2 credits |
| Deep Research — first run | 6 credits |
| Deep Research — expand | 4 credits |
| Contact found *with verified email* | 2 credits |
| Phone number found | 6 cr direct dial · 2 cr company line · 0 cr if already on file or BYOK |
| Research one company | 1 credit |
| Market / Role Intelligence report | 15 credits |
| Job board scraping | Uses your monthly scrape allowance (not credits) |
| Sorting, hot lists, campaigns, reviews, pipeline | Free |

---

## ✅ Requirements

- A **Kolvera account** on any plan — [kolvera.io](https://kolvera.io)
- **Kolvera connected to Claude** (Step 1 above)
- **A Claude plan with Skills** — Pro, Max, Team, or Enterprise (Skills aren't available on Free). Custom connectors work on Free too, but the skills need a paid plan.

---

## 📖 Walkthroughs

Three end-to-end runs you can copy. Each line in a code block is something you *say* to Claude — it does the rest.

<details>
<summary><b>① Your first market in 15 minutes</b> — Find</summary>

<br>

1. **Set your business context** (who you are, what you sell, your voice — everything inherits from this):
   ```
   Build my business context from [your-website-url] and set it as primary.
   ```
2. **Create your ICP:**
   ```
   Generate an ICP titled "AU HR Tech — Decision Makers" targeting HR tech companies in Australia with 20-500 employees, using my primary business context. Show me the full profile.
   ```
3. **Discover companies** (Deep Research, 6 cr; each expand 4 cr):
   ```
   Run Deep Research against my ICP, then show the results summary and company count.
   ```
4. **Find decision-makers:**
   ```
   Find contacts at the top 10 companies in my ICP, starting with the 50+ employee ones.
   ```
5. **Review:**
   ```
   Summary: how many companies, how many contacts found, how many valid emails, and which companies still need contacts?
   ```
</details>

<details>
<summary><b>② From a target list to a live campaign</b> — Organize → Engage</summary>

<br>

1. **Sort and enrich what you've gathered:**
   ```
   Sort my new contacts, then find emails for the ones missing them.
   ```
2. **Segment into tiers:**
   ```
   Build hot lists for my ICP, S/A/B by seniority and fit.
   ```
3. **Build and launch a campaign** (T.I.P.S. — two threads, two pains, 21 days):
   ```
   Build a campaign for my [hot list] hot list. Pain 1: [describe]. Pain 2: [describe]. Social proof: [customer + metric].
   ```
4. **Taking one person to market instead?** Use `rmp-campaign`:
   ```
   Take [name] to market. Create their profile, cross-reference my ICP, find buyers, and build the campaign.
   ```

**Tips:** run Deep Research before campaigns (it populates triggers for personalisation) · set concrete ICP pain points · use named-customer proof, not soft fallbacks.
</details>

<details>
<summary><b>③ Your daily & weekly rhythm</b> — Engage</summary>

<br>

- **Each morning:**
  ```
  Morning briefing
  ```
  (meetings, replies, follow-ups, pipeline alerts, your top 3 priorities)
- **Mid-day campaign check:**
  ```
  Check my campaigns
  ```
  (flags bounces, low opens, inbox issues, dead campaigns)
- **Review the pipeline:**
  ```
  Review my pipeline
  ```
- **Fridays:**
  ```
  Weekly review
  ```

**Handling a reply:** move the record forward and set the next step, e.g. *"Move [name] to meeting_booked. Note: '[summary]'. Next action: '[what to do]' on [date]."*
</details>

---

## 🛠 Advanced — Claude Code & power users

Prefer the filesystem? Every skill is a folder with a single `SKILL.md` inside `skills/`. Clone and drop them into your skills directory:

```bash
git clone https://github.com/kolverahq/kolvera-skills.git
cp -r kolvera-skills/skills/* ~/.claude/skills/
```

`~/.claude/skills/` is picked up by Claude Code automatically. (Claude.ai web and Desktop use the upload flow in Step 3 — skills don't sync between the web app and the filesystem, so install them where you'll use them.)

---

## 🤝 Contributing

Found a bug, or built a workflow that should be a skill? [Open an issue or PR](https://github.com/kolverahq/kolvera-skills/issues).

## License

MIT — use these however you like. See [LICENSE](LICENSE).

---

<div align="center">

Built by **[Kolvera](https://kolvera.io)** — AU-native sales intelligence for teams that sell.

</div>
