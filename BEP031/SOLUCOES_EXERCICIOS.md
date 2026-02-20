# Soluções - Exercícios BEP031 (FastAPI)

## Exercício 1: Configuração Inicial

```python
# main.py
from fastapi import FastAPI

app = FastAPI(title="API Exemplo")

@app.get("/")
def raiz():
    return {"mensagem": "API ok"}
```

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

---

## Exercício 2: Primeira Rota GET

```python
@app.get("/produtos")
def listar_produtos():
    return [
        {"id": 1, "nome": "Notebook Dell", "preco": 3500},
        {"id": 2, "nome": "Mouse Logitech", "preco": 150},
        {"id": 3, "nome": "Teclado Mecânico", "preco": 500},
    ]
```

---

## Exercício 3: Rota POST com Pydantic

```python
from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    preco: float
    categoria: str | None = None

@app.post("/produtos")
def criar_produto(produto: Produto):
    return {"id": 4, **produto.dict()}
```

---

## Exercício 4: Path Params

```python
from fastapi import HTTPException

@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    if produto_id != 1:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"id": 1, "nome": "Notebook Dell", "preco": 3500}
```

---

## Exercício 5: Query Params

```python
@app.get("/produtos")
def listar_produtos(categoria: str | None = None, preco_max: float | None = None, search: str | None = None):
    return {
        "categoria": categoria,
        "preco_max": preco_max,
        "search": search
    }
```

---

## Exercício 6: PUT e PATCH

```python
@app.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, produto: Produto):
    return {"id": produto_id, **produto.dict()}

@app.patch("/produtos/{produto_id}")
def atualizar_parcial(produto_id: int, dados: dict):
    return {"id": produto_id, "atualizado": dados}
```

---

## Exercício 7: DELETE

```python
from fastapi import Response, status

@app.delete("/produtos/{produto_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto(produto_id: int):
    return Response(status_code=status.HTTP_204_NO_CONTENT)
```

---

## Exercício 8: Validação e Erros

```python
@app.post("/produtos")
def criar_produto(produto: Produto):
    if not produto.nome or produto.preco <= 0:
        raise HTTPException(status_code=400, detail="Dados inválidos")
    return {"id": 5, **produto.dict()}
```

---

## Exercício 9: Modelo de Resposta

```python
from pydantic import BaseModel

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    categoria: str | None = None

@app.get("/produtos/{produto_id}", response_model=ProdutoResponse)
def buscar_produto(produto_id: int):
    return {"id": produto_id, "nome": "Notebook", "preco": 3500}
```

---

## Exercício 10: Documentação automática

Acesse:
- `http://localhost:8000/docs` (Swagger)
- `http://localhost:8000/redoc` (ReDoc)

O FastAPI gera automaticamente:
- documentação de endpoints
- exemplos de request/response
- validações e schemas

