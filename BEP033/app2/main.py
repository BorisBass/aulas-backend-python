import logging
import sqlite3
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from fastapi import Body, Depends, FastAPI, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

app = FastAPI(title="API Tarefas (JWT + Logs + SQLite)")

DB_PATH = Path(__file__).with_name("tarefas.db")
LOG_PATH = Path(__file__).with_name("api.log")

SECRET_KEY = "segredo"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def obter_conexao():
    return sqlite3.connect(DB_PATH)


def init_db():
    with obter_conexao() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                prioridade TEXT NOT NULL,
                status INTEGER NOT NULL
            )
            """
        )


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=LOG_PATH,
)
logger = logging.getLogger("api")
init_db()


def criar_token(payload: dict, exp_minutos: int = 10):
    dados = payload.copy()
    exp = datetime.now(timezone.utc) + timedelta(minutes=exp_minutos)
    dados.update({"exp": int(exp.timestamp())})
    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)


def validar_token(token: str):
    try:
        dados = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp_ts = dados.get("exp")
        if exp_ts is None:
            raise HTTPException(status_code=401, detail="Token sem exp")
        if datetime.now(timezone.utc).timestamp() > exp_ts:
            raise HTTPException(status_code=401, detail="Token expirado")
        return dados
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalido")


def usuario_do_header(request: Request):
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return "anon"
    token = auth.replace("Bearer ", "").strip()
    try:
        dados = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return dados.get("sub", "anon")
    except JWTError:
        return "anon"


@app.middleware("http")
async def log_requests(request: Request, call_next):
    inicio = time.time()
    resposta = await call_next(request)
    duracao = time.time() - inicio
    ip = request.client.host if request.client else "?"
    usuario = usuario_do_header(request)
    logger.info(
        f"{request.method} {request.url.path} - {resposta.status_code} - "
        f"{duracao:.2f}s - ip={ip} usuario={usuario}"
    )
    return resposta


def validar_prioridade(prioridade: str):
    return prioridade in ["alta", "media", "baixa"]


@app.post("/login")
def login(dados: dict = Body(...)):
    usuario = dados.get("usuario")
    senha = dados.get("senha")
    if usuario != "admin" or senha != "123":
        raise HTTPException(status_code=401, detail="Credenciais invalidas")
    token = criar_token({"sub": usuario})
    return {"token": token}


@app.get("/tarefas")
def listar_tarefas(token: str = Depends(oauth2_scheme)):
    validar_token(token)
    with obter_conexao() as conn:
        cursor = conn.execute("SELECT id, descricao, prioridade, status FROM tarefas")
        itens = [
            {
                "id": linha[0],
                "descricao": linha[1],
                "prioridade": linha[2],
                "status": linha[3],
            }
            for linha in cursor.fetchall()
        ]
    return itens


@app.get("/tarefas/{tarefa_id}")
def buscar_tarefa(tarefa_id: int, token: str = Depends(oauth2_scheme)):
    validar_token(token)
    with obter_conexao() as conn:
        cursor = conn.execute(
            "SELECT id, descricao, prioridade, status FROM tarefas WHERE id = ?",
            (tarefa_id,),
        )
        linha = cursor.fetchone()
        if not linha:
            raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
        return {
            "id": linha[0],
            "descricao": linha[1],
            "prioridade": linha[2],
            "status": linha[3],
        }


@app.post("/tarefas")
def criar_tarefa(tarefa: dict = Body(...), token: str = Depends(oauth2_scheme)):
    validar_token(token)
    descricao = tarefa.get("descricao")
    prioridade = tarefa.get("prioridade")
    if not descricao or not isinstance(descricao, str):
        raise HTTPException(status_code=400, detail="Descricao obrigatoria")
    if not prioridade or not validar_prioridade(prioridade):
        raise HTTPException(status_code=400, detail="Prioridade invalida")
    with obter_conexao() as conn:
        cursor = conn.execute(
            "INSERT INTO tarefas (descricao, prioridade, status) VALUES (?, ?, ?)",
            (descricao, prioridade, 0),
        )
        novo_id = cursor.lastrowid
        cursor = conn.execute(
            "SELECT id, descricao, prioridade, status FROM tarefas WHERE id = ?",
            (novo_id,),
        )
        linha = cursor.fetchone()
    return {
        "id": linha[0],
        "descricao": linha[1],
        "prioridade": linha[2],
        "status": linha[3],
    }


@app.put("/tarefas/{tarefa_id}/status")
def atualizar_status(
    tarefa_id: int, dados: dict = Body(...), token: str = Depends(oauth2_scheme)
):
    validar_token(token)
    status = dados.get("status")
    if status is None or not isinstance(status, (int, float)):
        raise HTTPException(status_code=400, detail="Status deve ser numero")
    if status < 0 or status > 100:
        raise HTTPException(status_code=400, detail="Status deve ser 0 a 100")
    with obter_conexao() as conn:
        cursor = conn.execute(
            "UPDATE tarefas SET status = ? WHERE id = ?",
            (int(status), tarefa_id),
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
        cursor = conn.execute(
            "SELECT id, descricao, prioridade, status FROM tarefas WHERE id = ?",
            (tarefa_id,),
        )
        linha = cursor.fetchone()
    return {
        "id": linha[0],
        "descricao": linha[1],
        "prioridade": linha[2],
        "status": linha[3],
    }
