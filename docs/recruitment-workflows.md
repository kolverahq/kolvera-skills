# Kolvera recruitment workflow alignment — 14 October 2026

Scope: reusable Kolvera-connected workflows found in current Zionic recruitment practice. No private candidate/client data, account credentials, internal commercial defaults or branded legal masters are included.

Read-only source review used the Zionic recruitment repository at commit 35f7abc plus current working workflow artifacts. Role-onboarding, candidate-information-pack and consultant starter v1.1 were uncommitted working artifacts, not proof of a shipped product. Existing call/Float/intake runbooks were also inspected. All named native tool parameters were checked against exposed Kolvera schemas; availability still depends on account/scopes.

| Workflow | Included here | Boundary |
|---|---|---|
| Role intake/calibration | recruitment-intake: client job, source-backed brief, review/revision, linked desk | Commercial contracts, invoices and staff provisioning are outside this skill |
| Evidence-based screening | candidate-pipeline screening reference | Human conversation/credential verification remain external; no protected-trait inference |
| Scoped representation | candidate-submission consent/version checklist and optional e-sign lifecycle | Approved jurisdiction-specific master required; no generic legal contract authored |
| Shortlist/submission | candidate-submission: consistent criteria, duplicate/history review, material/recipient checks, receipt then stage | Shortlist mutation does not itself send documents |
| Interview preparation | candidate-submission supporting procedure | Scheduling uses available authorised connector/manual route; no invented native interview automation |
| Meeting follow-through | meeting-follow-up with source-specific native/Fathom effects and receipts | Native private close-out and shared Fathom processing are not interchangeable |
| RMP map/readiness audit | RMP Float reference uses diagnose_rmp and source checks | No hardcoded customer/sector thresholds |
| Float privacy/commercial truth | RMP plus shared contract | Private pay and internal margin stay private; client charge comes from user's approved terms |
| Candidate/role material | candidate-submission document reference | Supports Kolvera submission; not a standalone design or calculator skill |
| Desk orientation/resume | shared Operations contract and map/work-the-desk | No automatic account provisioning, workspace merge or paid activation |

Cross-cutting: separate candidate lifecycle from client-job outcomes; preserve account/owner scope; distinguish rejection from explicit no-further-outreach; use stop_contact_outreach only for the latter and inspect its result. Do not bypass an opt-out by switching channel.

Compatibility: one standard SKILL.md workflow, complete relative references, model-neutral language, client-specific setup in README. No private filesystem paths or Zionic identity are required by installed skills.
