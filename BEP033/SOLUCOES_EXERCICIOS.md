# Soluções - Exercícios BEP033 (FastAPI)

## Exercício 1: Erro Padronizado
```python
from datetime import datetime

def resposta_erro(mensagem, detalhes=None, codigo=None):
    return {
        "erro": mensagem,
        "detalhes": detalhes or {},
        "codigo": codigo,
        "timestamp": datetime.now().isoformat()
    }
```

## Exercício 2: HTTPException
```python
from fastapi import HTTPException

@app.get("/produtos/{id}")
def buscar(id: int):
    if id != 1:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"id": 1}
```

## Exercício 3: Middleware de Logging
```python
import time, logging
from fastapi import Request

logger = logging.getLogger("api")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    logger.info(f"{request.method} {request.url.path} {response.status_code} {time.time()-start:.2f}s")
    return response
```

## Exercício 4: Validação
```python
from fastapi import HTTPException
from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str

@app.post("/usuarios")
def criar(u: Usuario):
    if len(u.nome) < 3:
        raise HTTPException(status_code=400, detail="Nome curto")
    return {"ok": True}
```

## Exercício 5: Logs de Segurança
```python
import logging
logger = logging.getLogger("api")

@app.get("/protegido")
def protegido(token: str | None = None):
    if not token:
        logger.warning("Acesso sem token")
        raise HTTPException(status_code=401, detail="Token necessário")
    return {"ok": True}
```
