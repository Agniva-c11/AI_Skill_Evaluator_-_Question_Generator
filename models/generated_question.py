from pydantic import BaseModel
from typing import List, Optional

class TheoreticalQuestion(BaseModel):
    question: str
    answer: Optional[str] = None

class CodingTestCase(BaseModel):
    input: str
    output: str

class CodingQuestion(BaseModel):
    question: str
    solution: Optional[str] = None
    test_cases: List[CodingTestCase]

class GeneratedQuestionSet(BaseModel):
    source: str
    topic: Optional[str] = None
    theoretical: List[TheoreticalQuestion]
    coding: List[CodingQuestion]
