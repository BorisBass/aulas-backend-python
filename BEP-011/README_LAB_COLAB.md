## BEP-011 — Guia de Laboratório no Google Colab (Python + SQLite)

Este guia detalha os comandos de conexão e operações básicas com SQLite usando Python no Google Colab. É uma continuação prática dos conceitos da aula.

### 1) Preparação
- Acesse: https://colab.research.google.com/#create=true
- O Colab já tem o módulo `sqlite3` embutido no Python. Não é necessário instalar nada.

### 2) Conectando ao SQLite
O SQLite funciona em arquivo único (.db) ou inteiramente em memória. No Colab, ambas as opções são úteis.

#### 2.1 Conexão em memória (volátil)
```python
import sqlite3

connection = sqlite3.connect(":memory:")  # não cria arquivo; ideal para testes rápidos
cursor = connection.cursor()               # cria um cursor para executar comandos SQL
```
Características:
- Velocidade alta para testes.
- O banco é perdido quando a conexão é fechada ou a sessão é reiniciada.

#### 2.2 Conexão em arquivo (persistente)
```python
import sqlite3

connection = sqlite3.connect("meu_banco.db")  # cria/abre um arquivo .db no ambiente do Colab
cursor = connection.cursor()
```
Características:
- Persiste entre células/notebook enquanto o arquivo existir no ambiente.
- Você pode baixar o arquivo .db no final do laboratório.

#### 2.3 Parâmetros úteis de `connect`
```python
sqlite3.connect(database, timeout=5.0, detect_types=0, isolation_level=None)
```
- `database`: caminho do arquivo ou `":memory:"`.
- `timeout`: tempo (em segundos) para aguardar locks de banco.
- `detect_types`: permite parsing de tipos; use `sqlite3.PARSE_DECLTYPES` para mapear `DATE`, etc.
- `isolation_level`: controla transações. `None` ativa autocommit; strings como `'DEFERRED'`, `'IMMEDIATE'`, `'EXCLUSIVE'` definem o modo de transação.

Exemplos:
```python
# autocommit ligado (toda instrução é confirmada automaticamente)
connection = sqlite3.connect("meu_banco.db", isolation_level=None)

# transações manuais (padrão). Use connection.commit() ao final
connection = sqlite3.connect("meu_banco.db")
```

### 3) Criando tabelas
```python
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT UNIQUE,
        idade INTEGER
    );
    """
)
connection.commit()  # confirma alterações quando não está em autocommit
```

### 4) Inserindo dados
```python
dados = [
    (1, "Ana Silva", "ana@example.com", 25),
    (2, "Carlos Santos", "carlos@example.com", 30),
    (3, "João Souza", "joao@example.com", 22),
]

cursor.executemany(
    "INSERT INTO clientes (id, nome, email, idade) VALUES (?, ?, ?, ?);",
    dados,
)
connection.commit()
```

Inserção única com placeholders:
```python
cursor.execute(
    "INSERT INTO clientes (id, nome, email, idade) VALUES (?, ?, ?, ?);",
    (4, "Marina Lima", "marina@example.com", 28),
)
connection.commit()
```

### 5) Consultando dados
```python
# todas as linhas
for row in cursor.execute("SELECT id, nome, email, idade FROM clientes;"):
    print(row)

# com filtro
for row in cursor.execute("SELECT nome, idade FROM clientes WHERE idade >= 25;"):
    print(row)

# ordenação
for row in cursor.execute("SELECT nome, idade FROM clientes ORDER BY idade DESC;"):
    print(row)
```

### 6) Atualizando e removendo
```python
# atualizar
cursor.execute("UPDATE clientes SET idade = ? WHERE id = ?;", (26, 1))
connection.commit()

# remover
cursor.execute("DELETE FROM clientes WHERE id = ?;", (3,))
connection.commit()
```

### 7) Boas práticas e recursos do `sqlite3`
- Use placeholders `?` para evitar SQL injection e problemas de formatação.
- Envolva operações críticas em transações (commit/rollback):
```python
try:
    cursor.execute("UPDATE clientes SET idade = idade + 1;")
    connection.commit()
except Exception as exc:
    connection.rollback()
    raise
```
- Ative restrições de chave estrangeira quando necessário:
```python
cursor.execute("PRAGMA foreign_keys = ON;")
```
- Leia resultados com `fetchone()`/`fetchall()` quando precisar manipular em memória:
```python
cursor.execute("SELECT id, nome FROM clientes;")
linhas = cursor.fetchall()
print(linhas)
```
- Para ver o schema rapidamente:
```python
for row in cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';"):
    print(row[0])
```

### 8) Encerrando a conexão
```python
cursor.close()
connection.close()
```

### 9) Extra — salvando e baixando o banco (arquivo)
Se usou arquivo (`meu_banco.db`), você pode baixá-lo no Colab:
```python
from google.colab import files
files.download("meu_banco.db")
```

### 10) Prática com CSV e JOIN (relacionamentos)
Importe os datasets de exemplo e pratique consultas com relacionamentos:

```python
import pandas as pd
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# importar clientes
df_clientes = pd.read_csv("https://raw.githubusercontent.com/BorisBass/aulas-backend-python/main/BEP-011/dados_clientes.csv")
df_clientes.to_sql("clientes", connection, index=False, if_exists="replace")

# importar pedidos
df_pedidos = pd.read_csv("https://raw.githubusercontent.com/BorisBass/aulas-backend-python/main/BEP-011/dados_pedidos.csv")
df_pedidos.to_sql("pedidos", connection, index=False, if_exists="replace")

print("Dados importados!")
```

Consultas com JOIN:
```python
# listar pedidos com nome do cliente
for row in cursor.execute("""
    SELECT c.nome, p.produto, p.valor, p.data
    FROM clientes c
    INNER JOIN pedidos p ON c.id = p.cliente_id
    ORDER BY p.data DESC;
"""):
    print(row)

# total por cliente
for row in cursor.execute("""
    SELECT c.nome, COUNT(p.id) as qtd_pedidos, SUM(p.valor) as total
    FROM clientes c
    LEFT JOIN pedidos p ON c.id = p.cliente_id
    GROUP BY c.id, c.nome
    ORDER BY total DESC;
"""):
    print(row)
```

---
Este roteiro cobre os principais comandos de conexão e operações básicas com SQLite no Colab, e expande opções úteis de `sqlite3.connect` e transações. Use-o como guia para seus testes.


