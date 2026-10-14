# Kolvera Skills for Claude and GPT-based clients

Reusable workflows around Kolvera MCP tools: build a market, work a desk, manage recruitment and prepare reviewed outreach. Standard `SKILL.md` folders work with compatible Agent Skills hosts. The workflow is shared; installation and available tools depend on the client and connected account.

**Verified:** 14 October 2026. Tool/cost snapshot: [contracts/kolvera.json](contracts/kolvera.json). It is an offline compatibility fixture, not a live capability guarantee.

## Connect Kolvera first

Use the authenticated Kolvera MCP connection: `https://mcp.kolvera.io/mcp`. Follow the [Kolvera connection guide](https://www.kolvera.io/guide/claude) and the current instructions for your host. Review workspace identity and granted scopes before running a workflow.

Tool names in skills are logical names; a client may prefix them. Inspect live tool schemas. If an account lacks a capability, stop that step and explain the gap instead of inventing calls.

## Install for your client

### Claude web / Desktop

Enable Code execution and Skills where required, then upload an individual skill ZIP through Customize → Skills. Skills are available on Free, Pro, Max, Team and Enterprise subject to workspace controls. Team/Enterprise policy can restrict uploads or sharing.
Use [Anthropic's current Skills instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude) for menus, provisioning and supported Claude Code account-skill loading.

### Codex

Copy each complete skill folder, including `references/`, into your user `~/.agents/skills/` or project `.agents/skills/` location. Connect Kolvera separately through the client's supported authenticated MCP setup. Do not paste a Claude configuration file into Codex or overwrite another installed skill without reviewing local customisations.
See [OpenAI's skill setup](https://learn.chatgpt.com/docs/build-skills). Account/plugin-provisioned skills and manually copied local folders are different installation paths.

### ChatGPT and other GPT-based hosts

Where your ChatGPT environment supports Skills or an approved MCP-backed plugin, package/install the complete folders using that environment's documented flow and connect the authorised Kolvera app. These standalone ZIPs are not themselves a published ChatGPT plugin.
For environments without native skill loading, the instructions can be used as an explicit workflow reference, but execution still requires exposed Kolvera tools. Uploading a file alone does not create a connector or grant tool access.
See [OpenAI Skills concepts](https://developers.openai.com/plugins/concepts/skills) and [API Skills](https://developers.openai.com/api/docs/guides/tools-skills) for supported developer integration. Do not assume Claude's ZIP-upload menu exists in every GPT client.

## Choose a workflow

Download links use the latest reviewed GitHub release. Each ZIP contains one complete skill folder and its required references. The all-skills bundle contains individual ZIPs; extract it before installing each.

| Skill | Example request | Download |
|---|---|---|
| map-the-market | Map the market for this niche and region | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/map-the-market.zip) |
| icp-review | Review why my desk is noisy | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/icp-review.zip) |
| deep-research | Discover companies within this credit cap | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/deep-research.zip) |
| job-scrape | Run this desk's saved job-board config | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/job-scrape.zip) |
| company-research | Research this company in Kolvera | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/company-research.zip) |
| contact-enrichment | Find these buyer titles at selected companies | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/contact-enrichment.zip) |
| prospect-sort | Classify this reviewed contact batch | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/prospect-sort.zip) |
| process-scrape | Reconcile and organise this imported batch | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/process-scrape.zip) |
| hot-list-build | Segment these prospects into useful lists | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/hot-list-build.zip) |
| candidate-pipeline | Record screening evidence and next action | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/candidate-pipeline.zip) |
| deal-pipeline | Review prospects and overdue actions | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/deal-pipeline.zip) |
| recruitment-intake | Turn this approved brief into a Kolvera client job | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/recruitment-intake.zip) |
| candidate-submission | Review this shortlist and submission authority | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/candidate-submission.zip) |
| meeting-follow-up | Review this Kolvera conversation and next actions | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/meeting-follow-up.zip) |
| rmp-campaign | Prepare this screened candidate's reverse market | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/rmp-campaign.zip) |
| campaign-build | Prepare a reviewed campaign for this audience | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/campaign-build.zip) |
| campaign-health | Check campaign and inbox evidence | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/campaign-health.zip) |
| work-the-desk | Triage this desk's New Leads | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/work-the-desk.zip) |
| morning-briefing | Show today's Kolvera priorities | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/morning-briefing.zip) |
| weekly-review | Review this week's evidenced activity | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/weekly-review.zip) |
| guidelines | Explain Kolvera workflow boundaries | [ZIP](https://github.com/kolverahq/kolvera-skills/releases/latest/download/guidelines.zip) |

[All skills bundle](https://github.com/kolverahq/kolvera-skills/releases/latest/download/kolvera-skills-all.zip)

Only Kolvera-related skills are included. Recruitment references support Kolvera records and tools; they are not general agency administration, marketing, legal advice or calculator skills. Planned workspace teams/consolidation are not exposed as shipped workflows.

## Budgets, privacy and sending

Every skill includes its own Operations contract, so a standalone installation retains job/retry, privacy and approval rules without relying on a sibling skill being loaded.
Authorisation persists within its stated scope. Agree paid caps, inspect actual returned cost and stop before exceeding them. Drafting, reviewing or triaging does not authorise external sends.

Verified credit snapshot:
- Deep Research: fresh 6, expansion 4; smart desk mode returns actual mode/cost/reason.
- Found verified-email contact: 2.
- Phone: fresh direct 2, fresh company line 2, cached direct 2, cached company line 1; already-present/BYOK paths differ.
- Market/Role Intelligence: 23.
- Company AI research: 1.

Use released pricing and current tool responses when this snapshot ages. Do not treat lifetime campaign totals as weekly metrics or uncertain async jobs as completed.

## Maintainers

No new dependencies. Python 3.13:
```bash
python scripts/sync_references.py --check
python -m unittest discover -s tests -v
python scripts/validate_release.py --root .
python build-release-zips.py --root . --output dist
python scripts/validate_release.py --root . --archives dist
```

Edit the canonical `contracts/operations.md`, then deliberately sync with `python scripts/sync_references.py --write`. CI checks the source, tool/cost fixture, references, pre-fix regressions, standalone archives and checksums. Refresh the snapshot from reviewed current tool schemas/product pricing; CI cannot prove live account permissions.
Release from a reviewed commit and tag. Publish per-skill ZIPs, bundle, manifest and checksums together. Verify downloaded assets. Source changes do not update previously downloaded or manually copied skills automatically; reinstall/review the new version in each host.

[Audit and remediation ledger](docs/2026-10-14-audit.md) · [Recruitment workflow alignment](docs/recruitment-workflows.md)

MIT. See [LICENSE](LICENSE).
