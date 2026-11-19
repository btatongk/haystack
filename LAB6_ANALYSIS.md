# Lab #6 - Investigation Record

**Team / student(s):** Joss / btatongk
**Mode:** Individual
**Approved upstream project:** https://github.com/deepset-ai/haystack
**Fork / working branch:** https://github.com/btatongk/haystack/tree/semester-investigation
**Original Lab #5 version:** 104a83f8799b1b8d9d18a88eb9a08305133aea2d
**Lab #6 pre-refactoring baseline:** 104a83f8799b1b8d9d18a88eb9a08305133aea2d (https://github.com/btatongk/haystack/commit/104a83f8799b1b8d9d18a88eb9a08305133aea2d)

> Keep this file short and evidence-based. Replace the placeholders as you go. Every analysis/test link must point to your **fork's GitHub-visible results**. Do not submit unsupported local-only tool screenshots.

## Task 1 - Stakeholder, GQM, and Code Smell Selection

**Selected stakeholder and exact fictional concern from handout:** "Our software keeps evolving. Future contributors need to understand and modify its components, but certain design choices might make that work unnecessarily difficult. Please investigate possible code smells, identify maintainability concerns worth addressing, and demonstrate a focused improvement without changing the software's intended behavior."

**GQM goal:** Analyze **handwritten Python implementation and test-adjacent source in this Haystack fork** for the purpose of **identifying and reducing maintainability concerns** with respect to **code size, responsibility, parameter complexity, and duplicated implementation** from the viewpoint of **Alex, the Software Maintainer**, in the context of **the future evolution of this public Haystack branch**.

| Initial question | Question wording | Relevant metric(s) / observation(s) | Why useful? |
|---|---|---|---|
| **Q1** | Which handwritten Python entities exhibit symptoms that may make them harder for future contributors to understand or change? | Ruff complexity/parameter findings, Radon-like complexity indicators if available, source length, responsibility count, and manual source inspection | Connects scanner signals to concrete source locations and distinguishes plausible concerns from ordinary warnings. |
| **Q2** | Which duplicated or excessively complex implementation candidates offer a defensible, behavior-preserving refactoring opportunity with acceptable risk? | Duplicate fragment count and size, function/class LOC and cyclomatic complexity, nearby test coverage/check evidence, and change scope | Supports prioritization and a small refactoring plan rather than selecting warnings only by severity or count. |

**Code-smell types chosen from the lecture:** The following targets are hypotheses to investigate, not assumptions that they exist.

| Smell type | Lecture slide(s) | Why relevant to our GQM? | How we plan to investigate it (tool/rule/metric/inspection) |
|---|---|---|---|
| 1. Long Method | Lecture catalogue, slide 32; analysis detail on slides 34-106 as applicable | Methods that combine many steps can be harder to understand, test, and change. | Ruff complexity rules and manual LOC/control-flow review of handwritten Python entities. |
| 2. Large Class / Overloaded Class | Lecture catalogue, slide 32; analysis detail on slides 34-106 as applicable | A class with too many responsibilities can increase the risk and effort of later changes. | Source inspection of large classes and their responsibilities, supported by LOC/class metrics if the chosen workflow provides them. |
| 3. Long Parameter List | Lecture catalogue, slide 32; analysis detail on slides 34-106 as applicable | A large parameter list can make call sites harder to understand and modify correctly. | Ruff parameter-count diagnostics and manual call-site/source review. |
| 4. Duplicated Code | Lecture catalogue, slide 32; analysis detail on slides 34-106 as applicable | Verified repeated implementation may create synchronization and evolution costs. | jscpd on GitHub Actions, followed by manual inspection of reported duplicate fragments. |

**Primary GitHub-integrated tool:** [Ruff on GitHub Actions](https://docs.astral.sh/ruff/) / [Haystack setup guide tool options](https://github.com/deepset-ai/haystack)

**Complementary tool (only if needed):** [jscpd](https://github.com/kucherenko/jscpd) on GitHub Actions

**Why these tools match our questions and selected smells:** Ruff can provide metric/rule indications for complexity and parameter lists in handwritten Python, but source inspection is still required to judge Long Method and Large Class. jscpd directly measures duplicate fragments; it does not establish that removing every duplicate is safe or worthwhile.

## Task 2 - Detect and Investigate Code Smells

**Analysis configuration:**

- Fork branch and **baseline SHA**: `semester-investigation`, 104a83f8799b1b8d9d18a88eb9a08305133aea2d
- Source directory/directories analyzed: `haystack/` handwritten Python package (initially; refine after baseline workflow setup)
- Exclusions (generated/test/vendor/weight data, etc.): tests, notebooks, Cython, third-party/generated code, unless a specific source scope is justified
- Tool(s), versions and relevant enabled rules/settings: [to be recorded after GitHub workflow is created and run]
- **Baseline GitHub scan / Actions run link(s):** [to be recorded]

| Selected smell type | Found / not found / not assessable | Tool result or source link | Interpretation / limitations |
|---|---|---|---|
| Long Method | Pending baseline analysis | [to be recorded] | A complexity warning is a symptom, not proof of poor design. |
| Large Class / Overloaded Class | Pending baseline analysis and manual inspection | [to be recorded] | Source relationships and responsibilities require manual judgment; general linters may not detect this directly. |
| Long Parameter List | Pending baseline analysis | [to be recorded] | Parameter count may be deliberate or constrained by an API; call-site compatibility matters. |
| Duplicated Code | Pending baseline jscpd analysis | [to be recorded] | Duplication count does not prove technical debt; copied code may differ in stability or intended domain. |

**Candidate issues inspected in source (at least two):**

| Candidate ID | File/entity permalink | What was actually observed? | Why it might matter / why uncertain |
|---|---|---|---|
| C1 | [to be recorded after baseline scan] | [actual source observation] | [maintainability impact and uncertainty] |
| C2 | [to be recorded after baseline scan] | [actual source observation] | [maintainability impact and uncertainty] |
| C3 (optional) | [to be recorded if needed] | [actual source observation] | [maintainability impact and uncertainty] |

**One warning we challenged, or one potentially missed issue:** [Record one rule false positive or a plausible smell that the selected tools do not establish directly.]

## Task 3 - Prioritize Technical Debt and Plan Refactoring

| Candidate | Expected future impact / relevance | Estimated effort and behavior risk | Prioritize now or defer? Why? |
|---|---|---|---|
| C1 | [to be completed] | [to be completed] | [to be completed] |
| C2 | [to be completed] | [to be completed] | [to be completed] |
| Additional (if needed) | [to be completed] | [to be completed] | [to be completed] |

**Selected documented issue(s) and individual ownership:** [Complete after candidate comparison.]

| Contributor / GitHub handle | Candidate ID | Planned refactoring | Expected benefit | GitHub regression check planned |
|---|---|---|---|---|
| btatongk | [C1 or C2] | [named refactoring] | [specific maintainability benefit] | [specific existing or targeted GitHub-visible test/check] |

## Task 4 - Refactor, Verify, and Commit

**Baseline test/check run(s) on GitHub:** [URL(s) and outcomes]
**After-refactoring SHA(s):** [full SHA(s)]
**After-refactoring scan / workflow run(s):** [URL(s)]
**After-refactoring test/check run(s):** [URL(s) and outcomes]

| Issue / contributor | Before (same scope and measurement) | After | Test / verification result | What does this actually establish? |
|---|---|---|---|---|
| | | | | |

**Answers to the original GQM questions:**

- **Q1:** [answer based on evidence, not only a warning count]
- **Q2:** [answer based on evidence, not only a warning count]

**Conclusion and limits:** [What was improved? Did any measurements worsen or remain unchanged? What cannot be claimed about maintainability or preserved behavior?]

### Individual implementation commits - permanent GitHub links

| Contributor / GitHub account | Documented issue (C1, C2, ...) | What was refactored? | **Permanent commit link** | PR or GitHub Actions push-run link |
|---|---|---|---|---|
| btatongk | | | | |

**Completed template location on `semester-investigation`:** [GitHub file URL]
**Template/report commit link:** [GitHub `/commit/FULL_SHA` URL]

**Evidence preservation note:** [If any GitHub Actions artifact is relevant, provide a run link and preserve its essential figures here because workflow artifacts can expire.]
