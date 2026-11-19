
    
  
"""Lab 5: Source-aware Haystack smoke tests for document store and BM25 retrieval.

Run from the local Haystack fork root after `python -m pip install -e .`:
    python evidence/lab5/haystack_smoke.py --check store
    python evidence/lab5/haystack_smoke.py --check retrieval

Checks that the imported `haystack` module belongs to the local checkout.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import haystack
from haystack import Document
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore


def run(check: str) -> None:
    checkout = Path.cwd().resolve()
    imported_from = Path(haystack.__file__).resolve()

    print(f"Python executable: {sys.executable}")
    print(f"Local checkout: {checkout}")
    print(f"Imported Haystack from: {imported_from}")

    assert imported_from.is_relative_to(checkout), (
        "Imported Haystack is NOT within the local checkout; install the "
        "source checkout with `python -m pip install -e .` before testing."
    )

    docs = [
        Document(
            id="aurora",
            content="Aurora borealis is visible near Earth's polar regions.",
        ),
        Document(
            id="waves",
            content="Bioluminescent waves are produced by light-emitting organisms.",
        ),
    ]
    store = InMemoryDocumentStore()
    written = store.write_documents(docs)
    assert written == 2, f"Expected 2 documents written, got {written}"

    if check == "store":
        total = store.count_documents()
        assert total == 2, f"Expected 2 documents in store, got {total}"
        print(f"PASS store: count_documents()={total}")
        return

    retriever = InMemoryBM25Retriever(document_store=store)
    ranked = retriever.run(query="bioluminescent waves", top_k=2)["documents"]
    ranked_ids = [doc.id for doc in ranked]
    assert ranked_ids and ranked_ids[0] == "waves", (
        f"Expected `waves` ranked first; got {ranked_ids}"
    )
    print(f"PASS retrieval: query='bioluminescent waves'; ranked_ids={ranked_ids}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", choices=("store", "retrieval"), required=True)
    args = parser.parse_args()
    run(args.check)


if __name__ == "__main__":
    main()

