# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-002 |
| CrossReference | [SA-001], [QC-SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [d4bf2df] |

---

## Artifact Under Review

- Instance reviewed: [SA-001]
- Checklist used: [QC-SA-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01, who is also the author)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Power/Interest grid is filled for every stakeholder, with no gaps or unclassified entries | Pass | S01 to S03 all have power, interest and quadrant. |
| 2 | Each stakeholder is assigned a unique, stable ID (e.g. S01-S11 style) reusable for RACI assignments in other artifacts | Pass | Stable IDs S01 to S03. |
| 3 | Roles and organizational context are defined with explicit Power and Interest levels, not just narrative description | Pass | Role and organisation given with levels. |
| 4 | Communication needs (channel, frequency, deliverable type) are mapped to project phases or milestones | Pass | Communication table CR-001 to CR-004 tied to milestones. |
| 5 | Conflicting stakeholder interests are identified with documented mitigation or resolution strategies | Pass | Three conflicts, each with a mitigation. |
| 6 | Stakeholder concerns are explicitly traced to Business Case objectives | Pass | Business Goal Alignment table maps each concern to O1 to O6. |
| 7 | Primary concerns are expressed in both business language and a recognized quality-attribute mapping (e.g. FURPS+) | Pass | Concerns CN-001 to CN-007 carry a FURPS+ attribute. |
| 8 | Document is understandable and navigable by non-technical stakeholders reviewing their own entry | Pass | Short and plain. |
| 9 | Every concern has a stable ID (`CN-NNN`) in the concern register, with the stakeholder who raised it; IDs are never renumbered or reused | Pass | Every concern has a CN ID and a stakeholder. |

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

[SA-001]: ../../stakeholder-analysis.md
[QC-SA-001]: ../../../framework/qc/artifacts/qc-stakeholder-analysis.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[d4bf2df]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/commit/d4bf2df2d88712f1b4e71c76be15fb497ac94ed4
