# Exercícios Práticos - BEP030: RESTful Web Services e Métodos HTTP

## Exercício 1: Identificando Métodos HTTP

**Objetivo:** Associar operações com métodos HTTP corretos.

**Tarefa:**
Para cada operação abaixo, indique qual método HTTP seria usado e explique:

1. Buscar lista de todos os produtos
2. Criar um novo produto
3. Atualizar o preço de um produto específico
4. Deletar um produto
5. Buscar informações de um produto específico
6. Atualizar todos os dados de um produto

---

## Exercício 2: Modelando URLs RESTful

**Objetivo:** Criar URLs RESTful para um sistema.

**Tarefa:**
Crie as URLs RESTful para um **Sistema de Blog** com os seguintes recursos:
- Posts (título, conteúdo, autor, data)
- Comentários (post, autor, conteúdo, data)
- Autores (nome, email, bio)

Para cada recurso, crie URLs para:
- Listar todos
- Buscar por ID
- Criar novo
- Atualizar
- Deletar

---

## Exercício 3: Status Codes

**Objetivo:** Associar situações com status codes apropriados.

**Tarefa:**
Para cada situação abaixo, indique qual status code HTTP seria retornado:

1. Usuário criado com sucesso
2. Produto não encontrado
3. Dados inválidos enviados
4. Usuário não autenticado
5. Usuário autenticado mas sem permissão
6. Erro interno no servidor
7. Produto atualizado com sucesso
8. Produto deletado com sucesso
9. Recurso criado e retornado
10. Requisição bem-sucedida sem conteúdo

---

## Exercício 4: PUT vs PATCH

**Objetivo:** Entender quando usar PUT ou PATCH.

**Tarefa:**
Para cada situação, indique se usaria PUT ou PATCH:

1. Atualizar apenas o email de um usuário
2. Atualizar todos os dados de um produto
3. Marcar um pedido como "entregue"
4. Atualizar nome, email e telefone de um cliente
5. Alterar apenas o status de um pedido

---

## Exercício 5: Corrigindo URLs Não-RESTful

**Objetivo:** Identificar e corrigir URLs que não seguem padrões REST.

**Tarefa:**
Reescreva as URLs abaixo seguindo os princípios REST:

1. `/api/getUser?id=123`
2. `/api/createProduct`
3. `/api/updateOrder/456`
4. `/api/deleteItem/789`
5. `/api/user/123/orders`
6. `/api/listProducts`
7. `/api/searchUsers?q=João`

---

## Exercício 6: Criando Endpoints Completos

**Objetivo:** Modelar endpoints REST completos.

**Tarefa:**
Crie os endpoints REST completos (método HTTP + URL + descrição) para um **Sistema de Tarefas (To-Do)**:

**Recursos:**
- Tarefas (id, título, descrição, concluída, data_criacao)
- Categorias (id, nome, cor)
- Usuários (id, nome, email)

**Requisitos:**
- Listar todas as tarefas
- Criar nova tarefa
- Buscar tarefa específica
- Atualizar tarefa (marcar como concluída)
- Deletar tarefa
- Listar tarefas de uma categoria
- Listar tarefas de um usuário

---

## Exercício 7: Query Parameters

**Objetivo:** Usar query parameters para filtros e paginação.

**Tarefa:**
Crie as URLs com query parameters para as seguintes situações:

1. Buscar produtos com preço menor que R$ 100
2. Buscar usuários da cidade "Salvador"
3. Listar produtos da página 2, com 20 itens por página
4. Buscar produtos ordenados por preço (crescente)
5. Buscar usuários com idade entre 18 e 30 anos
6. Buscar produtos que contenham "notebook" no nome

---

## Exercício 8: Respostas de Erro

**Objetivo:** Criar respostas de erro apropriadas.

**Tarefa:**
Para cada situação de erro, crie uma resposta JSON apropriada com status code:

1. Tentativa de criar usuário com email já existente
2. Tentativa de buscar produto que não existe
3. Tentativa de deletar produto sem autenticação
4. Tentativa de criar produto com dados inválidos (nome vazio)
5. Erro interno no servidor ao processar requisição

**Formato esperado:**
```json
{
  "erro": "Descrição do erro",
  "detalhes": {...},
  "codigo": "CÓDIGO_ERRO"
}
```

---

## Exercício 9: Versionamento de API

**Objetivo:** Entender versionamento de APIs.

**Tarefa:**
Você tem uma API que precisa evoluir. A versão 1.0 tem:
- GET /api/usuarios
- POST /api/usuarios

Na versão 2.0, você quer mudar a estrutura de resposta de usuários.

1. Como você versionaria essas URLs?
2. Como manteria compatibilidade com clientes da v1.0?
3. Crie exemplos de URLs versionadas

---

## Exercício 10: Análise de API Real

**Objetivo:** Analisar uma API REST real.

**Tarefa:**
Escolha uma API REST pública (GitHub, Twitter, etc.) e analise:

1. Que métodos HTTP são usados?
2. Como são estruturadas as URLs?
3. Que status codes são retornados?
4. Que formato de dados é usado (JSON/XML)?
5. Como são tratados erros?
6. A API é versionada? Como?

---

## Exercício 11: Consumo de API com Python (GET + print)

**Objetivo:** Consumir uma API pública usando Python.

**Tarefa:**
Execute os passos abaixo no **Jupyter Notebook** ou diretamente no **editor**:

1. Instale a biblioteca `requests`:
   ```
   pip install requests
   ```
2. Faça uma requisição GET e imprima o JSON:
   - API de posts: `https://jsonplaceholder.typicode.com/posts/1`
   - API de CEP: `https://viacep.com.br/ws/01001000/json/`

**Saída esperada:** dicionário com os dados retornados pelas APIs.

---

## Respostas e Soluções

As soluções detalhadas estão disponíveis no arquivo `SOLUCOES_EXERCICIOS.md`.

