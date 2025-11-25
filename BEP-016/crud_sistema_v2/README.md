# Sistema CRUD de Gerenciamento de Alunos - Versão 2 (Orientada a Objetos)

Esta é a versão 2 do sistema CRUD, desenvolvida usando **Programação Orientada a Objetos (POO)**.

## 📚 Conceitos Aplicados

Este sistema demonstra os conceitos aprendidos nas BEP-017 a BEP-022:

### BEP-017: Fundamentos de POO
- **Classes**: `Aluno`, `DatabaseManager`, `AlunoRepository`, `Menu`, `SistemaAlunos`
- **Objetos**: Instâncias das classes representando entidades do sistema
- **Atributos e Métodos**: Cada classe possui seus próprios atributos e comportamentos

### BEP-018: Criando e Instanciando Classes
- **Construtores (`__init__`)**: Todas as classes têm construtores apropriados
- **Instanciação**: Objetos são criados e utilizados em todo o sistema

### BEP-019: Encapsulamento
- **Atributos privados**: Uso de `_` para indicar atributos privados
- **Getters e Setters**: Propriedades (`@property`) para acesso controlado
- **Validação**: Validações nos setters garantem integridade dos dados

### BEP-020: Herança e Polimorfismo
- **Herança de Exceções**: Exceções customizadas herdam de `ErroSistema`
- **Polimorfismo**: Métodos com mesmo nome em classes diferentes

### BEP-021: Composição e Associação
- **Composição**: `SistemaAlunos` tem `AlunoRepository` e `Menu`
- **Associação**: `AlunoRepository` usa `DatabaseManager`

### BEP-022: Tratamento de Exceções
- **Exceções customizadas**: `ErroSistema`, `AlunoNaoEncontradoError`, `DadosInvalidosError`, `ErroBancoDados`
- **Try-except em classes**: Tratamento de exceções em todos os métodos
- **Hierarquia de exceções**: Exceções específicas herdam de exceção base

## 🏗️ Estrutura do Sistema

```
crud_sistema_v2/
├── __init__.py          # Inicialização do pacote
├── models.py            # Classe Aluno (entidade)
├── database.py          # Classe DatabaseManager (gerenciamento de BD)
├── repository.py        # Classe AlunoRepository (operações CRUD)
├── menu.py              # Classe Menu (interface)
├── sistema.py           # Classe SistemaAlunos (orquestrador)
├── exceptions.py        # Exceções customizadas
└── README.md            # Este arquivo
```

## 🔑 Principais Classes

### `Aluno` (models.py)
- Representa a entidade Aluno
- Encapsulamento com atributos privados
- Validação automática de dados
- Métodos: `atualizar()`, `to_dict()`, `to_tuple()`, `from_tuple()`

### `DatabaseManager` (database.py)
- Gerencia conexões com banco de dados
- Context manager (`with`)
- Métodos: `conectar()`, `fechar()`, `get_cursor()`

### `AlunoRepository` (repository.py)
- Padrão Repository para operações CRUD
- Composição com `DatabaseManager`
- Métodos: `criar()`, `buscar_por_id()`, `listar_todos()`, `atualizar()`, `remover()`

### `Menu` (menu.py)
- Interface do usuário
- Métodos estáticos para exibição
- Formatação de dados

### `SistemaAlunos` (sistema.py)
- Orquestra todo o sistema
- Composição: tem `AlunoRepository` e `Menu`
- Tratamento de exceções centralizado

## 🚀 Como Usar

### Execução Direta

**Opção 1: Executar o módulo sistema.py diretamente**
```bash
cd BEP-016
python -m crud_sistema_v2.sistema
```

**Opção 2: Executar o script run_crud_v2.py**
```bash
cd BEP-016
python -m crud_sistema_v2.run_crud_v2
```

**Opção 3: Executar o arquivo diretamente**
```bash
python BEP-016/crud_sistema_v2/sistema.py
```

### Como Módulo (de dentro de BEP-016)

```python
from crud_sistema_v2 import SistemaAlunos

sistema = SistemaAlunos()
sistema.iniciar()
```

### Uso das Classes Individualmente

```python
# Importar de dentro da pasta BEP-016
from crud_sistema_v2 import Aluno, DatabaseManager, AlunoRepository

# Criar aluno
aluno = Aluno(nome="João Silva", idade=20, curso="Python", nota=9.5)

# Gerenciar banco
db = DatabaseManager('meu_banco.db')
db.conectar()

# Operações CRUD
repo = AlunoRepository(db)
aluno_criado = repo.criar(aluno)
```

## 🔄 Diferenças da Versão 1 (Procedural)

| Aspecto | Versão 1 (Procedural) | Versão 2 (OO) |
|---------|----------------------|---------------|
| **Estrutura** | Funções em módulos | Classes e objetos |
| **Dados** | Tuplas e dicionários | Objetos `Aluno` |
| **Validação** | Manual em cada função | Automática na classe |
| **Encapsulamento** | Não há | Atributos privados |
| **Exceções** | Genéricas | Customizadas e hierárquicas |
| **Composição** | Não aplicada | Repository e Manager |
| **Reutilização** | Funções | Classes reutilizáveis |

## 📝 Exemplo de Uso

**Importante:** Execute os exemplos de dentro da pasta `BEP-016` ou ajuste o `sys.path`.

```python
# De dentro de BEP-016/
from crud_sistema_v2 import SistemaAlunos, Aluno, DatabaseManager, AlunoRepository

# Criar e iniciar sistema
sistema = SistemaAlunos('alunos_v2.db')
sistema.iniciar()

# Ou usar classes individualmente
db = DatabaseManager('alunos_v2.db')
db.conectar()

repo = AlunoRepository(db)

# Criar aluno
aluno = Aluno(nome="Maria", idade=22, curso="Python", nota=8.5)
aluno_criado = repo.criar(aluno)

# Buscar aluno
aluno_encontrado = repo.buscar_por_id(1)

# Listar todos
todos = repo.listar_todos()

# Atualizar
aluno_encontrado.nota = 9.0
repo.atualizar(aluno_encontrado)

# Remover
repo.remover(1)

db.fechar()
```

## 🎯 Benefícios da Versão OO

1. **Encapsulamento**: Dados protegidos e validados automaticamente
2. **Reutilização**: Classes podem ser usadas em outros contextos
3. **Manutenibilidade**: Código organizado e fácil de modificar
4. **Extensibilidade**: Fácil adicionar novas funcionalidades
5. **Testabilidade**: Classes podem ser testadas isoladamente
6. **Clareza**: Código mais expressivo e fácil de entender

## 📚 Próximos Passos

Compare esta versão com a versão 1 (`BEP-016/crud_sistema/`) para entender as diferenças entre programação procedural e orientada a objetos!

Veja também os slides comparativos em `BEP-CRUD/` para uma análise detalhada das diferenças entre as duas versões.

