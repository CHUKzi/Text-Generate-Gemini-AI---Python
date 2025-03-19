from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

app = FastAPI()

class RequestModel(BaseModel):
    request_type: str
    character_limit: int
    sample_note: str

def generate_text(request_type, char_limit, sample_note):
    prompt = f"Generate a detailed {request_type} within {char_limit} characters. Sample: {sample_note}"

    model = genai.GenerativeModel(os.getenv("MODEL"))
    response = model.generate_content(prompt)

    if response and response.text:
        return response.text.strip()
    return "No response generated."

@app.post("/generate")
async def generate(request: RequestModel):
    try:
        generated_text = generate_text(request.request_type, request.character_limit, request.sample_note)
        return {"generated_text": generated_text}
    except Exception as e:
        return {"error": str(e)}

