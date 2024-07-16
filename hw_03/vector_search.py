import numpy as np

from doc_schema import Docs


class VectorSearchEngine:
    def __init__(self, documents: list[Docs], embeddings: np.array):
        self.documents = documents
        self.embeddings = embeddings

    def search(self, v_query, num_results=5):
        scores = self.embeddings.dot(v_query)
        idx = np.argsort(-scores)[:num_results]
        return [self.documents[i] for i in idx]
