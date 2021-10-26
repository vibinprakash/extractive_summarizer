from fastapi import FastAPI
import uvicorn
from typing import Optional
from summarizer import Summarizer


model = Summarizer()
app = FastAPI()

@app.get('/')
async def home():
    return {'Extractive Summarizer':'Go to the /summarize to get the summary'}

@app.get("/summarize")
async def summarize(body: str,level: Optional[int] = 1):
    result = model(body, ratio=level/10)
    # if ratio is not None:
    #     result = model(body, ratio=ratio)
    # else:
    #     result = model(body, ratio=0.2)
    return {"Summary": result}


if __name__ == "__main__":
    uvicorn.run(app,port=8000)