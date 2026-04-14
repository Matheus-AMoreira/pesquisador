import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket

from src.agents.pesquisador import agent_pesquisador
from src.db.conexao import db

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    url = os.getenv("DATABASE_URL")

    if url is None:
        print("String de conexão não encontrada")
    else:
        await db.connect(url)
        print("Conexão com o banco estabelecida")

    yield

    await db.disconnect()
    print("Conexão com o banco encerrada")


app = FastAPI(lifespan=lifespan)


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    chat_history = []

    while True:
        data = await websocket.receive_text()

        nova_mensagem = {"role": "user", "content": data}
        chat_history.append(nova_mensagem)

        resposta_completa = await agent_pesquisador.ainvoke(
            {"messages": chat_history[-10:]}
        )

        ia_mensagem = resposta_completa["messages"][-1]
        chat_history.append(ia_mensagem)

        await websocket.send_text(ia_mensagem.content)
