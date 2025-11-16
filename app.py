from fastapi import FastAPI
from routers.resume import resume_router
from routers.topics import topics_router
from routers.questions import questions_router
from routers.coding import coding_router
from routers.scoring import scoring_router

app = FastAPI(title="AI Skill Evaluation System")

app.include_router(resume_router)
app.include_router(topics_router)
app.include_router(questions_router)
app.include_router(coding_router)
app.include_router(scoring_router)

@app.get("/")
def home():
    return {"message": "AI Skill Evaluation System is running"}
