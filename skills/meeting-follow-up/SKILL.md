---
name: meeting-follow-up
description: Review Kolvera meeting or conversation evidence, preview supported post-call processing and prepare scoped notes, actions and follow-up.
metadata:
  last_verified: "2026-10-14"
  compatible_tools: "Kolvera MCP; inspect live capabilities"
---

# Kolvera meeting follow-up

Read [Operations contract](references/operations.md). Select account, contact and actual meeting/conversation first. Recording and disclosure consent are distinct from permission to update CRM.

1. Find native notes with `list_meeting_notes`, then `get_conversation` for authorised summary/transcript. Follow next_after/version/has_more when reading pages; partial transcript is not full evidence. Speaker labels are observations, not verified contact identity.
2. Draft factual summary, decisions, corrections and actions with owner/due date. Separate quotes, stated facts and interpretation. Keep private candidate/client information out of broadly shared notes.
3. Select only the supported source mode of `process_post_call`:
   - Native: source_type="native", conversation_id, contact_id and stable request_id UUID; omit meeting_id. Requires conversations:read and contacts:write. dry_run=True creates a content-free receipt and transient preview; preview retries can return preview_not_retained. Real processing stores an owner-private close-out plan, not shared notes/actions or sends. Preview and real processing have different request identities. After a successful preview and explicit approval, allocate a separate commit UUID for dry_run=False; never change dry_run under the preview UUID. For an uncertain preview or commit, reuse that operation's original UUID only; do not create another request automatically.
   - Fathom: source_type="fathom" with meeting_id and no native fields, only for an actual connected Fathom BD/client meeting. Candidate meetings are not supported by that branch. dry_run=True previews. Authorised real processing appends shared notes/outcome, queues follow-up and next action; approving queued email sends.
4. Explain proposed effects and obtain any missing scope before real processing. No fallback between modes. Missing transcript, scope, capability or conflicting identity blocks that step.
5. Read back results/receipt and review queued drafts. A general meeting wrap does not authorise approving a sending action. Native private close-out is not proof shared CRM was updated; any later publication/mutation requires supported reviewed controls.
6. Report source ID, coverage/version, performed changes, queued versus sent state, unresolved evidence and next owner/date.

For an unsupported candidate call or manual note, draft a summary and use only verified authorised record-update tools; do not force it into the BD/client Fathom branch.
