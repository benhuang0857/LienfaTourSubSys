from fastapi import FastAPI, Request
from pydantic import BaseModel
from pypinyin import pinyin, lazy_pinyin, Style

# Define the request body model
class TextInput(BaseModel):
    text: str

# Initialize FastAPI app
app = FastAPI()

@app.post("/convert")
async def convert_pinyin(input: TextInput):
    text = input.text

    wade_giles = lazy_pinyin(text, style=Style.WADEGILES)
    hanyu_pinyin = lazy_pinyin(text, style=Style.NORMAL)
    pinyin_result = lazy_pinyin(text)
    bopomofo_result = pinyin(text, style=Style.BOPOMOFO)

    return {
        "wei-toma": wade_giles,
        "hanyu": hanyu_pinyin,
        "tong-yong": pinyin_result,
        "zhuyin": bopomofo_result
    }

# Run the application using: uvicorn filename:app --reload
# Example: uvicorn app:app --host 127.0.0.1 --port 8080 &
