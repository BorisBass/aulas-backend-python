# Sistema CRUD de Gerenciamento de Alunos - Versão 2 (Orientada a Objetos - Simplificada)

Esta é a versão 2 do sistema CRUD, desenvolvida usando **Programação Orientada a Objetos (POO) básica**.

## 📚 Conceitos Aplicados

Este sistema demonstra os conceitos básicos aprendidos nas BEP-017 a BEP-022:

### BEP-017: Fundamentos de POO
- **Classes**: `Aluno`, `DatabaseManager`, `AlunoRepository`, `Menu`, `SistemaAlunos`
- **Objetos**: Instâncias das classes representando entidades do sistema
- **Atributos e Métodos**: Cada classe possui seus próprios atributos e comportamentos

### BEP-018: Criando e Instanciando Classes
- **Construtores (`__init__`)**: Todas as classes têm construtores apropriados
- **Instanciação**: Objetos são criados e utilizados em todo o sistema

### BEP-019: Encapsulamento
- **Validação**: Validações nos construtores e métodos garantem integridade dos dados
- **Métodos de atualização**: Método `atualizar()` para modificar dados

### BEP-021: Composição e Associação
- **Composição**: `SistemaAlunos` tem `AlunoRepository` e `Menu`
- **Associação**: `AlunoRepository` usa `DatabaseManager`

### BEP-022: Tratamento de Exceções
- **Try-except básico**: Tratamento de exceções em todos os métodos
- **Exceções simples**: Uso de `ValueError` e `Exception` padrão do Python

## 🏗️ Estrutura do Sistema

```
crud_sistema_v2/
├── __init__.py          # Inicialização do pacote
├── models.py            # Classe Aluno (entidade)
├── database.py          # Classe DatabaseManager (gerenciamento de BD)
├── repository.py        # Classe AlunoRepository (operações CRUD)
├── menu.py              # Classe Menu (interface)
├── sistema.py           # Classe SistemaAlunos (orquestrador)
├── exceptions.py        # Exceções customizadas (simplificadas)
└── README.md            # Este arquivo
```

## 🔑 Principais Classes

### `Aluno` (models.py)
- Representa a entidade Aluno
- Validação automática de dados no construtor
- Métodos: `atualizar()`, `__str__()`

### `DatabaseManager` (database.py)
- Gerencia conexões com banco de dados
- Métodos: `conectar()`, `fechar()`, `get_cursor()`

### `AlunoRepository` (repository.py)
- Operações CRUD no banco de dados
- Composição com `DatabaseManager`
- Métodos: `criar()`, `buscar_por_id()`, `listar_todos()`, `atualizar()`, `remover()`

### `Menu` (menu.py)
- Interface do usuário
- Métodos estáticos (`@staticmethod`) para exibição
- Formatação de dados

### `SistemaAlunos` (sistema.py)
- Orquestra todo o sistema
- Composição: tem `AlunoRepository` e `Menu`
- Tratamento de exceções centralizado

## 🚀 Como Usar

### Execução Direta

**⚠️ IMPORTANTE:** Este sistema deve ser executado como módulo Python devido aos imports relativos.

```bash
# Na raiz do projeto (aulas/)
python3 -m BEP-016.crud_sistema_v2.sistema
```

**Nota:** Se você estiver usando `python` ao invés de `python3`, use:
```bash
python -m BEP-016.crud_sistema_v2.sistema
```

**Por que não funciona executar diretamente?**
- Os arquivos usam imports relativos (`from .database import ...`)
- Imports relativos só funcionam quando executados como módulo (`-m`)
- Isso é uma prática comum em Python para manter a estrutura de pacotes

### Como Módulo

**Nota:** Como o nome da pasta `BEP-016` contém hífen, não é possível importar diretamente. Use uma das opções abaixo:

**Opção 1: Ajustar sys.path**
```python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Agora pode importar usando importlib
import importlib.util
spec = importlib.util.spec_from_file_location(
    "crud_sistema_v2", 
    "BEP-016/crud_sistema_v2/sistema.py"
)
sistema_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sistema_module)

sistema = sistema_module.SistemaAlunos()
sistema.iniciar()
```

**Opção 2: Executar como módulo (recomendado)**
```bash
python -m BEP-016.crud_sistema_v2.sistema
```

### Uso das Classes Individualmente

**Nota:** Devido ao hífen no nome da pasta, é mais simples executar o sistema diretamente ou usar os arquivos individualmente dentro da pasta.

# Criar aluno
aluno = Aluno(nome="João Silva", idade=20, curso="Python", nota=9.5)

# Gerenciar banco
db = DatabaseManager('alunos_v2.db')
db.conectar()

# Operações CRUD
repo = AlunoRepository(db)
aluno_criado = repo.criar(aluno)

# Fechar conexão
db.fechar()
```

## 🔄 Diferenças da Versão 1 (Procedural)

| Aspecto | Versão 1 (Procedural) | Versão 2 (OO Simplificada) |
|---------|----------------------|----------------------------|
| **Estrutura** | Funções em módulos | Classes e objetos |
| **Dados** | Tuplas e dicionários | Objetos `Aluno` |
| **Validação** | Manual em cada função | Automática na classe |
| **Organização** | Funções separadas | Classes com métodos |
| **Exceções** | Genéricas | Try-except básico |
| **Composição** | Não aplicada | Repository e Manager |
| **Reutilização** | Funções | Classes reutilizáveis |

## 📝 Exemplo de Uso Completo

**Nota:** Devido ao hífen no nome da pasta `BEP-016`, a forma mais simples é executar o sistema diretamente:

```bash
# Executar o sistema completo
python -m BEP-016.crud_sistema_v2.sistema
```

Ou, se quiser usar as classes em um script próprio, você pode trabalhar dentro da pasta `BEP-016/crud_sistema_v2/`:

```python
# Dentro da pasta BEP-016/crud_sistema_v2/
from models import Aluno
from database import DatabaseManager
from repository import AlunoRepository

# Criar aluno
aluno = Aluno(nome="Maria", idade=22, curso="Python", nota=8.5)

# Gerenciar banco
db = DatabaseManager('alunos_v2.db')
db.conectar()

# Operações CRUD
repo = AlunoRepository(db)
aluno_criado = repo.criar(aluno)

# Buscar aluno
aluno_encontrado = repo.buscar_por_id(1)

# Listar todos
todos = repo.listar_todos()

# Atualizar
aluno_encontrado.atualizar(nota=9.0)
repo.atualizar(aluno_encontrado)

# Remover
repo.remover(1)

db.fechar()
```

## 🎯 Benefícios da Versão OO

1. **Organização**: Código agrupado em classes lógicas
2. **Reutilização**: Classes podem ser usadas em outros contextos
3. **Manutenibilidade**: Código organizado e fácil de modificar
4. **Validação**: Dados validados automaticamente na classe
5. **Clareza**: Código mais expressivo e fácil de entender

## ⚠️ Versão Simplificada

Esta é uma **versão simplificada** que usa apenas conceitos básicos de OOP:
- ✅ Classes e objetos básicos
- ✅ Construtores e métodos simples
- ✅ Validação básica
- ✅ Composição simples
- ✅ Try-except básico
- ❌ Sem type hints complexos (`Optional[int]`, etc.)
- ❌ Sem decoradores avançados (`@contextmanager`, `@classmethod` complexo)
- ❌ Sem exceções customizadas complexas
- ❌ Sem conceitos avançados não vistos nas aulas

## 📚 Próximos Passos

Compare esta versão com a versão 1 (`BEP-016/crud_sistema/`) para entender as diferenças entre programação procedural e orientada a objetos!

Veja também os slides comparativos em `BEP-CRUD/` para uma análise detalhada das diferenças entre as duas versões.
