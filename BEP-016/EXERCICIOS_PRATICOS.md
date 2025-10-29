# BEP-016: Conectando a Banco de Dados - Exercícios Práticos

## Exercício 1: Sistema de Produtos

### Objetivo
Criar um sistema completo para gerenciar produtos de uma loja.

### Requisitos
- Tabela `produtos` com campos: id, nome, preco, categoria, estoque, data_cadastro
- Funcionalidades: cadastrar, listar, buscar, atualizar, remover produtos
- Menu interativo
- Tratamento de erros
- Validação de dados

### Estrutura da Tabela
```sql
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT,
    estoque INTEGER DEFAULT 0,
    data_cadastro DATE DEFAULT CURRENT_DATE
);
```

### Funcionalidades a Implementar
1. **Cadastrar Produto**
   - Nome obrigatório
   - Preço obrigatório e positivo
   - Categoria opcional
   - Estoque inicial

2. **Listar Produtos**
   - Mostrar todos os produtos
   - Formatação bonita
   - Ordenação por nome

3. **Buscar Produto**
   - Buscar por nome
   - Buscar por categoria
   - Mostrar resultados formatados

4. **Atualizar Produto**
   - Selecionar por ID
   - Atualizar campos específicos
   - Validação de dados

5. **Remover Produto**
   - Selecionar por ID
   - Confirmação antes de remover
   - Verificar se existe

6. **Estatísticas**
   - Total de produtos
   - Produtos por categoria
   - Valor total do estoque
   - Produtos com estoque baixo

## Exercício 2: Sistema de Contatos

### Objetivo
Criar uma agenda de contatos com funcionalidades avançadas.

### Requisitos
- Tabela `contatos` com campos: id, nome, telefone, email, cidade, data_nascimento, data_cadastro
- Funcionalidades: CRUD completo + funcionalidades especiais
- Validação de email e telefone
- Busca avançada

### Estrutura da Tabela
```sql
CREATE TABLE contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT UNIQUE,
    email TEXT UNIQUE,
    cidade TEXT,
    data_nascimento DATE,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Funcionalidades Especiais
1. **Aniversariantes do Dia**
   - Mostrar contatos que fazem aniversário hoje
   - Usar funções de data do SQLite

2. **Contatos por Cidade**
   - Agrupar contatos por cidade
   - Mostrar quantidade por cidade

3. **Recém Cadastrados**
   - Contatos cadastrados na última semana
   - Contatos cadastrados no último mês

4. **Validação Avançada**
   - Validar formato de email
   - Validar formato de telefone
   - Verificar duplicatas

## Exercício 3: Sistema de Notas Escolares

### Objetivo
Criar um sistema para gerenciar notas de alunos com múltiplas disciplinas.

### Requisitos
- Três tabelas relacionadas: alunos, disciplinas, notas
- Relacionamentos com chaves estrangeiras
- Consultas com JOIN
- Relatórios avançados

### Estrutura das Tabelas
```sql
-- Tabela de alunos
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT UNIQUE,
    curso TEXT
);

-- Tabela de disciplinas
CREATE TABLE disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    codigo TEXT UNIQUE
);

-- Tabela de notas
CREATE TABLE notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    disciplina_id INTEGER,
    nota REAL,
    data_avaliacao DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (aluno_id) REFERENCES alunos (id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas (id)
);
```

### Funcionalidades a Implementar
1. **CRUD Básico**
   - Cadastrar alunos, disciplinas e notas
   - Listar, buscar, atualizar e remover

2. **Relatórios**
   - Boletim individual do aluno
   - Média por disciplina
   - Ranking de alunos
   - Alunos em recuperação (média < 6.0)

3. **Consultas Avançadas**
   - Melhores alunos por disciplina
   - Disciplinas com maior dificuldade
   - Evolução das notas ao longo do tempo

## Exercício 4: Sistema de Biblioteca

### Objetivo
Criar um sistema de empréstimo de livros com controle de usuários.

### Requisitos
- Duas tabelas relacionadas: livros e emprestimos
- Controle de disponibilidade
- Histórico de empréstimos
- Relatórios de uso

### Estrutura das Tabelas
```sql
-- Tabela de livros
CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    isbn TEXT UNIQUE,
    ano_publicacao INTEGER,
    disponivel BOOLEAN DEFAULT 1
);

-- Tabela de empréstimos
CREATE TABLE emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro_id INTEGER,
    usuario TEXT NOT NULL,
    data_emprestimo DATE DEFAULT CURRENT_DATE,
    data_devolucao DATE,
    FOREIGN KEY (livro_id) REFERENCES livros (id)
);
```

### Funcionalidades a Implementar
1. **Gestão de Livros**
   - Cadastrar livros
   - Listar livros disponíveis
   - Buscar por título ou autor

2. **Gestão de Empréstimos**
   - Emprestar livro
   - Devolver livro
   - Listar empréstimos ativos
   - Histórico de empréstimos

3. **Relatórios**
   - Livros mais emprestados
   - Usuários mais ativos
   - Livros em atraso
   - Estatísticas de uso

## Exercício 5: Sistema de Vendas

### Objetivo
Criar um sistema de vendas com clientes, produtos e pedidos.

### Requisitos
- Três tabelas relacionadas: clientes, produtos, pedidos
- Cálculos de totais
- Relatórios de vendas
- Controle de estoque

### Estrutura das Tabelas
```sql
-- Tabela de clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    telefone TEXT,
    endereco TEXT
);

-- Tabela de produtos
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER DEFAULT 0
);

-- Tabela de pedidos
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    total REAL NOT NULL,
    data_pedido DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (cliente_id) REFERENCES clientes (id),
    FOREIGN KEY (produto_id) REFERENCES produtos (id)
);
```

### Funcionalidades a Implementar
1. **Gestão de Clientes**
   - CRUD completo de clientes
   - Validação de email

2. **Gestão de Produtos**
   - CRUD completo de produtos
   - Controle de estoque

3. **Gestão de Pedidos**
   - Criar pedido
   - Calcular total automaticamente
   - Atualizar estoque
   - Listar pedidos por cliente

4. **Relatórios**
   - Vendas por período
   - Clientes mais ativos
   - Produtos mais vendidos
   - Receita total

## Dicas para os Exercícios

### Boas Práticas
1. **Sempre use try/except** para capturar erros
2. **Valide dados de entrada** antes de inserir no banco
3. **Use prepared statements** (?) para evitar SQL injection
4. **Sempre feche conexões** com o banco
5. **Use commit()** para salvar alterações
6. **Implemente confirmações** para operações críticas

### Estrutura do Código
1. **Função de conexão** separada
2. **Funções específicas** para cada operação
3. **Menu interativo** bem organizado
4. **Tratamento de erros** em todas as funções
5. **Validação de dados** antes das operações

### Testes
1. **Teste cada função** individualmente
2. **Teste cenários de erro** (dados inválidos, duplicatas)
3. **Verifique integridade** dos dados
4. **Teste performance** com muitos registros

## Desafios Extras

### Nível Intermediário
1. **Backup e Restore** do banco de dados
2. **Logs de auditoria** para todas as operações
3. **Validação avançada** (CPF, CNPJ, etc.)
4. **Relatórios em arquivo** (CSV, TXT)

### Nível Avançado
1. **Interface gráfica** com tkinter
2. **Relatórios em PDF** com bibliotecas específicas
3. **Sistema de usuários** com login e senha
4. **API REST** com Flask ou FastAPI

### Projetos Integrados
1. **Sistema completo** de e-commerce
2. **Sistema de gestão** escolar
3. **Sistema de clínica** médica
4. **Sistema de biblioteca** pública

## Recursos de Aprendizado

### Documentação
- [SQLite3 Python Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python Database Programming](https://realpython.com/python-sql/)

### Ferramentas
- **DB Browser for SQLite**: Interface gráfica para SQLite
- **SQLite Studio**: Editor de banco de dados
- **VS Code**: Editor com extensões para SQLite

### Prática
- **LeetCode**: Problemas de SQL
- **HackerRank**: Exercícios de banco de dados
- **Kaggle**: Datasets para prática

---

**Boa sorte com os exercícios! Lembre-se: a prática é essencial para dominar o desenvolvimento com bancos de dados.**
