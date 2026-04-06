from fastapi import FastAPI, WebSocket
from langchain_ollama import ChatOllama

app = FastAPI()

llm = ChatOllama(model="llama3.2")


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        resposta = llm.invoke(data)
        await websocket.send_text(resposta.content)
