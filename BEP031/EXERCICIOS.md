# Exercícios Práticos - BEP031: Criando uma API REST Simples (FastAPI)

## Exercício 1: Configuração Inicial

**Objetivo:** Configurar ambiente FastAPI.

**Tarefa:**
1. Crie um arquivo `main.py`
2. Instale FastAPI e Uvicorn
3. Crie uma rota `GET /` que retorna `{ "mensagem": "API ok" }`
4. Execute com `uvicorn main:app --reload`
5. Acesse `http://localhost:8000/docs`

---

## Exercício 2: Primeira Rota GET

**Objetivo:** Criar rota que retorna dados.

**Tarefa:**
Crie uma rota `GET /produtos` que retorna uma lista de produtos:
- Notebook Dell (3500)
- Mouse Logitech (150)
- Teclado Mecânico (500)

---

## Exercício 3: Rota POST com Pydantic

**Objetivo:** Criar rota POST validada.

**Tarefa:**
Crie uma rota `POST /produtos` usando Pydantic:
- Campos: nome (str), preco (float), categoria (opcional)
- Retorne o produto criado com um `id` simulado

---

## Exercício 4: Path Params

**Objetivo:** Buscar recurso por ID.

**Tarefa:**
Crie `GET /produtos/{produto_id}`:
- Retorne um produto simulado
- Se `produto_id` não existir, lance 404 com HTTPException

---

## Exercício 5: Query Params

**Objetivo:** Filtrar resultados.

**Tarefa:**
Modifique `GET /produtos` para aceitar:
- `categoria`
- `preco_max`
- `search`

---

## Exercício 6: PUT e PATCH

**Objetivo:** Atualizar recursos.

**Tarefa:**
Crie:
- `PUT /produtos/{id}` para atualizar completo
- `PATCH /produtos/{id}` para atualizar parcial

---

## Exercício 7: DELETE

**Objetivo:** Remover recurso.

**Tarefa:**
Crie `DELETE /produtos/{id}` retornando status 204.

---

## Exercício 8: Validação e Erros

**Objetivo:** Retornar erros consistentes.

**Tarefa:**
Ao criar produto, valide:
- nome obrigatório
- preco positivo
Se inválido, retorne 400 com mensagem clara.

---

## Exercício 9: Modelo de Resposta

**Objetivo:** Tipar resposta com Pydantic.

**Tarefa:**
Crie um `ResponseModel` com campos:
- id: int
- nome: str
- preco: float
- categoria: str | None

Use como `response_model` na rota.

---

## Exercício 10: Documentação automática

**Objetivo:** Explorar `/docs`.

**Tarefa:**
- Teste as rotas pelo Swagger
- Verifique exemplos de request/response
- Anote o que o FastAPI gera automaticamente

---

## Respostas e Soluções

As soluções detalhadas estão disponíveis no arquivo `SOLUCOES_EXERCICIOS.md`.
