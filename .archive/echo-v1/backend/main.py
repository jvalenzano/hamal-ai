from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel, Field
from litellm import completion
from groq import Groq
from dotenv import load_dotenv
import os
import tempfile
from dotenv import load_dotenv

# Load env vars
load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

app = FastAPI(title="Hamal API", version="0.1.0")

# --- Schemas ---

class IdeaInput(BaseModel):
    idea: str = Field(..., max_length=1000)

class ValidationResult(BaseModel):
    risk_score: int
    reasoning: str
    recommendation: str

# --- Endpoints ---

# --- Endpoints ---

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
