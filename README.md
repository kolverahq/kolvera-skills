<div align="center">

# Kolvera Skills for Claude

**Pre-built workflows that turn Claude into your Kolvera operating system.**

Say a trigger phrase — *"map the market for AU fintech"* — and Claude runs the whole workflow: the right Kolvera tools, in the right order, with the right stop rules and approval gates.

No prompt engineering. No clicking around the app. Just talk to Claude.

</div>

---

## ⚡ Quick start (about 5 minutes, no coding)

You need two things: **connect Kolvera to Claude once**, then **add the skills you want**. Both are done from inside Claude — no terminal required.

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

Skills run inside Claude's code sandbox, so it has to be enabled:
- **Settings → Capabilities → Code execution → On** (Free, Pro, and Max plans).
- On **Team / Enterprise**, an admin enables *Code execution* + *Skills* for the workspace first.

### Step 3 — Add a skill and use it

1. **Download a skill** — grab its `.zip` from the table below (one click).
2. In Claude, go to **Customize → Skills → ＋** and **upload the `.zip`**. Toggle it **on**.
3. **Say the trigger phrase** in any chat — e.g. *"Map the market for commercial cleaning in Melbourne."*

That's it. Claude now runs that whole workflow for you, pausing at each gate to check in.

> **New here? Install these three first:** **map-the-market**, **icp-review**, and **campaign-build** (in the table below). They cover most of the work.

---

## 📦 The skills

Every skill is consultative by design — it **reviews your setup, flags what's weak, suggests improvements, and confirms with you before spending credits.** (That behaviour comes from the **`kolvera-guidelines`** skill — upload it once and it applies across all of them.)

### 🟢 Core skills — *work for any vertical (recruitment, sales, IT/MSP, HR, facilities…)*

| Skill | Say this to Claude | What it does | Get it |
|---|---|---|---|
| **map-the-market** | *"Map the market for [your niche]"* | The full pipeline end-to-end: ICP → Deep Research → job scraping → contacts → hot lists. ~30–60 min with approval gates. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/map-the-market.zip) |
| **icp-review** | *"Review my ICP"* | Audits your targeting — tightens industries, sharpens exclusions, fills gaps. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/icp-review.zip) |
| **deep-research** | *"Run deep research on my ICP"* | Discovers companies you didn't know existed, with smart stop rules so you don't waste credits. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/deep-research.zip) |
| **job-scrape** | *"Scrape job boards for my ICP"* | Runs SEEK / LinkedIn / Indeed scrapes, filters results, finds who's actively hiring. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/job-scrape.zip) |
| **contact-enrichment** | *"Enrich contacts for my ICP"* | Finds decision-makers at your targets, with verified emails and phone numbers. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/contact-enrichment.zip) |
| **prospect-sort** | *"Sort my new contacts"* | Classifies contacts into prospects, candidates, and junk; links them to the right profiles. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/prospect-sort.zip) |
| **process-scrape** | *"I just scraped 50 contacts from LinkedIn"* | Dedupes, classifies by title, finds emails, builds hot lists. Works for prospect *and* candidate scrapes. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/process-scrape.zip) |
| **hot-list-build** | *"Build hot lists for my ICP"* | Segments prospects into S/A/B tiers, ready for campaigns. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/hot-list-build.zip) |
| **campaign-build** | *"Build a campaign for [hot list]"* | Multi-step email campaigns with the T.I.P.S. framework — copy, inboxes, enrolment, activation. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/campaign-build.zip) |
| **campaign-health** | *"Check my campaigns"* | Fast health check — flags bounces, low opens, inbox problems, dead campaigns. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/campaign-health.zip) |
| **morning-briefing** | *"Morning briefing"* | Daily digest: meetings, replies, follow-ups, pipeline alerts, top 3 priorities. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/morning-briefing.zip) |
| **weekly-review** | *"Weekly review"* | End-of-week synthesis: what moved, what's hot, where to focus next week. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/weekly-review.zip) |

### 🧑‍💼 Recruitment

| Skill | Say this to Claude | What it does | Get it |
|---|---|---|---|
| **rmp-campaign** | *"Take [candidate] to market"* | Full Reverse Market Profile workflow: create profile → match companies → find prospects → build campaign → activate. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/rmp-campaign.zip) |
| **candidate-pipeline** | *"Move [candidate] to [stage]"* | Manage candidate stages, grades, notes, and next actions across your pipeline. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/candidate-pipeline.zip) |

### 💼 B2B Sales

| Skill | Say this to Claude | What it does | Get it |
|---|---|---|---|
| **deal-pipeline** | *"Review my pipeline"* | Flags stale prospects, surfaces next actions, recommends adjustments. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/deal-pipeline.zip) |
| **company-research** | *"Research [company name]"* | Deep dive: AI research, decision-makers, hiring signals, buying triggers, recommended approach. | [⬇ Download](https://github.com/kolverahq/kolvera-skills/releases/latest/download/company-research.zip) |

> **Don't want to pick?** [⬇ **Download all skills**](https://github.com/kolverahq/kolvera-skills/releases/latest/download/kolvera-skills-all.zip) (one zip per skill inside — upload the ones you want). Also grab **[`guidelines.zip`](https://github.com/kolverahq/kolvera-skills/releases/latest/download/guidelines.zip)** so Claude stays consultative across all of them.

*More vertical packs (IT/MSP, HR consulting, facilities) are on the way — the core skills already work for those today.*

---

## 💡 Get better results

Add the **Kolvera MCP Prompt Guide PDF** to your Claude **Project knowledge** (next to the skills). It gives Claude the full tool reference (all 179 tools), polling timings, and known workarounds, so workflows run more reliably.

→ Download it from **[kolvera.io/guide/claude](https://kolvera.io/guide/claude)**.

If you have the **T.I.P.S. Cold Email Playbook** PDF, add that too — it powers the email framework in `campaign-build`.

---

## 💳 What things cost

Most actions are free. Credits are only spent on data and AI generation, and **every skill confirms with you before spending them.**

| What | Cost |
|---|---|
| Generate an ICP (AI) | 2 credits |
| Deep Research — first run | 3 credits |
| Deep Research — expand | 2 credits |
| Contact found *with verified email* | 2 credits |
| Phone number found | 6 cr direct dial · 2 cr company line · 0 cr if already on file or BYOK |
| Research one company | 1 credit |
| Market / Role Intelligence report | 10 credits (Pro & Agency) |
| Job board scraping | Uses your monthly scrape allowance (not credits) |
| Sorting, hot lists, campaigns, reviews, pipeline | Free |

---

## ✅ Requirements

- A **Kolvera account** on any plan — [kolvera.io](https://kolvera.io)
- **Kolvera connected to Claude** (Step 1 above)
- **A Claude plan that supports Skills + Connectors** — Free works for getting started; Pro/Max/Team give you more connectors and usage

---

## 📖 Walkthroughs

The [`examples/`](examples/) folder has plain-English, step-by-step runs:
- **[first-icp-in-15-minutes.md](examples/first-icp-in-15-minutes.md)** — your first target market from scratch
- **[recruitment-quickstart.md](examples/recruitment-quickstart.md)** — end-to-end recruitment workflow
- **[b2b-sales-quickstart.md](examples/b2b-sales-quickstart.md)** — end-to-end B2B sales workflow

---

## 🛠 Advanced — Claude Code & power users

Prefer the filesystem? Each skill is a folder with a single `SKILL.md` inside. Clone the repo and drop the folders into your skills directory:

```bash
git clone https://github.com/kolverahq/kolvera-skills.git
cp -r kolvera-skills/core/* kolvera-skills/recruitment/* kolvera-skills/b2b-sales/* ~/.claude/skills/
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
