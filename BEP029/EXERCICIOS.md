# Exercícios Práticos - BEP029: Conceitos Fundamentais de WebServices

## Exercício 1: Identificando WebServices

**Objetivo:** Identificar WebServices em aplicações do dia a dia.

**Tarefa:**
1. Liste 5 aplicativos ou sites que você usa regularmente
2. Para cada um, identifique:
   - Que tipo de WebService eles provavelmente usam (SOAP ou REST)
   - Que dados são trocados (ex: informações de login, posts, mensagens)
   - Que protocolo é usado (HTTP ou HTTPS)

**Exemplo:**
- **Aplicativo:** Instagram
  - **Tipo:** REST
  - **Dados:** Fotos, comentários, likes, stories
  - **Protocolo:** HTTPS

---

## Exercício 2: Comparando SOAP vs REST

**Objetivo:** Entender quando usar cada tipo de WebService.

**Tarefa:**
Para cada cenário abaixo, indique se você usaria SOAP ou REST e explique o porquê:

1. API pública para desenvolvedores de um aplicativo de rede social
2. Sistema bancário que precisa de segurança robusta e transações
3. API de um aplicativo mobile para buscar dados do servidor
4. Integração entre sistemas corporativos legados
5. Microserviço moderno que precisa ser rápido e simples

---

## Exercício 3: Formatos de Dados

**Objetivo:** Praticar criação de estruturas em XML e JSON.

**Tarefa:**
Crie estruturas de dados para representar um **Produto** com as seguintes informações:
- ID: 123
- Nome: "Notebook Dell"
- Preço: 3500.00
- Categoria: "Eletrônicos"
- Estoque: 15
- Fornecedor:
  - Nome: "TechStore"
  - CNPJ: "12.345.678/0001-90"

Crie a estrutura em:
1. **XML**
2. **JSON**

Compare o tamanho e legibilidade de cada formato.

---

## Exercício 4: Protocolos HTTP vs HTTPS

**Objetivo:** Entender a importância da segurança.

**Tarefa:**
Para cada situação abaixo, indique se HTTP ou HTTPS seria mais apropriado e explique:

1. Site de notícias públicas
2. Sistema de e-commerce com pagamento
3. API de login e autenticação
4. Blog pessoal sem dados sensíveis
5. Sistema bancário online

---

## Exercício 5: Arquitetura de WebServices

**Objetivo:** Modelar a comunicação entre sistemas.

**Tarefa:**
Desenhe um diagrama (texto ou desenho) mostrando como os seguintes sistemas se comunicariam via WebServices:

**Sistema de E-commerce:**
- Sistema de Estoque (verifica disponibilidade)
- Gateway de Pagamento (processa pagamentos)
- Sistema de Frete (calcula entrega)
- Sistema de Notificações (envia emails)

Mostre:
1. Quem é o cliente e quem é o servidor em cada comunicação
2. Que tipo de dados são trocados
3. Que protocolo é usado

---

## Exercício 6: Casos de Uso Reais

**Objetivo:** Identificar WebServices em situações reais.

**Tarefa:**
Escolha uma das situações abaixo e descreva como WebServices seriam usados:

1. **Aplicativo de Delivery:**
   - Como o app se comunica com o restaurante?
   - Como verifica a localização do entregador?
   - Como processa o pagamento?

2. **Sistema de Streaming:**
   - Como busca os vídeos disponíveis?
   - Como rastreia o progresso de visualização?
   - Como recomenda novos conteúdos?

3. **Rede Social:**
   - Como carrega o feed de posts?
   - Como envia mensagens?
   - Como atualiza o status online?

---

## Exercício 7: Análise de API Pública

**Objetivo:** Explorar uma API real.

**Tarefa:**
Escolha uma API pública (ex: GitHub API, OpenWeatherMap, etc.) e responda:

1. Que tipo de WebService é? (SOAP ou REST)
2. Que protocolo usa? (HTTP ou HTTPS)
3. Que formato de dados retorna? (JSON, XML, etc.)
4. Liste 3 endpoints (URLs) disponíveis
5. Que métodos HTTP são suportados?

**Dica:** Muitas APIs públicas têm documentação online. Use isso como referência.

---

## Exercício 8: Criando um Exemplo Simples

**Objetivo:** Praticar modelagem de WebService.

**Tarefa:**
Modele um WebService simples para um **Sistema de Biblioteca**:

1. Liste os recursos principais (ex: Livros, Usuários, Empréstimos)
2. Para cada recurso, defina:
   - Que operações são necessárias (buscar, criar, atualizar, deletar)
   - Que dados são trocados
   - Que formato usar (JSON ou XML)
3. Descreva como os sistemas se comunicariam

**Exemplo:**
- **Recurso:** Livros
  - **Operações:** Buscar todos, Buscar por ID, Criar novo, Atualizar, Deletar
  - **Dados:** ID, Título, Autor, ISBN, Ano
  - **Formato:** JSON

---

## Respostas e Soluções

As soluções detalhadas estão disponíveis no arquivo `SOLUCOES_EXERCICIOS.md`.

