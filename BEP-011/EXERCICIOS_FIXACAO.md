# BEP-011 — Exercícios de Fixação
## Introdução a Banco de Dados Relacionais

### 📋 **Instruções Gerais**
- Resolva os exercícios na ordem apresentada
- Use o Google Colab para praticar com SQLite
- Consulte o `README_LAB_COLAB.md` para comandos básicos
- Anote suas dúvidas para discussão em aula

---

## 🟢 **NÍVEL BÁSICO** (Conceitos Fundamentais)

### **Exercício 1: Identificação de Componentes**
Analise a tabela abaixo e responda:

| ID | Nome | Email | Idade | Cidade |
|----|------|-------|-------|--------|
| 1  | Ana Silva | ana@email.com | 25 | Salvador |
| 2  | Carlos Santos | carlos@email.com | 30 | São Paulo |
| 3  | Maria Lima | maria@email.com | 22 | Rio de Janeiro |

**Perguntas:**
a) Qual é a chave primária? Justifique sua escolha.
b) Identifique o tipo de dados adequado para cada coluna.
c) Quantos registros e quantas colunas existem?
d) Se você fosse adicionar uma coluna "Telefone", qual seria o tipo mais adequado?

### **Exercício 2: Relacional vs Não Relacional**
Para cada situação abaixo, indique se seria melhor usar um banco **relacional** ou **não relacional** e justifique:

a) Sistema bancário com contas, transações e clientes
b) Aplicativo de chat com mensagens em tempo real
c) E-commerce com produtos, pedidos e estoque
d) Sistema de logs de um servidor web
e) Rede social com posts, comentários e curtidas

### **Exercício 3: Chaves Primárias e Estrangeiras**
Dadas as tabelas:

**Tabela: Autores**
| ID | Nome | Nacionalidade |
|----|------|---------------|
| 1  | Machado de Assis | Brasileira |
| 2  | José Saramago | Portuguesa |

**Tabela: Livros**
| ID | Título | Autor_ID | Ano |
|----|--------|----------|-----|
| 1  | Dom Casmurro | 1 | 1899 |
| 2  | Ensaio sobre a Cegueira | 2 | 1995 |
| 3  | Memórias Póstumas | 1 | 1881 |

**Perguntas:**
a) Identifique as chaves primárias de cada tabela.
b) Identifique a chave estrangeira e explique o relacionamento.
c) Que tipo de relacionamento existe entre Autor e Livro?
d) Quantos livros cada autor escreveu?

---

## 🟡 **NÍVEL INTERMEDIÁRIO** (Modelagem e Constraints)

### **Exercício 4: Modelo Entidade-Relacionamento**
Desenhe um diagrama ER para um sistema de **biblioteca** com as seguintes regras:
- Um usuário pode pegar vários livros emprestados
- Um livro pode ser emprestado por vários usuários (em momentos diferentes)
- Cada empréstimo tem data de início e fim
- Um livro pode ter vários autores
- Um autor pode escrever vários livros

**Entidades sugeridas:** Usuário, Livro, Autor, Empréstimo

### **Exercício 5: Constraints e Validações**
Crie o comando SQL para a tabela `funcionarios` com as seguintes regras:
- ID: chave primária, auto-incremento
- Nome: obrigatório, máximo 100 caracteres
- Email: único, obrigatório
- Salário: obrigatório, deve ser maior que zero
- Data_contratacao: obrigatória, padrão data atual
- Departamento_ID: chave estrangeira para tabela departamentos

### **Exercício 6: Integridade Referencial**
Considere as tabelas:

```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto TEXT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

**Perguntas:**
a) O que acontece se tentarmos deletar um cliente que tem pedidos?
b) Como modificar a tabela pedidos para que, ao deletar um cliente, seus pedidos sejam automaticamente deletados?
c) Como modificar para que, ao deletar um cliente, os pedidos tenham cliente_id = NULL?

---

## 🔴 **NÍVEL AVANÇADO** (Prática com SQLite)

### **Exercício 7: Implementação no Colab**
No Google Colab, implemente o seguinte sistema:

**Tabelas:**
1. `cursos` (id, nome, carga_horaria)
2. `alunos` (id, nome, email, data_nascimento)
3. `matriculas` (id, aluno_id, curso_id, data_matricula, status)

**Dados de exemplo:**
- 3 cursos: Python (40h), SQL (20h), Web (60h)
- 4 alunos com dados completos
- 6 matrículas (alguns alunos em múltiplos cursos)

**Consultas a implementar:**
a) Listar todos os alunos matriculados em Python
b) Contar quantos alunos estão em cada curso
c) Mostrar alunos que não estão matriculados em nenhum curso
d) Listar cursos com mais de 2 alunos matriculados

### **Exercício 8: Análise de Dados**
Use os arquivos CSV fornecidos (`dados_clientes.csv` e `dados_pedidos.csv`) para:

a) Importar os dados no SQLite
b) Calcular o ticket médio por cliente
c) Identificar o cliente que mais gastou
d) Listar clientes que não fizeram pedidos
e) Calcular o total de vendas por mês (assumindo que as datas são de 2025)

### **Exercício 9: Otimização e Boas Práticas**
Para o sistema de biblioteca do Exercício 4:

a) Crie índices para melhorar a performance das consultas mais comuns
b) Implemente uma view que mostre livros disponíveis (não emprestados)
c) Crie um trigger que atualize automaticamente a data de devolução quando um livro for devolvido
d) Implemente validações para evitar empréstimos de livros já emprestados

---

## 🎯 **EXERCÍCIOS DESAFIO**

### **Exercício 10: Sistema Completo**
Projete e implemente um sistema de **controle de estoque** com:

**Requisitos:**
- Produtos com código, nome, preço, estoque mínimo
- Fornecedores com CNPJ, nome, contato
- Movimentações (entrada/saída) com data, quantidade, motivo
- Relatórios de produtos em falta
- Histórico de movimentações por período

**Entregáveis:**
1. Diagrama ER completo
2. Scripts SQL de criação das tabelas
3. Dados de exemplo (pelo menos 10 produtos, 3 fornecedores, 20 movimentações)
4. 5 consultas úteis para o negócio
5. Relatório de produtos com estoque abaixo do mínimo

### **Exercício 11: Análise de Performance**
Com base no sistema do Exercício 10:

a) Identifique as consultas mais lentas
b) Proponha índices para otimização
c) Analise o uso de memória e espaço em disco
d) Sugira melhorias na estrutura das tabelas

---

## 📚 **RECURSOS PARA RESOLUÇÃO**

### **Ferramentas Recomendadas:**
- **Google Colab**: Para prática com SQLite
- **DB Fiddle**: Para testes rápidos de SQL
- **Draw.io**: Para diagramas ER
- **SQLite Browser**: Para visualização de dados (opcional)

### **Documentação:**
- `README_LAB_COLAB.md`: Guia completo de SQLite no Colab
- `PLANO_DA_AULA.md`: Conceitos abordados na aula
- Slides BEP-011: Revisão dos conceitos

### **Dicas:**
1. Comece sempre pelo diagrama ER antes de criar as tabelas
2. Use nomes descritivos para tabelas e colunas
3. Sempre defina constraints apropriadas
4. Teste suas consultas com dados de exemplo
5. Documente suas decisões de modelagem

---

## ✅ **CRITÉRIOS DE AVALIAÇÃO**

### **Pontuação Sugerida:**
- **Nível Básico** (Exercícios 1-3): 30 pontos
- **Nível Intermediário** (Exercícios 4-6): 40 pontos  
- **Nível Avançado** (Exercícios 7-9): 50 pontos
- **Desafio** (Exercícios 10-11): 30 pontos

**Total: 150 pontos**

### **Entrega:**
- Código SQL comentado
- Diagramas ER (se aplicável)
- Explicação das decisões de modelagem
- Resultados das consultas

---

**Boa sorte e bons estudos! 🚀**
