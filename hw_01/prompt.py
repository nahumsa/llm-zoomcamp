import tiktoken

from searching import es_query
from pydantic import BaseModel


class ContextExample(BaseModel):
    question: str
    answer: str

    def generate_example(self) -> str:
        return f"""
Q: {self.question}
A: {self.answer}
"""


def generate_context() -> list[str]:
    question = "How do I execute a command in a running docker container?"
    filter_course = "machine-learning-zoomcamp"
    context_response = []
    for hit in es_query(question, filter_course=filter_course, size=3)["hits"]:
        context_response.append(
            ContextExample(
                question=question, answer=hit["_source"]["text"]
            ).generate_example()
        )
    return context_response


def generate_prompt(question: str, context: list[str]) -> str:
    all_context = "\n\n".join(context)
    return f"""
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{all_context}
""".strip()


if __name__ == "__main__":
    question = "How do I execute a command in a running docker container?"
    prompt = generate_prompt(question=question, context=generate_context())
    encoding = tiktoken.encoding_for_model("gpt-4o")
    print(prompt)
    print(f"length of the prompt: {len(prompt)}")
    print(f"# of tokens: {len(encoding.encode(prompt))}")
