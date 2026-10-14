# Public skills refresh — 14 October 2026

Status: implemented; independent review and current-head CI/public release pending.

## Scope and evidence
- Public repository base: 30bca2a5b4adb7b0425090764e478bf492d125bc.
- Product compatibility snapshot: 270642ad3f14bd368e28615d5f94c3df456ccc0b; production prices and paused enrolment checked separately.
- Only Kolvera-related workflows. Claude and GPT-based clients share standard folders; installation/capability paths documented separately.
- 21 skills: existing 18 plus recruitment-intake, candidate-submission and meeting-follow-up.
- Kolvera-linked screening, Float and audience-safe submission references added. No private Zionic identities, candidate records, rates, tax/margin defaults or account credentials included.
- Static validation only. No paid enrichment, sends, live account mutations or claimed live Claude/ChatGPT runtime tests.

## Findings
| ID | Implementation | Verification |
|---|---|---|
| F01 | Paid-job terminal receipts, confirmed-unstarted retries, no uncertain replay | Pre-fix and mutation guards; reviewed contract |
| F02 | Paused enrolment supported without resuming | Pre-fix guard and current production source |
| F03 | Correct RMP/candidate linkage; enrol, preview, explicit launch | Current exposed campaign schemas and review |
| F04 | Scoped private/legacy Float branching and staged disclosure | RMP Float reference and shared contract |
| F05 | report_id expansion, smart routing, qualified-fit stop logic | Tool-parameter fixture and bad-argument mutation |
| F06 | Updated prices and cache distinctions | Canonical table versus dated production snapshot |
| F07 | Every standalone folder includes operations reference | Source-sync and extracted-ZIP validation |
| F08 | Explicit tips/float/freeform; step_hints limited to freeform | Current campaign contracts |
| F09 | Lifetime totals separated from period evidence | Reporting workflow review |
| F10 | Desk/candidate-specific market criteria; legitimate leadership overlap retained | Independent review correction |
| F11 | Current Claude and OpenAI setup, platform distinctions | Official documentation checked 14 October |
| F12 | Stdlib validation, CI, deterministic ZIPs, manifest/checksums | Regression, tamper, path and standalone tests |
| F13 | Concise orchestration and generated shared invariants | One canonical operations source; no sibling dependency |

Additional verified correction: retired/unavailable initial RMP creation tools removed. Existing profile read/refresh is supported; initial creation gets an explicit app handoff when no tool exists. Unknown logical tool tokens and call examples now fail validation.

Independent work: validation builder GPT-6.1 Sol high; Zionic read-only workflow review GPT-6.1 Sol medium; critical reviewer GPT-6 Astra high. Lead GPT-6.1 Sol medium. No automatic model switch claimed.

## Independent review corrections
Critical review identified and corrected legitimate executive-title overlap, generation-based Float mode selection, separate native preview/commit UUIDs, standalone Float reference, and offer_presented stage spelling. A dated offline fixture remains explicit; no claim of live client/account tests. Final correction verification, CI and publication evidence follow in the release receipt.
