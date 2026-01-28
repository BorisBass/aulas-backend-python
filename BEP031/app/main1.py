from fastapi import Body, FastAPI, HTTPException

app = FastAPI(title="API Produtos")

produtos = [
    {"id": 1, "nome": "Livro Python", "preco": 79.9, "categoria": "livros"},
    {"id": 2, "nome": "Mouse USB", "preco": 49.9, "categoria": "eletronicos"},
]


@app.get("/")
def raiz():
    return {"mensagem": "API funcionando!"}


@app.get("/produtos")
def listar_produtos(categoria=None, preco_max=None):
    itens = produtos
    if categoria:
        itens = [p for p in itens if p.get("categoria") == categoria]
    if preco_max is not None:
        try:
            preco_max = float(preco_max)
            itens = [p for p in itens if p.get("preco") is not None and p["preco"] <= preco_max]
        except ValueError:
            raise HTTPException(status_code=400, detail="preco_max deve ser numero.")
    return {"categoria": categoria, "preco_max": preco_max, "itens": itens}


@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    raise HTTPException(status_code=404, detail="Produto nao encontrado.")


@app.post("/produtos")
def criar_produto(produto: dict = Body(...)):
    nome = produto.get("nome")
    preco = produto.get("preco")
    categoria = produto.get("categoria")
    if not nome or not isinstance(nome, str):
        raise HTTPException(status_code=400, detail="Campo 'nome' obrigatorio.")
    if preco is None or not isinstance(preco, (int, float)):
        raise HTTPException(status_code=400, detail="Campo 'preco' obrigatorio.")
    novo_id = max(p["id"] for p in produtos) + 1 if produtos else 1
    novo = {"id": novo_id, "nome": nome, "preco": preco, "categoria": categoria}
    produtos.append(novo)
    return novo

