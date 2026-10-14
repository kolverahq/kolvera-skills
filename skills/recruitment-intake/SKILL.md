---
name: recruitment-intake
description: Turn a reviewed recruitment brief and authorised source evidence into a Kolvera client job, role brief and linked role desk.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Kolvera recruitment intake

Read [Operations contract](references/operations.md). This skill creates/reviews Kolvera records; it does not approve commercial contracts, send invitations or provision staff accounts.

1. Confirm workspace, client company, hiring contact and desk. Read `list_client_jobs` and `get_client_job` before creating duplicates. Resolve direct-client versus platform assignment and any restrictions on source use.
2. Reconcile brief, authorised meeting notes/transcript, email and calibration. Separate confirmed requirements, employer claims, proposed criteria and contradictions. Identify outcomes, responsibilities, required evidence, location/work pattern, employment type, interview stages, currency and salary basis. Do not copy internal candidate calibration into public job description.
3. Use `create_client_job` or `update_client_job` for authorised facts. Pass explicit company/currency/basis/desk where supported. Do not invent fee percentages, replacement terms or salary from private candidate pay. Read back the resulting record.
4. Inspect `list_client_job_role_brief_sources` and `list_client_job_role_briefs`. Generate with `generate_client_job_role_brief` using only supported source kinds and authorised IDs/content. Native meeting-source drafts may be private; preserve returned mode and scope.
5. Review exact brief/revision with `review_client_job_role_brief`; use `revise_client_job_role_brief` for corrections. Explain coverage/conflicts; do not set acknowledge flags merely to get past a gate. `approve_client_job_role_brief` requires user scope covering approval of that exact version.
6. Create/link a role desk with `create_client_job_role_desk` only when requested and supported by the reviewed job. Creation does not authorise paid research, scraping or outreach.
7. Produce a role summary from the reviewed Kolvera record and list unresolved questions. Keep client/candidate-facing facts separate from internal notes. Report company/job/brief/desk IDs, version, approvals performed and next action.

If a source, legal/commercial step or connector is unavailable, leave it pending explicitly. No invented native contract, invoicing or document-generation tool.
