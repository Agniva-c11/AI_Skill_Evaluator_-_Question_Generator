import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "AI_Skill_Evaluator")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")  # default placeholder

JUDGE0_URL = os.getenv("JUDGE0_URL")  # e.g., https://judge0-ce.p.rapidapi.com
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
