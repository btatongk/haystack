"""Run the Lab 7 active-only retrieval case against the checked-out Haystack source."""

from __future__ import annotations

from pathlib import Path

import haystack
from haystack import Document
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore


def retrieve_solar_documents(retriever: InMemoryBM25Retriever) -> list[Document]:
    """Retrieve active documents for the Lab 7 solar-energy query."""
    return retriever.run(
        query="solar energy",
        filters={"field": "meta.status", "operator": "==", "value": "active"},
    )["documents"]


def main() -> None:
    """Run and assert the active-only local BM25 retrieval case."""
    checkout = Path.cwd().resolve()
    imported_from = Path(haystack.__file__).resolve()

    print(f"Checkout root: {checkout}")
    print(f"Imported Haystack from: {imported_from}")

    if not imported_from.is_relative_to(checkout):
        raise RuntimeError(f"Haystack was imported outside the checkout: {imported_from}")

    documents = [
        Document(
            id="active-solar-guide",
            content="Solar energy can be captured with photovoltaic panels to make clean electricity.",
            meta={"status": "active"},
        ),
        Document(
            id="archived-solar-guide",
            content="Solar energy solar energy solar energy solar panels energy archived procedure.",
            meta={"status": "archived"},
        ),
        Document(
            id="active-wind-guide",
            content="Wind turbines convert moving air into electricity.",
            meta={"status": "active"},
        ),
    ]
    store = InMemoryDocumentStore(shared=False)

    try:
        written = store.write_documents(documents)
        if written != len(documents):
            raise RuntimeError(f"Expected to index {len(documents)} documents, wrote {written}")

        retriever = InMemoryBM25Retriever(document_store=store, top_k=3)
        retrieved = retrieve_solar_documents(retriever)
        retrieved_ids = [document.id for document in retrieved]
        print("Query: solar energy")
        print(f"Retrieved document IDs: {retrieved_ids}")

        expected_ids = ["active-solar-guide"]
        if retrieved_ids != expected_ids:
            raise AssertionError(f"Expected active-only IDs {expected_ids}, received {retrieved_ids}")
        print("PASS active-only BM25 retrieval")
    finally:
        store.shutdown()


if __name__ == "__main__":
    main()
