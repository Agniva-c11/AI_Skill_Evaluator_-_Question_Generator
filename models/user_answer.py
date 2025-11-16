from pydantic import BaseModel
from typing import List

class UserAnswerItem(BaseModel):
    question: str
    correct_answer: str
    user_answer: str

class UserAnswerRequest(BaseModel):
    answers: List[UserAnswerItem]
