# Soluções - Exercícios BEP030: RESTful Web Services e Métodos HTTP

## Exercício 1: Identificando Métodos HTTP

1. **Buscar lista de todos os produtos**
   - **Método:** GET
   - **URL:** GET /api/produtos
   - **Explicação:** Operação de leitura, não modifica dados

2. **Criar um novo produto**
   - **Método:** POST
   - **URL:** POST /api/produtos
   - **Explicação:** Cria um novo recurso no servidor

3. **Atualizar o preço de um produto específico**
   - **Método:** PATCH
   - **URL:** PATCH /api/produtos/123
   - **Explicação:** Atualização parcial (apenas o preço)

4. **Deletar um produto**
   - **Método:** DELETE
   - **URL:** DELETE /api/produtos/123
   - **Explicação:** Remove um recurso do servidor

5. **Buscar informações de um produto específico**
   - **Método:** GET
   - **URL:** GET /api/produtos/123
   - **Explicação:** Operação de leitura de um recurso específico

6. **Atualizar todos os dados de um produto**
   - **Método:** PUT
   - **URL:** PUT /api/produtos/123
   - **Explicação:** Substitui o recurso completo

---

## Exercício 2: Modelando URLs RESTful

### Posts:
- GET /api/posts - Lista todos os posts
- GET /api/posts/123 - Busca post por ID
- POST /api/posts - Cria novo post
- PUT /api/posts/123 - Atualiza post completo
- PATCH /api/posts/123 - Atualiza post parcialmente
- DELETE /api/posts/123 - Deleta post

### Comentários:
- GET /api/comentarios - Lista todos os comentários
- GET /api/comentarios/456 - Busca comentário por ID
- POST /api/comentarios - Cria novo comentário
- PATCH /api/comentarios/456 - Atualiza comentário
- DELETE /api/comentarios/456 - Deleta comentário
- GET /api/posts/123/comentarios - Lista comentários de um post

### Autores:
- GET /api/autores - Lista todos os autores
- GET /api/autores/789 - Busca autor por ID
- POST /api/autores - Cria novo autor
- PUT /api/autores/789 - Atualiza autor completo
- PATCH /api/autores/789 - Atualiza autor parcialmente
- DELETE /api/autores/789 - Deleta autor

---

## Exercício 3: Status Codes

1. **Usuário criado com sucesso** → 201 Created
2. **Produto não encontrado** → 404 Not Found
3. **Dados inválidos enviados** → 400 Bad Request
4. **Usuário não autenticado** → 401 Unauthorized
5. **Usuário autenticado mas sem permissão** → 403 Forbidden
6. **Erro interno no servidor** → 500 Internal Server Error
7. **Produto atualizado com sucesso** → 200 OK
8. **Produto deletado com sucesso** → 204 No Content
9. **Recurso criado e retornado** → 201 Created
10. **Requisição bem-sucedida sem conteúdo** → 204 No Content

---

## Exercício 4: PUT vs PATCH

1. **Atualizar apenas o email de um usuário**
   - **Resposta:** PATCH
   - **Por quê:** Atualização parcial, apenas um campo

2. **Atualizar todos os dados de um produto**
   - **Resposta:** PUT
   - **Por quê:** Substituição completa do recurso

3. **Marcar um pedido como "entregue"**
   - **Resposta:** PATCH
   - **Por quê:** Atualização parcial, apenas o status

4. **Atualizar nome, email e telefone de um cliente**
   - **Resposta:** PUT ou PATCH
   - **Por quê:** PATCH se não enviar todos os campos, PUT se enviar todos

5. **Alterar apenas o status de um pedido**
   - **Resposta:** PATCH
   - **Por quê:** Atualização parcial de um único campo

---

## Exercício 5: Corrigindo URLs Não-RESTful

1. `/api/getUser?id=123` → `GET /api/usuarios/123`
2. `/api/createProduct` → `POST /api/produtos`
3. `/api/updateOrder/456` → `PUT /api/pedidos/456` ou `PATCH /api/pedidos/456`
4. `/api/deleteItem/789` → `DELETE /api/itens/789`
5. `/api/user/123/orders` → `GET /api/usuarios/123/pedidos`
6. `/api/listProducts` → `GET /api/produtos`
7. `/api/searchUsers?q=João` → `GET /api/usuarios?search=João`

---

## Exercício 6: Criando Endpoints Completos

### Tarefas:
- GET /api/tarefas - Lista todas as tarefas
- POST /api/tarefas - Cria nova tarefa
- GET /api/tarefas/123 - Busca tarefa específica
- PATCH /api/tarefas/123 - Atualiza tarefa (marcar como concluída)
- DELETE /api/tarefas/123 - Deleta tarefa
- GET /api/categorias/456/tarefas - Lista tarefas de uma categoria
- GET /api/usuarios/789/tarefas - Lista tarefas de um usuário

### Categorias:
- GET /api/categorias - Lista todas as categorias
- POST /api/categorias - Cria nova categoria
- GET /api/categorias/456 - Busca categoria específica
- PUT /api/categorias/456 - Atualiza categoria
- DELETE /api/categorias/456 - Deleta categoria

### Usuários:
- GET /api/usuarios - Lista todos os usuários
- POST /api/usuarios - Cria novo usuário
- GET /api/usuarios/789 - Busca usuário específico
- PATCH /api/usuarios/789 - Atualiza usuário
- DELETE /api/usuarios/789 - Deleta usuário

---

## Exercício 7: Query Parameters

1. **Produtos com preço menor que R$ 100**
   - GET /api/produtos?preco_max=100

2. **Usuários da cidade "Salvador"**
   - GET /api/usuarios?cidade=Salvador

3. **Página 2, 20 itens por página**
   - GET /api/produtos?page=2&limit=20

4. **Produtos ordenados por preço (crescente)**
   - GET /api/produtos?sort=preco&order=asc

5. **Usuários com idade entre 18 e 30**
   - GET /api/usuarios?idade_min=18&idade_max=30

6. **Produtos que contenham "notebook" no nome**
   - GET /api/produtos?search=notebook

---

## Exercício 8: Respostas de Erro

1. **Email já existente:**
```json
HTTP/1.1 409 Conflict
{
  "erro": "Email já cadastrado",
  "detalhes": {
    "email": "Este email já está em uso"
  },
  "codigo": "EMAIL_DUPLICADO"
}
```

2. **Produto não encontrado:**
```json
HTTP/1.1 404 Not Found
{
  "erro": "Produto não encontrado",
  "detalhes": {
    "id": 123
  },
  "codigo": "PRODUTO_NAO_ENCONTRADO"
}
```

3. **Sem autenticação:**
```json
HTTP/1.1 401 Unauthorized
{
  "erro": "Não autenticado",
  "detalhes": {
    "mensagem": "Token de autenticação necessário"
  },
  "codigo": "NAO_AUTENTICADO"
}
```

4. **Dados inválidos:**
```json
HTTP/1.1 400 Bad Request
{
  "erro": "Dados inválidos",
  "detalhes": {
    "nome": "Nome é obrigatório"
  },
  "codigo": "DADOS_INVALIDOS"
}
```

5. **Erro interno:**
```json
HTTP/1.1 500 Internal Server Error
{
  "erro": "Erro interno do servidor",
  "detalhes": {
    "mensagem": "Ocorreu um erro ao processar a requisição"
  },
  "codigo": "ERRO_INTERNO"
}
```

---

## Exercício 9: Versionamento de API

1. **URLs versionadas:**
   - v1.0: GET /api/v1/usuarios
   - v2.0: GET /api/v2/usuarios

2. **Manter compatibilidade:**
   - Manter v1.0 funcionando
   - Documentar mudanças
   - Avisar sobre depreciação
   - Fornecer período de migração

3. **Exemplos:**
```
GET /api/v1/usuarios  → Versão antiga (mantida)
GET /api/v2/usuarios  → Versão nova
GET /api/usuarios     → Versão padrão (pode redirecionar para v2)
```

---

## Exercício 10: Análise de API Real

**Exemplo: GitHub API**

1. **Métodos HTTP:** GET, POST, PUT, PATCH, DELETE
2. **Estrutura de URLs:**
   - GET /users/{username}
   - GET /repos/{owner}/{repo}
   - GET /repos/{owner}/{repo}/issues
3. **Status codes:** 200, 201, 204, 400, 401, 403, 404, 500
4. **Formato:** JSON
5. **Tratamento de erros:**
```json
{
  "message": "Not Found",
  "documentation_url": "https://docs.github.com/..."
}
```
6. **Versionamento:** Sim, via header `Accept: application/vnd.github.v3+json`

---

## Exercício 11: Consumo de API com Python (GET + print)

```python
import requests

# Exemplo 1: JSONPlaceholder
resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(resp.json())

# Exemplo 2: ViaCEP
resp = requests.get("https://viacep.com.br/ws/01001000/json/")
print(resp.json())
```

Se estiver no **Jupyter**, basta executar a célula. No **editor**, salve em `consumo_api.py` e rode:
```
python consumo_api.py
```

