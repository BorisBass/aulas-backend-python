# BEP-012: Explicações da Prática SQL

## 📋 Guia de Explicações para a Prática no Google Colab

Este documento explica cada parte da prática SQL criada para a BEP-012, detalhando os conceitos e comandos utilizados.

---

## 1. Configuração Inicial

### Importações Necessárias
```python
import sqlite3
import pandas as pd
```

**Explicação:**
- `sqlite3`: Módulo nativo do Python para trabalhar com bancos SQLite
- `pandas`: Biblioteca para manipulação e análise de dados (já disponível no Colab)

### Conexão com Banco
```python
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
```

**Explicação:**
- `:memory:`: Cria um banco de dados temporário na memória RAM
- `cursor`: Objeto para executar comandos SQL
- Vantagem: Não precisa salvar arquivos, ideal para prática

---

## 2. Comandos DDL (Data Definition Language)

### CREATE TABLE
```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT,
    telefone TEXT,
    cidade TEXT
)
```

**Explicação:**
- `INTEGER PRIMARY KEY`: Chave primária auto-incremento
- `TEXT NOT NULL`: Campo obrigatório de texto
- `TEXT`: Campo opcional de texto
- `REAL`: Número decimal (para preços)

### ALTER TABLE
```sql
ALTER TABLE clientes ADD COLUMN data_cadastro DATE
```

**Explicação:**
- Adiciona nova coluna a uma tabela existente
- `DATE`: Tipo de dados para datas
- Útil para evolução do banco sem perder dados

### PRAGMA table_info
```sql
PRAGMA table_info(clientes)
```

**Explicação:**
- Comando SQLite para verificar estrutura da tabela
- Retorna informações sobre colunas, tipos e restrições

---

## 3. Comandos DML (Data Manipulation Language)

### INSERT - Inserção Simples
```sql
INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro)
VALUES ('João Silva', 'joao@email.com', '(71) 99999-1111', 'Salvador', '2024-01-15')
```

**Explicação:**
- `INSERT INTO`: Comando para inserir dados
- Lista de colunas entre parênteses (opcional, mas recomendado)
- `VALUES`: Valores correspondentes às colunas

### INSERT - Inserção Múltipla
```python
cursor.executemany('''
INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro)
VALUES (?, ?, ?, ?, ?)
''', clientes)
```

**Explicação:**
- `executemany()`: Executa o mesmo comando para múltiplos registros
- `?`: Placeholders para valores (evita SQL injection)
- Lista de tuplas com os dados

---

## 4. Comandos de Consulta (SELECT)

### SELECT Básico
```sql
SELECT * FROM clientes
```

**Explicação:**
- `SELECT *`: Seleciona todas as colunas
- `FROM clientes`: Especifica a tabela
- `*`: Curinga para todas as colunas

### SELECT com Colunas Específicas
```sql
SELECT nome, email FROM clientes
```

**Explicação:**
- Lista apenas as colunas desejadas
- Melhor performance que `SELECT *`
- Mais claro sobre quais dados retornar

---

## 5. Filtros e Ordenação

### WHERE - Filtro por Condição
```sql
SELECT nome, email, cidade FROM clientes WHERE cidade = 'Salvador'
```

**Explicação:**
- `WHERE`: Cláusula para filtrar registros
- `=`: Operador de igualdade
- Apenas registros que atendem à condição

### ORDER BY - Ordenação
```sql
SELECT nome, preco FROM produtos ORDER BY preco DESC
```

**Explicação:**
- `ORDER BY`: Ordena os resultados
- `DESC`: Ordem decrescente (maior para menor)
- `ASC`: Ordem crescente (padrão, pode omitir)

### LIMIT - Limitar Resultados
```sql
SELECT nome, cidade FROM clientes LIMIT 3
```

**Explicação:**
- `LIMIT`: Limita número de registros retornados
- Útil para paginação e performance
- Sempre usar com ORDER BY para resultados consistentes

### LIKE - Busca por Padrão
```sql
SELECT nome, email FROM clientes WHERE nome LIKE 'A%'
```

**Explicação:**
- `LIKE`: Busca por padrões em texto
- `%`: Curinga para qualquer sequência de caracteres
- `'A%'`: Nomes que começam com 'A'

### Filtros Combinados
```sql
SELECT nome, preco, estoque 
FROM produtos 
WHERE estoque > 20 
ORDER BY nome
```

**Explicação:**
- Múltiplas cláusulas podem ser combinadas
- `WHERE` sempre antes de `ORDER BY`
- `>`: Operador maior que

---

## 6. Integração com Pandas

### Carregar Dados no Pandas
```python
df_clientes = pd.read_sql_query("SELECT * FROM clientes", conn)
```

**Explicação:**
- `pd.read_sql_query()`: Executa SQL e retorna DataFrame
- DataFrame: Estrutura de dados do pandas (como tabela)
- Facilita análise e visualização dos dados

---

## 7. Boas Práticas

### 1. Sempre Fechar Conexão
```python
conn.close()
```

**Explicação:**
- Libera recursos do sistema
- Evita vazamentos de memória
- Boa prática de programação

### 2. Usar Placeholders (?)
```python
cursor.execute("SELECT * FROM clientes WHERE cidade = ?", ('Salvador',))
```

**Explicação:**
- Evita SQL injection
- Mais seguro que concatenação de strings
- Melhor performance

### 3. Verificar Resultados
```python
if cliente_novo:
    print(f"Cliente encontrado: {cliente_novo[0]}")
```

**Explicação:**
- `fetchone()` retorna `None` se não encontrar
- Sempre verificar antes de usar
- Evita erros de atributo

---

## 8. Conceitos Importantes

### Tipos de Dados SQLite
- `INTEGER`: Números inteiros
- `REAL`: Números decimais
- `TEXT`: Texto
- `DATE`: Data (armazenada como texto)
- `BLOB`: Dados binários

### Operadores de Comparação
- `=`: Igual
- `!=` ou `<>`: Diferente
- `>`: Maior que
- `<`: Menor que
- `>=`: Maior ou igual
- `<=`: Menor ou igual

### Operadores Lógicos
- `AND`: E lógico
- `OR`: OU lógico
- `NOT`: Negação

### Curingas do LIKE
- `%`: Qualquer sequência de caracteres
- `_`: Qualquer caractere único

---

## 9. Exercícios e Soluções

### Exercício 1: Consultas Básicas
**Objetivo:** Praticar SELECT com filtros simples

**Soluções:**
1. Produtos < R$ 200: `WHERE preco < 200`
2. Nomes com 'A': `WHERE nome LIKE 'A%'`
3. Mais caros: `ORDER BY preco DESC LIMIT 2`

### Exercício 2: Inserção
**Objetivo:** Praticar INSERT e verificação

**Conceitos:**
- Inserção de dados
- Verificação com SELECT
- Uso de `fetchone()`

### Desafio Final
**Objetivo:** Combinar múltiplos conceitos

**Conceitos:**
- Filtro por data: `WHERE data_cadastro LIKE '2024%'`
- Ordenação: `ORDER BY data_cadastro DESC`
- Limitação: `LIMIT 3`

---

## 10. Próximos Passos

### Conceitos Avançados (BEP-013 em diante)
- UPDATE: Modificar dados existentes
- DELETE: Remover registros
- JOINs: Relacionar tabelas
- Funções agregadas: COUNT, SUM, AVG
- Subconsultas
- Índices e performance

### Recursos Adicionais
- Documentação oficial SQLite
- Prática com bancos reais
- Projetos práticos
- Normalização de dados

---

## 📝 Notas Importantes

1. **SQLite é case-insensitive** para palavras-chave
2. **Strings devem estar entre aspas simples**
3. **Números não precisam de aspas**
4. **Sempre testar comandos antes de usar em produção**
5. **Backup é essencial em bancos reais**

---

**Este guia serve como referência para entender cada parte da prática SQL da BEP-012.**
