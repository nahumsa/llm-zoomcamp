import pandas as pd
import numpy as np

from rouge import Rouge
from tqdm import tqdm
from sentence_transformers import SentenceTransformer


def norm_vec(v: np.array) -> np.array:
    return v / (np.sqrt((v * v).sum()))


github_url = "https://github.com/DataTalksClub/llm-zoomcamp/blob/main/04-monitoring/data/results-gpt4o-mini.csv"
url = f"{github_url}?raw=1"
df = pd.read_csv(url)
df = df.iloc[:300]

embedding_model = SentenceTransformer("multi-qa-mpnet-base-dot-v1")

answer_llm = df.iloc[0].answer_llm
encoded_answer = embedding_model.encode(answer_llm)
print(f"First value: {encoded_answer[0]}")


embed_llm = []
embed_og = []

for answer_llm, answer_orig in tqdm(
    zip(df.answer_llm.tolist(), df.answer_orig.tolist())
):
    embed_llm.append(embedding_model.encode(answer_llm))
    embed_og.append(embedding_model.encode(answer_orig))

dot_list = []
cossine_list = []

for og, llm in tqdm(zip(embed_og, embed_llm)):
    dot_list.append(og.dot(llm))
    cossine_list.append(norm_vec(og).dot(norm_vec(llm)))

print("Dot product:", np.percentile(dot_list, 75))

print("Cossine:", np.percentile(cossine_list, 75))

rouge_scorer = Rouge()

r = df.iloc[10]
scores = rouge_scorer.get_scores(r["answer_llm"], r["answer_orig"])[0]

print("Rouge-1 F-score:", scores["rouge-1"]["f"])  # type: ignore

f_list = []
for _, val in scores.items():
    f_list.append(val["f"])  # type: ignore


print("Avg. F-score:", np.mean(f_list))

scores = rouge_scorer.get_scores(
    df.answer_llm.tolist(),
    df.answer_orig.tolist(),
    avg=True,
)

print("Avg. Rouge-2 F-score:", scores["rouge-2"]["f"])
