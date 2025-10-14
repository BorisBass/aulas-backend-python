# Comandos de Banco de Dados - Lista Completa

Este documento contém uma lista abrangente de comandos usados em bancos de dados, especialmente SQLite3 com Python.

## 📚 Comandos de Conexão e Configuração

### `sqlite3.connect()`
**Explicação:** Estabelece uma conexão com o banco de dados SQLite.
```python
# Banco em memória (temporário)
conn = sqlite3.connect(':memory:')

# Banco em arquivo
conn = sqlite3.connect('meu_banco.db')

# Banco com configurações
conn = sqlite3.connect('banco.db', timeout=30.0)
```

### `conn.cursor()`
**Explicação:** Cria um cursor para executar comandos SQL e recuperar resultados.
```python
cursor = conn.cursor()
```

### `conn.close()`
**Explicação:** Fecha a conexão com o banco de dados.
```python
conn.close()
```

## 🔧 Comandos de Execução SQL

### `cursor.execute()`
**Explicação:** Executa um comando SQL.
```python
# Comando simples
cursor.execute("SELECT * FROM clientes")

# Comando com parâmetros (proteção contra SQL injection)
cursor.execute("SELECT * FROM clientes WHERE id = ?", (1,))
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ('João', 'joao@email.com'))
```

### `cursor.executemany()`
**Explicação:** Executa o mesmo comando SQL para múltiplos registros.
```python
dados = [
    ('João', 'joao@email.com'),
    ('Maria', 'maria@email.com'),
    ('Pedro', 'pedro@email.com')
]
cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
```

### `cursor.executescript()`
**Explicação:** Executa múltiplos comandos SQL separados por ponto e vírgula.
```python
script = """
CREATE TABLE clientes (id INTEGER PRIMARY KEY, nome TEXT);
INSERT INTO clientes (nome) VALUES ('João');
INSERT INTO clientes (nome) VALUES ('Maria');
"""
cursor.executescript(script)
```

## 💾 Comandos de Persistência

### `conn.commit()`
**Explicação:** Salva as alterações no banco de dados.
```python
cursor.execute("INSERT INTO clientes (nome) VALUES ('João')")
conn.commit()  # Salva a alteração
```

### `conn.rollback()`
**Explicação:** Desfaz alterações não commitadas.
```python
try:
    cursor.execute("INSERT INTO clientes (nome) VALUES ('João')")
    conn.commit()
except:
    conn.rollback()  # Desfaz se houver erro
```

## 📊 Comandos de Recuperação de Dados

### `cursor.fetchall()`
**Explicação:** Retorna todos os resultados de uma consulta SELECT.
```python
cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()
# Retorna: [(1, 'João', 'joao@email.com'), (2, 'Maria', 'maria@email.com')]
```

### `cursor.fetchone()`
**Explicação:** Retorna apenas o primeiro resultado de uma consulta.
```python
cursor.execute("SELECT * FROM clientes WHERE id = 1")
cliente = cursor.fetchone()
# Retorna: (1, 'João', 'joao@email.com') ou None se não encontrar
```

### `cursor.fetchmany(size)`
**Explicação:** Retorna um número específico de resultados.
```python
cursor.execute("SELECT * FROM clientes")
primeiros_5 = cursor.fetchmany(5)
# Retorna lista com no máximo 5 registros
```

## 🔍 Comandos PRAGMA (Informações do Sistema)

### `PRAGMA table_info(tabela)`
**Explicação:** Mostra informações sobre as colunas de uma tabela.
```python
cursor.execute("PRAGMA table_info(clientes)")
colunas = cursor.fetchall()
# Retorna: [(0, 'id', 'INTEGER', 0, None, 1), (1, 'nome', 'TEXT', 1, None, 0)]
```

### `PRAGMA foreign_keys = ON`
**Explicação:** Ativa a verificação de chaves estrangeiras.
```python
cursor.execute("PRAGMA foreign_keys = ON")
```

### `PRAGMA foreign_keys = OFF`
**Explicação:** Desativa a verificação de chaves estrangeiras.
```python
cursor.execute("PRAGMA foreign_keys = OFF")
```

### `PRAGMA database_list`
**Explicação:** Lista todos os bancos de dados anexados.
```python
cursor.execute("PRAGMA database_list")
bancos = cursor.fetchall()
```

### `PRAGMA table_list`
**Explicação:** Lista todas as tabelas no banco de dados.
```python
cursor.execute("PRAGMA table_list")
tabelas = cursor.fetchall()
```

### `PRAGMA index_list(tabela)`
**Explicação:** Lista todos os índices de uma tabela.
```python
cursor.execute("PRAGMA index_list(clientes)")
indices = cursor.fetchall()
```

### `PRAGMA index_info(indice)`
**Explicação:** Mostra informações sobre um índice específico.
```python
cursor.execute("PRAGMA index_info(idx_nome)")
info_indice = cursor.fetchall()
```

## 🏗️ Comandos DDL (Data Definition Language)

### `CREATE TABLE`
**Explicação:** Cria uma nova tabela.
```python
cursor.execute('''
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    data_cadastro DATE DEFAULT CURRENT_DATE
)
''')
```

### `CREATE INDEX`
**Explicação:** Cria um índice para melhorar performance.
```python
cursor.execute("CREATE INDEX idx_nome ON clientes(nome)")
cursor.execute("CREATE UNIQUE INDEX idx_email ON clientes(email)")
```

### `CREATE VIEW`
**Explicação:** Cria uma view (consulta salva).
```python
cursor.execute('''
CREATE VIEW clientes_ativos AS
SELECT nome, email FROM clientes 
WHERE data_cadastro >= '2024-01-01'
''')
```

### `ALTER TABLE`
**Explicação:** Modifica a estrutura de uma tabela existente.
```python
# Adicionar coluna
cursor.execute("ALTER TABLE clientes ADD COLUMN telefone TEXT")

# Renomear tabela
cursor.execute("ALTER TABLE clientes RENAME TO usuarios")
```

### `DROP TABLE`
**Explicação:** Remove uma tabela completamente.
```python
cursor.execute("DROP TABLE clientes")
```

### `DROP INDEX`
**Explicação:** Remove um índice.
```python
cursor.execute("DROP INDEX idx_nome")
```

### `DROP VIEW`
**Explicação:** Remove uma view.
```python
cursor.execute("DROP VIEW clientes_ativos")
```

## 📝 Comandos DML (Data Manipulation Language)

### `INSERT INTO`
**Explicação:** Insere novos registros em uma tabela.
```python
# Inserção simples
cursor.execute("INSERT INTO clientes (nome, email) VALUES ('João', 'joao@email.com')")

# Inserção com múltiplos valores
cursor.execute('''
INSERT INTO clientes (nome, email) VALUES 
('João', 'joao@email.com'),
('Maria', 'maria@email.com')
''')
```

### `SELECT`
**Explicação:** Consulta dados de uma ou mais tabelas.
```python
# Selecionar tudo
cursor.execute("SELECT * FROM clientes")

# Selecionar colunas específicas
cursor.execute("SELECT nome, email FROM clientes")

# Selecionar com condições
cursor.execute("SELECT * FROM clientes WHERE cidade = 'Salvador'")
```

### `UPDATE`
**Explicação:** Atualiza registros existentes.
```python
cursor.execute("UPDATE clientes SET email = 'novo@email.com' WHERE id = 1")
cursor.execute("UPDATE clientes SET cidade = 'Salvador' WHERE cidade = 'SSA'")
```

### `DELETE`
**Explicação:** Remove registros de uma tabela.
```python
cursor.execute("DELETE FROM clientes WHERE id = 1")
cursor.execute("DELETE FROM clientes WHERE cidade = 'Salvador'")
```

## 🔍 Comandos de Filtro e Ordenação

### `WHERE`
**Explicação:** Filtra registros por condições.
```python
# Igualdade
cursor.execute("SELECT * FROM clientes WHERE cidade = 'Salvador'")

# Maior que
cursor.execute("SELECT * FROM produtos WHERE preco > 100")

# LIKE (busca por padrão)
cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'João%'")

# IN (valores em lista)
cursor.execute("SELECT * FROM clientes WHERE cidade IN ('Salvador', 'Feira')")

# BETWEEN (entre valores)
cursor.execute("SELECT * FROM produtos WHERE preco BETWEEN 50 AND 200")
```

### `ORDER BY`
**Explicação:** Ordena os resultados.
```python
# Ordem crescente
cursor.execute("SELECT * FROM clientes ORDER BY nome")

# Ordem decrescente
cursor.execute("SELECT * FROM produtos ORDER BY preco DESC")

# Múltiplas colunas
cursor.execute("SELECT * FROM clientes ORDER BY cidade, nome")
```

### `LIMIT`
**Explicação:** Limita o número de registros retornados.
```python
# Primeiros 10 registros
cursor.execute("SELECT * FROM clientes LIMIT 10")

# Com OFFSET (pular registros)
cursor.execute("SELECT * FROM clientes LIMIT 10 OFFSET 20")
```

### `GROUP BY`
**Explicação:** Agrupa registros por valores de coluna.
```python
cursor.execute("SELECT cidade, COUNT(*) FROM clientes GROUP BY cidade")
```

### `HAVING`
**Explicação:** Filtra grupos (usado com GROUP BY).
```python
cursor.execute('''
SELECT cidade, COUNT(*) as total 
FROM clientes 
GROUP BY cidade 
HAVING total > 5
''')
```

## 📊 Funções de Agregação

### `COUNT()`
**Explicação:** Conta o número de registros.
```python
cursor.execute("SELECT COUNT(*) FROM clientes")
cursor.execute("SELECT COUNT(DISTINCT cidade) FROM clientes")
```

### `SUM()`
**Explicação:** Soma valores de uma coluna.
```python
cursor.execute("SELECT SUM(preco) FROM produtos")
```

### `AVG()`
**Explicação:** Calcula a média de valores.
```python
cursor.execute("SELECT AVG(preco) FROM produtos")
```

### `MIN()` e `MAX()`
**Explicação:** Encontra o menor e maior valor.
```python
cursor.execute("SELECT MIN(preco), MAX(preco) FROM produtos")
```

## 🔗 Comandos de JOIN

### `INNER JOIN`
**Explicação:** Retorna registros que têm correspondência em ambas as tabelas.
```python
cursor.execute('''
SELECT c.nome, p.nome as produto
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
''')
```

### `LEFT JOIN`
**Explicação:** Retorna todos os registros da tabela esquerda e correspondências da direita.
```python
cursor.execute('''
SELECT c.nome, p.nome as produto
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
''')
```

### `RIGHT JOIN`
**Explicação:** Retorna todos os registros da tabela direita e correspondências da esquerda.
```python
cursor.execute('''
SELECT c.nome, p.nome as produto
FROM clientes c
RIGHT JOIN pedidos p ON c.id = p.cliente_id
''')
```

## 🛡️ Comandos de Transação

### `BEGIN`
**Explicação:** Inicia uma transação.
```python
cursor.execute("BEGIN")
```

### `COMMIT`
**Explicação:** Confirma uma transação.
```python
cursor.execute("COMMIT")
```

### `ROLLBACK`
**Explicação:** Desfaz uma transação.
```python
cursor.execute("ROLLBACK")
```

### `SAVEPOINT`
**Explicação:** Cria um ponto de salvamento em uma transação.
```python
cursor.execute("SAVEPOINT ponto1")
cursor.execute("ROLLBACK TO ponto1")
```

## 🔧 Comandos de Configuração

### `PRAGMA journal_mode`
**Explicação:** Define o modo de journal do banco.
```python
cursor.execute("PRAGMA journal_mode = WAL")  # Write-Ahead Logging
cursor.execute("PRAGMA journal_mode = DELETE")  # Modo padrão
```

### `PRAGMA synchronous`
**Explicação:** Define o nível de sincronização.
```python
cursor.execute("PRAGMA synchronous = NORMAL")
cursor.execute("PRAGMA synchronous = FULL")
```

### `PRAGMA cache_size`
**Explicação:** Define o tamanho do cache em páginas.
```python
cursor.execute("PRAGMA cache_size = 1000")
```

## 📋 Comandos de Informação

### `PRAGMA user_version`
**Explicação:** Define ou consulta a versão do usuário do banco.
```python
cursor.execute("PRAGMA user_version = 1")
cursor.execute("PRAGMA user_version")
```

### `PRAGMA schema_version`
**Explicação:** Consulta a versão do esquema do banco.
```python
cursor.execute("PRAGMA schema_version")
```

### `PRAGMA database_size`
**Explicação:** Mostra informações sobre o tamanho do banco.
```python
cursor.execute("PRAGMA database_size")
```

## 🎯 Exemplo Completo de Uso

```python
import sqlite3

def exemplo_completo():
    # Conectar ao banco
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    try:
        # Configurar
        cursor.execute("PRAGMA foreign_keys = ON")
        
        # Criar tabela
        cursor.execute('''
            CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE,
                cidade TEXT
            )
        ''')
        
        # Inserir dados
        cursor.executemany('''
            INSERT INTO clientes (nome, email, cidade)
            VALUES (?, ?, ?)
        ''', [
            ('João Silva', 'joao@email.com', 'Salvador'),
            ('Maria Santos', 'maria@email.com', 'Feira de Santana'),
            ('Pedro Costa', 'pedro@email.com', 'Salvador')
        ])
        
        # Consultar dados
        cursor.execute("SELECT * FROM clientes WHERE cidade = 'Salvador'")
        clientes = cursor.fetchall()
        
        # Mostrar resultados
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}")
        
        # Confirmar alterações
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Erro: {e}")
        conn.rollback()
    finally:
        conn.close()

# Executar exemplo
exemplo_completo()
```

## 📚 Dicas Importantes

1. **Sempre use parâmetros** (`?`) em vez de concatenação de strings para evitar SQL injection
2. **Sempre faça commit** após INSERT, UPDATE, DELETE
3. **Sempre feche a conexão** com `close()`
4. **Use try/except** para tratar erros
5. **Ative foreign keys** com `PRAGMA foreign_keys = ON`
6. **Use transações** para operações complexas
7. **Crie índices** para melhorar performance em consultas frequentes
