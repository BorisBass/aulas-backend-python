from fastapi import FastAPI, WebSocket

app = FastAPI()  # cria a aplicacao

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()  # aceita a conexao
    while True:
        data = await ws.receive_text()  # recebe mensagem
        await ws.send_text(f"Echo: {data}")  # devolve resposta