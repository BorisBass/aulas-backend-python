# Comandos sqlite3.connect - Guia Completo

## 1. Conexão Básica

### `sqlite3.connect(database)`
**Explicação:** Conecta a um banco de dados SQLite. Se o arquivo não existir, será criado automaticamente.

**Exemplo:**
```python
import sqlite3

# Conecta ao banco 'exemplo.db'
conn = sqlite3.connect('exemplo.db')
print("Conectado com sucesso!")
conn.close()
```

## 2. Conexão com Timeout

### `sqlite3.connect(database, timeout=5.0)`
**Explicação:** Define um tempo limite para operações de bloqueio. Útil quando múltiplos processos acessam o mesmo banco.

**Exemplo:**
```python
import sqlite3

# Conecta com timeout de 10 segundos
conn = sqlite3.connect('exemplo.db', timeout=10.0)
print("Conectado com timeout de 10 segundos")
conn.close()
```

## 3. Conexão com Detecção de Tipos

### `sqlite3.connect(database, detect_types=0)`
**Explicação:** Controla a detecção automática de tipos de dados. Por padrão é 0 (desabilitado).

**Exemplo:**
```python
import sqlite3

# Conecta sem detecção de tipos
conn = sqlite3.connect('exemplo.db', detect_types=0)
print("Conectado sem detecção de tipos")
conn.close()
```

## 4. Conexão com Detecção de Tipos Avançada

### `sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)`
**Explicação:** Habilita a detecção automática de tipos Python baseada na declaração da coluna e no nome da coluna.

**Exemplo:**
```python
import sqlite3

# Conecta com detecção completa de tipos
conn = sqlite3.connect('exemplo.db', 
                      detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
print("Conectado com detecção completa de tipos")
conn.close()
```

## 5. Conexão com Isolamento

### `sqlite3.connect(database, isolation_level=None)`
**Explicação:** Define o nível de isolamento das transações. `None` significa autocommit (cada comando é commitado automaticamente).

**Exemplo:**
```python
import sqlite3

# Conecta com autocommit
conn = sqlite3.connect('exemplo.db', isolation_level=None)
print("Conectado com autocommit")
conn.close()
```

## 6. Conexão com Isolamento DEFERRED

### `sqlite3.connect(database, isolation_level='DEFERRED')`
**Explicação:** Transações são iniciadas quando o primeiro comando SQL é executado.

**Exemplo:**
```python
import sqlite3

# Conecta com isolamento DEFERRED
conn = sqlite3.connect('exemplo.db', isolation_level='DEFERRED')
print("Conectado com isolamento DEFERRED")
conn.close()
```

## 7. Conexão com Isolamento IMMEDIATE

### `sqlite3.connect(database, isolation_level='IMMEDIATE')`
**Explicação:** Transações são iniciadas imediatamente quando executadas.

**Exemplo:**
```python
import sqlite3

# Conecta com isolamento IMMEDIATE
conn = sqlite3.connect('exemplo.db', isolation_level='IMMEDIATE')
print("Conectado com isolamento IMMEDIATE")
conn.close()
```

## 8. Conexão com Isolamento EXCLUSIVE

### `sqlite3.connect(database, isolation_level='EXCLUSIVE')`
**Explicação:** Transações são iniciadas em modo exclusivo, bloqueando outras conexões.

**Exemplo:**
```python
import sqlite3

# Conecta com isolamento EXCLUSIVE
conn = sqlite3.connect('exemplo.db', isolation_level='EXCLUSIVE')
print("Conectado com isolamento EXCLUSIVE")
conn.close()
```

## 9. Conexão com Verificação de Integridade

### `sqlite3.connect(database, check_same_thread=True)`
**Explicação:** Verifica se a conexão está sendo usada no mesmo thread que foi criada. Por padrão é `True`.

**Exemplo:**
```python
import sqlite3

# Conecta com verificação de thread
conn = sqlite3.connect('exemplo.db', check_same_thread=True)
print("Conectado com verificação de thread")
conn.close()
```

## 10. Conexão sem Verificação de Thread

### `sqlite3.connect(database, check_same_thread=False)`
**Explicação:** Permite usar a conexão em threads diferentes. Útil para aplicações multithreaded.

**Exemplo:**
```python
import sqlite3

# Conecta sem verificação de thread
conn = sqlite3.connect('exemplo.db', check_same_thread=False)
print("Conectado sem verificação de thread")
conn.close()
```

## 11. Conexão com URI

### `sqlite3.connect(database, uri=False)`
**Explicação:** Define se o parâmetro database deve ser interpretado como URI. Por padrão é `False`.

**Exemplo:**
```python
import sqlite3

# Conecta sem interpretação de URI
conn = sqlite3.connect('exemplo.db', uri=False)
print("Conectado sem URI")
conn.close()
```

## 12. Conexão com URI Habilitada

### `sqlite3.connect(database, uri=True)`
**Explicação:** Permite usar URIs para especificar opções de conexão.

**Exemplo:**
```python
import sqlite3

# Conecta com URI habilitada
conn = sqlite3.connect('file:exemplo.db?mode=rw', uri=True)
print("Conectado com URI")
conn.close()
```

## 13. Conexão com Cursor Factory

### `sqlite3.connect(database, factory=sqlite3.Connection)`
**Explicação:** Define uma classe personalizada para criar conexões.

**Exemplo:**
```python
import sqlite3

# Conecta com factory padrão
conn = sqlite3.connect('exemplo.db', factory=sqlite3.Connection)
print("Conectado com factory padrão")
conn.close()
```

## 14. Conexão com Cursor Factory Personalizada

### `sqlite3.connect(database, factory=MinhaConexao)`
**Explicação:** Usa uma classe personalizada que herda de `sqlite3.Connection`.

**Exemplo:**
```python
import sqlite3

class MinhaConexao(sqlite3.Connection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Conexão personalizada criada!")

# Conecta com factory personalizada
conn = sqlite3.connect('exemplo.db', factory=MinhaConexao)
print("Conectado com factory personalizada")
conn.close()
```

## 15. Conexão com Cached Statements

### `sqlite3.connect(database, cached_statements=100)`
**Explicação:** Define o número de statements SQL que serão cacheados. Por padrão é 100.

**Exemplo:**
```python
import sqlite3

# Conecta com cache de 200 statements
conn = sqlite3.connect('exemplo.db', cached_statements=200)
print("Conectado com cache de 200 statements")
conn.close()
```

## 16. Conexão Completa com Múltiplas Opções

### `sqlite3.connect(database, timeout=5.0, detect_types=0, isolation_level=None, check_same_thread=True, factory=sqlite3.Connection, cached_statements=100, uri=False)`
**Explicação:** Combina todas as opções disponíveis em uma única conexão.

**Exemplo:**
```python
import sqlite3

# Conecta com todas as opções
conn = sqlite3.connect(
    'exemplo.db',
    timeout=5.0,
    detect_types=0,
    isolation_level=None,
    check_same_thread=True,
    factory=sqlite3.Connection,
    cached_statements=100,
    uri=False
)
print("Conectado com todas as opções")
conn.close()
```

## 17. Conexão em Memória

### `sqlite3.connect(':memory:')`
**Explicação:** Cria um banco de dados temporário em memória. Útil para testes e dados temporários.

**Exemplo:**
```python
import sqlite3

# Conecta a um banco em memória
conn = sqlite3.connect(':memory:')
print("Conectado a banco em memória")

# Cria uma tabela temporária
conn.execute('CREATE TABLE temp (id INTEGER, nome TEXT)')
conn.execute('INSERT INTO temp VALUES (1, "Teste")')

# Consulta os dados
resultado = conn.execute('SELECT * FROM temp').fetchall()
print("Dados:", resultado)

conn.close()
```

## 18. Conexão com Modo de Abertura

### `sqlite3.connect('file:exemplo.db?mode=rw')`
**Explicação:** Especifica o modo de abertura do arquivo (read-write, read-only, etc.).

**Exemplo:**
```python
import sqlite3

# Conecta em modo read-write
conn = sqlite3.connect('file:exemplo.db?mode=rw', uri=True)
print("Conectado em modo read-write")
conn.close()

# Conecta em modo read-only
conn = sqlite3.connect('file:exemplo.db?mode=ro', uri=True)
print("Conectado em modo read-only")
conn.close()
```

## 19. Conexão com Cache Compartilhado

### `sqlite3.connect('file:exemplo.db?cache=shared')`
**Explicação:** Habilita o cache compartilhado entre múltiplas conexões.

**Exemplo:**
```python
import sqlite3

# Conecta com cache compartilhado
conn = sqlite3.connect('file:exemplo.db?cache=shared', uri=True)
print("Conectado com cache compartilhado")
conn.close()
```

## 20. Conexão com WAL Mode

### `sqlite3.connect('file:exemplo.db?mode=rw&journal_mode=WAL')`
**Explicação:** Habilita o Write-Ahead Logging (WAL) para melhor performance em aplicações concorrentes.

**Exemplo:**
```python
import sqlite3

# Conecta com WAL mode
conn = sqlite3.connect('file:exemplo.db?mode=rw&journal_mode=WAL', uri=True)
print("Conectado com WAL mode")
conn.close()
```

## Resumo dos Parâmetros

| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|--------|-----------|
| `database` | str | - | Caminho para o arquivo do banco |
| `timeout` | float | 5.0 | Timeout para operações de bloqueio |
| `detect_types` | int | 0 | Detecção automática de tipos |
| `isolation_level` | str/None | None | Nível de isolamento das transações |
| `check_same_thread` | bool | True | Verificação de thread |
| `factory` | class | Connection | Classe para criar conexões |
| `cached_statements` | int | 100 | Número de statements cacheados |
| `uri` | bool | False | Interpretar database como URI |

## Dicas Importantes

1. **Sempre feche as conexões** com `conn.close()`
2. **Use context managers** para garantir o fechamento automático
3. **Para aplicações multithreaded**, use `check_same_thread=False`
4. **Para melhor performance**, ajuste `cached_statements`
5. **Para dados temporários**, use `:memory:`
6. **Para aplicações concorrentes**, considere WAL mode
