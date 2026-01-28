from fastapi import Body, FastAPI, HTTPException

app = FastAPI(title="API Exemplo")

usuarios = [
    {"id": 1, "nome": "João", "email": "joao@email.com"},
    {"id": 2, "nome": "Maria", "email": "maria@email.com"},
]

@app.get("/")
def raiz():
    return {"mensagem": "API funcionando!"}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario nao encontrado.")


@app.post("/usuarios")
def criar_usuario(usuario: dict = Body(...)):
    try:
        nome = usuario.get("nome")
        email = usuario.get("email")
        if not nome or not isinstance(nome, str):
            raise HTTPException(status_code=400, detail="Campo 'nome' obrigatorio.")
        if not email or not isinstance(email, str):
            raise HTTPException(status_code=400, detail="Campo 'email' obrigatorio.")
        novo_id = max(u["id"] for u in usuarios) + 1 if usuarios else 1
        novo = {"id": novo_id, "nome": nome, "email": email}
        usuarios.append(novo)
        return novo
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Erro interno ao criar usuario.")