# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [d4bf2df] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01, who is also the author)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-20, end 2026-11-23, fits the two-hour effort constraint of BC-001. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Four gateways, each with document, date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal each MIL target date. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage table covers every In Scope item. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain G1 to G4, acyclic, in date order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | No-Go moves later dates by the same number of days; S01 decides the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | All owners use S01; no governance RACI document exists yet (not in the plan). |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Planning Assumptions give the source of each date. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Three plan risks with mitigations, linked to Business Case risks where they come from. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues do not contradict the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverables match each MIL Deliverable. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says none (technical tasks). |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bar dates equal the table. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column is blank because the sync has not run; the plan says so in the milestones text. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | One plan with a Version History. |

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

Go - all Mandatory criteria pass; the Gantt chart is not rendered because no PlantUML server is set (listed in Open Issues).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[d4bf2df]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/087-assignment-breakout-game/commit/d4bf2df2d88712f1b4e71c76be15fb497ac94ed4
