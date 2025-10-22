# ACID: Propriedades Fundamentais dos Bancos de Dados

## 📋 Índice
1. [Introdução](#introdução)
2. [O que é ACID?](#o-que-é-acid)
3. [Atomicidade (A)](#atomicidade-a)
4. [Consistência (C)](#consistência-c)
5. [Isolamento (I)](#isolamento-i)
6. [Durabilidade (D)](#durabilidade-d)
7. [Exemplos Práticos](#exemplos-práticos)
8. [Níveis de Isolamento](#níveis-de-isolamento)
9. [Implementação em SGBDs](#implementação-em-sgbds)
10. [Casos de Uso](#casos-de-uso)
11. [Boas Práticas](#boas-práticas)

---

## 🎯 Introdução

**ACID** é um acrônimo que representa as quatro propriedades fundamentais que um sistema de gerenciamento de banco de dados (SGBD) deve garantir para transações confiáveis. Essas propriedades são essenciais para manter a integridade e confiabilidade dos dados, especialmente em ambientes com múltiplos usuários simultâneos.

### 🤔 Por que ACID é Importante?

Imagine um sistema bancário onde você transfere R$ 100 de uma conta para outra:

- **Sem ACID**: O dinheiro poderia "desaparecer" se houvesse falha no meio da operação
- **Com ACID**: A operação é garantida como um todo ou não acontece

---

## 🔤 O que é ACID?

**ACID** é formado pelas iniciais de quatro propriedades:

| Propriedade | Descrição | Garantia |
|-------------|-----------|----------|
| **A**tomicidade | Tudo ou nada | A transação é executada completamente ou não é executada |
| **C**onsistência | Dados válidos | O banco permanece em estado consistente |
| **I**solamento | Execução independente | Transações concorrentes não interferem entre si |
| **D**urabilidade | Persistência | Mudanças são permanentes após commit |

---

## ⚛️ Atomicidade (A)

### 📖 Definição
**Atomicidade** garante que uma transação seja tratada como uma unidade indivisível - ou todas as operações da transação são executadas com sucesso, ou nenhuma delas é executada.

### 🔍 Características
- **Tudo ou Nada**: A transação é atômica (indivisível)
- **Rollback Automático**: Se qualquer operação falhar, todas são desfeitas
- **Estado Consistente**: O banco nunca fica em estado intermediário

### 💡 Exemplo Prático: Transferência Bancária

```sql
-- Transação de transferência
BEGIN TRANSACTION;

-- 1. Debita da conta origem
UPDATE contas 
SET saldo = saldo - 100 
WHERE id = 1;

-- 2. Credita na conta destino
UPDATE contas 
SET saldo = saldo + 100 
WHERE id = 2;

-- 3. Registra a transação
INSERT INTO transacoes (origem, destino, valor, data) 
VALUES (1, 2, 100, NOW());

COMMIT; -- Confirma todas as operações
```

**Cenários:**
- ✅ **Sucesso**: Todas as 3 operações executam
- ❌ **Falha**: Se qualquer operação falhar, todas são desfeitas (ROLLBACK)

### 🚨 Exemplo de Falha

```sql
BEGIN TRANSACTION;

UPDATE contas SET saldo = saldo - 100 WHERE id = 1; -- ✅ Sucesso
UPDATE contas SET saldo = saldo + 100 WHERE id = 2; -- ✅ Sucesso
INSERT INTO transacoes VALUES (1, 2, 100, NOW());   -- ❌ ERRO: Tabela não existe

-- O SGBD automaticamente faz ROLLBACK
-- O saldo da conta 1 volta ao valor original
```

---

## 🎯 Consistência (C)

### 📖 Definição
**Consistência** garante que uma transação leve o banco de dados de um estado válido para outro estado válido, respeitando todas as regras de integridade definidas.

### 🔍 Características
- **Regras de Negócio**: Todas as constraints são respeitadas
- **Integridade Referencial**: Chaves estrangeiras válidas
- **Validações**: Dados dentro dos domínios permitidos
- **Estado Válido**: O banco sempre permanece consistente

### 💡 Exemplo Prático: Sistema de Vendas

```sql
-- Regras de consistência:
-- 1. Saldo não pode ser negativo
-- 2. Quantidade em estoque não pode ser negativa
-- 3. Preço deve ser positivo

BEGIN TRANSACTION;

-- Venda de produto
UPDATE produtos 
SET estoque = estoque - 5 
WHERE id = 1 AND estoque >= 5; -- Verifica consistência

-- Se estoque < 5, a operação falha e a transação é desfeita
INSERT INTO vendas (produto_id, quantidade, preco) 
VALUES (1, 5, 50.00);

COMMIT;
```

### 🚨 Exemplo de Violação de Consistência

```sql
-- Tentativa de vender mais do que tem em estoque
BEGIN TRANSACTION;

UPDATE produtos 
SET estoque = estoque - 10  -- Estoque atual: 3
WHERE id = 1;               -- Resultado: estoque = -7 ❌

-- O SGBD detecta a violação e faz ROLLBACK
-- Mantém a consistência (estoque não pode ser negativo)
```

---

## 🔒 Isolamento (I)

### 📖 Definição
**Isolamento** garante que transações concorrentes (simultâneas) não interfiram entre si, como se fossem executadas sequencialmente.

### 🔍 Características
- **Execução Independente**: Transações não se "veem" mutuamente
- **Dados Intermediários**: Mudanças não commitadas são invisíveis
- **Níveis de Isolamento**: Diferentes graus de isolamento disponíveis
- **Concorrência Segura**: Múltiplos usuários podem trabalhar simultaneamente

### 💡 Exemplo Prático: Reserva de Assentos

```sql
-- Usuário A e B tentam reservar o mesmo assento simultaneamente

-- Transação A
BEGIN TRANSACTION;
SELECT * FROM assentos WHERE id = 1 AND status = 'disponivel';
-- Assento disponível ✅

-- Transação B (executando simultaneamente)
BEGIN TRANSACTION;
SELECT * FROM assentos WHERE id = 1 AND status = 'disponivel';
-- Também vê disponível ✅

-- Transação A
UPDATE assentos SET status = 'reservado', usuario = 'A' WHERE id = 1;
COMMIT; -- ✅ Sucesso

-- Transação B
UPDATE assentos SET status = 'reservado', usuario = 'B' WHERE id = 1;
-- ❌ Falha: Assento já foi reservado por A
-- ROLLBACK automático
```

### 🔄 Problemas de Concorrência

| Problema | Descrição | Exemplo |
|----------|-----------|---------|
| **Dirty Read** | Lê dados não commitados | Lê saldo antes do commit |
| **Non-Repeatable Read** | Dados mudam entre leituras | Saldo diferente em duas consultas |
| **Phantom Read** | Novos registros aparecem | Novos pedidos entre consultas |
| **Lost Update** | Atualizações são perdidas | Dois usuários editam simultaneamente |

---

## 💾 Durabilidade (D)

### 📖 Definição
**Durabilidade** garante que uma vez que uma transação foi commitada, suas mudanças são permanentes e sobrevivem a falhas do sistema.

### 🔍 Características
- **Persistência**: Dados são salvos em armazenamento permanente
- **Recuperação**: Dados são recuperáveis após falhas
- **Log de Transações**: Registro de todas as operações
- **Backup e Restore**: Capacidade de restaurar dados

### 💡 Exemplo Prático: Sistema de Logs

```sql
-- Transação commitada
BEGIN TRANSACTION;

INSERT INTO logs (usuario, acao, timestamp) 
VALUES ('admin', 'login', NOW());

UPDATE usuarios 
SET ultimo_login = NOW() 
WHERE id = 1;

COMMIT; -- ✅ Dados são persistidos permanentemente
```

**Cenários de Falha:**
- ⚡ **Falha de Energia**: Dados permanecem após reinicialização
- 💥 **Crash do Sistema**: Log de transações permite recuperação
- 🔧 **Falha de Hardware**: Backup permite restauração

### 🛡️ Mecanismos de Durabilidade

```sql
-- 1. Write-Ahead Logging (WAL)
-- Log é escrito antes dos dados

-- 2. Checkpoint
-- Periódicamente, dados são sincronizados

-- 3. Redo Log
-- Registra operações para reexecução

-- 4. Undo Log
-- Registra operações para desfazer
```

---

## 🎯 Exemplos Práticos

### 🏦 Sistema Bancário

```sql
-- Transferência com todas as propriedades ACID
BEGIN TRANSACTION;

-- Atomicidade: Todas as operações ou nenhuma
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;

-- Consistência: Verifica regras de negócio
IF (SELECT saldo FROM contas WHERE id = 1) < 0 THEN
    ROLLBACK; -- Saldo não pode ser negativo
END IF;

-- Isolamento: Outras transações não veem mudanças intermediárias
-- Durabilidade: Após COMMIT, mudanças são permanentes

COMMIT;
```

### 🛒 E-commerce

```sql
-- Processamento de pedido
BEGIN TRANSACTION;

-- 1. Verifica estoque (Consistência)
SELECT estoque FROM produtos WHERE id = 1;
IF estoque < quantidade THEN
    ROLLBACK; -- Estoque insuficiente
END IF;

-- 2. Atualiza estoque (Atomicidade)
UPDATE produtos SET estoque = estoque - quantidade WHERE id = 1;

-- 3. Cria pedido
INSERT INTO pedidos (cliente_id, produto_id, quantidade, valor) 
VALUES (1, 1, quantidade, preco);

-- 4. Processa pagamento
INSERT INTO pagamentos (pedido_id, valor, status) 
VALUES (LAST_INSERT_ID(), preco, 'processando');

COMMIT; -- Durabilidade: Pedido é persistido permanentemente
```

---

## 📊 Níveis de Isolamento

### 🔍 Visão Geral

| Nível | Dirty Read | Non-Repeatable Read | Phantom Read | Performance |
|-------|------------|-------------------|--------------|-------------|
| **READ UNCOMMITTED** | ❌ Permite | ❌ Permite | ❌ Permite | 🚀 Mais Rápido |
| **READ COMMITTED** | ✅ Previne | ❌ Permite | ❌ Permite | ⚡ Rápido |
| **REPEATABLE READ** | ✅ Previne | ✅ Previne | ❌ Permite | 🐌 Médio |
| **SERIALIZABLE** | ✅ Previne | ✅ Previne | ✅ Previne | 🐌 Mais Lento |

### 💻 Exemplos de Uso

```sql
-- READ UNCOMMITTED (Menos restritivo)
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
-- Usado para relatórios que não precisam de precisão absoluta

-- READ COMMITTED (Padrão na maioria dos SGBDs)
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- Usado para operações normais de leitura

-- REPEATABLE READ
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- Usado quando precisa de leituras consistentes

-- SERIALIZABLE (Mais restritivo)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
-- Usado para operações críticas que não podem ter interferência
```

### 🎯 Escolha do Nível de Isolamento

```sql
-- Sistema de Reservas (Crítico)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
-- Reserva de assentos, quartos, etc.
COMMIT;

-- Sistema de Relatórios (Não crítico)
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
-- Relatórios estatísticos, dashboards
```

---

## 🗄️ Implementação em SGBDs

### 🐘 PostgreSQL

```sql
-- Configuração de transações
BEGIN;
-- ou
START TRANSACTION;

-- Configuração de isolamento
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Operações
INSERT INTO tabela VALUES (...);
UPDATE tabela SET ...;

-- Finalização
COMMIT;
-- ou
ROLLBACK;
```

### 🐬 MySQL

```sql
-- Configuração de transações
START TRANSACTION;

-- Configuração de isolamento
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Operações
INSERT INTO tabela VALUES (...);
UPDATE tabela SET ...;

-- Finalização
COMMIT;
-- ou
ROLLBACK;
```

### 🏢 SQL Server

```sql
-- Configuração de transações
BEGIN TRANSACTION;

-- Configuração de isolamento
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Operações
INSERT INTO tabela VALUES (...);
UPDATE tabela SET ...;

-- Finalização
COMMIT TRANSACTION;
-- ou
ROLLBACK TRANSACTION;
```

### 🐧 SQLite

```sql
-- SQLite usa transações automáticas
-- Cada comando é uma transação implícita

-- Transação explícita
BEGIN TRANSACTION;

-- Operações
INSERT INTO tabela VALUES (...);
UPDATE tabela SET ...;

-- Finalização
COMMIT;
-- ou
ROLLBACK;
```

---

## 🎯 Casos de Uso

### 🏦 **Sistema Bancário**
- **Transferências**: Atomicidade e Consistência críticas
- **Saldo**: Isolamento para evitar leituras inconsistentes
- **Auditoria**: Durabilidade para rastreamento permanente

### 🛒 **E-commerce**
- **Pedidos**: Atomicidade para não perder vendas
- **Estoque**: Consistência para não vender mais do que tem
- **Pagamentos**: Isolamento para evitar cobrança dupla

### 🎫 **Sistema de Reservas**
- **Assentos**: Isolamento para não vender o mesmo assento
- **Disponibilidade**: Consistência para manter dados corretos
- **Confirmação**: Durabilidade para manter reservas

### 📊 **Sistema de Relatórios**
- **Estatísticas**: Isolamento para dados consistentes
- **Agregações**: Consistência para cálculos corretos
- **Histórico**: Durabilidade para manter histórico

---

## ✅ Boas Práticas

### 🔧 **Design de Transações**

```sql
-- ✅ BOM: Transações curtas
BEGIN TRANSACTION;
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;

-- ❌ RUIM: Transação longa
BEGIN TRANSACTION;
-- Muitas operações...
-- Processamento pesado...
-- Consultas complexas...
COMMIT; -- Bloqueia recursos por muito tempo
```

### 🎯 **Tratamento de Erros**

```sql
-- ✅ BOM: Tratamento adequado
BEGIN TRANSACTION;
BEGIN TRY
    UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
    UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
    COMMIT;
END TRY
BEGIN CATCH
    ROLLBACK;
    -- Log do erro
    -- Notificação ao usuário
END CATCH;
```

### 🔒 **Níveis de Isolamento**

```sql
-- ✅ BOM: Usar o nível mínimo necessário
-- Para relatórios simples
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Para operações críticas
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

### 📝 **Logging e Auditoria**

```sql
-- ✅ BOM: Registrar operações importantes
BEGIN TRANSACTION;

-- Operação principal
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;

-- Log da operação
INSERT INTO auditoria (usuario, operacao, timestamp, detalhes)
VALUES ('admin', 'transferencia', NOW(), 'Conta 1: -100');

COMMIT;
```

### 🚀 **Performance**

```sql
-- ✅ BOM: Preparar dados antes da transação
-- Preparar dados fora da transação
SET @valor = 100;
SET @conta_origem = 1;
SET @conta_destino = 2;

-- Transação rápida
BEGIN TRANSACTION;
UPDATE contas SET saldo = saldo - @valor WHERE id = @conta_origem;
UPDATE contas SET saldo = saldo + @valor WHERE id = @conta_destino;
COMMIT;
```

---

## 🎓 Resumo

### 🔑 **Pontos Chave**

1. **ACID** são propriedades fundamentais para transações confiáveis
2. **Atomicidade**: Tudo ou nada
3. **Consistência**: Dados sempre válidos
4. **Isolamento**: Transações independentes
5. **Durabilidade**: Mudanças permanentes

### 🎯 **Benefícios**

- ✅ **Confiabilidade**: Dados sempre consistentes
- ✅ **Integridade**: Regras de negócio respeitadas
- ✅ **Concorrência**: Múltiplos usuários simultâneos
- ✅ **Recuperação**: Dados preservados após falhas

### 🚀 **Aplicação Prática**

- 🏦 **Sistemas Críticos**: Bancos, e-commerce, reservas
- 📊 **Aplicações Corporativas**: ERP, CRM, sistemas de gestão
- 🌐 **Aplicações Web**: Qualquer sistema com dados importantes
- 📱 **Aplicações Mobile**: Sincronização e consistência de dados

---

## 📚 Recursos Adicionais

### 📖 **Leitura Recomendada**
- Documentação oficial do seu SGBD
- "Database System Concepts" - Silberschatz
- "Fundamentals of Database Systems" - Elmasri & Navathe

### 🛠️ **Ferramentas**
- **PostgreSQL**: `pg_stat_statements` para monitoramento
- **MySQL**: `performance_schema` para análise
- **SQL Server**: `sys.dm_tran_active_transactions`

### 🎯 **Próximos Passos**
- Estude locks e deadlocks
- Aprenda sobre transações distribuídas
- Explore padrões de concorrência
- Pratique com cenários reais

---

**💡 Lembre-se**: ACID não é apenas teoria - é a base para sistemas de dados confiáveis e robustos. Domine esses conceitos para construir aplicações que seus usuários podem confiar!
