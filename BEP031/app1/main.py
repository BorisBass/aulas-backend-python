from fastapi import Body, FastAPI, HTTPException

app = FastAPI(title="API Exemplo")

usuarios = [
]

@app.get("/")
def raiz():
    return {"mensagem": "Api está funcionando!"}

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario nao encontrado.")

@app.post("/usuarios") #rota
def criar_usuario(usuario: dict = Body(...)):# ===> usuario = {"id": 4, "nome": "Ana", "email": "ana@email.com" }
    id = usuario.get("id")
    nome = usuario.get("nome")
    email = usuario.get("email")
    novo = {"id": id, "nome": nome, "email": email}
    usuarios.append(novo)
    return novo
