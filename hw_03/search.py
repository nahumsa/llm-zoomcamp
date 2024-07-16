import requests
import pandas as pd
import numpy as np
import tqdm
from pydantic import TypeAdapter
from sentence_transformers import SentenceTransformer

from doc_schema import Docs, GroundTruthDocs
from vector_search import VectorSearchEngine


def get_docs() -> list[Docs]:
    base_url = "https://github.com/DataTalksClub/llm-zoomcamp/blob/main"
    relative_url = "03-vector-search/eval/documents-with-ids.json"
    docs_url = f"{base_url}/{relative_url}?raw=1"
    docs_response = requests.get(docs_url)

    docs_list = TypeAdapter(list[Docs]).validate_python(docs_response.json())

    return [doc for doc in docs_list if doc.course == "machine-learning-zoomcamp"]


def get_embeddings(
    document_list: list[Docs], embedding_model: SentenceTransformer
) -> np.ndarray:
    embeddings = []
    for doc in tqdm.tqdm(document_list):
        embeddings.append(embedding_model.encode(doc.qa_text))

    return np.array(embeddings)


def hit_rate(relevance_total: list[bool]) -> float:
    return sum([sum(line) for line in relevance_total]) / len(relevance_total)


def get_ground_truth() -> list[GroundTruthDocs]:
    base_url = "https://github.com/DataTalksClub/llm-zoomcamp/blob/main"

    relative_url = "03-vector-search/eval/ground-truth-data.csv"
    ground_truth_url = f"{base_url}/{relative_url}?raw=1"

    df_ground_truth = pd.read_csv(ground_truth_url)
    df_ground_truth = df_ground_truth[
        df_ground_truth.course == "machine-learning-zoomcamp"
    ]
    return TypeAdapter(list[GroundTruthDocs]).validate_python(
        df_ground_truth.to_dict(orient="records")
    )


model_name = "multi-qa-distilbert-cos-v1"
embedding_model = SentenceTransformer(model_name)
documents = get_docs()

X = get_embeddings(document_list=documents, embedding_model=embedding_model)
print(f"Shape of X: {X.shape}")

user_question = "I just discovered the course. Can I still join it?"
question_embedding = embedding_model.encode(user_question)
scores = X.dot(question_embedding)
print(f"Score of the question: {scores.max()}")

search_engine = VectorSearchEngine(documents=documents, embeddings=X)

ground_truth = get_ground_truth()


all_relevance = []
for gt in tqdm.tqdm(ground_truth):
    results = search_engine.search(embedding_model.encode(gt.question), num_results=5)
    all_relevance.append([res.id == gt.document for res in results])

print(hit_rate(all_relevance))
