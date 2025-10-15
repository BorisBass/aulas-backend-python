# 🎯 BEP-013: Código para Google Colab

## 📚 Prática com UPDATE e DELETE

Copie e cole este código no Google Colab para praticar UPDATE e DELETE com SQLite3.

### 📦 Importações necessárias

```python
# Importações necessárias
import sqlite3
import pandas as pd
from datetime import datetime, timedelta

print("✅ Bibliotecas importadas com sucesso!")
```

### 🗄️ Configuração do Banco de Dados

```python
# Conectar ao banco de dados
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

print("✅ Conectado ao banco SQLite em memória")
```

### 🏗️ Criar Tabelas

```python
# Criar tabela de clientes
cursor.execute('''
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    telefone TEXT,
    cidade TEXT,
    idade INTEGER,
    categoria TEXT DEFAULT 'Normal',
    data_cadastro DATE DEFAULT CURRENT_DATE
)
''')

print("✅ Tabela 'clientes' criada com sucesso!")
```

```python
# Criar tabela de pedidos
cursor.execute('''
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto TEXT,
    valor REAL,
    data_pedido DATE,
    status TEXT DEFAULT 'pendente',
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
''')

print("✅ Tabela 'pedidos' criada com sucesso!")
```

### 📊 Inserir Dados de Exemplo

```python
# Inserir clientes de exemplo
clientes_exemplo = [
    (1, 'João Silva', 'joao@email.com', '(71) 99999-1111', 'Salvador', 30, 'Normal'),
    (2, 'Maria Santos', 'maria@email.com', '(71) 99999-2222', 'Feira de Santana', 25, 'Premium'),
    (3, 'Pedro Costa', 'pedro@email.com', None, 'Salvador', 35, 'Normal'),
    (4, 'Ana Oliveira', 'ana@email.com', '(71) 99999-4444', 'Camaçari', 28, 'VIP'),
    (5, 'Carlos Lima', 'carlos@email.com', '(71) 99999-5555', 'Salvador', 22, 'Normal'),
    (6, 'Lucia Ferreira', 'lucia@email.com', '(71) 99999-6666', 'Feira de Santana', 45, 'Premium'),
    (7, 'Roberto Alves', 'roberto@email.com', None, 'Camaçari', 38, 'Normal'),
    (8, 'Fernanda Souza', 'fernanda@email.com', '(71) 99999-8888', 'Salvador', 29, 'VIP')
]

cursor.executemany('INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?, ?)', clientes_exemplo)
conn.commit()

print("✅ Clientes inseridos com sucesso!")
```

```python
# Inserir pedidos de exemplo
pedidos_exemplo = [
    (1, 1, 'Notebook', 2500.00, '2024-01-15', 'entregue'),
    (2, 2, 'Mouse', 50.00, '2024-01-20', 'entregue'),
    (3, 1, 'Teclado', 120.00, '2024-02-01', 'pendente'),
    (4, 3, 'Monitor', 800.00, '2023-12-10', 'cancelado'),
    (5, 4, 'Headset', 200.00, '2024-01-25', 'entregue'),
    (6, 5, 'Webcam', 150.00, '2024-02-05', 'pendente'),
    (7, 2, 'Tablet', 1200.00, '2023-11-30', 'cancelado'),
    (8, 6, 'Smartphone', 1800.00, '2024-01-10', 'entregue')
]

cursor.executemany('INSERT INTO pedidos VALUES (?, ?, ?, ?, ?, ?)', pedidos_exemplo)
conn.commit()

print("✅ Pedidos inseridos com sucesso!")
```

### 👀 Visualizar Dados Iniciais

```python
# Visualizar todos os clientes
cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

print("👥 CLIENTES:")
print("ID | Nome | Email | Telefone | Cidade | Idade | Categoria")
print("-" * 80)
for cliente in clientes:
    print(f"{cliente[0]:2} | {cliente[1]:15} | {cliente[2]:20} | {str(cliente[3]):15} | {cliente[4]:15} | {cliente[5]:5} | {cliente[6]}")
```

```python
# Visualizar todos os pedidos
cursor.execute("SELECT * FROM pedidos")
pedidos = cursor.fetchall()

print("\n🛒 PEDIDOS:")
print("ID | Cliente_ID | Produto | Valor | Data | Status")
print("-" * 60)
for pedido in pedidos:
    print(f"{pedido[0]:2} | {pedido[1]:10} | {pedido[2]:10} | {pedido[3]:7.2f} | {pedido[4]} | {pedido[5]}")
```

## ✏️ Praticando UPDATE

### 🔧 Exemplo 1: UPDATE Simples

```python
# 1. Verificar o estado atual do cliente
cursor.execute("SELECT id, nome, telefone FROM clientes WHERE id = 3")
cliente_antes = cursor.fetchone()
print("🔍 ANTES da atualização:")
print(f"ID: {cliente_antes[0]}, Nome: {cliente_antes[1]}, Telefone: {cliente_antes[2]}")

# 2. Executar UPDATE
cursor.execute("UPDATE clientes SET telefone = '(71) 99999-3333' WHERE id = 3")
conn.commit()

# 3. Verificar o resultado
cursor.execute("SELECT id, nome, telefone FROM clientes WHERE id = 3")
cliente_depois = cursor.fetchone()
print("\n✅ DEPOIS da atualização:")
print(f"ID: {cliente_depois[0]}, Nome: {cliente_depois[1]}, Telefone: {cliente_depois[2]}")
```

### 🔧 Exemplo 2: UPDATE com Múltiplas Colunas

```python
# 1. Verificar o estado atual
cursor.execute("SELECT id, nome, categoria FROM clientes WHERE id = 5")
cliente_antes = cursor.fetchone()
print("🔍 ANTES da atualização:")
print(f"ID: {cliente_antes[0]}, Nome: {cliente_antes[1]}, Categoria: {cliente_antes[2]}")

# 2. Executar UPDATE com múltiplas colunas
cursor.execute("""
UPDATE clientes 
SET nome = 'Carlos Lima Silva', categoria = 'Premium' 
WHERE id = 5
""")
conn.commit()

# 3. Verificar o resultado
cursor.execute("SELECT id, nome, categoria FROM clientes WHERE id = 5")
cliente_depois = cursor.fetchone()
print("\n✅ DEPOIS da atualização:")
print(f"ID: {cliente_depois[0]}, Nome: {cliente_depois[1]}, Categoria: {cliente_depois[2]}")
```

### 🔧 Exemplo 3: UPDATE com Condições Múltiplas

```python
# 1. Verificar quantos clientes serão afetados
cursor.execute("SELECT COUNT(*) FROM clientes WHERE cidade = 'Salvador' AND idade > 25")
quantidade = cursor.fetchone()[0]
print(f"🔍 Clientes de Salvador com mais de 25 anos: {quantidade}")

# 2. Ver quais clientes serão atualizados
cursor.execute("SELECT id, nome, cidade, idade, categoria FROM clientes WHERE cidade = 'Salvador' AND idade > 25")
clientes_afetados = cursor.fetchall()
print("\n👥 Clientes que serão atualizados:")
for cliente in clientes_afetados:
    print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Cidade: {cliente[2]}, Idade: {cliente[3]}, Categoria atual: {cliente[4]}")

# 3. Executar UPDATE
cursor.execute("UPDATE clientes SET categoria = 'VIP' WHERE cidade = 'Salvador' AND idade > 25")
conn.commit()

# 4. Verificar resultado
cursor.execute("SELECT id, nome, categoria FROM clientes WHERE cidade = 'Salvador' AND idade > 25")
print("\n✅ RESULTADO:")
for cliente in cursor.fetchall():
    print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Nova categoria: {cliente[2]}")
```

## 🗑️ Praticando DELETE

### 🗑️ Exemplo 1: DELETE Seguro

```python
# 1. Verificar quantos pedidos serão removidos
cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status = 'cancelado' AND data_pedido LIKE '2023%'")
quantidade = cursor.fetchone()[0]
print(f"🔍 Pedidos cancelados de 2023: {quantidade}")

# 2. Ver quais pedidos serão removidos
cursor.execute("SELECT id, produto, data_pedido, status FROM pedidos WHERE status = 'cancelado' AND data_pedido LIKE '2023%'")
pedidos_remover = cursor.fetchall()
print("\n🗑️ Pedidos que serão removidos:")
for pedido in pedidos_remover:
    print(f"ID: {pedido[0]}, Produto: {pedido[1]}, Data: {pedido[2]}, Status: {pedido[3]}")

# 3. Executar DELETE
cursor.execute("DELETE FROM pedidos WHERE status = 'cancelado' AND data_pedido LIKE '2023%'")
conn.commit()

# 4. Verificar resultado
cursor.execute("SELECT COUNT(*) FROM pedidos")
total_restante = cursor.fetchone()[0]
print(f"\n✅ Pedidos restantes após remoção: {total_restante}")
```

### 🗑️ Exemplo 2: DELETE com Verificação de Dependências

```python
# 1. Verificar se o cliente Roberto Alves (ID 7) tem pedidos
cursor.execute("SELECT COUNT(*) FROM pedidos WHERE cliente_id = 7")
pedidos_cliente = cursor.fetchone()[0]
print(f"🔍 Pedidos do cliente ID 7: {pedidos_cliente}")

# 2. Se não tiver pedidos, podemos remover o cliente
if pedidos_cliente == 0:
    # Verificar dados do cliente antes de remover
    cursor.execute("SELECT id, nome, email FROM clientes WHERE id = 7")
    cliente = cursor.fetchone()
    print(f"\n🗑️ Removendo cliente: ID {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}")
    
    # Executar DELETE
    cursor.execute("DELETE FROM clientes WHERE id = 7")
    conn.commit()
    
    # Verificar se foi removido
    cursor.execute("SELECT COUNT(*) FROM clientes WHERE id = 7")
    cliente_existe = cursor.fetchone()[0]
    if cliente_existe == 0:
        print("✅ Cliente removido com sucesso!")
    else:
        print("❌ Erro ao remover cliente!")
else:
    print("⚠️ Cliente tem pedidos associados. Não pode ser removido!")
```

## 🔄 Transações Seguras

```python
# Exemplo de transação bem-sucedida
print("🔄 Iniciando transação...")

try:
    # Iniciar transação
    cursor.execute("BEGIN")
    
    # Operação 1: Atualizar idade de todos os clientes
    cursor.execute("UPDATE clientes SET idade = idade + 1")
    print("✅ Idades atualizadas")
    
    # Operação 2: Atualizar status de pedidos pendentes
    cursor.execute("UPDATE pedidos SET status = 'processando' WHERE status = 'pendente'")
    print("✅ Status dos pedidos atualizados")
    
    # Verificar se tudo está correto
    cursor.execute("SELECT COUNT(*) FROM clientes WHERE idade > 50")
    clientes_velhos = cursor.fetchone()[0]
    print(f"📊 Clientes com mais de 50 anos: {clientes_velhos}")
    
    # Se tudo estiver OK, confirmar transação
    cursor.execute("COMMIT")
    print("✅ Transação confirmada com sucesso!")
    
except Exception as e:
    # Se houver erro, desfazer tudo
    cursor.execute("ROLLBACK")
    print(f"❌ Erro: {e}")
    print("🔄 Transação desfeita - nenhuma alteração foi salva")
```

## 📊 Resultados Finais

```python
# Estado final dos clientes
cursor.execute("SELECT * FROM clientes ORDER BY id")
clientes_finais = cursor.fetchall()

print("👥 CLIENTES FINAIS:")
print("ID | Nome | Email | Telefone | Cidade | Idade | Categoria")
print("-" * 80)
for cliente in clientes_finais:
    print(f"{cliente[0]:2} | {cliente[1]:15} | {cliente[2]:20} | {str(cliente[3]):15} | {cliente[4]:15} | {cliente[5]:5} | {cliente[6]}")
```

```python
# Estado final dos pedidos
cursor.execute("SELECT * FROM pedidos ORDER BY id")
pedidos_finais = cursor.fetchall()

print("\n🛒 PEDIDOS FINAIS:")
print("ID | Cliente_ID | Produto | Valor | Data | Status")
print("-" * 60)
for pedido in pedidos_finais:
    print(f"{pedido[0]:2} | {pedido[1]:10} | {pedido[2]:10} | {pedido[3]:7.2f} | {pedido[4]} | {pedido[5]}")
```

## 🎯 Exercícios para Praticar

### 📝 Exercício 1: UPDATE
- Atualize o email do cliente "Maria Santos" para "maria.nova@email.com"
- Mude a categoria de todos os clientes de "Feira de Santana" para "Especial"

### 🗑️ Exercício 2: DELETE  
- Remova todos os pedidos com valor menor que R$ 100,00
- Remova clientes que não têm telefone (telefone IS NULL)

### 🔄 Exercício 3: Transação
- Crie uma transação que:
  1. Atualize a idade de todos os clientes VIP para +2 anos
  2. Mude o status de pedidos "processando" para "entregue"
  3. Se houver algum erro, desfaça tudo

### 💡 Dicas:
- Sempre use SELECT antes de UPDATE/DELETE para ver o que será afetado
- Use transações para operações críticas
- Teste suas queries em pequenos lotes primeiro

## 🔚 Fechar Conexão

```python
# Fechar conexão
conn.close()
print("✅ Conexão com o banco de dados fechada!")
print("\n🎉 Parabéns! Você praticou UPDATE e DELETE com segurança!")
print("📚 Lembre-se sempre das boas práticas:")
print("   • SEMPRE use WHERE em UPDATE e DELETE")
print("   • Verifique com SELECT antes de modificar")
print("   • Use transações para operações críticas")
print("   • Faça backup antes de operações importantes")
```
