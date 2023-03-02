import logging
import azure.functions as func
import requests
import openai
from FastAPIApp import app  # Main API application

# ############### 

@app.get("/sample")
async def index():
    return {
        "info": "Try /hello/Shivani for parameterized route.",
    }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }

# Rapid API
url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "0dd8668bb4msh7d84ecd476335fep118479jsn6d1e00ff27b0",
	"X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
}
@app.get("/translate/{translate}")
async def get_translate(translate: str):
    payload = {
	"from": "en",
	"to": "zh",
	"e": "",
	"q": translate
    }
    response = requests.request("POST", url, json=payload, headers=headers, timeout = 30)
    return {
        "translate": response.text,
    }

# OpenAI

openai.api_key = "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"

@app.get("/chat/{chat}")
async def get_chat(chat: str):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": chat}
        ]
        )
    return {
        "chat": completion.choices[0].message,
    }

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
