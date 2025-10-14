# 🛡️ Boas Práticas para UPDATE e DELETE

## 🎯 Introdução

Os comandos UPDATE e DELETE são poderosos, mas perigosos. Este guia apresenta as melhores práticas para usar esses comandos de forma segura e eficiente.

## ⚠️ Regras de Ouro

### 1. 🎯 SEMPRE use WHERE
**NUNCA execute UPDATE ou DELETE sem a cláusula WHERE!**

```sql
-- ✅ CORRETO
UPDATE clientes SET categoria = 'VIP' WHERE cidade = 'Salvador';

-- ❌ PERIGOSO - Atualiza TODOS os clientes
UPDATE clientes SET categoria = 'VIP';
```

### 2. 👀 Verifique antes de modificar
**SEMPRE teste sua condição WHERE com SELECT primeiro:**

```sql
-- 1. Verificar o que será afetado
SELECT COUNT(*) FROM clientes WHERE cidade = 'Salvador';
SELECT * FROM clientes WHERE cidade = 'Salvador';

-- 2. Se estiver correto, executar UPDATE
UPDATE clientes SET categoria = 'VIP' WHERE cidade = 'Salvador';
```

### 3. 🔒 Use transações para operações críticas
**Proteja operações importantes com transações:**

```sql
BEGIN;
UPDATE clientes SET categoria = 'Premium' WHERE idade > 30;
UPDATE produtos SET preco = preco * 1.1;
-- Verificar se tudo está correto
SELECT COUNT(*) FROM clientes WHERE categoria = 'Premium';
-- Se OK, confirmar
COMMIT;
-- Se houver problema, desfazer
-- ROLLBACK;
```

## 📋 Checklist de Segurança

### Antes de executar UPDATE/DELETE:

- [ ] **Identifique exatamente** quais registros serão afetados
- [ ] **Teste a condição WHERE** com SELECT
- [ ] **Conte os registros** que serão modificados
- [ ] **Verifique dependências** (chaves estrangeiras)
- [ ] **Faça backup** se necessário
- [ ] **Use transações** para operações críticas
- [ ] **Tenha um plano de rollback**

### Durante a execução:

- [ ] **Execute em ambiente de teste** primeiro
- [ ] **Monitore a performance** em operações grandes
- [ ] **Use LIMIT** para operações em lote
- [ ] **Valide resultados** após cada operação

### Após a execução:

- [ ] **Verifique os resultados** com SELECT
- [ ] **Confirme que não há inconsistências**
- [ ] **Documente as alterações** realizadas
- [ ] **Monitore o sistema** por possíveis problemas

## 🔧 Padrões de Código Seguro

### UPDATE Seguro

```sql
-- Padrão recomendado para UPDATE
-- 1. Verificar registros que serão afetados
SELECT id, nome, categoria 
FROM clientes 
WHERE cidade = 'Salvador' AND idade > 25;

-- 2. Contar quantos serão afetados
SELECT COUNT(*) 
FROM clientes 
WHERE cidade = 'Salvador' AND idade > 25;

-- 3. Executar UPDATE
UPDATE clientes 
SET categoria = 'VIP' 
WHERE cidade = 'Salvador' AND idade > 25;

-- 4. Verificar resultado
SELECT COUNT(*) 
FROM clientes 
WHERE categoria = 'VIP';
```

### DELETE Seguro

```sql
-- Padrão recomendado para DELETE
-- 1. Verificar registros que serão removidos
SELECT id, nome, email 
FROM clientes 
WHERE telefone IS NULL;

-- 2. Contar quantos serão removidos
SELECT COUNT(*) 
FROM clientes 
WHERE telefone IS NULL;

-- 3. Verificar dependências
SELECT COUNT(*) 
FROM pedidos 
WHERE cliente_id IN (
    SELECT id FROM clientes WHERE telefone IS NULL
);

-- 4. Se não houver dependências, executar DELETE
DELETE FROM clientes 
WHERE telefone IS NULL;

-- 5. Verificar resultado
SELECT COUNT(*) FROM clientes;
```

## 🔄 Transações Seguras

### Estrutura Básica

```sql
BEGIN;
-- Operações aqui
UPDATE tabela1 SET campo = valor WHERE condição;
DELETE FROM tabela2 WHERE condição;
-- Verificações
SELECT COUNT(*) FROM tabela1 WHERE campo = valor;
-- Se tudo OK, confirmar
COMMIT;
-- Se houver problema, desfazer
-- ROLLBACK;
```

### Exemplo Prático

```sql
-- Transação para atualizar preços e remover produtos obsoletos
BEGIN;

-- 1. Atualizar preços
UPDATE produtos 
SET preco = preco * 1.1 
WHERE categoria = 'Informática';

-- 2. Remover produtos sem estoque
DELETE FROM produtos 
WHERE estoque = 0 AND data_cadastro < '2023-01-01';

-- 3. Verificar resultados
SELECT COUNT(*) FROM produtos WHERE preco > 1000;
SELECT COUNT(*) FROM produtos WHERE estoque = 0;

-- 4. Se tudo estiver correto, confirmar
COMMIT;

-- Em caso de erro:
-- ROLLBACK;
```

## 🚀 Otimização de Performance

### Operações em Lote

```sql
-- Para grandes volumes, processe em lotes
DELETE FROM logs 
WHERE data_log < '2023-01-01' 
LIMIT 1000;

-- Repetir até não haver mais registros
-- Ou usar um loop no código da aplicação
```

### Índices e Performance

```sql
-- Criar índices para melhorar performance
CREATE INDEX idx_cliente_cidade ON clientes(cidade);
CREATE INDEX idx_pedido_data ON pedidos(data_pedido);
CREATE INDEX idx_produto_categoria ON produtos(categoria);
```

### Monitoramento

```sql
-- Verificar quantos registros serão afetados
EXPLAIN QUERY PLAN 
UPDATE clientes 
SET categoria = 'VIP' 
WHERE cidade = 'Salvador';

-- Monitorar performance
PRAGMA table_info(clientes);
PRAGMA index_list(clientes);
```

## 🛡️ Proteções Adicionais

### Validação de Dados

```sql
-- Verificar se o valor existe antes de atualizar
UPDATE clientes 
SET categoria = 'Premium' 
WHERE id = 123 
AND EXISTS (SELECT 1 FROM clientes WHERE id = 123);
```

### Verificação de Integridade

```sql
-- Verificar chaves estrangeiras antes de deletar
DELETE FROM clientes 
WHERE id = 123 
AND NOT EXISTS (
    SELECT 1 FROM pedidos WHERE cliente_id = 123
);
```

### Logs e Auditoria

```sql
-- Criar tabela de log para auditoria
CREATE TABLE log_alteracoes (
    id INTEGER PRIMARY KEY,
    tabela TEXT,
    operacao TEXT,
    registro_id INTEGER,
    dados_antigos TEXT,
    dados_novos TEXT,
    usuario TEXT,
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger para log automático (exemplo conceitual)
-- CREATE TRIGGER log_update_clientes
-- AFTER UPDATE ON clientes
-- BEGIN
--     INSERT INTO log_alteracoes (tabela, operacao, registro_id, dados_antigos, dados_novos)
--     VALUES ('clientes', 'UPDATE', NEW.id, OLD.categoria, NEW.categoria);
-- END;
```

## 🚨 Cenários de Risco

### ⚠️ Riscos Comuns

1. **UPDATE sem WHERE**
   ```sql
   -- PERIGOSO - Atualiza todos os registros
   UPDATE clientes SET categoria = 'VIP';
   ```

2. **DELETE sem WHERE**
   ```sql
   -- PERIGOSO - Remove todos os registros
   DELETE FROM clientes;
   ```

3. **WHERE incorreto**
   ```sql
   -- PERIGOSO - Condição muito ampla
   UPDATE clientes SET categoria = 'VIP' WHERE cidade = 'S'; -- Pode afetar mais que o esperado
   ```

4. **Falta de verificação de dependências**
   ```sql
   -- PERIGOSO - Pode quebrar integridade referencial
   DELETE FROM clientes WHERE id = 123; -- Se houver pedidos associados
   ```

### 🛡️ Como Evitar

1. **Sempre teste com SELECT primeiro**
2. **Use transações para operações críticas**
3. **Faça backup antes de operações importantes**
4. **Valide condições WHERE cuidadosamente**
5. **Verifique dependências antes de deletar**
6. **Use LIMIT em operações grandes**
7. **Monitore o sistema após alterações**

## 📊 Exemplos de Recuperação

### Backup e Restore

```sql
-- Fazer backup antes de operações críticas
CREATE TABLE clientes_backup AS SELECT * FROM clientes;

-- Em caso de problema, restaurar
DELETE FROM clientes;
INSERT INTO clientes SELECT * FROM clientes_backup;
```

### Rollback Manual

```sql
-- Se você souber exatamente o que foi alterado
-- Pode fazer rollback manual
UPDATE clientes 
SET categoria = 'Normal' 
WHERE categoria = 'VIP' AND cidade = 'Salvador';
```

## 🎯 Checklist Final

### Antes de executar qualquer UPDATE/DELETE:

- [ ] **Entendi exatamente** o que a operação fará?
- [ ] **Testei a condição WHERE** com SELECT?
- [ ] **Contei quantos registros** serão afetados?
- [ ] **Verifiquei dependências** e relacionamentos?
- [ ] **Fiz backup** se necessário?
- [ ] **Usei transações** para operações críticas?
- [ ] **Tenho um plano** para reverter se necessário?
- [ ] **Executei em ambiente de teste** primeiro?

### Lembre-se:

> **"É melhor ser cauteloso e verificar duas vezes do que lamentar uma vez."**

Os comandos UPDATE e DELETE são ferramentas poderosas, mas com grande poder vem grande responsabilidade. Use-os com sabedoria e sempre priorize a segurança dos dados.
