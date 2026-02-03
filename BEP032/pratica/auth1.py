from fastapi import FastAPI, Depends, HTTPException  # importa o necessario
from fastapi.security import HTTPBasic, HTTPBasicCredentials  # suporte ao Basic Auth

app = FastAPI()  # cria a aplicacao
security = HTTPBasic()  # ativa o esquema Basic

@app.get("/lista") # rota não protegida
def lista():
    return [{"mensagem": "deu tudo certo aqui está sua lista"}]

@app.get("/usuarios")  # rota protegida
def listar_usuarios(credentials: HTTPBasicCredentials = Depends(security)):
    # pega usuario e senha enviados no header
    if credentials.username != "admin":
        # se estiver errado, retorna 401 (nao autorizado)
        raise HTTPException(status_code=401, detail="Usuário não cadastrado")
    if credentials.password != "123":
        # se estiver errado, retorna 401 (nao autorizado)
        raise HTTPException(status_code=401, detail="Senha inválida")
    # se estiver correto, retorna dados em JSON
    # vai no banco de dados, recebe a lista de usuários e retorna esta lista em json
    return [{"mensagem": "deu tudo certo"}]