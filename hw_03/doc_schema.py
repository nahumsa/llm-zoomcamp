from pydantic import BaseModel, computed_field


class Docs(BaseModel):
    id: str
    text: str
    question: str
    course: str

    @computed_field
    @property
    def qa_text(self) -> str:
        return f"{self.question} {self.text}"


class GroundTruthDocs(BaseModel):
    document: str
    question: str
    course: str
