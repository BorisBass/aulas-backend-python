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