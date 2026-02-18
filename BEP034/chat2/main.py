from fastapi import FastAPI, WebSocket

app = FastAPI()
clientes = []  # lista de conexoes ativas

@app.websocket("/ws/chat")
async def chat(ws: WebSocket):
    await ws.accept()  # aceita a conexao
    clientes.append(ws)  # guarda o cliente
    try:
        while True:
            msg = await ws.receive_text()  # recebe mensagem
            for c in clientes:  # envia para todos
                await c.send_text(msg)
    except:
        clientes.remove(ws)  # remove quando desconecta