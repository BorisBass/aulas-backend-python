# BEP-014: Modelagem e Normalização de Dados

## Objetivo
Ensinar os alunos a estruturar dados de forma eficiente para evitar redundância e inconsistência.

## Conteúdo da Aula

### Slide 01: Introdução à Modelagem de Dados

#### O que é Modelagem de Dados?
A **modelagem de dados** é o processo de criar uma representação abstrata e estruturada dos dados que serão armazenados em um banco de dados, definindo como as informações se relacionam entre si.

#### Por que Modelar Dados?
- **Evitar Redundância**: Eliminar duplicação desnecessária de informações
- **Garantir Integridade**: Manter consistência e confiabilidade dos dados
- **Melhorar Performance**: Otimizar consultas e operações no banco
- **Facilitar Manutenção**: Simplificar alterações e expansões futuras

#### Problema: Tabela Não Normalizada
Exemplo de tabela de pedidos mal estruturada:

| Pedido_ID | Cliente_Nome | Cliente_Email | Produto_Nome | Produto_Categoria | Quantidade | Preço |
|-----------|--------------|---------------|--------------|-------------------|------------|-------|
| 1 | João Silva | joao@email.com | Notebook Dell | Eletrônicos | 1 | R$ 2.500 |
| 1 | João Silva | joao@email.com | Mouse Logitech | Eletrônicos | 2 | R$ 50 |
| 2 | Maria Santos | maria@email.com | Notebook Dell | Eletrônicos | 1 | R$ 2.500 |

**Problemas Identificados:**
- **Redundância**: Dados do cliente e produto repetidos
- **Inconsistência**: Risco de dados divergentes
- **Performance**: Consultas mais lentas
- **Manutenção**: Alterações em múltiplos locais

#### Objetivos da Normalização
A **normalização** é o processo de organizar os dados em tabelas para eliminar redundâncias e inconsistências:

- **1ª Forma Normal (1FN)** - Eliminar grupos repetitivos
- **2ª Forma Normal (2FN)** - Eliminar dependências parciais
- **3ª Forma Normal (3FN)** - Eliminar dependências transitivas

---

### Slide 02: 1ª Forma Normal (1FN)

#### Definição da 1ª Forma Normal
Uma tabela está na **1ª Forma Normal (1FN)** quando:
- ✅ **Todos os valores** em cada coluna são **atômicos** (indivisíveis)
- ✅ **Não há grupos repetitivos** ou arrays em uma única coluna
- ✅ **Cada célula** contém apenas **um valor**
- ✅ **Não há** colunas com múltiplos valores separados por vírgulas

#### Exemplo: Tabela NÃO Normalizada
| ID | Nome | Telefones | Cursos |
|----|------|-----------|--------|
| 1 | João Silva | (71) 99999-1111, (71) 3333-2222 | Python, Java, SQL |
| 2 | Maria Santos | (75) 88888-3333 | JavaScript, React |

**Problemas:**
- Coluna "Telefones": Múltiplos valores separados por vírgula
- Coluna "Cursos": Múltiplos valores separados por vírgula
- Não atômico: Cada célula contém mais de um valor

#### Exemplo: Tabela na 1ª Forma Normal
| ID | Nome | Telefone | Curso |
|----|------|----------|-------|
| 1 | João Silva | (71) 99999-1111 | Python |
| 1 | João Silva | (71) 3333-2222 | Java |
| 1 | João Silva | (71) 99999-1111 | SQL |
| 2 | Maria Santos | (75) 88888-3333 | JavaScript |
| 2 | Maria Santos | (75) 88888-3333 | React |

**Características da 1FN:**
- **Valores atômicos**: Cada célula contém apenas um valor
- **Sem grupos repetitivos**: Não há múltiplos valores em uma coluna
- **Estrutura simples**: Fácil de consultar e manipular

#### Como Aplicar a 1ª Forma Normal
1. **Identificar**: Encontrar colunas com múltiplos valores
2. **Separar**: Dividir valores em linhas individuais
3. **Verificar**: Confirmar que cada célula tem um valor
4. **Aplicar**: Implementar a nova estrutura

---

### Slide 03: 2ª Forma Normal (2FN)

#### Definição da 2ª Forma Normal
Uma tabela está na **2ª Forma Normal (2FN)** quando:
- ✅ **Já está na 1FN** (pré-requisito obrigatório)
- ✅ **Elimina dependências parciais** da chave primária
- ✅ **Todos os atributos não-chave** dependem **completamente** da chave primária
- ✅ **Não há** atributos que dependem apenas de parte da chave primária

#### Conceitos Importantes
- **Chave Primária**: Campo(s) que identificam unicamente cada registro
- **Dependência Funcional**: Quando um atributo determina outro atributo
- **Dependência Parcial**: Atributo depende apenas de parte da chave primária
- **Dependência Completa**: Atributo depende de toda a chave primária

#### Exemplo: Tabela NÃO na 2FN
| Pedido_ID | Produto_ID | Cliente_Nome | Produto_Nome | Categoria | Quantidade | Preço |
|-----------|------------|--------------|--------------|-----------|------------|-------|
| 1 | 101 | João Silva | Notebook Dell | Eletrônicos | 1 | R$ 2.500 |
| 1 | 102 | João Silva | Mouse Logitech | Eletrônicos | 2 | R$ 50 |
| 2 | 101 | Maria Santos | Notebook Dell | Eletrônicos | 1 | R$ 2.500 |

**Problemas:**
- **Chave Primária**: (Pedido_ID, Produto_ID)
- **Dependência Parcial**: Cliente_Nome depende apenas de Pedido_ID
- **Dependência Parcial**: Produto_Nome e Categoria dependem apenas de Produto_ID
- **Redundância**: Dados do cliente e produto repetidos

#### Solução: Tabelas na 2FN

**Tabela: PEDIDOS**
| Pedido_ID | Cliente_Nome | Data_Pedido |
|-----------|--------------|-------------|
| 1 | João Silva | 2025-01-15 |
| 2 | Maria Santos | 2025-01-16 |

**Tabela: PRODUTOS**
| Produto_ID | Produto_Nome | Categoria | Preço |
|------------|--------------|-----------|-------|
| 101 | Notebook Dell | Eletrônicos | R$ 2.500 |
| 102 | Mouse Logitech | Eletrônicos | R$ 50 |

**Tabela: ITENS_PEDIDO**
| Pedido_ID | Produto_ID | Quantidade |
|-----------|------------|------------|
| 1 | 101 | 1 |
| 1 | 102 | 2 |
| 2 | 101 | 1 |

#### Benefícios da 2FN
- **Menos Redundância**: Dados do cliente e produto não se repetem
- **Facilita Atualizações**: Mudanças em um local só
- **Integridade**: Menor risco de inconsistências
- **Performance**: Consultas mais eficientes

---

### Slide 04: 3ª Forma Normal (3FN)

#### Definição da 3ª Forma Normal
Uma tabela está na **3ª Forma Normal (3FN)** quando:
- ✅ **Já está na 2FN** (pré-requisito obrigatório)
- ✅ **Elimina dependências transitivas**
- ✅ **Não há** atributos não-chave que dependem de outros atributos não-chave
- ✅ **Todos os atributos não-chave** dependem **diretamente** da chave primária

#### O que é Dependência Transitiva?
Uma **dependência transitiva** ocorre quando:
- A → B e B → C, então A → C (transitivamente)
- Onde A é a chave primária, B e C são atributos não-chave

**Problema**: O atributo C depende de B, que depende de A, mas C deveria depender diretamente de A.

#### Exemplo: Tabela NÃO na 3FN
| Pedido_ID | Cliente_ID | Cliente_Nome | Cliente_Email | Cidade_ID | Cidade_Nome | Estado | Data_Pedido |
|-----------|------------|--------------|---------------|-----------|-------------|--------|-------------|
| 1 | 101 | João Silva | joao@email.com | 1 | Salvador | BA | 2025-01-15 |
| 2 | 102 | Maria Santos | maria@email.com | 2 | Feira de Santana | BA | 2025-01-16 |
| 3 | 103 | Pedro Costa | pedro@email.com | 1 | Salvador | BA | 2025-01-17 |

**Dependências Transitivas:**
- Pedido_ID → Cliente_ID → Cliente_Nome, Cliente_Email
- Pedido_ID → Cidade_ID → Cidade_Nome, Estado

#### Solução: Tabelas na 3FN

**Tabela: PEDIDOS**
| Pedido_ID | Cliente_ID | Data_Pedido |
|-----------|------------|-------------|
| 1 | 101 | 2025-01-15 |
| 2 | 102 | 2025-01-16 |
| 3 | 103 | 2025-01-17 |

**Tabela: CLIENTES**
| Cliente_ID | Cliente_Nome | Cliente_Email | Cidade_ID |
|------------|--------------|---------------|-----------|
| 101 | João Silva | joao@email.com | 1 |
| 102 | Maria Santos | maria@email.com | 2 |
| 103 | Pedro Costa | pedro@email.com | 1 |

**Tabela: CIDADES**
| Cidade_ID | Cidade_Nome | Estado |
|-----------|-------------|--------|
| 1 | Salvador | BA |
| 2 | Feira de Santana | BA |

#### Benefícios da 3FN
- **Zero Redundância**: Eliminação completa de dados duplicados
- **Atualizações Simples**: Mudanças em um local só
- **Máxima Integridade**: Consistência total dos dados
- **Performance Otimizada**: Consultas mais rápidas e eficientes

---

### Slide 05: Impacto da Modelagem na Performance e Integridade

#### Por que a Modelagem é Importante?
A qualidade da modelagem de dados tem impacto direto em:
- **Performance**: Velocidade das consultas e operações
- **Integridade**: Consistência e confiabilidade dos dados
- **Manutenibilidade**: Facilidade de manutenção e evolução
- **Custos**: Economia de recursos e armazenamento

#### Impacto na Performance

**Modelagem Ruim:**
- Consultas lentas: Muitos dados para processar
- Índices ineficientes: Dados duplicados
- Joins complexos: Múltiplas tabelas desnecessárias
- Bloqueios frequentes: Conflitos de acesso
- Uso excessivo de memória: Dados redundantes

**Modelagem Boa:**
- Consultas rápidas: Dados organizados
- Índices eficientes: Estrutura otimizada
- Joins simples: Relacionamentos claros
- Menos bloqueios: Acesso otimizado
- Uso eficiente de memória: Sem redundância

#### Impacto na Integridade dos Dados

**Problemas de Integridade:**
- Dados inconsistentes: Informações divergentes
- Anomalias de inserção: Dados obrigatórios ausentes
- Anomalias de atualização: Esquecer atualizações
- Anomalias de exclusão: Perda de dados importantes
- Violação de regras: Dados inválidos

**Integridade Garantida:**
- Dados consistentes: Informações únicas
- Inserções seguras: Validação automática
- Atualizações controladas: Mudanças em um local
- Exclusões seguras: Sem perda de dados
- Regras respeitadas: Validação automática

#### Exemplo Prático: Sistema de E-commerce

**Abordagem Ruim (Não Normalizada):**
```sql
-- Tabela única com todos os dados
CREATE TABLE vendas_ruim (
    venda_id INT,
    cliente_nome VARCHAR(100),
    cliente_email VARCHAR(100),
    produto_nome VARCHAR(100),
    produto_categoria VARCHAR(50),
    produto_preco DECIMAL(10,2),
    quantidade INT,
    data_venda DATE
);
```

**Abordagem Boa (Normalizada):**
```sql
-- Tabelas separadas e relacionadas
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE produtos (
    produto_id INT PRIMARY KEY,
    nome VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(10,2)
);

CREATE TABLE vendas (
    venda_id INT PRIMARY KEY,
    cliente_id INT,
    data_venda DATE,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

CREATE TABLE itens_venda (
    venda_id INT,
    produto_id INT,
    quantidade INT,
    PRIMARY KEY (venda_id, produto_id),
    FOREIGN KEY (venda_id) REFERENCES vendas(venda_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);
```

#### Métricas de Performance
- **Tempo de Consulta**: Modelagem boa: 50-80% mais rápida
- **Uso de Armazenamento**: Modelagem boa: 30-60% menos espaço
- **Uso de Memória**: Modelagem boa: 40-70% menos RAM
- **Processamento**: Modelagem boa: 60-90% menos CPU

#### Quando NÃO Normalizar?
Em alguns casos específicos, a normalização pode não ser a melhor opção:
- **Data Warehouses**: Dados históricos para análise
- **Relatórios complexos**: Quando performance é crítica
- **Sistemas legados**: Migração gradual necessária
- **Dados temporários**: Cache ou logs

**Regra**: Normalize para operações (CRUD), desnormalize para relatórios (READ).

---

### Slide 06: Exercícios Práticos de Normalização

#### Exercício 1: Sistema de Biblioteca
Analise a tabela abaixo e identifique os problemas de normalização:

| Emprestimo_ID | Usuario_Nome | Usuario_Email | Livro_Titulo | Livro_Autor | Livro_Categoria | Data_Emprestimo | Data_Devolucao |
|---------------|--------------|---------------|--------------|-------------|-----------------|-----------------|----------------|
| 1 | João Silva | joao@email.com | Python para Iniciantes | Maria Santos | Programação | 2025-01-10 | 2025-01-24 |
| 2 | Ana Costa | ana@email.com | Python para Iniciantes | Maria Santos | Programação | 2025-01-12 | 2025-01-26 |
| 3 | João Silva | joao@email.com | Banco de Dados | Pedro Lima | Programação | 2025-01-15 | 2025-01-29 |

**Questões para Análise:**
1. Esta tabela está na 1ª Forma Normal? Por quê?
2. Quais dependências parciais você identifica?
3. Quais dependências transitivas existem?
4. Como você normalizaria esta tabela?

#### Exercício 2: Sistema de Vendas
Analise a tabela de vendas e aplique a normalização:

| Venda_ID | Cliente_ID | Cliente_Nome | Cliente_Telefone | Produto_ID | Produto_Nome | Categoria_ID | Categoria_Nome | Quantidade | Preco_Unitario |
|----------|------------|--------------|------------------|------------|--------------|--------------|----------------|------------|----------------|
| 1 | 101 | Maria Silva | (71) 99999-1111 | 201 | Notebook Dell | 301 | Eletrônicos | 1 | R$ 2.500 |
| 1 | 101 | Maria Silva | (71) 99999-1111 | 202 | Mouse Logitech | 301 | Eletrônicos | 2 | R$ 50 |
| 2 | 102 | João Santos | (75) 88888-2222 | 201 | Notebook Dell | 301 | Eletrônicos | 1 | R$ 2.500 |

**Questões para Análise:**
1. Identifique a chave primária desta tabela
2. Quais dependências parciais existem?
3. Quais dependências transitivas você encontra?
4. Projete as tabelas normalizadas na 3FN

#### Exercício 3: Sistema Acadêmico
Normalize a tabela de matrículas:

| Matricula_ID | Aluno_Nome | Aluno_CPF | Curso_Nome | Curso_Duracao | Disciplina_Nome | Disciplina_Carga | Professor_Nome | Nota |
|--------------|------------|-----------|------------|---------------|-----------------|------------------|----------------|------|
| 1 | Ana Costa | 123.456.789-00 | Ciência da Computação | 4 anos | Programação I | 60h | Prof. Silva | 8.5 |
| 1 | Ana Costa | 123.456.789-00 | Ciência da Computação | 4 anos | Banco de Dados | 80h | Prof. Santos | 9.0 |

#### Tarefas para os Exercícios:
1. **Analise cada tabela** e identifique problemas de normalização
2. **Aplique a 1FN**: Elimine grupos repetitivos
3. **Aplique a 2FN**: Elimine dependências parciais
4. **Aplique a 3FN**: Elimine dependências transitivas
5. **Desenhe o diagrama** das tabelas normalizadas
6. **Identifique as chaves** primárias e estrangeiras

#### Dicas para Resolução:
1. **Identifique**: Encontre a chave primária e analise as dependências
2. **Liste**: Anote todas as dependências funcionais
3. **Separe**: Divida em tabelas menores e específicas
4. **Verifique**: Confirme que cada tabela está na 3FN

---

### Slide 07: Soluções dos Exercícios

#### Solução Exercício 1: Sistema de Biblioteca

**Problemas identificados:**
- Dependências parciais: Usuario_Nome, Usuario_Email dependem apenas de Emprestimo_ID
- Dependências parciais: Livro_Titulo, Livro_Autor, Livro_Categoria dependem apenas de Emprestimo_ID
- Dependências transitivas: Livro_Categoria depende de Livro_Titulo

**Tabelas Normalizadas (3FN):**

**USUARIOS**
| Usuario_ID | Nome | Email |
|------------|------|-------|
| 1 | João Silva | joao@email.com |
| 2 | Ana Costa | ana@email.com |

**LIVROS**
| Livro_ID | Titulo | Autor | Categoria_ID |
|----------|--------|-------|--------------|
| 1 | Python para Iniciantes | Maria Santos | 1 |
| 2 | Banco de Dados | Pedro Lima | 1 |

**CATEGORIAS**
| Categoria_ID | Nome |
|--------------|------|
| 1 | Programação |

**EMPRESTIMOS**
| Emprestimo_ID | Usuario_ID | Livro_ID | Data_Emprestimo | Data_Devolucao |
|---------------|------------|----------|-----------------|----------------|
| 1 | 1 | 1 | 2025-01-10 | 2025-01-24 |
| 2 | 2 | 1 | 2025-01-12 | 2025-01-26 |
| 3 | 1 | 2 | 2025-01-15 | 2025-01-29 |

#### Solução Exercício 2: Sistema de Vendas

**Problemas identificados:**
- Chave primária: (Venda_ID, Produto_ID)
- Dependências parciais: Cliente_Nome, Cliente_Telefone dependem apenas de Cliente_ID
- Dependências parciais: Produto_Nome, Preco_Unitario dependem apenas de Produto_ID
- Dependências parciais: Categoria_Nome depende apenas de Categoria_ID
- Dependências transitivas: Categoria_Nome depende de Produto_ID através de Categoria_ID

**Tabelas Normalizadas (3FN):**

**CLIENTES**
| Cliente_ID | Nome | Telefone |
|------------|------|----------|
| 101 | Maria Silva | (71) 99999-1111 |
| 102 | João Santos | (75) 88888-2222 |

**CATEGORIAS**
| Categoria_ID | Nome |
|--------------|------|
| 301 | Eletrônicos |

**PRODUTOS**
| Produto_ID | Nome | Categoria_ID | Preco_Unitario |
|------------|------|--------------|----------------|
| 201 | Notebook Dell | 301 | R$ 2.500 |
| 202 | Mouse Logitech | 301 | R$ 50 |

**VENDAS**
| Venda_ID | Cliente_ID | Data_Venda |
|----------|------------|------------|
| 1 | 101 | 2025-01-15 |
| 2 | 102 | 2025-01-16 |

**ITENS_VENDA**
| Venda_ID | Produto_ID | Quantidade |
|----------|------------|------------|
| 1 | 201 | 1 |
| 1 | 202 | 2 |
| 2 | 201 | 1 |

#### Benefícios Alcançados
- **Eliminação de Redundância**: Dados únicos em cada tabela
- **Integridade Garantida**: Consistência dos dados
- **Performance Otimizada**: Consultas mais eficientes
- **Manutenção Simplificada**: Alterações em um local só

---

### Slide 08: Resumo e Conclusão

#### O que Aprendemos Hoje?
Nesta aula, exploramos os conceitos fundamentais de **modelagem e normalização de dados**, essenciais para criar bancos de dados eficientes e confiáveis.

#### As Três Formas Normais

**1ª Forma Normal (1FN):**
- Valores atômicos
- Sem grupos repetitivos
- Cada célula = um valor
- Base para as outras formas

**2ª Forma Normal (2FN):**
- Já está na 1FN
- Elimina dependências parciais
- Atributos dependem da chave completa
- Reduz redundância

**3ª Forma Normal (3FN):**
- Já está na 2FN
- Elimina dependências transitivas
- Atributos dependem diretamente da chave
- Máxima normalização

#### Processo de Normalização
1. Identificar a chave primária
2. Aplicar 1FN - Eliminar grupos repetitivos
3. Aplicar 2FN - Eliminar dependências parciais
4. Aplicar 3FN - Eliminar dependências transitivas
5. Verificar integridade e performance

#### Benefícios da Normalização
- **Eliminação de Redundância**: Dados únicos e consistentes
- **Integridade dos Dados**: Consistência e confiabilidade
- **Performance Otimizada**: Consultas mais rápidas
- **Facilidade de Manutenção**: Alterações simplificadas

#### Quando NÃO Normalizar?
Em alguns casos específicos, a desnormalização pode ser necessária:
- **Data Warehouses**: Dados históricos para análise
- **Relatórios Complexos**: Quando performance é crítica
- **Cache Temporário**: Dados de sessão ou temporários
- **Sistemas Legados**: Migração gradual necessária

#### Boas Práticas
- **Sempre comece pela 1FN**: É a base para todas as outras
- **Identifique as dependências**: Mapeie todas as relações
- **Pense na performance**: Balance normalização vs velocidade
- **Documente suas decisões**: Registre o raciocínio
- **Teste com dados reais**: Valide com cenários práticos
- **Considere o futuro**: Pense em expansões

#### Conexão com Outras Aulas
Os conceitos de normalização se conectam diretamente com:
- **BEP-011**: Conceitos de banco de dados relacionais
- **BEP-012/013**: Comandos SQL (SELECT, INSERT, UPDATE, DELETE)
- **BEP-015**: Joins e consultas avançadas
- **BEP-016**: Conectando Python com banco de dados

#### Conquistas da Aula
- **Conceitos Dominados**: 1FN, 2FN, 3FN e suas aplicações
- **Habilidades Desenvolvidas**: Identificar e resolver problemas de normalização
- **Pensamento Crítico**: Analisar trade-offs entre normalização e performance
- **Próximos Passos**: Pronto para consultas avançadas e joins

#### Próxima Aula: BEP-015
Na próxima aula, vamos aprender sobre **Joins e Consultas Avançadas**, onde aplicaremos os conceitos de normalização para integrar dados de múltiplas tabelas de forma eficiente.

**Tópicos:**
- INNER JOIN, LEFT JOIN, RIGHT JOIN
- Subconsultas, ORDER BY, GROUP BY
- Foco: Integrar dados de múltiplas tabelas

#### Exercício Final
**Desafio**: Projete um sistema de e-commerce normalizado considerando:
- Clientes com endereços
- Produtos com categorias e fornecedores
- Pedidos com múltiplos itens
- Pagamentos e entregas

**Objetivo**: Aplicar todas as formas normais e justificar suas decisões de modelagem.

---

## Exercício Final Integrado

### Sistema de E-commerce Normalizado

**Desafio**: Projete um sistema completo de e-commerce aplicando todas as formas normais.

#### Requisitos:
1. **Clientes**: Nome, email, telefone, endereço completo
2. **Produtos**: Nome, descrição, preço, categoria, fornecedor
3. **Pedidos**: Cliente, data, status, valor total
4. **Itens do Pedido**: Produto, quantidade, preço unitário
5. **Pagamentos**: Forma de pagamento, status, valor
6. **Entregas**: Endereço, status, data estimada

#### Tarefas:
1. **Identifique** todas as entidades e seus atributos
2. **Aplique** a 1ª, 2ª e 3ª formas normais
3. **Crie** o diagrama das tabelas normalizadas
4. **Defina** as chaves primárias e estrangeiras
5. **Justifique** suas decisões de modelagem
6. **Considere** cenários de uso e performance

#### Entregáveis:
- Diagrama ER das tabelas normalizadas
- Script SQL para criação das tabelas
- Justificativa das decisões de normalização
- Análise de trade-offs entre normalização e performance

---

## Recursos Adicionais

### Comandos SQL para Prática
```sql
-- Criar tabelas normalizadas
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    cidade_id INT,
    FOREIGN KEY (cidade_id) REFERENCES cidades(cidade_id)
);

CREATE TABLE produtos (
    produto_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    categoria_id INT,
    fornecedor_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id),
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(fornecedor_id)
);

CREATE TABLE pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    data_pedido DATE NOT NULL,
    status ENUM('pendente', 'processando', 'enviado', 'entregue') DEFAULT 'pendente',
    valor_total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

CREATE TABLE itens_pedido (
    pedido_id INT,
    produto_id INT,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (pedido_id, produto_id),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(produto_id)
);
```

### Checklist de Normalização
- [ ] Tabela está na 1FN? (valores atômicos, sem grupos repetitivos)
- [ ] Tabela está na 2FN? (sem dependências parciais)
- [ ] Tabela está na 3FN? (sem dependências transitivas)
- [ ] Chaves primárias definidas corretamente?
- [ ] Chaves estrangeiras estabelecidas?
- [ ] Integridade referencial garantida?
- [ ] Performance considerada?
- [ ] Manutenibilidade assegurada?

### Glossário
- **Atributo**: Coluna de uma tabela
- **Chave Primária**: Campo(s) que identificam unicamente cada registro
- **Chave Estrangeira**: Campo que referencia a chave primária de outra tabela
- **Dependência Funcional**: Relação onde um atributo determina outro
- **Normalização**: Processo de organizar dados para eliminar redundância
- **Redundância**: Duplicação desnecessária de dados
- **Integridade**: Consistência e confiabilidade dos dados


