# Lab #7 — From Code to Operation: Investigation Record

**Team:** Individual
**Student(s) / GitHub handle(s):** [Full name to confirm] — @btatongk
**Fork / working branch:** https://github.com/btatongk/haystack/tree/semester-investigation
**Upstream project and pinned version:** https://github.com/deepset-ai/haystack / fork baseline commit `bc7a6ba24a601c1737f820785f25ae0fdb3e8057`

## 1. Stakeholder, goal and selected functionality

**Stakeholder concern:** Sam, Release Engineer: "A change works on the developer's machine, but I need confidence that our software can be installed and exercised in a clean environment. When its behavior changes, our delivery checks should make that change visible and help us decide whether the new version is acceptable."

**GQM goal:** Analyze **a fork-owned Haystack BM25 document retrieval path** for the purpose of **evaluating deployment and behavioral-change verification** with respect to **clean-environment executability and document eligibility correctness**, from the viewpoint of **Sam, Release Engineer**, in the context of **the `btatongk/haystack` fork running on a GitHub-hosted Ubuntu runner**.

| Question | Question in your own words | Evidence / measurement and why it helps |
|---|---|---|
| Q1 | Can a clean Ubuntu runner install Haystack from this fork and execute an in-memory BM25 retrieval case using the checked-out source? | Record the checkout SHA, `haystack.__file__` path, editable-install outcome, query, and returned document IDs. This connects the functional result to the intended fork commit rather than a preinstalled package. |
| Q2 | Does the changed retrieval path exclude archived documents while still returning the relevant active document for the same query? | Compare returned IDs before and after the filter; assert the archived ID is excluded and the active solar guide remains the top eligible result. This demonstrates both the intentional change and a relevant unchanged invariant. |

**Selected function/component:** [`InMemoryBM25Retriever.run`](https://github.com/btatongk/haystack/blob/bc7a6ba24a601c1737f820785f25ae0fdb3e8057/haystack/components/retrievers/in_memory/bm25_retriever.py#L121)
**Why this represents the software's purpose:** Haystack provides components for retrieval-augmented applications, and this real in-memory BM25 component searches indexed documents for a query. It exercises meaningful indexing and retrieval behavior without external services, credentials, or model downloads.

**Representative input and baseline expectation:** Index three local documents: `active-solar-guide` (solar energy, status `active`), `archived-solar-guide` (strong solar/energy term match, status `archived`), and `active-wind-guide` (unrelated, status `active`). Query for `"solar energy"` with `top_k=3`. A local runtime check against the fork returned `["archived-solar-guide", "active-solar-guide"]` without an eligibility filter.

**Planned small behavior change:** In a small Lab 7 application-facing retrieval function that genuinely invokes `InMemoryBM25Retriever`, add a metadata filter `meta.status == "active"` so archived documents are ineligible to be returned. Keep the Haystack component itself unchanged. The same local runtime check with that filter returned `["active-solar-guide"]`.

**What must still work unchanged?** The relevant active solar guide remains the first returned document. The unrelated `active-wind-guide` remains outside the results for this query, and the runner must prove it imported Haystack from its checkout.

## 2. Baseline: deploy and execute on GitHub

| Evidence | Baseline |
|---|---|
| Baseline commit SHA and link | [To record after the baseline workflow commit is approved and pushed] |
| Actions workflow file link | [`.github/workflows/lab7-retrieval.yml`](.github/workflows/lab7-retrieval.yml) |
| Ubuntu/runtime and relevant dependency versions | GitHub-hosted `ubuntu-24.04`, Python 3.11, Hatch 1.16.5 |
| How the fork's code is installed/built and verified as the executed code | `hatch run` installs the project from the checked-out repository in its Hatch environment; the job logs `git rev-parse HEAD`; the script prints and asserts `haystack.__file__` is inside the checkout |
| Functional case executed (command/script/test or local endpoint) | [`scripts/lab7_retrieval.py`](scripts/lab7_retrieval.py) indexes three local documents and calls the application-facing `retrieve_solar_documents()` path backed by `InMemoryBM25Retriever.run` |
| Expected vs observed behavior | Local baseline check: expected archived guide first; observed IDs `["archived-solar-guide", "active-solar-guide"]` |
| Check result and meaningful measurement(s), if any | Local Hatch-run baseline passed; output IDs were `["archived-solar-guide", "active-solar-guide"]`, and the imported module path was within the checkout; GitHub baseline pending |
| Exact GitHub Actions run URL | [Pending] |

**What does this establish, and what does it not establish?** The local Hatch-run check establishes the baseline output for this fixed input and confirms the imported module came from the local checkout. It is not GitHub-hosted evidence and does not yet establish clean-runner installation or the behavior of a pushed commit.

## 3. Controlled change and verification

**Source/function changed:** [Planned Lab 7 application-facing retrieval function; link after implementation]
**Reason for change:** Exclude archived material from current retrieval results so users do not receive outdated guidance as the top answer.
**Code-change commit(s):** [Not created; do not commit without user approval]

| Item | Before change | After change |
|---|---|---|
| Same input/case | Three documents; query `"solar energy"` | Same three documents and query |
| Expected behavior under each version's stated contract | Archived solar guide may rank first | Only active documents are eligible; active solar guide should rank first |
| Observed behavior on GitHub runner | [Pending] | [Pending] |
| Automated case check/result | [To implement] | [To implement] |
| Unchanged regression/invariant check | Fork checkout verified; solar relevance is measured | Active solar guide is still returned first; fork checkout verified |
| Exact Actions run URL | [Pending] | [Pending] |
| Commit SHA | [Pending] | [Pending] |

**How do your checks distinguish the two versions?** [Complete after implementing and running the checks.]

**Did anything fail unexpectedly? What did you learn or fix?** [Complete after the GitHub runs.]

## 4. Engineering judgment and submission

**Answer Q1:** [Complete from both GitHub Actions runs.]

**Answer Q2:** [Complete from both GitHub Actions runs.]

**Release decision:** [Accept changed version / request changes / insufficient evidence — and why]

**One important limitation or missing check:** The fixed in-memory corpus is small and synthetic; it demonstrates execution and the filtering contract but not retrieval quality on production-scale, diverse, or changing documents.

| GitHub evidence | Link |
|---|---|
| Lab #7 pull request (within your fork) | [Pending; requires approval before creating or merging] |
| **Merged commit** on `semester-investigation` | [Pending] |
| Final `LAB7_ANALYSIS.md` on merged branch | [Pending] |
| Student 1 meaningful commit(s) | [Pending] |

**LLM assistance (if used):** Assisted with scoping the BM25 case, drafting the report, and implementation planning. The API behavior and local before/after result were checked against the fork's source and runtime.

**Submission reminder:** Each student submits `Lab7_YOUR_GITHUB_HANDLE.txt` to the Lab #7 MS Teams submit folder, containing their name, fork URL, merged-commit URL and final analysis URL.
