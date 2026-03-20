from fastapi import FastAPI
from app.service import mask_profanity

app = FastAPI()

@app.get("/mask")
def mask(text: str):
    return {"result": mask_profanity(text)}