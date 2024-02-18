from fastapi import FastAPI
from pydantic import BaseModel

from backend.model import MMSModel

app = FastAPI()
model = MMSModel()

class Text(BaseModel):
    content: str

@app.get("/")
async def root():
    return "Send text via the /convert/ POST API."

@app.post("/convert/")
async def convert_text_to_speech(text: Text):
    print(f'Text: {text.content}')
    return model.convert_to_speech(text.content)