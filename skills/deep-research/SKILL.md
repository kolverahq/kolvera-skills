---
name: deep-research
description: Discover companies for a Kolvera desk or candidate market using paid Deep Research, with budget, polling and evidence-based stop rules.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Deep Research

Read [Operations contract](references/operations.md) before paid work. This workflow works with Claude or GPT-based clients exposing the required tools.

1. Identify the desk with `list_icp_profiles` and `get_icp_profile`, or the candidate market. Review criteria and existing reports with `list_research_reports`. Agree a discovery budget; do not start another job for an already running report.
2. Call `trigger_deep_research(icp_id=...)` for a desk. Precision may be strict, balanced or broad. Let stored criteria supply the brief unless the user requests a different one.
3. Retain returned report_id and inspect mode/cost/reason. Smart mode may expand an existing desk report rather than purchase fresh discovery. A deliberately fresh run uses mode="fresh"; bare briefs and candidate-only runs are fresh.
4. Poll `get_research_report(report_id=..., fields="status")` at the returned hint (normally no faster than 30 seconds). Fetch fields="full" after completion. Expansion may take several minutes. A stall requires diagnosis of that report, not buying another run.
5. Explain verified-fit desk additions separately from report novelty and net CRM creations. Review industry/location/size fit; propose criteria changes before further spending.
6. For another approved round, call `expand_deep_research(report_id=...)` using the returned report ID. Keep the same polling and budget ledger.
7. Honour expansion_history.recommendation: stop needs a revised brief or new evidence; review means mapping evidence is incomplete. Do not justify another run from raw novelty alone. Stop at the agreed cap or diminishing qualified additions, whichever comes first.

Close with report ID, actual spend, qualified additions, existing-workspace matches, evidence limitations and next proposed action. Verify desk company counts through the profile rather than assuming report growth equals CRM growth.
