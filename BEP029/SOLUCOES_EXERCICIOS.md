# Soluções - Exercícios BEP029: Conceitos Fundamentais de WebServices

## Exercício 1: Identificando WebServices

**Exemplos de Respostas:**

1. **WhatsApp**
   - Tipo: REST
   - Dados: Mensagens, status, contatos, mídia
   - Protocolo: HTTPS

2. **Netflix**
   - Tipo: REST
   - Dados: Catálogo de filmes, progresso de visualização, recomendações
   - Protocolo: HTTPS

3. **Uber**
   - Tipo: REST
   - Dados: Localização, corridas, motoristas, pagamentos
   - Protocolo: HTTPS

4. **Gmail**
   - Tipo: REST (Gmail API)
   - Dados: Emails, anexos, contatos
   - Protocolo: HTTPS

5. **Spotify**
   - Tipo: REST
   - Dados: Músicas, playlists, artistas, recomendações
   - Protocolo: HTTPS

---

## Exercício 2: Comparando SOAP vs REST

1. **API pública para desenvolvedores de rede social**
   - **Resposta:** REST
   - **Por quê:** APIs públicas modernas geralmente usam REST por ser mais simples, rápida e fácil de usar. Desenvolvedores preferem REST.

2. **Sistema bancário com segurança robusta**
   - **Resposta:** SOAP
   - **Por quê:** Sistemas bancários precisam de segurança robusta (WS-Security), transações ACID e contratos formais (WSDL). SOAP oferece isso.

3. **API de aplicativo mobile**
   - **Resposta:** REST
   - **Por quê:** REST é mais leve (JSON), mais rápido e consome menos dados, ideal para mobile.

4. **Integração entre sistemas legados**
   - **Resposta:** SOAP
   - **Por quê:** Sistemas legados muitas vezes já usam SOAP e têm contratos WSDL definidos.

5. **Microserviço moderno**
   - **Resposta:** REST
   - **Por quê:** Microserviços modernos priorizam simplicidade, velocidade e flexibilidade, características do REST.

---

## Exercício 3: Formatos de Dados

### XML:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<produto>
    <id>123</id>
    <nome>Notebook Dell</nome>
    <preco>3500.00</preco>
    <categoria>Eletrônicos</categoria>
    <estoque>15</estoque>
    <fornecedor>
        <nome>TechStore</nome>
        <cnpj>12.345.678/0001-90</cnpj>
    </fornecedor>
</produto>
```

### JSON:
```json
{
  "id": 123,
  "nome": "Notebook Dell",
  "preco": 3500.00,
  "categoria": "Eletrônicos",
  "estoque": 15,
  "fornecedor": {
    "nome": "TechStore",
    "cnpj": "12.345.678/0001-90"
  }
}
```

**Comparação:**
- **Tamanho:** JSON é menor (mais compacto)
- **Legibilidade:** Ambos são legíveis, mas JSON é mais simples
- **Uso:** JSON é mais comum em APIs REST modernas

---

## Exercício 4: Protocolos HTTP vs HTTPS

1. **Site de notícias públicas**
   - **Resposta:** HTTPS (recomendado) ou HTTP
   - **Por quê:** Mesmo sem dados sensíveis, HTTPS protege contra interceptação e melhora SEO.

2. **Sistema de e-commerce com pagamento**
   - **Resposta:** HTTPS (obrigatório)
   - **Por quê:** Dados de pagamento são extremamente sensíveis. HTTPS é obrigatório.

3. **API de login e autenticação**
   - **Resposta:** HTTPS (obrigatório)
   - **Por quê:** Senhas e tokens devem ser criptografados durante transmissão.

4. **Blog pessoal sem dados sensíveis**
   - **Resposta:** HTTPS (recomendado) ou HTTP
   - **Por quê:** HTTPS é melhor, mas HTTP pode ser aceitável se não houver dados sensíveis.

5. **Sistema bancário online**
   - **Resposta:** HTTPS (obrigatório)
   - **Por quê:** Dados financeiros são extremamente sensíveis. HTTPS é obrigatório.

---

## Exercício 5: Arquitetura de WebServices

**Diagrama de Comunicação:**

```
┌─────────────────┐
│  E-commerce     │
│  (Cliente)      │
└────────┬────────┘
         │
         ├─── GET /estoque/produto/123 ────┐
         │                                  │
         ├─── POST /pagamento/processar ────┤
         │                                  │
         ├─── GET /frete/calcular ──────────┤
         │                                  │
         └─── POST /notificacoes/enviar ────┤
                                            │
         ┌──────────────────────────────────┴──────────┐
         │                                             │
    ┌────▼────┐  ┌──────────┐  ┌──────┐  ┌──────────┐ │
    │ Estoque │  │Pagamento│  │Frete │  │Notif.    │ │
    │(Servidor)│  │(Servidor)│ │(Serv.)│ │(Servidor)│ │
    └─────────┘  └──────────┘  └──────┘  └──────────┘ │
```

**Comunicação:
- E-commerce (Cliente) → Estoque (Servidor): Verifica disponibilidade
- E-commerce (Cliente) → Pagamento (Servidor): Processa pagamento
- E-commerce (Cliente) → Frete (Servidor): Calcula entrega
- E-commerce (Cliente) → Notificações (Servidor): Envia emails

**Protocolo:** HTTPS (dados sensíveis)
**Formato:** JSON

---

## Exercício 6: Casos de Uso Reais

**Exemplo: Aplicativo de Delivery**

1. **Comunicação com restaurante:**
   - GET /api/restaurantes/{id}/cardapio - Busca cardápio
   - POST /api/pedidos - Cria pedido
   - GET /api/pedidos/{id}/status - Verifica status

2. **Localização do entregador:**
   - GET /api/entregadores/{id}/localizacao - Busca localização atual
   - WebSocket para atualizações em tempo real

3. **Pagamento:**
   - POST /api/pagamentos/processar - Processa pagamento
   - Protocolo: HTTPS (obrigatório)
   - Formato: JSON

---

## Exercício 7: Análise de API Pública

**Exemplo: GitHub API**

1. **Tipo:** REST
2. **Protocolo:** HTTPS
3. **Formato:** JSON
4. **Endpoints:**
   - GET /users/{username}
   - GET /repos/{owner}/{repo}
   - GET /repos/{owner}/{repo}/issues
5. **Métodos HTTP:** GET, POST, PUT, PATCH, DELETE

---

## Exercício 8: Criando um Exemplo Simples

**Sistema de Biblioteca - Modelagem:**

### 1. Recurso: Livros
- **Operações:**
  - GET /api/livros - Lista todos
  - GET /api/livros/{id} - Busca por ID
  - POST /api/livros - Cria novo
  - PUT /api/livros/{id} - Atualiza
  - DELETE /api/livros/{id} - Deleta
- **Dados:** ID, Título, Autor, ISBN, Ano, Disponível
- **Formato:** JSON

### 2. Recurso: Usuários
- **Operações:**
  - GET /api/usuarios - Lista todos
  - GET /api/usuarios/{id} - Busca por ID
  - POST /api/usuarios - Cria novo
  - PATCH /api/usuarios/{id} - Atualiza parcialmente
  - DELETE /api/usuarios/{id} - Deleta
- **Dados:** ID, Nome, Email, Telefone, Tipo
- **Formato:** JSON

### 3. Recurso: Empréstimos
- **Operações:**
  - GET /api/emprestimos - Lista todos
  - GET /api/emprestimos/{id} - Busca por ID
  - POST /api/emprestimos - Cria novo empréstimo
  - PATCH /api/emprestimos/{id} - Devolve livro (atualiza status)
- **Dados:** ID, Livro_ID, Usuario_ID, Data_Emprestimo, Data_Devolucao, Status
- **Formato:** JSON

**Comunicação:**
- Cliente (Sistema Web/Mobile) → Servidor (API Biblioteca)
- Protocolo: HTTPS
- Formato: JSON
- Tipo: REST

