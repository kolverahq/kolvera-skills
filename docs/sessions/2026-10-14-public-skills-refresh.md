# Kolvera public skills refresh — 14 October 2026

**Shipped:** v1.5.0; PR #1 merged as bcc5c4e08f4d587cc42dd45d26c5157d24f19abb.
**Migration:** None; public skills repository only.
**Status:** Shipped and verified.
**Tags:** skills, recruitment, documentation, security

All 13 audit findings were fixed across the existing 18 workflows. Three Kolvera-connected workflows were added: recruitment-intake, candidate-submission and meeting-follow-up. Claude and GPT/Codex setup paths are documented separately, while workflow instructions use standard SKILL.md folders and bundled references. Current Zionic recruitment practices informed screening, consent, shortlist, Float and meeting references; no private account data, identities or commercial defaults were published.

Validation: 32 stdlib tests passed; 21 standalone skill folders, ZIP payloads, shared references, manifest and SHA256 checksums passed. Independent critical review corrections were applied and re-reviewed. PR CI 38551527256 passed for head746ff64ae4939960a0800ca6e831580c6b9d2bb1; main CI38551629879 passed for the merge commit. All24 public release assets were downloaded and validated against source. Static fixtures do not prove live account capability or client execution; no paid calls, live CRM writes or outbound sends were used in testing.

Release: https://github.com/kolverahq/kolvera-skills/releases/tag/v1.5.0 . Detailed ledger: [remediation](../2026-10-14-remediation.md). Canonical project memory was updated and mirrors reported HEALTHY. Implementation, validation and product-source audit worktrees/branches were retired; shared dirty Kolvera and Zionic trees were untouched.

**Open / owed:** No implementation or release work remains. Previously uploaded/manually copied skills require deliberate reinstall with local customisations reviewed; installed copies were not overwritten. Future live-client validation is outside this completed static/package refresh.
