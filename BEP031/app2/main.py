from pathlib import Path
import sqlite3

from fastapi import Body, FastAPI, HTTPException

app = FastAPI(title="API Produtos (SQLite)")

DB_PATH = Path(__file__).with_name("produtos.db")


def obter_conexao():
    return sqlite3.connect(DB_PATH)


def init_db():
    with obter_conexao() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                categoria TEXT
            )
            """
        )
        cursor = conn.execute("SELECT COUNT(*) FROM produtos")
        total = cursor.fetchone()[0]
        if total == 0:
            conn.execute(
                "INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)",
                ("Livro Python", 79.9, "livros"),
            )
            conn.execute(
                "INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)",
                ("Mouse USB", 49.9, "eletronicos"),
            )


init_db()


@app.get("/")
def raiz():
    return {"mensagem": "API funcionando com SQLite!"}


@app.get("/produtos")
def listar_produtos(categoria=None, preco_max=None):
    filtros = []
    params = []
    if categoria:
        filtros.append("categoria = ?")
        params.append(categoria)
    if preco_max is not None:
        try:
            preco_max = float(preco_max)
        except ValueError:
            raise HTTPException(status_code=400, detail="preco_max deve ser numero.")
        filtros.append("preco <= ?")
        params.append(preco_max)

    sql = "SELECT id, nome, preco, categoria FROM produtos"
    if filtros:
        sql += " WHERE " + " AND ".join(filtros)

    with obter_conexao() as conn:
        cursor = conn.execute(sql, params)
        itens = [
            {"id": linha[0], "nome": linha[1], "preco": linha[2], "categoria": linha[3]}
            for linha in cursor.fetchall()
        ]

    return {"categoria": categoria, "preco_max": preco_max, "itens": itens}


@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    with obter_conexao() as conn:
        cursor = conn.execute(
            "SELECT id, nome, preco, categoria FROM produtos WHERE id = ?",
            (produto_id,),
        )
        linha = cursor.fetchone()
        if not linha:
            raise HTTPException(status_code=404, detail="Produto nao encontrado.")
        return {"id": linha[0], "nome": linha[1], "preco": linha[2], "categoria": linha[3]}


@app.post("/produtos")
def criar_produto(produto: dict = Body(...)):
    nome = produto.get("nome")
    preco = produto.get("preco")
    categoria = produto.get("categoria")
    if not nome or not isinstance(nome, str):
        raise HTTPException(status_code=400, detail="Campo 'nome' obrigatorio.")
    if preco is None or not isinstance(preco, (int, float)):
        raise HTTPException(status_code=400, detail="Campo 'preco' obrigatorio.")

    with obter_conexao() as conn:
        cursor = conn.execute(
            "INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)",
            (nome, preco, categoria),
        )
        novo_id = cursor.lastrowid
        cursor = conn.execute(
            "SELECT id, nome, preco, categoria FROM produtos WHERE id = ?",
            (novo_id,),
        )
        linha = cursor.fetchone()

    return {"id": linha[0], "nome": linha[1], "preco": linha[2], "categoria": linha[3]}
