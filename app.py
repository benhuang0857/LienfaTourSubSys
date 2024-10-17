from fastapi import FastAPI
from pydantic import BaseModel
from pypinyin import pinyin, Style
import re

# Define the request body model
class TextInput(BaseModel):
    text: str

# Initialize FastAPI app
app = FastAPI()

# 正則表達式來去除聲調符號
def remove_tone(bopomofo):
    return re.sub(r'[ˊˇˋ˙]', '', bopomofo)

@app.post("/convert")
async def convert_pinyin(input: TextInput):
    text = input.text

    # 生成帶聲調的注音
    bopomofo_result = pinyin(text, style=Style.BOPOMOFO)

    # 去掉聲調符號
    bopomofo_no_tone = [''.join(remove_tone(b) for b in bopomofo) for bopomofo in bopomofo_result]

    return {
        "zhuyin": bopomofo_no_tone  # 注音去掉聲調
    }

# Run the application using: uvicorn filename:app --reload
# Example: uvicorn app:app --host 127.0.0.1 --port 8080 --reload &
