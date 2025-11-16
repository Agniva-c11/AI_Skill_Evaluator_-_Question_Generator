from fastapi import APIRouter, UploadFile, HTTPException
from services.resume_parser import parse_resume
from llm.resume_analyzer import analyze_resume
from llm.question_generator import generate_questions_from_resume
from database import db
import os

resume_router = APIRouter(prefix="/resume", tags=["resume"])

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@resume_router.post("/upload")
async def upload_resume(file: UploadFile):
    # Save file
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")

    # Parse -> Analyze -> Generate
    text = parse_resume(file_path)
    analysis = analyze_resume(text)
    questions = generate_questions_from_resume(analysis)

    # store generated questions in DB (clear structure for later use)
    db.generated_questions.insert_one({
        "source": "resume",
        "file_name": file.filename,
        "analysis": analysis,
        "questions": questions
    })

    return {"analysis": analysis, "questions": questions}
