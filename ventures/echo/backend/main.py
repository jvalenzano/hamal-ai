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

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/analyze", response_model=ValidationResult)
def analyze_idea(input_data: IdeaInput):
    try:
        # Pydantic schema for structured output
        # Note: LiteLLM supports response_format with some providers, 
        # or we prompt engineered it if structured output isn't native to the specific Groq model yet.
        # For Llama 3.1 70B on Groq, JSON mode is supported.
        
        prompt = f"""
        Analyze this startup idea: "{input_data.idea}"
        
        Return a JSON object with:
        - risk_score: integer 0-100 (0 = safe, 100 = risky)
        - reasoning: 1 sentence summary of risks
        - recommendation: "Validate", "Refine", or "Kill"
        """

        response = completion(
            model="groq/llama-3.1-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"} 
        )
        
        content = response.choices[0].message.content
        return ValidationResult.model_validate_json(content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- Transcribe Endpoint ---

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        # Create a temporary file to store the uploaded audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp_audio:
            content = await file.read()
            temp_audio.write(content)
            temp_audio_path = temp_audio.name

        # Open the file and send to Groq for transcription
        with open(temp_audio_path, "rb") as file_obj:
            transcription = client.audio.transcriptions.create(
                file=(temp_audio_path, file_obj.read()),
                model="distil-whisper-large-v3-en",
                response_format="json",
                language="en",
                temperature=0.0
            )

        # Clean up
        os.remove(temp_audio_path)

        return {"text": transcription.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
