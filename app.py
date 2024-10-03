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
        "wei_toma": [p.upper() for p in wade_giles],  # 威妥瑪拼音大寫
        "hanyu": [p.upper() for p in hanyu_pinyin],    # 漢語拼音大寫
        "tong_yong": [p.upper() for p in pinyin_result], # 通用拼音大寫
        "zhuyin": bopomofo_result  # 注音保持不變
    }

# Run the application using: uvicorn filename:app --reload
# Example: uvicorn app:app --host 127.0.0.1 --port 8080 --reload &
