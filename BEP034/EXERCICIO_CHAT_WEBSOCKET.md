## Exercicio pratico: Chat com WebSocket

Objetivo: criar um chat simples usando FastAPI e WebSockets, com um cliente Python.

### Arquivos

- `main.py` (servidor WebSocket)
- `cliente.py` (cliente de teste)

### Dependencias

Instale no venv:

```
pip install fastapi uvicorn websockets
```

### Servidor (main.py)

```python
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
```

### Cliente (cliente.py)

```python
import asyncio
import websockets

async def cliente():
    async with websockets.connect("ws://localhost:8000/ws/chat") as ws:
        while True:
            texto = input("Digite a mensagem (ou sair): ").strip()
            if texto.lower() == "sair":
                break
            await ws.send(texto)
            resposta = await ws.recv()
            print("Recebido:", resposta)

asyncio.run(cliente())
```

### Como executar

1) Inicie o servidor:

```
uvicorn main:app --reload
```

2) Em outro terminal, rode o cliente:

```
python cliente.py
```

### Observacoes

- Se o cliente der timeout, verifique se o servidor esta ativo e se a rota e `/ws/chat`.
- Para testar com varios clientes, abra mais terminais e rode o `cliente.py`.
