from typing import Optional
from elasticsearch import Elasticsearch
from pprint import pprint


def es_query(
    query: str,
    fields: list[str] = ["question^4", "text", "section"],
    filter_course: Optional[str] = None,
    index_name="intro",
    size: int = 5,
) -> list[dict]:
    search_query = {
        "size": size,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": fields,
                        "type": "best_fields",
                    }
                },
            }
        },
    }

    if filter_course:
        search_query["query"]["bool"]["filter"] = {"term": {"course": filter_course}}

    es = Elasticsearch("http://localhost:9200")
    response = es.search(index=index_name, body=search_query)

    return response["hits"]


if __name__ == "__main__":
    question = "How do I execute a command in a running docker container?"
    print(f"making question: {question}")
    print(f"max score: {es_query(question)['hits'][0]['_score']}")  # type: ignore
    filter_course = "machine-learning-zoomcamp"
    print(f"making question: {question} with filter: {filter_course}")
    print("question:")
    print(
        es_query(question, filter_course=filter_course)["hits"][2]["_source"][  # type: ignore
            "question"
        ],
    )
