from fastapi import FastAPI, Body, Depends, HTTPException  # importacoes principais
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials  # token no header
import secrets  # gera tokens aleatorios

app = FastAPI()  # cria a aplicacao
security = HTTPBearer()  # habilita o esquema Bearer
TOKENS = {}  # armazena tokens validos (exemplo simples)

@app.post("/login")  # rota para gerar token
def login(dados: dict = Body(...)):
    usuario = dados.get("usuario")
    senha = dados.get("senha")
    if usuario not in ["admin", "admin1"] or senha not in ["1234", "1231"]:  # valida credenciais
        raise HTTPException(status_code=401, detail="Credenciais invalidas")
    token = secrets.token_urlsafe(32)  # cria o token
    TOKENS[token] = {"usuario": usuario}  # guarda token em memoria
    return {"token": token}  # devolve token ao cliente

@app.get("/lista") # rota não protegida
def lista():
    return [{"mensagem": "deu tudo certo aqui está sua lista"}]

@app.get("/lista_clientes")  # rota protegida por token
def lista_clientes(creds: HTTPAuthorizationCredentials = Depends(security)):
    token = creds.credentials  # pega o token enviado
    if token not in TOKENS:  # valida token
        raise HTTPException(status_code=401, detail="Token invalido")
    return {"mensagem": "Aqui vai a lista de cçientes pq vc passou o token certo"}