from sentence_transformers import SentenceTransformer

model_name = "multi-qa-distilbert-cos-v1"
embedding_model = SentenceTransformer(model_name)

user_question = "I just discovered the course. Can I still join it?"
embedding = embedding_model.encode(user_question)
print(embedding[0])
