"""
EXEMPLO PRÁTICO: Cursor vs Cursor + Connection

Demonstra a diferença entre operações de leitura e escrita
"""

import sqlite3

print("=" * 60)
print("EXEMPLO: Cursor vs Cursor + Connection")
print("=" * 60)

# Criar conexão de exemplo
conn = sqlite3.connect(':memory:')  # Banco em memória (temporário)
cursor = conn.cursor()

# Criar tabela de exemplo
cursor.execute('''
    CREATE TABLE alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT
    )
''')
conn.commit()

print("\n1. OPERAÇÃO DE LEITURA (SELECT)")
print("-" * 60)

def listar_alunos(cursor):
    """
    ✅ CORRETO: Só precisa do cursor
    Por quê? Só lê dados, não altera nada
    """
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    return alunos

# Testar
print("Função: listar_alunos(cursor)")
print("Parâmetro: cursor apenas")
print("SQL: SELECT (só leitura)")
print("Precisa commit? NÃO")
print("✅ Resultado: listar_alunos(cursor)")

print("\n2. OPERAÇÃO DE ESCRITA (INSERT)")
print("-" * 60)

def cadastrar_aluno(cursor, conn):
    """
    ✅ CORRETO: Precisa cursor + conn
    Por quê? Altera dados, precisa fazer commit()
    """
    cursor.execute("INSERT INTO alunos (nome) VALUES (?)", ("João",))
    conn.commit()  # ← ESSENCIAL para salvar!
    return "Aluno cadastrado"

# Testar
print("Função: cadastrar_aluno(cursor, conn)")
print("Parâmetros: cursor + conn")
print("SQL: INSERT (altera dados)")
print("Precisa commit? SIM")
print("✅ Resultado: cadastrar_aluno(cursor, conn)")

print("\n3. O QUE ACONTECE SEM COMMIT?")
print("-" * 60)

def cadastrar_aluno_ERRADO(cursor):
    """
    ❌ ERRADO: Esqueceu o conn!
    Resultado: Dados não são salvos
    """
    cursor.execute("INSERT INTO alunos (nome) VALUES (?)", ("Maria",))
    # Falta conn.commit()!
    # Os dados ficam em memória mas não são salvos!

print("Função: cadastrar_aluno_ERRADO(cursor)")
print("Problema: Falta conn.commit()")
print("Resultado: Dados não são salvos permanentemente")
print("❌ ERRO: Dados serão perdidos!")

print("\n4. COMPARAÇÃO VISUAL")
print("-" * 60)

print("""
LEITURA (SELECT):
   cursor.execute("SELECT ...")
   → Não altera banco
   → Não precisa salvar
   → Só precisa cursor
   
ESCRITA (INSERT/UPDATE/DELETE):
   cursor.execute("INSERT ...")
   conn.commit()  ← Obrigatório!
   → Altera banco
   → Precisa salvar
   → Precisa cursor + conn
""")

print("\n5. TABELA DE REFERÊNCIA")
print("-" * 60)

tabela = [
    ("SELECT", "listar_alunos", "cursor", "Não altera"),
    ("SELECT", "buscar_aluno", "cursor", "Não altera"),
    ("INSERT", "cadastrar_aluno", "cursor + conn", "Precisa commit()"),
    ("UPDATE", "atualizar_aluno", "cursor + conn", "Precisa commit()"),
    ("DELETE", "remover_aluno", "cursor + conn", "Precisa commit()"),
]

print(f"{'SQL':<10} {'Função':<20} {'Parâmetros':<20} {'Motivo'}")
print("-" * 70)
for sql, funcao, params, motivo in tabela:
    print(f"{sql:<10} {funcao:<20} {params:<20} {motivo}")

print("\n6. REGRA DE OURO")
print("-" * 60)
print("""
🔍 Se a função faz SELECT:
   → Só precisa cursor
   
✏️ Se a função faz INSERT/UPDATE/DELETE:
   → Precisa cursor + conn
   → Precisa fazer conn.commit()
""")

print("\n7. TESTE PRÁTICO")
print("-" * 60)

# Teste 1: Leitura
print("Teste 1: Leitura (só cursor)")
alunos = listar_alunos(cursor)
print(f"   Resultado: {len(alunos)} aluno(s) encontrado(s)")
print("   ✅ Funcionou sem conn!")

# Teste 2: Escrita correta
print("\nTeste 2: Escrita correta (cursor + conn)")
resultado = cadastrar_aluno(cursor, conn)
print(f"   Resultado: {resultado}")
alunos = listar_alunos(cursor)
print(f"   Alunos no banco: {len(alunos)}")
print("   ✅ Funcionou com commit()!")

# Teste 3: Escrita errada
print("\nTeste 3: Escrita SEM commit (simulado)")
print("   cursor.execute('INSERT ...')")
print("   # Falta conn.commit()")
print("   ❌ Dados não são salvos!")

conn.close()

print("\n" + "=" * 60)
print("CONCLUSÃO")
print("=" * 60)
print("""
✅ LEITURA (SELECT):
   - Só precisa cursor
   - Não precisa commit()
   
✅ ESCRITA (INSERT/UPDATE/DELETE):
   - Precisa cursor + conn
   - OBRIGATÓRIO fazer commit()
   - Sem commit(), dados não são salvos!
""")









