# MIL-004 G4 Wiki and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed Go in RC-007, stand-in review, not independent | pending |

---

## Purpose

Decides whether the project can be called finished: the wiki explains what each step gave in three languages, the reflection is written and the repository passes its last scan.

## Deliverable

A wiki in `docs/wiki/` in English, Danish and Bahasa Malaysia with the same page set (home, getting started, one page per step with its screenshot and what was gained, reflection), a sidebar, and a final README check.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every English wiki page has a Danish (`-da`) and a Malay (`-ms`) page | Met | Not met |
| 2 | Each of the seven step pages shows its screenshot and a "What we gained" section | Met | Not met |
| 3 | The wiki is reviewed against `QC-WIKI-001` with a Go | Met | Not met |
| 4 | `bash framework/scripts/check-readme.sh`, `check-languages.sh` and `check-plan.sh` pass | Met | Not met |
| 5 | The final opengrep scan reports 0 findings of severity error | Met | Not met |
| 6 | Pull request opened with `Closes #N` lines for every task, and its checks are green | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The finished game and all seven screenshots exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3, O4 | [BC-001] Objectives |
| CN-002, CN-007 | [SA-001] concern register |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-23 — one day after G3.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | Write `Home`, `Getting-Started`, `Step-1` to `Step-7` and `Reflection` in English, each step page with its screenshot, what was built and a "What we gained" section. English is the authoritative text. | No | [BC-001] |
| 2 | Write the Danish wiki | Translate every English page to Danish (`-da`), same page set, with the language line at the top of each page. | No | [BC-001] |
| 3 | Write the Bahasa Malaysia wiki | Translate every English page to Bahasa Malaysia (`-ms`), same page set, with the language line at the top of each page. | No | [BC-001] |
| 4 | Write the sidebar | Add `_Sidebar.md` as `framework/process/wiki.md` describes: the English page list once and a Languages section last. | No | [BC-001] |
| 5 | Write the reflection | Write the assignment reflection (how the project was approached, what was hard and easy, the biggest learning, what would change) as the `Reflection` page in three languages. | No | [BC-001] |
| 6 | Review the wiki against QC-WIKI-001 | Review the wiki, write the `RC-*` record and fix any finding before the pull request. | No | [BC-001] |
| 7 | Final checks and scan | Run the framework checks and the opengrep scan on the whole repository, update the README appendix and confirm the issues and milestones on the git host are closed. | No | [BC-001] |

---

[BC-001]: ../business-case.md
