# BEP-014: Exercícios Práticos de Normalização

## Exercício 1: Sistema de Biblioteca

### Tabela Original (NÃO Normalizada)
```sql
CREATE TABLE emprestimos_original (
    emprestimo_id INT,
    usuario_nome VARCHAR(100),
    usuario_email VARCHAR(100),
    usuario_telefone VARCHAR(20),
    livro_titulo VARCHAR(200),
    livro_autor VARCHAR(100),
    livro_categoria VARCHAR(50),
    livro_editora VARCHAR(100),
    data_emprestimo DATE,
    data_devolucao DATE,
    data_devolucao_efetiva DATE,
    multa DECIMAL(10,2)
);
```

**Dados de Exemplo:**
| emprestimo_id | usuario_nome | usuario_email | usuario_telefone | livro_titulo | livro_autor | livro_categoria | livro_editora | data_emprestimo | data_devolucao | data_devolucao_efetiva | multa |
|---------------|--------------|---------------|------------------|--------------|-------------|-----------------|---------------|-----------------|----------------|------------------------|-------|
| 1 | João Silva | joao@email.com | (71) 99999-1111 | Python para Iniciantes | Maria Santos | Programação | Editora A | 2025-01-10 | 2025-01-24 | 2025-01-25 | 5.00 |
| 2 | Ana Costa | ana@email.com | (75) 88888-2222 | Python para Iniciantes | Maria Santos | Programação | Editora A | 2025-01-12 | 2025-01-26 | 2025-01-26 | 0.00 |
| 3 | João Silva | joao@email.com | (71) 99999-1111 | Banco de Dados | Pedro Lima | Programação | Editora B | 2025-01-15 | 2025-01-29 | 2025-01-29 | 0.00 |
| 4 | Maria Santos | maria@email.com | (73) 77777-3333 | Java Avançado | Carlos Oliveira | Programação | Editora A | 2025-01-20 | 2025-02-03 | NULL | 0.00 |

### Tarefas:
1. **Identifique** todos os problemas de normalização
2. **Aplique** as três formas normais
3. **Crie** as tabelas normalizadas
4. **Defina** as chaves primárias e estrangeiras
5. **Justifique** suas decisões

### Solução Esperada:
```sql
-- Tabela de Usuários
CREATE TABLE usuarios (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

-- Tabela de Categorias
CREATE TABLE categorias (
    categoria_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL
);

-- Tabela de Editoras
CREATE TABLE editoras (
    editora_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

-- Tabela de Livros
CREATE TABLE livros (
    livro_id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    categoria_id INT,
    editora_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id),
    FOREIGN KEY (editora_id) REFERENCES editoras(editora_id)
);

-- Tabela de Empréstimos
CREATE TABLE emprestimos (
    emprestimo_id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    livro_id INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE NOT NULL,
    data_devolucao_efetiva DATE,
    multa DECIMAL(10,2) DEFAULT 0.00,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id),
    FOREIGN KEY (livro_id) REFERENCES livros(livro_id)
);
```

---

## Exercício 2: Sistema de Vendas Online

### Tabela Original (NÃO Normalizada)
```sql
CREATE TABLE vendas_original (
    venda_id INT,
    cliente_nome VARCHAR(100),
    cliente_email VARCHAR(100),
    cliente_telefone VARCHAR(20),
    cliente_endereco VARCHAR(200),
    cliente_cidade VARCHAR(100),
    cliente_estado VARCHAR(2),
    cliente_cep VARCHAR(10),
    produto_nome VARCHAR(200),
    produto_descricao TEXT,
    produto_categoria VARCHAR(50),
    produto_fornecedor VARCHAR(100),
    produto_preco DECIMAL(10,2),
    quantidade INT,
    desconto DECIMAL(5,2),
    forma_pagamento VARCHAR(50),
    status_pagamento VARCHAR(50),
    data_venda DATE,
    data_entrega DATE
);
```

**Dados de Exemplo:**
| venda_id | cliente_nome | cliente_email | cliente_telefone | cliente_endereco | cliente_cidade | cliente_estado | cliente_cep | produto_nome | produto_descricao | produto_categoria | produto_fornecedor | produto_preco | quantidade | desconto | forma_pagamento | status_pagamento | data_venda | data_entrega |
|----------|--------------|---------------|------------------|------------------|----------------|----------------|-------------|--------------|-------------------|-------------------|-------------------|---------------|------------|----------|-----------------|------------------|------------|--------------|
| 1 | Maria Silva | maria@email.com | (71) 99999-1111 | Rua A, 123 | Salvador | BA | 40000-000 | Notebook Dell | Notebook para trabalho | Eletrônicos | Fornecedor X | 2500.00 | 1 | 5.00 | Cartão | Aprovado | 2025-01-15 | 2025-01-20 |
| 1 | Maria Silva | maria@email.com | (71) 99999-1111 | Rua A, 123 | Salvador | BA | 40000-000 | Mouse Logitech | Mouse sem fio | Eletrônicos | Fornecedor Y | 50.00 | 2 | 0.00 | Cartão | Aprovado | 2025-01-15 | 2025-01-20 |
| 2 | João Santos | joao@email.com | (75) 88888-2222 | Rua B, 456 | Feira de Santana | BA | 44000-000 | Notebook Dell | Notebook para trabalho | Eletrônicos | Fornecedor X | 2500.00 | 1 | 10.00 | PIX | Aprovado | 2025-01-16 | 2025-01-21 |

### Tarefas:
1. **Analise** a estrutura da tabela
2. **Identifique** todas as dependências
3. **Normalize** até a 3FN
4. **Crie** o script SQL
5. **Explique** os benefícios alcançados

---

## Exercício 3: Sistema Acadêmico

### Tabela Original (NÃO Normalizada)
```sql
CREATE TABLE matriculas_original (
    matricula_id INT,
    aluno_nome VARCHAR(100),
    aluno_cpf VARCHAR(14),
    aluno_email VARCHAR(100),
    aluno_telefone VARCHAR(20),
    aluno_endereco VARCHAR(200),
    aluno_cidade VARCHAR(100),
    aluno_estado VARCHAR(2),
    curso_nome VARCHAR(100),
    curso_duracao INT,
    curso_tipo VARCHAR(50),
    disciplina_nome VARCHAR(100),
    disciplina_carga_horaria INT,
    disciplina_creditos INT,
    professor_nome VARCHAR(100),
    professor_email VARCHAR(100),
    professor_especialidade VARCHAR(100),
    semestre VARCHAR(10),
    ano INT,
    nota_final DECIMAL(4,2),
    frequencia DECIMAL(5,2),
    status_matricula VARCHAR(50)
);
```

**Dados de Exemplo:**
| matricula_id | aluno_nome | aluno_cpf | aluno_email | aluno_telefone | aluno_endereco | aluno_cidade | aluno_estado | curso_nome | curso_duracao | curso_tipo | disciplina_nome | disciplina_carga_horaria | disciplina_creditos | professor_nome | professor_email | professor_especialidade | semestre | ano | nota_final | frequencia | status_matricula |
|--------------|------------|-----------|-------------|----------------|----------------|--------------|--------------|------------|---------------|------------|-----------------|--------------------------|-------------------|----------------|-----------------|------------------------|----------|-----|------------|------------|------------------|
| 1 | Ana Costa | 123.456.789-00 | ana@email.com | (71) 99999-1111 | Rua C, 789 | Salvador | BA | Ciência da Computação | 4 | Bacharelado | Programação I | 60 | 4 | Prof. Silva | silva@ifba.edu.br | Programação | 1 | 2025 | 8.5 | 85.0 | Aprovada |
| 1 | Ana Costa | 123.456.789-00 | ana@email.com | (71) 99999-1111 | Rua C, 789 | Salvador | BA | Ciência da Computação | 4 | Bacharelado | Banco de Dados | 80 | 5 | Prof. Santos | santos@ifba.edu.br | Banco de Dados | 1 | 2025 | 9.0 | 90.0 | Aprovada |
| 2 | Pedro Lima | 987.654.321-00 | pedro@email.com | (75) 88888-3333 | Rua D, 321 | Feira de Santana | BA | Engenharia de Software | 4 | Bacharelado | Programação I | 60 | 4 | Prof. Silva | silva@ifba.edu.br | Programação | 1 | 2025 | 7.5 | 80.0 | Aprovada |

### Tarefas:
1. **Identifique** todas as entidades
2. **Mapeie** as dependências funcionais
3. **Aplique** a normalização completa
4. **Crie** o diagrama ER
5. **Implemente** o banco de dados

---

## Exercício 4: Sistema de RH

### Tabela Original (NÃO Normalizada)
```sql
CREATE TABLE funcionarios_original (
    funcionario_id INT,
    nome VARCHAR(100),
    cpf VARCHAR(14),
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(200),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    cep VARCHAR(10),
    departamento_nome VARCHAR(100),
    departamento_sigla VARCHAR(10),
    departamento_orcamento DECIMAL(15,2),
    cargo_nome VARCHAR(100),
    cargo_salario_base DECIMAL(10,2),
    cargo_nivel VARCHAR(50),
    supervisor_nome VARCHAR(100),
    supervisor_cargo VARCHAR(100),
    data_admissao DATE,
    data_ultimo_reajuste DATE,
    salario_atual DECIMAL(10,2),
    beneficios VARCHAR(200),
    status_funcionario VARCHAR(50)
);
```

### Tarefas:
1. **Analise** a complexidade da tabela
2. **Identifique** múltiplas dependências transitivas
3. **Normalize** completamente
4. **Considere** cenários de consulta
5. **Avalie** trade-offs de performance

---

## Exercício 5: Sistema de E-commerce Completo

### Cenário:
Você precisa projetar um sistema completo de e-commerce que inclui:

1. **Clientes**: Dados pessoais e endereços múltiplos
2. **Produtos**: Com categorias, subcategorias e fornecedores
3. **Estoque**: Controle de quantidade por produto
4. **Pedidos**: Com múltiplos itens e status
5. **Pagamentos**: Múltiplas formas e parcelamentos
6. **Entregas**: Rastreamento e histórico
7. **Avaliações**: Clientes avaliam produtos
8. **Cupons**: Descontos e promoções

### Tarefas:
1. **Projete** o modelo completo
2. **Aplique** todas as formas normais
3. **Considere** relacionamentos complexos
4. **Otimize** para consultas comuns
5. **Documente** suas decisões

---

## Exercícios de Análise

### Exercício 6: Identificação de Problemas
Analise as seguintes tabelas e identifique os problemas de normalização:

#### Tabela A:
```sql
CREATE TABLE vendas_problema_a (
    venda_id INT,
    cliente_id INT,
    cliente_nome VARCHAR(100),
    cliente_email VARCHAR(100),
    produto_id INT,
    produto_nome VARCHAR(100),
    produto_categoria VARCHAR(50),
    produto_preco DECIMAL(10,2),
    quantidade INT,
    data_venda DATE
);
```

#### Tabela B:
```sql
CREATE TABLE funcionarios_problema_b (
    funcionario_id INT,
    nome VARCHAR(100),
    departamento VARCHAR(100),
    gerente VARCHAR(100),
    salario DECIMAL(10,2),
    data_admissao DATE,
    telefones VARCHAR(200), -- "1111-1111, 2222-2222"
    habilidades VARCHAR(300) -- "Python, Java, SQL"
);
```

#### Tabela C:
```sql
CREATE TABLE pedidos_problema_c (
    pedido_id INT,
    cliente_id INT,
    cliente_nome VARCHAR(100),
    cliente_cidade VARCHAR(100),
    cliente_estado VARCHAR(2),
    produto_id INT,
    produto_nome VARCHAR(100),
    produto_categoria VARCHAR(50),
    categoria_descricao VARCHAR(200),
    quantidade INT,
    preco_unitario DECIMAL(10,2),
    data_pedido DATE
);
```

### Exercício 7: Decisões de Design
Para cada cenário, decida se deve normalizar ou desnormalizar e justifique:

1. **Tabela de Logs**: Registra todas as ações dos usuários
2. **Relatório de Vendas**: Gerado mensalmente para análise
3. **Cache de Sessão**: Dados temporários de usuários logados
4. **Tabela de Configurações**: Parâmetros do sistema
5. **Histórico de Preços**: Evolução dos preços dos produtos

---

## Soluções e Comentários

### Dicas para Resolução:

1. **Sempre comece identificando a chave primária**
2. **Mapeie todas as dependências funcionais**
3. **Aplique as formas normais sequencialmente**
4. **Considere o contexto de uso**
5. **Avalie trade-offs de performance**
6. **Documente suas decisões**

### Checklist de Verificação:
- [ ] Tabela está na 1FN?
- [ ] Tabela está na 2FN?
- [ ] Tabela está na 3FN?
- [ ] Chaves primárias definidas?
- [ ] Chaves estrangeiras estabelecidas?
- [ ] Integridade referencial garantida?
- [ ] Performance considerada?
- [ ] Manutenibilidade assegurada?

### Comandos SQL Úteis:
```sql
-- Verificar estrutura de tabela
DESCRIBE nome_da_tabela;

-- Verificar chaves estrangeiras
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE REFERENCED_TABLE_SCHEMA = 'nome_do_banco';

-- Verificar índices
SHOW INDEX FROM nome_da_tabela;
```

---

## Exercício Final: Projeto Completo

### Desafio Final
Projete um sistema de **gerenciamento de biblioteca universitária** que deve incluir:

#### Entidades Principais:
1. **Usuários** (estudantes, professores, funcionários)
2. **Livros** (com informações completas)
3. **Empréstimos** (com histórico)
4. **Reservas** (sistema de fila)
5. **Multas** (controle de atrasos)
6. **Categorias** (classificação dos livros)
7. **Editoras** (informações das editoras)
8. **Autores** (informações dos autores)

#### Requisitos Funcionais:
- Usuários podem ter múltiplos empréstimos
- Livros podem ter múltiplos autores
- Sistema de reservas com fila
- Controle de multas por atraso
- Histórico completo de empréstimos
- Relatórios de uso da biblioteca

#### Requisitos Não-Funcionais:
- Performance otimizada para consultas
- Integridade referencial garantida
- Facilidade de manutenção
- Escalabilidade para crescimento

### Entregáveis:
1. **Diagrama ER** completo
2. **Script SQL** para criação das tabelas
3. **Justificativa** das decisões de normalização
4. **Análise de performance** e otimizações
5. **Documentação** do modelo de dados

### Critérios de Avaliação:
- ✅ Aplicação correta das formas normais
- ✅ Identificação adequada de chaves
- ✅ Relacionamentos bem definidos
- ✅ Justificativas claras e coerentes
- ✅ Consideração de cenários reais
- ✅ Otimizações de performance
- ✅ Documentação completa

---

## Recursos Adicionais

### Ferramentas Recomendadas:
- **MySQL Workbench**: Para modelagem visual
- **phpMyAdmin**: Para administração do banco
- **DBeaver**: Cliente universal de banco de dados
- **Lucidchart**: Para diagramas ER online

### Livros e Referências:
- "Database System Concepts" - Silberschatz
- "Fundamentals of Database Systems" - Elmasri & Navathe
- "SQL for Mere Mortals" - Viescas & Hernandez

### Próximos Passos:
Após dominar a normalização, você estará pronto para:
- **BEP-015**: Joins e Consultas Avançadas
- **BEP-016**: Conectando Python com Banco de Dados
- **BEP-017**: Índices e Otimização de Performance
- **BEP-018**: Transações e Controle de Concorrência


