# 📚 Exercícios Complementares - BEP-012 com UPDATE e DELETE

## 🎯 Objetivo
Completar os exercícios da BEP-012 adicionando as operações UPDATE e DELETE, formando um conjunto CRUD completo.

## 📋 Contexto dos Exercícios
Vamos usar as mesmas tabelas da BEP-012, mas agora com operações de modificação e remoção de dados.

### 🗄️ Estrutura das Tabelas

```sql
-- Tabela de clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    telefone TEXT,
    cidade TEXT,
    idade INTEGER,
    categoria TEXT DEFAULT 'Normal',
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- Tabela de produtos
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL,
    categoria TEXT,
    estoque INTEGER DEFAULT 0,
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- Tabela de pedidos
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    valor_total REAL,
    data_pedido DATE,
    status TEXT DEFAULT 'pendente',
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
```

## 📊 Dados de Exemplo

### 👥 Clientes
```sql
INSERT INTO clientes (nome, email, telefone, cidade, idade, categoria) VALUES
('João Silva', 'joao@email.com', '(71) 99999-1111', 'Salvador', 30, 'Normal'),
('Maria Santos', 'maria@email.com', '(71) 99999-2222', 'Feira de Santana', 25, 'Premium'),
('Pedro Costa', 'pedro@email.com', NULL, 'Salvador', 35, 'Normal'),
('Ana Oliveira', 'ana@email.com', '(71) 99999-4444', 'Camaçari', 28, 'VIP'),
('Carlos Lima', 'carlos@email.com', '(71) 99999-5555', 'Salvador', 22, 'Normal'),
('Lucia Ferreira', 'lucia@email.com', '(71) 99999-6666', 'Feira de Santana', 45, 'Premium'),
('Roberto Alves', 'roberto@email.com', NULL, 'Camaçari', 38, 'Normal'),
('Fernanda Souza', 'fernanda@email.com', '(71) 99999-8888', 'Salvador', 29, 'VIP');
```

### 🛍️ Produtos
```sql
INSERT INTO produtos (nome, preco, categoria, estoque) VALUES
('Notebook Dell', 2500.00, 'Informática', 10),
('Mouse Logitech', 50.00, 'Informática', 25),
('Teclado Mecânico', 120.00, 'Informática', 15),
('Monitor Samsung', 800.00, 'Informática', 8),
('Headset Gamer', 200.00, 'Informática', 12),
('Webcam HD', 150.00, 'Informática', 20),
('Tablet iPad', 1200.00, 'Informática', 5),
('Smartphone iPhone', 1800.00, 'Telefonia', 3);
```

### 🛒 Pedidos
```sql
INSERT INTO pedidos (cliente_id, produto_id, quantidade, valor_total, data_pedido, status) VALUES
(1, 1, 1, 2500.00, '2024-01-15', 'entregue'),
(2, 2, 2, 100.00, '2024-01-20', 'entregue'),
(1, 3, 1, 120.00, '2024-02-01', 'pendente'),
(3, 4, 1, 800.00, '2023-12-10', 'cancelado'),
(4, 5, 1, 200.00, '2024-01-25', 'entregue'),
(5, 6, 1, 150.00, '2024-02-05', 'pendente'),
(2, 7, 1, 1200.00, '2023-11-30', 'cancelado'),
(6, 8, 1, 1800.00, '2024-01-10', 'entregue');
```

## 🎯 Exercícios de UPDATE

### 📝 Exercício 1: Atualização Simples
**Objetivo:** Atualizar informações básicas de clientes.

1. **Atualizar telefone:**
   - Atualize o telefone do cliente "Pedro Costa" para "(71) 99999-3333"

2. **Atualizar email:**
   - Mude o email do cliente "Maria Santos" para "maria.nova@email.com"

3. **Atualizar categoria:**
   - Promova o cliente "Carlos Lima" para categoria "Premium"

### 📝 Exercício 2: Atualização em Lote
**Objetivo:** Atualizar múltiplos registros com base em condições.

1. **Por cidade:**
   - Atualize a categoria para "VIP" de todos os clientes de Salvador com mais de 25 anos

2. **Por idade:**
   - Aumente a idade de todos os clientes em 1 ano

3. **Por categoria:**
   - Mude a categoria de todos os clientes "Normal" para "Standard"

### 📝 Exercício 3: Atualização de Produtos
**Objetivo:** Gerenciar informações de produtos.

1. **Ajuste de preços:**
   - Aumente o preço de todos os produtos da categoria "Informática" em 10%

2. **Atualização de estoque:**
   - Reduza o estoque de todos os produtos em 2 unidades

3. **Reclassificação:**
   - Mude a categoria do "Smartphone iPhone" de "Telefonia" para "Informática"

### 📝 Exercício 4: Atualização de Pedidos
**Objetivo:** Gerenciar status e informações de pedidos.

1. **Atualização de status:**
   - Mude o status de todos os pedidos "pendente" para "processando"

2. **Recálculo de valores:**
   - Atualize o valor_total de todos os pedidos cancelados para 0.00

3. **Atualização de data:**
   - Mude a data de todos os pedidos de 2023 para "2024-01-01"

## 🗑️ Exercícios de DELETE

### 🗑️ Exercício 5: Remoção Segura
**Objetivo:** Remover registros com validações.

1. **Remoção por condição:**
   - Remova todos os clientes que não têm telefone (telefone IS NULL)

2. **Remoção por data:**
   - Remova todos os pedidos cancelados de 2023

3. **Remoção por valor:**
   - Remova todos os pedidos com valor_total menor que R$ 100,00

### 🗑️ Exercício 6: Remoção com Verificação de Dependências
**Objetivo:** Remover registros verificando relacionamentos.

1. **Verificar antes de remover:**
   - Identifique clientes que não têm pedidos e remova-os

2. **Remoção de produtos:**
   - Remova produtos que não têm pedidos associados

3. **Limpeza de dados antigos:**
   - Remova pedidos de 2023 que estão cancelados

### 🗑️ Exercício 7: Remoção em Lote
**Objetivo:** Remover múltiplos registros de forma controlada.

1. **Remoção por categoria:**
   - Remova todos os produtos da categoria "Telefonia"

2. **Remoção por idade:**
   - Remova clientes com mais de 50 anos (se existirem)

3. **Limpeza de estoque:**
   - Remova produtos com estoque zero

## 🔄 Exercícios de Transações

### 🔄 Exercício 8: Transação Simples
**Objetivo:** Executar operações atômicas.

1. **Transação de atualização:**
   - Crie uma transação que:
     - Atualize a categoria de todos os clientes VIP para "Premium"
     - Aumente o preço de todos os produtos em 5%
     - Se houver erro, desfaça tudo

### 🔄 Exercício 9: Transação Complexa
**Objetivo:** Operações múltiplas com validação.

1. **Transação de limpeza:**
   - Crie uma transação que:
     - Remova pedidos cancelados de 2023
     - Atualize o status de pedidos pendentes para "processando"
     - Remova clientes sem telefone
     - Se qualquer operação falhar, desfaça tudo

### 🔄 Exercício 10: Transação de Manutenção
**Objetivo:** Manutenção de dados com segurança.

1. **Transação de manutenção:**
   - Crie uma transação que:
     - Atualize a idade de todos os clientes (+1 ano)
     - Reduza o estoque de produtos vendidos
     - Atualize o status de pedidos entregues para "finalizado"
     - Valide se não há inconsistências antes de confirmar

## 🎯 Exercícios Combinados (CRUD Completo)

### 🎯 Exercício 11: Sistema de Promoção
**Objetivo:** Implementar um sistema completo de promoção.

1. **Criar promoção:**
   - Insira novos clientes VIP
   - Atualize preços de produtos com desconto de 15%
   - Crie pedidos para os novos clientes

2. **Gerenciar promoção:**
   - Atualize status dos pedidos promocionais
   - Remova produtos com estoque insuficiente
   - Finalize a promoção removendo descontos

### 🎯 Exercício 12: Limpeza de Dados
**Objetivo:** Implementar rotina de limpeza de dados.

1. **Identificar dados inconsistentes:**
   - Encontre clientes sem pedidos
   - Identifique produtos sem estoque
   - Localize pedidos órfãos

2. **Executar limpeza:**
   - Remova dados inconsistentes
   - Atualize informações desatualizadas
   - Reorganize categorias

3. **Validar resultado:**
   - Verifique integridade dos dados
   - Confirme que não há inconsistências
   - Gere relatório da limpeza

## 📋 Soluções dos Exercícios

### 🔧 Soluções UPDATE

```sql
-- Exercício 1.1: Atualizar telefone
UPDATE clientes 
SET telefone = '(71) 99999-3333' 
WHERE nome = 'Pedro Costa';

-- Exercício 1.2: Atualizar email
UPDATE clientes 
SET email = 'maria.nova@email.com' 
WHERE nome = 'Maria Santos';

-- Exercício 1.3: Atualizar categoria
UPDATE clientes 
SET categoria = 'Premium' 
WHERE nome = 'Carlos Lima';

-- Exercício 2.1: Atualização por cidade e idade
UPDATE clientes 
SET categoria = 'VIP' 
WHERE cidade = 'Salvador' AND idade > 25;

-- Exercício 2.2: Aumentar idade
UPDATE clientes 
SET idade = idade + 1;

-- Exercício 2.3: Mudar categoria
UPDATE clientes 
SET categoria = 'Standard' 
WHERE categoria = 'Normal';
```

### 🗑️ Soluções DELETE

```sql
-- Exercício 5.1: Remover clientes sem telefone
DELETE FROM clientes 
WHERE telefone IS NULL;

-- Exercício 5.2: Remover pedidos cancelados de 2023
DELETE FROM pedidos 
WHERE status = 'cancelado' AND data_pedido LIKE '2023%';

-- Exercício 5.3: Remover pedidos com valor baixo
DELETE FROM pedidos 
WHERE valor_total < 100.00;

-- Exercício 6.1: Remover clientes sem pedidos
DELETE FROM clientes 
WHERE id NOT IN (SELECT DISTINCT cliente_id FROM pedidos WHERE cliente_id IS NOT NULL);
```

### 🔄 Soluções Transações

```sql
-- Exercício 8: Transação simples
BEGIN;
UPDATE clientes SET categoria = 'Premium' WHERE categoria = 'VIP';
UPDATE produtos SET preco = preco * 1.05;
COMMIT;

-- Em caso de erro:
-- ROLLBACK;
```

## 💡 Dicas Importantes

### ✅ Boas Práticas
1. **Sempre use WHERE** em UPDATE e DELETE
2. **Teste com SELECT** antes de modificar
3. **Use transações** para operações críticas
4. **Faça backup** antes de operações em massa
5. **Valide dados** antes de confirmar transações

### ⚠️ Cuidados
1. **DELETE é irreversível** - use com extrema cautela
2. **UPDATE sem WHERE** afeta todos os registros
3. **Transações longas** podem causar bloqueios
4. **Chaves estrangeiras** podem impedir remoções
5. **Índices** podem ser afetados por operações em massa

### 🎯 Objetivos de Aprendizagem
- Dominar sintaxe de UPDATE e DELETE
- Entender importância da cláusula WHERE
- Implementar operações seguras
- Usar transações adequadamente
- Completar operações CRUD
- Aplicar boas práticas de banco de dados

## 🏆 Desafio Final

Crie um script Python que implemente um sistema completo de gerenciamento de dados com:
- Menu interativo
- Operações CRUD completas
- Validações de dados
- Tratamento de erros
- Transações seguras
- Relatórios de operações

Este sistema deve permitir ao usuário gerenciar clientes, produtos e pedidos de forma segura e eficiente.
