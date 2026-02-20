# BEP-015: Exercícios Práticos - Joins e Consultas Avançadas

## 📋 Exercícios Adicionais

### 🏪 Cenário: Sistema de Loja Online

**Tabela: CLIENTES**
| ID | Nome | Email | Cidade | Estado |
|----|------|-------|--------|--------|
| 1 | Ana Silva | ana@email.com | Salvador | BA |
| 2 | Bruno Santos | bruno@email.com | São Paulo | SP |
| 3 | Carla Lima | carla@email.com | Rio de Janeiro | RJ |
| 4 | Diego Costa | diego@email.com | Salvador | BA |
| 5 | Elena Souza | elena@email.com | Brasília | DF |

**Tabela: CATEGORIAS**
| ID | Nome | Descrição |
|----|------|-----------|
| 1 | Eletrônicos | Produtos eletrônicos |
| 2 | Roupas | Vestuário e acessórios |
| 3 | Livros | Livros e materiais educativos |
| 4 | Casa | Produtos para casa |

**Tabela: PRODUTOS**
| ID | Nome | Categoria_ID | Preço | Estoque |
|----|------|--------------|-------|---------|
| 1 | Smartphone | 1 | R$ 800 | 50 |
| 2 | Notebook | 1 | R$ 2000 | 20 |
| 3 | Camiseta | 2 | R$ 50 | 100 |
| 4 | Livro Python | 3 | R$ 80 | 30 |
| 5 | Mesa | 4 | R$ 300 | 15 |

**Tabela: PEDIDOS**
| ID | Cliente_ID | Data | Status | Total |
|----|------------|------|--------|-------|
| 1 | 1 | 2025-01-15 | Concluído | R$ 850 |
| 2 | 2 | 2025-01-16 | Concluído | R$ 2050 |
| 3 | 1 | 2025-01-17 | Pendente | R$ 130 |
| 4 | 3 | 2025-01-18 | Concluído | R$ 50 |
| 5 | 4 | 2025-01-19 | Concluído | R$ 300 |

**Tabela: ITENS_PEDIDO**
| ID | Pedido_ID | Produto_ID | Quantidade | Preço_Unitario |
|----|-----------|------------|------------|----------------|
| 1 | 1 | 1 | 1 | R$ 800 |
| 2 | 1 | 4 | 1 | R$ 80 |
| 3 | 2 | 2 | 1 | R$ 2000 |
| 4 | 2 | 3 | 1 | R$ 50 |
| 5 | 3 | 3 | 2 | R$ 50 |
| 6 | 3 | 4 | 1 | R$ 80 |
| 7 | 4 | 3 | 1 | R$ 50 |
| 8 | 5 | 5 | 1 | R$ 300 |

---

## 🎯 Exercícios

### Exercício 1: INNER JOIN - Clientes com Pedidos
**Objetivo:** Mostrar todos os clientes que fizeram pedidos com informações do pedido.

**Resultado esperado:**
| Nome | Email | Data Pedido | Status | Total |
|------|-------|-------------|--------|-------|
| Ana Silva | ana@email.com | 2025-01-15 | Concluído | R$ 850 |
| Bruno Santos | bruno@email.com | 2025-01-16 | Concluído | R$ 2050 |
| Ana Silva | ana@email.com | 2025-01-17 | Pendente | R$ 130 |
| Carla Lima | carla@email.com | 2025-01-18 | Concluído | R$ 50 |
| Diego Costa | diego@email.com | 2025-01-19 | Concluído | R$ 300 |

### Exercício 2: LEFT JOIN - Todos os Clientes
**Objetivo:** Mostrar todos os clientes, mesmo os que não fizeram pedidos.

**Resultado esperado:**
| Nome | Email | Data Pedido | Status | Total |
|------|-------|-------------|--------|-------|
| Ana Silva | ana@email.com | 2025-01-15 | Concluído | R$ 850 |
| Ana Silva | ana@email.com | 2025-01-17 | Pendente | R$ 130 |
| Bruno Santos | bruno@email.com | 2025-01-16 | Concluído | R$ 2050 |
| Carla Lima | carla@email.com | 2025-01-18 | Concluído | R$ 50 |
| Diego Costa | diego@email.com | 2025-01-19 | Concluído | R$ 300 |
| Elena Souza | elena@email.com | NULL | NULL | NULL |

### Exercício 3: Subconsulta - Clientes com Pedidos Acima da Média
**Objetivo:** Encontrar clientes que fizeram pedidos com valor acima da média.

**Resultado esperado:**
| Nome | Email | Total Pedido |
|------|-------|--------------|
| Bruno Santos | bruno@email.com | R$ 2050 |

### Exercício 4: GROUP BY - Vendas por Categoria
**Objetivo:** Calcular total de vendas por categoria.

**Resultado esperado:**
| Categoria | Total Vendas | Quantidade Itens |
|-----------|--------------|------------------|
| Eletrônicos | R$ 2800 | 2 |
| Roupas | R$ 200 | 4 |
| Livros | R$ 160 | 2 |
| Casa | R$ 300 | 1 |

### Exercício 5: ORDER BY - Produtos Mais Vendidos
**Objetivo:** Mostrar produtos ordenados por quantidade vendida (maior para menor).

**Resultado esperado:**
| Produto | Categoria | Quantidade Vendida | Valor Total |
|---------|-----------|-------------------|-------------|
| Camiseta | Roupas | 4 | R$ 200 |
| Smartphone | Eletrônicos | 1 | R$ 800 |
| Notebook | Eletrônicos | 1 | R$ 2000 |
| Livro Python | Livros | 2 | R$ 160 |
| Mesa | Casa | 1 | R$ 300 |

### Exercício 6: Combinado - Relatório de Vendas por Cliente
**Objetivo:** Mostrar relatório completo de vendas por cliente, ordenado por valor total.

**Resultado esperado:**
| Cliente | Cidade | Total Pedidos | Valor Total | Status |
|---------|--------|---------------|-------------|--------|
| Bruno Santos | São Paulo | 1 | R$ 2050 | Concluído |
| Ana Silva | Salvador | 2 | R$ 980 | Misto |
| Diego Costa | Salvador | 1 | R$ 300 | Concluído |
| Carla Lima | Rio de Janeiro | 1 | R$ 50 | Concluído |
| Elena Souza | Brasília | 0 | R$ 0 | Sem pedidos |

---

## 🎯 Exercícios Avançados

### Exercício 7: Múltiplos JOINs
**Objetivo:** Mostrar detalhes completos dos pedidos com informações do cliente, produtos e categorias.

**Resultado esperado:**
| Cliente | Produto | Categoria | Quantidade | Preço Unitário | Subtotal |
|---------|---------|-----------|-------------|----------------|----------|
| Ana Silva | Smartphone | Eletrônicos | 1 | R$ 800 | R$ 800 |
| Ana Silva | Livro Python | Livros | 1 | R$ 80 | R$ 80 |
| Bruno Santos | Notebook | Eletrônicos | 1 | R$ 2000 | R$ 2000 |
| Bruno Santos | Camiseta | Roupas | 1 | R$ 50 | R$ 50 |
| Ana Silva | Camiseta | Roupas | 2 | R$ 50 | R$ 100 |
| Ana Silva | Livro Python | Livros | 1 | R$ 80 | R$ 80 |
| Carla Lima | Camiseta | Roupas | 1 | R$ 50 | R$ 50 |
| Diego Costa | Mesa | Casa | 1 | R$ 300 | R$ 300 |

### Exercício 8: Subconsulta com EXISTS
**Objetivo:** Encontrar clientes que compraram produtos de uma categoria específica.

**Resultado esperado:** Clientes que compraram produtos da categoria "Eletrônicos"
| Cliente | Email | Cidade |
|---------|-------|--------|
| Ana Silva | ana@email.com | Salvador |
| Bruno Santos | bruno@email.com | São Paulo |

### Exercício 9: HAVING - Categorias com Vendas Acima de R$ 500
**Objetivo:** Encontrar categorias que tiveram vendas totais acima de R$ 500.

**Resultado esperado:**
| Categoria | Total Vendas |
|-----------|--------------|
| Eletrônicos | R$ 2800 |

### Exercício 10: CASE - Classificação de Clientes
**Objetivo:** Classificar clientes por valor total de compras.

**Resultado esperado:**
| Cliente | Valor Total | Classificação |
|---------|--------------|---------------|
| Bruno Santos | R$ 2050 | VIP |
| Ana Silva | R$ 980 | Regular |
| Diego Costa | R$ 300 | Regular |
| Carla Lima | R$ 50 | Iniciante |
| Elena Souza | R$ 0 | Sem compras |

---

## 🎯 Soluções

### Solução 1: INNER JOIN - Clientes com Pedidos
```sql
SELECT 
    c.nome,
    c.email,
    p.data as data_pedido,
    p.status,
    p.total
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id;
```

### Solução 2: LEFT JOIN - Todos os Clientes
```sql
SELECT 
    c.nome,
    c.email,
    p.data as data_pedido,
    p.status,
    p.total
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id;
```

### Solução 3: Subconsulta - Clientes com Pedidos Acima da Média
```sql
SELECT 
    c.nome,
    c.email,
    p.total
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
WHERE p.total > (
    SELECT AVG(total) 
    FROM pedidos
);
```

### Solução 4: GROUP BY - Vendas por Categoria
```sql
SELECT 
    cat.nome as categoria,
    SUM(ip.quantidade * ip.preco_unitario) as total_vendas,
    SUM(ip.quantidade) as quantidade_itens
FROM categorias cat
INNER JOIN produtos prod ON cat.id = prod.categoria_id
INNER JOIN itens_pedido ip ON prod.id = ip.produto_id
GROUP BY cat.nome;
```

### Solução 5: ORDER BY - Produtos Mais Vendidos
```sql
SELECT 
    prod.nome as produto,
    cat.nome as categoria,
    SUM(ip.quantidade) as quantidade_vendida,
    SUM(ip.quantidade * ip.preco_unitario) as valor_total
FROM produtos prod
INNER JOIN categorias cat ON prod.categoria_id = cat.id
INNER JOIN itens_pedido ip ON prod.id = ip.produto_id
GROUP BY prod.nome, cat.nome
ORDER BY quantidade_vendida DESC;
```

### Solução 6: Combinado - Relatório de Vendas por Cliente
```sql
SELECT 
    c.nome as cliente,
    c.cidade,
    COUNT(p.id) as total_pedidos,
    COALESCE(SUM(p.total), 0) as valor_total,
    CASE 
        WHEN COUNT(p.id) = 0 THEN 'Sem pedidos'
        WHEN COUNT(CASE WHEN p.status = 'Pendente' THEN 1 END) > 0 THEN 'Misto'
        ELSE 'Concluído'
    END as status
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome, c.cidade
ORDER BY valor_total DESC;
```

### Solução 7: Múltiplos JOINs
```sql
SELECT 
    c.nome as cliente,
    prod.nome as produto,
    cat.nome as categoria,
    ip.quantidade,
    ip.preco_unitario,
    (ip.quantidade * ip.preco_unitario) as subtotal
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
INNER JOIN itens_pedido ip ON p.id = ip.pedido_id
INNER JOIN produtos prod ON ip.produto_id = prod.id
INNER JOIN categorias cat ON prod.categoria_id = cat.id
ORDER BY c.nome, prod.nome;
```

### Solução 8: Subconsulta com EXISTS
```sql
SELECT 
    c.nome as cliente,
    c.email,
    c.cidade
FROM clientes c
WHERE EXISTS (
    SELECT 1 
    FROM pedidos p
    INNER JOIN itens_pedido ip ON p.id = ip.pedido_id
    INNER JOIN produtos prod ON ip.produto_id = prod.id
    INNER JOIN categorias cat ON prod.categoria_id = cat.id
    WHERE p.cliente_id = c.id 
    AND cat.nome = 'Eletrônicos'
);
```

### Solução 9: HAVING - Categorias com Vendas Acima de R$ 500
```sql
SELECT 
    cat.nome as categoria,
    SUM(ip.quantidade * ip.preco_unitario) as total_vendas
FROM categorias cat
INNER JOIN produtos prod ON cat.id = prod.categoria_id
INNER JOIN itens_pedido ip ON prod.id = ip.produto_id
GROUP BY cat.nome
HAVING SUM(ip.quantidade * ip.preco_unitario) > 500;
```

### Solução 10: CASE - Classificação de Clientes
```sql
SELECT 
    c.nome as cliente,
    COALESCE(SUM(p.total), 0) as valor_total,
    CASE 
        WHEN COALESCE(SUM(p.total), 0) >= 1000 THEN 'VIP'
        WHEN COALESCE(SUM(p.total), 0) >= 500 THEN 'Regular'
        WHEN COALESCE(SUM(p.total), 0) > 0 THEN 'Iniciante'
        ELSE 'Sem compras'
    END as classificacao
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome
ORDER BY valor_total DESC;
```

---

## 🎯 Dicas para Resolução

### 1. Analise o Problema
- Identifique quais tabelas são necessárias
- Determine o tipo de relacionamento (1:1, 1:N, N:N)
- Defina o que você quer mostrar no resultado

### 2. Escolha o JOIN Adequado
- **INNER JOIN**: Apenas registros com correspondência
- **LEFT JOIN**: Todos os registros da tabela da esquerda
- **RIGHT JOIN**: Todos os registros da tabela da direita

### 3. Use Funções de Agregação
- **COUNT()**: Contar registros
- **SUM()**: Somar valores
- **AVG()**: Calcular média
- **MAX()/MIN()**: Maior/menor valor

### 4. Ordene os Resultados
- **ORDER BY**: Organizar dados
- **GROUP BY**: Agrupar para cálculos
- **HAVING**: Filtrar grupos

### 5. Teste Suas Consultas
- Execute passo a passo
- Verifique os resultados
- Otimize a performance

---

## 🎯 Próximos Passos

1. **Pratique com dados reais** - Crie seu próprio banco de dados
2. **Explore funções avançadas** - HAVING, CASE, COALESCE
3. **Estude otimização** - Índices e EXPLAIN
4. **Aprenda sobre views** - Consultas reutilizáveis
5. **Pratique com projetos** - Aplicações reais

---

**💡 Lembre-se**: A prática é fundamental para dominar JOINs e consultas avançadas. Continue exercitando e explore diferentes cenários!
