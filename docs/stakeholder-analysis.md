# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version; reviewed Go in RC-002, stand-in review, not independent | pending |

---

## Purpose

The analysis names the people who have power over or interest in the Breakout project, so that owners, reviewers and the people the documents are written for are cited by stable IDs. It uses the power/interest grid and maps each concern to a FURPS+ attribute.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A finished, well-documented assignment that shows what was learned |
| S02 | Udemy coursists | Course participants who share and compare code | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | MEDIUM | Keep Informed | A clear description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews every artifact and accepts the plan. Power and interest are both high.
- **Keep Informed (S02, S03):** they cannot change the project, but the README and the wiki are written for them, so they are informed through those documents. S02 has high interest because the repository is built for course participants; S03 has medium interest because visitors browse once.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The game must work like the original Breakout and finish the assignment | Functionality |
| CN-002 | S01 | Each lecture step is documented so the learning is visible | Supportability |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Supportability |
| CN-004 | S02 | README tells how to create a `.venv`, run the game and run the tests | Usability |
| CN-005 | S03 | The repository has a clear description, topics and README | Usability |
| CN-006 | S03 | Nothing has to be installed to run the game except Python | Implementation constraint |
| CN-007 | S02 | The wiki is available in English, Danish and Bahasa Malaysia | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat | Per milestone | Summary of pull requests, reviews and stand-in decisions | Every milestone |
| CR-002 | README | Once per release | Run instructions and a screenshot per step | MIL-002, MIL-003 |
| CR-003 | Wiki | Once per release | What was gained in each step, in three languages | MIL-004 |
| CR-004 | Repository page | Once | Description and topics | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Assignment's names against a clean layered design (CN-003 against CN-005) | S02, S03 | Use the assignment's names for the public classes (`Paddle`, `Ball`, `Bricks`, `Scoreboard`) and keep the rules in separate pure modules behind them |
| A short README against every step documented (CN-004 against CN-002) | S02, S01 | The README holds one screenshot and one line per step; the explanation is in the wiki |
| No dependencies against a screenshot tool being needed (CN-006) | S03, S01 | The screenshot tool lives only in the Docker image used for development, not in the project's dependencies |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | O1 ([BC-001]) |
| S01 | CN-002 | O3 ([BC-001]) |
| S02 | CN-003 | O1, O2 ([BC-001]) |
| S02 | CN-004 | O5 ([BC-001]) |
| S02 | CN-007 | O4 ([BC-001]) |
| S03 | CN-005 | O6 ([BC-001]) |
| S03 | CN-006 | O5 ([BC-001]) |

No use case is modelled: the game is a learning exercise with one player, and every task is a plain technical task (see the Project Plan, Open Issues).

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Pending review | 2026-11-20 |

---

[BC-001]: ./business-case.md
