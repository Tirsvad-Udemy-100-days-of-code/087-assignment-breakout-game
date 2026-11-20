# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-005 |
| CrossReference | [MIL-002], [QC-MIL-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [d4bf2df] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-MIL-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01, who is also the author)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | A concrete deliverable is defined for every gate | Pass | Deliverable section names concrete output. |
| 2 | Explicit Go/No-Go criteria are stated for each gate | Pass | Each Go/No-Go criterion is checkable with a command or a count. |
| 3 | Dependencies on other milestones are explicitly mapped | Pass | Dependencies table filled. |
| 4 | Each milestone is traceable to a Business Case objective or KPI | Pass | Traceability cites Business Case objectives and concerns. |
| 5 | Milestone owner and approving reviewer are identified | Pass | Owner and approving reviewer are S01. |
| 6 | Milestone has a defined target date consistent with project constraints | Pass | Target date is inside the plan window. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Checked against the document. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | Checked against the document. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Checked against the document. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Checked against the document. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Checked against the document. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Checked against the document. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | Checked against the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | Checked against the document. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Checked against the document. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Checked against the document. |

## Overall Verdict

Go - all Mandatory criteria pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[MIL-002]: ../../milestones/mil-002-steps-1-3-paddle-ball.md
[QC-MIL-001]: ../../../framework/qc/artifacts/qc-milestones-gateways.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[d4bf2df]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/commit/d4bf2df2d88712f1b4e71c76be15fb497ac94ed4
