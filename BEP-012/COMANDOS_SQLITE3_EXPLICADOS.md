# Comandos SQLite3 Explicados

Este documento explica os principais comandos usados no SQLite3 com Python, especialmente os que aparecem na prática do slide11.

## 📚 Comandos de Conexão

### `sqlite3.connect()`
**O que faz:** Estabelece uma conexão com o banco de dados SQLite.

**Sintaxe:**
```python
conn = sqlite3.connect(':memory:')  # Banco em memória
conn = sqlite3.connect('arquivo.db')  # Banco em arquivo
```

**Explicação:**
- `:memory:` cria um banco temporário na memória (desaparece quando o programa termina)
- `'arquivo.db'` cria ou conecta a um arquivo de banco de dados
- Retorna um objeto de conexão que usamos para executar comandos

### `conn.cursor()`
**O que faz:** Cria um cursor para executar comandos SQL.

**Sintaxe:**
```python
cursor = conn.cursor()
```

**Explicação:**
- O cursor é como um "ponteiro" que aponta para os resultados das consultas
- Usamos o cursor para executar comandos SQL e recuperar resultados

## 🔧 Comandos de Execução

### `cursor.execute()`
**O que faz:** Executa um comando SQL.

**Sintaxe:**
```python
cursor.execute("SELECT * FROM clientes")
cursor.execute("INSERT INTO clientes (nome) VALUES (?)", ('João',))
```

**Explicação:**
- Executa comandos SQL como SELECT, INSERT, UPDATE, DELETE
- O segundo parâmetro (tupla) substitui os `?` na consulta (proteção contra SQL injection)

### `cursor.executemany()`
**O que faz:** Executa o mesmo comando SQL para múltiplos registros.

**Sintaxe:**
```python
dados = [('João', 'joao@email.com'), ('Maria', 'maria@email.com')]
cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
```

**Explicação:**
- Mais eficiente que executar INSERT várias vezes
- Cada tupla na lista representa um registro a ser inserido

## 💾 Comandos de Persistência

### `conn.commit()`
**O que faz:** Salva as alterações no banco de dados.

**Sintaxe:**
```python
cursor.execute("INSERT INTO clientes (nome) VALUES ('João')")
conn.commit()  # Salva a alteração
```

**Explicação:**
- **IMPORTANTE:** Sem commit, as alterações são perdidas quando a conexão fecha
- Usar após INSERT, UPDATE, DELETE
- Não é necessário após SELECT (apenas leitura)

### `conn.close()`
**O que faz:** Fecha a conexão com o banco de dados.

**Sintaxe:**
```python
conn.close()
```

**Explicação:**
- Libera recursos do sistema
- Salva automaticamente as alterações pendentes
- Boa prática sempre fechar a conexão

## 📊 Comandos de Recuperação de Dados

### `cursor.fetchall()`
**O que faz:** Retorna todos os resultados de uma consulta SELECT.

**Sintaxe:**
```python
cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()
```

**Explicação:**
- Retorna uma lista de tuplas
- Cada tupla representa uma linha da tabela
- Cada elemento da tupla é uma coluna
- Exemplo: `[(1, 'João', 'joao@email.com'), (2, 'Maria', 'maria@email.com')]`

### `cursor.fetchone()`
**O que faz:** Retorna apenas o primeiro resultado de uma consulta.

**Sintaxe:**
```python
cursor.execute("SELECT * FROM clientes WHERE id = 1")
cliente = cursor.fetchone()
```

**Explicação:**
- Retorna uma tupla com o primeiro registro
- Útil quando sabemos que a consulta retorna apenas um resultado
- Retorna `None` se não houver resultados

### `cursor.fetchmany(size)`
**O que faz:** Retorna um número específico de resultados.

**Sintaxe:**
```python
cursor.execute("SELECT * FROM clientes")
primeiros_5 = cursor.fetchmany(5)
```

**Explicação:**
- Retorna uma lista com no máximo `size` registros
- Útil para paginação ou processamento em lotes

## 🔍 Comandos de Informação (PRAGMA)

### `PRAGMA table_info(tabela)`
**O que faz:** Mostra informações sobre as colunas de uma tabela.

**Sintaxe:**
```python
cursor.execute("PRAGMA table_info(clientes)")
colunas = cursor.fetchall()
```

**Explicação:**
- Retorna informações sobre cada coluna da tabela
- Cada linha contém: [id, nome, tipo, not_null, default_value, pk]
- Útil para descobrir a estrutura de uma tabela

**Exemplo de resultado:**
```python
[(0, 'id', 'INTEGER', 0, None, 1),  # id, INTEGER, PRIMARY KEY
 (1, 'nome', 'TEXT', 1, None, 0),   # nome, TEXT, NOT NULL
 (2, 'email', 'TEXT', 0, None, 0)]  # email, TEXT, pode ser NULL
```

### `PRAGMA foreign_keys = ON`
**O que faz:** Ativa a verificação de chaves estrangeiras.

**Sintaxe:**
```python
cursor.execute("PRAGMA foreign_keys = ON")
```

**Explicação:**
- Por padrão, SQLite não verifica chaves estrangeiras
- Com esta opção, o banco verifica se as referências são válidas
- Boa prática sempre ativar

## 🛡️ Tratamento de Erros

### Try/Except com SQLite3
**O que faz:** Captura e trata erros que podem ocorrer com o banco.

**Sintaxe:**
```python
try:
    cursor.execute("INSERT INTO clientes (nome) VALUES ('João')")
    conn.commit()
    print("Cliente inserido com sucesso!")
except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")
    conn.rollback()  # Desfaz alterações em caso de erro
```

**Explicação:**
- `sqlite3.Error` captura erros específicos do SQLite
- `conn.rollback()` desfaz alterações não commitadas
- Importante para manter a integridade dos dados

## 📝 Exemplo Completo

```python
import sqlite3

try:
    # Conectar ao banco
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Criar tabela
    cursor.execute('''
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT
        )
    ''')
    
    # Inserir dados
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", 
                   ('João Silva', 'joao@email.com'))
    conn.commit()
    
    # Consultar dados
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    
    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}")
        
except sqlite3.Error as e:
    print(f"Erro: {e}")
finally:
    # Sempre fechar a conexão
    if conn:
        conn.close()
```

## 🎯 Dicas Importantes

1. **Sempre use `?` em vez de concatenação de strings** para evitar SQL injection
2. **Sempre faça `commit()`** após INSERT, UPDATE, DELETE
3. **Sempre feche a conexão** com `close()`
4. **Use try/except** para tratar erros
5. **Ative foreign keys** com `PRAGMA foreign_keys = ON`
6. **Use `fetchall()`** para múltiplos resultados, `fetchone()` para um único resultado
