import requests
import elasticsearch


def load_documents() -> list[dict]:
    docs_url = "https://github.com/DataTalksClub/llm-zoomcamp/blob/main/01-intro/documents.json?raw=1"
    docs_response = requests.get(docs_url)
    documents_raw = docs_response.json()

    documents = []

    for course in documents_raw:
        course_name = course["course"]

        for doc in course["documents"]:
            doc["course"] = course_name
            documents.append(doc)
    return documents


if __name__ == "__main__":
    es = elasticsearch.Elasticsearch(hosts="http://localhost:9200")

    index_name = "intro"
    index_settings = {
        "settings": {"number_of_shards": 1, "number_of_replicas": 0},
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "section": {"type": "text"},
                "question": {"type": "text"},
                "course": {"type": "keyword"},
            }
        },
    }
    es.indices.create(index=index_name, body=index_settings)

    for doc in load_documents():
        es.index(index=index_name, document=doc)
