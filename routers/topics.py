from fastapi import APIRouter
from services.topic_service import get_topic_questions
from database import db

topics_router = APIRouter(prefix="/topics", tags=["topics"])

@topics_router.get("/{topic}")
def get_topic(topic: str):
    q = get_topic_questions(topic)
    db.generated_questions.insert_one({
        "source": "topic",
        "topic": topic,
        "questions": q
    })
    return {"topic": topic, "questions": q}
