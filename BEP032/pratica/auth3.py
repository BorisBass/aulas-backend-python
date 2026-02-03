from fastapi import Body, Depends, FastAPI, HTTPException  # imports principais
from fastapi.security import OAuth2PasswordBearer  # extrai token do header
from jose import jwt, JWTError  # cria e valida JWT
from datetime import datetime, timedelta, timezone  # expiração do token

SECRET_KEY = "segredo"  # chave usada para assinar o JWT
ALGORITHM = "HS256"  # algoritmo de assinatura

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")  # rota que gera token

app = FastAPI()  # cria a aplicacao

def criar_token(payload: dict, exp_minutos: int = 2):
    dados = payload.copy()  # copia os dados
    exp = datetime.now(timezone.utc) + timedelta(minutes=exp_minutos)  # expira em 3 min
    dados.update({"exp": int(exp.timestamp())})  # adiciona expiracao em timestamp
    dados.update({"admin": "S"}) # autorização S = cadastro / N = modificação
    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)  # assina o token

@app.post("/login")  # rota de login
def login(dados: dict = Body(...)):
    usuario = dados.get("usuario")
    senha = dados.get("senha")
    if usuario != "admin" or senha != "123":
        raise HTTPException(status_code=401, detail="Credenciais invalidas")
    token = criar_token({"sub": usuario})  # sub = subject (usuario)
    return {"token": token}

@app.get("/protegido")  # rota protegida
def protegido(token: str = Depends(oauth2_scheme)):
    try:
        dados = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # valida token
        exp_ts = dados.get("exp")
        if exp_ts is None:
            raise HTTPException(status_code=401, detail="Token sem data de expiração")
        if datetime.now(timezone.utc).timestamp() > exp_ts:
            raise HTTPException(status_code=401, detail="Token expirado")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalido")
    exp_iso = datetime.fromtimestamp(exp_ts, tz=timezone.utc).isoformat()
    return {"usuario": dados.get("sub"), "expira_em": exp_iso, "É admin? ": dados.get("admin")}