from fastapi import APIRouter
from database import db

questions_router = APIRouter(prefix="/questions", tags=["questions"])

@questions_router.get("/resume")
def get_resume_questions():
    return list(db.generated_questions.find({"source": "resume"}, {"_id": 0}))

@questions_router.get("/topic/{topic}")
def get_topic_questions(topic: str):
    return list(db.generated_questions.find({"topic": topic}, {"_id": 0}))
