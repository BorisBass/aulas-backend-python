# Soluções - Exercícios BEP032 (FastAPI)

## Exercício 2: Basic Auth
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.get("/usuarios")
def listar_usuarios(creds: HTTPBasicCredentials = Depends(security)):
    if creds.username != "admin" or creds.password != "123":
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return [{"id": 1, "nome": "João"}]
```

## Exercício 3: Token simples
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import secrets

app = FastAPI()
security = HTTPBearer()
TOKENS = {}

@app.post("/login")
def login(usuario: str, senha: str):
    if usuario != "admin" or senha != "123":
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = secrets.token_urlsafe(32)
    TOKENS[token] = usuario
    return {"token": token}

@app.get("/protegido")
def protegido(creds: HTTPAuthorizationCredentials = Depends(security)):
    if creds.credentials not in TOKENS:
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"mensagem": "Acesso autorizado"}
```

## Exercício 4: JWT
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "segredo"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
app = FastAPI()

def criar_token(sub: str, minutos=30):
    exp = datetime.utcnow() + timedelta(minutes=minutos)
    return jwt.encode({"sub": sub, "exp": exp}, SECRET_KEY, algorithm=ALGORITHM)

@app.get("/protegido")
def protegido(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"usuario": payload.get("sub")}
```

## Exercício 5: Autorização simples
```python
def is_admin(usuario: str):
    return usuario == "admin"

@app.post("/produtos")
def criar_produto(usuario: str):
    if not is_admin(usuario):
        raise HTTPException(status_code=403, detail="Sem permissão")
    return {"ok": True}
```
