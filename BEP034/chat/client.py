import asyncio
import websockets

async def cliente():
    try:
        async with websockets.connect("ws://127.0.0.1:8000/ws") as ws:
            await ws.send("Ola WebSocket!")  # envia mensagem
            resposta = await ws.recv()  # espera resposta
            print("Recebido:", resposta)  # mostra no terminal
    except Exception as e:
        print("Erro no cliente:", e)  # trata erro

asyncio.run(cliente())