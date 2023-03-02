import logging
import azure.functions as func
from FastAPIApp import app  # Main API application
import requests

url = "https://aeona3.p.rapidapi.com/"
headers = {
	"X-RapidAPI-Key": "0dd8668bb4msh7d84ecd476335fep118479jsn6d1e00ff27b0",
	"X-RapidAPI-Host": "aeona3.p.rapidapi.com"
}

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

@app.get("/chat/{chat}")
async def get_chat(chat: str):
    querystring = {"text":chat,"userId":"12312312312"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return {
        "chat": response.text,
    }

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
